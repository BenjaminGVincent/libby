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

python3 scripts/build_table.py "$SLUG"
python3 scripts/build_evidence.py "$SLUG"
python3 scripts/build_board.py "$SLUG"
python3 scripts/build_recommendations.py "$SLUG"

# PHI re-scan against rendered docs before commit (belt-and-suspenders).
python3 scripts/scan_for_phi.py --mode=files \
  "data/cases/$SLUG/recommendations.jsonl" \
  "docs/cases/$SLUG/index.md" \
  "docs/cases/$SLUG/plain_language.md" \
  "docs/cases/$SLUG/recommendations.md" \
  "docs/cases/$SLUG/board.md" \
  "docs/cases/$SLUG/evidence.md" \
  "docs/cases/$SLUG/trials.md" 2>&1 | tee /dev/stderr | tail -5

echo "Done. Review docs/cases/$SLUG/ before committing."
