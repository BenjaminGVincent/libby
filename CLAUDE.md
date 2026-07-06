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
intake → `promote_profile.py` → target_validator → trial_screener → clinician →
researcher → accessibility_screener → 5 board personas × 2 rounds → PI →
translator → reporter. Standalone horizon-scan track: preclinical_phd_screener →
preclinical_reporter (does not feed the board/PI).

## Data model & gates
- `data/cases/<slug>/` holds committed JSONL/JSON; board output lives only in
  `board/{positions,critiques}.jsonl`. `docs/cases/<slug>/` holds rendered pages.
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
