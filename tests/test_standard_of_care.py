"""Tests for the standard-of-care track.

Three things are worth locking down here:
  - the renderer's pre-flight actually blocks the ways this specific report could
    mislead a treating team (an option called actionable when a gate is open, when
    the patient already progressed on it, or when the only endorsement behind it
    was written for a different population);
  - the schema agrees with the pre-flight, so a row cannot pass validation and
    then fail the build for a reason the schema should have caught, or vice versa;
  - the track stays additive — the rendered page says so, and nothing here reaches
    into the ranked recommendations.
"""

import json
from datetime import date, timedelta
from pathlib import Path

import jsonschema
import pytest

REPO = Path(__file__).resolve().parent.parent

import build_standard_of_care as soc  # noqa: E402

SCHEMA = json.loads((REPO / "scripts" / "schema" / "standard_of_care.schema.json").read_text("utf-8"))
VALIDATOR = jsonschema.Draft202012Validator(SCHEMA)

TODAY = date.today().isoformat()


def _row(**over):
    row = {
        "soc_id": "carboplatin-etoposide-1l",
        "case_slug": "t",
        "option_label": "Carboplatin + etoposide",
        "category": "systemic_chemotherapy",
        "intent": "life_prolonging",
        "line_of_therapy": "first_line",
        "endorsements": [
            {
                "source": "NCCN",
                "designation": "Category 1, preferred",
                "indication_text": "Extensive-stage disease, first line, ECOG 0-2.",
                "population_match": "matches_this_patient",
                "version_or_date": "NCCN v2.2026",
                "citation": "guideline:NCCN v2.2026",
            }
        ],
        "eligibility_status": "eligible",
        "eligibility_rationale": "No prior systemic therapy on file; organ function adequate.",
        "consideration_status": "consider_now",
        "priority": "essential",
        "rationale": "Guideline-preferred first-line regimen for this disease state.",
        "last_verified_utc": TODAY,
    }
    row.update(over)
    return row


# ---------- schema ----------


def test_valid_row_passes_schema():
    VALIDATOR.validate(_row())


def test_every_schema_field_is_documented():
    """Guard against a schema property with no description — these render as
    column semantics a downstream agent has to guess at."""
    undocumented = [
        name for name, spec in SCHEMA["properties"].items()
        if "description" not in spec and name not in ("case_slug", "notes")
    ]
    assert not undocumented, undocumented


def test_schema_requires_an_endorsement():
    """An option with no approval and no guideline carriage is not standard of
    care; the definition of the track is enforced, not merely documented."""
    with pytest.raises(jsonschema.ValidationError):
        VALIDATOR.validate(_row(endorsements=[]))


def test_schema_requires_prior_exposure_note_when_already_received():
    with pytest.raises(jsonschema.ValidationError):
        VALIDATOR.validate(_row(
            eligibility_status="already_received",
            consideration_status="already_received",
        ))
    VALIDATOR.validate(_row(
        eligibility_status="already_received",
        consideration_status="already_received",
        prior_exposure_note="4 cycles, best response PR, stopped for progression.",
    ))


def test_schema_requires_blocking_factors_when_ineligible():
    with pytest.raises(jsonschema.ValidationError):
        VALIDATOR.validate(_row(
            eligibility_status="contraindicated",
            consideration_status="not_applicable",
        ))
    VALIDATOR.validate(_row(
        eligibility_status="contraindicated",
        consideration_status="not_applicable",
        blocking_factors=["Grade 3 neuropathy on file."],
    ))


def test_schema_requires_gate_status_when_biomarker_required():
    with pytest.raises(jsonschema.ValidationError):
        VALIDATOR.validate(_row(
            consideration_status="requires_further_workup",
            biomarker_requirement={"required": True, "biomarker": "PD-L1"},
        ))
    VALIDATOR.validate(_row(
        consideration_status="requires_further_workup",
        biomarker_requirement={
            "required": True,
            "biomarker": "PD-L1",
            "threshold": "CPS >= 1",
            "status_in_case": "not_measured",
        },
    ))


def test_schema_rejects_last_verified_that_is_not_a_date():
    with pytest.raises(jsonschema.ValidationError):
        VALIDATOR.validate(_row(last_verified_utc="last spring"))


# ---------- renderer pre-flight ----------


def test_preflight_passes_on_clean_row():
    soc.preflight([_row()])  # must not raise


