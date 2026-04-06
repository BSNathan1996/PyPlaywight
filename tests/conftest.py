import sys
from pathlib import Path
from PyPlaywight.src.utils.config import load_config
from PyPlaywight.src.common.helper.helper import Helper

import pytest

ROOT_DIR = Path(__file__).resolve().parents[1]
PARENT_DIR = ROOT_DIR.parent
if str(PARENT_DIR) not in sys.path:
    sys.path.insert(0, str(PARENT_DIR))


def _project_root() -> Path:
    """
    Returns repository root folder (assuming conftest.py is in tests/).
    """
    return Path(__file__).resolve().parents[1]

@pytest.fixture(scope="session")
def config():
    """
    Session-scoped config loader (reads config.properties).
    """
    return load_config(_project_root() / "config.properties")

@pytest.fixture
def helper(page):
    """Provide a test helper wrapper around Playwright's page fixture."""
    return Helper(page)