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
from libbylib import load_jsonl

REPO = Path(__file__).resolve().parent.parent




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


# surfaced_reason → (badge label, CSS pill class). `none` renders no badge; the
# other reasons flag a feature-targeting investigational option that is surfaced in
# the Experimental table but not ranked as a live top-tier choice.
SURFACED_META = {
    "unavailable": ("Unavailable", "flag-unavailable"),
    "consolidated": ("Consolidated", "flag-consolidated"),
    "thin_evidence": ("Thin evidence", "flag-thin"),
    "not_enrollable": ("Not enrollable", "flag-not-enrollable"),
}


def _is_surfaced_only(r: dict) -> bool:
    """True for a row surfaced-but-not-ranked (a non-`none` surfaced_reason)."""
    return (r.get("surfaced_reason") or "none") != "none"


def surfaced_badge(reason: str | None) -> str:
    meta = SURFACED_META.get(reason or "none")
    if not meta:
        return "—"
    label, cls = meta
    return f'<span class="flag-badge {cls}">{html.escape(label)}</span>'


RECS_HEAD = (
    "<th>Rank</th><th>Intervention</th>"
    "<th>Likelihood of effect</th><th>Toxicity burden</th>"
    "<th>Counter-productive MoA</th><th>Overall</th>"
    "<th>Key references</th>"
)

