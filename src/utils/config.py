import os
from pathlib import Path
from typing import Optional
class Config:
    """
    Immutable configuration container for the automation framework.

    Attributes:
        browser: Playwright browser name (e.g., "chromium", "firefox", "webkit").
        headless: Whether to run browser in headless mode.
        timeout_ms: Default Playwright timeout in milliseconds.
        parallel: Number of parallel workers for test execution.
    """
    browser: str
    headless: bool
    timeout_ms: int
    parallel: int

def _bool(v: str) -> bool:
    """
    Convert a string value into a boolean.

    Accepts common "truthy" values:
        {"1", "true", "yes", "on"} (case-insensitive)

    Anything else is treated as False.

    Args:
        v: Input string read from config file.

    Returns:
        bool: Parsed boolean value.
    """
    return v.lower() in {"1","true","yes","on"}

def _int(v: Optional[str], *, default: Optional[int] = None) -> Optional[int]:
    """Safely parse an int from string; return default if value is None/empty."""
    if v is None:
        return default
    s = v.strip()
    if s == "":
        return default
    return int(s)

def load_config(path: Path) -> Config:
    """
    Load configuration from a properties file.
    """
    raw = {}
    # Read config file line-by-line
    for line in path.read_text().splitlines():
        # Ignore commented lines and only process key=value entries
        if "=" in line and not line.strip().startswith("#"):
            k,v = line.split("=",1)
            raw[k.strip()] = v.strip()

    required = [
        "browser",
        "headless",
        "timeout_ms",
        "parallel",
    ]
    for k in required:
        if k not in raw:
            raise KeyError(f"Missing required config key: {k}")

    # ADO PAT: prefer env var ADO_PAT; fallback to properties if ever added.
    ado_pat_env = os.getenv("ADO_PAT", "").strip()
    ado_pat_prop = raw.get("PERSONAL_ACCESS_TOKEN", "").strip()  # optional property if you add later
    ado_pat = ado_pat_env or ado_pat_prop or None

    return Config(
        
        browser=raw["browser"],
        headless=_bool(raw["headless"]),
        timeout_ms=_int(raw["timeout_ms"]),
        parallel=_int(raw["parallel"]),
    )