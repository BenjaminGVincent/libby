#!/usr/bin/env python3
"""Promote a scrubbed profile from local PHI-bearing case/ into committed data/.

Usage: python3 scripts/promote_profile.py <case_slug>

Reads:   case/<slug>/derived/{profile,preferences}.json
Writes:  data/cases/<slug>/{profile,preferences}.json

Only proceeds after both files pass JSON-schema validation AND the PHI scanner.
This is the only path PHI-side data takes into committed territory.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
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


def load_schema(name: str) -> dict:
    path = SCHEMA_DIR / f"{name}.schema.json"
    return json.loads(path.read_text(encoding="utf-8"))


def validate_json(payload: dict, schema_name: str, label: str) -> list[str]:
    schema = load_schema(schema_name)
    validator = jsonschema.Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(payload), key=lambda e: e.path)
    if not errors:
        return []
    out = [f"{label} failed schema validation:"]
    for err in errors:
        loc = "/".join(str(p) for p in err.path) or "<root>"
        out.append(f"  - {loc}: {err.message}")
    return out


def run_phi_scan(paths: list[Path]) -> int:
    cmd = [
        sys.executable,
        str(REPO / "scripts" / "scan_for_phi.py"),
        "--mode=files",
        "--root",
        str(REPO),
        *[str(p) for p in paths],
    ]
    result = subprocess.run(cmd)
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug", help="Case slug (e.g. nsclc-egfr-l858r-post-osi-a4f2)")
    args = parser.parse_args()

    slug = args.slug
    src_dir = REPO / "case" / slug / "derived"
    dst_dir = REPO / "data" / "cases" / slug

    profile_src = src_dir / "profile.json"
    prefs_src = src_dir / "preferences.json"

    if not profile_src.exists() or not prefs_src.exists():
        print(
            f"Expected {profile_src} and {prefs_src}. Run `/intake {slug}` first.",
            file=sys.stderr,
        )
        return 2

    try:
        profile = json.loads(profile_src.read_text(encoding="utf-8"))
        prefs = json.loads(prefs_src.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}", file=sys.stderr)
        return 2

    errors: list[str] = []
    errors += validate_json(profile, "profile", str(profile_src))
    errors += validate_json(prefs, "preferences", str(prefs_src))
    if errors:
        for line in errors:
            print(line, file=sys.stderr)
        return 1

    # PHI scan against the source files (still under case/, not yet promoted).
    rc = run_phi_scan([profile_src, prefs_src])
    if rc != 0:
        print("PHI scan refused promotion.", file=sys.stderr)
        return rc

    # Belt-and-suspenders: enforce that the slug itself is not initials/DOB-shaped.
    if not slug.replace("-", "").isalnum():
        print(f"Slug {slug!r} contains unexpected characters; refusing.", file=sys.stderr)
        return 1

    dst_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(profile_src, dst_dir / "profile.json")
    shutil.copy2(prefs_src, dst_dir / "preferences.json")
    print(f"Promoted {slug}: {dst_dir / 'profile.json'} and {dst_dir / 'preferences.json'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
