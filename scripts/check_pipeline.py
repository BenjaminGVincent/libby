#!/usr/bin/env python3
"""Assert a Libby case ran every required pipeline stage before it is published.

Usage:
  python3 scripts/check_pipeline.py <slug> [<slug> ...]
  python3 scripts/check_pipeline.py --all

Why artifact-based, not runs.jsonl-based: runs.jsonl is a free-text provenance
log and its per-persona `round` telemetry is recorded inconsistently across
agents, so it cannot reliably prove the board ran both rounds. The authoritative
evidence that a stage completed is the artifact it owns. This checker keys off
those artifacts:

  - board round 1  -> board/positions.jsonl carries all five personas
  - board round 2  -> board/critiques.jsonl carries all five critics, no
                      self-critique
  - PI synthesis   -> recommendations.jsonl + docs/cases/<slug>/index.md
  - translator     -> docs/cases/<slug>/plain_language.md
  - upstream tiers -> trials / clinical_evidence / preclinical_evidence /
                      target_validation JSONL present and non-empty

The preclinical horizon-scan track is standalone (does not feed the board/PI),
so it is reported informationally and never gates.

Exit codes: 0 = complete, 1 = one or more required stages missing, 2 = usage.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CASES_DIR = REPO / "data" / "cases"
DOCS_DIR = REPO / "docs" / "cases"

PERSONAS = {"risktaker", "conservative", "critic", "concensusite", "advocate"}


def _rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text("utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            # A malformed line is a real defect, but validate_case.py is the
            # authority on JSON validity — here we just skip it so the checker
            # reports a clean stage failure (e.g. "personas missing") instead of
            # crashing with a traceback.
            continue
    return out


def check_pipeline(slug: str) -> tuple[list[str], list[str]]:
    """Return (failures, notes) for one case."""
    case = CASES_DIR / slug
    docs = DOCS_DIR / slug
    failures: list[str] = []
    notes: list[str] = []

    if not case.is_dir():
        return ([f"{slug}: no such case directory {case}"], [])

    # Non-empty required JSONL / JSON tiers.
    required_nonempty = {
        "intake/promote": case / "profile.json",
        "preferences": case / "preferences.json",
        "trial_screener": case / "trials.jsonl",
        "clinician": case / "clinical_evidence.jsonl",
        "researcher": case / "preclinical_evidence.jsonl",
        "target_validator": case / "target_validation.jsonl",
        "PI (recommendations)": case / "recommendations.jsonl",
    }
    # accessibility_screener is a required published stage for real cases (10/11
    # of the committed corpus carries it). `demo-` slugs are minimal fixtures that
    # predate the stage — exempt them rather than fabricate published access-path
    # classifications and manufacturer/trial contacts just to satisfy the gate.
    if not slug.startswith("demo-"):
        required_nonempty["accessibility_screener"] = case / "accessibility.jsonl"

    for stage, path in required_nonempty.items():
        if not path.exists():
            failures.append(f"{stage}: missing {path.relative_to(REPO)}")
        elif path.suffix == ".jsonl":
            if not _rows(path):
                failures.append(f"{stage}: empty {path.relative_to(REPO)}")
        else:
            # JSON document: catch both a 0-byte file and a structurally-empty one
            # (e.g. "{}" or whitespace) that a size check alone would pass.
            try:
                payload = json.loads(path.read_text("utf-8"))
            except json.JSONDecodeError:
                failures.append(f"{stage}: malformed JSON {path.relative_to(REPO)}")
            else:
                if not payload:
                    failures.append(f"{stage}: empty {path.relative_to(REPO)}")

    # Rendered PI + translator surfaces.
    for stage, path in {"PI (index.md)": docs / "index.md",
                        "translator": docs / "plain_language.md"}.items():
        if not path.exists():
            failures.append(f"{stage}: missing {path.relative_to(REPO)}")

    # Board round 1: all five personas present in positions.
    positions = _rows(case / "board" / "positions.jsonl")
    pos_personas = {r.get("persona") for r in positions}
    missing_pos = PERSONAS - pos_personas
    if not positions:
        failures.append("board round 1: missing board/positions.jsonl")
    elif missing_pos:
        failures.append(f"board round 1: personas missing from positions: {sorted(missing_pos)}")

    # Board round 2: all five critics present in critiques; flag self-critique.
    critiques = _rows(case / "board" / "critiques.jsonl")
    critic_personas = {r.get("critic_persona") for r in critiques}
    missing_cri = PERSONAS - critic_personas
    if not critiques:
        failures.append("board round 2: missing board/critiques.jsonl")
    elif missing_cri:
        failures.append(f"board round 2: critics missing from critiques: {sorted(missing_cri)}")
    self_crit = [r for r in critiques if r.get("critic_persona") == r.get("target_persona")]
    if self_crit:
        failures.append(f"board round 2: {len(self_crit)} self-critique row(s) (critic == target)")

    # Informational: standalone preclinical track.
    if (case / "preclinical_recommendations.jsonl").exists():
        notes.append(f"{slug}: preclinical horizon-scan track present")

    return (failures, notes)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slugs", nargs="*")
    parser.add_argument("--all", action="store_true", help="Check every case under data/cases/")
    args = parser.parse_args()

    slugs = (
        sorted(p.name for p in CASES_DIR.iterdir() if p.is_dir())
        if args.all
        else args.slugs
    )
    if not slugs:
        parser.error("give at least one slug, or --all")

    total_fail = 0
    for slug in slugs:
        failures, notes = check_pipeline(slug)
        for n in notes:
            print(f"note  {n}")
        if failures:
            print(f"INCOMPLETE  {slug}: {len(failures)} stage(s) missing", file=sys.stderr)
            for f in failures:
                print(f"  - {f}", file=sys.stderr)
        else:
            print(f"COMPLETE    {slug}")
        total_fail += len(failures)

    if total_fail:
        print(f"\n{total_fail} missing stage(s).", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
