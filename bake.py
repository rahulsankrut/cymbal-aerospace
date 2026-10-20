#!/usr/bin/env python3
"""Cymbal Aerospace CLM Demo Baker ("bake clm demo" / "bake clm").

Usage:
  /Users/rahulsankrut/Desktop/code/boeing/.venv/bin/python bake.py [clm | clm-demo] [--quick | --full]
"""

from __future__ import annotations

import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
BAKE_SCRIPT = ROOT / "scripts" / "bake_demo.py"


def main() -> int:
    flags = [a for a in sys.argv[1:] if a.startswith("-")]
    cmd = [sys.executable, str(BAKE_SCRIPT), *flags]
    return subprocess.run(cmd, cwd=str(ROOT)).returncode


if __name__ == "__main__":
    raise SystemExit(main())
