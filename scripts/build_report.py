#!/usr/bin/env python3
"""
Compose a Libby case's external-review artifacts:

  1. docs/cases/<slug>/<slug>-libby-report.pdf
       Clinician-grade PDF: cover -> executive summary -> PI's index.md body
       (verbatim, with the page-chrome stripped) -> sources appendix.
  2. docs/cases/<slug>/<slug>-plain-language.pdf
       Patient/caregiver PDF wrapping plain_language.md with a friendlier cover.
       Skipped if plain_language.md does not exist yet.
  3. docs/cases/<slug>/<slug>-recommendations.html
       Self-contained HTML of the ranked recommendations table (scenarios
       respected). Inlines the trial-table + libby palette so it works
       offline without MkDocs Material.

Usage:
    python3 scripts/build_report.py <slug>

Reads (read-only):
    data/cases/<slug>/executive_summary.md   (owned by reporter)
    data/cases/<slug>/recommendations.jsonl  (owned by PI)
    data/cases/<slug>/profile.json
    data/cases/<slug>/preferences.json
    docs/cases/<slug>/index.md               (owned by PI)
    docs/cases/<slug>/plain_language.md      (owned by translator; optional)

Writes:
    docs/cases/<slug>/<slug>-libby-report.pdf
    docs/cases/<slug>/<slug>-plain-language.pdf      (when source exists)
    docs/cases/<slug>/<slug>-recommendations.html

Pure Python; depends on `fpdf2` (declared in pyproject.toml). No system libs.
The renderer is adapted from io-shieldbreak/scripts/build_report.py — same
markdown subset (paragraphs, ###/####, bullets, ordered lists, GFM tables,
inline bold/italic/links/code, hr) plus a self-contained HTML emitter.
"""

from __future__ import annotations

import hashlib
import html as _html
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data" / "cases"
DOCS_DIR = REPO_ROOT / "docs" / "cases"


# ---------- input loading ----------


def _load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def _load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


# ---------- markdown post-processing ----------


# Strip MkDocs / Material chrome that has no meaning outside the live site.
_RX_NOINDEX = re.compile(r'^\s*<meta name="robots"[^>]*>\s*$', re.MULTILINE)
_RX_DISCLAIMER_ADMONITION = re.compile(
    r'^!!! (?:danger\s+)?(?:disclaimer|warning)\b[^\n]*\n(?:[ \t]+[^\n]*\n)+',
    re.MULTILINE,
)
_RX_NAV_FOOTER = re.compile(
    r'^\[Back to case\]\(index\.md\)[^\n]*\n?',
    re.MULTILINE,
)


def _strip_page_chrome(md: str) -> str:
    md = _RX_NOINDEX.sub("", md)
    md = _RX_DISCLAIMER_ADMONITION.sub("", md)
    md = _RX_NAV_FOOTER.sub("", md)
    return md.lstrip("\n")


def _drop_h1(md: str) -> str:
    """Drop the leading `# Title` line — the cover already carries the title."""
    return re.sub(r"\A#\s[^\n]*\n+", "", md, count=1)


# ---------- sources appendix ----------


_RX_PMID = re.compile(r"^pmid:(.+)$", re.IGNORECASE)
_RX_NCT = re.compile(r"^nct:(.+)$", re.IGNORECASE)


def _collect_sources(recs: list[dict]) -> tuple[list[str], list[str]]:
    pmids: list[str] = []
    ncts: list[str] = []
    seen_pmid: set[str] = set()
    seen_nct: set[str] = set()
    for r in recs:
        for anchor in r.get("evidence_anchor") or []:
            anchor = str(anchor).strip()
            m = _RX_PMID.match(anchor)
            if m:
                pid = m.group(1).strip()
                if pid and pid not in seen_pmid:
                    seen_pmid.add(pid)
                    pmids.append(pid)
                continue
            m = _RX_NCT.match(anchor)
            if m:
                nid = m.group(1).strip()
                if nid and nid not in seen_nct:
                    seen_nct.add(nid)
                    ncts.append(nid)
    return pmids, ncts


def _sources_markdown(recs: list[dict]) -> str:
    pmids, ncts = _collect_sources(recs)
    if not pmids and not ncts:
        return ""
    parts = ["## Sources\n"]
    if pmids:
        parts.append("**PubMed (PMID):**\n")
        for pid in pmids:
            parts.append(f"- [{pid}](https://pubmed.ncbi.nlm.nih.gov/{pid})")
        parts.append("")
    if ncts:
        parts.append("**ClinicalTrials.gov (NCT):**\n")
        for nid in ncts:
            parts.append(f"- [{nid}](https://clinicaltrials.gov/study/{nid})")
        parts.append("")
    return "\n".join(parts)


# ---------- standalone HTML ----------


_INLINE_CSS = """
:root {
  --ink: #1A202C;
  --ink-muted: #4A5568;
  --rule: #E2E8F0;
  --header-bg: #F4F6F8;
  --accent: #5B3A87;
  --bg: #FFFFFF;
  --warn-fg: #6F2E1A;
  --warn-bg: #FBE9E7;
  --warn-border: #ECC4BB;
}
body {
  font-family: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif;
  color: var(--ink);
  background: var(--bg);
  max-width: 80rem;
  margin: 2rem auto;
  padding: 0 1.5rem;
  line-height: 1.5;
}
h1, h2, h3 { color: var(--ink); }
h1 { font-size: 1.6rem; }
h2 { font-size: 1.2rem; margin-top: 2rem; }
h3 { font-size: 1.05rem; margin-top: 1.5rem; }
small.scenario-key { color: var(--ink-muted); }
.disclaimer {
  border: 1px solid var(--warn-border);
  background: var(--warn-bg);
  color: var(--warn-fg);
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;
  margin: 1rem 0 2rem;
  font-size: 0.95rem;
}
.disclaimer strong { color: #B71C1C; }
.profile-grid {
  display: grid;
  grid-template-columns: max-content 1fr;
  gap: 0.25rem 1rem;
  margin: 1rem 0 2rem;
  font-size: 0.95rem;
}
.profile-grid dt { font-weight: 600; color: var(--ink-muted); }
.profile-grid dd { margin: 0; }
.trial-table-wrap { color: var(--ink); }
.trial-scroll { overflow-x: auto; }
.trial-table {
  border-collapse: collapse;
  width: 100%;
  font-size: 0.88em;
}
.trial-table thead th {
  background: var(--header-bg);
  font-weight: 600;
  text-align: left;
  padding: 0.5em 0.6em;
  border-top: 2px solid var(--ink);
  border-bottom: 1px solid var(--ink);
  white-space: nowrap;
}
.trial-table tbody td {
  padding: 0.5em 0.6em;
  border-bottom: 1px solid var(--rule);
  font-variant-numeric: tabular-nums;
  vertical-align: top;
}
.trial-table tbody tr:last-child td {
  border-bottom: 2px solid var(--ink);
}
.persona {
  display: inline-block;
  padding: 0.05em 0.5em;
  border-radius: 0.35em;
  font-size: 0.78em;
  font-weight: 600;
  margin-right: 0.25em;
  border: 1px solid transparent;
}
.persona-risktaker    { background: #FFE9D6; color: #6F3A0F; border-color: #F0CFAE; }
.persona-conservative { background: #DFEBFB; color: #1B3A6B; border-color: #B5CDEE; }
.persona-critic       { background: #F1E5FF; color: #441E72; border-color: #D4BBF2; }
.persona-concensusite { background: #DDF1EE; color: #134E48; border-color: #B0DBD3; }
.persona-advocate     { background: #FFE5EE; color: #6E1638; border-color: #F0BBCB; }
.split-glyph { font-weight: 700; color: #5A4500; }
.not-recommended {
  color: var(--ink-muted);
  text-decoration: line-through;
}
.scenario-conditional {
  display: inline-block;
  font-size: 0.78em;
  font-weight: 600;
  color: #5A4500;
  background: #FFF7E0;
  border: 1px solid #F1DD9A;
  border-radius: 0.35em;
  padding: 0.05em 0.45em;
  margin-left: 0.35em;
  white-space: nowrap;
}
.pipeline-note {
  color: var(--ink-muted);
  font-size: 0.9rem;
  margin: 0.25rem 0 0.75rem;
}
.pipeline-context-table { font-size: 0.82em; color: var(--ink-muted); }
.pipeline-context-table thead th {
  background: #FAFAFA;
  border-top: 1px solid var(--ink-muted);
  border-bottom: 1px solid var(--ink-muted);
}
.pipeline-context-table tbody tr:last-child td { border-bottom: 1px solid var(--ink-muted); }
.pipeline-context-table .intervention-name { color: var(--ink); font-weight: 600; }
.pipeline-context-table .alias-list { color: var(--ink-muted); font-size: 0.9em; }
.pipeline-context-table .basket-flag {
  display: inline-block;
  font-size: 0.78em;
  font-weight: 600;
  color: #134E48;
  background: #DDF1EE;
  border: 1px solid #B0DBD3;
  border-radius: 0.35em;
  padding: 0.02em 0.4em;
  margin-left: 0.35em;
  white-space: nowrap;
}
.pipeline-context-table .discontinued-flag {
  display: inline-block;
  font-size: 0.78em;
  font-weight: 600;
  color: #5A2A2A;
  background: #F2E1E1;
  border: 1px solid #DDB7B7;
  border-radius: 0.35em;
  padding: 0.02em 0.4em;
  margin-left: 0.35em;
  white-space: nowrap;
}
footer.libby-footer {
  margin-top: 3rem;
  padding-top: 1rem;
  border-top: 1px solid var(--rule);
  color: var(--ink-muted);
  font-size: 0.85rem;
}
"""


def _persona_badges_html(personas: list[str] | None) -> str:
    if not personas:
        return "&mdash;"
    return " ".join(
        f'<span class="persona persona-{_html.escape(p)}">{_html.escape(p)}</span>'
        for p in personas
    )


def _fmt_html(v) -> str:
    if v is None or v == "":
        return "&mdash;"
    if isinstance(v, list):
        return "; ".join(_html.escape(str(x)) for x in v) or "&mdash;"
    return _html.escape(str(v))


def _status_class(status: str) -> str:
    return {
        "recommended": "",
        "considered_with_caveats": "split-glyph",
        "not_recommended": "not-recommended",
    }.get(status, "")


_RECS_HEAD_HTML = (
    "<th>Rank</th><th>Intervention</th>"
    "<th>Likelihood of effect</th><th>Toxicity burden</th>"
    "<th>Counter-productive MoA</th><th>Overall</th>"
)


def _persona_line_html(r: dict) -> str:
    pieces: list[str] = []
    for label, key in (("endorse", "endorsed_by"), ("dissent", "dissent_by"), ("veto", "veto_by")):
        personas = r.get(key) or []
        if not personas:
            continue
        pills = " ".join(
            f'<span class="persona persona-{_html.escape(p)}">{_html.escape(p)}</span>' for p in personas
        )
        pieces.append(f'<small><em>{label}:</em> {pills}</small>')
    return "<br>".join(pieces)


def _intervention_cell_html(r: dict, *, show_personas: bool = True) -> str:
    label = _fmt_html(r.get("intervention_label"))
    scen = r.get("scenario")
    if isinstance(scen, str) and scen.endswith(":positive"):
        biomarker_short = scen.split(":", 1)[0]
        head = (
            f"<strong>{label}</strong> "
            f'<span class="scenario-conditional">(conditional on {_html.escape(biomarker_short)} positive)</span>'
        )
    else:
        head = f"<strong>{label}</strong>"
    if show_personas:
        persona = _persona_line_html(r)
        body = f"{head}<br>{persona}" if persona else head
    else:
        body = head
    return f"<td>{body}</td>"


