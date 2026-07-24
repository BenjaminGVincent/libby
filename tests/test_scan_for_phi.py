"""Tests for scripts/scan_for_phi.py — the PHI tripwire.

This scanner is the automated defense on the PHI boundary (pre-commit hook +
CI tree scan). It was previously untested. These tests pin the detector shapes,
the oncology-acronym allowlist, the by-design suppression, the ignore token,
and the main() exit codes.
"""

import scan_for_phi as phi


def _write(tmp_path, name, text):
    p = tmp_path / name
    p.write_text(text, encoding="utf-8")
    return p


def _labels(hits):
    return {label for _lineno, label, _desc, _line in hits}


# --- positive detections: each PHI shape must be caught -----------------------

def test_ssn_detected(tmp_path):
    hits = phi.scan_file(_write(tmp_path, "note.md", "SSN is 123-45-6789 here"))
    assert "ssn" in _labels(hits)


def test_us_phone_detected(tmp_path):
    hits = phi.scan_file(_write(tmp_path, "note.md", "call 415-555-1234 now"))
    assert "us_phone" in _labels(hits)


def test_email_detected(tmp_path):
    hits = phi.scan_file(_write(tmp_path, "note.md", "email jane.doe@example.com"))
    assert "email" in _labels(hits)


def test_labeled_mrn_detected(tmp_path):
    hits = phi.scan_file(_write(tmp_path, "note.md", "MRN: A1234567"))
    assert "mrn_label" in _labels(hits)


def test_iso_date_detected(tmp_path):
    hits = phi.scan_file(_write(tmp_path, "note.md", "resected 2024-03-15 status post"))
    assert "iso_date_full" in _labels(hits)


def test_us_date_detected(tmp_path):
    hits = phi.scan_file(_write(tmp_path, "note.md", "seen 03/15/2024 in clinic"))
    assert "us_date" in _labels(hits)


def test_dob_label_detected(tmp_path):
    hits = phi.scan_file(_write(tmp_path, "note.md", "D.O.B. redacted"))
    assert "dob_label" in _labels(hits)


def test_all_caps_name_detected(tmp_path):
    hits = phi.scan_file(_write(tmp_path, "note.md", "SMITH, JOHN is the patient"))
    assert "all_caps_name" in _labels(hits)


def test_patient_name_label_detected(tmp_path):
    hits = phi.scan_file(_write(tmp_path, "note.md", "Patient name: withheld"))
    assert "patient_label" in _labels(hits)


# --- negatives: benign oncology text must not trip the tripwire ---------------

def test_mrna_not_flagged_as_mrn(tmp_path):
    # mRNA-4203 (lowercase m, embedded RNA) must not match the MRN label.
    hits = phi.scan_file(_write(tmp_path, "note.md", "mRNA-4203 vaccine cohort"))
    assert "mrn_label" not in _labels(hits)


def test_month_year_not_flagged(tmp_path):
    # Month-precision dates are the approved shape and must not match.
    hits = phi.scan_file(_write(tmp_path, "note.md", "progressed 2024-03 on osimertinib"))
    assert "iso_date_full" not in _labels(hits)


def test_allowlisted_acronym_pair_not_flagged(tmp_path):
    hits = phi.scan_file(_write(tmp_path, "note.md", "per NCCN, ESMO guidelines"))
    assert "all_caps_name" not in _labels(hits)


def test_society_acronym_run_not_flagged(tmp_path):
    """The standard-of-care screener names its endorsing bodies in runs, which
    read as NAME, NAME pairs unless every society is allowlisted."""
    text = "carried by NCCN, ESMO, ASCO, ASH, EHA, ASTRO, SITC, AUA, AASLD"
    hits = phi.scan_file(_write(tmp_path, "note.md", text))
    assert "all_caps_name" not in _labels(hits)


def test_mixed_acronym_and_name_pair_is_flagged(tmp_path):
    # One token allowlisted, the other a plausible surname -> still PHI.
    hits = phi.scan_file(_write(tmp_path, "note.md", "reviewed by NCCN, KOWALSKI"))
    assert "all_caps_name" in _labels(hits)


# --- all_caps_pair_is_phi unit behavior ---------------------------------------

def test_all_caps_pair_helper():
    assert phi.all_caps_pair_is_phi("SMITH, JONES") is True
    assert phi.all_caps_pair_is_phi("NCCN, ESMO") is False
    assert phi.all_caps_pair_is_phi("no pair here") is False


# --- ignore token -------------------------------------------------------------

def test_ignore_token_suppresses_line(tmp_path):
    line = "contact 415-555-1234  # phi-scan: ignore"
    hits = phi.scan_file(_write(tmp_path, "note.md", line))
    assert hits == []


# --- by-design artifact suppression -------------------------------------------

