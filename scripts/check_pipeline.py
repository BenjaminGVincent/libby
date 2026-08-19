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


def check_question_case(slug: str, case: Path, docs: Path) -> tuple[list[str], list[str]]:
    """Completeness rules for a question-scoped run.

    A question run does the same research and tumor-board work as a full case but
    is scoped to one question instead of a target set, so the feature-ranking
    artifacts do not all apply:

      - `question.json` replaces profile.json::targetable_features[] as the scope
        spine, and `question_answer.json` replaces recommendations.jsonl as the
        terminal artifact.
      - `recommendations.jsonl` is required ONLY when the answer is option-shaped.
        Requiring it unconditionally would push every question into a ranking,
        which is the failure mode the track exists to avoid.
      - `target_validation.jsonl` and `accessibility.jsonl` are informational: a
        prognostic or mechanistic question may have no assay to harden and no
        intervention to price.
      - `profile.json` is required only for a linked question. A standalone
        question has no patient and no PHI surface.

    The board is NOT relaxed. The full five personas over two rounds is what the
    question track buys, and a question answered without it is a literature
    search wearing a case report's clothes.
    """
    failures: list[str] = []
    notes: list[str] = []

    try:
        question = json.loads((case / "question.json").read_text("utf-8"))
    except (OSError, json.JSONDecodeError):
        return ([f"{slug}: question.json unreadable or malformed"], [])

    required_nonempty = {
        "question_framer": case / "question.json",
        "trial_screener": case / "trials.jsonl",
        "clinician": case / "clinical_evidence.jsonl",
        "researcher": case / "preclinical_evidence.jsonl",
        "question_synthesist": case / "question_answer.json",
    }

    linked = question.get("source_case_slug")
    if linked:
        required_nonempty["inherited profile"] = case / "profile.json"

    try:
        answer = json.loads((case / "question_answer.json").read_text("utf-8"))
    except (OSError, json.JSONDecodeError):
        answer = {}

    shape = answer.get("answer_shape_used") or question.get("answer_shape")
    if shape == "verdict_plus_ranked_options":
        required_nonempty["synthesist (ranked options)"] = case / "recommendations.jsonl"

    for stage, path in required_nonempty.items():
        if not path.exists():
            failures.append(f"{stage}: missing {path.relative_to(REPO)}")
        elif path.suffix == ".jsonl":
            if not _rows(path):
                failures.append(f"{stage}: empty {path.relative_to(REPO)}")
        else:
            try:
                payload = json.loads(path.read_text("utf-8"))
            except json.JSONDecodeError:
                failures.append(f"{stage}: malformed JSON {path.relative_to(REPO)}")
            else:
                if not payload:
                    failures.append(f"{stage}: empty {path.relative_to(REPO)}")

    if not (docs / "question.md").exists():
        failures.append(f"question_reporter: missing {(docs / 'question.md').relative_to(REPO)}")

    # Board: unrelaxed, same rule as a full case.
    positions = _rows(case / "board" / "positions.jsonl")
    pos_personas = {r.get("persona") for r in positions}
    if not positions:
        failures.append("board round 1: missing or empty board/positions.jsonl")
    elif PERSONAS - pos_personas:
        failures.append(
            "board round 1: missing personas " + ", ".join(sorted(PERSONAS - pos_personas))
        )

    critiques = _rows(case / "board" / "critiques.jsonl")
    crit_personas = {r.get("critic_persona") for r in critiques}
    if not critiques:
        failures.append("board round 2: missing or empty board/critiques.jsonl")
    else:
        if PERSONAS - crit_personas:
            failures.append(
                "board round 2: missing critics " + ", ".join(sorted(PERSONAS - crit_personas))
            )
        selfcrit = [r for r in critiques if r.get("critic_persona") == r.get("target_persona")]
        if selfcrit:
            failures.append(f"board round 2: {len(selfcrit)} self-critique row(s)")

    kind = "linked to " + linked if linked else "standalone"
    notes.append(f"{slug}: question-scoped run ({kind}), answer shape {shape}")
    if not (case / "target_validation.jsonl").exists():
        notes.append(f"{slug}: no target_validation (not required for a question run)")
    if not (case / "accessibility.jsonl").exists():
        notes.append(f"{slug}: no accessibility screen (not required for a question run)")

    return (failures, notes)


def check_pipeline(slug: str) -> tuple[list[str], list[str]]:
    """Return (failures, notes) for one case."""
    case = CASES_DIR / slug
    docs = DOCS_DIR / slug
    failures: list[str] = []
    notes: list[str] = []

    if not case.is_dir():
        return ([f"{slug}: no such case directory {case}"], [])

    # A question-scoped run is gated differently. `question.json` is the marker:
    # it is the scope spine that replaces targetable_features[], so its presence
    # is what says "judge this as a question, not as a feature ranking".
    if (case / "question.json").exists():
        return check_question_case(slug, case, docs)

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

    # Informational: standalone biomarker-survey track. Reported rather than
    # gated because the committed corpus predates it, and because a case whose
    # workup genuinely covers the panel is a legitimate state. The note names
    # the gap counts so a reviewer can see the survey ran and what it found.
    survey = _rows(case / "biomarker_survey.jsonl")
    if survey:
        gaps = sum(1 for r in survey if r.get("measurement_status") == "not_measured")
        soft = sum(1 for r in survey if r.get("measurement_status") == "measured_not_hardened")
        notes.append(
            f"{slug}: biomarker survey present ({len(survey)} surveyed, "
            f"{gaps} not measured, {soft} not decision-grade)"
        )
        # A handoff row that never reached the target_validator is a real break in
        # the chain: the gap was found and then dropped. Informational for now,
        # since the survey can legitimately run after the validator has finished.
        pending = [r for r in survey if r.get("handoff_to_target_validator")]
        if pending and not (case / "target_validation.jsonl").exists():
            notes.append(
                f"{slug}: {len(pending)} biomarker-survey row(s) awaiting /target_validator"
            )

    # Informational: standalone standard-of-care track. Never gates. It is additive
    # to the targetable-feature ranking rather than a stage of it, the committed
    # corpus predates it, and a case can legitimately publish without it. The note
    # reports what the screen found so a reviewer can see it ran.
    soc = _rows(case / "standard_of_care.jsonl")
    if soc:
        now = sum(1 for r in soc if r.get("consideration_status") == "consider_now")
        gated = sum(1 for r in soc if r.get("consideration_status") == "requires_further_workup")
        notes.append(
            f"{slug}: standard-of-care screen present ({len(soc)} assessed, "
            f"{now} to consider now, {gated} behind an open gate)"
        )
        # The sequencing column is the one thing this track cannot fill before the
        # PI has ranked. Flag it so a mid-pipeline run gets refreshed rather than
        # publishing with the trade-offs silently absent.
        if (case / "recommendations.jsonl").exists() and not any(
            (r.get("relationship_to_targeted_options") or {}).get("relation") for r in soc
        ):
            notes.append(
                f"{slug}: standard-of-care rows carry no sequencing link to the ranked "
                f"options; re-run /standard_of_care_screener to fill it"
            )

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