def _cpm_cell_html(r: dict) -> str:
    cpm = r.get("counter_productive_moa") or {}
    severity = cpm.get("severity")
    description = cpm.get("description")
    if not severity:
        return "<td>&mdash;</td>"
    sev_html = f"<strong>{_html.escape(str(severity))}</strong>"
    if description:
        return f'<td>{sev_html} <span class="cpm-desc">({_html.escape(str(description))})</span></td>'
    return f"<td>{sev_html}</td>"


def _overall_cell_html(r: dict) -> str:
    overall = r.get("overall")
    if not overall:
        return "<td>&mdash;</td>"
    return f"<td><strong>{_html.escape(str(overall))}</strong></td>"


def _render_recs_table_html(
    rows: list[dict], *, show_personas: bool = True, renumber: bool = False
) -> str:
    """Render rows as the recs HTML table.

    `renumber=True` rewrites the Rank cell to the row's 1-based position
    within `rows` (used by the per-feature tables in the self-contained
    HTML, where each pathway gets its own ranked list 1..n rather than
    inheriting the global ranking series). The underlying `rank` field on
    the row is unchanged.
    """
    if not rows:
        return "<p><em>No rows.</em></p>"
    body: list[str] = []
    for i, r in enumerate(rows, start=1):
        rank_cell = i if renumber else r.get("rank")
        body.append(
            "    <tr>"
            f"<td>{_fmt_html(rank_cell)}</td>"
            f"{_intervention_cell_html(r, show_personas=show_personas)}"
            f"<td>{_fmt_html(r.get('likelihood_of_effect'))}</td>"
            f"<td>{_fmt_html(r.get('toxicity_burden'))}</td>"
            f"{_cpm_cell_html(r)}"
            f"{_overall_cell_html(r)}"
            "</tr>"
        )
    return (
        '<div class="trial-table-wrap">\n'
        '  <div class="trial-scroll">\n'
        '    <table class="trial-table">\n'
        f'      <thead><tr>{_RECS_HEAD_HTML}</tr></thead>\n'
        '      <tbody>\n' + "\n".join(body) + "\n      </tbody>\n"
        "    </table>\n  </div>\n</div>\n"
    )


_FEATURE_LABELS: dict[str, str] = {
    # Friendlier human-readable names for known scenario_short prefixes.
    # Any prefix not in this map renders title-cased.
    "dll3_ihc": "DLL3-targeting interventions",
    "prame_ihc_hla": "PRAME-targeting interventions",
}


def _feature_label_for_scenario(scenario_short: str) -> str:
    if scenario_short in _FEATURE_LABELS:
        return _FEATURE_LABELS[scenario_short]
    pretty = scenario_short.replace("_", " ").title()
    return f"{pretty} interventions"


def _group_by_feature(rows: list[dict]) -> "list[tuple[str, list[dict]]]":
    """Group biomarker-conditional rows by their scenario prefix.

    Returns an ordered list of (scenario_short, rows) pairs, preserving the
    order in which scenarios first appear in `rows`. Untagged (`scenario`
    null/empty/'shared') rows go under the synthetic key `__unscoped`.
    The HTML composer renders one table per feature.
    """
    seen: list[str] = []
    by_feature: dict[str, list[dict]] = {}
    for r in rows:
        scen = r.get("scenario")
        if isinstance(scen, str) and ":" in scen:
            key = scen.split(":", 1)[0]
        else:
            key = "__unscoped"
        if key not in by_feature:
            by_feature[key] = []
            seen.append(key)
        by_feature[key].append(r)
    for k in by_feature:
        by_feature[k].sort(key=lambda r: r.get("rank") or 999)
    return [(k, by_feature[k]) for k in seen]


