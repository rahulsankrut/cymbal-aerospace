#!/usr/bin/env python3
"""
CLM Contract Consolidation Script (`clm-contract-consolidation/scripts/consolidate.py`).
Consolidates recorded SME and Contract Owner positions and user comments from the Working Review .docx
into the final Counter-Proposal .docx (with OOXML Track Changes <w:ins>/<w:del> and <w:comment> margins)
and 4-Tab SharePoint Deviation Matrix .xlsx, verifies external sanitization, and updates the Canvas Workbench.
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
    if not argv or argv[0] != "consolidate":
        sys.argv = [str(core_dir / "clm_cli.py"), "consolidate", *argv]
    else:
        sys.argv = [str(core_dir / "clm_cli.py"), *argv]
    clm_cli.main()


if __name__ == "__main__":
    main()
