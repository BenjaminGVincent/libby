#!/usr/bin/env python3
"""Validate a Libby case's committed artifacts against scripts/schema/*.schema.json.

Usage:
  python3 scripts/validate_case.py <slug> [<slug> ...]
  python3 scripts/validate_case.py --all

Every JSONL row and every JSON document under data/cases/<slug>/ is checked against
its schema. Until now only profile/preferences were validated (in promote_profile.py);
the other artifacts had schemas that nothing loaded. This closes that gap and is wired
into scripts/run_case.sh (fail-fast, before the renderers) and CI.

Exit codes: 0 = all valid, 1 = one or more schema errors, 2 = usage / missing input.
Warnings (unexpected/ drifted files) do not fail the run on their own; pass --strict
to promote warnings to errors.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print(
        "Missing dependency `jsonschema`. Install with `pip install jsonschema>=4.21`.",
        file=sys.stderr,
    )
    sys.exit(2)

REPO = Path(__file__).resolve().parent.parent
SCHEMA_DIR = REPO / "scripts" / "schema"
CASES_DIR = REPO / "data" / "cases"

# Single-document JSON artifacts → schema name.
JSON_ARTIFACTS = {
    "profile.json": "profile",
    "preferences.json": "preferences",
}

# JSONL artifacts (one object per line) → schema name. Paths are relative to the
# case directory so the board/ subdir is addressed explicitly.
JSONL_ARTIFACTS = {
    "trials.jsonl": "trials",
    "clinical_evidence.jsonl": "clinical_evidence",
    "preclinical_evidence.jsonl": "preclinical_evidence",
    "preclinical_pipeline.jsonl": "preclinical_pipeline",
    "preclinical_recommendations.jsonl": "preclinical_recommendations",
    "recommendations.jsonl": "recommendations",
    "target_validation.jsonl": "target_validation",
    "biomarker_survey.jsonl": "biomarker_survey",
    "accessibility.jsonl": "accessibility",
    "runs.jsonl": "runs",
    "board/positions.jsonl": "positions",
    "board/critiques.jsonl": "critiques",
}

# Canonical board personas (note the deliberate `concensusite` misspelling). Used by
# the cross-file referential-integrity pass to catch a critique or recommendation that
# names a persona that never posted — including a "corrected" consensusite spelling.
PERSONAS = frozenset({"risktaker", "conservative", "critic", "concensusite", "advocate"})

_SCHEMA_CACHE: dict[str, jsonschema.Draft202012Validator] = {}


class SchemaError(Exception):
    """A mapped schema file is missing or malformed — a repo-integrity problem,
    surfaced as a clean per-artifact error rather than an uncaught traceback."""


def validator_for(schema_name: str) -> jsonschema.Draft202012Validator:
    if schema_name not in _SCHEMA_CACHE:
        schema_path = SCHEMA_DIR / f"{schema_name}.schema.json"
        try:
            schema = json.loads(schema_path.read_text("utf-8"))
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise SchemaError(f"cannot load schema {schema_path.name}: {e}") from e
        _SCHEMA_CACHE[schema_name] = jsonschema.Draft202012Validator(schema)
    return _SCHEMA_CACHE[schema_name]


def _format_errors(validator, payload, where: str) -> list[str]:
    errs = sorted(validator.iter_errors(payload), key=lambda e: list(e.path))
    out = []
    for err in errs:
        loc = "/".join(str(p) for p in err.path) or "<root>"
        out.append(f"  {where}: {loc}: {err.message}")
    return out


def validate_json_doc(path: Path, schema_name: str) -> list[str]:
    try:
        payload = json.loads(path.read_text("utf-8"))
    except json.JSONDecodeError as e:
        return [f"  {path.name}: JSON parse error: {e}"]
    try:
        validator = validator_for(schema_name)
    except SchemaError as e:
        return [f"  {path.name}: {e}"]
    return _format_errors(validator, payload, path.name)


def validate_jsonl(path: Path, schema_name: str) -> list[str]:
    try:
        validator = validator_for(schema_name)
    except SchemaError as e:
        return [f"  {path.name}: {e}"]
    errors: list[str] = []
    for lineno, raw in enumerate(path.read_text("utf-8").splitlines(), start=1):
        raw = raw.strip()
        if not raw:
            continue
        try:
            row = json.loads(raw)
        except json.JSONDecodeError as e:
            errors.append(f"  {path.name}:{lineno}: JSON parse error: {e}")
            continue
        errors.extend(_format_errors(validator, row, f"{path.name}:{lineno}"))
    return errors


def _load_rows(path: Path) -> list[dict]:
    """Parse a JSONL file into rows, skipping blank/malformed lines (schema
    validation is the authority on malformed JSON; here we only need the shape)."""
    if not path.exists():
        return []
    rows: list[dict] = []
    for raw in path.read_text("utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        try:
            rows.append(json.loads(raw))
        except json.JSONDecodeError:
            continue
    return rows


def referential_warnings(case_dir: Path, slug: str, check_refs: bool) -> list[str]:
    """Cross-file referential-integrity warnings for one case.

    Two tiers, by false-positive risk (measured against the committed corpus):

    - Always on (0 corpus hits): every persona named in a critique or in a
      recommendation's endorse/dissent/veto list must be one of the five canonical
      personas. Catches a hallucinated or "corrected" (consensusite) persona id.
    - Opt-in via --check-refs: every critique's `target_intervention_id` must resolve
      to an intervention that actually appears in the case's board picks or ranked
      recommendations. This is a genuine drift signal but the corpus is not yet clean
      (personas sometimes target a synonym id), so it stays out of the default --strict
      stream until the data is reconciled. Citation membership is deliberately NOT
      checked here — the `reference_checking` skill owns citation correctness, and
      board personas legitimately cite beyond the exact dossier rows.
    """
    warnings: list[str] = []
    critiques = _load_rows(case_dir / "board" / "critiques.jsonl")
    recs = _load_rows(case_dir / "recommendations.jsonl")

    for i, r in enumerate(critiques, start=1):
        for key in ("critic_persona", "target_persona"):
            val = r.get(key)
            if val is not None and val not in PERSONAS:
                warnings.append(f"{slug}: critiques.jsonl:{i}: {key} {val!r} is not a known persona")
    for i, r in enumerate(recs, start=1):
        for key in ("endorsed_by", "dissent_by", "veto_by"):
            for val in (r.get(key) or []):
                if val not in PERSONAS:
                    warnings.append(f"{slug}: recommendations.jsonl:{i}: {key} lists unknown persona {val!r}")

    if check_refs:
        known_iids = {
            p.get("intervention_id")
            for row in _load_rows(case_dir / "board" / "positions.jsonl")
            for p in (row.get("picks") or [])
        }
        known_iids |= {r.get("intervention_id") for r in recs}
        known_iids.discard(None)
        for i, r in enumerate(critiques, start=1):
            tid = r.get("target_intervention_id")
            if tid and tid not in known_iids:
                warnings.append(
                    f"{slug}: critiques.jsonl:{i}: target_intervention_id {tid!r} "
                    f"resolves to no board pick or ranked recommendation"
                )
    return warnings


def validate_case(slug: str, check_refs: bool = False) -> tuple[list[str], list[str]]:
    """Return (errors, warnings) for one case."""
    case_dir = CASES_DIR / slug
    errors: list[str] = []
    warnings: list[str] = []

    if not case_dir.is_dir():
        return ([f"{slug}: no such case directory {case_dir}"], [])

    for name, schema_name in JSON_ARTIFACTS.items():
        p = case_dir / name
        if p.exists():
            errors.extend(validate_json_doc(p, schema_name))

    for rel, schema_name in JSONL_ARTIFACTS.items():
        p = case_dir / rel
        if p.exists():
            errors.extend(validate_jsonl(p, schema_name))

    # Drift detection: any .jsonl in the case tree not covered by the maps above.
    mapped = {(case_dir / rel).resolve() for rel in JSONL_ARTIFACTS}
    for p in sorted(case_dir.rglob("*.jsonl")):
        if p.resolve() in mapped:
            continue
        warnings.append(f"{slug}: unexpected artifact not in schema map: {p.relative_to(case_dir)}")

    # A stray top-level positions.jsonl / critiques.jsonl is drift — board files
    # belong under board/ (build_board.py only reads board/).
    for stray in ("positions.jsonl", "critiques.jsonl"):
        if (case_dir / stray).exists():
            warnings.append(f"{slug}: stray top-level {stray} (canonical location is board/{stray})")

    warnings.extend(referential_warnings(case_dir, slug, check_refs))

    return (errors, warnings)


def iter_slugs(args) -> list[str]:
    if args.all:
        return sorted(p.name for p in CASES_DIR.iterdir() if p.is_dir())
    return args.slugs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slugs", nargs="*", help="Case slug(s) to validate")
    parser.add_argument("--all", action="store_true", help="Validate every case under data/cases/")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    parser.add_argument(
        "--check-refs",
        action="store_true",
        help=(
            "Additionally audit cross-file references that are not yet corpus-clean "
            "(critique target_intervention_id resolution). Emitted as warnings; not run "
            "by default so --strict CI stays green until the data is reconciled."
        ),
    )
    args = parser.parse_args()

    slugs = iter_slugs(args)
    if not slugs:
        parser.error("give at least one slug, or --all")

    total_errors = 0
    total_warnings = 0
    for slug in slugs:
        errors, warnings = validate_case(slug, check_refs=args.check_refs)
        for w in warnings:
            print(f"WARN  {w}", file=sys.stderr)
        if errors:
            print(f"FAIL  {slug}: {len(errors)} schema error(s)", file=sys.stderr)
            for line in errors:
                print(line, file=sys.stderr)
        else:
            print(f"OK    {slug}")
        total_errors += len(errors)
        total_warnings += len(warnings)

    if total_warnings:
        print(f"\n{total_warnings} warning(s).", file=sys.stderr)
    if total_errors:
        print(f"{total_errors} schema error(s) across {len(slugs)} case(s).", file=sys.stderr)
        return 1
    if args.strict and total_warnings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