# Header for the "Also considered" table: swaps the Rank column for a Flag column.
RECS_HEAD_FLAGGED = (
    "<th>Flag</th><th>Intervention</th>"
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
    # State the verdict in words on rows the board argued against. Previously the
    # only signal was a line-through on the whole row, which also struck the
    # rationale. A badge survives monochrome printing and screen readers.
    if (r.get("status") or "") == "not_recommended":
        head += ' <span class="flag-badge badge-not-recommended">Not recommended</span>'
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


def render_recs_table(rows: list[dict], *, flagged: bool = False) -> str:
    """Render a recs table. When `flagged`, the leading column shows the
    `surfaced_reason` badge instead of the numeric rank (used for the
    "Also considered" group). Each row carries its `status`-derived CSS class so
    `not_recommended` / `considered_with_caveats` rows are visually distinct."""
    if not rows:
        return "_No rows in this group._\n"
    body = []
    for r in rows:
        cls = status_class(r.get("status") or "recommended")
        tr_open = f'    <tr class="{cls}">' if cls else "    <tr>"
        lead = surfaced_badge(r.get("surfaced_reason")) if flagged else fmt(r.get("rank"))
        body.append(
            tr_open
            + f"<td>{lead}</td>"
            f"{_intervention_cell(r)}"
            f"<td>{fmt(r.get('likelihood_of_effect'))}</td>"
            f"<td>{fmt(r.get('toxicity_burden'))}</td>"
            f"{_cpm_cell(r)}"
            f"{_overall_cell(r)}"
            f"{_key_references_cell(r)}"
            "</tr>"
        )
    head = RECS_HEAD_FLAGGED if flagged else RECS_HEAD
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


_TABLE_LEGEND = (
    '!!! note "Reading the columns"\n'
    "    **Toxicity burden** is patient-level G3+ AE severity (Low / Moderate / High) "
    "summarized from trial publications. **Counter-productive MoA** is the "
    "mechanism-level risk that the intervention's own pathway could blunt the "
    "therapeutic goal — distinct from patient AEs. The board's endorse / dissent / "
    "veto state appears as pills under each intervention; full per-persona "
    "rationale lives on the [board page](board.md).\n"
)


def group_by_scenario(rows: list[dict]) -> tuple[list[dict], list[dict], list[dict]]:
    """Split rows into (workup_rows, ranked_rows, also_considered_rows).

    - `workup_rows`: `scenario == "shared"` — the rank-1 confirmatory test that
      gates whether biomarker-conditional therapeutic recs apply.
    - `ranked_rows`: live, ranked options (`surfaced_reason` is `none`/absent) —
      the top-tier + caveated + not-recommended options, rank-ordered.
    - `also_considered_rows`: feature-targeting investigational options surfaced
      but not ranked (`surfaced_reason` ∈ unavailable/consolidated/thin_evidence/
      not_enrollable) — rendered in a flagged "Also considered" table.

    Backward-compatible: when no row carries a `surfaced_reason`, `also_considered`
    is empty and the page renders exactly as the pre-two-table single ranked view.
    """
    workup: list[dict] = []
    ranked: list[dict] = []
    also: list[dict] = []
    for r in rows:
        if r.get("scenario") == "shared":
            workup.append(r)
        elif _is_surfaced_only(r):
            also.append(r)
        else:
            ranked.append(r)
    workup.sort(key=lambda r: r.get("rank") or 999)
    ranked.sort(key=lambda r: r.get("rank") or 999)
    # Group also-considered by reason (stable), then by rank within a reason.
    reason_order = list(SURFACED_META)
    also.sort(key=lambda r: (reason_order.index(r.get("surfaced_reason"))
                             if r.get("surfaced_reason") in reason_order else 99,
                             r.get("rank") or 999))
    return workup, ranked, also


def downloads_block(case_docs: Path, slug: str) -> str:
    """Surface reporter-built artifacts at the top of recommendations.md.

    Empty string when none exist yet — keeps the page clean before /reporter
    has run, and the page doesn't need a re-render once it does (the
    reporter calls back through run_case.sh which re-runs this script).
    """
    html_artifacts = [
        (
            "target_validation.md",
            "Target validation paths",
            "per-feature biomarker-workup table with providers and references, sortable in-browser",
        ),
        (
            f"{slug}-recommendations.html",
            "Recommendations table",
            "ranked options + pipeline context + per-intervention evidence in detail — self-contained HTML that opens offline",
        ),
        (
            "preclinical_recommendations.md",
            "Preclinical recommendations",
            "forward-looking horizon scan of earlier-than-clinical candidate drugs, compounds, and strategies, in a sortable in-browser table",
        ),
        (
            f"{slug}-preclinical.html",
            "Preclinical recommendations (offline)",
            "same preclinical horizon scan packaged as a self-contained HTML that opens offline",
        ),
        (
            "accessibility.md",
            "Access guide",
            "how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a sortable in-browser table",
        ),
        (
            f"{slug}-accessibility.html",
            "Access guide (offline)",
            "same access-guide content packaged as a self-contained HTML that opens offline",
        ),
        (
            "manuscripts.md",
            "Master manuscripts table",
            "every paper considered — n, effect, variance, toxicities, in a sortable in-browser table",
        ),
        (
            f"{slug}-manuscripts.html",
            "Master manuscripts table (offline)",
            "same manuscripts inventory packaged as a self-contained HTML that opens offline",
        ),
    ]
    pdf_artifacts = [
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
            f"{slug}-preclinical.pdf",
            "Preclinical recommendations",
            "forward-looking horizon scan of earlier-than-clinical candidates, one deep section per candidate, in a print-friendly PDF",
        ),
        (
            f"{slug}-accessibility.pdf",
            "Access guide",
            "trial recruitment contacts + manufacturer medical-info lines, in a print-friendly PDF",
        ),
        (
            f"{slug}-manuscripts.pdf",
            "Master manuscripts table",
            "every paper considered — n, effect, variance, toxicities, in a print-friendly PDF",
        ),
        (
            f"{slug}-plain-language.pdf",
            "Patient/caregiver PDF",
            "plain-language summary",
        ),
    ]
    html_present = [(n, l, b) for n, l, b in html_artifacts if (case_docs / n).exists()]
    pdf_present = [(n, l, b) for n, l, b in pdf_artifacts if (case_docs / n).exists()]
    if not html_present and not pdf_present:
        return ""
    lines = ["## Downloads\n"]
    if html_present:
        lines.append("### HTML\n")
        for name, label, blurb in html_present:
            lines.append(f"- [{label}]({html.escape(name)}) — {blurb}")
        lines.append("")
    if pdf_present:
        lines.append("### PDF\n")
        for name, label, blurb in pdf_present:
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

    workup, ranked, also = group_by_scenario(rows)

    case_docs = REPO / "docs" / "cases" / slug
    # Only cross-link the Standard-of-care page when the SoC screener has run for
    # this case — a dangling link aborts `mkdocs build --strict` (and CI).
    soc_ref = (
        "Approved and guideline-carried options for this patient's disease live on the "
        "[Standard-of-care page](standard_of_care.md) instead."
        if (case_docs / "standard_of_care.md").exists()
        else "Approved and guideline-carried standard-of-care options are reported separately."
    )
    parts = [
        '<meta name="robots" content="noindex">\n',
        f"# Experimental options — `{slug}`\n",
        "_Investigational / trial-only interventions that target the patient's stated "
        f"features, ranked by the board's synthesis. {soc_ref}_\n",
    ]
    dl = downloads_block(case_docs, slug)
    if dl:
        parts.append(dl)

    counts = f"{len(rows)} rows: {len(workup)} workup + {len(ranked)} ranked"
    if also:
        counts += f" + {len(also)} also considered"
    parts.append(f"_{counts}._\n")

    if workup:
        parts.append("## Shared first step\n")
        parts.append(
            "_The confirmatory test gates whether biomarker-conditional recs below apply. "
            "Run regardless of which therapy is ultimately chosen._\n"
        )
        parts.append(render_recs_table(workup))
        parts.append("## Ranked options\n")
        parts.append(
            "_Biomarker-conditional recs are flagged inline. The ranking is scoped to "
            "drugs that target the user's stated targetable feature._\n"
        )
        parts.append(render_recs_table(ranked))
    else:
        parts.append("## Ranked options\n")
        parts.append(render_recs_table(ranked))

    if also:
        parts.append("## Also considered — not ranked\n")
        parts.append(
            "_Feature-targeting investigational options the board considered but did not "
            "rank as live top-tier choices. The **Flag** column says why: "
            "**Unavailable** (program discontinued/terminated), **Consolidated** (one product "
            "of an approach ranked above), **Thin evidence** (no peer-reviewed clinical "
            "efficacy yet), **Not enrollable** (cross-tumor evidence or geographically "
            "inaccessible). See the [Access guide](accessibility.md) for how each would be obtained._\n"
        )
        parts.append(render_recs_table(also, flagged=True))

    parts.append(_TABLE_LEGEND)

    nav = [
        "[Back to case](index.md)", "[Trials](trials.md)", "[Evidence](evidence.md)",
        "[Manuscripts](manuscripts.md)", "[Target validation](target_validation.md)",
        "[Board](board.md)", "[Plain language](plain_language.md)",
    ]
    # Only link the preclinical page when this case actually has that track.
    if (case_docs / "preclinical_recommendations.md").exists():
        nav.append("[Preclinical](preclinical_recommendations.md)")
    parts.append(" · ".join(nav) + "\n")
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