def test_preflight_blocks_em_dash_in_prose():
    rows = [_row(rationale="Guideline-preferred — and well tolerated.")]
    with pytest.raises(soc.BuildError, match="em-dash"):
        soc.preflight(rows)


def test_preflight_blocks_em_dash_in_narrative():
    with pytest.raises(soc.BuildError, match="em-dash"):
        soc.preflight([_row()], narrative="Two options remain — both are standard.")


def test_preflight_blocks_consider_now_behind_an_open_gate():
    """An option behind an unmeasured biomarker is not actionable yet. Presenting
    it as one overstates what the record supports."""
    rows = [_row(biomarker_requirement={
        "required": True,
        "biomarker": "PD-L1",
        "threshold": "CPS >= 1",
        "status_in_case": "not_measured",
    })]
    with pytest.raises(soc.BuildError, match="open biomarker gate"):
        soc.preflight(rows)


def test_preflight_allows_closed_gate():
    rows = [_row(biomarker_requirement={
        "required": True,
        "biomarker": "PD-L1",
        "threshold": "CPS >= 1",
        "status_in_case": "met",
    })]
    soc.preflight(rows)  # must not raise


def test_preflight_blocks_consider_now_on_already_received():
    """Re-offering a regimen the patient already progressed on is the most
    damaging error this page can make."""
    rows = [_row(
        eligibility_status="already_received",
        prior_exposure_note="6 cycles, progressed at 4 months.",
    )]
    with pytest.raises(soc.BuildError, match="contradicts eligibility_status"):
        soc.preflight(rows)


def test_preflight_blocks_consider_now_on_contraindicated():
    rows = [_row(eligibility_status="contraindicated", blocking_factors=["Grade 3 neuropathy."])]
    with pytest.raises(soc.BuildError, match="contradicts eligibility_status"):
        soc.preflight(rows)


def test_preflight_blocks_consider_now_with_only_extrapolated_endorsements():
    """An endorsement written for a different population is an extrapolation.
    Calling it standard of care for this patient is the unsafe failure."""
    rows = [_row(endorsements=[{
        "source": "NCCN",
        "designation": "Category 2A",
        "indication_text": "Limited-stage disease, concurrent chemoradiation.",
        "population_match": "different_population",
    }])]
    with pytest.raises(soc.BuildError, match="no endorsement covers this patient"):
        soc.preflight(rows)


def test_preflight_allows_partial_match_for_consider_now():
    """A partial match is a real, if hedged, basis; the agent names the
    discrepancy in the rationale rather than being blocked from reporting it."""
    rows = [_row(endorsements=[{
        "source": "ESMO",
        "designation": "I, A",
        "indication_text": "First line, ECOG 0-1.",
        "population_match": "partial_match",
    }])]
    soc.preflight(rows)


def test_preflight_blocks_missing_endorsement():
    with pytest.raises(soc.BuildError, match="not standard of care"):
        soc.preflight([_row(endorsements=[])])


def test_preflight_blocks_missing_verification_date():
    rows = [_row()]
    del rows[0]["last_verified_utc"]
    with pytest.raises(soc.BuildError, match="last_verified_utc"):
        soc.preflight(rows)


def test_preflight_blocks_already_received_without_note():
    rows = [_row(eligibility_status="already_received", consideration_status="already_received")]
    with pytest.raises(soc.BuildError, match="prior_exposure_note"):
        soc.preflight(rows)


# ---------- staleness ----------


def test_stale_row_is_flagged_but_does_not_block():
    old = (date.today() - timedelta(days=soc.STALE_AFTER_DAYS + 1)).isoformat()
    rows = [_row(last_verified_utc=old)]
    soc.preflight(rows)  # stale is a signal to the reader, not a build failure
    assert soc._is_stale(rows[0])
    assert "re-check" in soc.render_page("t", rows)


def test_fresh_row_is_not_flagged():
    assert not soc._is_stale(_row())
    assert "re-check" not in soc.render_page("t", [_row()])


# ---------- rendered output ----------


def test_page_states_the_track_is_additive():
    """The user-facing guarantee: a reader arriving from the ranking must not
    read this page as a filter on it."""
    page = soc.render_page("t", [_row()])
    assert "does not narrow" in page


def test_page_shows_population_match_next_to_the_endorsement():
    page = soc.render_page("t", [_row(endorsements=[{
        "source": "NCCN",
        "designation": "Category 2A",
        "indication_text": "Limited-stage disease.",
        "population_match": "different_population",
    }], consideration_status="not_applicable")])
    assert "different population" in page


