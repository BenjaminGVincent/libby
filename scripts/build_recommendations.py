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

REPO = Path(__file__).resolve().parent.parent


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


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


RECS_HEAD = (
    "<th>Rank</th><th>Status</th><th>Intervention</th>"
    "<th>Endorsed by</th><th>Dissent</th><th>Veto</th>"
    "<th>Expected benefit</th><th>Key risks</th>"
    "<th>Preference fit</th><th>Guideline</th>"
    "<th>Evidence anchor</th><th>Open questions</th>"
)


def render_recs_table(rows: list[dict]) -> str:
    if not rows:
        return "_No rows in this scenario._\n"
    body = []
    for r in rows:
        status = r.get("status", "recommended")
        klass = status_class(status)
        body.append(
            "    <tr>"
            f"<td>{fmt(r.get('rank'))}</td>"
            f'<td class="{klass}">{html.escape(status)}</td>'
            f"<td><strong>{fmt(r.get('intervention_label'))}</strong></td>"
            f"<td>{persona_badges(r.get('endorsed_by'))}</td>"
            f"<td>{persona_badges(r.get('dissent_by'))}</td>"
            f"<td>{persona_badges(r.get('veto_by'))}</td>"
            f"<td>{fmt(r.get('expected_benefit'))}</td>"
            f"<td>{fmt(r.get('key_risks'))}</td>"
            f"<td>{fmt(r.get('preference_alignment'))}</td>"
            f"<td>{fmt(r.get('guideline_status'))}</td>"
            f"<td>{fmt(r.get('evidence_anchor'))}</td>"
            f"<td>{fmt(r.get('open_questions'))}</td>"
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


def group_by_scenario(rows: list[dict]) -> tuple[list[dict], dict[str, dict]]:
    """Split rows into (shared_rows, scenarios_by_key).

    `shared_rows` are rows with scenario in (None, "", "shared") — they apply
    to every branch (typically rank-1 workup steps). `scenarios_by_key` maps
    each non-shared scenario string to {"label": str, "rows": [dict]}.
    """
    shared: list[dict] = []
    scenarios: dict[str, dict] = {}
    for r in rows:
        scen = r.get("scenario")
        if not scen or scen == "shared":
            shared.append(r)
            continue
        scenarios.setdefault(scen, {"label": r.get("scenario_label") or scen, "rows": []})
        scenarios[scen]["rows"].append(r)
    shared.sort(key=lambda r: r.get("rank") or 999)
    for s in scenarios.values():
        s["rows"].sort(key=lambda r: r.get("rank") or 999)
    return shared, scenarios


def downloads_block(case_docs: Path, slug: str) -> str:
    """Surface reporter-built artifacts at the top of recommendations.md.

    Empty string when none exist yet — keeps the page clean before /reporter
    has run, and the page doesn't need a re-render once it does (the
    reporter calls back through run_case.sh which re-runs this script).
    """
    artifacts = [
        (
            f"{slug}-libby-report.pdf",
            "Clinician PDF report",
            "ranked recommendations + evidence + sources",
        ),
        (
            f"{slug}-plain-language.pdf",
            "Patient/caregiver PDF",
            "plain-language summary",
        ),
        (
            f"{slug}-recommendations.html",
            "Self-contained HTML",
            "recommendations table that opens offline",
        ),
    ]
    present = [(name, label, blurb) for name, label, blurb in artifacts if (case_docs / name).exists()]
    if not present:
        return ""
    lines = ["## Downloads\n"]
    for name, label, blurb in present:
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

    shared, scenarios = group_by_scenario(rows)

    parts = [
        '<meta name="robots" content="noindex">\n',
        f"# Recommendations — `{slug}`\n",
    ]

    case_docs = REPO / "docs" / "cases" / slug
    dl = downloads_block(case_docs, slug)
    if dl:
        parts.append(dl)

    if scenarios:
        parts.append(
            f"_{len(rows)} rows across {len(scenarios)} scenario(s) "
            f"plus {len(shared)} shared row(s)._\n"
        )
        if shared:
            parts.append("## Shared first step (applies to every scenario)\n")
            parts.append(render_recs_table(shared))
        for key, payload in scenarios.items():
            parts.append(f"## {payload['label']}\n")
            parts.append(f'<small><code>scenario: {html.escape(key)}</code></small>\n')
            parts.append(render_recs_table(payload["rows"]))
    else:
        parts.append(f"_{len(rows)} ranked options._\n")
        parts.append(render_recs_table(shared))

    parts.append(
        f"[Back to case](index.md) · [Trials](trials.md) · "
        f"[Evidence](evidence.md) · [Board](board.md) · "
        f"[Plain language](plain_language.md)\n"
    )
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
