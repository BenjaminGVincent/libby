"""Tests for the biomarker-survey track.

Three things are worth locking down here:
  - the committed reference panel still matches the workbook it was imported from
    (a hand-edit of the machine-generated file is the failure mode);
  - the renderer's pre-flight actually blocks the contract violations it claims to
    (a silently-published wrong page is worse than a failed build);
  - the survey → target_validator handoff is visible in the rendered
    target-validation page, including the case where it was dropped.
"""

import json
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent

import build_biomarker_survey as bs  # noqa: E402
import build_target_validation as btv  # noqa: E402
import import_biomarker_panel as ibp  # noqa: E402


# ---------- reference panels ----------


def test_panel_matches_workbook():
    """The committed panel is machine-generated; drift means someone hand-edited it."""
    workbook = REPO / "selected_biomarker_target_list.xlsx"
    if not workbook.exists():
        pytest.skip("source workbook not present in this checkout")
    pytest.importorskip("openpyxl")
    rebuilt = ibp.serialize(ibp.build_panel(workbook))
    committed = (REPO / "data" / "reference" / "selected_biomarker_panel.json").read_text("utf-8")
    assert rebuilt == committed, (
        "selected_biomarker_panel.json is out of sync with the workbook; "
        "re-run scripts/import_biomarker_panel.py"
    )


def test_panel_shape():
    panel = json.loads((REPO / "data" / "reference" / "selected_biomarker_panel.json").read_text("utf-8"))
    assert panel["target_count"] == len(panel["targets"])
    keys = [t["panel_key"] for t in panel["targets"]]
    assert len(keys) == len(set(keys)), "panel_key must be unique — the renderer joins on it"
    for t in panel["targets"]:
        assert t["gene_symbol"]
        assert t["default_assay"]


def test_tumor_agnostic_panel_shape():
    agnostic = json.loads((REPO / "data" / "reference" / "tumor_agnostic_biomarkers.json").read_text("utf-8"))
    assert agnostic["biomarker_count"] == len(agnostic["biomarkers"])
    keys = [b["panel_key"] for b in agnostic["biomarkers"]]
    assert len(keys) == len(set(keys))
    for b in agnostic["biomarkers"]:
        assert b["relevance_class"] in ("tumor_agnostic", "tumor_subset")
        assert b["default_assay"]
        assert b["therapeutic_implication"], "an entry with no therapeutic implication has no reason to be screened"


def test_every_survey_row_schema_field_is_documented():
    """Guard against a schema property with no description — these render as
    column semantics a downstream agent has to guess at."""
    schema = json.loads((REPO / "scripts" / "schema" / "biomarker_survey.schema.json").read_text("utf-8"))
    undocumented = [
        name for name, spec in schema["properties"].items()
        if "description" not in spec and name not in ("case_slug", "notes")
    ]
    assert not undocumented, undocumented


# ---------- renderer pre-flight ----------


def _agnostic_keys():
    agnostic = json.loads((REPO / "data" / "reference" / "tumor_agnostic_biomarkers.json").read_text("utf-8"))
    return [b["panel_key"] for b in agnostic["biomarkers"]]


def _row(panel_key, **over):
    row = {
        "survey_id": f"{panel_key}-row",
        "case_slug": "t",
        "panel_source": "tumor_agnostic_biomarkers",
        "panel_key": panel_key,
        "biomarker_label": panel_key.upper(),
        "relevance_class": "tumor_agnostic",
        "relevance_rationale": "Predictive regardless of primary site.",
        "measurement_status": "not_measured",
        "priority": "high",
        "screening_recommendation": "order_now",
        "rationale": "Nothing on file establishes this.",
    }
    row.update(over)
    return row


def _full_survey(**over_last):
    rows = [_row(k) for k in _agnostic_keys()]
    if over_last:
        rows[-1].update(over_last)
    return rows


def test_preflight_passes_on_complete_survey():
    rows = _full_survey()
    bs.preflight(rows, bs.compute_coverage(rows))  # must not raise


def test_preflight_blocks_missing_tumor_agnostic_entry():
    rows = _full_survey()[:-1]
    with pytest.raises(bs.BuildError, match="tumor-agnostic"):
        bs.preflight(rows, bs.compute_coverage(rows))


def test_preflight_blocks_em_dash_in_prose():
    rows = _full_survey(rationale="Nothing on file — a panel would report it.")
    with pytest.raises(bs.BuildError, match="em-dash"):
        bs.preflight(rows, bs.compute_coverage(rows))


