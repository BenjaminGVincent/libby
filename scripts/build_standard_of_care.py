#!/usr/bin/env python3
"""Render standard_of_care.jsonl into the case's "Standard of care options" page
plus its self-contained HTML and print-PDF companions.

This track is additive and deliberately parallel to the targetable-feature
ranking. The board, the PI, and the translator stay mechanism-scoped; this page
carries the options that are standard because a regulator approved them for this
population or a major society's guideline carries them. Nothing here removes,
reranks, or narrows a feature-targeted option, and the page says so in its own
legend so a reader cannot mistake one track for a filter on the other.

Outputs (under docs/cases/<slug>/):
  standard_of_care.md              mkdocs in-browser page (sortable HTML tables)
  <slug>-standard-of-care.html     self-contained, opens offline
  <slug>-standard-of-care.pdf      print-friendly, grouped by next step

Pure Python. Reuses the PDF / self-contained-HTML helpers in build_report.py so
every Libby track renders with one shared font stack, cover style, and CSS.
"""

from __future__ import annotations

import argparse
import html
import sys
from datetime import date, datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
# scripts/ is sys.path[0] when run as `python3 scripts/build_standard_of_care.py`,
# so build_report imports cleanly and its __main__ guard keeps it inert.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_report as br  # noqa: E402
from libbylib import load_jsonl  # noqa: E402

PAGE_TITLE = "Standard of care options"

# An endorsement older than this renders with a "re-check" marker. Guidelines
# version a few times a year; a claim verified more than two quarters ago is not
# wrong, but it is no longer evidence of current practice.
STALE_AFTER_DAYS = 180

# ---------- display vocab ----------

CONSIDERATION_LABELS = {
    "consider_now": "Consider now",
    "consider_at_next_decision_point": "Consider at next decision point",
    "requires_further_workup": "Requires further workup",
    "already_received": "Already received",
    "not_applicable": "Not applicable",
}

ELIGIBILITY_LABELS = {
    "eligible": "Eligible",
    "likely_eligible": "Likely eligible",
    "conditionally_eligible": "Conditionally eligible",
    "likely_ineligible": "Likely ineligible",
    "contraindicated": "Contraindicated",
    "already_received": "Already received",
    "unknown": "Not determinable from the record",
}

CATEGORY_LABELS = {
    "systemic_chemotherapy": "Systemic chemotherapy",
    "targeted_therapy": "Targeted therapy",
    "immunotherapy": "Immunotherapy",
    "endocrine_therapy": "Endocrine therapy",
    "radiotherapy": "Radiotherapy",
    "radiopharmaceutical": "Radiopharmaceutical",
    "surgery": "Surgery",
    "locoregional_therapy": "Locoregional therapy",
    "cellular_therapy": "Cellular therapy",
    "transplant": "Transplant",
    "supportive_care": "Supportive care",
    "surveillance": "Surveillance",
    "other": "Other",
}

LINE_LABELS = {
    "neoadjuvant": "Neoadjuvant",
    "adjuvant": "Adjuvant",
    "first_line": "First line",
    "maintenance": "Maintenance",
    "second_line": "Second line",
    "third_line_or_later": "Third line or later",
    "salvage": "Salvage",
    "any_line": "Any line",
    "not_applicable": "Not line-indexed",
}

INTENT_LABELS = {
    "curative": "curative intent",
    "life_prolonging": "life-prolonging intent",
    "disease_control": "disease-control intent",
    "symptom_palliation": "symptom palliation",
    "risk_reduction": "risk reduction",
}

MATCH_LABELS = {
    "matches_this_patient": "covers this patient",
    "partial_match": "partial population match",
    "different_population": "different population",
    "unclear": "population match unclear",
}

BIOMARKER_STATUS_LABELS = {
    "met": "threshold met",
    "not_met": "threshold not met",
    "not_measured": "never measured",
    "pending": "result pending",
    "unknown": "status unknown",
}

RELATION_LABELS = {
    "precedes_targeted_options": "Comes before the targeted options",
    "concurrent_with_targeted_options": "Can run alongside the targeted options",
    "follows_targeted_options": "Comes after the targeted options",
    "competes_for_same_line": "Competes for the same line of therapy",
    "may_foreclose_targeted_option": "May foreclose a targeted option",
    "may_be_foreclosed_by_targeted_option": "May be foreclosed by a targeted option",
    "independent": "Independent of the targeted options",
}