def _group_by_scenario(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    """Split rows into (workup_rows, unified_rows).

    `workup_rows` are rows with `scenario == "shared"` — the rank-1 confirmatory
    test. `unified_rows` is everything else: biomarker-conditional recs
    tagged `scenario: "<biomarker_short>:positive"` in gated cases, or
    untagged `scenario: null` recs in non-gated cases. Rank-ordered for a
    single ranked table. Conditional recs surface the (conditional on …)
    flag at render time.
    """
    workup: list[dict] = []
    unified: list[dict] = []
    for r in rows:
        scen = r.get("scenario")
        if scen == "shared":
            workup.append(r)
        else:
            unified.append(r)
    workup.sort(key=lambda r: r.get("rank") or 999)
    unified.sort(key=lambda r: r.get("rank") or 999)
    return workup, unified


def _profile_dl_html(profile: dict, preferences: dict) -> str:
    if not profile and not preferences:
        return ""
    rows: list[tuple[str, str]] = []
    if profile:
        for label, key in (
            ("Primary site", "primary_site"),
            ("Histology", "histology"),
            ("Stage", "stage"),
            ("ECOG", "ecog"),
            ("Age band", "age_band"),
            ("Sex", "sex"),
        ):
            v = profile.get(key)
            if v not in (None, ""):
                rows.append((label, str(v)))
        biomarkers = profile.get("biomarkers") or []
        if biomarkers:
            biomarker_strs = []
            for b in biomarkers:
                pieces = [str(b.get("name") or "?")]
                if b.get("value") not in (None, ""):
                    pieces.append(str(b["value"]))
                if b.get("confirmation_status") and b["confirmation_status"] != "confirmed":
                    pieces.append(f"({b['confirmation_status']})")
                biomarker_strs.append(" ".join(pieces))
            rows.append(("Biomarkers", "; ".join(biomarker_strs)))
    if preferences:
        w = preferences.get("efficacy_toxicity_weight")
        if w is not None:
            rows.append(("Efficacy/toxicity weight", str(w)))
        toxv = preferences.get("toxicity_vetoes") or []
        if toxv:
            rows.append(("Toxicity vetoes", ", ".join(str(x) for x in toxv)))
        mods = preferences.get("modality_constraints") or []
        if mods:
            rows.append(("Modality constraints", ", ".join(str(x) for x in mods)))
        if preferences.get("trials_preferred") is not None:
            rows.append(("Trials preferred", "yes" if preferences["trials_preferred"] else "no"))
    if not rows:
        return ""
    items = "\n".join(
        f"  <dt>{_html.escape(label)}</dt><dd>{_html.escape(value)}</dd>"
        for label, value in rows
    )
    return f'<dl class="profile-grid">\n{items}\n</dl>\n'


_FEATURE_TOKENS: dict[str, tuple[str, ...]] = {
    # Substring tokens (lowercased) used to assign a trial row to a feature
    # for the pipeline-context tables. Matched against intervention,
    # aliases, and biomarker fields.
    "dll3_ihc": ("dll3",),
    "prame_ihc_hla": ("prame",),
}


def _classify_trial_feature(trial: dict) -> str | None:
    """Best-effort feature key for a trials.jsonl row.

    Returns one of the keys in `_FEATURE_TOKENS` (e.g. `dll3_ihc`) when the
    trial's intervention / aliases / biomarker mention that token, else None.
    Used to bucket pipeline-context rows under the right per-feature heading
    in the self-contained HTML report.
    """
    haystack_parts: list[str] = []
    for key in ("intervention", "biomarker"):
        val = trial.get(key)
        if isinstance(val, str):
            haystack_parts.append(val.lower())
    aliases = trial.get("aliases") or []
    if isinstance(aliases, list):
        haystack_parts.extend(str(a).lower() for a in aliases)
    haystack = " ".join(haystack_parts)
    for feature_key, tokens in _FEATURE_TOKENS.items():
        if any(tok in haystack for tok in tokens):
            return feature_key
    return None


def _ranked_drug_aliases(recs: list[dict], trials: list[dict]) -> set[str]:
    """Lowercased alias tokens for drugs already represented in ranked recs.

    For each non-workup ranked rec, look up trials whose `nct_id` appears in
    the rec's `evidence_anchor` (`nct:NCTxxxxxxxx`) and harvest their
    `intervention` + `aliases`. Used to suppress those drugs from the
    pipeline-context table — the user wants to see *other* options, not the
    same drug twice.
    """
    ranked_ncts: set[str] = set()
    for r in recs:
        if r.get("scenario") == "shared":
            continue
        for anchor in r.get("evidence_anchor") or []:
            if isinstance(anchor, str) and anchor.lower().startswith("nct:"):
                ranked_ncts.add(anchor.split(":", 1)[1].strip())
    aliases: set[str] = set()
    for t in trials:
        if t.get("nct_id") in ranked_ncts:
            interv = t.get("intervention")
            if isinstance(interv, str):
                aliases.add(interv.lower())
            for a in t.get("aliases") or []:
                if isinstance(a, str):
                    aliases.add(a.lower())
    # Strip parenthetical class qualifiers like "tarlatamab (DLL3 × CD3 BiTE)"
    # so a trial whose `intervention` is bare "tarlatamab" still matches.
    cleaned: set[str] = set()
    for a in aliases:
        cleaned.add(a)
        if "(" in a:
            cleaned.add(a.split("(", 1)[0].strip())
    return {a for a in cleaned if a}


def _trial_matches_ranked_drug(trial: dict, ranked_aliases: set[str]) -> bool:
    """True if the trial's intervention or aliases overlap a ranked drug.

    Compared on lowercased exact string match against the cleaned alias set
    (see `_ranked_drug_aliases`). Used to dedupe pipeline-context rows.
    """
    interv = (trial.get("intervention") or "").lower()
    if interv in ranked_aliases:
        return True
    if "(" in interv and interv.split("(", 1)[0].strip() in ranked_aliases:
        return True
    for a in trial.get("aliases") or []:
        if isinstance(a, str) and a.lower() in ranked_aliases:
            return True
    return False


def _phase_sort_key(phase: object) -> float:
    """Return a numeric ordering key for a phase string ('3' > '2' > '1/2' > '1').

    Phase strings vary ('1', '1/2', '2', '3'); '1/2' is treated as halfway
    between '1' and '2' so it sorts strictly between them. Negative so
    descending sort puts the most-advanced phase first.
    """
    if not isinstance(phase, str):
        return 0.0
    s = phase.strip()
    if "/" in s:
        parts = [int(p) for p in s.split("/") if p.strip().isdigit()]
        if parts:
            return -(min(parts) + 0.5)
    if s.isdigit():
        return -int(s)
    return 0.0


def _tumor_relationship_sort_key(rel: object) -> int:
    """Sort key: basket/biomarker rows before cross-tumor extrapolation.

    `basket_or_biomarker_match` is the more decision-relevant class because
    eligibility may turn on sponsor confirmation rather than a categorical
    cross-tumor extrapolation; surface those first.
    """
    if rel == "basket_or_biomarker_match":
        return 0
    if rel == "cross_tumor_extrapolation":
        return 1
    return 2


def _pipeline_context_rows(
    feature_key: str, trials: list[dict], ranked_aliases: set[str]
) -> list[dict]:
    """Filter + sort trials.jsonl rows for the pipeline-context table.

    Keeps trials that target `feature_key` and whose drug isn't already in
    the ranked table. Sorted by tumor-type relationship (basket first), then
    phase (most-advanced first), with NCT as a stable tiebreaker.
    """
    out: list[dict] = []
    for t in trials:
        if _classify_trial_feature(t) != feature_key:
            continue
        if _trial_matches_ranked_drug(t, ranked_aliases):
            continue
        out.append(t)
    out.sort(
        key=lambda t: (
            1 if t.get("development_status") == "discontinued" else 0,
            _tumor_relationship_sort_key(t.get("tumor_type_relationship")),
            _phase_sort_key(t.get("phase")),
            (t.get("nct_id") or ""),
        )
    )
    return out


_PIPELINE_HEAD_HTML = (
    "<th>Intervention</th><th>Modality</th><th>Phase</th>"
    "<th>Enrolling indication</th><th>Recruitment</th><th>Trial</th>"
)


def _pipeline_intervention_cell_html(t: dict) -> str:
    interv = t.get("intervention") or "—"
    aliases = t.get("aliases") or []
    extras: list[str] = []
    for a in aliases:
        if not isinstance(a, str):
            continue
        if a.lower() in interv.lower():
            continue
        extras.append(a)
    flag_html = ""
    if t.get("tumor_type_relationship") == "basket_or_biomarker_match":
        flag_html = ' <span class="basket-flag">basket / biomarker</span>'
    if t.get("development_status") == "discontinued":
        flag_html += ' <span class="discontinued-flag">discontinued</span>'
    name = (
        f'<span class="intervention-name">{_html.escape(str(interv))}</span>'
        f"{flag_html}"
    )
    if extras:
        alias_str = ", ".join(_html.escape(a) for a in extras[:3])
        name += f'<br><span class="alias-list">{alias_str}</span>'
    return f"<td>{name}</td>"


def _pipeline_trial_cell_html(t: dict) -> str:
    nct = t.get("nct_id")
    if not nct:
        return "<td>&mdash;</td>"
    href = f"https://clinicaltrials.gov/study/{_html.escape(nct)}"
    sponsor = t.get("sponsor")
    sponsor_html = ""
    if isinstance(sponsor, str) and sponsor.strip() and sponsor.strip() != "—":
        sponsor_html = f'<br><span class="alias-list">{_html.escape(sponsor)}</span>'
    return (
        f'<td><a href="{href}" target="_blank" rel="noopener noreferrer">'
        f"{_html.escape(nct)}</a>{sponsor_html}</td>"
    )


def _render_pipeline_context_table_html(rows: list[dict]) -> str:
    """Render the pipeline-context (not-currently-enrollable) table for one feature.

    Smaller / muted styling deliberately distinguishes it from the ranked
    options table above. Columns are deliberately leaner: intervention,
    modality, phase, enrolling indication, recruitment status, trial NCT.
    """
    if not rows:
        return ""
    body: list[str] = []
    for t in rows:
        body.append(
            "    <tr>"
            f"{_pipeline_intervention_cell_html(t)}"
            f"<td>{_fmt_html(t.get('modality'))}</td>"
            f"<td>{_fmt_html(t.get('phase'))}</td>"
            f"<td>{_fmt_html(t.get('indication'))}</td>"
            f"<td>{_fmt_html(t.get('recruitment_status'))}</td>"
            f"{_pipeline_trial_cell_html(t)}"
            "</tr>"
        )
    return (
        '<div class="trial-table-wrap">\n'
        '  <div class="trial-scroll">\n'
        '    <table class="trial-table pipeline-context-table">\n'
        f'      <thead><tr>{_PIPELINE_HEAD_HTML}</tr></thead>\n'
        '      <tbody>\n' + "\n".join(body) + "\n      </tbody>\n"
        "    </table>\n  </div>\n</div>\n"
    )


def _render_recommendations_html(
    slug: str,
    recs: list[dict],
    profile: dict,
    preferences: dict,
    trials: list[dict] | None = None,
) -> str:
    """Self-contained recommendations HTML, designed for forwarding offline.

    Four deliberate departures from the deterministic recommendations.md page:
      1. Persona pills (endorse / dissent / veto) are dropped — full per-persona
         rationale lives on board.md, and a forwardable artifact wants the
         clinical bottom line without the multi-agent voting metadata.
      2. Therapeutic options are grouped by targetable feature (one HTML table
         per scenario prefix — DLL3-targeting, PRAME-targeting, etc.) so the
         reader sees each pathway as its own ranked list rather than as a
         single mixed table.
      3. Workup rows (`scenario: "shared"`) are excluded — biomarker testing
         is documented in the standalone Target validation paths report.
      4. Each per-feature section is followed by a "pipeline context" table
         enumerating other agents in the same target class drawn from
         trials.jsonl — the agents the patient cannot currently enroll in
         (mostly cross-tumor SCLC/melanoma trials) but that shape how the
         board reasons about the modality landscape. Drugs already in the
         ranked table are excluded so the same agent doesn't appear twice.
    """
    today = datetime.now(timezone.utc).date().isoformat()
    trials = trials or []

    # (1) drop workup rows; (2) group remaining by scenario prefix.
    therapeutic_rows = [r for r in recs if r.get("scenario") != "shared"]
    feature_groups = _group_by_feature(therapeutic_rows)
    ranked_aliases = _ranked_drug_aliases(recs, trials)

    parts = [
        '<!DOCTYPE html>',
        '<html lang="en">',
        '<head>',
        '<meta charset="utf-8">',
        '<meta name="robots" content="noindex">',
        f'<title>Libby recommendations &mdash; {_html.escape(slug)}</title>',
        '<style>',
        _INLINE_CSS,
        '</style>',
        '</head>',
        '<body>',
        f'<h1>Libby recommendations &mdash; <code>{_html.escape(slug)}</code></h1>',
        '<div class="disclaimer">',
        '<strong>Decision support, not medical advice.</strong> Libby is an experimental ',
        'multi-agent decision-support tool. The recommendations below have not been ',
        'reviewed by a clinician treating this patient. Do not act on this page without ',
        'consulting a qualified oncologist.',
        '</div>',
    ]

    profile_html = _profile_dl_html(profile, preferences)
    if profile_html:
        parts.append("<h2>Profile snapshot</h2>")
        parts.append(profile_html)

    def _emit_feature_block(scenario_short: str, group_rows: list[dict], heading: str | None) -> None:
        if heading:
            parts.append(f"<h2>{_html.escape(heading)}</h2>")
        parts.append(_render_recs_table_html(group_rows, show_personas=False, renumber=True))
        if scenario_short == "__unscoped" or not trials:
            return
        pipeline_rows = _pipeline_context_rows(scenario_short, trials, ranked_aliases)
        if not pipeline_rows:
            return
        parts.append("<h3>Pipeline context &mdash; not currently enrollable</h3>")
        parts.append(
            '<p class="pipeline-note">Other agents in this target class drawn from the case '
            "dossier. The patient cannot currently enroll in these trials (most enroll a "
            "different tumor type), but they are included for context on the broader "
            "modality landscape. Drugs already listed in the ranked table above are not "
            "repeated here.</p>"
        )
        parts.append(_render_pipeline_context_table_html(pipeline_rows))

    if not therapeutic_rows:
        parts.append("<p><em>No therapeutic recommendations.</em></p>")
    elif len(feature_groups) > 1:
        parts.append(
            f"<p><em>{len(therapeutic_rows)} ranked therapeutic options across "
            f"{len(feature_groups)} targetable features. Biomarker workup steps "
            "live in the standalone Target validation paths report.</em></p>"
        )
        for scenario_short, group_rows in feature_groups:
            heading = (
                _feature_label_for_scenario(scenario_short)
                if scenario_short != "__unscoped"
                else "Biomarker-independent options"
            )
            _emit_feature_block(scenario_short, group_rows, heading)
    else:
        # Single feature — no need for per-feature headings.
        parts.append(
            f"<p><em>{len(therapeutic_rows)} ranked therapeutic options. "
            "Biomarker workup steps live in the standalone Target validation paths report.</em></p>"
        )
        scenario_short, group_rows = feature_groups[0]
        heading = (
            _feature_label_for_scenario(scenario_short)
            if scenario_short != "__unscoped"
            else None
        )
        _emit_feature_block(scenario_short, group_rows, heading)

    parts.append(
        '<footer class="libby-footer">'
        f'Generated {_html.escape(today)} &middot; Libby &middot; <code>{_html.escape(slug)}</code>'
        '</footer>'
    )
    parts.append('</body></html>')
    return "\n".join(parts) + "\n"


# ---------- PDF rendering (adapted from io-shieldbreak) ----------


# Color palette (RGB tuples)
INK = (26, 26, 38)
INK_MUTED = (107, 107, 127)
INK_FAINT = (164, 164, 178)
ACCENT = (91, 58, 135)
RULE = (180, 180, 196)
RULE_FAINT = (220, 220, 228)
ROW_ALT = (250, 250, 253)
HEADER_BG = (236, 237, 246)
COVER_BG = (244, 240, 251)
COVER_BG_PATIENT = (240, 248, 244)


_FONT_FAMILY = "Helvetica"


_FONT_CANDIDATES = {
    "": [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    ],
    "B": [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
    ],
    "I": [
        "/System/Library/Fonts/Supplemental/Arial Italic.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Oblique.ttf",
    ],
    "BI": [
        "/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-BoldOblique.ttf",
    ],
}


_ASCII_SUBS = {
    "•": "*", "—": "--", "–": "-", "−": "-", "…": "...",
    "↑": "^", "↓": "v", "→": "->", "←": "<-", "↔": "<->",
    "≥": ">=", "≤": "<=", "≠": "!=", "≈": "~=", "±": "+/-",
    "“": '"', "”": '"', "‘": "'", "’": "'", "·": "-", "×": "x",
    "™": "(TM)", "®": "(R)", "©": "(C)", "°": " deg",
    "α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta",
    "ε": "epsilon", "ζ": "zeta", "η": "eta", "θ": "theta",
    "ι": "iota", "κ": "kappa", "λ": "lambda", "μ": "mu", "µ": "mu",
    "ν": "nu", "ξ": "xi", "π": "pi", "ρ": "rho", "σ": "sigma",
    "τ": "tau", "υ": "upsilon", "φ": "phi", "χ": "chi",
    "ψ": "psi", "ω": "omega",
    "Α": "Alpha", "Β": "Beta", "Γ": "Gamma", "Δ": "Delta",
    "Ε": "Epsilon", "Λ": "Lambda", "Μ": "Mu", "Π": "Pi",
    "Σ": "Sigma", "Φ": "Phi",
}


def _register_unicode_font(pdf) -> str:
    global _FONT_FAMILY
    found_any = False
    for style, paths in _FONT_CANDIDATES.items():
        for p in paths:
            if Path(p).exists():
                pdf.add_font("libby-body", style=style, fname=p)
                found_any = True
                break
    _FONT_FAMILY = "libby-body" if found_any else "Helvetica"
    return _FONT_FAMILY


def _ascii_fallback(text: str) -> str:
    if _FONT_FAMILY != "Helvetica":
        return text
    out: list[str] = []
    for ch in text:
        if ch in _ASCII_SUBS:
            out.append(_ASCII_SUBS[ch])
        elif ord(ch) <= 0xFF:
            out.append(ch)
        else:
            out.append("?")
    return "".join(out)


def XPos_LMARGIN():
    from fpdf.enums import XPos
    return XPos.LMARGIN


def YPos_NEXT():
    from fpdf.enums import YPos
    return YPos.NEXT


# ---------- markdown block renderer ----------


_TABLE_LINE = re.compile(r"^\s*\|.*\|\s*$")
_TABLE_SEP = re.compile(r"^\s*\|?[\s|:\-]+\|?\s*$")
_INLINE_BOLD = re.compile(r"\*\*(.+?)\*\*")
_INLINE_ITALIC = re.compile(r"(?<!\*)\*([^*]+?)\*(?!\*)")
_INLINE_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_INLINE_CODE = re.compile(r"`([^`]+)`")


def _is_block_start(line: str, lines: list[str], idx: int) -> bool:
    s = line.strip()
    if s.startswith(("# ", "## ", "### ", "#### ", "- ", "* ", "+ ", "> ")):
        return True
    if re.match(r"^\s*\d+\.\s+", line):
        return True
    if s in ("---", "***", "___"):
        return True
    if (
        _TABLE_LINE.match(line)
        and idx + 1 < len(lines)
        and _TABLE_SEP.match(lines[idx + 1])
    ):
        return True
    return False


def _render_markdown_block(pdf, md: str, top_h1: bool) -> None:
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()

        if not s:
            pdf.ln(2)
            i += 1
            continue

        if s.startswith("# ") and top_h1:
            pdf.set_text_color(*INK)
            pdf.set_font(_FONT_FAMILY, "B", 18)
            pdf.cell(0, 9, _ascii_fallback(s[2:].strip()), new_x=XPos_LMARGIN(), new_y=YPos_NEXT())
            pdf.set_draw_color(*INK)
            pdf.set_line_width(0.6)
            pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
            pdf.ln(4)
            i += 1
            continue

        if s.startswith("## "):
            pdf.ln(3)
            pdf.set_text_color(*INK)
            pdf.set_font(_FONT_FAMILY, "B", 14)
            _multiline_text(pdf, s[3:].strip(), line_h=7, size=14)
            pdf.set_draw_color(*INK)
            pdf.set_line_width(0.4)
            pdf.line(pdf.l_margin, pdf.get_y() + 0.5, pdf.w - pdf.r_margin, pdf.get_y() + 0.5)
            pdf.ln(3)
            i += 1
            continue

        if s.startswith("### "):
            pdf.ln(3)
            pdf.set_text_color(*INK)
            _multiline_text(pdf, s[4:].strip(), line_h=6, size=12)
            pdf.ln(1)
            i += 1
            continue

        if s.startswith("#### "):
            pdf.set_text_color(*INK)
            _multiline_text(pdf, s[5:].strip(), line_h=5.5, size=11)
            i += 1
            continue

        if s in ("---", "***", "___"):
            pdf.ln(2)
            pdf.set_draw_color(*RULE_FAINT)
            pdf.set_line_width(0.2)
            pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
            pdf.ln(4)
            i += 1
            continue

        if _TABLE_LINE.match(line) and i + 1 < len(lines) and _TABLE_SEP.match(lines[i + 1]):
            j = i
            while j < len(lines) and (_TABLE_LINE.match(lines[j]) or _TABLE_SEP.match(lines[j])):
                j += 1
            _render_table(pdf, lines[i:j])
            i = j
            continue

        if re.match(r"^\s*[-*+]\s+", line):
            j = i
            while j < len(lines) and (
                re.match(r"^\s*[-*+]\s+", lines[j])
                or (lines[j].startswith("  ") and lines[j].strip())
            ):
                j += 1
            _render_bullets(pdf, lines[i:j])
            i = j
            continue

        if re.match(r"^\s*\d+\.\s+", line):
            j = i
            while j < len(lines) and (
                re.match(r"^\s*\d+\.\s+", lines[j])
                or (lines[j].startswith("  ") and lines[j].strip())
            ):
                j += 1
            _render_ordered(pdf, lines[i:j])
            i = j
            continue

        if s.startswith("> "):
            _render_blockquote(pdf, s[2:])
            i += 1
            continue

        para_lines = [line]
        j = i + 1
        while j < len(lines) and lines[j].strip() and not _is_block_start(lines[j], lines, j):
            para_lines.append(lines[j])
            j += 1
        _render_paragraph(pdf, " ".join(p.strip() for p in para_lines))
        i = j


def _render_paragraph(pdf, text: str) -> None:
    pdf.set_text_color(*INK)
    pdf.set_font(_FONT_FAMILY, "", 10)
    _emit_inline_runs(pdf, text, line_height=5)
    pdf.ln(2)


def _render_blockquote(pdf, text: str) -> None:
    x0 = pdf.l_margin
    pdf.set_x(x0 + 3)
    pdf.set_text_color(63, 63, 92)
    pdf.set_font(_FONT_FAMILY, "I", 10)
    _emit_inline_runs(pdf, text, line_height=5, indent=3)
    pdf.set_x(x0)
    pdf.set_draw_color(*RULE)
    pdf.set_line_width(0.5)
    pdf.ln(1)


def _render_bullets(pdf, lines: list[str]) -> None:
    pdf.set_text_color(*INK)
    pdf.set_font(_FONT_FAMILY, "", 10)
    for line in lines:
        m = re.match(r"^(\s*)[-*+]\s+(.*)$", line)
        if not m:
            continue
        depth = (len(m.group(1)) // 2)
        bullet_x = pdf.l_margin + depth * 4
        text = m.group(2)
        pdf.set_x(bullet_x)
        pdf.cell(3, 5, _ascii_fallback("•"))
        pdf.set_x(bullet_x + 4)
        _emit_inline_runs(pdf, text, line_height=5, indent=bullet_x + 4 - pdf.l_margin)
    pdf.ln(1)


def _render_ordered(pdf, lines: list[str]) -> None:
    pdf.set_text_color(*INK)
    pdf.set_font(_FONT_FAMILY, "", 10)
    n = 1
    for line in lines:
        m = re.match(r"^\s*(\d+)\.\s+(.*)$", line)
        if not m:
            continue
        text = m.group(2)
        pdf.set_x(pdf.l_margin)
        pdf.cell(7, 5, f"{n}.")
        pdf.set_x(pdf.l_margin + 7)
        _emit_inline_runs(pdf, text, line_height=5, indent=7)
        n += 1
    pdf.ln(1)


# ---------- inline-span renderer ----------


def _emit_inline_runs(pdf, text: str, line_height: float, indent: float = 0.0) -> None:
    runs = _tokenize_inline(text)
    line_w = pdf.w - pdf.r_margin - pdf.l_margin - indent
    x_left = pdf.l_margin + indent
    pdf.set_x(x_left)
    cur_x = x_left
    for run in runs:
        s, style, color, link = run
        s = _ascii_fallback(s)
        # Capture leading + trailing whitespace per word so the space between
        # a bold run's closing `**` and the next word is preserved. The earlier
        # pattern `\S+\s*` discarded leading whitespace on a run, which made
        # "**PRAME IHC** to confirm" render as "PRAME IHCto confirm".
        words = re.findall(r"\s*\S+\s*", s)
        for word in words:
            pdf.set_font(_FONT_FAMILY, style, 10)
            pdf.set_text_color(*color)
            w = pdf.get_string_width(word)
            if cur_x + w > pdf.l_margin + indent + line_w + 0.01:
                pdf.ln(line_height)
                cur_x = x_left
                pdf.set_x(cur_x)
                if word.startswith(" "):
                    word = word.lstrip(" ")
                    w = pdf.get_string_width(word)
            pdf.cell(w, line_height, word, link=link or "")
            cur_x += w
    pdf.ln(line_height)


def _tokenize_inline(text: str) -> list[tuple[str, str, tuple, str]]:
    parts: list[tuple[str, bool]] = []
    last = 0
    for m in _INLINE_CODE.finditer(text):
        if m.start() > last:
            parts.append((text[last : m.start()], False))
        parts.append((m.group(1), True))
        last = m.end()
    if last < len(text):
        parts.append((text[last:], False))

    runs: list[tuple[str, str, tuple, str]] = []
    for part_text, is_code in parts:
        if is_code:
            runs.append((part_text, "", INK_MUTED, ""))
            continue
        runs.extend(_tokenize_links(part_text))
    return runs


def _tokenize_links(text: str) -> list[tuple[str, str, tuple, str]]:
    runs: list[tuple[str, str, tuple, str]] = []
    last = 0
    for m in _INLINE_LINK.finditer(text):
        if m.start() > last:
            runs.extend(_tokenize_emph(text[last : m.start()], link=""))
        runs.extend(_tokenize_emph(m.group(1), link=m.group(2), is_link=True))
        last = m.end()
    if last < len(text):
        runs.extend(_tokenize_emph(text[last:], link=""))
    return runs


def _tokenize_emph(text: str, link: str = "", is_link: bool = False) -> list[tuple[str, str, tuple, str]]:
    color = ACCENT if is_link else INK
    runs: list[tuple[str, str, tuple, str]] = []
    last = 0
    for m in _INLINE_BOLD.finditer(text):
        if m.start() > last:
            runs.extend(_tokenize_italic(text[last : m.start()], color, link))
        runs.append((m.group(1), "B", color, link))
        last = m.end()
    if last < len(text):
        runs.extend(_tokenize_italic(text[last:], color, link))
    return runs


def _tokenize_italic(text: str, color: tuple, link: str) -> list[tuple[str, str, tuple, str]]:
    runs: list[tuple[str, str, tuple, str]] = []
    last = 0
    for m in _INLINE_ITALIC.finditer(text):
        if m.start() > last:
            runs.append((text[last : m.start()], "", color, link))
        runs.append((m.group(1), "I", color, link))
        last = m.end()
    if last < len(text):
        runs.append((text[last:], "", color, link))
    return runs


# ---------- table renderer ----------


def _render_table(pdf, lines: list[str]) -> None:
    rows: list[list[str]] = []
    for line in lines:
        s = line.strip().strip("|")
        if _TABLE_SEP.match(line):
            continue
        cells = [c.strip() for c in re.split(r"\s*\|\s*", s)]
        rows.append(cells)
    if not rows:
        return

    n_cols = len(rows[0])
    page_w = pdf.w - pdf.l_margin - pdf.r_margin
    headers = [h.lower() for h in rows[0]]
    widths = _column_widths(headers, page_w, n_cols)

    pdf.ln(2)
    pdf.set_fill_color(*HEADER_BG)
    pdf.set_draw_color(*INK)
    pdf.set_line_width(0.4)
    pdf.set_text_color(*INK)
    pdf.set_font(_FONT_FAMILY, "B", 8)
    _render_table_row(pdf, rows[0], widths, fill=True, header=True)

    pdf.set_font(_FONT_FAMILY, "", 8)
    pdf.set_text_color(*INK)
    for ri, row in enumerate(rows[1:]):
        if len(row) < n_cols:
            row = row + [""] * (n_cols - len(row))
        elif len(row) > n_cols:
            row = row[:n_cols]
        zebra = ri % 2 == 1
        _render_table_row(pdf, row, widths, fill=zebra, header=False)
    pdf.ln(2)


def _column_widths(headers: list[str], page_w: float, n: int) -> list[float]:
    if n == 13 and any("toxicit" in h for h in headers):
        # Manuscripts master table: Report | Reference | Type | Inclusion | Intervention | Indication | Design | n | Effect | Variance | Toxicities | Case fit | Notes
        ratios = [0.07, 0.06, 0.05, 0.07, 0.07, 0.09, 0.07, 0.03, 0.08, 0.08, 0.16, 0.05, 0.12]
    elif n == 4 and any("rationale" in h or "notes" in h for h in headers):
        ratios = [0.15, 0.20, 0.25, 0.40]
    elif n == 5:
        ratios = [0.06, 0.18, 0.28, 0.20, 0.28]
    elif n == 6:
        ratios = [0.06, 0.16, 0.22, 0.16, 0.16, 0.24]
    else:
        ratios = [1.0 / n] * n
    return [page_w * r for r in ratios]


_RX_SINGLE_LINK_CELL = re.compile(r"^\s*\[([^\]]+)\]\(([^)]+)\)\s*$")


def _cell_link(cell: str) -> str:
    """Return the URL when a cell is a single markdown link `[label](url)`.

    Used by the table renderer to attach a clickable hyperlink to the rendered
    cell. When the cell is plain text or contains mixed content, returns ''.
    The Reference column on the manuscripts master table is always a single
    link or `—`, so this catches every case there.
    """
    m = _RX_SINGLE_LINK_CELL.match(cell)
    return m.group(2) if m else ""


def _is_bold_cell(cell: str) -> tuple[bool, str]:
    """Detect a cell whose entire content is wrapped in `**...**`.

    Returns (is_bold, inner). When the cell starts and ends with `**`, the
    outer wrapper is stripped and the inner content is returned (italic /
    link / code markdown inside the inner is preserved). Otherwise the cell
    is returned unchanged. Used by the table renderer to honor cell-level
    bold (the convention reporter uses for preferred-provider rows in
    `target_validation_report.md`).
    """
    s = cell.strip()
    if len(s) >= 4 and s.startswith("**") and s.endswith("**"):
        return True, s[2:-2]
    return False, cell


def _render_table_row(pdf, cells: list[str], widths: list[float], fill: bool, header: bool) -> None:
    line_h = 4.2 if not header else 4.6
    pad_v = 1.2
    cell_lines: list[list[str]] = []
    cell_links: list[str] = []
    cell_bolds: list[bool] = []
    for cell, w in zip(cells, widths):
        is_bold, inner_cell = _is_bold_cell(cell)
        plain = _strip_inline_md(inner_cell)
        eff_style = "B" if (header or is_bold) else ""
        wrapped = _word_wrap(_ascii_fallback(plain), w - 2.4, pdf, font_style=eff_style)
        cell_lines.append(wrapped)
        cell_links.append("" if header else _cell_link(inner_cell if is_bold else cell))
        cell_bolds.append(is_bold)
    n_lines = max(1, max(len(c) for c in cell_lines))
    row_h = max(line_h * n_lines + pad_v * 2, 6)

    if pdf.get_y() + row_h > pdf.h - pdf.b_margin:
        pdf.add_page()

    x0 = pdf.l_margin
    y0 = pdf.get_y()
    if fill:
        bg = HEADER_BG if header else ROW_ALT
        pdf.set_fill_color(*bg)
        pdf.rect(x0, y0, sum(widths), row_h, style="F")

    pdf.set_draw_color(*RULE_FAINT if not header else INK)
    pdf.set_line_width(0.5 if header else 0.2)
    pdf.line(x0, y0 + row_h, x0 + sum(widths), y0 + row_h)
    if header:
        pdf.set_line_width(0.5)
        pdf.line(x0, y0, x0 + sum(widths), y0)

    cx = x0
    for cell, w, lines, link, is_bold in zip(cells, widths, cell_lines, cell_links, cell_bolds):
        cy = y0 + pad_v
        for ln in lines:
            pdf.set_xy(cx + 1.2, cy)
            _emit_table_cell_line(pdf, ln, w - 2.4, header, cell_link=link, force_bold=is_bold)
            cy += line_h
        cx += w

    pdf.set_xy(x0, y0 + row_h)


def _emit_table_cell_line(pdf, text: str, w: float, header: bool, cell_link: str = "", force_bold: bool = False) -> None:
    pdf.set_text_color(*INK)
    if cell_link and not header:
        # The whole cell is one hyperlinked run — `_render_table_row` already
        # stripped the markdown so `text` is the visible label. Render it as
        # ACCENT-colored clickable text with the URL attached.
        ascii_text = _ascii_fallback(text)
        pdf.set_font(_FONT_FAMILY, "B" if force_bold else "", 8)
        pdf.set_text_color(*ACCENT)
        ww = pdf.get_string_width(ascii_text)
        if ww > w + 0.01:
            ww = w
        pdf.cell(ww, 4.2, ascii_text, link=cell_link)
        return
    runs = _tokenize_inline(text)
    cur_x = pdf.get_x()
    y = pdf.get_y()
    for run_text, style, color, link in runs:
        eff_style = style
        if force_bold and not header and "B" not in eff_style:
            eff_style = ("B" + eff_style) if eff_style else "B"
        pdf.set_font(_FONT_FAMILY, eff_style if not header else "B", 8)
        run_color = color if not header else INK
        pdf.set_text_color(*run_color)
        pdf.set_xy(cur_x, y)
        ww = pdf.get_string_width(_ascii_fallback(run_text))
        if cur_x + ww > pdf.get_x() + w + 0.01:
            break
        pdf.cell(ww, 4.2, _ascii_fallback(run_text), link=link or "")
        cur_x += ww


def _strip_inline_md(text: str) -> str:
    text = _INLINE_LINK.sub(r"\1", text)
    text = _INLINE_BOLD.sub(r"\1", text)
    text = _INLINE_ITALIC.sub(r"\1", text)
    text = _INLINE_CODE.sub(r"\1", text)
    return text


def _word_wrap(text: str, width: float, pdf, font_style: str = "", size: int = 8) -> list[str]:
    pdf.set_font(_FONT_FAMILY, font_style, size)
    words = text.split()
    if not words:
        return [""]
    lines: list[str] = []
    current = words[0]
    for w in words[1:]:
        candidate = current + " " + w
        if pdf.get_string_width(candidate) <= width:
            current = candidate
        else:
            lines.append(current)
            current = w
    lines.append(current)
    return lines


def _multiline_text(pdf, text: str, line_h: float, size: int = 16) -> None:
    width = pdf.w - pdf.r_margin - pdf.l_margin
    lines = _word_wrap(_ascii_fallback(text), width, pdf, font_style="B", size=size)
    pdf.set_font(_FONT_FAMILY, "B", size)
    for ln in lines:
        pdf.cell(0, line_h, ln, new_x=XPos_LMARGIN(), new_y=YPos_NEXT())


# ---------- cover ----------


_DISCLAIMER_CLINICIAN = (
    "Libby is an experimental decision-support tool. The recommendations in this "
    "report have not been reviewed by a clinician treating this patient. Do not "
    "act on this report without consulting a qualified oncologist."
)
_DISCLAIMER_PATIENT = (
    "This is decision-support information, not a treatment plan. Please share it "
    "with your oncologist before making any decisions based on what's here."
)


def _render_cover(pdf, title: str, subtitle: str, today: str, eyebrow: str, bg: tuple, disclaimer: str) -> None:
    pdf.add_page()
    pdf.set_fill_color(*bg)
    pdf.rect(0, 0, pdf.w, pdf.h, style="F")

    pdf.set_y(40)
    pdf.set_x(20)
    pdf.set_text_color(*ACCENT)
    pdf.set_font(_FONT_FAMILY, "B", 10)
    pdf.cell(0, 6, _ascii_fallback(eyebrow))

    pdf.set_y(58)
    pdf.set_x(20)
    pdf.set_text_color(*INK)
    pdf.set_font(_FONT_FAMILY, "B", 26)
    pdf.multi_cell(w=pdf.w - 40, h=11, text=_ascii_fallback(title), align="L")

    if subtitle:
        pdf.ln(6)
        pdf.set_x(20)
        pdf.set_font(_FONT_FAMILY, "I", 12)
        pdf.set_text_color(63, 63, 92)
        pdf.multi_cell(w=pdf.w - 40, h=6, text=_ascii_fallback(subtitle), align="L")

    pdf.set_y(pdf.h - 50)
    pdf.set_x(20)
    pdf.set_text_color(*INK_MUTED)
    pdf.set_font(_FONT_FAMILY, "", 10)
    pdf.cell(0, 5, f"Generated {today}")

    pdf.set_y(pdf.h - 32)
    pdf.set_x(20)
    pdf.set_draw_color(*RULE)
    pdf.set_line_width(0.2)
    pdf.line(20, pdf.h - 33, pdf.w - 20, pdf.h - 33)
    pdf.ln(2)
    pdf.set_x(20)
    pdf.set_text_color(*INK_MUTED)
    pdf.set_font(_FONT_FAMILY, "I", 8)
    pdf.multi_cell(w=pdf.w - 40, h=4, text=_ascii_fallback(disclaimer))


# ---------- PDF entry points ----------


def _make_clinician_pdf(slug: str, exec_md: str, body_md: str, sources_md: str, out_path: Path) -> None:
    try:
        from fpdf import FPDF
    except ImportError as e:
        raise SystemExit(
            "build_report: missing dependency `fpdf2`.\n  pip install fpdf2"
        ) from e

    today = datetime.now(timezone.utc).date().isoformat()
    title = slug

    class ReportPDF(FPDF):
        def footer(self_):
            if self_.page_no() <= 1:
                return
            self_.set_y(-12)
            self_.set_font(_FONT_FAMILY, "I", 8)
            self_.set_text_color(*INK_MUTED)
            self_.cell(
                0,
                6,
                _ascii_fallback(
                    f"{self_.page_no()} of {{nb}}    ·    Libby case    ·    {slug}"
                ),
                align="C",
            )

    pdf = ReportPDF(orientation="P", unit="mm", format="Letter")
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(left=18, top=20, right=18)
    pdf.alias_nb_pages()
    _register_unicode_font(pdf)

    _render_cover(
        pdf, title, "Multi-agent decision support — clinician track",
        today, "LIBBY CASE REPORT", COVER_BG, _DISCLAIMER_CLINICIAN,
    )

    if exec_md.strip():
        pdf.add_page()
        _render_markdown_block(pdf, exec_md, top_h1=True)

    if body_md.strip():
        pdf.add_page()
        _render_markdown_block(pdf, body_md, top_h1=False)

    if sources_md.strip():
        pdf.add_page()
        _render_markdown_block(pdf, sources_md, top_h1=False)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(out_path))


def _pipe_escape(s: str) -> str:
    return s.replace("|", "\\|").replace("\n", " ").strip()


def _tox_for_pdf(t: dict) -> str:
    term = t.get("term") or "?"
    grade = t.get("grade")
    n_events = t.get("n_events")
    denom = t.get("denominator")
    rate = t.get("rate_pct")
    head = term + (f" G{grade}" if grade and grade != "any" else "")
    rate_parts: list[str] = []
    if n_events is not None and denom is not None:
        rate_parts.append(f"{n_events}/{denom}")
    elif denom is not None:
        rate_parts.append(f"n={denom}")
    if rate is not None:
        try:
            r = float(rate)
            rate_parts.append(f"{r:g}%")
        except (TypeError, ValueError):
            rate_parts.append(f"{rate}%")
    if rate_parts:
        return f"{head} ({', '.join(rate_parts)})"
    return head


def _reference_for_pdf(r: dict) -> str:
    """Return a clickable markdown link for the manuscript's canonical reference.

    The PDF table cell renderer tokenizes `[label](url)` into a run that emits
    `pdf.cell(..., link=url)`, so the rendered cell is a hyperlink the reader
    can click. PubMed > DOI > ClinicalTrials.gov, mirroring the web table's
    reference_cell precedence.
    """
    pmid = r.get("pmid")
    if pmid:
        return f"[PMID {pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid})"
    doi = r.get("doi")
    if doi:
        return f"[doi:{doi}](https://doi.org/{doi})"
    nct = r.get("nct_id") or r.get("evidence_id") or ""
    if str(nct).upper().startswith("NCT"):
        return f"[{nct}](https://clinicaltrials.gov/study/{nct})"
    return "—"


def _notes_for_pdf(r: dict, excluded: bool, kind: str) -> str:
    bits: list[str] = []
    if excluded:
        reason = r.get("exclusion_reason")
        if reason:
            bits.append(f"Excluded: {reason}")
    authored = r.get("notes") or r.get("caveats")
    if authored:
        bits.append(str(authored))
    if not excluded:
        gaps: list[str] = []
        if kind == "trial" and not r.get("pmid"):
            gaps.append("registration only — no peer-reviewed publication yet")
        if r.get("indication") and not r.get("toxicities") and not r.get("safety_summary") and kind != "preclinical":
            gaps.append("toxicity table not extracted")
        if r.get("indication") and r.get("effect_size") in (None, "") and kind != "preclinical":
            gaps.append("primary endpoint not extracted")
        if gaps:
            bits.append("(" + "; ".join(gaps) + ")")
    return " — ".join(bits) if bits else "—"


def _row_for_pdf(r: dict, kind: str) -> list[str]:
    """Return the 13 cells (in PDF COLS order) for one manuscript row, plain text.

    Order: Report, Reference, Type, Inclusion, Intervention, Indication, Design,
    n, Effect, Variance, Toxicities, Case fit, Notes.
    """
    first = r.get("first_author") or "—"
    last = r.get("last_author") or "—"
    yr = r.get("year") or "—"
    journal = r.get("journal") or ""
    report = f"{first}/{last} ({yr})"
    if journal:
        report = f"{report} — {journal}"

    reference = _reference_for_pdf(r)

    inclusion_status = (r.get("inclusion_status") or "included")
    if inclusion_status == "considered_excluded":
        inclusion_str = f"excluded — {r.get('exclusion_reason') or '?'}"
    else:
        inclusion_str = "included"
    excluded = inclusion_status == "considered_excluded"

    if kind == "clinical" or kind == "trial":
        intervention = r.get("intervention_label") or "—"
        ind = r.get("indication") or "—"
        line = r.get("line_of_therapy")
        pop = r.get("population_detail")
        ind_full = ind + (f" ({line})" if line else "")
        if pop:
            ind_full += f"; {pop}"
        design = r.get("design") or "—"
        n_str = str(r.get("n")) if r.get("n") not in (None, "") else "—"

        if excluded:
            effect = "—"
            variance = "—"
            tox_str = "—"
        else:
            e = r.get("effect_size")
            units = r.get("effect_units") or ""
            if e is None or e == "":
                effect = "—"
            else:
                effect = f"{e} {units}".strip()
            outcome = r.get("outcome")
            if outcome:
                effect = f"{effect} — {outcome}"

            var_parts: list[str] = []
            lo, hi = r.get("ci_lower"), r.get("ci_upper")
            if lo is not None and hi is not None:
                var_parts.append(f"95% CI {lo}–{hi}")
            free = r.get("variance_or_ci")
            if free:
                var_parts.append(str(free))
            p = r.get("p_value")
            if p not in (None, "", "—"):
                var_parts.append(f"p={p}")
            variance = "; ".join(var_parts) if var_parts else "—"

            tox = r.get("toxicities") or []
            if tox:
                tox_str = "; ".join(_tox_for_pdf(t) for t in tox)
            else:
                tox_str = r.get("safety_summary") or "—"

        fit = r.get("case_match") or "—"
    else:  # preclinical
        intervention = r.get("intervention_label") or "—"
        ind_full = r.get("model_system") or "—"
        design = r.get("mechanism") or "—"
        n_str = r.get("n_units") or "—"
        if excluded:
            effect = "—"
            variance = "—"
        else:
            qual = r.get("effect_size_qual") or ""
            finding = r.get("key_finding") or ""
            effect = (f"{qual} — {finding}" if qual and finding else (qual or finding)) or "—"
            var_parts = []
            if r.get("control_arm"):
                var_parts.append(f"vs {r['control_arm']}")
            if r.get("translatability_score"):
                var_parts.append(f"translatability: {r['translatability_score']}")
            variance = "; ".join(var_parts) if var_parts else "—"
        tox_str = "n/a (preclinical)"
        fit = r.get("case_match") or "—"

    notes_str = _notes_for_pdf(r, excluded, kind)
    return [
        report,
        reference,
        kind,
        inclusion_str,
        intervention,
        ind_full,
        design,
        n_str,
        effect,
        variance,
        tox_str,
        fit,
        notes_str,
    ]


def _trial_to_synthetic_for_pdf(t: dict) -> dict:
    return {
        "case_slug": t.get("case_slug"),
        "intervention_label": t.get("intervention") or "—",
        "indication": t.get("indication") or "—",
        "line_of_therapy": t.get("line"),
        "population_detail": t.get("biomarker") or "",
        "design": t.get("design") or t.get("phase") or "—",
        "n": t.get("n"),
        "first_author": t.get("first_author"),
        "last_author": t.get("last_author"),
        "year": t.get("year"),
        "journal": t.get("journal") or ("ClinicalTrials.gov registration" if not t.get("pmid") else ""),
        "outcome": t.get("endpoint") or "",
        "effect_size": t.get("effect_size"),
        "ci_lower": t.get("ci_lower"),
        "ci_upper": t.get("ci_upper"),
        "p_value": t.get("p_value"),
        "case_match": t.get("fit_to_case"),
        "pmid": t.get("pmid"),
    }


def _manuscripts_md_for_pdf(slug: str, clinical: list[dict], preclinical: list[dict], trials: list[dict]) -> str:
    headers = [
        "Report", "Reference", "Type", "Inclusion", "Intervention", "Indication / model",
        "Design", "n", "Effect size", "Variance",
        "Toxicities (type, n/N, rate)", "Case fit", "Notes",
    ]
    seen_pmids: set[str] = {str(r.get("pmid")) for r in clinical + preclinical if r.get("pmid")}
    extra_trials = [_trial_to_synthetic_for_pdf(t) for t in trials
                    if not (t.get("pmid") and str(t["pmid"]) in seen_pmids)]
    n_clin_inc = sum(1 for r in clinical if (r.get("inclusion_status") or "included") == "included")
    n_clin_exc = len(clinical) - n_clin_inc
    n_prec_inc = sum(1 for r in preclinical if (r.get("inclusion_status") or "included") == "included")
    n_prec_exc = len(preclinical) - n_prec_inc

    lines = [
        f"# Manuscripts considered — {slug}",
        "",
        f"Master inventory: {len(clinical)} clinical ({n_clin_inc} included, "
        f"{n_clin_exc} considered & excluded) + {len(preclinical)} pre-clinical "
        f"({n_prec_inc} included, {n_prec_exc} considered & excluded) + "
        f"{len(extra_trials)} additional trial publications/registrations. "
        "One row per manuscript, sorted by year (newest first). Excluded rows are "
        "papers a Libby agent reviewed and chose NOT to feed to the board, with the "
        "exclusion reason captured.",
        "",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    triples = (
        [(r, "clinical") for r in clinical]
        + [(r, "preclinical") for r in preclinical]
        + [(r, "trial") for r in extra_trials]
    )
    triples.sort(key=lambda pair: -(pair[0].get("year") or 0))
    for r, kind in triples:
        cells = _row_for_pdf(r, kind)
        lines.append("| " + " | ".join(_pipe_escape(c) for c in cells) + " |")
    lines.append("")
    return "\n".join(lines)


def _make_manuscripts_pdf(slug: str, clinical: list[dict], preclinical: list[dict], trials: list[dict], out_path: Path) -> None:
    try:
        from fpdf import FPDF
    except ImportError as e:
        raise SystemExit(
            "build_report: missing dependency `fpdf2`.\n  pip install fpdf2"
        ) from e

    today = datetime.now(timezone.utc).date().isoformat()

    class ManuscriptsPDF(FPDF):
        def footer(self_):
            if self_.page_no() <= 1:
                return
            self_.set_y(-12)
            self_.set_font(_FONT_FAMILY, "I", 8)
            self_.set_text_color(*INK_MUTED)
            self_.cell(
                0,
                6,
                _ascii_fallback(
                    f"{self_.page_no()} of {{nb}}    ·    Libby — manuscripts inventory    ·    {slug}"
                ),
                align="C",
            )

    pdf = ManuscriptsPDF(orientation="L", unit="mm", format="Letter")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_margins(left=12, top=14, right=12)
    pdf.alias_nb_pages()
    _register_unicode_font(pdf)

    _render_cover(
        pdf, f"Manuscripts considered — {slug}",
        "Master inventory: every paper reviewed in this case",
        today, "LIBBY — MANUSCRIPTS INVENTORY",
        COVER_BG, _DISCLAIMER_CLINICIAN,
    )

    pdf.add_page()
    body_md = _manuscripts_md_for_pdf(slug, clinical, preclinical, trials)
    _render_markdown_block(pdf, body_md, top_h1=True)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(out_path))


def _make_target_validation_pdf(slug: str, body_md: str, out_path: Path) -> None:
    """Render data/cases/<slug>/target_validation_report.md → PDF.

    Portrait, single small disclaimer cover, then the report's prose body. The
    report itself is reporter-authored and short (~200-300 words), so a one-
    or two-page PDF is the expected shape.
    """
    try:
        from fpdf import FPDF
    except ImportError as e:
        raise SystemExit(
            "build_report: missing dependency `fpdf2`.\n  pip install fpdf2"
        ) from e

    today = datetime.now(timezone.utc).date().isoformat()

    class TargetValidationPDF(FPDF):
        def footer(self_):
            if self_.page_no() <= 1:
                return
            self_.set_y(-12)
            self_.set_font(_FONT_FAMILY, "I", 8)
            self_.set_text_color(*INK_MUTED)
            self_.cell(
                0,
                6,
                _ascii_fallback(
                    f"{self_.page_no()} of {{nb}}    ·    Libby — target validation paths    ·    {slug}"
                ),
                align="C",
            )

    pdf = TargetValidationPDF(orientation="P", unit="mm", format="Letter")
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(left=18, top=20, right=18)
    pdf.alias_nb_pages()
    _register_unicode_font(pdf)

    _render_cover(
        pdf, f"Target validation paths — {slug}",
        "The diagnostic and biomarker workup that hardens the targetable-feature call",
        today, "LIBBY — TARGET VALIDATION PATHS",
        COVER_BG, _DISCLAIMER_CLINICIAN,
    )

    pdf.add_page()
    _render_markdown_block(pdf, body_md, top_h1=False)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(out_path))


