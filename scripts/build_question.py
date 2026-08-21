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


DELIVERABLE_LABEL = {
    "yes": ("Available", "fit-strong"),
    "trial_only": ("Trial only", "fit-partial"),
    "off_label": ("Off-label", "fit-partial"),
    "expanded_access": ("Expanded access", "fit-partial"),
    "no": ("Not deliverable", "fit-none"),
}


def _wrap_table(head: str, body: str) -> str:
    """Wrap a table in the scroll container the other renderers use.

    Without it the table is pinned to 100% width, so every column squeezes and
    the prose cells wrap into very tall rows. With it, the per-column min-widths
    below let the table exceed the container and scroll sideways instead.
    """
    return (
        '<div class="trial-table-wrap">\n'
        '  <div class="trial-scroll">\n'
        '    <table class="trial-table">\n'
        f'      <thead>{head}</thead>\n'
        f'      <tbody>{body}</tbody>\n'
        "    </table>\n"
        "  </div>\n"
        "</div>\n"
    )


def render_candidates_table(ans: dict) -> str:
    """The evidence behind the verdict, one row per candidate assessed.

    Rendered even when the verdict is negative. A reader who is told "no" needs
    the response rates, toxicity and references that produced it, and dropping
    the table because the answer was unfavourable hides the reasoning.

    The response-rate column always prints the endpoint next to the number,
    because a composite rate is not a CR rate and a table that blurs them
    invites comparison of different endpoints as if they were one.
    """
    rows = ans.get("candidates") or []
    if not rows:
        return ""
    basis = (ans.get("ranking_basis") or "").strip()

    out = []
    for c in sorted(rows, key=lambda r: r.get("rank", 999)):
        rr = c.get("response_rate") or {}
        bits = [f"<strong>{fmt(rr.get('value'))}</strong>"]
        if rr.get("endpoint"):
            bits.append(f'<br><small class="persona-line">{fmt(rr["endpoint"])}</small>')
        if rr.get("n"):
            bits.append(f'<br><small>{fmt(rr["n"])}</small>')
        if rr.get("ci"):
            bits.append(f'<br><small>95% CI {fmt(rr["ci"])}</small>')
        if rr.get("population_match"):
            bits.append(f'<br><small class="persona-line"><em>{fmt(rr["population_match"])}</em></small>')
        rate_cell = "".join(bits)

        tox = c.get("toxicity") or {}
        tox_cell = fmt(tox.get("summary"))
        if tox.get("population_match"):
            tox_cell += f'<br><small class="persona-line"><em>{fmt(tox["population_match"])}</em></small>'

        dlabel, dcls = DELIVERABLE_LABEL.get(c.get("deliverable", ""), ("&mdash;", "fit-weak"))
        out.append(
            "<tr>"
            + f'<td class="col-q-rank">{c.get("rank", "&mdash;")}</td>'
            + f'<td class="col-q-candidate"><strong>{fmt(c.get("label"))}</strong>'
            + (f'<br><small class="persona-line">{fmt(c["notes"])}</small>' if c.get("notes") else "")
            + "</td>"
            + f'<td class="col-q-rate">{rate_cell}</td>'
            + f'<td class="col-q-tox">{tox_cell}</td>'
            + f'<td class="col-q-avail"><span class="fit-badge {dcls}">{dlabel}</span></td>'
            + f'<td class="col-q-refs">{references_cell(c.get("references"))}</td>'
            + "</tr>"
        )

    head = (
        '<tr><th class="col-q-rank">Rank</th><th class="col-q-candidate">Candidate</th>'
        '<th class="col-q-rate">Response rate</th><th class="col-q-tox">Toxicity</th>'
        '<th class="col-q-avail">Available to her</th>'
        '<th class="col-q-refs">Key references</th></tr>'
    )
    basis_line = (
        f'\n!!! note "What this ranking orders by"\n    {basis}\n\n'
        if basis else "\n"
    )
    return "## Candidates assessed\n" + basis_line + _wrap_table(head, "".join(out))