# Order the sequencing section so the trade-off relations lead. A reader scanning
# this section is looking for the decisions where one path costs the other.
RELATION_ORDER = {
    "competes_for_same_line": 0,
    "may_foreclose_targeted_option": 1,
    "may_be_foreclosed_by_targeted_option": 2,
    "precedes_targeted_options": 3,
    "concurrent_with_targeted_options": 4,
    "follows_targeted_options": 5,
    "independent": 6,
}

PRIORITY_ORDER = {"essential": 0, "high": 1, "medium": 2, "low": 3}
LINE_ORDER = {
    "neoadjuvant": 0,
    "first_line": 1,
    "maintenance": 2,
    "second_line": 3,
    "third_line_or_later": 4,
    "salvage": 5,
    "adjuvant": 6,
    "any_line": 7,
    "not_applicable": 8,
}

PRIORITY_BADGE = {
    "essential": ("essential", "fit-strong"),
    "high": ("high", "fit-partial"),
    "medium": ("medium", "fit-weak"),
    "low": ("low", "fit-none"),
}

# The page sections, in render order, keyed by consideration_status.
SECTIONS = [
    (
        "consider_now",
        "Options to consider now",
        "Standard options this patient is eligible for, with an endorsement that covers "
        "their situation, and no unresolved gate in front of them.",
    ),
    (
        "consider_at_next_decision_point",
        "Options at the next decision point",
        "Standard for a line this patient has not reached yet, or for a disease state "
        "that has not arrived. Listed now so the sequence is visible in advance.",
    ),
    (
        "requires_further_workup",
        "Standard options behind an open gate",
        "Endorsed for this patient's situation, but gated on a result that is missing, "
        "pending, or below threshold. The gate has to close before the option is real.",
    ),
    (
        "already_received",
        "Already received",
        "Carried so the report reads as a complete account of the standard options rather "
        "than a list that quietly omits what has been tried.",
    ),
    (
        "not_applicable",
        "Assessed and set aside",
        "Screened against this patient and found not to apply. Listed for the audit trail.",
    ),
]

# Prose fields the agent authors. These render verbatim into clinician-facing
# cells, so they carry the reporter's em-dash ban (see .claude/agents/reporter.md
# rule 1). The `—` the renderer itself emits for an empty cell is a placeholder,
# not prose, and is unaffected.
PROSE_FIELDS = ("rationale", "eligibility_rationale", "prior_exposure_note", "notes")
EM_DASH = "—"


class BuildError(Exception):
    """A contract violation that must block the build rather than render wrong."""


# ---------- helpers ----------


def fmt(v) -> str:
    if v is None or v == "":
        return "—"
    if isinstance(v, list):
        return "; ".join(html.escape(str(x)) for x in v) or "—"
    return html.escape(str(v))


def priority_badge(p: str | None) -> str:
    if not p:
        return "—"
    label, css = PRIORITY_BADGE.get(p, (p, "fit-none"))
    return f'<span class="fit-badge {css}">{html.escape(label)}</span>'


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
    if low.startswith(("http://", "https://")):
        return f'<a href="{html.escape(s)}">{html.escape(s)}</a>'
    if low.startswith(("guideline:", "fda:")):
        return f"<em>{html.escape(s.split(':', 1)[1].strip())}</em>"
    return html.escape(s)


def references_cell(refs: list[str] | None) -> str:
    if not refs:
        return "—"
    return "<br>".join(_ref_link(r) for r in refs)


def sort_key(r: dict) -> tuple:
    """Order rows by the table's own ranking when it has one.

    The Standard-of-care table numbers itself 1..n independently of the
    Experimental table's 1..m — they are co-equal tables, not one list split in
    two. Screens written before ranks existed fall back to the priority ordering
    they were built with, which is why `rank` sorts ahead of it rather than
    replacing it.
    """
    rank = r.get("rank")
    return (
        0 if isinstance(rank, int) else 1,
        rank if isinstance(rank, int) else 99,
        PRIORITY_ORDER.get(r.get("priority"), 99),
        LINE_ORDER.get(r.get("line_of_therapy"), 99),
        r.get("option_label") or "",
    )


