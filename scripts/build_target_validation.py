#!/usr/bin/env python3
"""Render target_validation.jsonl → docs/cases/<slug>/target_validation.md.

The page is grouped by feature (one H2 per profile.json::targetable_features[]
entry) with a single table per feature listing the recommended biomarkers /
assays / functional studies that would harden the target call. Rows are
sorted within each feature by (priority, decision_relevance) so the
load-bearing gating tests sit at the top.
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from collections import OrderedDict
from pathlib import Path
from libbylib import load_jsonl

REPO = Path(__file__).resolve().parent.parent

PRIORITY_ORDER = {"essential": 0, "high": 1, "medium": 2, "low": 3}
DECISION_ORDER = {
    "gates_intervention": 0,
    "confirms_target_call": 1,
    "refines_target_subtype": 2,
    "informs_resistance": 3,
    "informs_prognosis": 4,
    "informs_microenvironment": 5,
    "informs_germline_implications": 6,
    None: 7,
}

PRIORITY_BADGE = {
    "essential": ("essential", "fit-strong"),
    "high": ("high", "fit-partial"),
    "medium": ("medium", "fit-weak"),
    "low": ("low", "fit-none"),
}

TEST_TYPE_LABEL = {
    "confirmatory": "confirmatory",
    "orthogonal_validation": "orthogonal validation",
    "heterogeneity": "heterogeneity",
    "subtyping": "subtyping",
    "co_mutation": "co-mutation",
    "resistance_marker": "resistance marker",
    "functional_assay": "functional assay",
    "microenvironment": "microenvironment",
    "germline": "germline",
}




def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


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


def gates_cell(rows: list[str] | None) -> str:
    if not rows:
        return "—"
    pieces: list[str] = []
    for g in rows:
        gs = str(g)
        if gs.upper().startswith("NCT"):
            pieces.append(
                f'<a href="https://clinicaltrials.gov/study/{html.escape(gs)}">{html.escape(gs)}</a>'
            )
        else:
            pieces.append(f"<code>{html.escape(gs)}</code>")
    return ", ".join(pieces)


def references_cell(refs: list[str] | None) -> str:
    if not refs:
        return "—"
    pieces: list[str] = []
    for r in refs:
        rs = str(r)
        if rs.lower().startswith("pmid:"):
            pid = rs.split(":", 1)[1].strip()
            pieces.append(
                f'<a href="https://pubmed.ncbi.nlm.nih.gov/{html.escape(pid)}">PMID&nbsp;{html.escape(pid)}</a>'
            )
        elif rs.lower().startswith("nct:"):
            nid = rs.split(":", 1)[1].strip()
            pieces.append(
                f'<a href="https://clinicaltrials.gov/study/{html.escape(nid)}">{html.escape(nid)}</a>'
            )
        elif rs.lower().startswith("guideline:"):
            label = rs.split(":", 1)[1].strip()
            pieces.append(f"<em>{html.escape(label)}</em>")
        else:
            pieces.append(html.escape(rs))
    return "<br>".join(pieces)


def sort_key(r: dict) -> tuple:
    return (
        PRIORITY_ORDER.get(r.get("priority"), 99),
        DECISION_ORDER.get(r.get("decision_relevance"), 99),
        r.get("validation_id") or "",
    )


def providers_cell(providers: list[dict] | None) -> str:
    """Compact per-provider list. Each provider renders as a bold name + brand
    inline + contact line(s), one provider per row. The provider with
    `preferred: true` gets a leading ★ + a yellow 'preferred' badge and is
    moved to the top of the stack."""
    if not providers:
        return "—"
    # Sort: preferred first, then by name (stable for ties).
    sorted_providers = sorted(
        [p for p in providers if p and p.get("name")],
        key=lambda p: (0 if p.get("preferred") else 1, str(p.get("name") or "")),
    )
    pieces: list[str] = []
    for p in sorted_providers:
        is_preferred = bool(p.get("preferred"))
        name_html = html.escape(str(p["name"]))
        head_bits = [f"<strong>{name_html}</strong>"]
        brand = p.get("assay_brand")
        if brand:
            head_bits.append(f"<em>{html.escape(str(brand))}</em>")
        head = " · ".join(head_bits)
        if is_preferred:
            head += ' <span class="fit-badge fit-strong">preferred</span>'
        contacts: list[str] = []
        url = p.get("contact_url")
        if url:
            contacts.append(f'<a href="{html.escape(str(url))}">test info</a>')
        address = p.get("address")
        if address:
            contacts.append(html.escape(str(address)))
        phone = p.get("contact_phone")
        if phone:
            contacts.append(html.escape(str(phone)))
        email = p.get("contact_email")
        if email:
            contacts.append(f'<a href="mailto:{html.escape(str(email))}">{html.escape(str(email))}</a>')
        contact_line = " · ".join(contacts) if contacts else "—"
        notes = p.get("notes")
        flag = ""
        if p.get("us_based") is True and not is_preferred:
            flag = ' <span class="fit-badge fit-strong">US</span>'
        elif p.get("us_based") is False:
            flag = ' <span class="fit-badge fit-weak">non-US</span>'
        pieces.append(
            f"<div>{head}{flag}<br><small>{contact_line}</small>"
            + (f"<br><small><em>{html.escape(str(notes))}</em></small>" if notes else "")
            + "</div>"
        )
    return "<br>".join(pieces) if pieces else "—"


def decision_gated_cell(r: dict) -> str:
    val = r.get("decision_gated")
    if val:
        return html.escape(str(val))
    # Fall back to a derived label when the row hasn't been backfilled yet.
    gates = r.get("gates_intervention") or []
    if gates:
        return html.escape(", ".join(str(g) for g in gates))
    rel = r.get("decision_relevance")
    if rel:
        return html.escape(str(rel).replace("_", " "))
    return "—"


def render_table(rows: list[dict]) -> str:
    if not rows:
        return "_No validation rows for this feature._\n"
    head = (
        "<th>Priority</th><th>Test</th><th>Type</th>"
        "<th>Modality</th><th>Tissue</th><th>Turnaround</th>"
        "<th>Decision gated</th><th>Rationale</th>"
        "<th>Providers</th><th>References</th>"
    )
    body: list[str] = []
    for r in rows:
        body.append(
            "    <tr>"
            f"<td>{priority_badge(r.get('priority'))}</td>"
            f"<td><strong>{fmt(r.get('test_name'))}</strong></td>"
            f"<td>{html.escape(TEST_TYPE_LABEL.get(r.get('test_type', ''), r.get('test_type') or '—'))}</td>"
            f"<td>{fmt(r.get('assay_modality'))}</td>"
            f"<td>{fmt(r.get('tissue_required_estimate') or r.get('tissue_type'))}</td>"
            f"<td>{fmt(r.get('turnaround_estimate'))}</td>"
            f"<td>{decision_gated_cell(r)}</td>"
            f"<td>{fmt(r.get('rationale'))}</td>"
            f"<td>{providers_cell(r.get('providers'))}</td>"
            f"<td>{references_cell(r.get('references'))}</td>"
            "</tr>"
        )
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


def render_survey_handoffs(rows: list[dict], survey: list[dict]) -> str:
    """Biomarkers the survey measured but could not call decision-grade.

    The preclinical_biomarker_surveyor finds these; hardening them is this
    report's job. Rendering them here (rather than only in the biomarker survey)
    keeps the handoff visible: a gap that was found and then dropped shows up as
    an unaddressed row instead of disappearing between two pages.
    """
    handoffs = [r for r in survey if r.get("handoff_to_target_validator")]
    if not handoffs:
        return ""

    answered = {r.get("source_survey_id") for r in rows if r.get("source_survey_id")}
    n_open = sum(1 for h in handoffs if h.get("survey_id") not in answered)

    head = (
        "<th>Biomarker</th><th>What is on file</th><th>Why it is not decision-grade</th>"
        "<th>Hardening step</th><th>Status</th>"
    )
    body: list[str] = []
    for h in sorted(handoffs, key=lambda r: (PRIORITY_ORDER.get(r.get("priority"), 99),
                                             r.get("biomarker_label") or "")):
        sid = h.get("survey_id")
        matched = [r for r in rows if r.get("source_survey_id") == sid]
        if matched:
            step = "<br>".join(f"<strong>{fmt(m.get('test_name'))}</strong>" for m in matched)
            status = '<span class="fit-badge fit-strong">addressed above</span>'
        else:
            step = "—"
            status = '<span class="fit-badge fit-weak">not yet addressed</span>'
        body.append(
            "    <tr>"
            f"<td><strong>{fmt(h.get('biomarker_label'))}</strong><br>"
            f"<small class=\"persona-line\">{priority_badge(h.get('priority'))}</small></td>"
            f"<td>{fmt(h.get('status_evidence'))}</td>"
            f"<td>{fmt(h.get('hardening_gap'))}</td>"
            f"<td>{step}</td>"
            f"<td>{status}</td>"
            "</tr>"
        )

    n = len(handoffs)
    noun = "biomarker" if n == 1 else "biomarkers"
    verb = "has" if n == 1 else "have"
    if n_open:
        open_clause = (
            f", and {'it' if n_open == n == 1 else f'{n_open} of them'} "
            f"{'has' if n_open == 1 else 'have'} no hardening step on this page yet."
        )
    else:
        open_clause = "."

    parts = [
        "## Measured, but not to decision resolution\n",
        f"_{n} {noun} from the "
        "[Selected general biomarker report](biomarker_survey.md) "
        f"{verb} a result on file that cannot carry a treatment decision as it stands"
        + open_clause
        + " These are distinct from the per-feature workup below: the target call is not "
        "in question, the resolution of the existing result is._\n",
        _table_wrap(head, body),
    ]
    return "\n".join(parts)


def _table_wrap(head: str, body: list[str]) -> str:
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


def group_rows_by_feature(rows: list[dict], features: list[dict]) -> "OrderedDict[str, list[dict]]":
    grouped: "OrderedDict[str, list[dict]]" = OrderedDict()
    for f in features:
        name = f.get("feature") or ""
        if name:
            grouped.setdefault(name, [])
    for r in rows:
        name = r.get("feature") or "(unspecified feature)"
        grouped.setdefault(name, []).append(r)
    for name in grouped:
        grouped[name].sort(key=sort_key)
    return grouped


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    args = parser.parse_args()
    slug = args.slug

    case_dir = REPO / "data" / "cases" / slug
    rows = load_jsonl(case_dir / "target_validation.jsonl")
    survey = load_jsonl(case_dir / "biomarker_survey.jsonl")
    profile = load_json(case_dir / "profile.json")
    features = profile.get("targetable_features") or []

    n_essential = sum(1 for r in rows if r.get("priority") == "essential")
    n_gates = sum(1 for r in rows if r.get("decision_relevance") == "gates_intervention")

    grouped = group_rows_by_feature(rows, features)

    parts: list[str] = [
        '<meta name="robots" content="noindex">\n',
        f"# Target validation — `{slug}`\n",
    ]

    if not rows:
        parts.append("_No target-validation rows yet. Run `/target_validator <slug>` to populate._\n")
    else:
        parts.append(
            f"_{len(rows)} validation rows across {len(grouped)} feature(s) — "
            f"{n_essential} essential, {n_gates} gating an intervention. "
            "Sorted within each feature by priority, then by decision relevance._\n"
        )
        parts.append(
            "_Essential / gates-intervention rows are the diagnostic prerequisites that must "
            "resolve before any feature-targeting therapy can be chosen. "
            "Rows tagged `confirms_target_call` harden the target call without gating a "
            "specific therapy; resistance / co-mutation / microenvironment rows refine "
            "sequencing and risk._\n"
        )

    for feature, frows in grouped.items():
        parts.append(f"## {html.escape(feature)}\n")
        parts.append(render_table(frows))

    handoffs = render_survey_handoffs(rows, survey)
    if handoffs:
        parts.append(handoffs)

    nav = [
        "[Back to case](index.md)", "[Trials](trials.md)", "[Evidence](evidence.md)",
        "[Manuscripts](manuscripts.md)", "[Board](board.md)",
        "[Recommendations](recommendations.md)",
    ]
    # Conditional: linking a page that was never rendered would break `mkdocs
    # build --strict` for every case that has not run the survey.
    if survey:
        nav.append("[Biomarker survey](biomarker_survey.md)")
    parts.append(" · ".join(nav) + "\n")
    parts.append(
        '!!! danger disclaimer "Decision support, not medical advice"\n'
        "    Libby is experimental. The validation tests on this page are decision-support;\n"
        "    confirm assay availability, current standards, and clinical relevance with the\n"
        "    treating team and the local pathology service.\n"
        "    See [PHI policy](../../phi_policy.md).\n"
    )

    body_md = "\n".join(parts) + "\n"
    dst = REPO / "docs" / "cases" / slug / "target_validation.md"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(body_md, encoding="utf-8")
    print(f"wrote {dst} ({len(rows)} rows, {n_essential} essential, {n_gates} gating)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