def references_cell(refs) -> str:
    if not refs:
        return "&mdash;"
    links = []
    for r in refs:
        r = str(r)
        if r.lower().startswith("pmid:"):
            pid = r.split(":", 1)[1]
            links.append(f'<a href="https://pubmed.ncbi.nlm.nih.gov/{html.escape(pid)}">PMID&nbsp;{html.escape(pid)}</a>')
        elif r.upper().startswith("NCT"):
            links.append(f'<a href="https://clinicaltrials.gov/study/{html.escape(r)}">{html.escape(r)}</a>')
        else:
            links.append(html.escape(r))
    return "<br>".join(links)


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
            + f'<td class="col-q-criterion">{fmt(r.get("criterion"))}</td>'
            + f'<td class="col-q-result"><span class="fit-badge {cls}">{mark}</span></td>'
            + f'<td class="col-q-points">{fmt(points)}</td>'
            + f'<td class="col-q-finding">{fmt(r.get("finding"))}</td>'
            + "</tr>"
        )
    head = (
        '<tr><th class="col-q-criterion">Pre-registered criterion</th>'
        '<th class="col-q-result">Result</th><th class="col-q-points">Points toward</th>'
        '<th class="col-q-finding">What was found</th></tr>'
    )
    return (
        "## What would have answered this, decided before the search\n\n"
        + _wrap_table(head, "".join(rows))
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
                + f'<td class="col-q-dir">{html.escape(heading)}</td>'
                + f'<td class="col-q-claim">{fmt(e.get("claim"))}</td>'
                + f'<td class="col-q-strength">{fmt(e.get("strength"))}</td>'
                + f'<td class="col-q-popmatch">{fmt(e.get("population_match"))}</td>'
                + "</tr>"
            )
        return "".join(out)

    head = (
        '<tr><th class="col-q-dir">Direction</th><th class="col-q-claim">Finding</th>'
        '<th class="col-q-strength">Strength</th>'
        '<th class="col-q-popmatch">Population match</th></tr>'
    )
    body = block("evidence_for", "For") + block("evidence_against", "Against")
    return "## Evidence both ways\n\n" + _wrap_table(head, body)


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
            + f'<td class="col-q-seat">{fmt(d.get("persona"))}</td>'
            + f'<td class="col-q-position">{fmt(d.get("position"))}</td>'
            + f'<td class="col-q-carried">{html.escape(mark)}</td>'
            + "</tr>"
        )
    head = (
        '<tr><th class="col-q-seat">Board seat</th><th class="col-q-position">Position</th>'
        '<th class="col-q-carried">Into the answer</th></tr>'
    )
    return "## Where the board disagreed\n\n" + _wrap_table(head, "".join(out))


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

    # The ranked table leads. A reader arrives at a question report wanting the
    # options and their numbers, and burying that under several paragraphs of
    # prose makes them scroll for the thing they came for. The narrative and the
    # answer follow it and explain it; the ranking_basis callout travels with the
    # table itself, so the table is not stranded without its caveat.
    parts.append("\n" + render_candidates_table(ans))

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

    # A ranked candidate table whose ordering axis is unstated will be read as
    # ordering by the endpoint in the page heading, which is the failure this
    # column exists to prevent.
    cands = ans.get("candidates") or []
    if cands and not (ans.get("ranking_basis") or "").strip():
        problems.append(
            "candidates are ranked but ranking_basis is empty — the table will be read as "
            "ordering by the question's endpoint whether or not it does"
        )
    for c in cands:
        rr = c.get("response_rate") or {}
        if rr.get("value") and not rr.get("endpoint"):
            problems.append(
                f"candidate '{c.get('label')}' reports a rate with no endpoint — "
                "a composite rate is not a CR rate and the table must say which it is"
            )

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
