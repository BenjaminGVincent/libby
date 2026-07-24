"""Tests for scripts/promote_profile.py — the PHI bridge into committed data.

The load-bearing guarantee: the PHI scan actually runs against the scrubbed
profile, which lives under case/. That only happens if promote passes
--include-case (without it scan_for_phi.py skips case/ paths and the scan is a
silent no-op). This pins that flag so the bridge can't regress to schema-only.
"""

import promote_profile as pp


def test_phi_scan_passes_include_case_flag(monkeypatch, tmp_path):
    captured = {}

    class _Result:
        returncode = 0

    def fake_run(cmd, *a, **k):
        captured["cmd"] = cmd
        return _Result()

    monkeypatch.setattr(pp.subprocess, "run", fake_run)
    rc = pp.run_phi_scan([tmp_path / "profile.json", tmp_path / "preferences.json"])

    assert rc == 0
    assert "--mode=files" in captured["cmd"]
    assert "--include-case" in captured["cmd"], (
        "promote must pass --include-case or the PHI scan silently skips the "
        "case/-side profile"
    )


def test_phi_scan_hit_returns_nonzero(monkeypatch, tmp_path):
    class _Result:
        returncode = 1

    monkeypatch.setattr(pp.subprocess, "run", lambda cmd, *a, **k: _Result())
    assert pp.run_phi_scan([tmp_path / "profile.json"]) == 1
