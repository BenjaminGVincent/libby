"""Tests for scripts/check_pipeline.py — the pre-publish completeness gate.

Uses a synthetic case tree (via monkeypatched CASES_DIR/DOCS_DIR) so the checker
can be exercised on both a complete case and one missing a board persona,
without depending on repo data.
"""

import json

import check_pipeline as cp


PERSONAS = ["risktaker", "conservative", "critic", "concensusite", "advocate"]


def _build_case(root, docs, slug, *, positions_personas, critics_personas,
                include_translator=True, include_accessibility=True):
    case = root / slug
    (case / "board").mkdir(parents=True)
    (case / "profile.json").write_text('{"case_slug": "%s"}' % slug)
    (case / "preferences.json").write_text('{"case_slug": "%s"}' % slug)
    names = ["trials", "clinical_evidence", "preclinical_evidence",
             "target_validation", "recommendations"]
    if include_accessibility:
        names.append("accessibility")
    for name in names:
        (case / f"{name}.jsonl").write_text('{"case_slug": "%s"}\n' % slug)
    (case / "board" / "positions.jsonl").write_text(
        "\n".join(json.dumps({"persona": p}) for p in positions_personas) + "\n"
    )
    # critiques: each critic targets one other persona (no self-critique)
    rows = []
    for c in critics_personas:
        target = next(p for p in PERSONAS if p != c)
        rows.append({"critic_persona": c, "target_persona": target})
    (case / "board" / "critiques.jsonl").write_text(
        "\n".join(json.dumps(r) for r in rows) + "\n"
    )
    d = docs / slug
    d.mkdir(parents=True)
    (d / "index.md").write_text("# index")
    if include_translator:
        (d / "plain_language.md").write_text("# plain")


def _patch(monkeypatch, tmp_path):
    root = tmp_path / "data" / "cases"
    docs = tmp_path / "docs" / "cases"
    root.mkdir(parents=True)
    docs.mkdir(parents=True)
    monkeypatch.setattr(cp, "CASES_DIR", root)
    monkeypatch.setattr(cp, "DOCS_DIR", docs)
    monkeypatch.setattr(cp, "REPO", tmp_path)
    return root, docs


def test_complete_case_passes(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "good", positions_personas=PERSONAS, critics_personas=PERSONAS)
    failures, _notes = cp.check_pipeline("good")
    assert failures == [], failures


def test_missing_board_persona_fails(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "bad", positions_personas=PERSONAS[:-1], critics_personas=PERSONAS)
    failures, _notes = cp.check_pipeline("bad")
    assert any("board round 1" in f for f in failures)


def test_missing_translator_fails(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "notrans", positions_personas=PERSONAS,
                critics_personas=PERSONAS, include_translator=False)
    failures, _notes = cp.check_pipeline("notrans")
    assert any("translator" in f for f in failures)


def test_self_critique_flagged(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "selfcrit", positions_personas=PERSONAS, critics_personas=PERSONAS)
    # inject a self-critique row
    cri = root / "selfcrit" / "board" / "critiques.jsonl"
    cri.write_text(cri.read_text() + json.dumps({"critic_persona": "critic", "target_persona": "critic"}) + "\n")
    failures, _notes = cp.check_pipeline("selfcrit")
    assert any("self-critique" in f for f in failures)


def test_missing_accessibility_fails_for_real_case(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "noaccess", positions_personas=PERSONAS,
                critics_personas=PERSONAS, include_accessibility=False)
    failures, _notes = cp.check_pipeline("noaccess")
    assert any("accessibility" in f for f in failures)


def test_demo_slug_exempt_from_accessibility(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "demo-thing", positions_personas=PERSONAS,
                critics_personas=PERSONAS, include_accessibility=False)
    failures, _notes = cp.check_pipeline("demo-thing")
    assert failures == [], failures


def test_malformed_jsonl_does_not_crash(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "bad", positions_personas=PERSONAS, critics_personas=PERSONAS)
    # a malformed board line must yield a clean failure, not a JSONDecodeError traceback
    pos = root / "bad" / "board" / "positions.jsonl"
    pos.write_text(pos.read_text() + "{not valid json\n")
    failures, _notes = cp.check_pipeline("bad")  # must not raise
    assert isinstance(failures, list)


def test_structurally_empty_profile_fails(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "emptyjson", positions_personas=PERSONAS, critics_personas=PERSONAS)
    (root / "emptyjson" / "profile.json").write_text("{}")  # non-zero bytes, no content
    failures, _notes = cp.check_pipeline("emptyjson")
    assert any("profile.json" in f for f in failures)


