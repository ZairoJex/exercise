"""Verify that commands are running in the dedicated Python 3.11 environment."""

import platform
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EXPECTED_VENV = (REPO_ROOT / ".venv").resolve()
ACTIVE_PREFIX = Path(sys.prefix).resolve()


def main() -> None:
    assert sys.version_info[:2] == (3, 11), (
        f"Expected Python 3.11, got {platform.python_version()}"
    )
    assert ACTIVE_PREFIX == EXPECTED_VENV, (
        f"Expected {EXPECTED_VENV}, got {ACTIVE_PREFIX}"
    )

    print("[OK] Python:", platform.python_version())
    print("[OK] Interpreter:", sys.executable)
    print("[OK] Virtual environment:", ACTIVE_PREFIX)
    print("[OK] This environment is isolated from other local projects.")


if __name__ == "__main__":
    main()
