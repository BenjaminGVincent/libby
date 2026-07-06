"""Shared pytest fixtures / path setup for the Libby test suite.

The build/validation scripts live in scripts/ and are written as standalone
CLIs (not an installed package), so make them importable by adding scripts/ to
sys.path for the duration of the test session.
"""

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPTS = REPO / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
