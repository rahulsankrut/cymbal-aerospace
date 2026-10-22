---
name: contract-redline-analyzer
description: >-
  Analyzes existing contract modifications (redlines) between document versions.
  Summarizes specific textual edits/diffs into Markdown comparison tables or
  classifies contract clauses as standard (template unchanged) versus
  non-standard (modified during negotiation) against contract schema
  definitions. Use when asked to inspect existing contract redlines, compare
  standard and modified versions, or classify clauses as standard vs.
  non-standard. Do not use for reviewing clean drafts to generate proposed
  redlines from scratch (use contract-review-and-redlining), strategic
  accept/reject/counter recommendations on counterparty redlines (use
  contract-redline-analysis-and-recommendation), or post-execution obligation
  extraction (use contract-obligation-extraction).
---

<!-- disableFinding(LINE_OVER_80) -->

[ROUTING & TRIGGER RULES] Trigger this skill when asked questions in either of
the following scenarios:

### Skill Differentiation: When to Use Which Redline Skill

*   **`contract-redline-analyzer` (This Skill)**: Use when pre-existing
    redlines, diffs, or two versions of an agreement (standard template vs.
    negotiated draft) already exist, and you need a technical,
    section-by-section diff comparison table or classification of clauses into
    standard (unchanged) vs. non-standard (modified).
    *   *Do NOT use for*: Generating proposed redlines on clean paper against
        legal playbooks (use `contract-review-and-redlining`).
    *   *Do NOT use for*: Strategic commercial evaluation of counterparty
        revisions to recommend `[ACCEPT]`, `[REJECT]`, or `[COUNTER]` positions
        (use `contract-redline-analysis-and-recommendation`).
*   **`contract-review-and-redlining`**: Use when you need to review a clean
    contract draft or third-party paper against corporate legal playbooks to
    generate proposed surgical redlines, strike-throughs, and comment bubbles
    from scratch.
*   **`contract-redline-analysis-and-recommendation`**: Use when you need
    strategic business analysis and negotiation recommendations (`[ACCEPT]`,
    `[REJECT]`, `[COUNTER]`) on counterparty redlines evaluated against
    commercial practice guidelines.

### Scenario A: Redlines & Modifications Summary

Trigger when asked to see, compare, or list the raw textual modifications,
edits, or redlines. **Keywords**: Redlines, Modifications, Changed sections,
Edited, Differences, Diffs, Comparison.

**Example Triggers**:

*   "What are the redlines in contract aJfKf000000cgBhKAI?"
*   "Show me the modifications for contract ID aJfKf000000cgBhKAI."
*   "Can you compare the standard and redlined versions of aJfKf000000cgBhKAI?"

### Scenario B: Standard vs Non-Standard Clause Classification

Trigger when asked to classify, separate, or identify which clauses are
"standard" (template unchanged) versus "non-standard" (modified/redlined).
**Keywords**: Standard vs non-standard clauses, Classify clauses, Which clauses
are modified, List standard clauses, Identify redlined clauses.

**Example Triggers**:

*   "Give me the standard and non-standard clauses for contract 1234"
*   "Classify the clauses for contract aJfKf000000cgBhKAI as standard or
    non-standard"
*   "List the standard and modified clauses in contract 98765"

--------------------------------------------------------------------------------

[EXECUTION & RESPONSE GUIDELINES]

1.  **Input Extraction & Document Retrieval**:

    Extract the `contract_id` or obtain the contract texts/diffs from the input
    source provided in the request (which may be a document URL, local file
    path, database identifier, or text provided directly in context). Use
    available environment integrations, document parsers, database clients, or
    filesystem APIs to load the contract text or comparison data before
    initiating analysis. Note that automated contract lookup by bare ID alone is
    not configured; if only a `contract_id` is provided without contract
    documents or accessible integrations, ensure you have located or requested
    the contract texts or diffs before proceeding. Do NOT proceed to Scenario A
    or Scenario B without contract documents.

2.  **Determine Scenario**: Identify whether the request requires a low-level
    redline summary (Scenario A) or a high-level clause classification (Scenario
    B).

--------------------------------------------------------------------------------

### GUIDELINES FOR SCENARIO A: Redlines & Modifications Summary

1.  **Obtain Comparison Diffs**: Compare the standard and modified contract
    texts (or diffs) obtained in step 1. Perform a section-by-section comparison
    to identify additions (`+`), deletions (`-`), and textual modifications
    across sections.