def rank_cell(r: dict) -> str:
    """Lead cell: the row's rank within this table, or `—` on a legacy screen."""
    rank = r.get("rank")
    return f"<td>{rank}</td>" if isinstance(rank, int) else "<td>—</td>"


def _is_stale(row: dict, today: date | None = None) -> bool:
    """True when the row's endorsements were last checked long enough ago that a
    reader should re-verify before acting. Never blocks the build: a stale row is
    still the best record the case has, it just has to say so."""
    raw = row.get("last_verified_utc")
    if not raw:
        return False
    try:
        verified = date.fromisoformat(str(raw))
    except ValueError:
        return False
    today = today or datetime.now(timezone.utc).date()
    return (today - verified).days > STALE_AFTER_DAYS


def option_cell(r: dict) -> str:
    bits = [f"<strong>{fmt(r.get('option_label'))}</strong>"]
    meta = [
        CATEGORY_LABELS.get(r.get("category"), r.get("category")),
        LINE_LABELS.get(r.get("line_of_therapy"), r.get("line_of_therapy")),
        INTENT_LABELS.get(r.get("intent"), r.get("intent")),
    ]
    line = " · ".join(html.escape(str(m)) for m in meta if m)
    if line:
        bits.append(f'<small class="persona-line">{line}</small>')
    aliases = r.get("option_aliases") or []
    if aliases:
        bits.append(f"<small><em>also called:</em> {fmt(aliases)}</small>")
    return "<td>" + "<br>".join(bits) + "</td>"


def endorsement_cell(r: dict) -> str:
    """The column that carries the whole claim: who endorses this, for whom.

    `population_match` renders next to every entry because an endorsement written
    for a different population is an extrapolation, and a reader has to be able to
    see that without opening the citation.
    """
    ends = r.get("endorsements") or []
    if not ends:
        return "<td>—</td>"
    pieces = []
    for e in ends:
        src = html.escape(str(e.get("source") or ""))
        des = html.escape(str(e.get("designation") or ""))
        head = f"<strong>{src}</strong>" + (f" {des}" if des else "")
        tail = []
        match = MATCH_LABELS.get(e.get("population_match"))
        if match:
            tail.append(html.escape(match))
        if e.get("version_or_date"):
            tail.append(html.escape(str(e["version_or_date"])))
        if tail:
            head += f' <small class="persona-line">({" · ".join(tail)})</small>'
        if e.get("indication_text"):
            head += f"<br><small>{html.escape(str(e['indication_text']))}</small>"
        if e.get("citation"):
            head += f"<br><small>{_ref_link(str(e['citation']))}</small>"
        pieces.append(f"<div>{head}</div>")
    stale = ' <small class="persona-line">(re-check: verified over 6 months ago)</small>' if _is_stale(r) else ""
    verified = f'<div><small>verified {fmt(r.get("last_verified_utc"))}{stale}</small></div>'
    return "<td>" + "".join(pieces) + verified + "</td>"


def eligibility_cell(r: dict) -> str:
    status = ELIGIBILITY_LABELS.get(r.get("eligibility_status"), r.get("eligibility_status") or "—")
    bits = [f"<strong>{html.escape(str(status))}</strong>"]
    if r.get("eligibility_rationale"):
        bits.append(f"<small>{html.escape(str(r['eligibility_rationale']))}</small>")
    for bf in r.get("blocking_factors") or []:
        bits.append(f'<small class="persona-line">blocker: {html.escape(str(bf))}</small>')
    if r.get("prior_exposure_note"):
        bits.append(f"<small><em>prior exposure:</em> {html.escape(str(r['prior_exposure_note']))}</small>")
    gate = r.get("biomarker_requirement") or {}
    if gate.get("required"):
        gate_bits = html.escape(str(gate.get("biomarker") or "biomarker"))
        if gate.get("threshold"):
            gate_bits += f" {html.escape(str(gate['threshold']))}"
        st = BIOMARKER_STATUS_LABELS.get(gate.get("status_in_case"), gate.get("status_in_case") or "")
        bits.append(f'<small class="persona-line">gate: {gate_bits} ({html.escape(str(st))})</small>')
    return "<td>" + "<br>".join(bits) + "</td>"


