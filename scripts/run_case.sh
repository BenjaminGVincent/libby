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
# --strict matches CI (validate.yml), so drift warnings (unexpected/stray artifacts)
# surface here rather than passing locally and only failing in CI.
python3 scripts/validate_case.py --strict "$SLUG"

python3 scripts/build_table.py "$SLUG"
python3 scripts/build_evidence.py "$SLUG"
python3 scripts/build_manuscripts.py "$SLUG"
python3 scripts/build_board.py "$SLUG"
python3 scripts/build_recommendations.py "$SLUG"
python3 scripts/build_preclinical.py "$SLUG"
python3 scripts/build_target_validation.py "$SLUG"
python3 scripts/build_biomarker_survey.py "$SLUG"
python3 scripts/build_standard_of_care.py "$SLUG"
python3 scripts/build_accessibility.py "$SLUG"

# Build PDFs + HTML downloads (clinician report, plain-language, manuscripts, recs HTML).
# Capture the exit code instead of swallowing it with `|| true`, so a broken report
# is loud rather than a silent no-op.
report_rc=0
python3 scripts/build_report.py "$SLUG" 2>&1 || report_rc=$?
if [ "$report_rc" -ne 0 ]; then
  echo "ERROR: build_report.py failed for $SLUG (exit $report_rc) — PDFs/HTML downloads are stale or missing." >&2
fi

# PHI re-scan before commit (belt-and-suspenders), run AFTER build_report so the
# freshly-built self-contained .html downloads are covered too. The file list is
# derived from the case tree rather than hand-maintained, so a new artifact type
# can't silently escape the local scan. scan_for_phi filters by extension, so
# passing every file is safe (binaries are skipped). CI's --mode=tree scan is the
# authoritative gate; this catches problems before they reach a commit.
scan_targets=()
while IFS= read -r f; do scan_targets+=("$f"); done < <(
  find "data/cases/$SLUG" "docs/cases/$SLUG" -type f 2>/dev/null | sort
)
if [ "${#scan_targets[@]}" -gt 0 ]; then
  python3 scripts/scan_for_phi.py --mode=files "${scan_targets[@]}"
fi

# Non-fatal completeness check: surface any missing pipeline stage (a partial
# render mid-pipeline is legitimate, so this warns rather than blocks). CI runs
# the same check as a hard gate on published cases.
if ! python3 scripts/check_pipeline.py "$SLUG"; then
  echo "WARNING: $SLUG is missing pipeline stages (see above) — fine mid-pipeline, but not publishable yet." >&2
fi

echo "Done. Review docs/cases/$SLUG/ before committing."
exit "$report_rc"
