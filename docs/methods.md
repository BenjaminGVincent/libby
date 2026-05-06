# Methods

## Targetable-feature scope (cross-cutting rule)

Libby is a **targetable-feature ranker**, not a standard-of-care concierge.
The case slug commits to a specific molecular feature (or features) named in
`profile.json::targetable_features[]` — e.g. *DLL3 RNA expression*, *EGFR
L858R*, *MET exon-14 skipping*. Every downstream surface — the trial table,
the clinical-evidence dossier, the preclinical dossier, the board positions,
the PI ranking, the executive summary, the plain-language page, and the PDF
report — is scoped to drugs whose mechanism plausibly targets one of those
features.

A drug is **in scope** if its mechanism binds, modulates, or acts via the
named feature. A drug is **out of scope** if it does not, even when it has
RCT-grade evidence in the patient's tumor type. Standard 2L+ care for the
indication that doesn't act on the feature (e.g. multi-kinase TKIs in a
DLL3-RNA case) is out of scope: the patient pursues those through their
treating team, independent of Libby.

The contract is enforced at every agent boundary:

- `trial_screener` only logs trials whose drug targets the feature.
- `clinician` only compiles clinical evidence for feature-targeting drugs.
- `researcher` only logs preclinical evidence for feature-targeting drugs.
- The 5 board personas only reason over the in-scope dossier.
- `PI` only ranks feature-targeting interventions; out-of-scope drugs are
  not named in the ranking, in "Classes examined but not ranked", or in any
  narrative.
- `translator` and `reporter` carry the same rule into the patient and PDF
  surfaces.

When a biomarker confirmatory test is negative and the test was the gate on
the feature, the case has no within-scope recommendations and the
cross-cutting caveat says exactly that — *without* naming standard-care
alternatives. The treating team's standard-care conversation is a separate
artifact from Libby's case page.

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

### 4. Research tier

```
/trial_screener <slug>     # data/cases/<slug>/trials.jsonl
/clinician      <slug>     # data/cases/<slug>/clinical_evidence.jsonl
/researcher     <slug>     # data/cases/<slug>/preclinical_evidence.jsonl
```

Each agent reads only `data/cases/<slug>/{profile,preferences}.json`,
`target_validation.jsonl` (when present), and the prior agent's output.
They never read `case/<slug>/clinical/` directly.

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

Runs `build_table.py`, `build_evidence.py`, `build_board.py`,
`build_recommendations.py`, and a final PHI re-scan against rendered docs.

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

All committed JSONL artifacts validate against schemas in
`scripts/schema/`:

- `profile.schema.json` — scrubbed patient profile.
- `preferences.schema.json` — user tradeoff weights and vetoes.
- `trials.schema.json` — trial-screener row.
- `clinical_evidence.schema.json` — clinical-evidence row.
- `preclinical_evidence.schema.json` — pre-clinical evidence row.
- `positions.schema.json` — board round-1 position.
- `critiques.schema.json` — board round-2 cross-critique.
- `recommendations.schema.json` — PI's ranked recommendation row.

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
  (standard care for the indication) are out of scope and **do not appear
  in the case output at all** — not in the ranking, not in "Classes examined
  but not ranked", not by name in any narrative. The cross-cutting caveat in
  `index.md` carries the "if test negative, no within-scope recommendations"
  mapping without enumerating standard-care alternatives. The trial screener,
  clinician, and researcher contracts enforce mechanism-scope upstream so
  out-of-scope drugs do not enter the dossier in the first place.
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