def evidence_cell(r: dict) -> str:
    ev = r.get("evidence") or []
    if not ev:
        return "<td>—</td>"
    pieces = []
    for e in ev:
        line = f"<strong>{html.escape(str(e.get('source_label') or ''))}</strong>"
        meta = [e.get("design")]
        if e.get("n"):
            meta.append(f"n={e['n']}")
        meta_line = " · ".join(html.escape(str(m)) for m in meta if m)
        if meta_line:
            line += f' <small class="persona-line">({meta_line})</small>'
        if e.get("effect_size"):
            line += f"<br><small>{html.escape(str(e['effect_size']))}</small>"
        links = []
        if e.get("pmid"):
            links.append(_ref_link(f"pmid:{e['pmid']}"))
        if e.get("nct_id"):
            links.append(_ref_link(f"nct:{e['nct_id']}"))
        if links:
            line += "<br><small>" + " · ".join(links) + "</small>"
        pieces.append(f"<div>{line}</div>")
    return "<td>" + ("".join(pieces) or "—") + "</td>"


def _table(head: str, body_rows: list[str]) -> str:
    return (
        '<div class="trial-table-wrap">\n'
        '  <div class="trial-scroll">\n'
        '    <table class="trial-table">\n'
        f"      <thead><tr>{head}</tr></thead>\n"
        "      <tbody>\n" + "\n".join(body_rows) + "\n      </tbody>\n"
        "    </table>\n"
        "  </div>\n"
        "</div>\n"
    )


# ---------- tables ----------


def render_option_table(rows: list[dict]) -> str:
    if not rows:
        return ""
    head = (
        "<th>Rank</th><th>Priority</th><th>Option</th><th>What makes it standard</th>"
        "<th>Fit to this patient</th><th>Key evidence</th>"
        "<th>Toxicities that would change the decision</th>"
        "<th>Rationale</th><th>References</th>"
    )
    body = []
    for r in rows:
        body.append(
            "    <tr>"
            f"{rank_cell(r)}"
            f"<td>{priority_badge(r.get('priority'))}</td>"
            f"{option_cell(r)}"
            f"{endorsement_cell(r)}"
            f"{eligibility_cell(r)}"
            f"{evidence_cell(r)}"
            f"<td>{fmt(r.get('toxicity_highlights'))}</td>"
            f"<td>{fmt(r.get('rationale'))}</td>"
            f"<td>{references_cell(r.get('references'))}</td>"
            "</tr>"
        )
    return _table(head, body)


def render_received_table(rows: list[dict]) -> str:
    if not rows:
        return ""
    head = "<th>Option</th><th>What was given</th><th>What makes it standard</th><th>Note</th>"
    body = []
    for r in rows:
        body.append(
            "    <tr>"
            f"{option_cell(r)}"
            f"<td>{fmt(r.get('prior_exposure_note'))}</td>"
            f"{endorsement_cell(r)}"
            f"<td>{fmt(r.get('rationale'))}</td>"
            "</tr>"
        )
    return _table(head, body)


def render_sequencing(rows: list[dict]) -> str:
    """How the standard options sit alongside the feature-targeted ranking.

    This is the one place the two tracks touch, and it runs one way: it names
    sequencing consequences and never reranks or removes a targeted option.
    """
    tagged = [r for r in rows if (r.get("relationship_to_targeted_options") or {}).get("relation")]
    if not tagged:
        return ""
    grouped: dict[str, list[dict]] = {}
    for r in tagged:
        grouped.setdefault(r["relationship_to_targeted_options"]["relation"], []).append(r)

    lines = [
        "## How these sit alongside the experimental options\n",
        "_These options and the experimental ranking are two co-equal tables, and nothing "
        "here changes that ranking. What this section adds is the sequencing: where a standard "
        "option and an experimental one compete for the same line, and where taking one would "
        "close the door on the other._\n",
    ]
    for relation in sorted(grouped, key=lambda k: RELATION_ORDER.get(k, 99)):
        lines.append(f"**{RELATION_LABELS.get(relation, relation)}**\n")
        for r in sorted(grouped[relation], key=sort_key):
            note = (r.get("relationship_to_targeted_options") or {}).get("note") or ""
            related = (r.get("relationship_to_targeted_options") or {}).get("related_intervention_ids") or []
            suffix = f" (interacts with: {', '.join(related)})" if related else ""
            lines.append(f"- **{r.get('option_label')}**: {note}{suffix}".rstrip())
        lines.append("")
    return "\n".join(lines)


