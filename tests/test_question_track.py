"""Tests for the question-scoped track: schemas, completeness gate, and renderer.

A question run does the same research and tumor-board work as a full case but is
scoped to one question instead of a target set. These tests pin the three
contracts that make that safe:

  1. `question.json` presence routes check_pipeline.py to the question rules, so
     a question case is never judged against the feature-ranking artifact map.
  2. The board is NOT relaxed for a question run — five personas, two rounds.
  3. The renderer refuses to publish an answer whose audit trail is broken:
     a drifted question, unreported pre-registered criteria, a missing scope
     caveat, or an answer shape upgraded past the framer's read.
"""

import json

import jsonschema
import pytest

import check_pipeline as cp
import build_question as bq

from pathlib import Path

SCHEMA_DIR = Path(__file__).resolve().parent.parent / "scripts" / "schema"


def _schema(name):
    return json.loads((SCHEMA_DIR / f"{name}.schema.json").read_text())


PERSONAS = ["risktaker", "conservative", "critic", "concensusite", "advocate"]

QUESTION = "Is there a case for adding maintenance olaparib at first progression?"


def _question(**over):
    q = {
        "question_id": "add-olaparib-maintenance",
        "case_slug": "q-demo",
        "question": QUESTION,
        "asked_as": None,
        "interpretation_notes": None,
        "question_type": "intervention",
        "decision_context": "Treating oncologist deciding the maintenance plan.",
        "in_scope": ["PARP inhibitors in this histology"],
        "out_of_scope": ["The rest of the therapeutic landscape"],
        "acceptance_criteria": [
            {"criterion": "A randomized trial in this histology", "would_support": "yes", "found": None},
            {"criterion": "A negative confirmatory trial", "would_support": "no", "found": None},
        ],
        "answer_shape": "verdict",
        "source_case_slug": None,
        "inherited_context": None,
        "framed_at_utc": "2026-08",
        "notes": None,
    }
    q.update(over)
    return q


def _answer(**over):
    a = {
        "question_id": "add-olaparib-maintenance",
        "case_slug": "q-demo",
        "question": QUESTION,
        "verdict": "insufficient_evidence",
        "confidence": "low",
        "answer": "The evidence does not reach this question in this histology.",
        "evidence_for": [],
        "evidence_against": [{"claim": "No randomized data", "strength": "moderate"}],
        "acceptance_criteria_result": [
            {"criterion": "A randomized trial in this histology", "met": False, "finding": "None found."},
            {"criterion": "A negative confirmatory trial", "met": None, "finding": "Not determinable."},
        ],
        "what_would_change_it": ["A randomized readout in this histology"],
        "board_dissent": [],
        "scope_caveat": "Only PARP maintenance was assessed.",
        "answer_shape_used": "verdict",
        "answered_at_utc": "2026-08",
        "notes": None,
    }
    a.update(over)
    return a


# ---------------------------------------------------------------- completeness


def _patch(monkeypatch, tmp_path):
    root = tmp_path / "data" / "cases"
    docs = tmp_path / "docs" / "cases"
    root.mkdir(parents=True)
    docs.mkdir(parents=True)
    monkeypatch.setattr(cp, "CASES_DIR", root)
    monkeypatch.setattr(cp, "DOCS_DIR", docs)
    monkeypatch.setattr(cp, "REPO", tmp_path)
    return root, docs


def _build_question_case(root, docs, slug, *, question=None, answer=None,
                         critics=None, with_recommendations=False,
                         with_profile=False):
    case = root / slug
    (case / "board").mkdir(parents=True)
    (case / "question.json").write_text(json.dumps(question or _question()))
    (case / "question_answer.json").write_text(json.dumps(answer or _answer()))
    for name in ["trials", "clinical_evidence", "preclinical_evidence"]:
        (case / f"{name}.jsonl").write_text('{"case_slug": "%s"}\n' % slug)
    if with_recommendations:
        (case / "recommendations.jsonl").write_text('{"case_slug": "%s"}\n' % slug)
    if with_profile:
        (case / "profile.json").write_text('{"case_slug": "%s"}' % slug)
    (case / "board" / "positions.jsonl").write_text(
        "\n".join(json.dumps({"persona": p}) for p in PERSONAS) + "\n"
    )
    rows = []
    for c in (critics if critics is not None else PERSONAS):
        target = next(p for p in PERSONAS if p != c)
        rows.append({"critic_persona": c, "target_persona": target})
    (case / "board" / "critiques.jsonl").write_text(
        "\n".join(json.dumps(r) for r in rows) + "\n"
    )
    d = docs / slug
    d.mkdir(parents=True)
    (d / "question.md").write_text("# question report")