def _accessibility_md_for_pdf(slug: str, rows: list[dict]) -> str:
    """Convert accessibility.jsonl rows into a markdown body the PDF renderer can consume.

    Mirrors the on-page web layout (build_accessibility.py) but uses pipe tables
    and headings the existing markdown subset supports. No HTML.
    """
    if not rows:
        return f"# Access guide — {slug}\n\n_No accessibility rows yet._\n"

    status_label = {
        "standard_of_care": "Standard of care",
        "off_label_use": "Off-label use",
        "clinical_trial_only": "Clinical trial",
        "compassionate_use": "Compassionate use",
        "expanded_access_program": "Expanded access program",
        "not_yet_accessible": "Not yet accessible",
        "unavailable": "Unavailable",
    }
    status_order = list(status_label.keys())

    def _normalize(raw):
        if isinstance(raw, list):
            return [s for s in raw if s]
        if isinstance(raw, str) and raw:
            return [raw]
        return []

    def _primary(statuses: list[str]) -> str:
        for s in status_order:
            if s in statuses:
                return s
        return "unavailable"

    def _statuses_str(statuses: list[str]) -> str:
        ordered = [s for s in status_order if s in statuses]
        return " + ".join(status_label.get(s, s) for s in ordered) or "—"

    for r in rows:
        r["_statuses"] = _normalize(r.get("access_status"))
        r["_primary"] = _primary(r["_statuses"])

    by_status: dict[str, list[dict]] = {}
    for r in rows:
        by_status.setdefault(r["_primary"], []).append(r)
    for s in by_status:
        by_status[s].sort(key=lambda x: x.get("intervention_label") or "")

    # Numbered ordering shared between the summary table and the per-intervention
    # deep sections — mirrors the web page so the printed report's numbers match.
    numbered: list[tuple[int, str, dict]] = []
    n = 1
    for status in status_order:
        for r in by_status.get(status, []):
            numbered.append((n, status, r))
            n += 1
    by_status_numbered: dict[str, list[tuple[int, dict]]] = {}
    for num, status, r in numbered:
        by_status_numbered.setdefault(status, []).append((num, r))

    lines: list[str] = [
        f"# Access guide — {slug}",
        "",
        "How a patient or treating team could practically access each intervention "
        "in this case's dossier. Trial recruitment contacts and manufacturer "
        "medical-information lines are captured for direct outreach. The number in "
        "the first column of the summary table is the entry's identifier in the "
        "per-intervention sections below — use it to find the deep section "
        "quickly. Information ages — each row carries a `Verified` date; re-screen "
        "before relying on a specific contact or trial slot.",
        "",
        "## Summary",
        "",
        "| # | Intervention | Modality | Access status | Regulatory | Recommended first action |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for num, status, r in numbered:
        first_step = (r.get("next_steps") or ["—"])[0]
        lines.append(
            f"| {num} "
            f"| {r.get('intervention_label') or '—'} "
            f"| {r.get('modality') or '—'} "
            f"| {_statuses_str(r['_statuses'])} "
            f"| {r.get('regulatory_status') or '—'} "
            f"| {first_step} |"
        )
    lines.append("")

    for s in status_order:
        group = by_status_numbered.get(s, [])
        if not group:
            continue
        lines.append(f"## {status_label.get(s, s)} ({len(group)})")
        lines.append("")
        for num, r in group:
            label = r.get("intervention_label") or r.get("intervention_id") or "?"
            lines.append(f"### {num}. {label}")
            lines.append("")
            aliases = r.get("aliases") or []
            if aliases:
                lines.append(f"_Aliases:_ {', '.join(aliases)}")
                lines.append("")
            meta_bits = []
            if r.get("modality"):
                meta_bits.append(f"**Modality:** {r['modality']}")
            if r.get("regulatory_status"):
                meta_bits.append(f"**Regulatory:** {r['regulatory_status']}")
            if r.get("guideline_status"):
                meta_bits.append(f"**Guidelines:** {r['guideline_status']}")
            if r.get("geographic_scope"):
                meta_bits.append(f"**Geographic scope:** {r['geographic_scope']}")
            if r.get("last_verified_utc"):
                meta_bits.append(f"**Verified:** {r['last_verified_utc']}")
            if meta_bits:
                lines.append("  ·  ".join(meta_bits))
                lines.append("")
            if r.get("access_summary"):
                lines.append(r["access_summary"])
                lines.append("")
            if r.get("next_steps"):
                lines.append("**Next steps**")
                lines.append("")
                for i, step in enumerate(r["next_steps"], 1):
                    lines.append(f"{i}. {step}")
                lines.append("")
            trials = r.get("trials") or []
            if trials:
                lines.append("**Trial pathways**")
                lines.append("")
                lines.append("| NCT | Phase | Status | Eligible | Central contact |")
                lines.append("| --- | --- | --- | --- | --- |")
                for t in trials:
                    contact_bits = []
                    if t.get("central_contact_name"):
                        contact_bits.append(t["central_contact_name"])
                    if t.get("central_contact_email"):
                        contact_bits.append(t["central_contact_email"])
                    if t.get("central_contact_phone"):
                        contact_bits.append(t["central_contact_phone"])
                    contact = "; ".join(contact_bits) or "—"
                    lines.append(
                        f"| [{t.get('nct_id') or '—'}](https://clinicaltrials.gov/study/{t.get('nct_id') or ''}) "
                        f"| {t.get('phase') or '—'} "
                        f"| {t.get('recruitment_status') or '—'} "
                        f"| {t.get('patient_eligible') or '—'} "
                        f"| {contact} |"
                    )
                lines.append("")
            m = r.get("manufacturer") or {}
            if m:
                lines.append("**Manufacturer / sponsor contact**")
                lines.append("")
                man_bits = []
                if m.get("company"):
                    man_bits.append(f"**Company:** {m['company']}")
                if m.get("medical_information_phone"):
                    man_bits.append(f"**Med info phone:** `{m['medical_information_phone']}`")
                if m.get("medical_information_email"):
                    man_bits.append(f"**Med info email:** [{m['medical_information_email']}](mailto:{m['medical_information_email']})")
                if m.get("product_information_url"):
                    man_bits.append(f"**Product info:** [{m['product_information_url']}]({m['product_information_url']})")
                if m.get("compassionate_use_url"):
                    man_bits.append(f"**Compassionate / expanded access:** [{m['compassionate_use_url']}]({m['compassionate_use_url']})")
                if m.get("compassionate_use_email"):
                    man_bits.append(f"**Compassionate use email:** [{m['compassionate_use_email']}](mailto:{m['compassionate_use_email']})")
                for b in man_bits:
                    lines.append(f"- {b}")
                if m.get("notes"):
                    lines.append(f"- **Notes:** {m['notes']}")
                lines.append("")
            if r.get("payer_access_notes"):
                lines.append(f"**Payer / coverage:** {r['payer_access_notes']}")
                lines.append("")
            if r.get("notes"):
                lines.append(f"**Notes:** {r['notes']}")
                lines.append("")
            lines.append("---")
            lines.append("")
    return "\n".join(lines)


def _make_accessibility_pdf(slug: str, rows: list[dict], out_path: Path) -> None:
    """Render the access guide to a portrait-Letter PDF for the Downloads section."""
    try:
        from fpdf import FPDF
    except ImportError as e:
        raise SystemExit(
            "build_report: missing dependency `fpdf2`.\n  pip install fpdf2"
        ) from e

    today = datetime.now(timezone.utc).date().isoformat()

    class AccessibilityPDF(FPDF):
        def footer(self_):
            if self_.page_no() <= 1:
                return
            self_.set_y(-12)
            self_.set_font(_FONT_FAMILY, "I", 8)
            self_.set_text_color(*INK_MUTED)
            self_.cell(
                0,
                6,
                _ascii_fallback(
                    f"{self_.page_no()} of {{nb}}    ·    Libby — access guide    ·    {slug}"
                ),
                align="C",
            )

    pdf = AccessibilityPDF(orientation="P", unit="mm", format="Letter")
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(left=18, top=20, right=18)
    pdf.alias_nb_pages()
    _register_unicode_font(pdf)

    _render_cover(
        pdf, f"Access guide — {slug}",
        "How to access each therapy: trial contacts + manufacturer medical-info",
        today, "LIBBY — ACCESS GUIDE",
        COVER_BG, _DISCLAIMER_CLINICIAN,
    )

    pdf.add_page()
    body_md = _accessibility_md_for_pdf(slug, rows)
    _render_markdown_block(pdf, body_md, top_h1=True)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(out_path))


