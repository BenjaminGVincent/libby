#!/usr/bin/env python3
"""Render biomarker_survey.jsonl into the case's "Selected general biomarker
report" page plus its self-contained HTML and print-PDF companions.

Where build_target_validation.py renders the workup that hardens a feature the
case already claims, this renders the complement: the biomarkers on the selected
panel that this patient has NOT been tested for, and the ones tested to a
resolution that cannot carry a treatment decision.

Outputs (under docs/cases/<slug>/):
  biomarker_survey.md              mkdocs in-browser page (sortable HTML tables)
  <slug>-biomarker-survey.html     self-contained, opens offline
  <slug>-biomarker-survey.pdf      print-friendly, grouped by recommended action

Pure Python. Reuses the PDF / self-contained-HTML helpers in build_report.py so
every Libby track renders with one shared font stack, cover style, and CSS.
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
# scripts/ is sys.path[0] when run as `python3 scripts/build_biomarker_survey.py`,
# so build_report imports cleanly and its __main__ guard keeps it inert.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_report as br  # noqa: E402
from libbylib import load_jsonl  # noqa: E402

PANEL_PATH = REPO / "data" / "reference" / "selected_biomarker_panel.json"
AGNOSTIC_PATH = REPO / "data" / "reference" / "tumor_agnostic_biomarkers.json"

PAGE_TITLE = "Selected general biomarker report"

# ---------- display vocab ----------

STATUS_LABELS = {
    "not_measured": "Not measured",
    "measured_not_hardened": "Measured, not decision-grade",
    "not_assessable": "Not assessable yet",
    "indeterminate": "Record ambiguous",
    "measured_hardened": "Measured",
}

RELEVANCE_LABELS = {
    "tumor_agnostic": "Tumor-agnostic",
    "tumor_subset": "Relevant across a tumor subset",
    "tumor_type_specific": "Relevant to this tumor type",
}

RECOMMENDATION_LABELS = {
    "order_now": "Order now",
    "bundle_with_planned_testing": "Bundle with planned testing",
    "reflex_if_positive": "Reflex if positive",
    "order_if_tissue_available": "Order if tissue available",
    "defer": "Defer",
    "no_action": "No action",
}

INDICATION_LABELS = {
    "approved_this_tumor_type": "approved, this tumor type",
    "approved_other_tumor_type": "approved, other tumor type",
    "tumor_agnostic": "tumor-agnostic approval",
    "trial_only": "trial only",
    "preclinical_only": "preclinical only",
}

PRIORITY_ORDER = {"essential": 0, "high": 1, "medium": 2, "low": 3}
STATUS_ORDER = {
    "not_measured": 0,
    "measured_not_hardened": 1,
    "not_assessable": 2,
    "indeterminate": 3,
    "measured_hardened": 4,
}
RELEVANCE_ORDER = {"tumor_agnostic": 0, "tumor_subset": 1, "tumor_type_specific": 2}

PRIORITY_BADGE = {
    "essential": ("essential", "fit-strong"),
    "high": ("high", "fit-partial"),
    "medium": ("medium", "fit-weak"),
    "low": ("low", "fit-none"),
}

# Prose fields the agent authors. These render verbatim into clinician-facing
# cells, so they carry the reporter's em-dash ban (see .claude/agents/reporter.md
# rule 1). The `—` the renderer itself emits for an empty cell is a placeholder,
# not prose, and is unaffected.
PROSE_FIELDS = ("relevance_rationale", "hardening_gap", "rationale", "notes")
EM_DASH = "—"


class BuildError(Exception):
    """A contract violation that must block the build rather than render wrong."""


# ---------- helpers ----------


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
    if low.startswith(("guideline:", "fda:")):
        return f"<em>{html.escape(s.split(':', 1)[1].strip())}</em>"
    return html.escape(s)


def _symbol_list(symbols: list[str], escape: bool = False) -> str:
    """Join bare gene symbols with ' · ' rather than ', '.

    A comma-separated run of ALL-CAPS symbols ("CD19, CD200, CD276, ...") matches
    the PHI scanner's `all_caps_name` pattern, which exists to catch "SURNAME,
    SURNAME". Allowlisting all 72 symbols would blunt a real tripwire and would
    drift every time the panel workbook changes, so the separator changes instead.
    """
    out = [html.escape(str(s)) if escape else str(s) for s in symbols]
    return " · ".join(out)


def references_cell(refs: list[str] | None) -> str:
    if not refs:
        return "—"
    return "<br>".join(_ref_link(r) for r in refs)


def sort_key(r: dict) -> tuple:
    return (
        PRIORITY_ORDER.get(r.get("priority"), 99),
        RELEVANCE_ORDER.get(r.get("relevance_class"), 99),
        STATUS_ORDER.get(r.get("measurement_status"), 99),
        r.get("biomarker_label") or "",
    )


def biomarker_cell(r: dict) -> str:
    label = fmt(r.get("biomarker_label"))
    bits = [f"<strong>{label}</strong>"]
    rel = RELEVANCE_LABELS.get(r.get("relevance_class"))
    if rel:
        bits.append(f'<small class="persona-line">{html.escape(rel)}</small>')
    return "<td>" + "<br>".join(bits) + "</td>"


def assay_cell(r: dict) -> str:
    assay = r.get("recommended_assay") or {}
    if not assay.get("test_name"):
        return "<td>—</td>"
    bits = [f"<strong>{html.escape(str(assay['test_name']))}</strong>"]
    meta = [
        assay.get("assay_modality"),
        assay.get("tissue_required"),
        assay.get("turnaround_estimate"),
    ]
    meta_line = " · ".join(html.escape(str(m)) for m in meta if m)
    if meta_line:
        bits.append(f"<small>{meta_line}</small>")
    if assay.get("bundled_with"):
        bits.append(
            f'<small class="persona-line"><em>bundles with:</em> '
            f"{html.escape(str(assay['bundled_with']))}</small>"
        )
    return "<td>" + "<br>".join(bits) + "</td>"


def implication_cell(r: dict) -> str:
    imps = r.get("therapeutic_implication") or []
    if not imps:
        return "<td>—</td>"
    pieces = []
    for i in imps:
        name = html.escape(str(i.get("intervention") or ""))
        if not name:
            continue
        line = f"<strong>{name}</strong>"
        tail = []
        if i.get("modality"):
            tail.append(html.escape(str(i["modality"])))
        match = INDICATION_LABELS.get(i.get("indication_match"))
        if match:
            tail.append(html.escape(match))
        if tail:
            line += f' <small class="persona-line">({" · ".join(tail)})</small>'
        if i.get("nct_id"):
            nid = html.escape(str(i["nct_id"]))
            line += f'<br><small><a href="https://clinicaltrials.gov/study/{nid}">{nid}</a></small>'
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


# ---------- the three tables ----------


def render_gap_table(rows: list[dict]) -> str:
    """Not-measured / not-assessable rows: the core deliverable of this report."""
    if not rows:
        return "_Every in-scope biomarker on the panel has a result on file._\n"
    head = (
        "<th>Priority</th><th>Biomarker</th><th>Status</th>"
        "<th>Why it is in scope</th><th>Recommended assay</th>"
        "<th>What a positive result would open</th><th>Next step</th>"
        "<th>Rationale</th><th>References</th>"
    )
    body = []
    for r in rows:
        body.append(
            "    <tr>"
            f"<td>{priority_badge(r.get('priority'))}</td>"
            f"{biomarker_cell(r)}"
            f"<td>{html.escape(STATUS_LABELS.get(r.get('measurement_status'), r.get('measurement_status') or '—'))}</td>"
            f"<td>{fmt(r.get('relevance_rationale'))}</td>"
            f"{assay_cell(r)}"
            f"{implication_cell(r)}"
            f"<td>{html.escape(RECOMMENDATION_LABELS.get(r.get('screening_recommendation'), r.get('screening_recommendation') or '—'))}</td>"
            f"<td>{fmt(r.get('rationale'))}</td>"
            f"<td>{references_cell(r.get('references'))}</td>"
            "</tr>"
        )
    return _table(head, body)


def render_not_hardened_table(rows: list[dict]) -> str:
    if not rows:
        return ""
    head = (
        "<th>Priority</th><th>Biomarker</th><th>What is on file</th>"
        "<th>Gap</th><th>What would close it</th><th>Next step</th><th>References</th>"
    )
    body = []
    for r in rows:
        body.append(
            "    <tr>"
            f"<td>{priority_badge(r.get('priority'))}</td>"
            f"{biomarker_cell(r)}"
            f"<td>{fmt(r.get('status_evidence'))}</td>"
            f"<td>{fmt(r.get('hardening_gap'))}</td>"
            f"{assay_cell(r)}"
            f"<td>{html.escape(RECOMMENDATION_LABELS.get(r.get('screening_recommendation'), r.get('screening_recommendation') or '—'))}</td>"
            f"<td>{references_cell(r.get('references'))}</td>"
            "</tr>"
        )
    return _table(head, body)


def render_measured_table(rows: list[dict]) -> str:
    if not rows:
        return ""
    head = "<th>Biomarker</th><th>Status</th><th>Where it is recorded</th><th>Note</th>"
    body = []
    for r in rows:
        body.append(
            "    <tr>"
            f"{biomarker_cell(r)}"
            f"<td>{html.escape(STATUS_LABELS.get(r.get('measurement_status'), r.get('measurement_status') or '—'))}</td>"
            f"<td>{fmt(r.get('status_evidence'))}</td>"
            f"<td>{fmt(r.get('rationale'))}</td>"
            "</tr>"
        )
    return _table(head, body)


def _indent_block(block: str, spaces: int = 4) -> str:
    """Indent a rendered block so it nests inside a mkdocs `??? note` admonition.

    Blank lines stay blank; indenting them would end the admonition early and
    dump the rest of the table into the page body.
    """
    pad = " " * spaces
    lines = [(pad + ln if ln.strip() else ln) for ln in block.splitlines()]
    return "\n".join(lines) + "\n"


def render_set_aside_table(rows: list[dict]) -> str:
    """The panel entries assessed and found not relevant to this tumour.

    Deliberately narrow: biomarker and the one-line reason. These rows exist so a
    reader can tell "assessed and set aside, here is why" from "nobody looked",
    which the old bare list of gene symbols could not do. Anything wider would
    make the section worth reading, which is the opposite of the intent — the
    actionable tables are above it.
    """
    if not rows:
        return ""
    head = "<th>Biomarker</th><th>Why it was set aside</th>"
    body = []
    for r in rows:
        body.append(
            "    <tr>"
            f"{biomarker_cell(r)}"
            f"<td>{fmt(r.get('relevance_rationale'))}</td>"
            "</tr>"
        )
    return _table(head, body)


def render_bundles(rows: list[dict]) -> str:
    """Collapse the recommended assays onto the orders that would carry them.

    A gap list is only actionable if the reader can see that fifteen rows
    resolve to three orders.
    """
    bundles: dict[str, list[str]] = {}
    for r in rows:
        assay = r.get("recommended_assay") or {}
        key = assay.get("bundled_with") or assay.get("test_name")
        if not key:
            continue
        bundles.setdefault(str(key), []).append(str(r.get("biomarker_label") or r.get("panel_key")))
    if not bundles:
        return ""
    ordered = sorted(bundles.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    lines = [
        "## What this collapses to\n",
        "_The gaps above resolve onto this many distinct orders. Biomarkers that ride "
        "along on the same assay are grouped together._\n",
    ]
    for name, markers in ordered:
        lines.append(f"- **{html.escape(name)}** — {html.escape(', '.join(sorted(set(markers))))}")
    lines.append("")
    return "\n".join(lines)


# ---------- coverage ----------


def compute_coverage(rows: list[dict]) -> dict:
    """Panel coverage, derived rather than stored.

    Two shapes are supported, distinguished by whether the survey carries any
    `screened_not_relevant` row:

    * **Full survey** (current contract). The surveyor emits a row for every
      panel entry, classifying the irrelevant ones `screened_not_relevant`
      rather than omitting them, so a reader can tell "assessed and set aside,
      here is why" from "nobody looked". Those rows render as their own table.
    * **Legacy shortlist.** Surveys written before that change omit the
      irrelevant targets entirely, and the out-of-scope list is the panel minus
      the emitted rows — a bare list of gene symbols with no per-target reason.
      Kept so already-published cases still render as they were built.

    `set_aside_rows` is the full-survey list and is empty for a legacy survey;
    `out_of_scope` is the legacy list and is empty for a full survey. A reader
    should never see both.
    """
    panel = load_json(PANEL_PATH)
    agnostic = load_json(AGNOSTIC_PATH)
    targets = panel.get("targets") or []
    agnostic_entries = agnostic.get("biomarkers") or []

    surveyed = {r.get("panel_key") for r in rows}
    target_keys = {t["panel_key"]: t["gene_symbol"] for t in targets if t.get("panel_key")}
    agnostic_keys = {b["panel_key"]: b["biomarker_label"] for b in agnostic_entries if b.get("panel_key")}

    missing_agnostic = [label for key, label in agnostic_keys.items() if key not in surveyed]

    set_aside_rows = [r for r in rows if r.get("relevance_class") == "screened_not_relevant"]
    if set_aside_rows:
        # Full survey: nothing is omitted, so there is no subtraction to do.
        out_of_scope: list[str] = []
    else:
        out_of_scope = sorted(gene for key, gene in target_keys.items() if key not in surveyed)

    set_aside_keys = {r.get("panel_key") for r in set_aside_rows}
    return {
        "panel_targets": len(target_keys),
        "panel_agnostic": len(agnostic_keys),
        "targets_in_scope": len(target_keys) - len(out_of_scope) - len(set_aside_keys),
        "out_of_scope": out_of_scope,
        "set_aside_rows": set_aside_rows,
        "missing_agnostic": missing_agnostic,
        "panel_run": (panel.get("source") or {}).get("run_timestamp_iso"),
    }


def preflight(rows: list[dict], coverage: dict, narrative: str = "") -> None:
    """Block the build on a contract violation rather than publishing a wrong page."""
    problems: list[str] = []

    if EM_DASH in narrative:
        problems.append(
            "biomarker_survey_report.md: em-dash (U+2014) in the reporter narrative; "
            "use a period, comma, or colon"
        )

    if coverage["missing_agnostic"]:
        problems.append(
            "every tumor-agnostic panel entry must be surveyed in every case; missing: "
            + ", ".join(coverage["missing_agnostic"])
        )

    for r in rows:
        rid = r.get("survey_id") or r.get("panel_key") or "<row>"
        for field in PROSE_FIELDS:
            value = r.get(field)
            if isinstance(value, str) and EM_DASH in value:
                problems.append(
                    f"{rid}: em-dash (U+2014) in `{field}`; use a period, comma, colon, "
                    "or an en-dash inside a numeric range"
                )
        if r.get("measurement_status") == "measured_not_hardened":
            if not r.get("hardening_gap"):
                problems.append(f"{rid}: measured_not_hardened requires a `hardening_gap`")
            if not r.get("handoff_to_target_validator"):
                problems.append(
                    f"{rid}: measured_not_hardened requires `handoff_to_target_validator: true` "
                    "so /target_validator picks the gap up"
                )

    if problems:
        raise BuildError(
            "build_biomarker_survey: refusing to render.\n  - " + "\n  - ".join(problems)
        )


# ---------- page ----------


def _tv_ref(case_docs: Path | None) -> str:
    """Reference to the Target validation paths page, linked only when it exists.

    The survey can run before /target_validator has rendered its page, and a link
    to a missing page breaks `mkdocs build --strict`.
    """
    if case_docs is not None and (case_docs / "target_validation.md").exists():
        return "[Target validation paths](target_validation.md)"
    return "Target validation paths"


def _legend(case_docs: Path | None) -> str:
    return (
        '!!! note "Reading this report"\n'
        "    This page answers one question per biomarker: has this patient been tested "
        "for it, and was the test at a resolution that can carry a treatment decision. "
        "**Not measured** means nothing is on file, which is not the same as a negative "
        "result. **Measured, not decision-grade** means a result exists but cannot be "
        "acted on as it stands; those gaps are worked into the "
        f"{_tv_ref(case_docs)} report. **Priority** weighs what "
        "is going unassessed against how routine the assay is. Most of these biomarkers "
        "will be negative if tested; the case for testing rests on the size of the option "
        "that opens if positive, not on how likely a positive is.\n"
    )


def _downloads_block(slug: str) -> str:
    items = [
        (f"{slug}-biomarker-survey.html", f"{PAGE_TITLE} (offline HTML)",
         "the same survey, self-contained HTML that opens offline"),
        (f"{slug}-biomarker-survey.pdf", f"{PAGE_TITLE} (PDF)",
         "print-friendly, grouped by recommended action"),
    ]
    lines = ["## Downloads\n"]
    for name, label, blurb in items:
        lines.append(f"- [{label}]({html.escape(name)}) — {blurb}")
    lines.append("")
    return "\n".join(lines)


def load_narrative(case_dir: Path) -> str:
    """The biomarker_reporter's opening narrative, inlined verbatim when present.

    Same contract as the reporter's target_validation_report.md: the prose is the
    agent's, the tables are the renderer's, and neither rewrites the other.
    """
    path = case_dir / "biomarker_survey_report.md"
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()


def _nav_line(case_docs: Path) -> str:
    """Sibling-page links, filtered to pages that exist.

    Linking a page a case never rendered would break `mkdocs build --strict`, and
    the survey can legitimately run before the rest of the pipeline has produced
    its pages.
    """
    candidates = [
        ("index.md", "Back to case"),
        ("target_validation.md", "Target validation"),
        ("recommendations.md", "Recommendations"),
        ("trials.md", "Trials"),
        ("evidence.md", "Evidence"),
        ("board.md", "Board"),
    ]
    links = [f"[{label}]({name})" for name, label in candidates if (case_docs / name).exists()]
    return " · ".join(links) + "\n" if links else ""


def render_page(slug: str, rows: list[dict], coverage: dict, narrative: str = "",
                case_docs: Path | None = None) -> str:
    gaps = [r for r in rows if r.get("measurement_status") in ("not_measured", "not_assessable", "indeterminate")]
    not_hardened = [r for r in rows if r.get("measurement_status") == "measured_not_hardened"]
    measured = [r for r in rows if r.get("measurement_status") == "measured_hardened"]
    n_essential = sum(1 for r in gaps if r.get("priority") == "essential")

    parts = [
        '<meta name="robots" content="noindex">\n',
        f"# {PAGE_TITLE} — `{slug}`\n",
        "_Which biomarkers on the selected panel this patient has been tested for, and "
        "which have never been measured. The panel covers targets established in this "
        "tumor type, targets relevant across a subset of tumor types, and biomarkers "
        "that predict benefit regardless of where the tumor started, such as MSI-H/dMMR "
        "and high tumor mutational burden gating PD-1 blockade._\n",
        _downloads_block(slug),
        f"_{len(rows)} biomarkers surveyed: {len(gaps)} with no usable result on file "
        f"({n_essential} essential), {len(not_hardened)} measured but not to decision "
        f"resolution, {len(measured)} already established. Panel coverage: "
        f"{coverage['panel_agnostic']} tumor-agnostic biomarkers plus "
        f"{coverage['targets_in_scope']} of {coverage['panel_targets']} protein targets "
        "in scope for this tumor._\n",
    ]

    if narrative:
        parts.append(narrative + "\n")

    parts.extend([
        "## Gaps: biomarkers with no usable result on file\n",
        render_gap_table(sorted(gaps, key=sort_key)),
    ])

    bundles = render_bundles(gaps)
    if bundles:
        parts.append(bundles)

    if not_hardened:
        parts.append("## Measured, but not to decision resolution\n")
        parts.append(
            "_A result exists for each of these, but not at the resolution a treatment "
            "decision needs. The workup that would close each gap is carried into the "
            f"{_tv_ref(case_docs)} report._\n"
        )
        parts.append(render_not_hardened_table(sorted(not_hardened, key=sort_key)))

    if measured:
        parts.append("## Already established\n")
        parts.append("_On file at decision resolution. No further action from this survey._\n")
        parts.append(render_measured_table(sorted(measured, key=sort_key)))

    if coverage["set_aside_rows"]:
        parts.append("## Panel entries assessed and set aside\n")
        parts.append(
            f'??? note "{len(coverage["set_aside_rows"])} of '
            f'{coverage["panel_targets"]} panel targets were assessed and set aside"\n'
            "    Every biomarker on the reference panel is assessed for every case, so "
            "this section records what was considered and why it was set aside rather "
            "than leaving it absent. Collapsed because none of it carries an action.\n"
        )
        parts.append(
            _indent_block(render_set_aside_table(coverage["set_aside_rows"]))
        )
    elif coverage["out_of_scope"]:
        # Legacy shortlist survey: no per-target reason exists to render.
        parts.append("## Panel targets out of scope for this tumor\n")
        parts.append(
            f'??? note "{len(coverage["out_of_scope"])} of '
            f'{coverage["panel_targets"]} panel targets were screened and set aside"\n'
            "    Set aside as having no plausible connection to this patient's tumor "
            "type or stated features. Listed for completeness of the audit trail.\n\n"
            "    " + _symbol_list(coverage["out_of_scope"], escape=True) + "\n"
        )

    parts.append(_legend(case_docs))
    if case_docs is not None:
        nav = _nav_line(case_docs)
        if nav:
            parts.append(nav)
    parts.append(
        '!!! danger disclaimer "Decision support, not medical advice"\n'
        "    Libby is experimental. An unmeasured biomarker on this page is a gap in the\n"
        "    record, not a prediction that the patient carries it. Assay availability,\n"
        "    current approval status, and whether any of this testing is worth the tissue\n"
        "    are decisions for the treating team. See [PHI policy](../../phi_policy.md).\n"
    )
    return "\n".join(parts) + "\n"


# ---------- print PDF ----------


def _deep_markdown(slug: str, rows: list[dict], coverage: dict, narrative: str = "") -> str:
    gaps = [r for r in rows if r.get("measurement_status") in ("not_measured", "not_assessable", "indeterminate")]
    not_hardened = [r for r in rows if r.get("measurement_status") == "measured_not_hardened"]
    measured = [r for r in rows if r.get("measurement_status") == "measured_hardened"]

    lines: list[str] = [f"# {PAGE_TITLE}\n"]
    lines.append(
        "Which biomarkers on the selected panel this patient has been tested for, and "
        "which have never been measured. The panel covers targets established in this "
        "tumor type, targets relevant across a subset of tumor types, and biomarkers "
        "that predict benefit regardless of where the tumor started. An unmeasured "
        "biomarker below is a gap in the record, not a prediction that the patient "
        "carries it.\n"
    )
    lines.append(
        f"**Surveyed:** {len(rows)} biomarkers. **No usable result on file:** {len(gaps)}. "
        f"**Measured but not decision-grade:** {len(not_hardened)}. "
        f"**Already established:** {len(measured)}.\n"
    )

    if narrative:
        lines.append(narrative + "\n")

    if gaps:
        lines.append("## Gaps: biomarkers with no usable result on file\n")
        for r in sorted(gaps, key=sort_key):
            lines.append(f"### {r.get('biomarker_label') or r.get('panel_key')}\n")
            meta = [
                f"**Priority:** {r.get('priority') or '-'}",
                f"**Scope:** {RELEVANCE_LABELS.get(r.get('relevance_class'), r.get('relevance_class') or '-')}",
                f"**Status:** {STATUS_LABELS.get(r.get('measurement_status'), r.get('measurement_status') or '-')}",
            ]
            lines.append("  ".join(meta) + "\n")
            if r.get("relevance_rationale"):
                lines.append(r["relevance_rationale"] + "\n")
            if r.get("rationale"):
                lines.append(r["rationale"] + "\n")
            assay = r.get("recommended_assay") or {}
            if assay.get("test_name"):
                extra = " · ".join(
                    str(x) for x in (assay.get("assay_modality"), assay.get("tissue_required"),
                                     assay.get("turnaround_estimate")) if x
                )
                lines.append(f"**Recommended assay.** {assay['test_name']}" + (f" ({extra})" if extra else "") + "\n")
                if assay.get("bundled_with"):
                    lines.append(f"**Bundles with.** {assay['bundled_with']}\n")
            imps = r.get("therapeutic_implication") or []
            if imps:
                lines.append("**A positive result would open.**\n")
                for i in imps:
                    tail = " · ".join(
                        str(x) for x in (i.get("modality"),
                                         INDICATION_LABELS.get(i.get("indication_match")),
                                         i.get("nct_id")) if x
                    )
                    lines.append(f"- {i.get('intervention')}" + (f" ({tail})" if tail else ""))
                lines.append("")
            lines.append(
                f"**Next step.** {RECOMMENDATION_LABELS.get(r.get('screening_recommendation'), r.get('screening_recommendation') or '-')}\n"
            )
            if r.get("references"):
                lines.append("**References.** " + "; ".join(str(x) for x in r["references"]) + "\n")

    if not_hardened:
        lines.append("## Measured, but not to decision resolution\n")
        lines.append(
            "A result exists for each of these, but not at the resolution a treatment "
            "decision needs. The workup that would close each gap is carried into the "
            "Target validation paths report.\n"
        )
        for r in sorted(not_hardened, key=sort_key):
            lines.append(f"### {r.get('biomarker_label') or r.get('panel_key')}\n")
            lines.append(f"**Priority:** {r.get('priority') or '-'}\n")
            if r.get("status_evidence"):
                lines.append("**On file.** " + "; ".join(str(x) for x in r["status_evidence"]) + "\n")
            if r.get("hardening_gap"):
                lines.append(f"**Gap.** {r['hardening_gap']}\n")
            if r.get("rationale"):
                lines.append(r["rationale"] + "\n")

    if measured:
        lines.append("## Already established\n")
        for r in sorted(measured, key=sort_key):
            evidence = "; ".join(str(x) for x in (r.get("status_evidence") or [])) or "on file"
            lines.append(f"- **{r.get('biomarker_label') or r.get('panel_key')}** — {evidence}")
        lines.append("")

    if coverage["out_of_scope"]:
        lines.append("## Panel targets out of scope for this tumor\n")
        lines.append(
            f"{len(coverage['out_of_scope'])} of {coverage['panel_targets']} panel targets "
            "were screened and set aside as having no plausible connection to this "
            "patient's tumor type or stated features: "
            + _symbol_list(coverage["out_of_scope"])
            + "\n"
        )
    return "\n".join(lines)


def _make_pdf(slug: str, rows: list[dict], coverage: dict, out_path: Path, narrative: str = "") -> None:
    try:
        from fpdf import FPDF
    except ImportError as e:  # pragma: no cover
        raise SystemExit(
            "build_biomarker_survey: missing dependency `fpdf2`.\n  pip install fpdf2"
        ) from e

    today = datetime.now(timezone.utc).date().isoformat()

    class SurveyPDF(FPDF):
        def footer(self_):
            if self_.page_no() <= 1:
                return
            self_.set_y(-12)
            self_.set_font(br._FONT_FAMILY, "I", 8)
            self_.set_text_color(*br.INK_MUTED)
            self_.cell(
                0, 6,
                br._ascii_fallback(
                    f"{self_.page_no()} of {{nb}}    ·    Libby — biomarker survey    ·    {slug}"
                ),
                align="C",
            )

    pdf = SurveyPDF(orientation="P", unit="mm", format="Letter")
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(left=18, top=20, right=18)
    pdf.alias_nb_pages()
    br._register_unicode_font(pdf)
    br._render_cover(
        pdf, slug,
        f"{PAGE_TITLE} — biomarker screening coverage and gaps",
        today, "LIBBY — BIOMARKER SURVEY",
        br.COVER_BG, br._DISCLAIMER_CLINICIAN,
    )
    pdf.add_page()
    br._render_markdown_block(pdf, _deep_markdown(slug, rows, coverage, narrative), top_h1=True)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(out_path))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug")
    args = parser.parse_args()
    slug = args.slug

    case_dir = REPO / "data" / "cases" / slug
    case_docs = REPO / "docs" / "cases" / slug
    rows = load_jsonl(case_dir / "biomarker_survey.jsonl")

    page = case_docs / "biomarker_survey.md"
    html_dst = case_docs / f"{slug}-biomarker-survey.html"
    pdf_dst = case_docs / f"{slug}-biomarker-survey.pdf"

    # No rows → the survey has not run for this case. Don't leave an empty page
    # for the case-output / downloads injectors to surface; strip stale artifacts.
    if not rows:
        for stale in (page, html_dst, pdf_dst):
            if stale.exists():
                stale.unlink()
        print(f"no biomarker_survey.jsonl rows for {slug}; nothing rendered")
        return 0

    coverage = compute_coverage(rows)
    narrative = load_narrative(case_dir)
    try:
        preflight(rows, coverage, narrative)
    except BuildError as e:
        print(str(e), file=sys.stderr)
        return 1

    case_docs.mkdir(parents=True, exist_ok=True)
    page_md = render_page(slug, rows, coverage, narrative, case_docs)
    page.write_text(page_md, encoding="utf-8")
    print(f"wrote {page} ({len(rows)} rows)")

    html_out = br._render_self_contained_html_page(
        slug, f"Libby {PAGE_TITLE.lower()} — {slug}", PAGE_TITLE, page_md,
    )
    html_dst.write_text(html_out, encoding="utf-8")
    print(f"built {html_dst}")

    _make_pdf(slug, rows, coverage, pdf_dst, narrative)
    print(f"built {pdf_dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
