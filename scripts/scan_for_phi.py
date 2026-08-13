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
        # Per-alternative word boundaries: the dotted form D.O.B. ends in a
        # literal '.', so a trailing \b would never align after it (dot is a
        # non-word char) and the label would slip through. Anchor \b only where
        # a word char actually ends the token.
        re.compile(r"\b(?:DOB\b|D\.O\.B\.|Date of Birth\b)", re.IGNORECASE),
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
SCAN_EXTS = {".md", ".markdown", ".json", ".jsonl", ".yaml", ".yml", ".txt", ".csv", ".tsv", ".html"}

IGNORE_TOKEN = "phi-scan: ignore"

# Oncology acronyms that commonly appear in ALL-CAPS comma ALL-CAPS form
# (society guidelines, trial-family lists, common abbreviations). When BOTH
# tokens of an all_caps_name match are in this set, the hit is suppressed —
# `NCCN, ESMO` and `TATTON, SAVANNAH` are not patient names.
ONCOLOGY_ACRONYM_ALLOWLIST = frozenset({
    # Societies / regulators / guidelines
    "NCCN", "ESMO", "ASCO", "ASH", "IASLC", "AACR", "AUA", "EAU", "ASTRO",
    # Societies whose guidelines the standard_of_care_screener cites by name;
    # they appear in runs of society acronyms ("ASH, EHA, ASTRO, SITC") that
    # otherwise read as a NAME, NAME pair.
    "EHA", "SITC", "AASLD",
    # European LeukemiaNet — the AML guideline body the concensusite cites in
    # runs like "NCCN, ELN, and ASH converge", which read as a NAME, NAME pair.
    "ELN",
    # All-caps clinician credential that trails a ClinicalTrials.gov central-contact
    # name (e.g. "Fahmida Hoq, MBBS, MS") and reads as a NAME, NAME pair with the
    # adjacent "MS". Added minimally; extend with other all-caps postnominals only
    # as real contact rows surface them.
    "MBBS",
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
    "AML", "MDS", "ALL", "CLL", "CML", "CMML", "DLBCL", "FL", "HL", "MM",
    # Tumor-type acronyms in the selected-biomarker panel's cancer_relevance prose
    # (data/reference/selected_biomarker_panel.json)
    "ESCC", "MCL",
    # AML / MDS regimens, transplant conditioning, and drug shorthands
    # (relapsed/refractory AML + allo-HCT vocabulary)
    "FLAG", "IDA", "FLAGIDA", "GO", "CMA", "TBI", "ATG", "RIC", "MAC",
    # All-caps trade names / product codes in accessibility alias lists
    # (e.g. "MYLOTARG, CMA-676", "DECNUPAZ, PVEK", "ADSPAM, MT-401-OTS")
    "MYLOTARG", "DECNUPAZ", "PVEK", "ADSPAM",
    # Pancreatic adenocarcinoma vocabulary: tumor type, trial families, drug
    # codes, effector mechanisms, ADC payloads, and cell lines that appear as
    # comma-separated all-caps pairs in PDAC case prose (e.g. "PDAC, NAPOLI-3",
    # "SPOTLIGHT, GLOW", "ADCC, CDC", "ADC, MMAE", "KEYTRUDA, MK-3475",
    # "PDAC, ELI-002", "PDAC, FG-M108", "HPAF-II, HPAC").
    #
    # Entries are the tokens ALL_CAPS_PAIR_RE actually yields: its character
    # class is [A-Z][A-Z]+, so hyphens and digits terminate the match and a
    # product code like "ELI-002" must be allowlisted as "ELI", not in full.
    #
    # Allowlisting affects only the ALL-CAPS name heuristic. Date, email, and
    # phone detection are untouched, and a genuine surname pair still flags,
    # because every token in a pair must be allowlisted for it to be cleared.
    "PDAC", "NAPOLI", "SPOTLIGHT", "GLOW", "GLEAM", "PYNNACLE",
    "ADCC", "CDC", "ADC", "MMAE", "KEYTRUDA", "MK",
    "ELI", "FG", "HPAF", "HPAC", "CLDN", "VYLOY", "VENTANA",
    "FLAMSA", "DLI", "GVHD", "GVL", "HCT", "HSCT", "NRM", "VOD", "SOS",
    "MRD", "LSC", "HMA", "AZA", "DEC", "CPX", "MEC", "HIDAC", "CLAG",
    "NPM", "CEBPA", "DNMT", "TET", "ASXL", "RUNX", "MECOM", "EVI",
    "KMT", "IDH", "FLT", "BPDCN", "TCR", "MHAG", "STR",
    # MDS subtype / prognostic-score / assay acronyms + AML trial families
    "RCMD", "IPSS", "RARS", "RAEB", "LOD", "CNV", "VAF", "PYNNACLE",
    "CBX", "TCRM", "TCE", "CG", "TRD",
    # Oncology trial-family acronyms surfaced by the re-run (avoid NAME,NAME false positives)
    "MATAO", "PARAGON", "DENALI", "FALCON", "MOONRAY", "KONQUER", "PRIMROSE",
    "PRIMAVERA", "REGOBONE", "CABONE", "ATHENA", "HERIZON", "FOENIX", "FIGHT",
    "CLARIDHY", "ROAR", "KRYSTAL", "MOUNTAINEER", "REFOCUS", "VIOLETTE", "PETRA",
    "PLASMAMATCH", "REDISCOVER", "MOUNTAINTAP", "SURVIVE", "MATRIX", "DRUP",
    "PANTUMOR", "PANTUMOUR", "REFOCUS", "HERTHENA", "DELLPHI", "MERU", "FORTRAS",
    "CROSSCHECK", "ALLOHA", "MOUNTAINTAP", "AUGMENT", "COMET", "PYNNACLE",
    # ClinicalTrials.gov recruitment-status tokens that appear in agent run-log notes
    "RECRUITING", "ENROLLING", "SUSPENDED", "WITHHELD", "AVAILABLE",
    # ADC payloads / drug-modality + disease-subsite acronyms in rendered tables
    "MMAE", "MMAF", "DM1", "DM4", "SN38", "ICC", "ECC", "BTC", "GEA",
    "SIERRA", "ALLOHA", "AUGMENT",
    # PRAME / TCR / ImmTAC platform / mechanism
    "PRAME", "TCR", "TCER", "HLA",
    # Geographies (regions / countries, frequent in access guides)
    "US", "EU", "UK", "AU", "JP",
    # Roman numerals adjacent to gene / complex / grade tokens in mechanism prose
    # (e.g. "complex II, SDH-deficient", "grade III"); only suppresses a pair when
    # the other token is also allowlisted, so a real surname pair still flags.
    "II", "III", "VI", "VII",
    # Drug-class / mechanism modality acronyms
    "BITE", "CAR", "ADC", "DXD", "PBD", "TOP",
    # Pipeline-program tokens that surface in narrative
    "INN", "USAN", "GVHD",
    # Genomics / pathology
    "TCGA", "MSI", "TMB", "MMR", "HRD", "GIST", "TPS",
    # Misc oncology / pharm
    "CAR", "ADC", "TKI", "DXD", "PROTAC", "IO", "IND", "BLA", "ORR",
    "PFS", "OS", "DCR", "DOR", "TTR", "PR", "CR", "SD", "PD", "NE",
    "PK", "PKPD", "TEAE", "TRAE",
    "BICR", "IRC", "AE", "TRAE", "SAE", "DLT", "MTD", "RP2D",
    # Trial-stage / dose-finding shorthands + control-arm trial names in rendered tables
    "FIH", "RDE", "RDD", "MABEL", "MPACT", "MABEL",
    # Toxicity / AE acronyms
    "CRS", "ILD", "ICANS", "VTE", "DVT", "PE", "AKI", "GI", "HFS",
    "HTN", "QTC", "LVEF", "LFT", "AST", "ALT", "ANC", "WBC", "BUN",
    "PMID", "DOI", "NCT", "CDX", "IHC", "ISH", "FISH", "NGS", "RNA", "DNA",
    "MRNA", "LNCRNA", "PDX", "WES", "WGS", "FFPE", "EHR", "CTDNA",
    "EGFR", "MET", "KRAS", "BRAF", "ALK", "ROS", "RET", "NTRK", "FGFR",
    "PD", "PDL", "HER",
    # RAS isoforms, kinases, MAPK pathway
    "NRAS", "HRAS", "RAS", "RAF", "MEK", "ERK", "MAPK", "SOS", "GEF",
    "GAP", "GTP", "GDP", "SHP", "FAK", "CDK", "CDKN", "MYC", "AKT", "PI3K",
    "MTOR", "MOA",
    # Tumor-type acronyms / histology
    "PDAC", "GBM", "TNBC", "HCC", "RCC", "CRC", "HNSCC", "LGSOC", "HGSOC",
    "UM", "DIPG",
    # Sarcoma (uLMS) case vocabulary that surfaces in ALL-CAPS pairs across the
    # rendered pages: histology shorthands ("LMS, ECOG"; "MRCLS, HLA"), the
    # ESTRO society in the ESC cardio-oncology byline ("EHA, ESTRO"), the
    # cancer/testis antigen family ("PRAME, MAGE"), lab panels ("CK, CBC"),
    # imaging and sponsor tokens ("CT, LLC"), HRR/HRD panel prose ("HRR, TMB"),
    # skin-histology pairs in access guides ("CSCC, BCC"), and the nucleotide
    # excision repair gene family in the trabectedin mechanism rows
    # ("CSB, XPA"; "XPC, XPD"; "XPF, XPG"). Both tokens of a pair must be
    # allowlisted, so genuine surname pairs still flag.
    "LMS", "ULMS", "MRCLS", "ASPS", "ESTRO", "MAGE", "CK", "CBC", "CT", "LLC",
    "HRR", "CSCC", "BCC", "CSB", "XPA", "XPC", "XPD", "XPF", "XPG",
    # Drug class / mechanism extensions
    "HCQ", "PARP", "PARPi", "TKI", "ICI", "ICB", "FAP", "CAF", "MDSC", "TIL",
    "MRD",
    # Cancer-syndrome / risk acronyms
    "LFS", "HBOC", "HNPCC", "MAP", "FAP",
    # Methodology / metrology
    "HRD", "LOH", "ROBINS", "ROB", "GRADE", "PICO",
    # Mouse-model strains that surface in preclinical evidence
    "KPC", "KPP", "GEMM",
    # Trial-family names (PDAC + adjacent)
    "POLO", "NEJM", "JCO",
    # Outcome / endpoint shorthand
    "RFS", "DFS", "EFS", "TTR", "TTP", "TTNT", "HR", "MSS",
    # Journal abbreviations occasionally cited in agent prose
    "CCR", "STTT",
    # SoC PDAC chemo regimen names that read as ALL-CAPS
    "FOLFIRINOX", "NALIRIFOX", "FOLFOX", "FOLFIRI",
    # Misc pancreatic-trial-family + adjacent acronyms
    "MTAP", "PRMT", "SHP",
    # GIST + SDH-deficient GIST vocabulary
    "GIST", "SDH", "SDHA", "SDHB", "SDHC", "SDHD", "SDHAF", "SDHAF2",
    "KIT", "PDGFRA", "DOG", "MGMT", "VHL", "MAX", "VAF", "WT",
    # Paraganglioma / pheochromocytoma syndromes + adjacent
    "PPGL", "PCC", "HLRCC", "PGL",
    # Trial families surfaced by GIST + dSDH-GIST literature
    "LITESPARK", "PEMIGIST", "GRID", "INVICTUS", "SOLAR", "INVAGO",
    "MEGALIT", "INAVO",
    # Adjuvant-GIST RCT acronyms (Z9001 / SSGXVIII / PERSIST-5)
    "SSGXVIII", "PERSIST",
    # Drug shorthands / brand names + tool compounds that appear as ALL-CAPS
    "TMZ", "TEMODAR", "TEMODAL", "BPTES",
    # Institutions + cancer centers
    "DFCI", "UCLA", "UCSD", "UCSF", "MSK", "MSKCC", "MDACC", "BWH",
    "MGH", "FHCC", "FCCC",
    # Statistical / readout shorthand
    "CI", "RR", "BR",
    # Misc histology / tumor-type acronyms
    "ATC", "PTC", "FTC",
    # Common physiology / lab labels
    "TSH", "BP", "ECG", "EKG", "CBC", "BMP", "CMP", "EDTA",
    # Genes / proteins that appear as ALL-CAPS in agent prose
    "VEGFA", "VEGFR", "VEGF", "EPO", "HIF", "IGF",
    # Administration-route shorthand (intravenous / intraperitoneal)
    "IV", "IP",
    # Genomic-instability-score shorthand (PAOLA-1 HRD companion-diagnostic)
    "GIS",
    # TNBC + breast vocabulary (BRCA / HRD / PARP-i adjacent)
    "BRCA", "PALB", "ATM", "ATR", "CHK", "BARD", "RAD", "BRIP", "CHEK",
    "CDK", "CDK12", "CCNE", "CCNE1", "PTEN", "PIK3CA", "TP53", "AKT",
    "DDR", "ITWG", "TIL", "TILS", "TIRC", "CPS", "TPS",
    # TNBC trial families
    "MEDIOLA", "TOPACIO", "DORA", "EMBRACA", "OLYMPIAD", "OLYMPIA",
    "ASCENT", "TROPION", "KEYLYNK", "TROFUSE", "IMPASSION", "NRG", "SABR",
    "BRAVO", "EORTC", "TNT", "CRUK", "BROCADE", "CAPITELLO", "EPIK",
    # PDX label / drug class extension
    "TMT", "MK", "TPC", "SN", "SGS", "DXD",
    # Targets / receptors common in TNBC + breast
    "TROP", "TROP2", "DLL", "HLA", "B2M",
    # Imaging / pathology
    "FISH", "PFTS", "HRCT", "MRI", "CT",
    # Radiation oncology / interventional radiology procedural acronyms
    "SBRT", "SBRS", "SABR", "IR", "IORT", "EBRT", "IMRT", "VMAT",
    # Hormone-receptor acronyms (breast)
    "ER", "PR", "HR",
    # US state postal codes (common in trial-site geography lists)
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI",
    "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI",
    "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC",
    "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT",
    "VT", "VA", "WA", "WV", "WI", "WY", "DC",
    # GBM / neuro-oncology vocabulary (CNS WHO classification, trial families,
    # performance status, gene names, ADC payloads, PD biomarkers)
    "HGG", "LGG", "KPS", "MSP", "SDMA", "MMAF", "MPNST", "GEJ",
    "ATRX", "IDH", "CSF", "CNS", "RT", "PI", "AM",
    "AGILE", "ROAR", "SURVIVE", "INCIPIENT", "EANO", "PVSRIPO",
    "INTELLANCE", "BRAIN",
    # CCTG trial-identifier prefix tokens (CCTG CE.6 elderly GBM hypofractionated)
    "CE",
    # mCRC + peritoneal-disease vocabulary (atypical-KRAS / PIK3CA / CRS-HIPEC cases)
    # Tumor markers
    "CEA", "CA",
    # Trial families / RCT acronyms surfaced in mCRC literature
    "CRYSTAL", "PRIME", "OPUS", "FIRE", "VII", "MRC", "NORDIC", "COIN",
    "PEAK", "CALGB", "SWOG", "TRIBE", "MAVERICC", "BICC", "BEACON",
    "AVF", "AVF2107", "RAISE", "VELOUR", "SUNLIGHT", "FRESCO", "CORRECT",
    "CONCUR", "CAIRO", "PRODIGE", "COLOPEC", "PROPHYLOCHIP", "EFFIPEC",
    "RASOLVE", "KRYSTAL", "CODEBREAK", "DESTINY", "MOUNTAINEER", "HERACLES",
    "INTRINSIC", "INAVO120", "ASCEND", "BATTMAN", "ALASCCA", "PYNNACLE",
    "OLYMPIA", "OPTIMOX", "INVAGO",
    # Cohort / epidemiology study acronyms
    "NHS", "HPFS",
    # RNA-seq / transcriptomic profiling
    "WTS", "WTX", "CMS", "RNASEQ",
    # Mouse-model and PDX strain vocabulary
    "KPF",
    # Hematologic abbreviations alongside MM (already in)
    "NHL",
    # MAPK / RAS pathway descriptors
    "LOF", "GOF",
    # Tumor-type acronyms specific to mCRC neighborhood
    "BTC", "NEPC", "GEC",
    # Pancreatic / biliary / GU acronyms occasionally cited cross-tumor
    "PIPAC",
    # Disease-phenotype shorthands surfaced in mCRC peritoneal-disease prose
    "NLM", "LM", "PCI",
    # ICI / immunotherapy combo / agent shorthands
    "BOT", "BAL", "EAP", "FMD", "ICI",
    # Pharmacogenomics / dosing
    "DPYD", "UGT", "UGT1A1", "CPIC",
    # Cancer-related genes appearing in ALL-CAPS prose
    "APC", "MUTYH", "POLE", "POLD", "SMAD", "ERBB", "BCL2L1", "TOP1",
    "AURKA", "MYBL", "ZNF217", "CDX",
    # Replication-fork-protection / DNA-repair genes in preclinical-horizon prose
    "TIMELESS", "TIPIN", "CLASPIN",
    # Lynch-syndrome / hereditary CRC germline panel genes
    "EPCAM",
    # Treatment-arm / clinical-shorthand vocabulary
    "BSC",
    # Institutions / cancer-center acronyms not yet listed
    "USC", "UPMC",
    # Trial-program / cancer-network tokens
    "NRG", "CCTG", "NEXT", "AACR",
    # Procedure / regimen tokens
    "CRS", "HIPEC", "SBRT", "PIPAC",
    # Chemo backbone acronyms used in mCRC
    "FOLFOXIRI",
    # Quality-of-life / scoring instruments
    "TTR",
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


# Guideline releases are cited with day precision by design ("NCCN AML
# v3.2026 (11/24/2025)", "Version 3.2026 (11/24/2025)") — a publication date
# of a versioned guideline text, not a patient date. Suppress a us_date hit
# only when EVERY day-precision date on the line sits inside such a
# version-parenthetical; a real clinical date elsewhere on the line still flags.
_GUIDELINE_VERSION_PREFIX_RE = re.compile(
    r"(?:[Vv]ersion\s+|\bv)\d+\.\d{4}\s*\(\s*(?:the\s+)?$"
)
_US_DATE_RE = re.compile(r"\b\d{1,2}/\d{1,2}/(?:19|20)\d{2}\b")


def us_dates_are_guideline_versions(line: str) -> bool:
    """Return True if every day-precision US date on the line is the
    publication date inside a guideline-version parenthetical."""
    matches = list(_US_DATE_RE.finditer(line))
    if not matches:
        return False
    return all(
        _GUIDELINE_VERSION_PREFIX_RE.search(line[: m.start()]) for m in matches
    )


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
    # The standard-of-care track carries a mandatory `last_verified_utc` on every
    # row, plus guideline versions and approval dates inside the endorsement
    # entries. Those dates are the point of the artifact: a standard-of-care claim
    # that cannot be re-checked against the version it came from is worthless, and
    # guidelines move several times a year. Same rationale as `accessibility.jsonl`
    # — patient-identifier patterns (MRN, SSN, ALL-CAPS NAME pairs) still scan here.
    "standard_of_care.md",
    "standard_of_care.jsonl",
    "standard_of_care_report.md",
    # The standard-of-care track carries a mandatory `last_verified_utc` on every
    # row, plus guideline versions and approval dates inside the endorsement
    # entries. Those dates are the point of the artifact: a standard-of-care claim
    # that cannot be re-checked against the version it came from is worthless, and
    # guidelines move several times a year. Same rationale as `accessibility.jsonl`
    # — patient-identifier patterns (MRN, SSN, ALL-CAPS NAME pairs) still scan here.
    "standard_of_care.md",
    "standard_of_care.jsonl",
    "standard_of_care_report.md",
    # The reporter's executive summary is a synthesis of `index.md` and may
    # surface the same sponsor-inquiry email / phone (e.g. `medinfo@revmed.com`
    # / `1-844-2-REVMED`) the PI inlined for the load-bearing single phone
    # call on the case. Same rationale as `index.md`: PHI patterns that
    # indicate patient identifiers still scan; only `_BYDESIGN_LABELS`
    # (us_phone, email, iso_date_full) are suppressed.
    "executive_summary.md",
    # `runs.jsonl` is the per-case agent-run log; its whole purpose is to
    # record `run_id` strings and `timestamp_utc` ISO timestamps with day
    # precision. These look like PHI dates to the regex but are by design.
    "runs.jsonl",
    # The clinical / preclinical evidence JSONLs carry `last_author_contact`
    # emails by design — the clinician / researcher contracts treat
    # corresponding-author emails (lifted from published papers) as part of
    # the reviewer hand-off. These are public business contacts, not PHI.
    "clinical_evidence.jsonl",
    "preclinical_evidence.jsonl",
    # The PI-authored clinician dossier (`index.md`), the deterministic
    # recommendations table (`recommendations.md`), the board proceedings
    # (`board.md`), and the upstream recommendations / board JSONLs inline
    # published business contacts (lab customer-service phones, trial-sponsor
    # contact emails, navigator phone numbers) inside prose that explains how
    # to actually order the workup or screen for the named trial. Same
    # rationale as `accessibility.md`: PHI patterns that indicate patient
    # identifiers (MRN, SSN, ALL-CAPS NAME pairs) still scan; only
    # `_BYDESIGN_LABELS` (us_phone, email, iso_date_full) are suppressed.
    "index.md",
    "recommendations.md",
    "recommendations.jsonl",
    "board.md",
    # The persona-authored board JSONLs (positions.jsonl, critiques.jsonl)
    # surface trial-navigator phones and sponsor medical-info emails inside
    # rationale prose by design — same rationale as `board.md` and
    # `recommendations.md`. PHI patterns that indicate patient identifiers
    # (MRN, SSN, ALL-CAPS NAME pairs) still scan; only `_BYDESIGN_LABELS`
    # (us_phone, email, iso_date_full) are suppressed.
    "positions.jsonl",
    "critiques.jsonl",
    # Vendored agent-skill docs (`.claude/skills/*/SKILL.md`) are developer
    # material, never patient data. They carry API-etiquette contact params by
    # design — the reference_checking skill embeds a `&email=` NCBI eutils /
    # CrossRef mailto so PubMed identifies the caller. Patient identifiers (MRN,
    # SSN, DOB, ALL-CAPS NAME pairs) still scan; only `_BYDESIGN_LABELS`
    # (us_phone, email, iso_date_full) are suppressed.
    "SKILL.md",
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

# Section-heading markers that open a by-design region in `index.md` until
# the next H2 (`## `) heading or EOF. The PI's Run log section records
# day-precision authoring timestamps by design (same rationale as
# `runs.jsonl`); the date is an agent-run identifier, not patient PHI.
_BYDESIGN_HEADING_OPENERS = ("## Run log",)


def scan_file(path: Path) -> list[tuple[int, str, str, str]]:
    """Return (lineno, label, description, line) for each hit."""
    if path.suffix.lower() not in SCAN_EXTS:
        return []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except (FileNotFoundError, IsADirectoryError, PermissionError):
        return []
    file_level_suppress = _BYDESIGN_LABELS if _is_bydesign_artifact(path) else set()
    # Self-contained .html/.pdf report downloads (e.g. <slug>-accessibility.html)
    # are deterministic renders of pages that surface business contacts and
    # authoring dates by design — the same labels the markdown by-design regions
    # suppress. Suppress those labels file-wide for HTML; hard patient identifiers
    # (ssn / mrn_label / dob_label / patient_label / all_caps_name) still scan.
    if path.suffix.lower() == ".html":
        file_level_suppress = file_level_suppress | _BYDESIGN_LABELS
    # runs.jsonl is agent-authored process telemetry written AFTER the intake
    # scrub — it never carries patient identifiers, but its free-text notes are
    # dense with ALL-CAPS oncology acronym lists (e.g. "AML PDX, CBX", "GBM,
    # RECRUITING") that trip the NAME,NAME heuristic. Suppress that one label
    # here; MRN/SSN/labeled-DOB/patient-name-label patterns still scan.
    if path.name == "runs.jsonl":
        file_level_suppress = file_level_suppress | {"all_caps_name"}
    hits: list[tuple[int, str, str, str]] = []
    in_bydesign_region = False
    region_end_marker: str | None = None
    in_bydesign_heading = False
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
        # Heading-bracketed by-design region: opens on a known H2, closes
        # on the next H2 (or EOF). The opener line itself is in-region.
        stripped = line.lstrip()
        if stripped.startswith("## "):
            in_bydesign_heading = any(
                stripped.startswith(opener) for opener in _BYDESIGN_HEADING_OPENERS
            )
        if not in_bydesign_region:
            for begin, _end in _BYDESIGN_REGION_MARKERS:
                if begin in line:
                    in_bydesign_region = True
                    region_end_marker = _end
                    break
        suppress_labels = file_level_suppress | (
            _BYDESIGN_LABELS if (in_bydesign_region or in_bydesign_heading) else set()
        )
        for label, pattern, description in PATTERNS:
            if label in suppress_labels:
                continue
            if not pattern.search(line):
                continue
            if label == "all_caps_name" and not all_caps_pair_is_phi(line):
                continue
            if label == "us_date" and us_dates_are_guideline_versions(line):
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
    parser.add_argument(
        "--include-case",
        action="store_true",
        help=(
            "Scan explicitly-named paths under case/ (mode=files only). Used by "
            "promote_profile.py to actually scan the scrubbed profile before it is "
            "promoted. tree/staged modes always skip case/ regardless of this flag."
        ),
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    scan_case_paths = args.include_case and args.mode == "files"

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
        if is_under_case_dir(path, root) and not scan_case_paths:
            # case/ files are gitignored; if they're staged that's caught above.
            # In tree/staged mode there's no reason to scan local-only PHI here.
            # promote_profile.py passes --include-case so the scrubbed profile IS
            # scanned before it crosses into committed territory.
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