def test_preflight_blocks_em_dash_in_narrative():
    rows = _full_survey()
    with pytest.raises(bs.BuildError, match="em-dash"):
        bs.preflight(rows, bs.compute_coverage(rows), narrative="A gap — a real one.")


def test_preflight_blocks_not_hardened_without_gap():
    rows = _full_survey(
        measurement_status="measured_not_hardened",
        handoff_to_target_validator=True,
        screening_recommendation="order_now",
    )
    with pytest.raises(bs.BuildError, match="hardening_gap"):
        bs.preflight(rows, bs.compute_coverage(rows))


def test_preflight_blocks_not_hardened_without_handoff():
    rows = _full_survey(
        measurement_status="measured_not_hardened",
        hardening_gap="RNA only.",
        handoff_to_target_validator=False,
    )
    with pytest.raises(bs.BuildError, match="handoff_to_target_validator"):
        bs.preflight(rows, bs.compute_coverage(rows))


def test_coverage_derives_out_of_scope_targets():
    rows = _full_survey()
    coverage = bs.compute_coverage(rows)
    # No protein-target rows were emitted, so every panel target is out of scope.
    assert coverage["targets_in_scope"] == 0
    assert len(coverage["out_of_scope"]) == coverage["panel_targets"]
    assert coverage["missing_agnostic"] == []


# ---------- rendered output ----------


def test_page_distinguishes_not_measured_from_negative():
    """The whole track hinges on 'never tested' not reading as 'tested, negative'."""
    rows = _full_survey()
    page = bs.render_page("t", rows, bs.compute_coverage(rows))
    assert "Not measured" in page
    assert "not the same as a negative" in page


def test_page_reports_measured_rows_separately():
    rows = _full_survey()
    rows[0].update(
        measurement_status="measured_hardened",
        screening_recommendation="no_action",
        status_evidence=["profile.json:biomarkers[0]"],
    )
    page = bs.render_page("t", rows, bs.compute_coverage(rows))
    assert "Already established" in page


def test_nav_links_only_pages_that_exist(tmp_path):
    rows = _full_survey()
    (tmp_path / "index.md").write_text("x")
    page = bs.render_page("t", rows, bs.compute_coverage(rows), case_docs=tmp_path)
    assert "[Back to case](index.md)" in page
    # target_validation.md was never rendered for this case; linking it would
    # break `mkdocs build --strict`.
    assert "(target_validation.md)" not in page


# ---------- handoff into target validation ----------


def _handoff_row(survey_id="msi-dmmr-row"):
    return {
        "survey_id": survey_id,
        "biomarker_label": "MSI / dMMR",
        "priority": "essential",
        "measurement_status": "measured_not_hardened",
        "hardening_gap": "Called from a hotspot panel not sized to report it.",
        "handoff_to_target_validator": True,
        "status_evidence": ["profile.json:biomarkers[1]"],
    }


def test_target_validation_flags_unaddressed_handoff():
    out = btv.render_survey_handoffs(rows=[], survey=[_handoff_row()])
    assert "not yet addressed" in out
    assert "MSI / dMMR" in out


def test_target_validation_marks_addressed_handoff():
    validation = [{
        "validation_id": "msi-orthogonal",
        "test_name": "MMR protein IHC",
        "source_survey_id": "msi-dmmr-row",
    }]
    out = btv.render_survey_handoffs(rows=validation, survey=[_handoff_row()])
    assert "addressed above" in out
    assert "MMR protein IHC" in out
    assert "not yet addressed" not in out


def test_target_validation_ignores_survey_without_handoffs():
    survey = [{"survey_id": "x", "handoff_to_target_validator": False}]
    assert btv.render_survey_handoffs(rows=[], survey=survey) == ""


# --- Full-coverage surveys -------------------------------------------------
#
# The survey reports every biomarker considered, not only the ones that survived
# scoping: an irrelevant panel entry gets a `screened_not_relevant` row carrying
# its reason, instead of being omitted and reconstructed as a bare gene symbol.
# Surveys written before that change omit them, and must keep rendering as built.

import build_biomarker_survey as bs


def _cov_row(key, cls, **kw):
    r = {
        "panel_key": key,
        "biomarker_label": key.upper(),
        "relevance_class": cls,
        "measurement_status": "not_measured",
        "priority": "low",
        "relevance_rationale": f"reason for {key}",
    }
    r.update(kw)
    return r