def test_question_case_passes_without_feature_ranking_artifacts(monkeypatch, tmp_path):
    """The whole point: no target_validation, no accessibility, no
    recommendations, no plain_language, no index.md — and it still passes."""
    root, docs = _patch(monkeypatch, tmp_path)
    _build_question_case(root, docs, "q-demo")
    failures, _ = cp.check_pipeline("q-demo")
    assert failures == [], failures


def test_question_case_does_not_use_full_case_rules(monkeypatch, tmp_path):
    """A full case missing those artifacts fails; the question case above does
    not. Pins that the branch actually branches."""
    root, docs = _patch(monkeypatch, tmp_path)
    _build_question_case(root, docs, "q-demo")
    (root / "q-demo" / "question.json").unlink()
    failures, _ = cp.check_pipeline("q-demo")
    assert failures, "without question.json this must fall back to full-case rules"


def test_board_is_not_relaxed_for_questions(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    _build_question_case(root, docs, "q-demo", critics=PERSONAS[:3])
    failures, _ = cp.check_pipeline("q-demo")
    assert any("round 2" in f for f in failures), failures


def test_option_shaped_answer_requires_recommendations(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    _build_question_case(
        root, docs, "q-demo",
        answer=_answer(answer_shape_used="verdict_plus_ranked_options"),
    )
    failures, _ = cp.check_pipeline("q-demo")
    assert any("ranked options" in f for f in failures), failures

    _patch(monkeypatch, tmp_path / "second")
    root2 = tmp_path / "second" / "data" / "cases"
    docs2 = tmp_path / "second" / "docs" / "cases"
    _build_question_case(
        root2, docs2, "q-demo",
        answer=_answer(answer_shape_used="verdict_plus_ranked_options"),
        with_recommendations=True,
    )
    failures2, _ = cp.check_pipeline("q-demo")
    assert failures2 == [], failures2


def test_linked_question_requires_a_resolvable_source(monkeypatch, tmp_path):
    """A linked question inherits the source case's profile in place. Pointing at
    a case that does not exist is the failure, not the absence of a local copy —
    a required local file would be one no agent owns."""
    root, docs = _patch(monkeypatch, tmp_path)
    _build_question_case(
        root, docs, "q-demo",
        question=_question(source_case_slug="no-such-case"),
    )
    failures, _ = cp.check_pipeline("q-demo")
    assert any("linked source" in f for f in failures), failures


def test_linked_question_passes_when_source_resolves(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    src = root / "published-case"
    src.mkdir(parents=True)
    (src / "profile.json").write_text('{"case_slug": "published-case"}')
    _build_question_case(
        root, docs, "q-demo",
        question=_question(source_case_slug="published-case"),
    )
    failures, _ = cp.check_pipeline("q-demo")
    assert failures == [], failures


def test_linked_question_needs_no_local_profile_copy(monkeypatch, tmp_path):
    """No PHI-derived data is duplicated into the question tree."""
    root, docs = _patch(monkeypatch, tmp_path)
    src = root / "published-case"
    src.mkdir(parents=True)
    (src / "profile.json").write_text('{"case_slug": "published-case"}')
    _build_question_case(
        root, docs, "q-demo",
        question=_question(source_case_slug="published-case"),
    )
    assert not (root / "q-demo" / "profile.json").exists()
    failures, _ = cp.check_pipeline("q-demo")
    assert failures == [], failures


def test_standalone_question_needs_no_profile(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    _build_question_case(root, docs, "q-demo")
    failures, _ = cp.check_pipeline("q-demo")
    assert not any("profile" in f for f in failures), failures


# -------------------------------------------------------------------- renderer


def test_preflight_accepts_a_clean_answer():
    bq.preflight(_question(), _answer(), "A narrative with no em dash.")


def test_preflight_rejects_drifted_question():
    with pytest.raises(SystemExit):
        bq.preflight(_question(), _answer(question="A different question entirely?"), "")


def test_preflight_rejects_unreported_criteria():
    """The audit trail that the answer was not assembled backwards."""
    bad = _answer(acceptance_criteria_result=[
        {"criterion": "A randomized trial in this histology", "met": False, "finding": "None."}
    ])
    with pytest.raises(SystemExit):
        bq.preflight(_question(), bad, "")


def test_preflight_rejects_missing_scope_caveat():
    with pytest.raises(SystemExit):
        bq.preflight(_question(), _answer(scope_caveat="  "), "")


def test_preflight_rejects_upgraded_answer_shape():
    """The synthesist may downgrade the framer's read, never upgrade it."""
    with pytest.raises(SystemExit):
        bq.preflight(
            _question(answer_shape="verdict"),
            _answer(answer_shape_used="verdict_plus_ranked_options", notes=None),
            "",
        )


def test_insufficient_evidence_does_not_get_a_positive_badge():
    """A reader skimming for a green badge must not read 'we could not answer
    this' as a soft yes."""
    assert bq.VERDICT_CLASS["insufficient_evidence"] != bq.VERDICT_CLASS["yes"]
    assert bq.VERDICT_CLASS["qualified_no"] == bq.VERDICT_CLASS["no"]


def test_unmet_criteria_still_render():
    html = bq.render_criteria_table(_question(), _answer())
    assert "Not met" in html and "Undetermined" in html


def test_page_leads_with_verdict_and_carries_scope():
    page = bq.render_page("q-demo", _question(), _answer(), "Narrative here.")
    assert page.index("Insufficient evidence") < page.index("Narrative here.")
    assert "Only PARP maintenance was assessed." in page


def test_candidates_table_precedes_the_prose():
    """A reader comes to a question report for the options and their numbers.
    The verdict is one line at the top; the table follows it, and the narrative
    explains the table rather than delaying it."""
    ans = _answer(candidates=[_candidate()], ranking_basis="eligibility and population match")
    page = bq.render_page("q-demo", _question(), ans, "Narrative here.")
    assert page.index("Candidates assessed") < page.index("Narrative here.")
    assert page.index("Insufficient evidence") < page.index("Candidates assessed")
    # The basis caveat travels with the table, so the table is never stranded.
    assert page.index("What this ranking orders by") < page.index("Narrative here.")


# --------------------------------------------------------------------- schemas


def test_fixtures_validate_against_their_schemas():
    """A schema nothing validates against is decoration. Pin that the fixtures
    these tests reason over are the shape the agents are told to write."""
    jsonschema.validate(_question(), _schema("question"))
    jsonschema.validate(_answer(), _schema("question_answer"))


def test_schema_refuses_freeform_verdict():
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(_answer(verdict="probably"), _schema("question_answer"))


def test_schema_requires_scope_caveat():
    bad = _answer()
    del bad["scope_caveat"]
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, _schema("question_answer"))


def test_schema_requires_at_least_one_acceptance_criterion():
    """Pre-registered criteria are the track's guard against motivated
    reasoning, so an empty list must not validate."""
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(_question(acceptance_criteria=[]), _schema("question"))


# ------------------------------------------------------------ candidates table


def _candidate(**over):
    c = {
        "rank": 1,
        "label": "CLAG-GO (NCT04050280)",
        "response_rate": {"value": "58%", "endpoint": "CR (true)", "n": "66/114",
                          "ci": None, "population_match": "pre-venetoclax, no post-allo subgroup"},
        "toxicity": {"summary": "High (45% severe infection, 7% early death)",
                     "key_rates": [], "population_match": None},
        "deliverable": "trial_only",
        "references": ["pmid:18076637", "NCT04050280"],
        "notes": None,
    }
    c.update(over)
    return c


def test_candidates_table_renders_on_a_negative_verdict():
    """The evidence behind a 'no' is what the reader needs most. Dropping the
    table because the answer was unfavourable hides the reasoning."""
    ans = _answer(verdict="no", candidates=[_candidate()],
                  ranking_basis="eligibility and population match, not demonstrated CR probability")
    html = bq.render_candidates_table(ans)
    assert "CLAG-GO" in html
    assert "58%" in html and "CR (true)" in html
    assert "45% severe infection" in html
    assert "18076637" in html
    page = bq.render_page("q-demo", _question(), ans, "")
    assert "Candidates assessed" in page


def test_candidate_rate_must_carry_its_endpoint():
    """A composite rate is not a CR rate."""
    bad = _candidate(response_rate={"value": "75%", "endpoint": None, "n": "41/55",
                                    "ci": None, "population_match": None})
    with pytest.raises(SystemExit):
        bq.preflight(_question(), _answer(candidates=[bad], ranking_basis="magnitude"), "")


def test_ranked_candidates_require_a_stated_basis():
    with pytest.raises(SystemExit):
        bq.preflight(_question(), _answer(candidates=[_candidate()], ranking_basis=""), "")


def test_ranking_basis_required_by_schema_when_candidates_exist():
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(_answer(candidates=[_candidate()]), _schema("question_answer"))
    jsonschema.validate(
        _answer(candidates=[_candidate()], ranking_basis="eligibility and population match"),
        _schema("question_answer"),
    )


def test_deliverability_is_visible_in_the_table():
    """The best-evidenced candidate is often the one with no route."""
    ans = _answer(candidates=[_candidate(deliverable="no", label="Lintuzumab-Ac225 + CLAG-M")],
                  ranking_basis="mechanism fit")
    html = bq.render_candidates_table(ans)
    assert "Not deliverable" in html


def test_no_candidates_means_no_table():
    assert bq.render_candidates_table(_answer()) == ""
