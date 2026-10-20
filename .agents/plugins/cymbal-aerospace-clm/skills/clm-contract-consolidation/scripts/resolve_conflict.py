#!/usr/bin/env python3
"""
CLM Cross-Department Conflict Resolution Script (`clm-contract-consolidation/scripts/resolve_conflict.py`).
Resolves cross-clause / cross-department conflicts in the Working Review .docx (such as the Stage 2
Finance vs. Legal conflict on Deal BA-2026-TR-5510 where Legal Playbook guardrails take precedence
over Finance's commercial cap-for-discount trade-off) and updates the Review Workbench HTML.
"""
from __future__ import annotations

from pathlib import Path
import sys


def _resolve_core_cli_dir() -> Path:
    script_path = Path(__file__).resolve()
    candidates = [
        script_path.parents[2],
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
    if not argv or argv[0].startswith("-"):
        argv = ["resolve-conflict", *argv]
    sys.argv = [str(core_dir / "clm_cli.py"), *argv]
    clm_cli.main()


if __name__ == "__main__":
    main()