def _make_patient_pdf(slug: str, body_md: str, out_path: Path) -> None:
    try:
        from fpdf import FPDF
    except ImportError as e:
        raise SystemExit(
            "build_report: missing dependency `fpdf2`.\n  pip install fpdf2"
        ) from e

    today = datetime.now(timezone.utc).date().isoformat()

    class PatientPDF(FPDF):
        def footer(self_):
            if self_.page_no() <= 1:
                return
            self_.set_y(-12)
            self_.set_font(_FONT_FAMILY, "I", 8)
            self_.set_text_color(*INK_MUTED)
            self_.cell(
                0,
                6,
                _ascii_fallback(
                    f"{self_.page_no()} of {{nb}}    ·    Libby — patient track    ·    {slug}"
                ),
                align="C",
            )

    pdf = PatientPDF(orientation="P", unit="mm", format="Letter")
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(left=18, top=20, right=18)
    pdf.alias_nb_pages()
    _register_unicode_font(pdf)

    _render_cover(
        pdf, slug, "Plain-language summary for patient and caregiver",
        today, "LIBBY — PATIENT/CAREGIVER TRACK",
        COVER_BG_PATIENT, _DISCLAIMER_PATIENT,
    )

    pdf.add_page()
    _render_markdown_block(pdf, body_md, top_h1=True)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(out_path))


