#!/usr/bin/env python3
"""Render board/positions.jsonl + critiques.jsonl → docs/cases/<slug>/board.md.

Layout:
  1. Agreement-matrix heatmap (interventions x personas).
  2. Per-intervention sections, each showing each persona's stance + cross-critiques.
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PERSONAS = ["risktaker", "conservative", "critic", "concensusite", "advocate"]


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def fmt(v) -> str:
    if v is None or v == "":
        return "—"
    return html.escape(str(v))


def stance_for_pick(positions: list[dict], persona: str, intervention_id: str) -> str | None:
    """Return persona's rank for this intervention if they picked it, else None."""
    for p in positions:
        if p.get("persona") != persona:
            continue
        for pick in p.get("picks", []) or []:
            if pick.get("intervention_id") == intervention_id:
                return f"rank {pick.get('rank')}"
    return None


def critique_cell(critiques: list[dict], critic: str, intervention_id: str) -> str:
    """Cell-level summary for the agreement matrix."""
    relevant = [
        c for c in critiques
        if c.get("critic_persona") == critic and c.get("target_intervention_id") == intervention_id
    ]
    if not relevant:
        return ""
    levels = sorted({c.get("agreement_level") for c in relevant if c.get("agreement_level")})
    rank = {"endorse": 0, "qualified": 1, "dissent": 2, "veto": 3}
    levels.sort(key=lambda l: rank.get(l, 99))
    if levels:
        return levels[-1]  # most severe wins
    return ""


def cell_class(level: str) -> str:
    return {
        "endorse": "cell-endorse",
        "qualified": "cell-qualified",
        "dissent": "cell-dissent",
        "veto": "cell-veto",
    }.get(level, "cell-absent")


def collect_interventions(positions: list[dict]) -> list[tuple[str, str]]:
    """Return ordered (intervention_id, intervention_label) preserving rank-1 priority."""
    seen: dict[str, str] = {}
    rank1_first: list[str] = []
    others: list[str] = []
    for p in positions:
        for pick in sorted(p.get("picks", []) or [], key=lambda x: x.get("rank") or 999):
            iid = pick.get("intervention_id")
            label = pick.get("intervention_label") or iid
            if not iid or iid in seen:
                continue
            seen[iid] = label
            if pick.get("rank") == 1:
                rank1_first.append(iid)
            else:
                others.append(iid)
    return [(iid, seen[iid]) for iid in rank1_first + others]


def render_matrix(positions: list[dict], critiques: list[dict], interventions: list[tuple[str, str]]) -> str:
    if not interventions:
        return "_No interventions in board output._\n"
    head = "<th>Intervention</th>" + "".join(f"<th>{p}</th>" for p in PERSONAS)
    body_rows = []
    for iid, label in interventions:
        cells = [f"<td><strong>{html.escape(label)}</strong></td>"]
        for persona in PERSONAS:
            stance = stance_for_pick(positions, persona, iid)
            level = critique_cell(critiques, persona, iid)
            display = stance or level or ""
            klass = cell_class(level) if level else ("cell-endorse" if stance else "cell-absent")
            cells.append(f'<td class="{klass}">{html.escape(display)}</td>')
        body_rows.append("    <tr>" + "".join(cells) + "</tr>")
    return (
        '<div class="trial-table-wrap">\n'
        '  <table class="agreement-matrix">\n'
        f'    <thead><tr>{head}</tr></thead>\n'
        f'    <tbody>\n' + "\n".join(body_rows) + "\n    </tbody>\n"
        "  </table>\n"
        "</div>\n"
    )


def render_intervention_section(
    iid: str,
    label: str,
    positions: list[dict],
    critiques: list[dict],
) -> str:
    parts = [f"### {html.escape(label)} (`{html.escape(iid)}`)\n"]
    parts.append("**Persona stances**\n")
    parts.append('<div class="trial-table-wrap"><table class="trial-table"><thead><tr>'
                 '<th>Persona</th><th>Rank</th><th>Confidence</th><th>Rationale</th><th>Concerns</th>'
                 '</tr></thead><tbody>')
    for persona in PERSONAS:
        pos = next((p for p in positions if p.get("persona") == persona), None)
        pick = None
        if pos:
            for x in pos.get("picks", []) or []:
                if x.get("intervention_id") == iid:
                    pick = x
                    break
        if pick:
            parts.append(
                f'<tr><td><span class="persona persona-{persona}">{persona}</span></td>'
                f'<td>{fmt(pick.get("rank"))}</td>'
                f'<td>{fmt(pick.get("confidence"))}</td>'
                f'<td>{fmt(pick.get("rationale"))}</td>'
                f'<td>{html.escape("; ".join(pick.get("primary_concerns") or []) or "—")}</td></tr>'
            )
        else:
            parts.append(
                f'<tr><td><span class="persona persona-{persona}">{persona}</span></td>'
                f'<td>—</td><td>—</td><td><em>did not pick</em></td><td>—</td></tr>'
            )
    parts.append("</tbody></table></div>\n")

    relevant_critiques = [
        c for c in critiques if c.get("target_intervention_id") == iid
    ]
    if relevant_critiques:
        parts.append("\n**Cross-critiques**\n")
        parts.append('<div class="trial-table-wrap"><table class="trial-table"><thead><tr>'
                     '<th>Critic</th><th>Target</th><th>Agreement</th><th>Dimension</th><th>Comment</th>'
                     '</tr></thead><tbody>')
        for c in relevant_critiques:
            parts.append(
                f'<tr><td><span class="persona persona-{c.get("critic_persona")}">{c.get("critic_persona")}</span></td>'
                f'<td>{fmt(c.get("target_persona"))}</td>'
                f'<td><span class="agree-{c.get("agreement_level")}">{fmt(c.get("agreement_level"))}</span></td>'
                f'<td>{fmt(c.get("dimension"))}</td>'
                f'<td>{fmt(c.get("comment"))}</td></tr>'
            )
        parts.append("</tbody></table></div>\n")
    return "\n".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    args = parser.parse_args()
    slug = args.slug

    case_dir = REPO / "data" / "cases" / slug
    positions = load_jsonl(case_dir / "board" / "positions.jsonl")
    critiques = load_jsonl(case_dir / "board" / "critiques.jsonl")

    interventions = collect_interventions(positions)
    matrix = render_matrix(positions, critiques, interventions)

    sections = [render_intervention_section(iid, label, positions, critiques) for iid, label in interventions]

    body = (
        '<meta name="robots" content="noindex">\n\n'
        f"# Tumor-board transcript — `{slug}`\n\n"
        f"_{len(positions)} positions, {len(critiques)} cross-critiques._\n\n"
        "## Agreement matrix\n\n"
        "Cells show round-1 picks (rank N) where the persona endorsed at round 1, "
        "or the round-2 critique level otherwise. Endorse · Qualified · Dissent · Veto · (no opinion).\n\n"
        f"{matrix}\n"
        "## By intervention\n\n"
        + "\n\n".join(sections) + "\n\n"
        f"[Back to case](index.md) · [Trials](trials.md) · [Evidence](evidence.md) · "
        f"[Manuscripts](manuscripts.md) · [Recommendations](recommendations.md)\n\n"
        '!!! danger disclaimer "Decision support, not medical advice"\n'
        "    See [PHI policy](../../phi_policy.md).\n"
    )
    dst = REPO / "docs" / "cases" / slug / "board.md"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(body, encoding="utf-8")
    print(f"wrote {dst} (positions={len(positions)}, critiques={len(critiques)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