def test_all_committed_cases_complete():
    # Every published case in the repo should pass the completeness gate.
    slugs = sorted(p.name for p in cp.CASES_DIR.iterdir() if p.is_dir())
    incomplete = {s: cp.check_pipeline(s)[0] for s in slugs}
    incomplete = {s: f for s, f in incomplete.items() if f}
    assert not incomplete, incomplete


# --- Two-table coverage ----------------------------------------------------
#
# The landscape splits across the Experimental ranking and the standard-of-care
# screen. Which table a therapy lands in is the PI's call; vanishing from both
# is not. These exercise the union check, not either table alone.


def _write_soc(case, options):
    (case / "standard_of_care.jsonl").write_text(
        "\n".join(json.dumps({"soc_id": sid, "option_label": lab})
                  for sid, lab in options) + "\n"
    )


def _write_recs(case, rows):
    (case / "recommendations.jsonl").write_text(
        "\n".join(json.dumps(r) for r in rows) + "\n"
    )


def _write_evidence(case, items, fname="clinical_evidence.jsonl"):
    (case / fname).write_text(
        "\n".join(json.dumps({"intervention_id": i, "intervention_label": lab})
                  for i, lab in items) + "\n"
    )


def test_therapy_in_neither_table_fails(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "c", positions_personas=PERSONAS, critics_personas=PERSONAS)
    case = root / "c"
    _write_evidence(case, [("chemo", "Doxorubicin-based chemotherapy")])
    _write_soc(case, [("soc-rt", "Palliative radiotherapy")])
    _write_recs(case, [{"intervention_id": "glutaminase",
                        "intervention_label": "IACS-6274",
                        "access_route": "clinical_trial_only"}])
    failures, _ = cp.check_pipeline("c")
    assert any("table coverage" in f for f in failures), failures
    assert any("chemo" in f for f in failures), failures


def test_therapy_routed_to_standard_of_care_passes(monkeypatch, tmp_path):
    """Routing is a filing decision, not an omission: a therapy that lives only
    on the standard-of-care table is covered."""
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "c", positions_personas=PERSONAS, critics_personas=PERSONAS)
    case = root / "c"
    _write_evidence(case, [("chemo", "Doxorubicin-based chemotherapy")])
    _write_soc(case, [("chemo", "Doxorubicin-based chemotherapy")])
    _write_recs(case, [{"intervention_id": "glutaminase",
                        "intervention_label": "IACS-6274",
                        "access_route": "clinical_trial_only"}])
    failures, _ = cp.check_pipeline("c")
    assert not any("table coverage" in f for f in failures), failures


def test_therapy_in_experimental_table_passes(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "c", positions_personas=PERSONAS, critics_personas=PERSONAS)
    case = root / "c"
    _write_evidence(case, [("glutaminase", "IACS-6274")])
    _write_recs(case, [{"intervention_id": "glutaminase",
                        "intervention_label": "IACS-6274",
                        "access_route": "clinical_trial_only"}])
    failures, _ = cp.check_pipeline("c")
    assert not any("table coverage" in f for f in failures), failures


def test_coverage_matches_on_label_stem_across_tracks(monkeypatch, tmp_path):
    """The two tracks assign their own IDs, so a label-stem match counts."""
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "c", positions_personas=PERSONAS, critics_personas=PERSONAS)
    case = root / "c"
    _write_evidence(case, [("surgery-primary-site", "Orthopaedic stabilisation of the acetabulum")])
    _write_soc(case, [("soc-fix", "Orthopaedic stabilisation (fixation) of the fracture")])
    _write_recs(case, [{"intervention_id": "x", "intervention_label": "Other",
                        "access_route": "off_label_use"}])
    failures, _ = cp.check_pipeline("c")
    assert not any("table coverage" in f for f in failures), failures


def test_coverage_matches_any_evidence_label_for_an_intervention(monkeypatch, tmp_path):
    """An evidence tier files several rows under one intervention_id with
    different labels. If ANY of them stem-matches a table row, the therapy is
    covered — matching only the first label falsely flagged a routed therapy
    whose lead evidence row was phrased differently ("Anthracycline-based
    chemotherapy" vs the SoC table's "Doxorubicin-based chemotherapy")."""
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "c", positions_personas=PERSONAS, critics_personas=PERSONAS)
    case = root / "c"
    _write_evidence(case, [
        ("cytotoxic-chemotherapy", "Anthracycline-based chemotherapy (advanced chondrosarcoma)"),
        ("cytotoxic-chemotherapy", "Doxorubicin / cisplatin with BH3 mimetic ABT-737"),
    ])
    _write_soc(case, [("doxorubicin-1l", "Doxorubicin-based chemotherapy (doxorubicin alone or with ifosfamide or cisplatin)")])
    _write_recs(case, [{"intervention_id": "glutaminase", "intervention_label": "IACS-6274",
                        "access_route": "clinical_trial_only"}])
    failures, _ = cp.check_pipeline("c")
    assert not any("table coverage" in f for f in failures), failures


