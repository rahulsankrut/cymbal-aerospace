#!/usr/bin/env python3
"""
CLM Contract Intake Script (`clm-contract-intake/scripts/intake.py`).
Compares a supplier redlined .docx against the Cymbal Tier-1 Avionics Playbook baseline .docx,
queries BigQuery historical precedents in parallel across redlined clauses, identifies SME
routing owners, initializes the Working Review .docx, and renders the interactive Word 365
& Playbook Reviewer UI in Canvas.
"""
from __future__ import annotations

from pathlib import Path
import sys


def _resolve_core_cli_dir() -> Path:
    script_path = Path(__file__).resolve()
    candidates = [
        script_path.parents[2],  # <root>/skills/
        Path("/Users/rahulsankrut/ge_spark_workspace/skills"),
        Path("/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/skills"),
        Path("/Users/rahulsankrut/Desktop/code/boeing/skills"),
    ]
    for cand in candidates:
        if (cand / "clm_cli.py").exists():
            return cand
    raise FileNotFoundError("Could not locate clm_cli.py runtime.")


def main() -> None:
    core_dir = _resolve_core_cli_dir()
    if str(core_dir) not in sys.path:
        sys.path.insert(0, str(core_dir))
    import clm_cli

    argv = sys.argv[1:]
    if not argv or argv[0] != "ingest":
        sys.argv = [str(core_dir / "clm_cli.py"), "ingest", *argv]
    else:
        sys.argv = [str(core_dir / "clm_cli.py"), *argv]
    clm_cli.main()


if __name__ == "__main__":
    main()
