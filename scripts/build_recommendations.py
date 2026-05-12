#!/usr/bin/env python3
"""Render recommendations.jsonl → docs/cases/<slug>/recommendations.md.

Builds the final ranked-table page. The PI agent also produces a clinician-grade
index.md prose page; this script is the deterministic table view that links from it.
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
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def persona_badges(personas: list[str] | None) -> str:
    if not personas:
        return "—"
    return " ".join(f'<span class="persona persona-{p}">{html.escape(p)}</span>' for p in personas)


def fmt(v) -> str:
    if v is None or v == "":
        return "—"
    if isinstance(v, list):
        return "; ".join(html.escape(str(x)) for x in v) or "—"
    return html.escape(str(v))


def status_class(status: str) -> str:
    return {
        "recommended": "",
        "considered_with_caveats": "split-glyph",
        "not_recommended": "not-recommended",
    }.get(status, "")


RECS_HEAD = (
    "<th>Rank</th><th>Intervention</th>"
    "<th>Likelihood of effect</th><th>Toxicity burden</th>"
    "<th>Counter-productive MoA</th><th>Overall</th>"
    "<th>Key references</th>"
)


def _key_references_cell(r: dict) -> str:
    """Render `evidence_anchor[]` as a stacked list of clickable links.

    PubMed (`pmid:NNNNNNNN`) → pubmed.ncbi.nlm.nih.gov; ClinicalTrials.gov
    (`nct:NCTNNNNNNNN`) → clinicaltrials.gov; anything else as plain text.
    One link per line (`<br>`-separated) so the column scans top-to-bottom.
    """
    anchors = r.get("evidence_anchor") or []
    if not anchors:
        return "<td>—</td>"
    pieces: list[str] = []
    for a in anchors:
        s = str(a).strip()
        if s.lower().startswith("pmid:"):
            pid = s.split(":", 1)[1].strip()
            pieces.append(
                f'<a href="https://pubmed.ncbi.nlm.nih.gov/{html.escape(pid)}">PMID&nbsp;{html.escape(pid)}</a>'
            )
        elif s.lower().startswith("nct:"):
            nid = s.split(":", 1)[1].strip()
            pieces.append(
                f'<a href="https://clinicaltrials.gov/study/{html.escape(nid)}">{html.escape(nid)}</a>'
            )
        else:
            pieces.append(html.escape(s))
    return "<td>" + "<br>".join(pieces) + "</td>"


def _persona_line(r: dict) -> str:
    """Compact persona pills row: endorse / dissent / veto, when any persona registered."""
    pieces: list[str] = []
    for label, key in (("endorse", "endorsed_by"), ("dissent", "dissent_by"), ("veto", "veto_by")):
        personas = r.get(key) or []
        if not personas:
            continue
        pills = " ".join(f'<span class="persona persona-{p}">{html.escape(p)}</span>' for p in personas)
        pieces.append(f'<small class="persona-line"><em>{label}:</em> {pills}</small>')
    return "<br>".join(pieces)


def _intervention_cell(r: dict) -> str:
    """Intervention cell: bold label, conditional flag, and persona-state pills under it.

    Persona state moves into this cell (replacing dedicated Endorsed / Dissent / Veto
    columns) so the at-a-glance table stays narrow while board signal stays visible.
    """
    label = fmt(r.get("intervention_label"))
    scen = r.get("scenario")
    if isinstance(scen, str) and scen.endswith(":positive"):
        biomarker_short = scen.split(":", 1)[0]
        head = (
            f"<strong>{label}</strong> "
            f'<span class="scenario-conditional">(conditional on {html.escape(biomarker_short)} positive)</span>'
        )
    else:
        head = f"<strong>{label}</strong>"
    persona = _persona_line(r)
    body = f"{head}<br>{persona}" if persona else head
    return f"<td>{body}</td>"


def _cpm_cell(r: dict) -> str:
    """Counter-productive MoA cell: bold severity + parenthetical mechanism description."""
    cpm = r.get("counter_productive_moa") or {}
    severity = cpm.get("severity")
    description = cpm.get("description")
    if not severity:
        return "<td>—</td>"
    sev_html = f"<strong>{html.escape(str(severity))}</strong>"
    if description:
        return f'<td>{sev_html} <span class="cpm-desc">({html.escape(str(description))})</span></td>'
    return f"<td>{sev_html}</td>"


def _overall_cell(r: dict) -> str:
    overall = r.get("overall")
    if not overall:
        return "<td>—</td>"
    return f"<td><strong>{html.escape(str(overall))}</strong></td>"


def render_recs_table(rows: list[dict]) -> str:
    if not rows:
        return "_No rows in this scenario._\n"
    body = []
    for r in rows:
        body.append(
            "    <tr>"
            f"<td>{fmt(r.get('rank'))}</td>"
            f"{_intervention_cell(r)}"
            f"<td>{fmt(r.get('likelihood_of_effect'))}</td>"
            f"<td>{fmt(r.get('toxicity_burden'))}</td>"
            f"{_cpm_cell(r)}"
            f"{_overall_cell(r)}"
            f"{_key_references_cell(r)}"
            "</tr>"
        )
    return (
        '<div class="trial-table-wrap">\n'
        '  <div class="trial-scroll">\n'
        '    <table class="trial-table">\n'
        f'      <thead><tr>{RECS_HEAD}</tr></thead>\n'
        '      <tbody>\n' + "\n".join(body) + "\n      </tbody>\n"
        "    </table>\n"
        "  </div>\n"
        "</div>\n"
    )


_TABLE_LEGEND = (
    '!!! note "Reading the columns"\n'
    "    **Toxicity burden** is patient-level G3+ AE severity (Low / Moderate / High) "
    "summarized from trial publications. **Counter-productive MoA** is the "
    "mechanism-level risk that the intervention's own pathway could blunt the "
    "therapeutic goal — distinct from patient AEs. The board's endorse / dissent / "
    "veto state appears as pills under each intervention; full per-persona "
    "rationale lives on the [board page](board.md).\n"
)


def group_by_scenario(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    """Split rows into (workup_rows, unified_rows).

    `workup_rows` are rows with `scenario == "shared"` — the rank-1 confirmatory
    test that gates whether biomarker-conditional therapeutic recs apply.
    `unified_rows` is everything else (biomarker-conditional recs tagged
    `scenario: "<biomarker_short>:positive"` in gated cases, or untagged
    `scenario: null` recs in non-gated cases), rank-ordered for a single
    ranked table.

    Conditional recs surface the (conditional on …) flag at render time via
    `_intervention_cell` — they don't get split into a separate table.
    """
    workup: list[dict] = []
    unified: list[dict] = []
    for r in rows:
        scen = r.get("scenario")
        if scen == "shared":
            workup.append(r)
        else:
            unified.append(r)
    workup.sort(key=lambda r: r.get("rank") or 999)
    unified.sort(key=lambda r: r.get("rank") or 999)
    return workup, unified


def downloads_block(case_docs: Path, slug: str) -> str:
    """Surface reporter-built artifacts at the top of recommendations.md.

    Empty string when none exist yet — keeps the page clean before /reporter
    has run, and the page doesn't need a re-render once it does (the
    reporter calls back through run_case.sh which re-runs this script).
    """
    artifacts = [
        (
            f"{slug}-target-validation.pdf",
            "Target validation paths",
            "diagnostic + biomarker workup that hardens the targetable-feature call",
        ),
        (
            f"{slug}-recommendations.pdf",
            "Recommendations table",
            "ranked options + pipeline context + evidence in detail, in a print-friendly PDF",
        ),
        (
            f"{slug}-accessibility.pdf",
            "Access guide",
            "how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a print-friendly PDF",
        ),
        (
            "manuscripts.md",
            "Master manuscripts table",
            "every paper considered — n, effect, variance, toxicities, in a sortable in-browser table",
        ),
        (
            f"{slug}-plain-language.pdf",
            "Patient/caregiver PDF",
            "plain-language summary",
        ),
    ]
    present = [(name, label, blurb) for name, label, blurb in artifacts if (case_docs / name).exists()]
    if not present:
        return ""
    lines = ["## Downloads\n"]
    for name, label, blurb in present:
        lines.append(f"- [{label}]({html.escape(name)}) — {blurb}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    args = parser.parse_args()
    slug = args.slug

    case_dir = REPO / "data" / "cases" / slug
    rows = load_jsonl(case_dir / "recommendations.jsonl")

    workup, unified = group_by_scenario(rows)

    parts = [
        '<meta name="robots" content="noindex">\n',
        f"# Recommendations — `{slug}`\n",
    ]

    case_docs = REPO / "docs" / "cases" / slug
    dl = downloads_block(case_docs, slug)
    if dl:
        parts.append(dl)

    if workup:
        parts.append(
            f"_{len(rows)} rows: {len(workup)} workup + {len(unified)} ranked options._\n"
        )
        parts.append("## Shared first step\n")
        parts.append(
            "_The confirmatory test gates whether biomarker-conditional recs below apply. "
            "Run regardless of which therapy is ultimately chosen._\n"
        )
        parts.append(render_recs_table(workup))
        if unified:
            parts.append("## Ranked options\n")
            parts.append(
                "_Biomarker-conditional recs are flagged inline. The ranking is "
                "scoped to drugs that target the user's stated targetable feature; "
                "if the workup test is negative the within-scope options are exhausted, "
                "and standard care for the indication lies outside Libby's targetable-feature scope._\n"
            )
            parts.append(render_recs_table(unified))
    else:
        parts.append(f"_{len(rows)} ranked options._\n")
        parts.append(render_recs_table(unified))

    parts.append(_TABLE_LEGEND)

    parts.append(
        f"[Back to case](index.md) · [Trials](trials.md) · "
        f"[Evidence](evidence.md) · [Manuscripts](manuscripts.md) · "
        f"[Target validation](target_validation.md) · "
        f"[Board](board.md) · [Plain language](plain_language.md)\n"
    )
    parts.append(
        '!!! danger disclaimer "Decision support, not medical advice"\n'
        "    Libby is experimental. Recommendations on this page have not been\n"
        "    reviewed by a clinician treating this patient.\n"
        "    See [PHI policy](../../phi_policy.md).\n"
    )
    body_md = "\n".join(parts) + "\n"

    dst = REPO / "docs" / "cases" / slug / "recommendations.md"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(body_md, encoding="utf-8")
    print(f"wrote {dst} ({len(rows)} rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