def test_legacy_case_without_access_route_is_not_gated(monkeypatch, tmp_path):
    """Cases ranked before this check keep passing."""
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "c", positions_personas=PERSONAS, critics_personas=PERSONAS)
    case = root / "c"
    _write_evidence(case, [("chemo", "Doxorubicin-based chemotherapy")])
    _write_recs(case, [{"intervention_id": "glutaminase", "intervention_label": "IACS-6274"}])
    failures, _ = cp.check_pipeline("c")
    assert not any("table coverage" in f for f in failures), failures


# --- Per-table rank sequences ---------------------------------------------
#
# Each table numbers itself 1..n independently of the other: they are co-equal
# tables, not one list split in two. A gap or duplicate makes the sequence
# unreadable as a ranking, and a table starting at 2 implies a missing top row.


def _ranked_recs(case, ranks):
    _write_recs(case, [{"intervention_id": f"i{n}", "intervention_label": f"Drug {n}",
                        "access_route": "clinical_trial_only", "rank": n} for n in ranks])


def test_contiguous_ranks_pass(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "c", positions_personas=PERSONAS, critics_personas=PERSONAS)
    _ranked_recs(root / "c", [1, 2, 3])
    failures, _ = cp.check_pipeline("c")
    assert not any("ranks are not" in f for f in failures), failures


def test_rank_gap_fails(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "c", positions_personas=PERSONAS, critics_personas=PERSONAS)
    _ranked_recs(root / "c", [1, 2, 4])
    failures, _ = cp.check_pipeline("c")
    assert any("ranks are not" in f and "missing rank" in f for f in failures), failures


def test_duplicate_rank_fails(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "c", positions_personas=PERSONAS, critics_personas=PERSONAS)
    _ranked_recs(root / "c", [1, 2, 2])
    failures, _ = cp.check_pipeline("c")
    assert any("duplicate rank" in f for f in failures), failures


def test_ranking_must_not_start_above_one(monkeypatch, tmp_path):
    """A table beginning at 2 reads as though its top row was lost."""
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "c", positions_personas=PERSONAS, critics_personas=PERSONAS)
    _ranked_recs(root / "c", [2, 3, 4])
    failures, _ = cp.check_pipeline("c")
    assert any("ranks are not" in f for f in failures), failures


def test_two_tables_rank_independently(monkeypatch, tmp_path):
    """Both tables starting at 1 is correct, not a collision: the standard-of-care
    ranking is not a continuation of the experimental one."""
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "c", positions_personas=PERSONAS, critics_personas=PERSONAS)
    case = root / "c"
    _ranked_recs(case, [1, 2, 3])
    (case / "standard_of_care.jsonl").write_text(
        "\n".join(json.dumps({"soc_id": f"s{n}", "option_label": f"Standard {n}", "rank": n})
                  for n in (1, 2)) + "\n"
    )
    failures, _ = cp.check_pipeline("c")
    assert not any("ranks are not" in f for f in failures), failures


def test_partially_ranked_table_fails(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "c", positions_personas=PERSONAS, critics_personas=PERSONAS)
    case = root / "c"
    _write_recs(case, [
        {"intervention_id": "a", "intervention_label": "A", "access_route": "off_label_use", "rank": 1},
        {"intervention_id": "b", "intervention_label": "B", "access_route": "off_label_use"},
    ])
    failures, _ = cp.check_pipeline("c")
    assert any("rank the whole table or none of it" in f for f in failures), failures


def test_unranked_legacy_screen_is_not_gated(monkeypatch, tmp_path):
    root, docs = _patch(monkeypatch, tmp_path)
    _build_case(root, docs, "c", positions_personas=PERSONAS, critics_personas=PERSONAS)
    case = root / "c"
    _write_recs(case, [{"intervention_id": "a", "intervention_label": "A",
                        "access_route": "off_label_use"}])
    _write_soc(case, [("s1", "Standard one"), ("s2", "Standard two")])
    failures, _ = cp.check_pipeline("c")
    assert not any("ranks are not" in f for f in failures), failures
