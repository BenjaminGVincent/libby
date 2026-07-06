#!/usr/bin/env python3
"""Render the master manuscript inventory for a Libby case.

One flat table covering every paper considered (clinical + preclinical), with
the four user-named decision-relevant fields per row: sample size, effect size,
variance, and toxicities (type / number / frequency). Modeled on io-shieldbreak's
'Pharmacodynamic Results' / 'Scope inventory' table — one paper per row, no
per-intervention grouping, sortable by year.

Reads:
  data/cases/<slug>/clinical_evidence.jsonl
  data/cases/<slug>/preclinical_evidence.jsonl

Writes:
  docs/cases/<slug>/manuscripts.md
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path
from libbylib import load_jsonl

REPO = Path(__file__).resolve().parent.parent




def fmt(v, dash: str = "—") -> str:
    if v is None or v == "":
        return dash
    return html.escape(str(v))


def num_fmt(v, places: int = 2, dash: str = "—") -> str:
    if v is None or v == "":
        return dash
    try:
        return f"{float(v):.{places}f}"
    except (TypeError, ValueError):
        return html.escape(str(v))


def link_pmid(pmid) -> str:
    if not pmid:
        return ""
    return f'<a href="https://pubmed.ncbi.nlm.nih.gov/{html.escape(str(pmid))}">PMID&nbsp;{html.escape(str(pmid))}</a>'


def link_doi(doi) -> str:
    if not doi:
        return ""
    return f'<a href="https://doi.org/{html.escape(str(doi))}">DOI</a>'


def link_nct(nct) -> str:
    if not nct:
        return ""
    return f'<a href="https://clinicaltrials.gov/study/{html.escape(str(nct))}">{html.escape(str(nct))}</a>'


def reference_cell(r: dict) -> str:
    """Single canonical reference link: PubMed > DOI > NCT > evidence_id.

    The notion is one stable, dereferenceable URL per row. Secondary identifiers
    fall through to the Notes column or the per-intervention evidence page.
    """
    pmid = r.get("pmid")
    if pmid:
        return link_pmid(pmid)
    doi = r.get("doi")
    if doi:
        return f'<a href="https://doi.org/{html.escape(str(doi))}">doi:{html.escape(str(doi))}</a>'
    nct = r.get("nct_id") or r.get("evidence_id")
    if nct and str(nct).upper().startswith("NCT"):
        return link_nct(nct)
    return "—"


def notes_cell(r: dict) -> str:
    """Combine row `notes` with auto-generated explanations of missing data.

    Order:
      1. Inclusion-status text first when row is `considered_excluded` (the
         exclusion_reason is the most decision-relevant note).
      2. The agent-authored `notes` (clinical) or `caveats` (preclinical).
      3. Auto-generated explanations when key fields are empty (toxicities,
         effect_size, n, etc.) so a reviewer can tell missing-by-design from
         missing-by-omission at a glance.
    """
    bits: list[str] = []
    status = (r.get("inclusion_status") or "included").lower()
    if status == "considered_excluded":
        reason = r.get("exclusion_reason")
        if reason:
            bits.append(f"<strong>Excluded:</strong> {html.escape(str(reason))}")

    authored = r.get("notes") or r.get("caveats")
    if authored:
        bits.append(html.escape(str(authored)))

    if status != "considered_excluded":
        gaps: list[str] = []
        kind = r.get("_source") or ""
        if kind == "trial" and not r.get("pmid"):
            gaps.append("registration only — no peer-reviewed publication yet")
        if r.get("indication") and not r.get("toxicities") and not r.get("safety_summary"):
            gaps.append("toxicity table not extracted")
        if r.get("indication") and r.get("effect_size") in (None, ""):
            gaps.append("primary endpoint not extracted")
        if gaps:
            bits.append("<em>" + html.escape("; ".join(gaps)) + "</em>")

    return "<br>".join(bits) if bits else "—"


def report_cell(r: dict) -> str:
    first = r.get("first_author") or "—"
    last = r.get("last_author") or "—"
    yr = r.get("year") or "—"
    journal = r.get("journal") or ""
    parts = [f"{html.escape(str(first))}/{html.escape(str(last))} ({yr})"]
    if journal:
        parts.append(f"<em>{html.escape(str(journal))}</em>")
    return "<br>".join(parts)


def fit_badge(label: str | None) -> str:
    if not label:
        return "—"
    cls = {
        "strong": "fit-strong",
        "partial": "fit-partial",
        "weak": "fit-weak",
        "none": "fit-none",
        "cross_tumor_only": "fit-weak",
    }.get(label, "fit-none")
    pretty = label.replace("_", " ")
    return f'<span class="fit-badge {cls}">{html.escape(pretty)}</span>'


def kind_badge(kind: str) -> str:
    if kind == "clinical":
        return '<span class="rel-badge rel-indication">clinical</span>'
    if kind == "preclinical":
        return '<span class="rel-badge rel-cross-tumor">preclinical</span>'
    return '<span class="rel-badge rel-basket">trial publication</span>'


def status_badge(row: dict) -> str:
    status = (row.get("inclusion_status") or "included").lower()
    if status == "considered_excluded":
        reason = row.get("exclusion_reason") or "—"
        return (
            '<span class="rel-badge rel-other">excluded</span>'
            f'<br><small>{html.escape(str(reason))}</small>'
        )
    return '<span class="fit-badge fit-strong">included</span>'


_OUTCOME_LABEL_MAP = {
    "ORR": "ORR",
    "RR": "RR",
    "CR_rate": "CR rate",
    "DCR": "DCR",
    "DoR": "mDoR",
    "PFS": "mPFS",
    "PFS_rate": "PFS rate",
    "OS": "mOS",
    "OS_rate": "OS rate",
    "RFS": "mRFS",
    "DFS": "mDFS",
    "EFS": "mEFS",
    "TTR": "mTTR",
    "TTP": "mTTP",
    "TTNT": "mTTNT",
    "HR_OS": "OS HR",
    "HR_PFS": "PFS HR",
    "HR_DFS": "DFS HR",
    "HR_RFS": "RFS HR",
    "HR_EFS": "EFS HR",
    "AE_rate": "AE rate",
    "TRAE_rate": "TRAE rate",
    "discontinuation_rate": "Discontinuation",
    "biomarker": "Biomarker",
    "other": "Other",
}


def _fmt_outcome_effect(o: dict) -> str:
    """Render `<label>: <effect>[ <units>]` for one structured outcome entry."""
    name = o.get("name") or "other"
    label = _OUTCOME_LABEL_MAP.get(name, html.escape(str(name)))
    eff = o.get("effect_size")
    units = o.get("effect_units")
    if eff is None or eff == "":
        body = "—"
    else:
        body = num_fmt(eff, places=2) if isinstance(eff, (int, float)) else html.escape(str(eff))
        if units:
            body += f" {html.escape(str(units))}"
    subgroup = o.get("subgroup")
    out = f"<strong>{label}</strong>: {body}"
    if subgroup:
        out += f' <small>({html.escape(str(subgroup))})</small>'
    notes = o.get("notes")
    if notes:
        out += f' <small><em>{html.escape(str(notes))}</em></small>'
    return out


def _fmt_outcome_variance(o: dict) -> str:
    """Render the CI / variance / p-value bundle for one structured outcome entry."""
    parts: list[str] = []
    lo, hi = o.get("ci_lower"), o.get("ci_upper")
    if lo is not None and hi is not None:
        parts.append(f"95% CI {num_fmt(lo)}–{num_fmt(hi)}")
    free = o.get("variance_or_ci")
    if free:
        parts.append(html.escape(str(free)))
    p = o.get("p_value")
    if p not in (None, "", "—"):
        parts.append(f"p={html.escape(str(p))}")
    return " · ".join(parts) if parts else "—"


def effect_cell_clinical(r: dict) -> str:
    # Prefer the structured `outcomes[]` array — one stacked line per outcome.
    outcomes = r.get("outcomes") or []
    if outcomes:
        return "<br>".join(_fmt_outcome_effect(o) for o in outcomes)
    # Legacy fallback: single-outcome row from the original schema.
    e = r.get("effect_size")
    units = r.get("effect_units")
    if e is None or e == "":
        return "—"
    out = num_fmt(e, places=2) if isinstance(e, (int, float)) else html.escape(str(e))
    if units:
        out += f" {html.escape(str(units))}"
    return out


def variance_cell_clinical(r: dict) -> str:
    # Prefer the structured `outcomes[]` array — render the CI / p-value
    # bundle on the line that lines up with the matching Effect-size entry.
    outcomes = r.get("outcomes") or []
    if outcomes:
        return "<br>".join(_fmt_outcome_variance(o) for o in outcomes)
    # Legacy fallback: single-outcome row.
    lo, hi = r.get("ci_lower"), r.get("ci_upper")
    free = r.get("variance_or_ci")
    parts = []
    if lo is not None and hi is not None:
        parts.append(f"95% CI {num_fmt(lo)}–{num_fmt(hi)}")
    if free:
        parts.append(html.escape(str(free)))
    p = r.get("p_value")
    if p not in (None, "", "—"):
        parts.append(f"p={html.escape(str(p))}")
    return "<br>".join(parts) if parts else "—"


def n_cell_clinical(r: dict) -> str:
    n = r.get("n")
    if n in (None, ""):
        return "—"
    return html.escape(str(n))


def n_cell_preclinical(r: dict) -> str:
    n = r.get("n_units")
    if not n:
        return "—"
    return html.escape(str(n))


def effect_cell_preclinical(r: dict) -> str:
    qual = r.get("effect_size_qual")
    finding = r.get("key_finding") or ""
    if qual:
        return f"{html.escape(qual)} — {html.escape(finding)}" if finding else html.escape(qual)
    return html.escape(finding) or "—"


def variance_cell_preclinical(r: dict) -> str:
    parts = []
    control = r.get("control_arm")
    if control:
        parts.append(f"vs {html.escape(str(control))}")
    trans = r.get("translatability_score")
    if trans:
        parts.append(f"translatability: {html.escape(str(trans))}")
    return "<br>".join(parts) if parts else "—"


def fmt_toxicity(t: dict) -> str:
    """Render one toxicity row as 'term (grade): n/N (rate%)'."""
    term = html.escape(str(t.get("term") or "?"))
    grade = t.get("grade")
    n_events = t.get("n_events")
    denom = t.get("denominator")
    rate = t.get("rate_pct")

    grade_str = f" G{html.escape(str(grade))}" if grade and grade != "any" else ""
    head = f"<strong>{term}</strong>{grade_str}"

    rate_parts = []
    if n_events is not None and denom is not None:
        rate_parts.append(f"{n_events}/{denom}")
    elif denom is not None:
        rate_parts.append(f"n={denom}")
    if rate is not None:
        rate_parts.append(f"{num_fmt(rate, places=1).rstrip('0').rstrip('.')}%")
    rate_str = f" — {' · '.join(rate_parts)}" if rate_parts else ""

    return head + rate_str


def toxicities_cell(r: dict) -> str:
    tox = r.get("toxicities")
    summary = r.get("safety_summary")
    if not tox:
        return html.escape(summary) if summary else "—"
    items = "<br>".join(fmt_toxicity(t) for t in tox)
    return items


COLS: list[tuple[str, str]] = [
    ("Report",      "report"),
    ("Reference",   "reference"),
    ("Type",        "kind"),
    ("Inclusion",   "inclusion"),
    ("Intervention","intervention"),
    ("Indication / model", "indication"),
    ("Design",      "design"),
    ("n",           "n"),
    ("Effect size", "effect"),
    ("Variance",    "variance"),
    ("Toxicities (type · n/N · rate)", "toxicities"),
    ("Case fit",    "case_match"),
    ("Notes",       "notes"),
]


def render_clinical_row(r: dict) -> str:
    cells: list[str] = []
    excluded = (r.get("inclusion_status") or "included") == "considered_excluded"
    for _, key in COLS:
        if key == "report":
            cells.append(f"<td>{report_cell(r)}</td>")
        elif key == "reference":
            cells.append(f"<td>{reference_cell(r)}</td>")
        elif key == "kind":
            kind = "trial" if r.get("_source") == "trial" else "clinical"
            cells.append(f"<td>{kind_badge(kind)}</td>")
        elif key == "inclusion":
            cells.append(f"<td>{status_badge(r)}</td>")
        elif key == "notes":
            cells.append(f"<td>{notes_cell(r)}</td>")
        elif key == "intervention":
            cells.append(f"<td>{fmt(r.get('intervention_label'))}</td>")
        elif key == "indication":
            if excluded:
                cells.append("<td>—</td>")
            else:
                ind = r.get("indication") or ""
                pop = r.get("population_detail") or ""
                line = r.get("line_of_therapy") or ""
                tag = f" <em>({html.escape(line)})</em>" if line else ""
                sub = f"<br><small>{html.escape(pop)}</small>" if pop else ""
                cells.append(f"<td>{html.escape(ind)}{tag}{sub}</td>")
        elif key == "design":
            cells.append(f"<td>{fmt(r.get('design'))}</td>")
        elif key == "n":
            cells.append(f'<td class="num">{n_cell_clinical(r)}</td>')
        elif key == "effect":
            if excluded:
                cells.append('<td class="num">—</td>')
            else:
                outcome = r.get("outcome") or ""
                sub = f"<br><small>{html.escape(outcome)}</small>" if outcome else ""
                cells.append(f'<td class="num">{effect_cell_clinical(r)}{sub}</td>')
        elif key == "variance":
            cells.append(f'<td class="num">{variance_cell_clinical(r)}</td>')
        elif key == "toxicities":
            if excluded:
                cells.append("<td>—</td>")
            else:
                cells.append(f"<td>{toxicities_cell(r)}</td>")
        elif key == "case_match":
            cells.append(f"<td>{fit_badge(r.get('case_match'))}</td>")
        else:
            cells.append("<td>—</td>")
    return "        <tr>" + "".join(cells) + "</tr>"


def render_preclinical_row(r: dict) -> str:
    cells: list[str] = []
    excluded = (r.get("inclusion_status") or "included") == "considered_excluded"
    for _, key in COLS:
        if key == "report":
            cells.append(f"<td>{report_cell(r)}</td>")
        elif key == "reference":
            cells.append(f"<td>{reference_cell(r)}</td>")
        elif key == "kind":
            cells.append(f"<td>{kind_badge('preclinical')}</td>")
        elif key == "inclusion":
            cells.append(f"<td>{status_badge(r)}</td>")
        elif key == "notes":
            cells.append(f"<td>{notes_cell(r)}</td>")
        elif key == "intervention":
            cells.append(f"<td>{fmt(r.get('intervention_label'))}</td>")
        elif key == "indication":
            cells.append(f"<td>{fmt(r.get('model_system'))}</td>")
        elif key == "design":
            cells.append(f"<td>{fmt(r.get('mechanism'))}</td>")
        elif key == "n":
            cells.append(f'<td class="num">{n_cell_preclinical(r)}</td>')
        elif key == "effect":
            cells.append(f"<td>{effect_cell_preclinical(r)}</td>")
        elif key == "variance":
            cells.append(f"<td>{variance_cell_preclinical(r)}</td>")
        elif key == "toxicities":
            cells.append("<td><em>n/a (preclinical)</em></td>")
        elif key == "case_match":
            cells.append(f"<td>{fit_badge(r.get('case_match'))}</td>")
        else:
            cells.append("<td>—</td>")
    return "        <tr>" + "".join(cells) + "</tr>"


def trial_to_synthetic_row(t: dict) -> dict:
    """Map a trials.jsonl row into a clinical-evidence-shaped row for the master table.

    Used only for trial rows whose PMID is NOT already present in clinical_evidence.jsonl —
    surfaces trial publications (and registration-only entries) the clinician didn't promote.
    """
    nct = t.get("nct_id")
    has_pub = bool(t.get("pmid"))
    note_bits: list[str] = []
    if t.get("inclusion_match_notes"):
        note_bits.append(str(t["inclusion_match_notes"]))
    if not has_pub and nct:
        note_bits.append("Trial registration only — no peer-reviewed publication yet")
    return {
        "evidence_id": t.get("nct_id") or t.get("pmid") or "",
        "case_slug": t.get("case_slug"),
        "intervention_id": t.get("intervention_id") or (t.get("intervention") or "").lower().replace(" ", "-"),
        "intervention_label": t.get("intervention") or "—",
        "indication": t.get("indication") or "—",
        "line_of_therapy": t.get("line"),
        "population_detail": t.get("biomarker") or "",
        "design": t.get("design") or t.get("phase") or "—",
        "n": t.get("n"),
        "first_author": t.get("first_author"),
        "last_author": t.get("last_author"),
        "year": t.get("year"),
        "journal": t.get("journal") or ("ClinicalTrials.gov registration" if not has_pub else ""),
        "outcome": t.get("endpoint") or "",
        "effect_size": t.get("effect_size"),
        "effect_units": "",
        "ci_lower": t.get("ci_lower"),
        "ci_upper": t.get("ci_upper"),
        "p_value": t.get("p_value"),
        "case_match": t.get("fit_to_case"),
        "pmid": t.get("pmid"),
        "doi": t.get("doi"),
        "nct_id": nct,
        "notes": " · ".join(note_bits) if note_bits else "",
        "_source": "trial",
    }


def render_table(clinical: list[dict], preclinical: list[dict], trials: list[dict]) -> str:
    """Render a flat master table from clinical evidence + preclinical evidence + trial publications.

    Trial publications are pulled from trials.jsonl when their PMID is not already in
    clinical_evidence (avoids double-counting). Trial registration rows without a PMID
    are also surfaced so the user sees every manuscript and registration considered.
    """
    if not clinical and not preclinical and not trials:
        return "_No manuscripts indexed yet._\n"

    seen_pmids: set[str] = {str(r.get("pmid")) for r in clinical if r.get("pmid")}
    seen_pmids |= {str(r.get("pmid")) for r in preclinical if r.get("pmid")}
    extra_trial_rows: list[dict] = []
    for t in trials:
        pmid = t.get("pmid")
        if pmid and str(pmid) in seen_pmids:
            continue
        extra_trial_rows.append(trial_to_synthetic_row(t))

    head = "".join(f"<th>{html.escape(label)}</th>" for label, _ in COLS)
    body: list[str] = []
    triples: list[tuple[dict, str]] = (
        [(r, "clinical") for r in clinical]
        + [(r, "preclinical") for r in preclinical]
        + [(r, "trial") for r in extra_trial_rows]
    )
    triples.sort(key=lambda pair: -(pair[0].get("year") or 0))
    for r, kind in triples:
        if kind == "preclinical":
            body.append(render_preclinical_row(r))
        else:
            body.append(render_clinical_row(r))
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    args = parser.parse_args()
    slug = args.slug

    case_dir = REPO / "data" / "cases" / slug
    clinical = load_jsonl(case_dir / "clinical_evidence.jsonl")
    preclinical = load_jsonl(case_dir / "preclinical_evidence.jsonl")
    trials = load_jsonl(case_dir / "trials.jsonl")

    n_clin_inc = sum(1 for r in clinical if (r.get("inclusion_status") or "included") == "included")
    n_clin_exc = len(clinical) - n_clin_inc
    n_prec_inc = sum(1 for r in preclinical if (r.get("inclusion_status") or "included") == "included")
    n_prec_exc = len(preclinical) - n_prec_inc
    seen_pmids = {str(r.get("pmid")) for r in clinical + preclinical if r.get("pmid")}
    n_trial_extra = sum(1 for t in trials if not (t.get("pmid") and str(t["pmid"]) in seen_pmids))

    parts: list[str] = [
        '<meta name="robots" content="noindex">\n',
        f"# Manuscripts considered — `{slug}`\n",
        f"Master inventory: {len(clinical)} clinical "
        f"({n_clin_inc} included, {n_clin_exc} considered & excluded) + "
        f"{len(preclinical)} pre-clinical "
        f"({n_prec_inc} included, {n_prec_exc} considered & excluded) + "
        f"{n_trial_extra} additional trial publications/registrations. "
        "One row per paper, sorted by year (newest first). Excluded rows are "
        "papers a Libby agent reviewed and chose NOT to feed to the board, with the "
        "exclusion reason captured. Toxicities use CTCAE-style term · grade · n/N · "
        "rate. Pre-clinical rows leave the toxicity cell blank by design. A "
        "printable PDF version is linked from the case **Downloads** section.\n",
        render_table(clinical, preclinical, trials),
        f"[Back to case](index.md) · [Trials](trials.md) · [Evidence (per intervention)](evidence.md) · "
        f"[Target validation](target_validation.md) · "
        f"[Board](board.md) · [Recommendations](recommendations.md)\n",
        '!!! danger disclaimer "Decision support, not medical advice"\n'
        "    See [PHI policy](../../phi_policy.md).\n",
    ]

    body_md = "\n".join(parts) + "\n"
    dst = REPO / "docs" / "cases" / slug / "manuscripts.md"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(body_md, encoding="utf-8")
    print(f"wrote {dst} (clinical={len(clinical)}, preclinical={len(preclinical)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
