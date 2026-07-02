#!/usr/bin/env bash
# Run all deterministic build scripts for a Libby case.
# Usage: bash scripts/run_case.sh <slug>

set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "usage: $0 <slug>" >&2
  exit 2
fi

SLUG="$1"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

# Fail fast: every committed JSONL/JSON artifact must validate against its schema
# before we render anything from it. Catches agent output drift at the source.
python3 scripts/validate_case.py "$SLUG"

python3 scripts/build_table.py "$SLUG"
python3 scripts/build_evidence.py "$SLUG"
python3 scripts/build_manuscripts.py "$SLUG"
python3 scripts/build_board.py "$SLUG"
python3 scripts/build_recommendations.py "$SLUG"
python3 scripts/build_preclinical.py "$SLUG"
python3 scripts/build_target_validation.py "$SLUG"
python3 scripts/build_accessibility.py "$SLUG"

# PHI re-scan against rendered docs before commit (belt-and-suspenders).
python3 scripts/scan_for_phi.py --mode=files \
  "data/cases/$SLUG/recommendations.jsonl" \
  "docs/cases/$SLUG/index.md" \
  "docs/cases/$SLUG/plain_language.md" \
  "docs/cases/$SLUG/recommendations.md" \
  "docs/cases/$SLUG/preclinical_recommendations.md" \
  "docs/cases/$SLUG/board.md" \
  "docs/cases/$SLUG/evidence.md" \
  "docs/cases/$SLUG/manuscripts.md" \
  "docs/cases/$SLUG/target_validation.md" \
  "docs/cases/$SLUG/accessibility.md" \
  "docs/cases/$SLUG/trials.md" 2>&1 | tee /dev/stderr | tail -5

# Build PDFs + HTML downloads (clinician report, plain-language, manuscripts, recs HTML).
# Capture the exit code instead of swallowing it with `|| true`, so a broken report
# is loud rather than a silent no-op.
report_rc=0
python3 scripts/build_report.py "$SLUG" 2>&1 || report_rc=$?
if [ "$report_rc" -ne 0 ]; then
  echo "ERROR: build_report.py failed for $SLUG (exit $report_rc) — PDFs/HTML downloads are stale or missing." >&2
fi

echo "Done. Review docs/cases/$SLUG/ before committing."
exit "$report_rc"