# ---------- coverage + pre-flight ----------


def compute_summary(rows: list[dict]) -> dict:
    by_status: dict[str, int] = {}
    for r in rows:
        key = r.get("consideration_status") or "unknown"
        by_status[key] = by_status.get(key, 0) + 1
    return {
        "total": len(rows),
        "by_status": by_status,
        "actionable": by_status.get("consider_now", 0),
        "gated": by_status.get("requires_further_workup", 0),
        "received": by_status.get("already_received", 0),
        "stale": sum(1 for r in rows if _is_stale(r)),
    }


def preflight(rows: list[dict], narrative: str = "") -> None:
    """Block the build on a contract violation rather than publishing a wrong page.

    Every check here maps to a way this specific report could mislead a treating
    team: an option presented as actionable when a gate is open, when the patient
    already progressed on it, or when the only endorsement behind it was written
    for a different population.
    """
    problems: list[str] = []

    if EM_DASH in narrative:
        problems.append(
            "standard_of_care_report.md: em-dash (U+2014) in the screener narrative; "
            "use a period, comma, or colon"
        )

    for r in rows:
        rid = r.get("soc_id") or r.get("option_label") or "<row>"

        for field in PROSE_FIELDS:
            value = r.get(field)
            if isinstance(value, str) and EM_DASH in value:
                problems.append(
                    f"{rid}: em-dash (U+2014) in `{field}`; use a period, comma, colon, "
                    "or an en-dash inside a numeric range"
                )

        endorsements = r.get("endorsements") or []
        if not endorsements:
            problems.append(
                f"{rid}: no `endorsements`; an option with no approval and no guideline "
                "carriage is not standard of care and does not belong on this page"
            )
        if not r.get("last_verified_utc"):
            problems.append(
                f"{rid}: missing `last_verified_utc`; a standard-of-care claim with no "
                "verification date cannot be re-checked"
            )

        status = r.get("consideration_status")
        gate = r.get("biomarker_requirement") or {}
        gate_open = gate.get("required") and gate.get("status_in_case") in (
            "not_met", "not_measured", "pending", "unknown",
        )

        if status == "consider_now":
            if gate_open:
                problems.append(
                    f"{rid}: `consider_now` with an open biomarker gate "
                    f"({gate.get('biomarker')}: {gate.get('status_in_case')}); use "
                    "`requires_further_workup` until the gate closes"
                )
            if r.get("eligibility_status") in ("likely_ineligible", "contraindicated", "already_received"):
                problems.append(
                    f"{rid}: `consider_now` contradicts eligibility_status "
                    f"`{r.get('eligibility_status')}`"
                )
            covering = [
                e for e in endorsements
                if e.get("population_match") in ("matches_this_patient", "partial_match")
            ]
            if endorsements and not covering:
                problems.append(
                    f"{rid}: `consider_now` but no endorsement covers this patient "
                    "(every entry is `different_population` or `unclear`); this is an "
                    "extrapolation, not standard of care for this case"
                )

        if r.get("eligibility_status") == "already_received" and not r.get("prior_exposure_note"):
            problems.append(
                f"{rid}: `already_received` requires a `prior_exposure_note` recording what "
                "was given, the best response, and why it stopped"
            )

    if problems:
        raise BuildError(
            "build_standard_of_care: refusing to render.\n  - " + "\n  - ".join(problems)
        )


# ---------- page ----------


def _sibling_ref(case_docs: Path | None, filename: str, label: str) -> str:
    """Link a sibling page only when it exists; a link to a missing page breaks
    `mkdocs build --strict`, and this track can run before the rest of the pipeline."""
    if case_docs is not None and (case_docs / filename).exists():
        return f"[{label}]({filename})"
    return label


