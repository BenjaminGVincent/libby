#!/usr/bin/env python3
"""Render clinical_evidence.jsonl + preclinical_evidence.jsonl → docs/cases/<slug>/evidence.md.

Two sections: clinical (table by intervention) and preclinical (table by intervention).
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from collections import defaultdict
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


def link_pmid(pmid) -> str:
    if not pmid:
        return "—"
    return f'<a href="https://pubmed.ncbi.nlm.nih.gov/{html.escape(str(pmid))}">{html.escape(str(pmid))}</a>'


def link_doi(doi) -> str:
    if not doi:
        return "—"
    return f'<a href="https://doi.org/{html.escape(str(doi))}">{html.escape(str(doi))}</a>'


CLINICAL_COLS = [
    ("Intervention", "intervention_label"),
    ("Indication", "indication"),
    ("Design", "design"),
    ("n", "n"),
    ("Outcome", "outcome"),
    ("Effect", "effect_size"),
    ("CI / variance", "variance_or_ci"),
    ("Tier", "evidence_tier"),
    ("Last author", "last_author"),
    ("Contact", "last_author_contact"),
    ("Year", "year"),
    ("Journal", "journal"),
    ("PMID", "pmid"),
    ("DOI", "doi"),
]

PRECLINICAL_COLS = [
    ("Intervention", "intervention_label"),
    ("Model", "model_system"),
    ("Mechanism", "mechanism"),
    ("Key finding", "key_finding"),
    ("Effect", "effect_size_qual"),
    ("Translatability", "translatability_score"),
    ("Caveats", "caveats"),
    ("Year", "year"),
    ("Journal", "journal"),
    ("PMID", "pmid"),
    ("DOI", "doi"),
]


def render_table(rows: list[dict], cols: list[tuple[str, str]]) -> str:
    if not rows:
        return "_No rows yet._\n"
    rows_grouped = sorted(rows, key=lambda r: (r.get("intervention_label") or "", -(r.get("year") or 0)))
    head = "".join(f"<th>{html.escape(label)}</th>" for label, _ in cols)
    body = []
    for r in rows_grouped:
        cells = []
        for label, key in cols:
            if key == "pmid":
                cells.append(f"<td>{link_pmid(r.get(key))}</td>")
            elif key == "doi":
                cells.append(f"<td>{link_doi(r.get(key))}</td>")
            else:
                cells.append(f"<td>{fmt(r.get(key))}</td>")
        body.append("        <tr>" + "".join(cells) + "</tr>")
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
    clinical = load_jsonl(case_dir / "clinical_evidence.jsonl")
    preclinical = load_jsonl(case_dir / "preclinical_evidence.jsonl")

    body = (
        '<meta name="robots" content="noindex">\n\n'
        f"# Evidence — `{slug}`\n\n"
        '!!! danger disclaimer "Decision support, not medical advice"\n'
        "    See [PHI policy](../../phi_policy.md).\n\n"
        f"## Clinical evidence ({len(clinical)} rows)\n\n"
        f"{render_table(clinical, CLINICAL_COLS)}\n"
        f"## Pre-clinical evidence ({len(preclinical)} rows)\n\n"
        f"{render_table(preclinical, PRECLINICAL_COLS)}\n"
        f"[Back to case](index.md) · [Trials](trials.md) · [Board](board.md) · [Recommendations](recommendations.md)\n"
    )
    dst = REPO / "docs" / "cases" / slug / "evidence.md"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(body, encoding="utf-8")
    print(f"wrote {dst} (clinical={len(clinical)}, preclinical={len(preclinical)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
