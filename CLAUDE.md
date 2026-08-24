# CLAUDE.md — working conventions for Libby

Libby is a manually-driven multi-agent pipeline that surfaces candidate
therapeutics for one cancer patient's stated targetable features. Decision
support, not medical advice. Full method: `docs/methods.md`. This file anchors
the conventions an agent (human or model) must keep.

## PHI boundary (the one rule that must never break)
- `case/<slug>/` is gitignored PHI territory. It never enters version control.
- The only bridge to committed data is `scripts/promote_profile.py`, which
  schema-validates and PHI-scans before copying into `data/cases/<slug>/`.
- Never `git add -A` / `git add -u`. Stage explicit paths — `case/` would slip
  in otherwise. Use `git add data/cases/<slug>/ docs/cases/<slug>/`.
- `scripts/scan_for_phi.py` is the tripwire (pre-commit hook + CI tree scan). It
  is shape-based; the intake agent's scrub is the real defense.

## The pipeline
Manual agent invocations (`.claude/agents/*.md` are the "slash commands"; there
is no `.claude/commands/`). Order:
intake → `promote_profile.py` → preclinical_biomarker_surveyor → target_validator
→ trial_screener → clinician → researcher → accessibility_screener → 5 board
personas × 2 rounds → PI → translator → reporter. Standalone horizon-scan track:
preclinical_phd_screener → preclinical_reporter (does not feed the board/PI).
Biomarker-survey track: preclinical_biomarker_surveyor → biomarker_reporter for
the published page, and its `handoff_to_target_validator` rows into
target_validator (linked by `source_survey_id`, so a dropped handoff shows on the
page rather than vanishing).
Standard-of-care track: standalone standard_of_care_screener (owns both its JSONL
and its narrative, then renders its own page). Runs any time after
`promote_profile.py`; best after PI, when `relationship_to_targeted_options` can
name the ranked interventions it sequences against.

## Question-scoped runs
A parallel entry point for a single question, using the same research tier and
the same board (5 personas x 2 rounds, not relaxed) but scoped to a question
instead of a target set:
`question_framer` -> research tier -> board -> `question_synthesist` -> `question_reporter`.

- `question.json` replaces `profile.json::targetable_features[]` as the scope
  spine, and its presence is what routes `check_pipeline.py` to the question
  rules. `question_answer.json` is the terminal artifact, not a ranking.
- Linked (`source_case_slug` set) inherits the source case's profile in place
  (no copy into the question tree) and gets its own slug; the source case is
  never mutated. Standalone has no patient and no PHI surface.
- `acceptance_criteria` are written before the search and every one must be
  reported against afterwards. That audit trail is the point; both the gate and
  the renderer enforce it.
- The synthesist may downgrade the answer shape, never upgrade it.
  `insufficient_evidence` is a first-class verdict and must not be softened.
Full method: `docs/methods.md`.

## Two therapeutic tables, split by regulatory maturity
The landscape is reported as **two separate co-equal tables**, both on the case
page: the **Experimental table** (`PI` → `recommendations.jsonl`) and the
**Standard-of-care table** (`standard_of_care_screener` →
`standard_of_care.jsonl`). An option lands in exactly one, by maturity — an
approved or guideline-carried option is standard-of-care's *even when it targets
a stated feature*, and so are surgery, radiotherapy, chemotherapy and palliative
care when a guideline carries them.

Tables are the case's most important output, more important than prose. So the
rule that matters is about the **union**: a therapy may be routed between tables,
but it may never end up in neither. `check_pipeline.py` fails a case when a
therapy with dossier evidence appears in neither table (opt-in via
`access_route`; diagnostics are out of scope, being consolidated into the rank-1
workup row). Routing is a filing decision; dropping is a defect. The PI must also
name the routed therapies in the `index.md` scope note, so a reader looking for
chemotherapy learns in one line where it is and that the board ranked it, rather
than concluding it was rejected.

**Each table ranks itself 1..n, independently.** The Experimental table runs 1..n
and the Standard-of-care table runs its own 1..m; neither is a continuation of
the other, so both starting at 1 is correct. `check_pipeline.py` fails a gap, a
duplicate, a table starting above 1, or a partially-ranked table.

`access_route` on an experimental row distinguishes trial-only from off-label and
compassionate-use — within that table these are not interchangeable.
`surfaced_reason` demotes a row within its table; it never removes it.

## Standard of care is additive, never subtractive
The standard-of-care track never writes to `recommendations.jsonl` or any board
file, and it must never remove, rerank, narrow, or argue against an experimental
option. Adding standard care must not cost the case a single non-standard
option. The one sanctioned bridge is `relationship_to_targeted_options`, which
names sequencing and conflicts in one direction only and does not rank. If it
surfaces an *investigational* therapy the dossier missed, that is a gap to flag
for a `/trial_screener` or `/clinician` re-run, not something it absorbs into a
standard-of-care row. See the cross-cutting rule in `docs/methods.md`.

## Data model & gates
- `data/cases/<slug>/` holds committed JSONL/JSON; board output lives only in
  `board/{positions,critiques}.jsonl`. `docs/cases/<slug>/` holds rendered pages.
- `data/reference/` holds case-independent panels. `selected_biomarker_panel.json`
  is machine-generated by `scripts/import_biomarker_panel.py` from
  `selected_biomarker_target_list.xlsx` — never hand-edit it; fix the workbook and
  re-import (`--check` proves the committed copy is in sync).
  `tumor_agnostic_biomarkers.json` is hand-curated and safe to edit.
- Every artifact validates against `scripts/schema/*.schema.json`. Run
  `scripts/validate_case.py <slug>` (schema gate) and
  `scripts/check_pipeline.py <slug>` (stage-completeness gate). Both run in CI
  (`validate.yml`) and inside `run_case.sh`.
- Deterministic renderers share helpers from `scripts/libbylib.py` (`load_jsonl`,
  `FEATURE_LABELS`) — don't re-duplicate them.

## Prose & citations
- Every reference-emitting agent runs the reference-verification protocol in
  `.claude/snippets/reference_check.md` (the `reference_checking` skill) before
  logging — catches hallucinated/drifted PMIDs. `pmid` is a bare numeric string,
  `doi` a bare `10.xxxx/...` string, or `null`; schema patterns enforce the shape.
- Every prose-writing agent runs the humanizer pass per
  `.claude/snippets/humanizer.md` (single source — don't inline the skill path).
- `—` is a legitimate empty-cell placeholder in rendered tables. The "no
  em-dashes" rule is a humanizer prose guideline for patient-facing narrative,
  not a mechanical lint.

## Naming
- The guidelines persona is spelled `concensusite` everywhere (a canonical
  misspelling). Keep it consistent; do not "correct" individual files.
- `concensusite` alone among the board personas has web access, by design.

## Tests
`pytest` (see `tests/`). Run before committing script/schema changes.
