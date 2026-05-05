# Methods

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

### 3. Research tier

```
/trial_screener <slug>     # data/cases/<slug>/trials.jsonl
/clinician      <slug>     # data/cases/<slug>/clinical_evidence.jsonl
/researcher     <slug>     # data/cases/<slug>/preclinical_evidence.jsonl
```

Each agent reads only `data/cases/<slug>/{profile,preferences}.json` and the
prior agent's output. They never read `case/<slug>/clinical/` directly.

### 4. Tumor board — round 1 (positions)

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

### 5. Tumor board — round 2 (cross-critiques)

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

### 6. Synthesis

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

### 7. Render

```
bash scripts/run_case.sh <slug>
```

Runs `build_table.py`, `build_evidence.py`, `build_board.py`,
`build_recommendations.py`, and a final PHI re-scan against rendered docs.

### 8. Publish

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

## Hypothetical biomarker scenarios

When a biomarker driving candidate-intervention selection is not yet at the
resolution required for clinical decisions (e.g. DLL3 RNA expression measured
but IHC protein-level confirmation pending), Libby branches the
recommendation output into parallel scenarios rather than collapsing to a
single ranking.

The mechanism is on the schema and PI-prompt side:

- **`profile.json::biomarkers[].confirmation_status`** — one of `confirmed`
  (default), `rna_only`, `ihc_pending`, `ngs_pending`, `hypothetical_positive`,
  `hypothetical_negative`, `unknown`. Set during intake.
- **`profile.json::biomarkers[].decision_resolution`** — short description
  of what level of testing IS required (e.g. "IHC SP347 ≥1%").
- **`recommendations.jsonl::scenario`** — `null` for single-scenario runs,
  `<biomarker_short>:positive` / `<biomarker_short>:negative` for branched
  runs. Rows with `scenario: "shared"` apply to every branch (typically the
  rank-1 workup that gates branch selection).
- **`PI.md`** prompt rule: when any biomarker is non-confirmed, emit two
  complete sets of recommendations, re-computing endorsements / dissents /
  vetoes per scenario (board objections that were *contingent* on the
  biomarker may flip; objections on grounds independent of the biomarker
  persist).
- **`translator.md`** prompt rule: parallel "if positive / if negative"
  sections in the plain-language page.
- **`build_recommendations.py`** renders each scenario as its own ranked
  sub-table under a labeled heading.

Cap: 2 biomarker dimensions per case. More than one non-confirmed biomarker
collapses scenarios on the most-decision-relevant one; the others become
open questions in the relevant rows.

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
