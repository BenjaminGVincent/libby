# Methods

## Targetable-feature scope (cross-cutting rule)

Libby's **ranking** is a targetable-feature ranker. The case slug commits to a
specific molecular feature (or features) named in
`profile.json::targetable_features[]` — e.g. *DLL3 RNA expression*, *EGFR
L858R*, *MET exon-14 skipping*. The ranking surfaces — the trial table,
the clinical-evidence dossier, the preclinical dossier, the board positions,
the PI ranking, the executive summary, the plain-language page, and the PDF
report — are scoped to drugs whose mechanism plausibly targets one of those
features.

A drug is **in scope for the ranking** if its mechanism binds, modulates, or
acts via the named feature. It is **out of scope for the ranking** if it does
not, even when it has RCT-grade evidence in the patient's tumor type.

The contract is enforced at every agent boundary:

- `trial_screener` only logs trials whose drug targets the feature (including a
  drug approved for the tumor type whose eligibility hinges on an alteration the
  patient lacks — that is the `standard_of_care_screener`'s, not the dossier's).
- `clinician` only compiles clinical evidence for feature-targeting drugs.
- `researcher` only logs preclinical evidence for feature-targeting drugs.
- The 5 board personas only reason over the in-scope dossier.
- `PI` produces **the ranked table** (`recommendations.jsonl`): every therapy with
  any evidence behind it, tiered (top-tier ranked + non-top-tier flagged via
  `surfaced_reason`), with `access_route` marking standard care vs trial-only vs
  off-label. Nothing is routed out of it.
- `translator` and `reporter` carry the ranked table into the patient and PDF
  surfaces.

### One ranked table, with a detail surface beside it

The ranked table is the case's most important output, and a therapy that is not
in it is effectively invisible to a reader. So **every therapy with any evidence
gets a ranked row** — approved and investigational, feature-targeting and not.
Chemotherapy, surgery, radiotherapy and palliative care are ranked alongside
trial drugs.

- **The ranked table** (`PI` → `recommendations.jsonl`): all of it. `access_route`
  (from `accessibility.jsonl::access_status`) carries standard care /
  off-label / trial-only / compassionate / expanded-access / not-yet-accessible /
  unavailable. `surfaced_reason` (`unavailable` / `consolidated` / `thin_evidence` /
  `not_enrollable`) demotes a row *within* the table; it never removes it.
- **The Standard-of-care page** (`standard_of_care_screener` →
  `standard_of_care.jsonl`): a **detail surface**, not a destination. It holds what
  a ranked row cannot — regulatory and label language, guideline carriage with
  versions, eligibility and blocking factors, prior exposure, and sequencing
  trade-offs. Every option on it must also have a ranked row.

`check_pipeline.py` fails a case when a standard-of-care option has no ranked
row. The check is opt-in via the presence of `access_route`, so cases ranked
before this change remain valid under the contract they were built under.

**This supersedes the earlier two-table split by regulatory maturity**, under
which an approved option — including one the board ranked first — was routed out
of the ranking onto the standard-of-care page. That rule met its stated goal of
keeping the ranking from becoming a generic oncology recommender, but it cost
more than it saved: in a treatment-naive case the board's strongest agreement
could have no row in the main table, and its absence read as a judgement rather
than a filing decision. Scope is now carried by `access_route` and
`surfaced_reason` on a row, rather than by whether the row exists.

The one sanctioned bridge is `standard_of_care.jsonl::relationship_to_targeted_options`,
and it runs one way: it names sequencing and conflicts (a regimen that would
exhaust eligibility for a trial, a line the two tracks both want) without
ranking either against the other.

A negative biomarker test no longer empties the table. Under the earlier
feature-scoped contract, a negative result on the gating test left the case with
no within-scope recommendations, and the caveat said so. Now the conditional
rows are foreclosed but the rest of the ranking stands — the standard-of-care
rows and anything not gated on that biomarker — so the cross-cutting caveat
names what survives rather than sending the reader elsewhere. Saying "nothing
is left" should be rare, and true when said.

