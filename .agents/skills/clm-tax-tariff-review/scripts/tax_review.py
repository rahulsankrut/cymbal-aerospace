#!/usr/bin/env python3
"""
CLM Global Tax & Tariff SME Review Script (`clm-tax-tariff-review/scripts/tax_review.py`).
Evaluates SP3 §4.1 (Customs, Duties & Section 232/301 Tariffs), queries BigQuery Tax
precedents, resolves the cross-clause Firm-Fixed-Price SOW ceiling conflict with GP1 §3.1,
records the Tax SME's comment in the Working Review .docx, and renders the Tax Reviewer UI.
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
    if not argv or argv[0] not in ("tax-review", "harmonize"):
        sys.argv = [str(core_dir / "clm_cli.py"), "tax-review", *argv]
    else:
        sys.argv = [str(core_dir / "clm_cli.py"), *argv]
    clm_cli.main()


if __name__ == "__main__":
    main()
