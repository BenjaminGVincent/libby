#!/usr/bin/env python3
"""Render clinical_evidence.jsonl + preclinical_evidence.jsonl → docs/cases/<slug>/evidence.md.

Modeled on the io-shieldbreak Pharmacodynamic-Results table layout: per-manuscript
decision-relevant detail, grouped by intervention with H3 sub-headings so a clinician
scans evidence by drug rather than by paper.
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from collections import OrderedDict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def fmt(v, dash: str = "—") -> str:
    if v is None or v == "":
        return dash
    return html.escape(str(v))


def num_fmt(v, places: int = 2, dash: str = "—") -> str:
    if v is None or v == "":
        return dash
    try:
        return f"{float(v):.{places}f}"
    except (TypeError, ValueError):
        return html.escape(str(v))


def link_pmid(pmid) -> str:
    if not pmid:
        return "—"
    return f'<a href="https://pubmed.ncbi.nlm.nih.gov/{html.escape(str(pmid))}">{html.escape(str(pmid))}</a>'


def link_doi(doi) -> str:
    if not doi:
        return "—"
    return f'<a href="https://doi.org/{html.escape(str(doi))}">DOI</a>'


def author_year(r: dict) -> str:
    first = r.get("first_author") or "—"
    last = r.get("last_author") or "—"
    yr = r.get("year") or "—"
    journal = r.get("journal") or ""
    parts = [f"{html.escape(str(first))}/{html.escape(str(last))} ({yr})"]
    if journal:
        parts.append(f"<em>{html.escape(str(journal))}</em>")
    return "<br>".join(parts)


def fit_badge(label: str | None) -> str:
    if not label:
        return "—"
    cls = {
        "strong": "fit-strong",
        "partial": "fit-partial",
        "weak": "fit-weak",
        "none": "fit-none",
        "cross_tumor_only": "fit-weak",
    }.get(label, "fit-none")
    pretty = label.replace("_", " ")
    return f'<span class="fit-badge {cls}">{html.escape(pretty)}</span>'


def rob_badge(label: str | None) -> str:
    if not label or label == "n/a":
        return "—"
    severity = "ok" if "Low" in label or label.endswith(":low") else (
        "warn" if any(s in label for s in ("Some", "Moderate", "med", "informal:high")) else "bad"
    )
    klass = {"ok": "rob-low", "warn": "rob-med", "bad": "rob-high"}[severity]
    return f'<span class="rob-badge {klass}">{html.escape(label)}</span>'


def ci_cell(r: dict) -> str:
    lo, hi = r.get("ci_lower"), r.get("ci_upper")
    free = r.get("variance_or_ci")
    if lo is not None and hi is not None:
        return f"{num_fmt(lo)}–{num_fmt(hi)}"
    if free:
        return html.escape(str(free))
    return "—"


def effect_cell(r: dict) -> str:
    e = r.get("effect_size")
    units = r.get("effect_units")
    if e is None or e == "":
        return "—"
    out = num_fmt(e, places=2) if isinstance(e, (int, float)) else html.escape(str(e))
    if units:
        out += f" {html.escape(str(units))}"
    return out


CLINICAL_COLS: list[tuple[str, str]] = [
    ("Report",            "report"),
    ("n",                 "n"),
    ("Population",        "population_detail"),
    ("Line",              "line_of_therapy"),
    ("Design",            "design"),
    ("Comparator",        "comparator"),
    ("Dose / schedule",   "intervention_dose"),
    ("Endpoint",          "endpoint_type"),
    ("Outcome",           "outcome"),
    ("Effect",            "effect_cell"),
    ("CI",                "ci_cell"),
    ("p",                 "p_value"),
    ("Durability",        "median_dor_or_pfs"),
    ("Safety",            "safety_summary"),
    ("RoB",               "risk_of_bias"),
    ("Tier",              "evidence_tier"),
    ("Case fit",          "case_match"),
    ("PMID",              "pmid"),
    ("DOI",               "doi"),
    ("Notes",             "notes"),
]


def render_clinical_row(r: dict) -> str:
    cells: list[str] = []
    for label, key in CLINICAL_COLS:
        if key == "report":
            cells.append(f"<td>{author_year(r)}</td>")
        elif key == "effect_cell":
            cells.append(f'<td class="num">{effect_cell(r)}</td>')
        elif key == "ci_cell":
            cells.append(f'<td class="num">{ci_cell(r)}</td>')
        elif key == "n":
            cells.append(f'<td class="num">{fmt(r.get(key))}</td>')
        elif key == "p_value":
            cells.append(f'<td class="num">{fmt(r.get(key))}</td>')
        elif key == "pmid":
            cells.append(f"<td>{link_pmid(r.get(key))}</td>")
        elif key == "doi":
            cells.append(f"<td>{link_doi(r.get(key))}</td>")
        elif key == "case_match":
            cells.append(f"<td>{fit_badge(r.get(key))}</td>")
        elif key == "risk_of_bias":
            cells.append(f"<td>{rob_badge(r.get(key))}</td>")
        else:
            cells.append(f"<td>{fmt(r.get(key))}</td>")
    return "        <tr>" + "".join(cells) + "</tr>"


def render_clinical_table(rows: list[dict]) -> str:
    if not rows:
        return "_No clinical-evidence rows yet._\n"
    head = "".join(f"<th>{html.escape(label)}</th>" for label, _ in CLINICAL_COLS)
    body = [render_clinical_row(r) for r in rows]
    return (
        '<div class="trial-table-wrap">\n'
        '  <div class="trial-scroll">\n'
        '    <table class="trial-table">\n'
        f'      <thead><tr>{head}</tr></thead>\n'
        '      <tbody>\n' + "\n".join(body) + "\n      </tbody>\n"
        "    </table>\n"
        "  </div>\n"
        "</div>\n"
    )


def group_clinical_by_intervention(rows: list[dict]) -> "OrderedDict[str, dict]":
    """Stable ordering: by first appearance of intervention_id; rows within a group by year desc."""
    groups: "OrderedDict[str, dict]" = OrderedDict()
    for r in rows:
        iid = r.get("intervention_id") or "unknown"
        label = r.get("intervention_label") or iid
        groups.setdefault(iid, {"label": label, "rows": []})["rows"].append(r)
    for g in groups.values():
        g["rows"].sort(key=lambda r: -(r.get("year") or 0))
    return groups


PRECLINICAL_COLS: list[tuple[str, str]] = [
    ("Report",         "report"),
    ("Model",          "model_system"),
    ("n",              "n_units"),
    ("Control",        "control_arm"),
    ("Dose",           "dose_and_schedule"),
    ("Mechanism",      "mechanism"),
    ("Key finding",    "key_finding"),
    ("Effect (qual)",  "effect_size_qual"),
    ("Translatability","translatability_score"),
    ("Case fit",       "case_match"),
    ("PMID",           "pmid"),
    ("DOI",            "doi"),
    ("Caveats",        "caveats"),
]


def render_preclinical_row(r: dict) -> str:
    cells: list[str] = []
    for label, key in PRECLINICAL_COLS:
        if key == "report":
            cells.append(f"<td>{author_year(r)}</td>")
        elif key == "pmid":
            cells.append(f"<td>{link_pmid(r.get(key))}</td>")
        elif key == "doi":
            cells.append(f"<td>{link_doi(r.get(key))}</td>")
        elif key == "case_match":
            cells.append(f"<td>{fit_badge(r.get(key))}</td>")
        else:
            cells.append(f"<td>{fmt(r.get(key))}</td>")
    return "        <tr>" + "".join(cells) + "</tr>"


def render_preclinical_table(rows: list[dict]) -> str:
    if not rows:
        return "_No pre-clinical rows yet._\n"
    head = "".join(f"<th>{html.escape(label)}</th>" for label, _ in PRECLINICAL_COLS)
    body = [render_preclinical_row(r) for r in rows]
    return (
        '<div class="trial-table-wrap">\n'
        '  <div class="trial-scroll">\n'
        '    <table class="trial-table">\n'
        f'      <thead><tr>{head}</tr></thead>\n'
        '      <tbody>\n' + "\n".join(body) + "\n      </tbody>\n"
        "    </table>\n"
        "  </div>\n"
        "</div>\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    args = parser.parse_args()
    slug = args.slug

    case_dir = REPO / "data" / "cases" / slug
    clinical_all = load_jsonl(case_dir / "clinical_evidence.jsonl")
    preclinical_all = load_jsonl(case_dir / "preclinical_evidence.jsonl")
    clinical = [r for r in clinical_all if (r.get("inclusion_status") or "included") == "included"]
    preclinical = [r for r in preclinical_all if (r.get("inclusion_status") or "included") == "included"]
    n_clin_excluded = len(clinical_all) - len(clinical)
    n_prec_excluded = len(preclinical_all) - len(preclinical)

    parts: list[str] = [
        '<meta name="robots" content="noindex">\n',
        f"# Evidence — `{slug}`\n",
    ]
    if n_clin_excluded or n_prec_excluded:
        parts.append(
            f"_This page shows {len(clinical)} included clinical + {len(preclinical)} "
            f"included pre-clinical rows, grouped by intervention. "
            f"{n_clin_excluded} clinical and {n_prec_excluded} pre-clinical papers "
            f"were reviewed and excluded — see the [master manuscripts table](manuscripts.md) for the full audit trail._\n"
        )

    parts.append(f"## Clinical evidence ({len(clinical)} rows)\n")
    if clinical:
        parts.append(
            "Per-manuscript detail grouped by intervention. Each row is one published "
            "clinical-evidence finding. Columns mirror the per-publication "
            "decision-support layout used in companion projects (`io-shieldbreak`'s "
            "Pharmacodynamic-Results table).\n"
        )
        groups = group_clinical_by_intervention(clinical)
        for iid, payload in groups.items():
            parts.append(
                f"### {html.escape(payload['label'])}  \n"
                f'<small><code>intervention_id: {html.escape(iid)}</code> · '
                f"{len(payload['rows'])} row(s)</small>\n"
            )
            parts.append(render_clinical_table(payload["rows"]))
    else:
        parts.append("_No clinical evidence rows yet._\n")

    parts.append(f"## Pre-clinical evidence ({len(preclinical)} rows)\n")
    if preclinical:
        groups = group_clinical_by_intervention(preclinical)
        for iid, payload in groups.items():
            parts.append(
                f"### {html.escape(payload['label'])}  \n"
                f'<small><code>intervention_id: {html.escape(iid)}</code> · '
                f"{len(payload['rows'])} row(s)</small>\n"
            )
            parts.append(render_preclinical_table(payload["rows"]))
    else:
        parts.append("_No pre-clinical evidence rows yet._\n")

    parts.append(
        f"[Back to case](index.md) · [Trials](trials.md) · "
        f"[Manuscripts](manuscripts.md) · "
        f"[Board](board.md) · [Recommendations](recommendations.md)\n"
    )
    parts.append(
        '!!! danger disclaimer "Decision support, not medical advice"\n'
        "    See [PHI policy](../../phi_policy.md).\n"
    )

    body_md = "\n".join(parts) + "\n"
    dst = REPO / "docs" / "cases" / slug / "evidence.md"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(body_md, encoding="utf-8")
    print(f"wrote {dst} (clinical={len(clinical)}, preclinical={len(preclinical)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