## Question-scoped runs (parallel entry point)

The pipeline above answers one question: *which feature-targeting options exist
for this patient?* A **question run** answers a different one, using the same
research tier and the same tumor board, scoped to a single question instead of a
target set.

The scope spine changes. In a standard case it is
`profile.json::targetable_features[]`, and the cross-cutting rule above binds
every agent to it. In a question run it is **`question.json`**, authored by
`question_framer`: the question, its decision context, explicit `in_scope` and
`out_of_scope` boundaries, and `acceptance_criteria` — what evidence would
answer it, each way, **written before the search runs**. Downstream agents that
ask "is this in scope" check there instead.

A question run may be **linked** (`source_case_slug` set) or **standalone**
(null). A linked question inherits the source case's `profile.json` **in place** — no
copy is made into the question tree, so no PHI-derived data is duplicated — and
may cite that case's dossier rather than re-researching settled ground. It still
gets its own slug and its own page, so a published case is never mutated by a
later question. A standalone question has no patient, no `profile.json`,
and no PHI surface.

### What is and is not relaxed

**Not relaxed: the board.** Five personas, two rounds, same as a full case. That
rigour is what a question run buys; a question answered without it is a
literature search wearing a case report's clothes.

**Relaxed: the artifacts that presuppose a target set.** `target_validation.jsonl`
and `accessibility.jsonl` become informational — a prognostic or mechanistic
question may have no assay to harden and no intervention to price.
`recommendations.jsonl` is required only when the answer is option-shaped.

### The terminal artifact is an answer, not a ranking

`question_synthesist` writes **`question_answer.json`**: a verdict from a fixed
set, a confidence calibrated to the evidence rather than to how strongly the
board argued, the evidence each way with its `population_match` stated, the
board's preserved dissent, what would change the answer, and a required
`scope_caveat`.

Two guards matter more than the rest:

- **`acceptance_criteria_result` must report every pre-registered criterion, in
  order.** This is the audit trail proving the answer was not assembled backwards
  from a conclusion. `check_pipeline` and `build_question.py` both enforce it.
- **`insufficient_evidence` is a first-class verdict.** Dressing it up as a
  qualified yes misleads by the shape of the answer rather than its content, so
  the renderer deliberately gives it no positive badge colour.

The synthesist may **downgrade** the framer's `answer_shape` and may never
upgrade it. An unnecessary ranked table is worse than an absent one: a ranking
implies a completeness the run does not have, because a question run screened
one question and not the therapeutic landscape.

### Order

```
question_framer → [trial_screener, clinician, researcher] → 5 personas × 2 rounds
  → question_synthesist → question_reporter
```

`check_pipeline.py` branches on the presence of `question.json`.

## Pipeline

Libby is invoked one case at a time. A "case" is one patient (or one
consultation) tied to a kebab-case slug. Each case runs through 11 agent steps
and 4 deterministic build scripts.

### 1. Intake (PHI-bearing)

```
mkdir -p case/<slug>/clinical
cp /path/to/patient/notes/* case/<slug>/clinical/
/intake <slug>
```

The `intake` agent reads `case/<slug>/clinical/*` and asks the user clarifying
questions. It writes `case/<slug>/derived/{profile,preferences}.json` — both
files **scrubbed**: age band not birthdate, region not ZIP, biomarker values, no
patient or clinician names, no day-precision dates.

`case/` is gitignored. Nothing under it ever enters version control.

### 2. Promote

```
python3 scripts/promote_profile.py <slug>
```

The promotion script validates `derived/profile.json` and `preferences.json`
against the JSON schemas in `scripts/schema/`, runs the PHI scanner against
both files, and (only if both pass) copies them to `data/cases/<slug>/`. This is
the **only path** PHI-derived data takes into the committable tree.

### 2a. Biomarker survey

```
/preclinical_biomarker_surveyor <slug>   # data/cases/<slug>/biomarker_survey.jsonl
/biomarker_reporter             <slug>   # docs/cases/<slug>/biomarker_survey.md + HTML + PDF
```