def test_set_aside_rows_are_collected_and_not_double_counted():
    rows = [
        _cov_row("msi-dmmr", "tumor_agnostic"),
        _cov_row("cd276", "tumor_subset"),
        _cov_row("cldn18", "screened_not_relevant"),
        _cov_row("gucy2c", "screened_not_relevant"),
    ]
    cov = bs.compute_coverage(rows)
    assert len(cov["set_aside_rows"]) == 2
    # A full survey omits nothing, so there is no subtraction list to show.
    assert cov["out_of_scope"] == []


def test_legacy_survey_still_derives_out_of_scope_by_subtraction():
    """Surveys with no screened_not_relevant row keep the old behaviour."""
    rows = [_cov_row("msi-dmmr", "tumor_agnostic"), _cov_row("cd276", "tumor_subset")]
    cov = bs.compute_coverage(rows)
    assert cov["set_aside_rows"] == []
    assert len(cov["out_of_scope"]) > 0


def test_a_reader_never_sees_both_lists():
    """The two shapes are mutually exclusive; showing both would double-report."""
    for rows in (
        [_cov_row("msi-dmmr", "tumor_agnostic"), _cov_row("cldn18", "screened_not_relevant")],
        [_cov_row("msi-dmmr", "tumor_agnostic")],
    ):
        cov = bs.compute_coverage(rows)
        assert not (cov["set_aside_rows"] and cov["out_of_scope"])


def test_set_aside_table_carries_the_reason_not_just_the_name():
    """The whole point of the change: a per-target reason, which a bare gene
    symbol list could not carry."""
    html_out = bs.render_gap_table([_cov_row("cldn18", "screened_not_relevant")])
    assert "reason for cldn18" in html_out


def test_remaining_panel_uses_the_same_columns_as_the_gap_table():
    """Same table, same columns. What separates these rows from a gap row is the
    conclusion, not the depth of the record."""
    row = _cov_row("cldn18", "screened_not_relevant")
    assert bs.render_gap_table([row]).count("<th>") == bs.render_gap_table(
        [_cov_row("msi-dmmr", "tumor_agnostic")]
    ).count("<th>")


def test_indent_block_preserves_blank_lines():
    """Indenting a blank line ends a mkdocs admonition early and spills the rest
    of the table into the page body."""
    out = bs._indent_block("a\n\nb")
    assert out.splitlines() == ["    a", "", "    b"]


def test_set_aside_rows_never_appear_in_the_gap_buckets():
    """The bug this guards: `screened_not_relevant` rows are all `not_measured`
    by construction, so bucketing on measurement_status alone put all 63 of them
    in the gap table *and* the set-aside section. The page then reported 78 gaps
    for a survey with 15."""
    rows = [
        _cov_row("msi-dmmr", "tumor_agnostic"),
        _cov_row("cldn18", "screened_not_relevant"),
        _cov_row("gucy2c", "screened_not_relevant"),
    ]
    in_scope, gaps, not_hardened, measured = bs.bucket_rows(rows)
    assert [r["panel_key"] for r in gaps] == ["msi-dmmr"]
    assert [r["panel_key"] for r in in_scope] == ["msi-dmmr"]
    assert not_hardened == [] and measured == []
    # The two set-aside rows are held out of every status bucket, so they cannot
    # be counted as gaps and cannot render in the gap table.
    assert len(rows) - len(in_scope) == 2


def test_legacy_survey_buckets_unchanged():
    rows = [
        _cov_row("msi-dmmr", "tumor_agnostic"),
        _cov_row("tmb-high", "tumor_agnostic", measurement_status="measured_not_hardened"),
        _cov_row("hla", "tumor_subset", measurement_status="measured_hardened"),
    ]
    in_scope, gaps, not_hardened, measured = bs.bucket_rows(rows)
    assert len(gaps) == 1 and len(not_hardened) == 1 and len(measured) == 1
    assert len(in_scope) == len(rows)


def test_remaining_panel_table_is_visible_not_collapsed():
    """These entries were assessed like every other one, so they get their own
    visible table. A reader searching for a specific biomarker should find it
    without expanding anything."""
    rows = [
        _cov_row("msi-dmmr", "tumor_agnostic"),
        _cov_row("cldn18", "screened_not_relevant"),
    ]
    page = bs.render_page("slug", rows, bs.compute_coverage(rows), case_docs=None)
    assert "## Remaining panel biomarkers" in page
    # The section's own table must not sit inside a collapsible wrapper.
    tail = page.split("## Remaining panel biomarkers", 1)[1]
    assert "??? note" not in tail
    assert "<details" not in tail
    assert "<th>Recommended assay</th>" in tail
    assert "<th>What a positive result would open</th>" in tail