# ---------- index.md downloads-section injection ----------


_DOWNLOADS_BEGIN = "<!-- libby:downloads:begin -->"
_DOWNLOADS_END = "<!-- libby:downloads:end -->"
_RX_DOWNLOADS_BLOCK = re.compile(
    re.escape(_DOWNLOADS_BEGIN) + r".*?" + re.escape(_DOWNLOADS_END),
    re.DOTALL,
)
# Insert before the first H2 (## …) when no markers exist yet, so the section
# lands above "Profile snapshot" / "Recommendation summary" rather than at the
# bottom of the page.
_RX_FIRST_H2 = re.compile(r"^## ", re.MULTILINE)


def _downloads_section(slug: str, case_docs: Path) -> str:
    artifacts = [
        (
            f"{slug}-target-validation.pdf",
            "Target validation paths",
            "diagnostic + biomarker workup that hardens the targetable-feature call",
        ),
        (
            f"{slug}-recommendations.html",
            "Recommendations table",
            "ranked options + pipeline context — self-contained HTML that opens offline",
        ),
        (
            "accessibility.md",
            "Access guide",
            "how to access each therapy — trial recruitment contacts + manufacturer medical-info lines, in a sortable in-browser table",
        ),
        (
            "manuscripts.md",
            "Master manuscripts table",
            "every paper considered — n, effect, variance, toxicities, in a sortable in-browser table",
        ),
        (
            f"{slug}-plain-language.pdf",
            "Patient/caregiver PDF",
            "plain-language summary",
        ),
    ]
    present = [(n, lbl, b) for n, lbl, b in artifacts if (case_docs / n).exists()]
    if not present:
        return ""
    lines = [
        _DOWNLOADS_BEGIN,
        "",
        "## Downloads",
        "",
    ]
    for name, label, blurb in present:
        lines.append(f"- [{label}]({_cache_busted_link(case_docs / name, name)}) — {blurb}")
    lines.extend(["", _DOWNLOADS_END, ""])
    return "\n".join(lines)