Every other research-tier agent reasons forward from the features the case
already claims are targetable. The surveyor runs the opposite direction: it
screens the case record against two fixed panels and reports what was never
measured.

- `data/reference/selected_biomarker_panel.json` — 72 cell-surface and
  HLA-presented protein targets with their binder programs, machine-generated
  from `selected_biomarker_target_list.xlsx` by
  `scripts/import_biomarker_panel.py`.
- `data/reference/tumor_agnostic_biomarkers.json` — 9 hand-curated predictive
  biomarkers that are tumor-agnostic (MSI-H/dMMR, TMB-H, NTRK fusion, RET
  fusion, BRAF V600E, HER2 IHC 3+) or relevant across a tumor subset (PD-L1,
  HRD/BRCA, HLA class I genotype).

Each in-scope biomarker gets a `measurement_status`: `measured_hardened`,
`measured_not_hardened`, `not_measured`, `not_assessable`, or `indeterminate`.
The distinction that carries the whole track is between *tested and negative*
and *never tested*: a biomarker absent from `profile.json::biomarkers[]` is
`not_measured`, never negative.

All 9 tumor-agnostic entries are surveyed in every case regardless of tumor
type — that is the point of the track, and `build_biomarker_survey.py` refuses
to render a page that is missing one. Protein targets with no plausible
connection to the tumor get no row, and the renderer derives the out-of-scope
list by subtracting the emitted rows from the panel, so the audit trail stays
complete without padding the report.

`measured_not_hardened` rows carry `handoff_to_target_validator: true` and are
worked into the Target validation paths report (below) rather than this one.

### 3. Target validation

```
/target_validator <slug>   # data/cases/<slug>/target_validation.jsonl
```

For each `profile.json::targetable_features[]` entry, the validator surfaces
the additional biomarkers, orthogonal assays, resistance markers, and
functional studies that would harden the target call. Rows are tagged with
a `priority` (essential / high / medium / low) and a `decision_relevance`
(gates_intervention / confirms_target_call / refines_target_subtype /
informs_resistance / informs_prognosis / informs_microenvironment /
informs_germline_implications). The PI uses `priority: "essential"` +
`decision_relevance: "gates_intervention"` rows to compute the rank-1
shared workup row in `recommendations.jsonl` — the canonical example is
*DLL3 RNA → DLL3 IHC SP347* in the osteosarcoma case, where the IHC gates
every DLL3-directed therapy regardless of which specific drug is chosen.

The validator also absorbs the biomarker survey's handoffs. Each row it writes
to close one carries `source_survey_id` pointing back at the survey row, and
`build_target_validation.py` renders a "Measured, but not to decision
resolution" table that flags any handoff with no matching row as **not yet
addressed** — so a gap that was found and then dropped is visible on the
published page instead of lost between two reports.

### 4. Research tier

```
/trial_screener <slug>     # data/cases/<slug>/trials.jsonl
/clinician      <slug>     # data/cases/<slug>/clinical_evidence.jsonl
/researcher     <slug>     # data/cases/<slug>/preclinical_evidence.jsonl
```

Each agent reads only `data/cases/<slug>/{profile,preferences}.json`,
`target_validation.jsonl` (when present), and the prior agent's output.
They never read `case/<slug>/clinical/` directly.

### 4a. Standard of care screen

```
/standard_of_care_screener <slug>   # data/cases/<slug>/standard_of_care.jsonl
                                    # + standard_of_care_report.md
                                    # + docs/cases/<slug>/standard_of_care.md + HTML + PDF
```

The research tier reasons forward from the case's stated targetable features.
This track answers the question none of those agents will: what is the
established treatment for someone in this situation, and does this patient
still have it available? An option earns a row only if a regulator approved it
for a population that includes this patient, or a major academic or
clinical-society guideline (NCCN, ESMO, ASCO, ASH, EHA, ASTRO, SITC and peers)
carries it. Standard of care is not only drugs: surgery, radiotherapy,
locoregional therapy, transplant, and active surveillance get rows in the
settings where guidelines carry them.

