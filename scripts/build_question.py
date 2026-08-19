#!/usr/bin/env python3
"""Render the Question report page for a question-scoped Libby run.

Usage:
  python3 scripts/build_question.py <slug>

Reads:
  data/cases/<slug>/question.json          — the framer's scope spine
  data/cases/<slug>/question_answer.json   — the synthesist's answer
  data/cases/<slug>/question_report.md     — the reporter's narrative (optional)

Writes:
  docs/cases/<slug>/question.md
  docs/cases/<slug>/<slug>-question.html   (self-contained)
  docs/cases/<slug>/<slug>-question.pdf

The page leads with the verdict. Everything else on it exists to stop a narrow
answer being read as a broad clearance: the pre-registered acceptance criteria
with what was actually found against each, the evidence both ways with its
population match, the board's preserved dissent, and the scope caveat.
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import build_report as br  # noqa: E402

PAGE_TITLE = "Question report"

VERDICT_LABEL = {
    "yes": "Yes",
    "qualified_yes": "Qualified yes",
    "no": "No",
    "qualified_no": "Qualified no",
    "insufficient_evidence": "Insufficient evidence",
    "not_answerable_as_asked": "Not answerable as asked",
}

# Verdict styling reuses the recommendation pills. insufficient_evidence and
# not_answerable_as_asked deliberately do NOT get a positive colour: a reader
# skimming for a green badge must not read "we could not answer this" as a soft yes.
VERDICT_CLASS = {
    "yes": "flag-consolidated",
    "qualified_yes": "flag-thin",
    "no": "badge-not-recommended",
    "qualified_no": "badge-not-recommended",
    "insufficient_evidence": "flag-unavailable",
    "not_answerable_as_asked": "flag-unavailable",
}

STRENGTH_ORDER = {"strong": 0, "moderate": 1, "weak": 2}


def fmt(v) -> str:
    if v is None or v == "":
        return "&mdash;"
    if isinstance(v, list):
        return "; ".join(html.escape(str(x)) for x in v) or "&mdash;"
    return html.escape(str(v))


def _load(case_dir: Path, name: str) -> dict:
    path = case_dir / name
    if not path.exists():
        raise SystemExit(f"missing {path.relative_to(REPO)}")
    return json.loads(path.read_text(encoding="utf-8"))


def verdict_badge(ans: dict) -> str:
    v = ans.get("verdict", "")
    label = VERDICT_LABEL.get(v, v or "—")
    cls = VERDICT_CLASS.get(v, "flag-unavailable")
    conf = ans.get("confidence", "")
    conf_txt = f' <span class="persona-line">{html.escape(conf)} confidence</span>' if conf else ""
    return f'<span class="flag-badge {cls}">{html.escape(label)}</span>{conf_txt}'


def render_criteria_table(q: dict, ans: dict) -> str:
    """Pre-registered criteria against what was found.

    Rendered even when every row came back unmet or null: an unmet criterion is a
    finding, and omitting it would let the page read as though only supporting
    evidence was sought.
    """
    results = ans.get("acceptance_criteria_result") or []
    if not results:
        return ""
    direction = {c.get("criterion"): c.get("would_support") for c in (q.get("acceptance_criteria") or [])}
    rows = []
    for r in results:
        met = r.get("met")
        if met is True:
            mark, cls = "Met", "fit-strong"
        elif met is False:
            mark, cls = "Not met", "fit-none"
        else:
            mark, cls = "Undetermined", "fit-weak"
        points = direction.get(r.get("criterion")) or "—"
        rows.append(
            "<tr>"
            f"<td>{fmt(r.get('criterion'))}</td>"
            f"<td><span class=\"fit-badge {cls}\">{mark}</span></td>"
            f"<td>{fmt(points)}</td>"
            f"<td>{fmt(r.get('finding'))}</td>"
            "</tr>"
        )
    head = (
        "<tr><th>Pre-registered criterion</th><th>Result</th>"
        "<th>Points toward</th><th>What was found</th></tr>"
    )
    return (
        "## What would have answered this, decided before the search\n\n"
        '<table class="trial-table"><thead>' + head + "</thead><tbody>"
        + "".join(rows) + "</tbody></table>\n"
    )


def render_evidence_table(ans: dict) -> str:
    def block(key: str, heading: str) -> str:
        items = ans.get(key) or []
        if not items:
            return f"<tr><td colspan=\"4\"><em>None recorded.</em></td></tr>"
        items = sorted(items, key=lambda e: STRENGTH_ORDER.get(e.get("strength", "weak"), 3))
        out = []
        for e in items:
            out.append(
                "<tr>"
                f"<td>{html.escape(heading)}</td>"
                f"<td>{fmt(e.get('claim'))}</td>"
                f"<td>{fmt(e.get('strength'))}</td>"
                f"<td>{fmt(e.get('population_match'))}</td>"
                "</tr>"
            )
        return "".join(out)

    head = "<tr><th>Direction</th><th>Finding</th><th>Strength</th><th>Population match</th></tr>"
    body = block("evidence_for", "For") + block("evidence_against", "Against")
    return (
        "## Evidence both ways\n\n"
        '<table class="trial-table"><thead>' + head + "</thead><tbody>"
        + body + "</tbody></table>\n"
    )


def render_dissent(ans: dict) -> str:
    rows = ans.get("board_dissent") or []
    if not rows:
        return ""
    out = []
    for d in rows:
        carried = d.get("carried_into_answer")
        mark = "carried" if carried is True else ("noted" if carried is False else "—")
        out.append(
            "<tr>"
            f"<td>{fmt(d.get('persona'))}</td>"
            f"<td>{fmt(d.get('position'))}</td>"
            f"<td>{html.escape(mark)}</td>"
            "</tr>"
        )
    head = "<tr><th>Board seat</th><th>Position</th><th>Into the answer</th></tr>"
    return (
        "## Where the board disagreed\n\n"
        '<table class="trial-table"><thead>' + head + "</thead><tbody>"
        + "".join(out) + "</tbody></table>\n"
    )


def render_scope(q: dict, ans: dict) -> str:
    parts = ['!!! warning "What this run did not assess"\n']
    parts.append("    " + (ans.get("scope_caveat") or "").replace("\n", " ").strip() + "\n")
    oos = q.get("out_of_scope") or []
    if oos:
        parts.append("\n")
        for item in oos:
            parts.append(f"    - {item}\n")
    return "".join(parts)


def _nav_line(case_docs: Path) -> str:
    candidates = [
        ("index.md", "Back to case"),
        ("recommendations.md", "Recommendations"),
        ("standard_of_care.md", "Standard of care"),
        ("evidence.md", "Evidence"),
        ("board.md", "Board"),
    ]
    links = [f"[{label}]({name})" for name, label in candidates if (case_docs / name).exists()]
    return " · ".join(links) + "\n" if links else ""


def _downloads_block(slug: str) -> str:
    items = [
        (f"{slug}-question.html", f"{PAGE_TITLE} (offline HTML)",
         "the same answer, self-contained HTML that opens offline"),
        (f"{slug}-question.pdf", f"{PAGE_TITLE} (PDF)", "print-friendly"),
    ]
    lines = ["## Downloads\n"]
    for name, label, blurb in items:
        lines.append(f"- [{label}]({html.escape(name)}) — {blurb}")
    lines.append("")
    return "\n".join(lines)


def load_narrative(case_dir: Path) -> str:
    path = case_dir / "question_report.md"
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()


def render_page(slug: str, q: dict, ans: dict, narrative: str = "",
                case_docs: Path | None = None) -> str:
    parts: list[str] = [f"# {PAGE_TITLE}\n"]
    if case_docs is not None:
        nav = _nav_line(case_docs)
        if nav:
            parts.append(nav)

    parts.append(f"\n> {html.escape(q.get('question', ''))}\n")
    parts.append(f"\n**{verdict_badge(ans)}**\n")

    src = q.get("source_case_slug")
    if src:
        parts.append(
            f"\nThis question is about the published case `{html.escape(src)}`. "
            "That case's ranking was not revisited and stands as published.\n"
        )
    else:
        parts.append("\nThis is a standalone question: it is not anchored to a patient case.\n")

    if narrative:
        parts.append("\n" + narrative + "\n")

    parts.append("\n" + (ans.get("answer") or "") + "\n")

    parts.append("\n" + render_criteria_table(q, ans))
    parts.append("\n" + render_evidence_table(ans))

    changers = ans.get("what_would_change_it") or []
    if changers:
        parts.append("\n## What would change this answer\n\n")
        for c in changers:
            parts.append(f"- {c}\n")

    dissent = render_dissent(ans)
    if dissent:
        parts.append("\n" + dissent)

    parts.append("\n" + render_scope(q, ans))
    parts.append("\n" + _downloads_block(slug))
    return "".join(parts)


def preflight(q: dict, ans: dict, narrative: str = "") -> None:
    """Fail loudly on the contract violations that matter for this track."""
    problems: list[str] = []

    if ans.get("question") != q.get("question"):
        problems.append(
            "question_answer.json::question does not match question.json::question — "
            "the answer may have drifted from what was asked"
        )

    reg = [c.get("criterion") for c in (q.get("acceptance_criteria") or [])]
    got = [c.get("criterion") for c in (ans.get("acceptance_criteria_result") or [])]
    if reg != got:
        problems.append(
            "acceptance_criteria_result does not report every pre-registered criterion "
            "in order — this is the audit trail that the answer was not assembled backwards"
        )

    if not (ans.get("scope_caveat") or "").strip():
        problems.append("scope_caveat is empty — a narrow answer will read as a broad clearance")

    shape = ans.get("answer_shape_used") or q.get("answer_shape")
    if shape == "verdict_plus_ranked_options" and not ans.get("notes"):
        # Not fatal on its own, but an upgrade past the framer's read needs saying.
        if q.get("answer_shape") == "verdict":
            problems.append(
                "answer_shape_used upgrades the framer's 'verdict' to a ranked table; "
                "the synthesist may downgrade but not upgrade"
            )

    if "\u2014" in narrative:
        problems.append("narrative contains an em-dash (prose guideline for patient-facing text)")

    if problems:
        for p in problems:
            print(f"preflight: {p}", file=sys.stderr)
        raise SystemExit(1)


def _make_pdf(slug: str, page_md: str, out_path: Path) -> None:
    try:
        from fpdf import FPDF
    except ImportError as e:  # pragma: no cover
        raise SystemExit(
            "build_question: missing dependency `fpdf2`.\n  pip install fpdf2"
        ) from e

    today = datetime.now(timezone.utc).date().isoformat()

    class QuestionPDF(FPDF):
        def footer(self_):
            if self_.page_no() <= 1:
                return
            self_.set_y(-12)
            self_.set_font(br._FONT_FAMILY, "I", 8)
            self_.set_text_color(*br.INK_MUTED)
            self_.cell(0, 6, br._ascii_fallback(f"Libby {PAGE_TITLE.lower()} — {slug}"), align="C")

    pdf = QuestionPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=18)
    br._register_unicode_font(pdf)
    br._render_cover(
        pdf, PAGE_TITLE, slug, today, "LIBBY",
        br.COVER_BG, br._DISCLAIMER_CLINICIAN,
    )
    pdf.add_page()
    br._render_markdown_block(pdf, page_md, top_h1=True)
    pdf.output(str(out_path))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("slug")
    args = ap.parse_args(argv)
    slug = args.slug

    case_dir = REPO / "data" / "cases" / slug
    docs_dir = REPO / "docs" / "cases" / slug
    docs_dir.mkdir(parents=True, exist_ok=True)

    # No-op cleanly on a non-question case so run_case.sh can call this
    # unconditionally, the same way the other optional tracks behave.
    if not (case_dir / "question.json").exists():
        return 0

    q = _load(case_dir, "question.json")
    ans = _load(case_dir, "question_answer.json")
    narrative = load_narrative(case_dir)

    preflight(q, ans, narrative)

    page_md = render_page(slug, q, ans, narrative, case_docs=docs_dir)
    md_dst = docs_dir / "question.md"
    md_dst.write_text(page_md, encoding="utf-8")
    print(f"built {md_dst}")

    html_dst = docs_dir / f"{slug}-question.html"
    html_out = br._render_self_contained_html_page(
        slug, f"Libby {PAGE_TITLE.lower()} — {slug}", PAGE_TITLE, page_md,
    )
    html_dst.write_text(html_out, encoding="utf-8")
    print(f"built {html_dst}")

    pdf_dst = docs_dir / f"{slug}-question.pdf"
    _make_pdf(slug, page_md, pdf_dst)
    print(f"built {pdf_dst}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
