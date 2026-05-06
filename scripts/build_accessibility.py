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
    "clinical_trial_only":      ("Clinical trial only",     "fit-partial"),
    "compassionate_use":        ("Compassionate use",       "fit-weak"),
    "expanded_access_program":  ("Expanded access program", "fit-weak"),
    "not_yet_accessible":       ("Not yet accessible",      "fit-weak"),
    "unavailable":              ("Unavailable",             "fit-none"),
}


def status_badge(s: str | None) -> str:
    label, cls = _STATUS_META.get(s or "", (s or "—", "fit-none"))
    return f'<span class="fit-badge {cls}">{html.escape(label)}</span>'


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
        '<th>NCT</th><th>Phase</th><th>Indication</th>'
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
            f"<td>{nct_link}</td>"
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
    parts.append(
        f"**Access status:** {status_badge(r.get('access_status'))} &nbsp; "
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


_STATUS_ORDER = [
    "standard_of_care",
    "off_label_use",
    "clinical_trial_only",
    "compassionate_use",
    "expanded_access_program",
    "not_yet_accessible",
    "unavailable",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    args = parser.parse_args()
    slug = args.slug

    case_dir = REPO / "data" / "cases" / slug
    rows = load_jsonl(case_dir / "accessibility.jsonl")

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
        # Group by status, ordered by actionability. Within each group, sort by
        # intervention_label so numbers are reproducible run to run.
        by_status: dict[str, list[dict]] = {}
        for r in rows:
            by_status.setdefault(r.get("access_status") or "unavailable", []).append(r)
        for s in by_status:
            by_status[s].sort(key=lambda x: x.get("intervention_label") or "")

        # Build a single ordered list of (number, status, row) so the summary
        # table and the per-intervention deep sections share the same numbering.
        numbered: list[tuple[int, str, dict]] = []
        n = 1
        for status in _STATUS_ORDER:
            for r in by_status.get(status, []):
                numbered.append((n, status, r))
                n += 1

        # Top-of-page summary table — first column is the entry number, which
        # links directly to the per-intervention deep section anchor below.
        parts.append("## Summary\n")
        parts.append(
            "_The number in the first column links to the per-intervention "
            "section further down the page. Use it for quick navigation._\n"
        )
        parts.append('<table class="trial-table"><thead><tr>'
                     '<th>#</th><th>Intervention</th><th>Modality</th>'
                     '<th>Access status</th><th>Regulatory</th>'
                     '<th>Recommended first action</th>'
                     '</tr></thead><tbody>\n')
        for num, status, r in numbered:
            first_step = (r.get("next_steps") or ["—"])[0]
            parts.append(
                "<tr>"
                f'<td><a href="#access-{num}"><strong>{num}</strong></a></td>'
                f"<td><strong>{fmt(r.get('intervention_label'))}</strong></td>"
                f"<td>{fmt(r.get('modality'))}</td>"
                f"<td>{status_badge(status)}</td>"
                f"<td>{fmt(r.get('regulatory_status'))}</td>"
                f"<td>{html.escape(str(first_step))}</td>"
                "</tr>"
            )
        parts.append("</tbody></table>\n")

        # Per-intervention deep sections, grouped by status. Each H3 carries
        # the entry number from the summary table plus a `#access-<n>` anchor.
        by_status_numbered: dict[str, list[tuple[int, dict]]] = {}
        for num, status, r in numbered:
            by_status_numbered.setdefault(status, []).append((num, r))
        for status in _STATUS_ORDER:
            group = by_status_numbered.get(status, [])
            if not group:
                continue
            label, _cls = _STATUS_META.get(status, (status, "fit-none"))
            parts.append(f"\n## {label} ({len(group)})\n")
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