def test_bydesign_file_suppresses_business_contact(tmp_path):
    # accessibility.jsonl legitimately carries phones/emails/verify-dates.
    text = 'central_contact_phone 415-555-1234 and email lab@foundationmedicine.com'
    hits = phi.scan_file(_write(tmp_path, "accessibility.jsonl", text))
    assert _labels(hits) & {"us_phone", "email"} == set()


def test_bydesign_file_still_catches_patient_identifiers(tmp_path):
    # By-design files still scan for MRN/SSN/name — only business shapes relax.
    hits = phi.scan_file(_write(tmp_path, "accessibility.jsonl", "MRN: A1234567"))
    assert "mrn_label" in _labels(hits)


def test_standard_of_care_artifacts_allow_verification_dates(tmp_path):
    """Every standard-of-care row carries a mandatory `last_verified_utc`, and the
    endorsements carry guideline versions and approval dates. Without the by-design
    suppression the whole track would be unpublishable."""
    text = '{"last_verified_utc": "2026-07-24", "version_or_date": "FDA approval 2018-11"}'
    for name in ("standard_of_care.jsonl", "standard_of_care.md", "standard_of_care_report.md"):
        assert "iso_date_full" not in _labels(phi.scan_file(_write(tmp_path, name, text))), name


def test_standard_of_care_artifacts_still_catch_patient_identifiers(tmp_path):
    hits = phi.scan_file(_write(tmp_path, "standard_of_care.jsonl", "MRN: A1234567"))
    assert "mrn_label" in _labels(hits)


def test_non_bydesign_file_flags_email(tmp_path):
    hits = phi.scan_file(_write(tmp_path, "plain_language.md", "email jane@example.com"))
    assert "email" in _labels(hits)


# --- extension gating ---------------------------------------------------------

def test_binary_extension_skipped(tmp_path):
    hits = phi.scan_file(_write(tmp_path, "script.py", "SSN 123-45-6789"))
    assert hits == []


# --- is_under_case_dir --------------------------------------------------------

def test_is_under_case_dir(tmp_path):
    root = tmp_path
    (root / "case" / "slug").mkdir(parents=True)
    inside = root / "case" / "slug" / "profile.json"
    outside = root / "data" / "cases" / "slug" / "profile.json"
    assert phi.is_under_case_dir(inside, root) is True
    assert phi.is_under_case_dir(outside, root) is False


# --- main() exit codes (mode=files) -------------------------------------------

def test_main_clean_file_exit_zero(tmp_path, monkeypatch, capsys):
    clean = _write(tmp_path, "note.md", "ECOG 1, age band 60-69, progressed 2024-03")
    monkeypatch.setattr("sys.argv", ["scan_for_phi.py", "--mode=files", str(clean)])
    assert phi.main() == 0


def test_main_phi_file_exit_one(tmp_path, monkeypatch, capsys):
    dirty = _write(tmp_path, "note.md", "SSN 123-45-6789")
    monkeypatch.setattr("sys.argv", ["scan_for_phi.py", "--mode=files", str(dirty)])
    assert phi.main() == 1


# --- committed .html report downloads are scanned -----------------------------

def test_html_extension_scanned_for_patient_identifiers(tmp_path):
    # Self-contained .html downloads inline case data; a scrub miss must be caught.
    hits = phi.scan_file(_write(tmp_path, "case-report.html", "<p>MRN: A1234567</p>"))
    assert "mrn_label" in _labels(hits)


def test_html_suppresses_business_contacts(tmp_path):
    # HTML renders of accessibility/report pages carry manufacturer/trial contacts
    # and authoring dates by design — those relax, patient identifiers do not.
    text = "<td>call 415-555-1234</td><td>lab@foundationmedicine.com</td>"
    hits = phi.scan_file(_write(tmp_path, "case-accessibility.html", text))
    assert _labels(hits) & {"us_phone", "email"} == set()


# --- --include-case: promote_profile can scan case/-side files ----------------

def _case_file(tmp_path, text):
    p = tmp_path / "case" / "slug" / "derived" / "profile.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


def test_files_mode_skips_case_paths_by_default(tmp_path, monkeypatch):
    dirty = _case_file(tmp_path, '{"note": "SSN 123-45-6789"}')
    monkeypatch.setattr(
        "sys.argv",
        ["scan_for_phi.py", "--mode=files", "--root", str(tmp_path), str(dirty)],
    )
    assert phi.main() == 0  # case/ paths skipped in plain files mode (tree/staged safety)


def test_include_case_scans_case_paths(tmp_path, monkeypatch):
    dirty = _case_file(tmp_path, '{"note": "SSN 123-45-6789"}')
    monkeypatch.setattr(
        "sys.argv",
        ["scan_for_phi.py", "--mode=files", "--include-case", "--root", str(tmp_path), str(dirty)],
    )
    assert phi.main() == 1  # promote_profile.py passes --include-case so the scan runs
