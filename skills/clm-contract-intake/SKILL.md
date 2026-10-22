---
name: clm-contract-intake
description: Compares a supplier's redlined contract (.docx) against the Cymbal Tier-1 Avionics Playbook baseline (.docx — Preferred Standard, Pre-Approved Tier-1 Fallbacks, Regulatory Lockout Guardrails, and live BigQuery historical precedents across redlined positions), identifies the SME domain owners, initializes the Working Review Document, and renders the interactive Word 365 & Playbook Reviewer UI in Spark Canvas.
---

# Cymbal Aerospace CLM — Contract Intake, Playbook Diff & SME Identification (`clm-contract-intake`)

Use this skill when a user asks to ingest, compare, or triage a supplier's redlined contract (`.docx`) against the Cymbal Aerospace Standard Playbook/Proforma, check historical precedents across redlined clauses, identify which Subject Matter Experts (SMEs) own each exception, and open the interactive **Word 365 & Playbook Reviewer UI** in Canvas.

> **Single-Responsibility Boundary**: This skill performs contract parsing, Playbook & BigQuery precedent evaluation, Working Review `.docx` initialization, and Reviewer UI generation ONLY. Do **NOT** create or send Outlook emails or upload files to SharePoint unless the user explicitly asks for those actions (which are handled by `clm-comms` or the SharePoint connector).

---

## Step 1 — Run the Contract Intake & Playbook Comparison Script

Execute `scripts/intake.py` (which invokes the `ingest` workflow on the actual `.docx` files and queries BigQuery in parallel). Pass the appropriate `--deal-id` for the contract being inspected:
- **`BA-2026-AV-8921`** (Doc 1 — Apex AeroSystems Inc. — `$45M` Flight Control Computers FCC-900 — Stage 1 Fresh Vendor Redline Intake)
- **`BA-2026-TR-5510`** (Doc 2 — Vanguard Thrust Systems Corp. — `$38M` Thrust Reverser Actuators TRA-500 — Stage 2 Middle-Stage Working Review `.docx` with Finance vs. Legal Conflict)
- **`BA-2026-LG-7740`** (Doc 3 — Meridian Landing Gear Corp. — `$52M` Titanium Landing Gear Assemblies TLG-800 — Stage 3 Final-Stage SME-Reviewed Working `.docx`)

```bash
python3 /Users/rahulsankrut/ge_spark_workspace/skills/clm-contract-intake/scripts/intake.py \
  --deal-id BA-2026-AV-8921 \
  --vendor-docx-path specs/04_golden_fixtures/Vendor_Redlined_GP1.docx \
  --baseline-docx-path specs/04_golden_fixtures/Cymbal_GP1_Standard.docx
```

*(For Stage 2 Doc 2 Finance vs. Legal conflict inspection: `python3 /Users/rahulsankrut/ge_spark_workspace/skills/clm-contract-intake/scripts/intake.py --deal-id BA-2026-TR-5510`)*
*(Fallback path if running directly from the repository root: `python3 skills/clm-contract-intake/scripts/intake.py --deal-id <DEAL_ID>`)*

### What the Script Computes Live:
1. **Real `.docx` OOXML Track Changes & Word-Level Diff**: Parses `vendor_docx_path` against `baseline_docx_path`, separating untouched baseline clauses (`untouched_clauses`) from redlined exceptions (`redlined_exceptions`) and extracting embedded vendor margin comments (`<w:comment>`).
2. **Parallel BigQuery Precedent Search (`VECTOR_SEARCH`)**: Queries `boeing_clm.historical_clause_exceptions` concurrently across all redlined clauses (`bigquery_precedent_distribution`) to compute the historical `% Held Firm`, `% Compromise`, and `% Accepted Vendor` distribution and retrieve top matching historical supplier deals.
3. **Cross-Clause Conflict & Regulatory Lockout Detection**: Evaluates `boeing_clm.clause_conflict_rules` and statutory regulatory lockouts (`active_conflicts`).
4. **Working Review Document & Interactive Canvas UI**: Writes `<deal_id>_Working_Review.docx` and `cymbal_clm_redline_workbench.html` in the current working directory.

---

## Step 2 — Present the Live Intake & Playbook Triage Report

Using the JSON output returned by `scripts/intake.py`:
1. **Contract & Playbook Summary**:
   - State `total_clauses_parsed`, `untouched_clauses_count` (auto-cleared against the Playbook Preferred Standard), and `redlined_clauses_count` requiring SME review, along with the initialized `working_review_docx` filename.
2. **Redlined Exceptions, Playbook Guardrails & BigQuery Precedent Table**:
   - Render a Markdown table from `redlined_exceptions` and `sme_routing_owners` showing for each redlined clause:
     - Clause Ref & Title (`clause_ref`, `clause_title`)
     - Assigned SME Team & Owner (`sme_team`, `owner_name`, `owner_email`)
     - Playbook Verdict & Guardrail (`playbook_verdict`, `playbook_guardrail_summary`, `regulatory_flag`)
     - Live BigQuery Historical Precedent Distribution (`held_firm_pct`, `compromise_tier_1_pct`, `accepted_vendor_pct`, `total_historical_deals`)
     - Recommended Counter-Position (`recommended_counter_position`)
3. **Active Cross-Clause Conflicts**:
   - Surface any active cross-clause conflicts reported in `active_conflicts` (such as `rule_id`, `source_clause_id`, `conflicting_clause_id`, and `description`).
4. **Open the Interactive Reviewer UI (Antigravity Sidecar & Spark Canvas)**:
   - Output a clickable Markdown file link to `[cymbal_clm_redline_workbench.html](cymbal_clm_redline_workbench.html)` so the user can open the **Word 365 & Playbook Review Workbench** in Spark Canvas, alongside the Antigravity Sidecar pill links `[Cymbal CLM Workbench](sidecar://cymbal-aerospace-clm/cymbal-clm-workbench/)` and `[Cymbal Tax & Tariff Review](sidecar://cymbal-aerospace-clm/cymbal-clm-workbench/tax-workbench)`.
   - In Antigravity, if the conversation artifact directory (`<appDataDir>/brain/<conversation-id>/clm_inline_triage_widget.html`) is available, you may also embed the Short-Form Inline Triage Widget right in chat via `<agent-embed src="file:///<appDataDir>/brain/<conversation-id>/clm_inline_triage_widget.html"></agent-embed>`.