def _legend(case_docs: Path | None) -> str:
    return (
        '!!! note "Reading this report"\n'
        "    An option earns a row here only if a regulator approved it for a population "
        "that includes this patient, or a major society's guideline carries it. **What "
        "makes it standard** names the endorsing body and, next to it, whether that "
        "endorsement was written for this patient's situation or for a different "
        "population. **Fit to this patient** is judged against the case profile alone, so "
        "an option the patient has already had and progressed on is marked rather than "
        "re-offered. This page is additive: it runs alongside the "
        f"{_sibling_ref(case_docs, 'recommendations.md', 'ranked recommendations')} and "
        "does not narrow, rerank, or filter the targeted options that ranking surfaces.\n"
    )


def _downloads_block(slug: str) -> str:
    items = [
        (f"{slug}-standard-of-care.html", f"{PAGE_TITLE} (offline HTML)",
         "the same standard-of-care assessment, self-contained HTML that opens offline"),
        (f"{slug}-standard-of-care.pdf", f"{PAGE_TITLE} (PDF)",
         "print-friendly, grouped by next step"),
    ]
    lines = ["## Downloads\n"]
    for name, label, blurb in items:
        lines.append(f"- [{label}]({html.escape(name)}) — {blurb}")
    lines.append("")
    return "\n".join(lines)


def load_narrative(case_dir: Path) -> str:
    """The screener's opening narrative, inlined verbatim when present.

    Same contract as the other tracks: the prose is the agent's, the tables are
    the renderer's, and neither rewrites the other.
    """
    path = case_dir / "standard_of_care_report.md"
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()


def _nav_line(case_docs: Path) -> str:
    candidates = [
        ("index.md", "Back to case"),
        ("recommendations.md", "Recommendations"),
        ("target_validation.md", "Target validation"),
        ("biomarker_survey.md", "Biomarker survey"),
        ("trials.md", "Trials"),
        ("evidence.md", "Evidence"),
        ("accessibility.md", "Access guide"),
        ("board.md", "Board"),
    ]
    links = [f"[{label}]({name})" for name, label in candidates if (case_docs / name).exists()]
    return " · ".join(links) + "\n" if links else ""


def render_page(slug: str, rows: list[dict], narrative: str = "",
                case_docs: Path | None = None) -> str:
    summary = compute_summary(rows)

    parts = [
        '<meta name="robots" content="noindex">\n',
        f"# {PAGE_TITLE} — `{slug}`\n",
        "_The treatment strategies that are standard for this patient's situation, meaning "
        "a regulator approved them for a population that includes this patient or a major "
        "academic or clinical-society guideline carries them. This is one of the case's two "
        "therapeutic tables and frequently carries its primary recommendation; the experimental "
        "ranking is the other, and neither narrows the other._\n",
        _downloads_block(slug),
        f"_{summary['total']} standard options assessed: {summary['actionable']} to consider "
        f"now, {summary['gated']} behind an open gate, {summary['received']} already "
        f"received._\n",
    ]

    if narrative:
        parts.append(narrative + "\n")

    for status, heading, blurb in SECTIONS:
        section_rows = sorted([r for r in rows if r.get("consideration_status") == status], key=sort_key)
        if not section_rows:
            continue
        if status == "not_applicable":
            # Audit trail rather than a finding: collapse it so it does not compete
            # with the options a reader is actually here for.
            parts.append("## Assessed and set aside\n")
            parts.append(
                f'??? note "{len(section_rows)} option(s) screened against this patient and set aside"\n'
                f"    {blurb}\n\n"
                + "\n".join(
                    f"    - **{html.escape(str(r.get('option_label')))}**: "
                    f"{html.escape(str(r.get('rationale') or ''))}"
                    for r in section_rows
                )
                + "\n"
            )
            continue
        parts.append(f"## {heading}\n")
        parts.append(f"_{blurb}_\n")
        if status == "already_received":
            parts.append(render_received_table(section_rows))
        else:
            parts.append(render_option_table(section_rows))

    sequencing = render_sequencing(rows)
    if sequencing:
        parts.append(sequencing)

    parts.append(_legend(case_docs))
    if case_docs is not None:
        nav = _nav_line(case_docs)
        if nav:
            parts.append(nav)
    parts.append(
        '!!! danger disclaimer "Decision support, not medical advice"\n'
        "    Libby is experimental. Standard of care is set by a treating team using the\n"
        "    full clinical record, not by this page. Guideline versions and approvals move,\n"
        "    eligibility here is inferred from a scrubbed profile rather than an\n"
        "    examination, and nothing on this page is a recommendation to start, stop, or\n"
        "    sequence a treatment. See [PHI policy](../../phi_policy.md).\n"
    )
    return "\n".join(parts) + "\n"


