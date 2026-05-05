#!/usr/bin/env bash
# Install Libby's pre-commit hook by pointing git at .githooks/.
# Idempotent — safe to re-run.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

git config core.hooksPath .githooks
chmod +x .githooks/pre-commit

echo "Installed: core.hooksPath = .githooks"
echo "The pre-commit hook will run scripts/scan_for_phi.py on every commit."
