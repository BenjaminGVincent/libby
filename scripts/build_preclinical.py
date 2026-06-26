#!/usr/bin/env python3
"""Render preclinical_recommendations.jsonl into the case's "Preclinical
recommendations" page plus its self-contained HTML and print-PDF companions.

This is the forward-looking sibling of `build_recommendations.py` /
`build_report.py`. Where those package the board's ranked clinical options, this
renders the preclinical_reporter's ranked horizon scan of candidate drugs,
compounds, and treatment strategies that are EARLIER than clinical development
(or not yet developed) but plausibly target the patient's stated features.

Outputs (under docs/cases/<slug>/):
  preclinical_recommendations.md   mkdocs in-browser page (sortable HTML table)
  <slug>-preclinical.html          self-contained, opens offline
  <slug>-preclinical.pdf           print-friendly, one deep section per rank

Pure Python. Reuses the PDF / self-contained-HTML helpers in build_report.py so
the two tracks render with one shared font stack, cover style, and CSS.
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
# scripts/ is sys.path[0] when run as `python3 scripts/build_preclinical.py`,
# so build_report imports cleanly and its __main__ guard keeps it inert.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_report as br  # noqa: E402


# ---------- display vocab ----------

_STAGE_LABELS = {
    "conceptual": "Conceptual",
    "in_silico": "In silico",
    "in_vitro": "In vitro",
    "in_vivo_animal": "In vivo (animal)",
    "early_translational": "Early translational",
    "ind_enabling": "IND-enabling",
    "first_in_human_planned": "First-in-human planned",
}

_TYPE_LABELS = {
    "small_molecule": "small molecule",
    "biologic": "biologic",
    "antibody": "antibody",
    "adc": "ADC",
    "bispecific": "bispecific",
    "cell_therapy": "cell therapy",
    "vaccine": "vaccine",
    "oligonucleotide": "oligonucleotide",
    "protac_degrader": "PROTAC / degrader",
    "radioligand": "radioligand",
    "combination": "combination",
    "repurposed_drug": "repurposed drug",
    "conceptual_strategy": "conceptual strategy",
    "other": "other",
}


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def fmt(v) -> str:
    if v is None or v == "":
        return "—"
    if isinstance(v, list):
        return "; ".join(html.escape(str(x)) for x in v) or "—"
    return html.escape(str(v))


def _stage_label(v) -> str:
    return _STAGE_LABELS.get(v, fmt(v))


def _type_label(v) -> str:
    return _TYPE_LABELS.get(v, fmt(v))


# ---------- HTML table (mkdocs page) ----------

RECS_HEAD = (
    "<th>Rank</th><th>Candidate</th>"
    "<th>Stage</th><th>Evidence strength</th>"
    "<th>Translatability</th><th>Counter-productive MoA</th>"
    "<th>Overall</th><th>Key references</th>"
)


def _ref_link(s: str) -> str:
    s = str(s).strip()
    low = s.lower()
    if low.startswith("pmid:"):
        pid = s.split(":", 1)[1].strip()
        return f'<a href="https://pubmed.ncbi.nlm.nih.gov/{html.escape(pid)}">PMID&nbsp;{html.escape(pid)}</a>'
    if low.startswith("nct:"):
        nid = s.split(":", 1)[1].strip()
        return f'<a href="https://clinicaltrials.gov/study/{html.escape(nid)}">{html.escape(nid)}</a>'
    if low.startswith("doi:"):
        d = s.split(":", 1)[1].strip()
        return f'<a href="https://doi.org/{html.escape(d)}">doi:{html.escape(d)}</a>'
    if low.startswith("biorxiv:") or low.startswith("medrxiv:"):
        server, ident = s.split(":", 1)
        ident = ident.strip()
        return f'<a href="https://doi.org/{html.escape(ident)}">{html.escape(server)}:{html.escape(ident)}</a>'
    return html.escape(s)


def _key_references_cell(r: dict) -> str:
    anchors = r.get("evidence_anchor") or []
    if not anchors:
        return "<td>—</td>"
    return "<td>" + "<br>".join(_ref_link(a) for a in anchors) + "</td>"


def _candidate_cell(r: dict) -> str:
    label = fmt(r.get("intervention_label"))
    typ = r.get("intervention_type")
    head = f"<strong>{label}</strong>"
    if typ:
        head += f' <span class="scenario-conditional">({html.escape(_type_label(typ))})</span>'
    tgt = r.get("target_feature_label") or "; ".join(r.get("targets") or [])
    sub = f'<small class="persona-line"><em>targets:</em> {fmt(tgt)}</small>' if tgt else ""
    body = f"{head}<br>{sub}" if sub else head
    return f"<td>{body}</td>"


def _cpm_cell(r: dict) -> str:
    cpm = r.get("counter_productive_moa") or {}
    sev = cpm.get("severity")
    desc = cpm.get("description")
    if not sev:
        return "<td>—</td>"
    out = f"<strong>{html.escape(str(sev))}</strong>"
    if desc:
        out += f' <span class="cpm-desc">({html.escape(str(desc))})</span>'
    return f"<td>{out}</td>"


def _overall_cell(r: dict) -> str:
    overall = r.get("overall")
    if not overall:
        return "<td>—</td>"
    return f"<td><strong>{html.escape(str(overall))}</strong></td>"


def render_table(rows: list[dict]) -> str:
    if not rows:
        return "_No candidates in this group._\n"
    body = []
    for r in rows:
        body.append(
            "    <tr>"
            f"<td>{fmt(r.get('rank'))}</td>"
            f"{_candidate_cell(r)}"
            f"<td>{html.escape(_stage_label(r.get('development_stage')))}</td>"
            f"<td>{fmt((r.get('evidence_strength') or '').capitalize() or None)}</td>"
            f"<td>{fmt(r.get('translatability'))}</td>"
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


def _group_by_target(rows: list[dict]) -> list[tuple[str, list[dict]]]:
    """Group rows by primary target (targets[0]); preserve first-seen order.

    Single-feature cases collapse to one group, so the page reads as one
    ranked table; multi-feature cases get one ranked block per target.
    """
    groups: dict[str, list[dict]] = {}
    labels: dict[str, str] = {}
    order: list[str] = []
    for r in rows:
        key = (r.get("targets") or ["uncategorized"])[0]
        if key not in groups:
            groups[key] = []
            order.append(key)
            labels[key] = r.get("target_feature_label") or key.replace("_", " ")
        groups[key].append(r)
    out = []
    for key in order:
        g = sorted(groups[key], key=lambda r: r.get("rank") or 999)
        out.append((labels[key], g))
    return out


_LEGEND = (
    '!!! note "Reading the columns"\n'
    "    These are candidate ideas that are **earlier than clinical development**, "
    "or not yet developed at all. **Stage** is how far the candidate has progressed "
    "(conceptual through IND-enabling). **Evidence strength** is the qualitative weight "
    "of the preclinical support. **Counter-productive MoA** is the mechanism-level risk "
    "that the candidate's own pathway could blunt its therapeutic goal. None of these "
    "options is enrollable today; they are a horizon scan, not the ranked clinical "
    "recommendations on the [Recommendations table](recommendations.md).\n"
)


def _downloads_block(slug: str, has_rows: bool) -> str:
    # When the page has ranked rows, the build run always emits both the
    # offline HTML and the PDF, so list both deterministically rather than
    # racing the on-disk existence check (the HTML is rendered from this very
    # page_md, so it does not exist yet when this block is composed).
    if not has_rows:
        return ""
    items = [
        (f"{slug}-preclinical.html", "Preclinical recommendations (offline HTML)",
         "the same ranked horizon scan, self-contained HTML that opens offline"),
        (f"{slug}-preclinical.pdf", "Preclinical recommendations (PDF)",
         "one deep section per candidate, print-friendly"),
    ]
    lines = ["## Downloads\n"]
    for name, label, blurb in items:
        lines.append(f"- [{label}]({html.escape(name)}) — {blurb}")
    lines.append("")
    return "\n".join(lines)


def render_page(slug: str, rows: list[dict]) -> str:
    parts = [
        '<meta name="robots" content="noindex">\n',
        f"# Preclinical recommendations — `{slug}`\n",
        "_A forward-looking horizon scan: candidate drugs, compounds, and treatment "
        "strategies that are earlier than clinical development (or not yet developed) "
        "but plausibly target this patient's stated features. Separate from the board's "
        "[clinical recommendations](recommendations.md), and not reviewed by the virtual "
        "tumor board._\n",
    ]
    dl = _downloads_block(slug, bool(rows))
    if dl:
        parts.append(dl)

    if not rows:
        parts.append("_No preclinical candidates were ranked for this case._\n")
    else:
        groups = _group_by_target(rows)
        if len(groups) == 1:
            parts.append(f"_{len(rows)} ranked candidates._\n")
            parts.append(render_table(groups[0][1]))
        else:
            parts.append(
                f"_{len(rows)} ranked candidates across {len(groups)} targets._\n"
            )
            for label, g in groups:
                parts.append(f"## {html.escape(label)}\n")
                parts.append(render_table(g))

    parts.append(_LEGEND)
    parts.append(
        "[Back to case](index.md) · [Recommendations](recommendations.md) · "
        "[Trials](trials.md) · [Evidence](evidence.md) · "
        "[Manuscripts](manuscripts.md) · [Board](board.md)\n"
    )
    parts.append(
        '!!! danger disclaimer "Decision support, not medical advice"\n'
        "    Libby is experimental. These are early-stage research directions, not\n"
        "    treatment recommendations, and have not been reviewed by a clinician\n"
        "    treating this patient. See [PHI policy](../../phi_policy.md).\n"
    )
    return "\n".join(parts) + "\n"


# ---------- print PDF (one deep section per rank) ----------

def _deep_markdown(slug: str, rows: list[dict]) -> str:
    """Prose-friendly markdown for the PDF: one H2 per ranked candidate."""
    lines: list[str] = ["# Preclinical recommendations\n"]
    lines.append(
        "A forward-looking horizon scan of candidate drugs, compounds, and treatment "
        "strategies that are earlier than clinical development, or not yet developed, "
        "but plausibly target this patient's stated features. These are research "
        "directions, not enrollable options or treatment recommendations.\n"
    )
    for r in sorted(rows, key=lambda x: x.get("rank") or 999):
        label = r.get("intervention_label") or r.get("candidate_id") or "candidate"
        typ = _type_label(r.get("intervention_type")) if r.get("intervention_type") else None
        head = f"## {r.get('rank')}. {label}"
        if typ:
            head += f" ({typ})"
        lines.append(head + "\n")
        tgt = r.get("target_feature_label") or ", ".join(r.get("targets") or [])
        meta_bits = [
            f"**Target:** {tgt}" if tgt else None,
            f"**Stage:** {_stage_label(r.get('development_stage'))}",
            f"**Evidence strength:** {(r.get('evidence_strength') or '').capitalize() or '—'}",
        ]
        lines.append("  ".join(b for b in meta_bits if b) + "\n")
        if r.get("overall"):
            lines.append(f"**{r['overall']}**\n")
        if r.get("rationale_summary"):
            lines.append(r["rationale_summary"] + "\n")
        if r.get("mechanism"):
            lines.append(f"**Mechanism.** {r['mechanism']}\n")
        if r.get("translatability"):
            lines.append(f"**Translatability.** {r['translatability']}\n")
        if r.get("developability"):
            lines.append(f"**Developability.** {r['developability']}\n")
        cpm = r.get("counter_productive_moa") or {}
        if cpm.get("severity") and cpm.get("severity") != "N/A":
            desc = f" ({cpm['description']})" if cpm.get("description") else ""
            lines.append(f"**Counter-productive MoA.** {cpm['severity']}{desc}\n")
        if r.get("key_risks"):
            lines.append("**Key risks.**\n")
            for k in r["key_risks"]:
                lines.append(f"- {k}")
            lines.append("")
        if r.get("open_questions"):
            lines.append("**Open questions.**\n")
            for q in r["open_questions"]:
                lines.append(f"- {q}")
            lines.append("")
        anchors = r.get("evidence_anchor") or []
        if anchors:
            lines.append("**Key references.** " + "; ".join(str(a) for a in anchors) + "\n")
    return "\n".join(lines)


def _make_pdf(slug: str, rows: list[dict], out_path: Path) -> None:
    try:
        from fpdf import FPDF
    except ImportError as e:  # pragma: no cover
        raise SystemExit("build_preclinical: missing dependency `fpdf2`.\n  pip install fpdf2") from e

    today = datetime.now(timezone.utc).date().isoformat()

    class PreclinicalPDF(FPDF):
        def footer(self_):
            if self_.page_no() <= 1:
                return
            self_.set_y(-12)
            self_.set_font(br._FONT_FAMILY, "I", 8)
            self_.set_text_color(*br.INK_MUTED)
            self_.cell(
                0, 6,
                br._ascii_fallback(
                    f"{self_.page_no()} of {{nb}}    ·    Libby — preclinical horizon    ·    {slug}"
                ),
                align="C",
            )

    pdf = PreclinicalPDF(orientation="P", unit="mm", format="Letter")
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(left=18, top=20, right=18)
    pdf.alias_nb_pages()
    br._register_unicode_font(pdf)
    br._render_cover(
        pdf, slug,
        "Preclinical recommendations — forward-looking horizon scan",
        today, "LIBBY — PRECLINICAL HORIZON",
        br.COVER_BG, br._DISCLAIMER_CLINICIAN,
    )
    pdf.add_page()
    br._render_markdown_block(pdf, _deep_markdown(slug, rows), top_h1=True)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(out_path))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    args = parser.parse_args()
    slug = args.slug

    case_dir = REPO / "data" / "cases" / slug
    case_docs = REPO / "docs" / "cases" / slug
    rows = load_jsonl(case_dir / "preclinical_recommendations.jsonl")

    page = case_docs / "preclinical_recommendations.md"
    html_dst = case_docs / f"{slug}-preclinical.html"
    pdf_dst = case_docs / f"{slug}-preclinical.pdf"

    # No ranked rows → the preclinical track has not run for this case. Don't
    # leave an empty page that the case-output / downloads injectors would
    # otherwise surface; strip any stale artifacts and exit clean.
    if not rows:
        for stale in (page, html_dst, pdf_dst):
            if stale.exists():
                stale.unlink()
        print(f"no preclinical_recommendations.jsonl rows for {slug}; nothing rendered")
        return 0

    case_docs.mkdir(parents=True, exist_ok=True)
    page_md = render_page(slug, rows)
    page.write_text(page_md, encoding="utf-8")
    print(f"wrote {page} ({len(rows)} rows)")

    html_out = br._render_self_contained_html_page(
        slug, f"Libby preclinical recommendations — {slug}",
        "Preclinical recommendations", page_md,
    )
    html_dst.write_text(html_out, encoding="utf-8")
    print(f"built {html_dst}")

    _make_pdf(slug, rows, pdf_dst)
    print(f"built {pdf_dst}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