The track is **additive only** and does not feed the board or the PI. It runs
any time after `promote_profile.py`, but the useful slot is after `/PI`,
because that is when `relationship_to_targeted_options` can name the ranked
interventions a standard option would sequence against or foreclose.

Three judgments carry the track, and the renderer's pre-flight enforces each:

- **`endorsements[].population_match`** — whether the approval or guideline
  entry was written for *this* patient's situation or for a different stage,
  line, or biomarker subgroup. A `consider_now` row whose endorsements are all
  `different_population` or `unclear` is an extrapolation, not standard of
  care, and blocks the build.
- **`eligibility_status`** — judged against `profile.json` alone. The gap
  between a textbook option and a real one is usually `prior_therapies[]`. An
  `already_received` row requires a `prior_exposure_note` recording what was
  given, the best response, and why it stopped; re-offering a regimen the
  patient already progressed on is the worst error this page can make.
- **`consideration_status`** — an option behind an unmet, unmeasured, or
  pending biomarker gate is `requires_further_workup`, never `consider_now`.
  Same discipline the targeted track applies to biomarker-confirmation gating.
  Where the gate is one the biomarker survey already logged, `linked_survey_id`
  joins the two reports instead of duplicating the gap.

`last_verified_utc` is required on every row and means what it says. NCCN
versions several times a year; a row verified more than six months ago renders
with a re-check marker.

### 5. Tumor board — round 1 (positions)

```
/risktaker     <slug> --round 1
/conservative  <slug> --round 1
/critic        <slug> --round 1
/concensusite  <slug> --round 1
/advocate      <slug> --round 1
```

Each persona reads the research dossier and appends one row to
`data/cases/<slug>/board/positions.jsonl` — 3–5 ranked picks with rationale,
evidence citations, primary concerns, and confidence. Order is independent.

The five personas deliberate from the assembled dossier. One asymmetry is
intentional: `concensusite` (the guidelines persona) alone has `WebSearch` /
`WebFetch`, because professional guidelines (NCCN/ESMO/ASCO) update faster than
the indexed literature the dossier was built from. The other four personas have
no web access by design — this is not tool-config drift.

Canonical on-disk layout: board output lives only in
`data/cases/<slug>/board/{positions,critiques}.jsonl` (the merged files the
renderers read). Per-persona split files and top-level copies are not part of
the schema and should not be committed. The persona id is spelled
`concensusite` everywhere in code, schemas, and data (a canonical misspelling);
keep it consistent rather than "correcting" individual files.

### 6. Tumor board — round 2 (cross-critiques)

```
/risktaker     <slug> --round 2
/conservative  <slug> --round 2
/critic        <slug> --round 2
/concensusite  <slug> --round 2
/advocate      <slug> --round 2
```

Each persona reads all five round-1 positions and writes four critique rows
(one per other persona) to `data/cases/<slug>/board/critiques.jsonl`. Twenty
rows total. Round-2 prompts explicitly direct each agent to **disagree where
defensible** to mitigate consensus drift.

### 7. Synthesis

```
/PI <slug>          # data/cases/<slug>/recommendations.jsonl + docs/cases/<slug>/index.md
/translator <slug>  # docs/cases/<slug>/plain_language.md
```

The `PI` agent ingests the full dossier, all five positions, and all 20
critiques, and produces a ranked recommendation table. Hard rule: a `veto` from
`conservative` or `critic` is never silently dropped — either overridden with
documented reasoning or kept in the table marked `not_recommended`.

The `translator` agent produces the patient/caregiver track separately —
absolute-risk framing, no NCT IDs in body, "questions to ask your oncologist."
A separate agent (rather than a prompt branch on `PI`) because the audiences
need different *omissions*, not just different word choices.

### 8. Render

```
bash scripts/run_case.sh <slug>
```

