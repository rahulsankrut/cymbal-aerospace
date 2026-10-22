# Phase 4: Stakeholder Reporting & JSON Audit Trail (Parts B & C)

Use these rules during **Phase 4: Reporting & Audit Log** to handle unforeseen
terms, incorporate external links, and compile severity-sorted audit trails.

--------------------------------------------------------------------------------

## 1. Handling External URLs & Incorporated DPAs

Vendor agreements frequently incorporate terms by link (e.g., `"governed by the
terms at [URL]"` or `"DPA available at [URL]"`).

*   **Explicit Logging:** You must never silently ignore incorporated URLs or
    treat them as absent. Record all detected URLs in your `<scratchpad>` and
    the audit memo.
*   **Readable Links:** If the URL is publicly accessible or readable via your
    tools (`read_url_content`), fetch and evaluate the text against the
    playbook.
*   **Unreadable / Authenticated Links:** If the URL cannot be fetched (requires
    login or behind firewall), **do not enter a tool retry loop**. Immediately
    halt attempts to browse it, tag the item as `ESCALATED_OMISSION`, and append
    a comment requesting attachment: *"Agreement incorporates terms/DPA by
    reference at [URL], which cannot be accessed directly. Please attach the
    full PDF/text for legal compliance review."* For unreadable URLs or missing
    clauses tagged as ESCALATED_OMISSION, use "N/A" for playbook_rule_id and
    proposed_fix, and place the required missing-link comment into the
    internal_rationale.

--------------------------------------------------------------------------------

## 2. Deliverable Output Formatting (Part B)

**Additional Prompted Formatting:** If the provided Playbook or Prompt
explicitly requests additional sections, specific headers, or custom details in
the final report (e.g., requesting a "Stakeholder Summary" section or a specific
warning header), you MUST include them exactly as requested alongside the
standard template.

Your Phase 4 Phase deliverable must use the baseline formatting below,
incorporating any additionally requested details:

### Part B: Audience-Calibrated Executive Summary & Cover Note

Provide a high-level summary for the business stakeholder:

```markdown
# CLM Redlining Review Memo
## Executive Summary
- **Review Status:** [Review Complete - Minor Risks Found / Review Complete - Escalations Required]
- **The Catch:** [The biggest remaining risk]
- **Escalation Verification Checklist:** [Explicitly verify and list all required escalations identified during the audit (e.g., to Legal, Security). IF any `<clause_audit>` XML payload contains records tagged `PROCEDURAL_WARNING`, `ESCALATED_RED_LINE`, or `ESCALATED_OMISSION`, you MUST explicitly itemize them in the Checklist with their required operational action. If none, state "None Found". You MUST state this explicitly.]
- **Action Checklist:** [Next steps for the business owner]

## Counterparty Cover Note
[Insert the strictly formatted cover note using EXACT Playbook categories and contextual justifications]
```

**Cover Note Formatting Guidelines:**

1.  **Structure by Playbook Categories:** Organize points using Level 3 Markdown
    headers (`### [Category Name]`). You MUST strictly map all issues to one of
    the standard Playbook category headers defined in the active Playbook's
    template (never use local contract section names like "SOW Term" or
    "Services and Deliverables"). Ensure you map specific issues to the correct
    parent category using the semantic mapping guide provided in the active
    Playbook payload.
2.  **Contextual Justification & Client Directives:** Incorporate explicit
    business context and any specific transmittal directives provided in the
    prompt (e.g., target execution dates, diligence timelines, strategic
    framing) without inventing issues not present in the draft.
3.  **Document & Date Conventions:** Refer to the underlying document neutrally
    as the "Agreement" or "redlined draft" (do not reference raw file names),
    and always use full 4-digit years (e.g., 2025) for dates.

## 3. Generating the Severity-Sorted Audit Trail (Part C)

To ensure rapid human review and save tokens, Part C strictly itemizes clauses
that required redlines, omissions, or escalations (derived from the Gate 3
`<clause_audit>` XML payloads). You MUST sort your Gate 3 entries strictly by
severity, from highest risk to lowest risk.

### Severity Sorting Hierarchy:

1.  **Priority 1: Escalations & Critical Omissions (High Severity)** -> Clauses
    tagged `ESCALATED_RED_LINE` or `ESCALATED_OMISSION`.
2.  **Priority 2: Pre-Approved Fallbacks Applied (Medium Severity)** -> Clauses
    tagged `REDLINED_TO_FALLBACK`.
3.  **Priority 3: Preferred Positions & Operational Redlines (Low Severity)** ->
    Clauses tagged `REDLINED_TO_PREFERRED` or `REDLINED`.

### Commenting Strategy

Your comments are your primary mode of communication. You must generate two
distinct comments for every redline in the `<clause_audit>` payload:

*   `external_justification`: (For the counterparty) Polite, collaborative, and
    commercially reasonable. Frame justifications around mutual clarity,
    industry standards, or business logic.
*   `internal_rationale`: (For the internal business client) Analytical and
    strategic. Explain the legal/commercial risk, trade-offs, and required next
    steps (e.g., "Please confirm with Risk team...").
*   **Procedural Warnings & Missing Items:** For records tagged
    `PROCEDURAL_WARNING` or `ESCALATED_OMISSION`, populate `internal_rationale`
    with the required operational action, and set `proposed_fix` and
    `playbook_rule_id` to `"N/A"`.

--------------------------------------------------------------------------------

### JSON Metadata Schema (Part C):

For every Gate 3 `<clause_audit>` record, append an entry to the JSON audit
trail using exactly this schema:

```json
[
  {
    "redline_id": "RL_001",
    "clause_location": "Section [Number] ([Topic Title])",
    "playbook_says": "Preferred: [Preferred Rule Baseline]. Fallback: [Approved Fallback].",
    "contract_says": "[Exact non-compliant quote or position in draft]",
    "proposed_fix": "[Exact replacement text asserting Preferred or Fallback position]",
    "playbook_rule_id": "RULE_[TOPIC]_01",
    "status": "REDLINED_TO_PREFERRED",
    "business_impact": "Concise executive summary of commercial/legal impact.",
    "internal_rationale": "Internal legal rationale explaining risk mitigation.",
    "external_justification": "Customer-facing explanation provided in comment bubble.",
    "escalation_required": false
  }
]
```
