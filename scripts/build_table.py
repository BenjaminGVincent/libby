#!/usr/bin/env python3
"""Render data/cases/<slug>/trials.jsonl into docs/cases/<slug>/trials.md.

Uses the vendored trial-table style (21 canonical columns) plus three Libby
additions: Fit, Toxicity flags, Inclusion notes.

Pure-Python; no LLM, no external deps.
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows


def collapse_supersedes(rows: list[dict]) -> list[dict]:
    """Drop any row whose row_id is targeted by a `supersedes` field on a later row."""
    superseded = {r.get("supersedes") for r in rows if r.get("supersedes")}
    return [r for r in rows if r.get("row_id") not in superseded]


def fmt(value, dash: str = "—") -> str:
    if value is None or value == "":
        return dash
    return html.escape(str(value))


def num_fmt(value, places: int = 2, dash: str = "—") -> str:
    if value is None or value == "":
        return dash
    try:
        return f"{float(value):.{places}f}"
    except (TypeError, ValueError):
        return html.escape(str(value))


def link_pmid(pmid) -> str:
    if pmid in (None, "", "—"):
        return "—"
    return f'<a href="https://pubmed.ncbi.nlm.nih.gov/{html.escape(str(pmid))}">{html.escape(str(pmid))}</a>'


def link_doi(doi) -> str:
    if doi in (None, "", "—"):
        return "—"
    return f'<a href="https://doi.org/{html.escape(str(doi))}">{html.escape(str(doi))}</a>'


def fit_badge(fit: str) -> str:
    cls = {"strong": "fit-strong", "partial": "fit-partial", "weak": "fit-weak", "none": "fit-none"}
    klass = cls.get(fit, "fit-none")
    return f'<span class="fit-badge {klass}">{html.escape(str(fit or "—"))}</span>'


_TUMOR_REL_LABEL = {
    "primary_indication_match":   ("indication", "rel-indication"),
    "basket_or_biomarker_match":  ("basket",     "rel-basket"),
    "same_drug_other_indication": ("same-drug",  "rel-same-drug"),
    "cross_tumor_extrapolation":  ("cross-tumor", "rel-cross-tumor"),
}


def tumor_rel_badge(rel: str | None) -> str:
    if not rel:
        return "—"
    label, klass = _TUMOR_REL_LABEL.get(rel, (rel, "rel-other"))
    return f'<span class="rel-badge {html.escape(klass)}">{html.escape(label)}</span>'


def tox_pills(flags) -> str:
    if not flags:
        return "—"
    return " ".join(f'<span class="tox-flag">{html.escape(str(f))}</span>' for f in flags)


HEADERS = [
    ("First author",       "first_author",        "left",  False),
    ("Last author",        "last_author",         "left",  False),
    ("Year",               "year",                "right", True),
    ("Journal",            "journal",             "left",  False),
    ("NCT",                "nct_id",              "left",  False),
    ("Phase",              "phase",               "left",  False),
    ("Indication",         "indication",          "left",  False),
    ("Line",               "line",                "left",  False),
    ("Biomarker",          "biomarker",           "left",  False),
    ("n",                  "n",                   "right", True),
    ("Design",             "design",              "left",  False),
    ("Intervention",       "intervention",        "left",  False),
    ("Comparator",         "comparator",          "left",  False),
    ("Endpoint",           "endpoint",            "left",  False),
    ("Effect",             "effect_size",         "right", True),
    ("Lower CI",           "ci_lower",            "right", True),
    ("Upper CI",           "ci_upper",            "right", True),
    ("p",                  "p_value",             "right", True),
    ("Quality",            "quality",             "left",  False),
    ("PMID",               "pmid",                "left",  False),
    ("DOI",                "doi",                 "left",  False),
    ("Fit",                "fit_to_case",         "left",  False),
    ("Tumor-type relation","tumor_type_relationship", "left", False),
    ("Modality",           "modality",            "left",  False),
    ("Dev status",         "development_status",  "left",  False),
    ("Sponsor",            "sponsor",             "left",  False),
    ("Toxicity flags",     "toxicity_flags",      "left",  False),
    ("Inclusion notes",    "inclusion_match_notes", "left", False),
]


def dev_status_badge(status: str | None) -> str:
    if not status:
        return "—"
    pretty = status.replace("_", " ")
    cls_map = {
        "approved": "fit-strong",
        "phase_3_active": "fit-strong",
        "phase_2_active": "fit-partial",
        "phase_1_active": "fit-partial",
        "ind_cleared_pre_phase_1": "fit-weak",
        "discontinued": "fit-none",
        "legacy_research_only": "fit-none",
    }
    cls = cls_map.get(status, "fit-none")
    return f'<span class="fit-badge {cls}">{html.escape(pretty)}</span>'


def modality_badge(mod: str | None) -> str:
    if not mod:
        return "—"
    pretty = mod.replace("_", " ")
    return f'<span class="rel-badge rel-other">{html.escape(pretty)}</span>'


def render_table(rows: list[dict]) -> str:
    head_cells = "".join(
        f'<th class="{"num" if align == "right" else ""}">{html.escape(label)}</th>'
        for label, _, align, _ in HEADERS
    )
    body_rows = []
    for r in rows:
        cells = []
        for label, key, align, _ in HEADERS:
            klass = ' class="num"' if align == "right" else ""
            if key == "pmid":
                content = link_pmid(r.get(key))
            elif key == "doi":
                content = link_doi(r.get(key))
            elif key == "fit_to_case":
                content = fit_badge(r.get(key) or "")
            elif key == "tumor_type_relationship":
                content = tumor_rel_badge(r.get(key))
            elif key == "modality":
                content = modality_badge(r.get(key))
            elif key == "development_status":
                content = dev_status_badge(r.get(key))
            elif key == "toxicity_flags":
                content = tox_pills(r.get(key) or [])
            elif key in {"effect_size", "ci_lower", "ci_upper"}:
                content = num_fmt(r.get(key), places=2)
            else:
                content = fmt(r.get(key))
            cells.append(f"<td{klass}>{content}</td>")
        body_rows.append("        <tr>" + "".join(cells) + "</tr>")
    return (
        '<div class="trial-table-wrap">\n'
        '  <div class="trial-scroll">\n'
        '    <table class="trial-table">\n'
        f'      <thead>\n        <tr>{head_cells}</tr>\n      </thead>\n'
        f'      <tbody>\n' + "\n".join(body_rows) + "\n      </tbody>\n"
        "    </table>\n"
        "  </div>\n"
        "</div>\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    args = parser.parse_args()
    slug = args.slug

    src = REPO / "data" / "cases" / slug / "trials.jsonl"
    dst = REPO / "docs" / "cases" / slug / "trials.md"
    dst.parent.mkdir(parents=True, exist_ok=True)

    rows = collapse_supersedes(load_jsonl(src))
    rows.sort(key=lambda r: (r.get("year") or 0, r.get("first_author") or ""), reverse=True)

    table_html = render_table(rows) if rows else "_No trials extracted yet._\n"

    body = (
        '<meta name="robots" content="noindex">\n\n'
        f"# Trials — `{slug}`\n\n"
        f"_{len(rows)} trials._\n\n"
        f"{table_html}\n"
        f"[Back to case](index.md) · "
        f"[Evidence](evidence.md) · [Manuscripts](manuscripts.md) · "
        f"[Target validation](target_validation.md) · "
        f"[Board](board.md) · [Recommendations](recommendations.md)\n\n"
        '!!! danger disclaimer "Decision support, not medical advice"\n'
        "    Not a substitute for clinician review. See [PHI policy](../../phi_policy.md).\n"
    )
    dst.write_text(body, encoding="utf-8")
    print(f"wrote {dst} ({len(rows)} rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