2.  **Process & Format**:

    *   Filter out any sections that are unchanged.
    *   Translate the raw diff content (using standard diff format with `-` and
        `+` lines) into an easily readable **Markdown Table**.
    *   Strip away raw HTML/table tags or `@@` lines from the diff output.
    *   Your table MUST include columns: **Section / Clause**, **Modification
        Type**, **Original Text**, and **New Text**.
    *   Accompany the table with a brief, conversational summary explaining the
        most critical changes.

    *   Present the comparison table and summary in your response, or save it to
        a report artifact in the workspace if requested.

3.  **Fallback**: If contract texts were successfully compared and no
    modifications or differences were found, state in your response: "There are
    no redlines or modifications found for this contract. The contract matches
    the standard version exactly."

--------------------------------------------------------------------------------

### GUIDELINES FOR SCENARIO B: Standard vs Non-Standard Clause Classification

1.  **Load Clause Schema**:

    Inspect
    [contract_schema_for_classification.md](references/contract_schema_for_classification.md)
    to understand the definitions of contract clauses, credits, discounts, and
    commitments.

2.  **Determine Active Clauses & Modifications**: Identify all active clauses
    present in the contract text, and determine which provisions contain redline
    modifications relative to standard terms.

3.  **Map and Classify (Cognitive Step)**:

    *   For each modification or modified section:
        *   Analyze the changed text (e.g., names, amounts, terms being
            modified).
        *   For commercial and financial terms (such as discounts, credits,
            commitments, and rollover rules), compare the changed text against
            the definitions in
            `references/contract_schema_for_classification.md` and map it to the
            most relevant schema clause/property (e.g., if a Service Credit
            amount changes, map it to `credits_and_funds`; if rollover terms
            change, map it to `shortfall_rollover_terms` or
            `excess_rollover_terms`).
        *   For general contract legal provisions (such as Limitation of
            Liability, Indemnification, Confidentiality, Intellectual Property,
            Warranties, and Governing Law), map it to the canonical legal title
            of the clause.
        *   Mark this mapped clause as **Non-Standard**.
    *   All remaining active clauses that did NOT have any modifications are
        classified as **Standard**.

4.  **Format & Present**:

    *   For **Standard Clauses (Template Unchanged)**: Present them as a clean
        list or table. Use the exact schema names or their clear human-readable
        equivalents for commercial/financial terms (e.g., "Credits and Funds"
        for `credits_and_funds`, "Shortfall Rollover Terms" for
        `shortfall_rollover_terms`), and canonical legal titles for general
        legal provisions (e.g., "Limitation of Liability", "Governing Law"). Do
        NOT invent detailed titles.
    *   For **Non-Standard Clauses (Negotiated/Modified)**: You MUST present
        them in a **Markdown Table** strictly matching this template:

        ```markdown
        | Clause Name | Standard (Original) | Non-Standard (Modified) | Modification Summary |
        | :--- | :--- | :--- | :--- |
        | {clause_name} | {standard_terms} | {modified_terms} | {modification_summary} |
        ```

        *   **CRITICAL (Clause Name)**: For commercial and financial terms (such
            as discounts, credits, commitments, and rollover rules), the `Clause
            Name` column MUST strictly use the corresponding schema key or
            human-readable equivalent from
            `references/contract_schema_for_classification.md`. For general
            contract legal provisions (such as Limitation of Liability,
            Indemnification, Confidentiality, Intellectual Property, Warranties,
            and Governing Law), use the canonical legal title of the clause.
        *   **DO NOT** invent detailed/nested titles like "Individual SKU Fixed
            Price Discount" or "Service Credit 1". If the change is inside a
            Service Credit, the Clause Name is still "Credits and Funds" (or
            `credits_and_funds`), and the specific details (like SKU or Credit
            name) go into the `Standard (Original)` and `Non-Standard
            (Modified)` summary cells.
        *   Populate the table rows based on your mapping.

    *   Present the standard clauses and the non-standard clauses table in your
        response, or save them to a Markdown report artifact (e.g.,
        `<appDataDir>/brain/<conversation-id>/contract_redline_report.md`) in
        the workspace if requested, and clean up any intermediate temporary
        files.

5.  **Fallback**: If contract texts were successfully compared and no
    non-standard clauses were identified, state in your response: "All active
    clauses in this contract match the standard terms." If no clauses were
    found, state in your response: "No clauses found for this contract."