Fails fast on `validate_case.py` (schema-checks every committed artifact), then
runs `build_table.py`, `build_evidence.py`, `build_manuscripts.py`,
`build_board.py`, `build_recommendations.py`, `build_preclinical.py`,
`build_target_validation.py`, `build_biomarker_survey.py`,
`build_standard_of_care.py`, `build_accessibility.py`, a PHI re-scan against
rendered docs, and finally `build_report.py` (PDF/HTML downloads). It closes with
a non-fatal `check_pipeline.py` completeness warning. Shared render helpers
(`load_jsonl`, `FEATURE_LABELS`) live in `scripts/libbylib.py`.

### 8a. Validation and completeness gates

Two deterministic gates guard the committed artifacts, both also enforced in the
`validate.yml` CI workflow:

- `scripts/validate_case.py <slug> [--all] [--strict]` validates every JSONL row
  and JSON document against `scripts/schema/*.schema.json`. Referenced identifiers
  are format-checked here (`pmid` numeric, `doi` well-formed); existence and
  contextual correctness are the job of the `reference_checking` skill, which the
  evidence/synthesis agents invoke via `.claude/snippets/reference_check.md`.
- `scripts/check_pipeline.py <slug> [--all]` proves every required stage ran, from
  the board artifacts (5 personas in round 1, 5 critics in round 2, no
  self-critique) through PI + translator surfaces. It keys off artifacts rather
  than `runs.jsonl` because per-persona round telemetry is logged inconsistently.

### 9. Publish

```
git add data/cases/<slug>/ docs/cases/<slug>/
git commit -m "case <slug>: initial run"
git push
```

The pre-commit hook re-scans for PHI shapes. The `phi-scan.yml` CI workflow
runs the scanner against the full tree on every push and fails the deploy on
any hit. The `pages.yml` workflow then runs `mkdocs gh-deploy` to publish.

## Schemas

Every committed JSONL/JSON artifact validates against a schema in
`scripts/schema/`, enforced by `validate_case.py` (in `run_case.sh` and CI) —
not merely documented:

- `profile.schema.json` — scrubbed patient profile.
- `preferences.schema.json` — user tradeoff weights and vetoes.
- `target_validation.schema.json` — target-validator row.
- `biomarker_survey.schema.json` — biomarker-surveyor row.
- `standard_of_care.schema.json` — standard-of-care screener row.
- `trials.schema.json` — trial-screener row.
- `clinical_evidence.schema.json` — clinical-evidence row.
- `preclinical_evidence.schema.json` — pre-clinical evidence row.
- `preclinical_pipeline.schema.json` / `preclinical_recommendations.schema.json` — horizon-scan track.
- `accessibility.schema.json` — accessibility-screener row.
- `positions.schema.json` — board round-1 position.
- `critiques.schema.json` — board round-2 cross-critique.
- `recommendations.schema.json` — PI's ranked recommendation row.
- `runs.schema.json` — per-agent run-log row (`agent` is pinned to the canonical
  agent id; extra telemetry is permitted).

## Cross-tumor and basket trials

The `trial_screener` agent does NOT restrict the search to trials whose primary
indication matches the patient's tumor type. For rare-disease and refractory
patients, the highest-EV trial often lives outside the primary indication.
Each row in `trials.jsonl` is tagged with `tumor_type_relationship`:

- **`primary_indication_match`** — trial enrolls the patient's tumor type as
  a primary cohort. The default category.
- **`basket_or_biomarker_match`** — trial accepts the patient based on a
  biomarker regardless of tumor type (e.g. NTRK fusions, BRAF V600E, MSI-H,
  DLL3 IHC). These are the most under-recognized actionable opportunities for
  rare-disease patients and rank above same-tumor weak-evidence trials in
  practice.
- **`same_drug_other_indication`** — trial of a drug already proven elsewhere
  now being tested in the patient's tumor type. Bridges cross-tumor evidence
  to on-label care.