def test_page_separates_already_received_from_actionable():
    rows = [
        _row(),
        _row(
            soc_id="cisplatin-etoposide-1l",
            option_label="Cisplatin + etoposide",
            eligibility_status="already_received",
            consideration_status="already_received",
            prior_exposure_note="4 cycles, progressed at 5 months.",
        ),
    ]
    page = soc.render_page("t", rows)
    assert "Options to consider now" in page
    assert "Already received" in page
    assert "progressed at 5 months" in page


def test_page_renders_gated_options_in_their_own_section():
    rows = [_row(
        consideration_status="requires_further_workup",
        biomarker_requirement={
            "required": True,
            "biomarker": "PD-L1",
            "threshold": "CPS >= 1",
            "status_in_case": "not_measured",
            "linked_survey_id": "pdl1-not-measured",
        },
    )]
    page = soc.render_page("t", rows)
    assert "behind an open gate" in page
    assert "never measured" in page


def test_sequencing_section_leads_with_the_trade_offs():
    """A reader scanning this section is looking for the decisions where taking
    one path costs the other, so those relations sort first."""
    rows = [
        _row(soc_id="a", option_label="A", relationship_to_targeted_options={
            "relation": "independent", "note": "No interaction."}),
        _row(soc_id="b", option_label="B", relationship_to_targeted_options={
            "relation": "may_foreclose_targeted_option",
            "note": "Prior platinum would close the trial's enrollment window.",
            "related_intervention_ids": ["tarlatamab"]}),
    ]
    out = soc.render_sequencing(rows)
    assert out.index("May foreclose") < out.index("Independent")
    assert "tarlatamab" in out


def test_sequencing_section_absent_when_no_row_is_linked():
    assert soc.render_sequencing([_row()]) == ""


def test_summary_counts_by_status():
    rows = [
        _row(),
        _row(soc_id="b", consideration_status="requires_further_workup"),
        _row(soc_id="c", eligibility_status="already_received",
             consideration_status="already_received",
             prior_exposure_note="Progressed."),
    ]
    summary = soc.compute_summary(rows)
    assert (summary["total"], summary["actionable"], summary["gated"], summary["received"]) == (3, 1, 1, 1)


def test_nav_links_only_pages_that_exist(tmp_path):
    (tmp_path / "index.md").write_text("x")
    page = soc.render_page("t", [_row()], case_docs=tmp_path)
    assert "[Back to case](index.md)" in page
    # recommendations.md was never rendered for this case; linking it would
    # break `mkdocs build --strict`.
    assert "(recommendations.md)" not in page


# --- Append-only corrections -----------------------------------------------
#
# accessibility.jsonl and standard_of_care.jsonl are append-only, so a correction
# arrives as a new row carrying `supersedes` rather than as an edit. Without the
# filter both rows render and a reader sees the stale eligibility call beside the
# corrected one, with nothing marking which is current. The standard_of_care
# schema carried the field from the start but nothing honoured it.

from libbylib import drop_superseded


def test_superseded_row_is_dropped():
    rows = [
        {"soc_id": "a", "option_label": "Old call"},
        {"soc_id": "b", "option_label": "Corrected call", "supersedes": "a"},
    ]
    kept = drop_superseded(rows, "soc_id")
    assert [r["soc_id"] for r in kept] == ["b"]


def test_no_supersedes_is_a_noop_and_preserves_order():
    rows = [{"soc_id": "a"}, {"soc_id": "b"}, {"soc_id": "c"}]
    assert drop_superseded(rows, "soc_id") == rows


def test_works_for_accessibility_row_id_key():
    rows = [
        {"row_id": "x", "intervention_id": "drug"},
        {"row_id": "x-v2", "intervention_id": "drug", "supersedes": "x"},
    ]
    kept = drop_superseded(rows, "row_id")
    assert len(kept) == 1 and kept[0]["row_id"] == "x-v2"


def test_rows_without_ids_are_kept():
    rows = [{"option_label": "no id"}, {"soc_id": "b", "supersedes": "a"}]
    assert len(drop_superseded(rows, "soc_id")) == 2


def test_chained_supersedes_keeps_only_the_newest():
    rows = [
        {"soc_id": "v1"},
        {"soc_id": "v2", "supersedes": "v1"},
        {"soc_id": "v3", "supersedes": "v2"},
    ]
    kept = drop_superseded(rows, "soc_id")
    assert [r["soc_id"] for r in kept] == ["v3"]
