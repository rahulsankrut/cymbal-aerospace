#!/usr/bin/env python3
"""
CLM Microsoft Outlook Communications Script (`clm-comms/scripts/outlook_comms.py`).
Supports:
  - `route-smes`: Save (or `--send`) the 4 SME review routing emails in Microsoft Outlook Drafts.
  - `send-sme-reply`: Deliver an SME review update email (`--clause-id SP3-04` for Tax, etc.) into the Contract Owner's Outlook Inbox.
  - `poll-inbox`: Poll the Contract Owner's Outlook Inbox for `[SME REVIEW UPDATE: ...]` emails and sync approved SME positions into the Working Review .docx.
  - `draft-vendor-reply`: Save (or `--send`) the final consolidated Counter-Proposal email with .docx & .xlsx attachments in Microsoft Outlook Drafts.
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

    sys.argv = [str(core_dir / "clm_cli.py"), *sys.argv[1:]]
    clm_cli.main()


if __name__ == "__main__":
    main()
