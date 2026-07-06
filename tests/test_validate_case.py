"""Tests for scripts/validate_case.py — the schema gate over committed artifacts.

Covers the low-level validators against the real schemas in scripts/schema/,
plus an integration sweep asserting every committed case validates clean (guards
against future agent-output drift re-entering the tree).
"""

import json

import pytest

import validate_case as vc


# --- golden JSONL validation --------------------------------------------------

def _write_jsonl(tmp_path, rows):
    p = tmp_path / "rows.jsonl"
    p.write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")
    return p


def test_valid_positions_row_passes(tmp_path):
    row = {
        "persona": "risktaker",
        "case_slug": "demo",
        "written_at_utc": "2026-06-06T01:33:10Z",
        "picks": [],
        "abstain": True,
    }
    assert vc.validate_jsonl(_write_jsonl(tmp_path, [row]), "positions") == []


def test_positions_missing_required_field_fails(tmp_path):
    # `abstain` is required by positions.schema.json.
    row = {
        "persona": "risktaker",
        "case_slug": "demo",
        "written_at_utc": "2026-06-06T01:33:10Z",
        "picks": [],
    }
    errors = vc.validate_jsonl(_write_jsonl(tmp_path, [row]), "positions")
    assert errors and any("abstain" in e for e in errors)


def test_positions_bad_persona_enum_fails(tmp_path):
    row = {
        "persona": "consensusite",  # correct spelling — but code-canonical is concensusite
        "case_slug": "demo",
        "written_at_utc": "2026-06-06T01:33:10Z",
        "picks": [],
        "abstain": True,
    }
    errors = vc.validate_jsonl(_write_jsonl(tmp_path, [row]), "positions")
    assert errors and any("persona" in e for e in errors)


def test_runs_row_accepts_freeform_telemetry(tmp_path):
    # runs.schema.json pins `agent` but allows arbitrary extra keys.
    row = {"agent": "PI", "ts": "2026-06-06T01:33:10Z", "rows_appended": 4, "notes": "..."}
    assert vc.validate_jsonl(_write_jsonl(tmp_path, [row]), "runs") == []


def test_runs_row_rejects_lowercase_pi(tmp_path):
    row = {"agent": "pi"}
    errors = vc.validate_jsonl(_write_jsonl(tmp_path, [row]), "runs")
    assert errors and any("agent" in e for e in errors)


def test_blank_lines_ignored(tmp_path):
    p = tmp_path / "rows.jsonl"
    p.write_text('\n{"agent": "PI"}\n\n', encoding="utf-8")
    assert vc.validate_jsonl(p, "runs") == []


def test_malformed_json_reported(tmp_path):
    p = tmp_path / "rows.jsonl"
    p.write_text("{not valid json}\n", encoding="utf-8")
    errors = vc.validate_jsonl(p, "runs")
    assert errors and any("parse error" in e for e in errors)


# --- pmid / doi format gate (schema pattern) ----------------------------------

def _clin_row(**over):
    row = {
        "evidence_id": "e1",
        "case_slug": "demo",
        "intervention_id": "drugx",
        "intervention_label": "Drug X",
        "year": 2024,
    }
    row.update(over)
    return row


def _has_ref_error(errors):
    return any("pmid" in e or "doi" in e for e in errors)


def test_valid_pmid_and_doi_have_no_ref_error(tmp_path):
    # Row is intentionally minimal (other required fields may error) — we assert
    # only that a well-formed pmid/doi does NOT trip the format pattern.
    row = _clin_row(pmid="36720074", doi="10.1200/JCO.22.01616")
    assert not _has_ref_error(vc.validate_jsonl(_write_jsonl(tmp_path, [row]), "clinical_evidence"))


def test_null_pmid_and_doi_have_no_ref_error(tmp_path):
    row = _clin_row(pmid=None, doi=None)
    assert not _has_ref_error(vc.validate_jsonl(_write_jsonl(tmp_path, [row]), "clinical_evidence"))


def test_emdash_pmid_placeholder_fails(tmp_path):
    row = _clin_row(pmid="—")
    errors = vc.validate_jsonl(_write_jsonl(tmp_path, [row]), "clinical_evidence")
    assert errors and any("pmid" in e for e in errors)


def test_malformed_doi_fails(tmp_path):
    row = _clin_row(doi="https://doi.org/10.1200/JCO.22.01616")
    errors = vc.validate_jsonl(_write_jsonl(tmp_path, [row]), "clinical_evidence")
    assert errors and any("doi" in e for e in errors)


# --- integration: every committed case validates clean ------------------------

def _all_slugs():
    return sorted(p.name for p in vc.CASES_DIR.iterdir() if p.is_dir())


@pytest.mark.parametrize("slug", _all_slugs())
def test_committed_case_validates(slug):
    errors, _warnings = vc.validate_case(slug)
    assert errors == [], f"{slug} has schema errors:\n" + "\n".join(errors)
