"""Tests for the two-table Experimental recommendations rendering.

Covers the `surfaced_reason` grouping/flagging added for the Standard-of-care +
Experimental split: the on-site markdown renderer (build_recommendations.py) and
the self-contained HTML/PDF renderer (build_report.py) must partition rows into
workup / ranked / also-considered, flag the also-considered rows by reason, and
apply the (previously dead) status CSS class.
"""

import build_recommendations as br
import build_report as rp


def _rows():
    return [
        {"rank": 1, "scenario": "shared", "intervention_label": "HLA workup",
         "status": "recommended"},
        {"rank": 2, "intervention_label": "Iomab-B", "status": "recommended",
         "surfaced_reason": "none"},
        {"rank": 3, "intervention_label": "HA-1 TCR-T", "status": "recommended",
         "scenario": "hla_a0201:positive"},
        {"rank": 4, "intervention_label": "Flotetuzumab",
         "status": "considered_with_caveats", "surfaced_reason": "unavailable"},
        {"rank": 5, "intervention_label": "TSC-100",
         "status": "considered_with_caveats", "surfaced_reason": "consolidated"},
        {"rank": 6, "intervention_label": "Rezatapopt",
         "status": "considered_with_caveats", "surfaced_reason": "thin_evidence"},
    ]


# --- grouping ---------------------------------------------------------------

def test_group_three_way_partition():
    workup, ranked, also = br.group_by_scenario(_rows())
    assert [r["intervention_label"] for r in workup] == ["HLA workup"]
    assert [r["intervention_label"] for r in ranked] == ["Iomab-B", "HA-1 TCR-T"]
    assert [r["intervention_label"] for r in also] == ["Flotetuzumab", "TSC-100", "Rezatapopt"]


def test_backward_compat_no_surfaced_reason():
    # Legacy rows (no surfaced_reason) all land in ranked; also-considered empty.
    rows = [{"rank": 1, "intervention_label": "A", "status": "recommended"},
            {"rank": 2, "intervention_label": "B", "status": "not_recommended"}]
    workup, ranked, also = br.group_by_scenario(rows)
    assert not workup and not also
    assert len(ranked) == 2


# --- flag rendering ---------------------------------------------------------

def test_md_flagged_table_has_flag_column_and_badges():
    _, _, also = br.group_by_scenario(_rows())
    tbl = br.render_recs_table(also, flagged=True)
    assert "<th>Flag</th>" in tbl
    for cls in ("flag-unavailable", "flag-consolidated", "flag-thin"):
        assert cls in tbl


def test_md_status_class_now_applied():
    tbl = br.render_recs_table([{"intervention_label": "X", "status": "not_recommended"}])
    assert 'class="not-recommended"' in tbl


def test_html_flagged_table_has_flag_column_and_badges():
    _, _, also = br.group_by_scenario(_rows())
    tbl = rp._render_recs_table_html(also, flagged=True)
    assert "<th>Flag</th>" in tbl
    for cls in ("flag-unavailable", "flag-consolidated", "flag-thin"):
        assert cls in tbl


def test_html_status_class_now_applied():
    tbl = rp._render_recs_table_html(
        [{"intervention_label": "X", "status": "not_recommended"}])
    assert 'class="not-recommended"' in tbl


def test_surfaced_only_predicate():
    assert br._is_surfaced_only({"surfaced_reason": "unavailable"}) is True
    assert br._is_surfaced_only({"surfaced_reason": "none"}) is False
    assert br._is_surfaced_only({}) is False
    assert rp._is_surfaced_only({"surfaced_reason": "consolidated"}) is True


# --- Access column ---------------------------------------------------------
#
# Under the unified-table contract the ranked table carries standard-of-care
# therapies alongside investigational ones, so a reader can no longer infer
# "experimental" from a therapy merely being present. The Access column is what
# carries that distinction, which makes its presence load-bearing rather than
# decorative.


def test_access_column_in_both_headers():
    assert "<th>Access</th>" in br.RECS_HEAD
    assert "<th>Access</th>" in br.RECS_HEAD_FLAGGED


def test_access_badge_renders_standard_care_distinctly():
    soc = br.access_badge("standard_of_care")
    trial = br.access_badge("clinical_trial_only")
    assert "Standard care" in soc
    assert "Trial only" in trial
    assert soc != trial


def test_access_badge_absent_renders_placeholder_not_error():
    """Cases ranked before the unified change carry no access_route; that is an
    expected state, not a failure."""
    assert br.access_badge(None) == "<td>—</td>"


def test_access_cell_present_for_every_rendered_row():
    rows = [
        {"rank": 1, "intervention_label": "Doxorubicin", "access_route": "standard_of_care"},
        {"rank": 2, "intervention_label": "IACS-6274", "access_route": "clinical_trial_only"},
    ]
    html_out = br.render_recs_table(rows)
    assert html_out.count("rel-badge") == 2
    assert "Standard care" in html_out and "Trial only" in html_out
    # header column count must match the body cell count
    assert br.RECS_HEAD.count("<th>") == html_out.split("<tbody>")[1].split("</tr>")[0].count("<td>")
