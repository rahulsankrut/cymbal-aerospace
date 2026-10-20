#!/usr/bin/env python3
"""Launcher for Cymbal Aerospace CLM Workbench UI Sidecar (`clm_cli.py serve-bridge`)."""

from pathlib import Path
import subprocess
import sys


def main() -> None:
    sidecar_dir = Path(__file__).resolve().parent
    repo_root = sidecar_dir.parent.parent
    cli_path = repo_root / "skills" / "clm_cli.py"
    subprocess.run([sys.executable, str(cli_path), "serve-bridge"], check=True)


if __name__ == "__main__":
    main()
