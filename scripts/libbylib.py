"""Shared helpers for the Libby build scripts.

Extracted to kill two concrete duplications:
  - `load_jsonl` was reimplemented in 9 build scripts (identically).
  - `FEATURE_LABELS` was maintained in two places (`build_report.py` and
    `build_accessibility.py`) with a "keep in sync" comment — a live drift
    hazard. It now lives here once.

Only the pieces that were provably identical are consolidated. The per-file
`feature_label` helper functions are intentionally left in place because they
diverge (the access guide handles the `__unscoped` key; the report renderer does
not), so they keep their local behavior while sharing this one dictionary.

Build scripts run as `python3 scripts/build_*.py`, so scripts/ is on sys.path[0]
and `from libbylib import ...` resolves without packaging.
"""

from __future__ import annotations

import json
from pathlib import Path


def load_jsonl(path: Path) -> list[dict]:
    """Read a JSONL file into a list of dicts; return [] if the file is absent.

    Blank lines are skipped. Matches the behavior every build script relied on.
    """
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


# Friendlier human-readable names for known scenario_short / target keys.
# Any key not in this map renders title-cased by each caller's local
# feature-label helper. Single source of truth for both build_report.py and
# build_accessibility.py.
FEATURE_LABELS: dict[str, str] = {
    "dll3_ihc": "DLL3-targeting interventions",
    "prame_ihc_hla": "PRAME-targeting interventions",
    "kras_g12r": "KRAS G12R-targeting interventions",
    "cdkn2a_loss": "CDKN2A-loss / MTAP-targeting interventions",
    "germline_brca": "Germline BRCA / HRD-targeting interventions",
    "tp53_inactivating": "TP53-targeting interventions",
    "ccnd3_alteration": "CCND3 / CDK4-6-targeting interventions",
    "egfr_l858r": "EGFR L858R-targeting interventions",
    "met_amplification": "MET amplification-targeting interventions",
}


def drop_superseded(rows: list[dict], id_key: str) -> list[dict]:
    """Drop rows that a later row supersedes.

    Both `accessibility.jsonl` and `standard_of_care.jsonl` are append-only, so a
    correction arrives as a new row carrying `supersedes: "<id of the row it
    replaces>"` rather than as an edit. Without this filter both rows render and a
    reader sees the stale eligibility call sitting next to the corrected one, with
    nothing on the page saying which is current — the failure mode is silent and
    reads as contradiction rather than as an error.

    `id_key` is the artifact's identifier field (`row_id` / `soc_id`). Rows whose
    id is named by any surviving row's `supersedes` are removed. Order is
    preserved; rows without ids are kept untouched.
    """
    superseded = {
        r.get("supersedes") for r in rows if r.get("supersedes")
    }
    if not superseded:
        return rows
    return [r for r in rows if r.get(id_key) not in superseded]