- **`cross_tumor_extrapolation`** — trial in a different tumor type, included
  in the dossier for mechanism-of-action / efficacy evidence even though the
  patient cannot enroll. Informs board reasoning about whether the drug is
  worth pursuing through a basket trial or off-label use.

The render layer (`build_table.py`) surfaces the category as a colored
badge in the trial table so a clinician can scan enrollable-now vs
informational-only at a glance.

## Biomarker confirmation gating

When a biomarker driving candidate-intervention selection is not yet at the
resolution required for clinical decisions (e.g. DLL3 RNA expression measured
but IHC protein-level confirmation pending), Libby flags the confirmatory
test as the rank-1 workup and tags biomarker-conditional therapeutic recs.
Libby does NOT generate a parallel ranking for the negative-result branch:
if the test is negative, biomarker-conditional recs are foreclosed, and
the cross-cutting caveat in the case page documents what remains valid.

The mechanism is on the schema and PI-prompt side:

- **`profile.json::biomarkers[].confirmation_status`** — one of `confirmed`
  (default), `rna_only`, `ihc_pending`, `ngs_pending`, `hypothetical_positive`,
  `hypothetical_negative`, `unknown`. Set during intake.
- **`profile.json::biomarkers[].decision_resolution`** — short description
  of what level of testing IS required (e.g. "IHC SP347 ≥1%").
- **`recommendations.jsonl::scenario`** — three values:
    - `null` (default) — used in non-gated cases (every biomarker `confirmed`); the row applies in the case's single ranking.
    - `"shared"` — the rank-1 workup row representing the confirmatory test itself.
    - `"<biomarker_short>:positive"` (e.g. `dll3_ihc:positive`) — rec valid only if the named biomarker confirms positive; foreclosed if the test is negative.

  The `:negative` suffix is no longer emitted; the negative-result outcome
  is documented in the case page's cross-cutting caveat instead.
- **`PI.md`** prompt rule: when any biomarker gates a candidate intervention
  and is non-confirmed, emit a focused ranking with the workup at rank 1
  (`scenario: "shared"`) plus only the therapeutic rec(s) that target the
  gating feature, tagged `:positive`. Drugs that don't target the feature
  (standard care for the indication) are out of scope for the ranking and
  **do not appear anywhere in it** — not in the ranked table, not in "Classes
  examined but not ranked", not by name in any of the PI's narrative. The
  cross-cutting caveat in `index.md` carries the "if test negative, no
  within-scope recommendations" mapping in the ranking's own voice, without
  enumerating standard-care alternatives. Those alternatives are enumerated on
  the standard-of-care page instead, which the Case output section links; the
  `PI` neither writes nor reads that page. The trial screener, clinician, and
  researcher contracts enforce mechanism-scope upstream so out-of-scope drugs
  do not enter the dossier in the first place.
- **`translator.md`** prompt rule: surface the workup as "the first step
  everyone agreed on"; flag biomarker-conditional options inline with an
  "if negative" note; do NOT render a parallel negative-branch ranking.
- **`build_recommendations.py`** and **`build_report.py`** render the workup
  under a "Shared first step" header and the rest of the unified ranking
  in a single ranked table. Conditional recs are visually flagged.

Cap: 1 biomarker dimension for `:positive` tagging. If the case has more
than one non-confirmed biomarker, choose the single most-decision-relevant
one; flag the others as open questions.

## Limitations

- `fit_to_case` and `toxicity_flags` in `trials.jsonl` are **LLM-interpreted**,
  not deterministic. Two runs may classify the same trial differently. Treat as
  advisory.
- The PHI scanner is a **safety net, not the defense**. It catches shape-based
  PHI (MRN, SSN, dates, phone, email) but not a clinician's surname embedded in <!-- phi-scan: ignore -->
  free text. The scrub agent is the real guard.
- No outcome tracking. Libby is a recommender, not a registry.
- Persona convergence is a real risk. If all five board members read the same
  dossier and reach the same conclusion, "diversity" was performative. Plan to
  re-tune persona prompts if this happens.
