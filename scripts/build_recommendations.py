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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    args = parser.parse_args()
    slug = args.slug

    case_dir = REPO / "data" / "cases" / slug
    rows = load_jsonl(case_dir / "recommendations.jsonl")
    rows.sort(key=lambda r: r.get("rank") or 999)

    if not rows:
        table = "_No recommendations yet._\n"
    else:
        head = (
            "<th>Rank</th><th>Status</th><th>Intervention</th>"
            "<th>Endorsed by</th><th>Dissent</th><th>Veto</th>"
            "<th>Expected benefit</th><th>Key risks</th>"
            "<th>Preference fit</th><th>Guideline</th>"
            "<th>Evidence anchor</th><th>Open questions</th>"
        )
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
        table = (
            '<div class="trial-table-wrap">\n'
            '  <div class="trial-scroll">\n'
            '    <table class="trial-table">\n'
            f'      <thead><tr>{head}</tr></thead>\n'
            '      <tbody>\n' + "\n".join(body) + "\n      </tbody>\n"
            "    </table>\n"
            "  </div>\n"
            "</div>\n"
        )

    body_md = (
        '<meta name="robots" content="noindex">\n\n'
        f"# Recommendations — `{slug}`\n\n"
        '!!! danger disclaimer "Decision support, not medical advice"\n'
        "    Libby is experimental. Recommendations on this page have not been\n"
        "    reviewed by a clinician treating this patient.\n"
        "    See [PHI policy](../../phi_policy.md).\n\n"
        f"_{len(rows)} ranked options._\n\n"
        f"{table}\n"
        f"[Back to case](index.md) · [Trials](trials.md) · [Evidence](evidence.md) · [Board](board.md) · [Plain language](plain_language.md)\n"
    )

    dst = REPO / "docs" / "cases" / slug / "recommendations.md"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(body_md, encoding="utf-8")
    print(f"wrote {dst} ({len(rows)} rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