# ---------- print PDF ----------


def _deep_markdown(slug: str, rows: list[dict], narrative: str = "") -> str:
    summary = compute_summary(rows)
    lines: list[str] = [f"# {PAGE_TITLE}\n"]
    lines.append(
        "The treatment strategies that are standard for this patient's situation, meaning "
        "a regulator approved them for a population that includes this patient or a major "
        "academic or clinical-society guideline carries them. This is one of the case's two "
        "therapeutic tables and frequently carries its primary recommendation; the experimental "
        "ranking is the other, and neither narrows the other.\n"
    )
    lines.append(
        f"**Assessed:** {summary['total']} standard options. "
        f"**Consider now:** {summary['actionable']}. "
        f"**Behind an open gate:** {summary['gated']}. "
        f"**Already received:** {summary['received']}.\n"
    )

    if narrative:
        lines.append(narrative + "\n")

    for status, heading, blurb in SECTIONS:
        section_rows = sorted([r for r in rows if r.get("consideration_status") == status], key=sort_key)
        if not section_rows:
            continue
        lines.append(f"## {heading}\n")
        lines.append(blurb + "\n")
        for r in section_rows:
            # Lead the heading with this table's own rank when the screen carries
            # one, so the print surface reads in the same order as the web table.
            _rk = r.get("rank")
            _prefix = f"{_rk}. " if isinstance(_rk, int) else ""
            lines.append(f"### {_prefix}{r.get('option_label')}\n")
            meta = [
                f"**Priority:** {r.get('priority') or '-'}",
                f"**Modality:** {CATEGORY_LABELS.get(r.get('category'), r.get('category') or '-')}",
                f"**Line:** {LINE_LABELS.get(r.get('line_of_therapy'), r.get('line_of_therapy') or '-')}",
                f"**Intent:** {INTENT_LABELS.get(r.get('intent'), r.get('intent') or '-')}",
            ]
            lines.append("  ".join(meta) + "\n")

            ends = r.get("endorsements") or []
            if ends:
                lines.append("**What makes it standard.**\n")
                for e in ends:
                    tail = " · ".join(
                        str(x) for x in (
                            MATCH_LABELS.get(e.get("population_match")),
                            e.get("version_or_date"),
                        ) if x
                    )
                    head = f"- {e.get('source')} {e.get('designation') or ''}".rstrip()
                    lines.append(head + (f" ({tail})" if tail else ""))
                    if e.get("indication_text"):
                        lines.append(f"    - covers: {e['indication_text']}")
                lines.append("")

            lines.append(
                f"**Fit to this patient.** "
                f"{ELIGIBILITY_LABELS.get(r.get('eligibility_status'), r.get('eligibility_status') or '-')}"
                + (f" {r['eligibility_rationale']}" if r.get("eligibility_rationale") else "")
                + "\n"
            )
            for bf in r.get("blocking_factors") or []:
                lines.append(f"- blocker: {bf}")
            if r.get("blocking_factors"):
                lines.append("")
            if r.get("prior_exposure_note"):
                lines.append(f"**Prior exposure.** {r['prior_exposure_note']}\n")

            gate = r.get("biomarker_requirement") or {}
            if gate.get("required"):
                st = BIOMARKER_STATUS_LABELS.get(gate.get("status_in_case"), gate.get("status_in_case") or "-")
                thr = f" {gate['threshold']}" if gate.get("threshold") else ""
                lines.append(f"**Biomarker gate.** {gate.get('biomarker') or 'biomarker'}{thr} ({st})\n")

            if r.get("rationale"):
                lines.append(r["rationale"] + "\n")

            ev = r.get("evidence") or []
            if ev:
                lines.append("**Key evidence.**\n")
                for e in ev:
                    bits = [str(e.get("source_label") or "")]
                    if e.get("design"):
                        bits.append(str(e["design"]))
                    if e.get("n"):
                        bits.append(f"n={e['n']}")
                    if e.get("effect_size"):
                        bits.append(str(e["effect_size"]))
                    lines.append("- " + " · ".join(b for b in bits if b))
                lines.append("")

            if r.get("toxicity_highlights"):
                lines.append("**Toxicities that would change the decision.** "
                             + "; ".join(str(x) for x in r["toxicity_highlights"]) + "\n")

            rel = r.get("relationship_to_targeted_options") or {}
            if rel.get("relation"):
                note = f" {rel['note']}" if rel.get("note") else ""
                lines.append(
                    f"**Alongside the targeted options.** "
                    f"{RELATION_LABELS.get(rel['relation'], rel['relation'])}.{note}\n"
                )

            lines.append(f"**Last verified.** {r.get('last_verified_utc') or '-'}\n")
            if r.get("references"):
                lines.append("**References.** " + "; ".join(str(x) for x in r["references"]) + "\n")

    return "\n".join(lines)


