#!/usr/bin/env python3
"""Scan files for PHI-shaped strings.

Three modes:
  --mode=staged    Scan staged paths reported by `git diff --cached --name-only`.
  --mode=tree      Scan every tracked file in the repo.
  --mode=files     Scan the file paths passed as positional args.

Exit code is non-zero on any hit, plus a human-readable report on stderr.

The blocklist catches PHI shapes (MRN, SSN, US phone, email, day-precision
dates, ALL-CAPS NAME tokens). It will NOT catch a doctor's surname dropped into
a free-text rationale or a hospital name embedded in a quoted note. Treat the
scrub agent as the real defense and this scanner as a tripwire.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

# Refusal patterns — each (label, compiled_pattern, description).
# Patterns are intentionally conservative: high-recall on shape-based PHI,
# willing to false-positive on benign content (which the user can override
# via `# phi-scan: ignore` on the offending line).
PATTERNS: list[tuple[str, re.Pattern[str], str]] = [
    ("ssn", re.compile(r"\b\d{3}-\d{2}-\d{4}\b"), "US SSN-shaped string (NNN-NN-NNNN)"),
    (
        "us_phone",
        re.compile(r"(?<!\d)(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}(?!\d)"),
        "US phone number",
    ),
    (
        "email",
        re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
        "email address",
    ),
    (
        "mrn_label",
        # Require an explicit ":" or "#" after the label so mRNA-NNNN doesn't
        # match MRN-NNNN. Drop the case-insensitive flag so mRNA-4203 (lowercase
        # m, embedded RNA) is not matched as MRN.
        re.compile(r"\b(?:MRN|Medical Record Number)\s*[:#]\s*[A-Z0-9-]{4,}"),
        "labeled MRN",
    ),
    (
        "iso_date_full",
        re.compile(r"\b(19|20)\d{2}-\d{2}-\d{2}\b"),
        "day-precision ISO date (use age band / month-year only)",
    ),
    (
        "us_date",
        re.compile(r"\b\d{1,2}/\d{1,2}/(19|20)\d{2}\b"),
        "day-precision US date (use age band / month-year only)",
    ),
    (
        "dob_label",
        re.compile(r"\b(?:DOB|D\.O\.B\.|Date of Birth)\b", re.IGNORECASE),
        "labeled date of birth",
    ),
    (
        "all_caps_name",
        re.compile(r"\b[A-Z][A-Z]+,\s*[A-Z][A-Z]+\b"),
        "ALL-CAPS NAME, NAME pattern (likely patient or clinician identifier)",
    ),
    (
        "patient_label",
        re.compile(r"\b(?:Patient|Pt)\s+name\s*[:#]", re.IGNORECASE),
        "labeled patient name",
    ),
]

# Text-bearing extensions we scan. Binary / generated formats are skipped.
SCAN_EXTS = {".md", ".markdown", ".json", ".jsonl", ".yaml", ".yml", ".txt", ".csv", ".tsv"}

IGNORE_TOKEN = "phi-scan: ignore"

# Oncology acronyms that commonly appear in ALL-CAPS comma ALL-CAPS form
# (society guidelines, trial-family lists, common abbreviations). When BOTH
# tokens of an all_caps_name match are in this set, the hit is suppressed —
# `NCCN, ESMO` and `TATTON, SAVANNAH` are not patient names.
ONCOLOGY_ACRONYM_ALLOWLIST = frozenset({
    # Societies / regulators / guidelines
    "NCCN", "ESMO", "ASCO", "ASH", "IASLC", "AACR", "AUA", "EAU", "ASTRO",
    "FDA", "EMA", "MHRA", "PMDA", "NMPA", "TGA", "CDC", "NIH", "NCI", "WHO",
    "OECD", "RECIST", "ECOG", "RECIST", "CTCAE", "MCBS",
    # Statistical / methodology
    "RCT", "ITT", "SR", "MA", "SAE", "ROBI", "ROB",
    # Common trial-family acronyms (NSCLC + adjacent — extend as needed)
    "TATTON", "SAVANNAH", "SACHI", "SAFFRON", "CHRYSALIS", "MARIPOSA",
    "PAPILLON", "HERTHENA", "DESTINY", "CHECKMATE", "KEYNOTE", "ADAURA",
    "FLAURA", "AURA", "LIBRETTO", "LUMINOSITY", "INSIGHT", "VISION",
    # Sarcoma + DLL3 + adjacent trials
    "CABONE", "REGOBONE", "SARC", "AOST", "DELLPHI", "DAREON", "TAHOE",
    "TRINITY", "MERU",
    # Tumor / pathology acronyms (DLL3 + PRAME pipelines)
    "SCLC", "NSCLC", "NEC", "LCNEC", "NEPC", "GEP", "MTC", "EP",
    # Hematologic + non-solid (PRAME pipeline overlap)
    "AML", "MDS", "ALL", "CLL", "CML", "DLBCL", "FL", "HL", "MM",
    # PRAME / TCR / ImmTAC platform / mechanism
    "PRAME", "TCR", "TCER", "HLA",
    # Geographies (regions / countries, frequent in access guides)
    "US", "EU", "UK", "AU", "JP",
    # Drug-class / mechanism modality acronyms
    "BITE", "CAR", "ADC", "DXD", "PBD", "TOP",
    # Pipeline-program tokens that surface in narrative
    "INN", "USAN", "GVHD",
    # Genomics / pathology
    "TCGA", "MSI", "TMB", "MMR", "HRD", "GIST", "TPS",
    # Misc oncology / pharm
    "CAR", "ADC", "TKI", "DXD", "PROTAC", "IO", "IND", "BLA", "ORR",
    "PFS", "OS", "DCR", "DOR", "TTR", "PR", "CR", "SD", "PD", "NE",
    "BICR", "IRC", "AE", "TRAE", "SAE", "DLT", "MTD", "RP2D",
    # Toxicity / AE acronyms
    "CRS", "ILD", "ICANS", "VTE", "DVT", "PE", "AKI", "GI", "HFS",
    "HTN", "QTC", "LVEF", "LFT", "AST", "ALT", "ANC", "WBC", "BUN",
    "PMID", "DOI", "NCT", "CDX", "IHC", "FISH", "NGS", "RNA", "DNA",
    "MRNA", "LNCRNA", "PDX", "WES", "WGS", "FFPE", "EHR", "CTDNA",
    "EGFR", "MET", "KRAS", "BRAF", "ALK", "ROS", "RET", "NTRK", "FGFR",
    "PD", "PDL", "HER",
})

ALL_CAPS_PAIR_RE = re.compile(r"\b([A-Z][A-Z]+),\s*([A-Z][A-Z]+)\b")


def list_tree_files(root: Path) -> list[Path]:
    out = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=root,
        capture_output=True,
        text=True,
        check=True,
    )
    return [root / line for line in out.stdout.splitlines() if line.strip()]


def list_staged_files(root: Path) -> list[Path]:
    out = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
        cwd=root,
        capture_output=True,
        text=True,
        check=True,
    )
    return [root / line for line in out.stdout.splitlines() if line.strip()]


def is_under_case_dir(path: Path, root: Path) -> bool:
    try:
        rel = path.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return rel.parts and rel.parts[0] == "case"


def all_caps_pair_is_phi(line: str) -> bool:
    """Return True if any ALL-CAPS, ALL-CAPS pair on the line has at least one
    token outside the oncology-acronym allowlist (i.e. plausibly a name)."""
    for m in ALL_CAPS_PAIR_RE.finditer(line):
        a, b = m.group(1), m.group(2)
        if a not in ONCOLOGY_ACRONYM_ALLOWLIST or b not in ONCOLOGY_ACRONYM_ALLOWLIST:
            return True
    return False


# Files where structured manufacturer / trial / lab contact information and
# row-verification dates are surfaced by design. The accessibility report's
# whole purpose is to publish phone numbers, emails, and last-verified dates
# so a treating team can dial them. The target-validation files do the same
# for assay providers — they list reference labs (LabCorp, Foundation
# Medicine, Mayo Labs, etc.) with toll-free customer-service numbers and
# test-info URLs so a clinician can route a sample. PHI patterns are still
# meaningful inside such files — they just shift to the patterns that
# genuinely indicate patient identifiers (MRN, SSN, ALL-CAPS NAME pairs)
# rather than the patterns that legitimately match published business
# contacts.
_BYDESIGN_NAMES = {
    "accessibility.md",
    "accessibility.jsonl",
    "target_validation.md",
    "target_validation.jsonl",
    "target_validation_report.md",
}
_BYDESIGN_LABELS = {"email", "us_phone", "iso_date_full"}


def _is_bydesign_artifact(path: Path) -> bool:
    return path.name in _BYDESIGN_NAMES


# Marker pairs that bracket sections where business-contact patterns
# (us_phone, email, iso_date_full) are surfaced by design — used inside
# index.md, where the rest of the file should still be PHI-scanned strictly.
_BYDESIGN_REGION_MARKERS = (
    ("<!-- libby:target-validation:begin -->", "<!-- libby:target-validation:end -->"),
    ("<!-- libby:accessibility:begin -->", "<!-- libby:accessibility:end -->"),
)


def scan_file(path: Path) -> list[tuple[int, str, str, str]]:
    """Return (lineno, label, description, line) for each hit."""
    if path.suffix.lower() not in SCAN_EXTS:
        return []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except (FileNotFoundError, IsADirectoryError, PermissionError):
        return []
    file_level_suppress = _BYDESIGN_LABELS if _is_bydesign_artifact(path) else set()
    hits: list[tuple[int, str, str, str]] = []
    in_bydesign_region = False
    region_end_marker: str | None = None
    for lineno, line in enumerate(text.splitlines(), start=1):
        if IGNORE_TOKEN in line:
            # Toggle region state if a marker appears even on an ignored line.
            for begin, end in _BYDESIGN_REGION_MARKERS:
                if begin in line:
                    in_bydesign_region = True
                    region_end_marker = end
                if end in line:
                    in_bydesign_region = False
                    region_end_marker = None
            continue
        if not in_bydesign_region:
            for begin, _end in _BYDESIGN_REGION_MARKERS:
                if begin in line:
                    in_bydesign_region = True
                    region_end_marker = _end
                    break
        suppress_labels = file_level_suppress | (_BYDESIGN_LABELS if in_bydesign_region else set())
        for label, pattern, description in PATTERNS:
            if label in suppress_labels:
                continue
            if not pattern.search(line):
                continue
            if label == "all_caps_name" and not all_caps_pair_is_phi(line):
                continue
            hits.append((lineno, label, description, line.rstrip()))
        if in_bydesign_region and region_end_marker and region_end_marker in line:
            in_bydesign_region = False
            region_end_marker = None
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan repo files for PHI-shaped strings.")
    parser.add_argument(
        "--mode",
        choices=["staged", "tree", "files"],
        required=True,
        help="What set of files to scan.",
    )
    parser.add_argument("paths", nargs="*", help="File paths (mode=files only).")
    parser.add_argument(
        "--root",
        default=".",
        help="Repo root (default: cwd).",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()

    if args.mode == "staged":
        # Always block staged paths under case/ outright.
        staged = list_staged_files(root)
        case_violations = [p for p in staged if is_under_case_dir(p, root)]
        if case_violations:
            print(
                "PHI-scan: refusing to commit — paths under case/ are gitignored "
                "PHI territory and must never enter version control:",
                file=sys.stderr,
            )
            for p in case_violations:
                print(f"  - {p.relative_to(root)}", file=sys.stderr)
            return 2
        files = staged
    elif args.mode == "tree":
        files = list_tree_files(root)
    else:
        files = [Path(p).resolve() for p in args.paths]

    total_hits = 0
    for path in files:
        if not path.exists() or not path.is_file():
            continue
        if is_under_case_dir(path, root):
            # case/ files are gitignored; if they're staged that's caught above.
            # Don't bother scanning local-only PHI here.
            continue
        hits = scan_file(path)
        if hits:
            try:
                rel = path.relative_to(root)
            except ValueError:
                rel = path
            print(f"PHI-scan hit: {rel}", file=sys.stderr)
            for lineno, label, description, line in hits:
                print(
                    f"  line {lineno} [{label}] {description}\n      {line}",
                    file=sys.stderr,
                )
            total_hits += len(hits)

    if total_hits:
        print(
            f"\nPHI-scan: {total_hits} hit(s). Refusing. "
            f"To override a single line, append a `# {IGNORE_TOKEN}` comment.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
