"""Tests for scripts/check_pipeline.py — the pre-publish completeness gate.

Uses a synthetic case tree (via monkeypatched CASES_DIR/DOCS_DIR) so the checker
can be exercised on both a complete case and one missing a board persona,
without depending on repo data.
"""

import json

import check_pipeline as cp


PERSONAS = ["risktaker", "conservative", "critic", "concensusite", "advocate"]


def _build_case(root, docs, slug, *, positions_personas, critics_personas,
                include_translator=True):
    case = root / slug
    (case / "board").mkdir(parents=True)
    (case / "profile.json").write_text('{"case_slug": "%s"}' % slug)
    (case / "preferences.json").write_text('{"case_slug": "%s"}' % slug)
    for name in ("trials", "clinical_evidence", "preclinical_evidence",
                 "target_validation", "recommendations"):
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


def test_all_committed_cases_complete():
    # Every published case in the repo should pass the completeness gate.
    slugs = sorted(p.name for p in cp.CASES_DIR.iterdir() if p.is_dir())
    incomplete = {s: cp.check_pipeline(s)[0] for s in slugs}
    incomplete = {s: f for s, f in incomplete.items() if f}
    assert not incomplete, incomplete
