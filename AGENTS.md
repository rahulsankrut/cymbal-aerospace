# Cymbal Aerospace CLM Demo — Workspace Rules (`AGENTS.md`)

## "Bake CLM Demo" Shorthand Command (Mandatory Agent Action)

Whenever the user issues the shorthand instruction **`"Bake CLM demo"`** (or `"bake clm"`, `"bake aerospace"`, `"reset clm demo"`), immediately execute:

```bash
"/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.venv/bin/python" "/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/scripts/bake_demo.py" --full
```

> **IMPORTANT**: Never run `clm_cli.py route-smes` or `clm_cli.py ingest --with-drafts` during `Bake CLM demo`! The Outlook `Drafts` folder must remain at **`0` drafts** after baking so that **Spark** creates the 4 SME routing drafts and the final vendor reply draft live during the demo when prompted via `clm-comms`.

### What `scripts/bake_demo.py` Does:
1. **Resets Deal `BA-2026-AV-8921`**: Resets BigQuery (`vertex-ai-demos-468803.boeing_clm`), Cloud Run (`https://boeing-clm-engine-5udif2v3cq-uc.a.run.app`), and local Spark state (`~/ge_spark_workspace/skills/cymbal_clm_state.json`) back to pristine intake state (`status = INGESTED`).
2. **Syncs 4 Focused CLM Skills to Spark & Restarts the Host Loopback Bridge (`127.0.0.1:58921`)**:
   - `clm-contract-intake` (Proforma diff, BigQuery precedent check across all 4 positions, SME owner lookup, and interactive Document-Style Counter-Position Reviewer UI)
   - `clm-comms` (Outlook SME draft/send routing, SME reply delivery, Inbox polling, and final vendor reply draft/send)
   - `clm-tax-tariff-review` (Tax SME review on `SP3 §4.1`, BigQuery Tax precedents, `GP1 §3.1` FFP SOW conflict harmonization, and Tax Reviewer UI)
   - `clm-contract-consolidation` (Owner precedent verification across all 4 positions, consolidation of `BA-2026-AV-8921_Working_Review.docx` into final `.docx` and `.xlsx` with human user comments, and live SharePoint upload)
3. **Cleans Up ONLY Microsoft Outlook Mail & Calendar**:
   - Purges existing messages from `m365-admin@rahulsankrut.demo.altostrat.com` `Inbox` and `Drafts` (leaving `Drafts` at **`0`**).
   - Purges existing calendar events across the M365 demo roster.
   - **Does NOT touch or delete** SharePoint (`CymbalAerospace` or `CybmalFinance`), OneDrive, Jira, or Confluence.
4. **Seeds Fresh Cymbal Aerospace CLM Outlook Mail & Calendar**:
   - Seeds **5 Cymbal Aerospace CLM emails** (rolled to TODAY's date) into `Inbox`, including Adele Vance's urgent vendor redline submission with `Vendor_Redlined_GP1.docx` and `Apex_AeroSystems_Redline_Transmittal_Memo.docx` attached.
   - Seeds **6 Cymbal Aerospace CLM meetings** (rolled to TODAY and CURRENT WEEK) onto the Outlook Calendar so the generic `chief-of-staff` skill (*"What are my top priorities today?"*) naturally surfaces Deal `BA-2026-AV-8921` and today's 1:30 PM & 4:00 PM decision gates without any CLM-specific modifications to `chief-of-staff`.
