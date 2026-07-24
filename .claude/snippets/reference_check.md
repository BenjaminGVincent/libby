# Reference-verification protocol (shared)

Single source of truth for the citation-accuracy step. Any Libby agent that emits
`pmid` / `doi` / `nct` identifiers or inline references runs this before it records
its `runs.jsonl` row.

## When
After you have written your artifact (the JSONL rows or the rendered doc) and
**before** the humanizer/voice pass and the `runs.jsonl` write.

## How
1. Read the `reference_checking` skill once per run. Prefer the project-vendored
   copy at `.claude/skills/reference_checking/SKILL.md` (MIT, vendored into this
   repo so a fresh clone always has it); if the project copy is missing, fall back
   to `~/.claude/skills/reference_checking/SKILL.md`.
2. Run it over every reference you just wrote. It checks both **existence** and
   **contextual correctness**:
   - the `pmid` resolves and points to the paper you actually cite (not a
     wrong-identifier bug where the ID exists but names a different paper);
   - the `doi` resolves;
   - the paper genuinely supports the surrounding claim — the effect size,
     endpoint, or mechanism in the row is the one that paper reports (citation
     drift);
   - the paper is not retracted;
   - no duplicate citations pointing at the same source under different IDs.

## Fail-closed
Never ship a fabricated or mismatched identifier. If a `pmid`/`doi` does not
resolve or points to a different paper than your prose claims, either correct it
to the right identifier or set the field to `null` and move the descriptive
detail into free text. A `null` identifier is honest; a wrong one is not.

## Record the outcome
Add a `reference_check` object to this run's `runs.jsonl` row, e.g.
`"reference_check": {"checked": 34, "corrected": 2, "nulled": 1, "clean": true}`.
`clean` is `true` only when no unresolved or drifted identifier remains.
