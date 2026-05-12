#!/usr/bin/env python3
"""Render accessibility.jsonl → docs/cases/<slug>/accessibility.md.

One-page-per-case access guide. For each surfaced intervention: access
status (standard-of-care / off-label / clinical-trial / compassionate /
unavailable), trial recruitment contacts, manufacturer medical-info, and
ordered next-step actions the user / treating team would actually take.
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


def fmt(v, dash: str = "—") -> str:
    if v is None or v == "":
        return dash
    return html.escape(str(v))


_STATUS_META: dict[str, tuple[str, str]] = {
    "standard_of_care":         ("Standard of care",        "fit-strong"),
    "off_label_use":            ("Off-label use",           "fit-partial"),
    "clinical_trial_only":      ("Clinical trial",          "fit-partial"),
    "compassionate_use":        ("Compassionate use",       "fit-weak"),
    "expanded_access_program":  ("Expanded access program", "fit-weak"),
    "not_yet_accessible":       ("Not yet accessible",      "fit-weak"),
    "unavailable":              ("Unavailable",             "fit-none"),
}

_STATUS_ORDER = [
    "standard_of_care",
    "off_label_use",
    "clinical_trial_only",
    "compassionate_use",
    "expanded_access_program",
    "not_yet_accessible",
    "unavailable",
]


def normalize_status(raw) -> list[str]:
    """Accept either a list (current schema) or a bare string (legacy rows)."""
    if isinstance(raw, list):
        return [s for s in raw if s]
    if isinstance(raw, str) and raw:
        return [raw]
    return []


def primary_status(statuses: list[str]) -> str:
    """Return the most actionable status from a list, used for grouping."""
    for s in _STATUS_ORDER:
        if s in statuses:
            return s
    return "unavailable"


def status_badge(s: str | None) -> str:
    label, cls = _STATUS_META.get(s or "", (s or "—", "fit-none"))
    return f'<span class="fit-badge {cls}">{html.escape(label)}</span>'


def status_badges(statuses: list[str]) -> str:
    """Render every status in the list as a separate badge."""
    if not statuses:
        return status_badge(None)
    # Order by actionability, not by author order, so the strongest path leads.
    ordered = [s for s in _STATUS_ORDER if s in statuses]
    return " ".join(status_badge(s) for s in ordered)


def eligibility_badge(e: str | None) -> str:
    if not e:
        return ""
    cls = {
        "yes": "fit-strong",
        "likely": "fit-partial",
        "unconfirmed": "fit-weak",
        "no": "fit-none",
    }.get(e, "fit-none")
    return f'<span class="fit-badge {cls}">eligible: {html.escape(e)}</span>'


def link_or_text(url: str | None, label: str | None = None) -> str:
    if not url:
        return ""
    return f'<a href="{html.escape(url)}">{html.escape(label or url)}</a>'


def link_email(email: str | None) -> str:
    if not email:
        return ""
    return f'<a href="mailto:{html.escape(email)}">{html.escape(email)}</a>'


def render_trials_block(trials: list[dict]) -> str:
    if not trials:
        return "_No registered trials in the dossier._\n"
    rows: list[str] = [
        '<table class="trial-table">',
        '<thead><tr>'
        '<th class="col-nct">NCT</th><th>Phase</th><th>Indication</th>'
        '<th>Status</th><th>Patient eligible</th>'
        '<th>Central contact</th><th>Notes</th>'
        '</tr></thead>',
        '<tbody>',
    ]
    for t in trials:
        nct = t.get("nct_id") or ""
        nct_link = (
            f'<a href="https://clinicaltrials.gov/study/{html.escape(nct)}">{html.escape(nct)}</a>'
            if nct else "—"
        )
        contact_bits: list[str] = []
        if t.get("central_contact_name"):
            contact_bits.append(f"<strong>{fmt(t['central_contact_name'])}</strong>")
        if t.get("central_contact_email"):
            contact_bits.append(link_email(t.get("central_contact_email")))
        if t.get("central_contact_phone"):
            contact_bits.append(f"<code>{fmt(t['central_contact_phone'])}</code>")
        if t.get("sites_url"):
            contact_bits.append(link_or_text(t.get("sites_url"), "trial sites"))
        contact = "<br>".join(contact_bits) if contact_bits else "—"
        rows.append(
            "<tr>"
            f'<td class="col-nct">{nct_link}</td>'
            f"<td>{fmt(t.get('phase'))}</td>"
            f"<td>{fmt(t.get('indication'))}</td>"
            f"<td>{fmt(t.get('recruitment_status'))}</td>"
            f"<td>{eligibility_badge(t.get('patient_eligible'))}</td>"
            f"<td>{contact}</td>"
            f"<td>{fmt(t.get('notes'))}</td>"
            "</tr>"
        )
    rows.append("</tbody></table>")
    return '<div class="trial-table-wrap"><div class="trial-scroll">' + "\n".join(rows) + "</div></div>\n"


def render_manufacturer_block(m: dict) -> str:
    if not m:
        return "_No manufacturer information captured._\n"
    pairs: list[tuple[str, str]] = []
    if m.get("company"):
        pairs.append(("Company", fmt(m.get("company"))))
    if m.get("country_of_origin"):
        pairs.append(("Country", fmt(m.get("country_of_origin"))))
    if m.get("medical_information_phone"):
        pairs.append(("Medical info phone", f"<code>{fmt(m['medical_information_phone'])}</code>"))
    if m.get("medical_information_email"):
        pairs.append(("Medical info email", link_email(m["medical_information_email"])))
    if m.get("product_information_url"):
        pairs.append(("Product information", link_or_text(m["product_information_url"])))
    if m.get("compassionate_use_url"):
        pairs.append(("Compassionate / expanded access", link_or_text(m["compassionate_use_url"])))
    if m.get("compassionate_use_email"):
        pairs.append(("Compassionate use email", link_email(m["compassionate_use_email"])))
    if m.get("notes"):
        pairs.append(("Notes", fmt(m["notes"])))
    if not pairs:
        return "_No manufacturer information captured._\n"
    items = "\n".join(f"  <dt>{html.escape(k)}</dt><dd>{v}</dd>" for k, v in pairs)
    return f'<dl class="profile-grid">\n{items}\n</dl>\n'


def render_intervention_section(r: dict, number: int) -> str:
    label = r.get("intervention_label") or r.get("intervention_id") or "?"
    aliases = r.get("aliases") or []
    alias_str = (
        f' <small><code>{html.escape(", ".join(aliases))}</code></small>'
        if aliases
        else ""
    )
    anchor = f'access-{number}'
    parts: list[str] = []
    parts.append(
        f'### {number}. {html.escape(str(label))}{alias_str} '
        f'{{ #{anchor} }}\n'
    )
    statuses = r.get("_statuses") or normalize_status(r.get("access_status"))
    parts.append(
        f"**Access status:** {status_badges(statuses)} &nbsp; "
        f"**Modality:** {fmt(r.get('modality'))} &nbsp; "
        f"**Verified:** {fmt(r.get('last_verified_utc'))}\n"
    )

    summary = r.get("access_summary")
    if summary:
        parts.append(f"\n{html.escape(str(summary))}\n")

    reg = r.get("regulatory_status")
    guide = r.get("guideline_status")
    geo = r.get("geographic_scope")
    pairs: list[tuple[str, str]] = []
    if reg:
        pairs.append(("Regulatory", fmt(reg)))
    if guide:
        pairs.append(("Guidelines", fmt(guide)))
    if geo:
        pairs.append(("Geographic scope", fmt(geo)))
    if pairs:
        items = "\n".join(f"  <dt>{html.escape(k)}</dt><dd>{v}</dd>" for k, v in pairs)
        parts.append(f'\n<dl class="profile-grid">\n{items}\n</dl>\n')

    next_steps = r.get("next_steps") or []
    if next_steps:
        parts.append("\n**Next steps**\n")
        for i, step in enumerate(next_steps, 1):
            parts.append(f"{i}. {html.escape(str(step))}")
        parts.append("")

    parts.append("\n**Trial pathways**\n")
    parts.append(render_trials_block(r.get("trials") or []))

    parts.append("\n**Manufacturer / sponsor contact**\n")
    parts.append(render_manufacturer_block(r.get("manufacturer") or {}))

    payer = r.get("payer_access_notes")
    if payer:
        parts.append(f"\n**Payer / coverage notes.** {html.escape(str(payer))}\n")

    notes = r.get("notes")
    if notes:
        parts.append(f"\n**Notes.** {html.escape(str(notes))}\n")

    parts.append("\n---\n")
    return "\n".join(parts)


_FEATURE_LABELS: dict[str, str] = {
    # Mirror of `_FEATURE_LABELS` in `scripts/build_report.py`. Keep in sync.
    "dll3_ihc": "DLL3-targeting interventions",
    "prame_ihc_hla": "PRAME-targeting interventions",
    "kras_g12r": "KRAS G12R-targeting interventions",
    "cdkn2a_loss": "CDKN2A-loss / MTAP-targeting interventions",
    "germline_brca": "Germline BRCA / HRD-targeting interventions",
    "tp53_inactivating": "TP53-targeting interventions",
    "ccnd3_alteration": "CCND3 / CDK4-6-targeting interventions",
    "egfr_l858r": "EGFR L858R-targeting interventions",
    "met_amplification": "MET amplification-targeting interventions",
}


def _feature_label(key: str) -> str:
    if key in _FEATURE_LABELS:
        return _FEATURE_LABELS[key]
    if key == "__unscoped":
        return "Biomarker-independent interventions"
    pretty = key.replace("_", " ").title()
    return f"{pretty} interventions"


def _is_workup_rec(r: dict) -> bool:
    """Match the rule in `build_report.py::_is_workup_row`."""
    if r.get("scenario") == "shared":
        return True
    cpm = r.get("counter_productive_moa") or {}
    return cpm.get("severity") == "N/A"


def _build_canonical_order(recs: list[dict]) -> dict[str, tuple[int, int]]:
    """Compute the Recommendations-table order for each intervention.

    Returns `intervention_id → (group_index, rank_in_group)`. Group index is
    the position of the intervention's target group in the rendered
    Recommendations table (DLL3-targeting first if present, then PRAME,
    then KRAS G12R, etc. — driven by first-appearance order in the recs).
    Rank-in-group is the row's rank within its group. Workup rows are
    excluded.

    Used by the access guide to mirror the Recommendations table's
    grouping + ordering: KRAS-targeting access rows appear before
    germline-BRCA access rows, daraxonrasib appears before PF-07934040,
    etc.
    """
    seen: list[str] = []
    grouped: dict[str, list[dict]] = {}
    for r in recs:
        if _is_workup_rec(r):
            continue
        scen = r.get("scenario")
        if isinstance(scen, str) and ":" in scen:
            key = scen.split(":", 1)[0]
        else:
            tgts = r.get("targets") or []
            key = tgts[0] if tgts and isinstance(tgts[0], str) else "__unscoped"
        if key not in grouped:
            grouped[key] = []
            seen.append(key)
        grouped[key].append(r)
    out: dict[str, tuple[int, int]] = {}
    for g_idx, key in enumerate(seen):
        # Sort within group by global rank ascending.
        rows = sorted(grouped[key], key=lambda r: r.get("rank") or 999)
        for r_idx, r in enumerate(rows):
            iid = r.get("intervention_id")
            if iid:
                out[iid] = (g_idx, r_idx)
    return out


def _rec_target_for_access_row(
    row: dict, recs: list[dict]
) -> str | None:
    """Return the rec row's primary target key for an access row, when matched."""
    iid = row.get("intervention_id")
    for r in recs:
        if r.get("intervention_id") == iid:
            scen = r.get("scenario")
            if isinstance(scen, str) and ":" in scen:
                return scen.split(":", 1)[0]
            tgts = r.get("targets") or []
            return tgts[0] if tgts and isinstance(tgts[0], str) else None
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    args = parser.parse_args()
    slug = args.slug

    case_dir = REPO / "data" / "cases" / slug
    rows = load_jsonl(case_dir / "accessibility.jsonl")
    recs = load_jsonl(case_dir / "recommendations.jsonl")
    canonical = _build_canonical_order(recs)

    parts: list[str] = [
        '<meta name="robots" content="noindex">\n',
        f"# Access guide — `{slug}`\n",
        "How a patient or treating team could practically access each "
        "intervention in this case's dossier. One section per unique drug; "
        "trial recruitment contacts and manufacturer medical-information "
        "lines are captured for direct outreach. **Information ages — each "
        "row carries a `Verified` date; re-screen before relying on a "
        "specific contact or trial slot.**\n",
    ]

    if not rows:
        parts.append(
            "_No accessibility rows yet. Run `/accessibility_screener "
            + slug
            + "` to populate this page._\n"
        )
    else:
        # Normalize statuses to lists for badge rendering; the grouping itself
        # follows the Recommendations table (target group → rank within group)
        # rather than the access status, so the access guide reads in the same
        # sequence as the upstream ranking.
        for r in rows:
            r["_statuses"] = normalize_status(r.get("access_status"))
            r["_primary"] = primary_status(r["_statuses"])

        # Build the canonical order from `recommendations.jsonl` and group
        # each access row by its rec's target. Rows whose `intervention_id`
        # has no matching rec land in a sentinel "__orphan" group at the
        # very end — these should be rare (an upstream contract violation
        # where the accessibility_screener surfaced a drug the PI did not
        # rank).
        target_for_row: dict[int, str] = {}
        for i, r in enumerate(rows):
            tgt = _rec_target_for_access_row(r, recs)
            target_for_row[i] = tgt or "__orphan"

        # Order each row by (group_index, rank_in_group, intervention_label).
        # Orphans get a high group_index so they sort to the end.
        def _sort_key(idx: int) -> tuple[int, int, str]:
            r = rows[idx]
            iid = r.get("intervention_id") or ""
            pos = canonical.get(iid)
            if pos is None:
                return (10_000, 0, r.get("intervention_label") or iid)
            return (pos[0], pos[1], r.get("intervention_label") or iid)

        ordered_indices = sorted(range(len(rows)), key=_sort_key)
        numbered: list[tuple[int, str, dict]] = []
        for n, idx in enumerate(ordered_indices, start=1):
            r = rows[idx]
            numbered.append((n, target_for_row[idx], r))

        # Top-of-page summary table — first column is the entry number, which
        # links directly to the per-intervention deep section anchor below.
        parts.append("## Summary\n")
        parts.append(
            "_Entries are ordered to match the Recommendations table: "
            "by therapeutic target group, then by rank within each group. "
            "The number in the first column links to the per-intervention "
            "section further down the page._\n"
        )
        parts.append('<table class="trial-table"><thead><tr>'
                     '<th class="col-num">#</th><th>Intervention</th><th>Target</th>'
                     '<th>Access status</th><th>Regulatory</th>'
                     '<th>Recommended first action</th>'
                     '</tr></thead><tbody>\n')
        for num, target_key, r in numbered:
            first_step = (r.get("next_steps") or ["—"])[0]
            target_html = (
                html.escape(_feature_label(target_key).replace(" interventions", ""))
                if target_key != "__orphan"
                else "—"
            )
            parts.append(
                "<tr>"
                f'<td class="col-num"><a href="#access-{num}"><strong>{num}</strong></a></td>'
                f"<td><strong>{fmt(r.get('intervention_label'))}</strong></td>"
                f"<td>{target_html}</td>"
                f'<td>{status_badges(r["_statuses"])}</td>'
                f"<td>{fmt(r.get('regulatory_status'))}</td>"
                f"<td>{html.escape(str(first_step))}</td>"
                "</tr>"
            )
        parts.append("</tbody></table>\n")

        # Per-intervention deep sections, grouped by target. Each H3 carries
        # the entry number from the summary table plus a `#access-<n>` anchor,
        # preserving the same ordering as the summary table above.
        target_order: list[str] = []
        by_target: dict[str, list[tuple[int, dict]]] = {}
        for num, target_key, r in numbered:
            if target_key not in by_target:
                by_target[target_key] = []
                target_order.append(target_key)
            by_target[target_key].append((num, r))
        for target_key in target_order:
            group = by_target[target_key]
            heading = (
                _feature_label(target_key)
                if target_key != "__orphan"
                else "Unmatched interventions"
            )
            parts.append(f"\n## {html.escape(heading)} ({len(group)})\n")
            for num, r in group:
                parts.append(render_intervention_section(r, num))

    parts.append(
        f"\n[Back to case](index.md) · [Trials](trials.md) · "
        f"[Evidence](evidence.md) · [Manuscripts](manuscripts.md) · "
        f"[Board](board.md) · [Recommendations](recommendations.md)\n"
    )
    parts.append(
        '!!! danger disclaimer "Decision support, not medical advice"\n'
        "    Contacts and trial-slot information age quickly. Confirm directly with the trial site and manufacturer before relying on details on this page. See [PHI policy](../../phi_policy.md).\n"
    )

    body_md = "\n".join(parts) + "\n"
    dst = REPO / "docs" / "cases" / slug / "accessibility.md"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(body_md, encoding="utf-8")
    print(f"wrote {dst} ({len(rows)} interventions)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