def _cache_busted_link(path: Path, name: str) -> str:
    """Append ?v=<short-content-hash> to a download link.

    GitHub Pages and intermediate caches honor URL-based cache keys, so
    changing the query string is the most reliable way to force a refresh
    when the underlying bytes change. The hash is content-derived (sha1
    first 8 chars) so unchanged files keep their warm cache; only files
    whose content actually changed get a new URL. The `?v=` is the
    convention reCAPTCHA / GA / many CDNs use for the same purpose.
    """
    try:
        digest = hashlib.sha1(path.read_bytes()).hexdigest()[:8]
    except OSError:
        return name
    return f"{name}?v={digest}"


def _inject_downloads(index_path: Path, slug: str, case_docs: Path) -> bool:
    """Idempotently insert/refresh the Downloads section in index.md.

    Returns True when the file was modified. Strategy:
      - If markers already exist, replace the block in place.
      - Otherwise insert before the first H2; if no H2, append.
      - When no artifacts exist, strip any pre-existing markers (cleanup).
    """
    text = index_path.read_text(encoding="utf-8")
    block = _downloads_section(slug, case_docs)

    if _RX_DOWNLOADS_BLOCK.search(text):
        if not block:
            new_text = _RX_DOWNLOADS_BLOCK.sub("", text)
            new_text = re.sub(r"\n{3,}", "\n\n", new_text)
        else:
            new_text = _RX_DOWNLOADS_BLOCK.sub(block.rstrip("\n"), text)
    elif block:
        m = _RX_FIRST_H2.search(text)
        if m:
            new_text = text[: m.start()] + block + text[m.start() :]
        else:
            new_text = text.rstrip() + "\n\n" + block + "\n"
    else:
        return False

    if new_text == text:
        return False
    index_path.write_text(new_text, encoding="utf-8")
    return True


# ---------- index.md target-validation injection ----------