def _make_pdf(slug: str, rows: list[dict], out_path: Path, narrative: str = "") -> None:
    try:
        from fpdf import FPDF
    except ImportError as e:  # pragma: no cover
        raise SystemExit(
            "build_standard_of_care: missing dependency `fpdf2`.\n  pip install fpdf2"
        ) from e

    today = datetime.now(timezone.utc).date().isoformat()

    class SocPDF(FPDF):
        def footer(self_):
            if self_.page_no() <= 1:
                return
            self_.set_y(-12)
            self_.set_font(br._FONT_FAMILY, "I", 8)
            self_.set_text_color(*br.INK_MUTED)
            self_.cell(
                0, 6,
                br._ascii_fallback(
                    f"{self_.page_no()} of {{nb}}    ·    Libby — standard of care    ·    {slug}"
                ),
                align="C",
            )

    pdf = SocPDF(orientation="P", unit="mm", format="Letter")
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(left=18, top=20, right=18)
    pdf.alias_nb_pages()
    br._register_unicode_font(pdf)
    br._render_cover(
        pdf, slug,
        f"{PAGE_TITLE} — approved and guideline-endorsed strategies",
        today, "LIBBY — STANDARD OF CARE",
        br.COVER_BG, br._DISCLAIMER_CLINICIAN,
    )
    pdf.add_page()
    br._render_markdown_block(pdf, _deep_markdown(slug, rows, narrative), top_h1=True)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(out_path))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug")
    args = parser.parse_args()
    slug = args.slug

    case_dir = REPO / "data" / "cases" / slug
    case_docs = REPO / "docs" / "cases" / slug
    rows = load_jsonl(case_dir / "standard_of_care.jsonl")

    page = case_docs / "standard_of_care.md"
    html_dst = case_docs / f"{slug}-standard-of-care.html"
    pdf_dst = case_docs / f"{slug}-standard-of-care.pdf"

    # No rows → the screener has not run for this case. Don't leave an empty page
    # for the case-output / downloads injectors to surface; strip stale artifacts.
    if not rows:
        for stale in (page, html_dst, pdf_dst):
            if stale.exists():
                stale.unlink()
        print(f"no standard_of_care.jsonl rows for {slug}; nothing rendered")
        return 0

    narrative = load_narrative(case_dir)
    try:
        preflight(rows, narrative)
    except BuildError as e:
        print(str(e), file=sys.stderr)
        return 1

    case_docs.mkdir(parents=True, exist_ok=True)
    page_md = render_page(slug, rows, narrative, case_docs)
    page.write_text(page_md, encoding="utf-8")
    print(f"wrote {page} ({len(rows)} rows)")

    html_out = br._render_self_contained_html_page(
        slug, f"Libby {PAGE_TITLE.lower()} — {slug}", PAGE_TITLE, page_md,
    )
    html_dst.write_text(html_out, encoding="utf-8")
    print(f"built {html_dst}")

    _make_pdf(slug, rows, pdf_dst, narrative)
    print(f"built {pdf_dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