_TV_BEGIN = "<!-- libby:target-validation:begin -->"
_TV_END = "<!-- libby:target-validation:end -->"
_RX_TV_BLOCK = re.compile(
    re.escape(_TV_BEGIN) + r".*?" + re.escape(_TV_END),
    re.DOTALL,
)
# Match the "## Preferences" heading + its body up to (but not including) the
# next H2. Group 1 captures the heading + body; we insert the TV block
# immediately after it.
_RX_PREFERENCES_BLOCK = re.compile(
    r"(^##\s+Preferences\s*\n.*?)(?=^##\s+\S)",
    re.DOTALL | re.MULTILINE,
)


def _target_validation_section(report_md: str) -> str:
    """Wrap the reporter-authored prose with stable markers for re-injection.

    The reporter's report already contains its own H2 (`## Target validation
    paths`). We just bracket it with the markers and return.
    """
    body = report_md.strip()
    if not body:
        return ""
    return "\n".join([_TV_BEGIN, "", body, "", _TV_END, ""])


def _inject_target_validation(index_path: Path, report_md: str) -> bool:
    """Idempotently insert/refresh the Target-validation section in index.md.

    Placement: immediately after the `## Preferences` block (before the next
    H2 — typically `## Scope summary`).
    Returns True when the file was modified.
    """
    text = index_path.read_text(encoding="utf-8")
    block = _target_validation_section(report_md)

    if _RX_TV_BLOCK.search(text):
        if not block:
            new_text = _RX_TV_BLOCK.sub("", text)
            new_text = re.sub(r"\n{3,}", "\n\n", new_text)
        else:
            new_text = _RX_TV_BLOCK.sub(block.rstrip("\n"), text)
    elif block:
        m = _RX_PREFERENCES_BLOCK.search(text)
        if m:
            insert_at = m.end()
            new_text = text[:insert_at] + block + "\n" + text[insert_at:]
        else:
            # No Preferences section found; fall back to inserting before the
            # first H2 (rare — would be a malformed case page).
            m = _RX_FIRST_H2.search(text)
            if m:
                new_text = text[: m.start()] + block + text[m.start() :]
            else:
                new_text = text.rstrip() + "\n\n" + block + "\n"
    else:
        return False

    if new_text == text:
        return False
    index_path.write_text(new_text, encoding="utf-8")
    return True


# ---------- main ----------


_RX_BOLD_NO_SPACE_AFTER = re.compile(r"\*\*[^\s*][^*]*\*\*[A-Za-z0-9]")
_RX_BOLD_NO_SPACE_BEFORE = re.compile(r"[A-Za-z0-9]\*\*[^\s*][^*]*\*\*")
_RX_EM_DASH = re.compile(r"—")
_RX_RANK_REF = re.compile(r"\branks?[\s\-][0-9]", flags=re.IGNORECASE)


def _check_inline_bold_spacing(path: Path) -> list[tuple[int, str]]:
    """Return a list of (line_no, line) tuples where a bold run is glued
    directly to a word character on either side. Used as a pre-flight tripwire
    on reporter-authored prose so the rendered output never has run-on words
    like `**PRAME IHC**to confirm`.
    """
    if not path.exists():
        return []
    hits: list[tuple[int, str]] = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if _RX_BOLD_NO_SPACE_AFTER.search(line) or _RX_BOLD_NO_SPACE_BEFORE.search(line):
            hits.append((i, line.rstrip()))
    return hits


def _check_em_dashes(path: Path) -> list[tuple[int, str]]:
    """Return (line_no, line) tuples for any line containing a literal em-dash
    (U+2014). The reporter contract forbids em-dashes anywhere in
    `executive_summary.md` or `target_validation_report.md`. The humanizer
    skill flags em-dash overuse as a top AI-prose tell, and the reporter is
    expected to use periods, commas, colons, or sentence restructure instead.
    Hyphens (`-`) and en-dashes (`–`, used inside numeric ranges) are unaffected.
    """
    if not path.exists():
        return []
    hits: list[tuple[int, str]] = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if _RX_EM_DASH.search(line):
            hits.append((i, line.rstrip()))
    return hits


def _check_rank_references(path: Path) -> list[tuple[int, str]]:
    """Return (line_no, line) tuples for any "rank N" / "ranks N-M" / "rank-N"
    pattern in `target_validation_report.md`. The reporter contract requires
    the target-validation report to be a self-contained narrative; rank
    numbers come from `recommendations.jsonl` and force the reader to
    cross-reference another report. Refer to interventions by drug name and /
    or NCT instead.
    """
    if not path.exists():
        return []
    hits: list[tuple[int, str]] = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if _RX_RANK_REF.search(line):
            hits.append((i, line.rstrip()))
    return hits


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: build_report.py <slug>", file=sys.stderr)
        return 2
    slug = argv[1]

    case_data = DATA_DIR / slug
    case_docs = DOCS_DIR / slug
    if not case_docs.exists():
        print(f"build_report: missing {case_docs}", file=sys.stderr)
        return 1

    index_path = case_docs / "index.md"
    if not index_path.exists():
        print(f"build_report: missing {index_path} — run /PI first", file=sys.stderr)
        return 1

    exec_path = case_data / "executive_summary.md"
    if not exec_path.exists():
        print(
            f"build_report: missing {exec_path} — run the reporter first to author "
            "the executive summary",
            file=sys.stderr,
        )
        return 1

    # Pre-flight #1: refuse to render when reporter-authored prose has bold
    # runs glued to word characters. Markdown-hygiene tripwire; the fix is in
    # the source markdown (add a space), never in the rendered PDF.
    reporter_files = (exec_path, case_data / "target_validation_report.md")
    spacing_blockers: list[tuple[Path, int, str]] = []
    for f in reporter_files:
        for ln, line in _check_inline_bold_spacing(f):
            spacing_blockers.append((f, ln, line))
    if spacing_blockers:
        print(
            "build_report: refusing to render. Bold-run spacing violation "
            "(closing `**` must be followed by a space or punctuation, not a word "
            "character). Fix the source markdown.",
            file=sys.stderr,
        )
        for path, ln, line in spacing_blockers:
            print(f"  {path}:{ln}: {line}", file=sys.stderr)
        return 1

    # Pre-flight #2: refuse to render when reporter-authored prose contains an
    # em-dash. The humanizer skill flags em-dash overuse as a top AI-prose
    # tell, and the reporter contract forbids them outright in these files.
    # Hyphens (-) and en-dashes (used inside numeric ranges) are unaffected.
    em_dash_blockers: list[tuple[Path, int, str]] = []
    for f in reporter_files:
        for ln, line in _check_em_dashes(f):
            em_dash_blockers.append((f, ln, line))
    if em_dash_blockers:
        print(
            "build_report: refusing to render. Em-dash (U+2014) found in "
            "reporter-authored prose. Replace with a period, comma, colon, or "
            "sentence restructure (see reporter.md \"Markdown formatting "
            "hygiene\" for guidance). Hyphens and en-dashes are unaffected.",
            file=sys.stderr,
        )
        for path, ln, line in em_dash_blockers:
            print(f"  {path}:{ln}: {line}", file=sys.stderr)
        return 1

    # Pre-flight #3: refuse to render when target_validation_report.md
    # references a rank number from recommendations.jsonl. The
    # target-validation report is a standalone artifact; rank numbers force
    # the reader to cross-reference another report. Refer to interventions by
    # drug name and / or NCT instead. Only checks the target-validation
    # report; the executive summary is allowed to reference ranks because it
    # ships alongside the recommendation list it's summarizing.
    rank_blockers: list[tuple[Path, int, str]] = []
    tv_report = case_data / "target_validation_report.md"
    for ln, line in _check_rank_references(tv_report):
        rank_blockers.append((tv_report, ln, line))
    if rank_blockers:
        print(
            "build_report: refusing to render. Rank-number reference found in "
            "target_validation_report.md. The target-validation report is a "
            "standalone artifact and must not refer to ranks from "
            "recommendations.jsonl. Refer to interventions by drug name and / "
            "or NCT instead (see reporter.md Step 1.5 \"Self-contained "
            "narrative rule\" for guidance).",
            file=sys.stderr,
        )
        for path, ln, line in rank_blockers:
            print(f"  {path}:{ln}: {line}", file=sys.stderr)
        return 1

    recs = _load_jsonl(case_data / "recommendations.jsonl")
    profile = _load_json(case_data / "profile.json")
    preferences = _load_json(case_data / "preferences.json")

    exec_md = exec_path.read_text(encoding="utf-8")
    body_md = _strip_page_chrome(index_path.read_text(encoding="utf-8"))
    body_md = _drop_h1(body_md)
    sources_md = _sources_markdown(recs)

    # Clinician PDF removed from the Downloads section; strip any stale copy
    # so re-runs don't leave an unlinked artifact in `docs/`.
    clinician_out = case_docs / f"{slug}-libby-report.pdf"
    if clinician_out.exists():
        clinician_out.unlink()

    plain_path = case_docs / "plain_language.md"
    if plain_path.exists():
        plain_md = _strip_page_chrome(plain_path.read_text(encoding="utf-8"))
        plain_md = _drop_h1(plain_md)
        plain_out = case_docs / f"{slug}-plain-language.pdf"
        _make_patient_pdf(slug, plain_md, plain_out)
        print(
            f"built {plain_out.relative_to(REPO_ROOT)} — "
            f"{plain_out.stat().st_size / 1024:.0f} KB"
        )

    clinical = _load_jsonl(case_data / "clinical_evidence.jsonl")
    preclinical = _load_jsonl(case_data / "preclinical_evidence.jsonl")
    trials = _load_jsonl(case_data / "trials.jsonl")
    # Master-manuscripts PDF removed from the Downloads section. The web
    # version (`manuscripts.md`) remains as the primary artifact.
    manuscripts_out = case_docs / f"{slug}-manuscripts.pdf"
    if manuscripts_out.exists():
        manuscripts_out.unlink()

    accessibility_rows = _load_jsonl(case_data / "accessibility.jsonl")
    # Access guide PDF removed from the Downloads section. The web version
    # (`accessibility.md`) remains as the primary artifact.
    accessibility_pdf_out = case_docs / f"{slug}-accessibility.pdf"
    if accessibility_pdf_out.exists():
        accessibility_pdf_out.unlink()

    # Reporter-authored target-validation prose. Drives both the website
    # injection (after `## Preferences`) and the standalone PDF.
    tv_report_path = case_data / "target_validation_report.md"
    tv_report_md = ""
    if tv_report_path.exists():
        tv_report_md = tv_report_path.read_text(encoding="utf-8").strip()
    if tv_report_md:
        tv_pdf_out = case_docs / f"{slug}-target-validation.pdf"
        _make_target_validation_pdf(slug, tv_report_md, tv_pdf_out)
        print(
            f"built {tv_pdf_out.relative_to(REPO_ROOT)} — "
            f"{tv_pdf_out.stat().st_size / 1024:.0f} KB"
        )
    else:
        # If the reporter has not yet authored the report, strip any stale PDF
        # so the Downloads block doesn't surface a phantom link.
        tv_pdf_out = case_docs / f"{slug}-target-validation.pdf"
        if tv_pdf_out.exists():
            tv_pdf_out.unlink()

    html_out = case_docs / f"{slug}-recommendations.html"
    html_out.write_text(
        _render_recommendations_html(slug, recs, profile, preferences, trials),
        encoding="utf-8",
    )
    print(
        f"built {html_out.relative_to(REPO_ROOT)} — "
        f"{html_out.stat().st_size / 1024:.0f} KB"
    )

    if _inject_target_validation(index_path, tv_report_md):
        print(
            f"patched {index_path.relative_to(REPO_ROOT)} — target-validation section "
            f"({'inserted' if tv_report_md else 'cleared'})"
        )

    if _inject_downloads(index_path, slug, case_docs):
        print(f"patched {index_path.relative_to(REPO_ROOT)} — downloads section")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
