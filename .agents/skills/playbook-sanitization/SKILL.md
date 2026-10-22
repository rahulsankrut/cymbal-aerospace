---
name: playbook-sanitization
description: >-
  The skill Sanitizes, anonymizes, cleans, and restructures legal playbooks, agreements,
  contract guidelines, and negotiation tables. Use when asked to remove PII,
  personal names, email addresses, internal URLs, tools, systems, or
  confidential internal concession thresholds while preserving generic roles,
  operational responsibilities, legal obligations, rights, restrictions,
  remedies, fallbacks, and governing law. Also use when requested to summarize,
  organize, or extract negotiation positions (standard positions, fallbacks,
  escalation triggers), compliance obligations, breach notice checklists, or
  audit rights from playbooks, or to normalize grammar and convert sanitized
  legal documents to clean Markdown with an audit change log.
license: Apache-2.0
metadata:
  display_description: Strips names, links, and private details to make playbooks safe to share.
  display_name: "Playbook cleaner"
  version: "1.0.0"
  skill_version_cl: "994973514"
  publisher: google
---

# Playbook Sanitization

## Overview

Sanitizes and anonymizes legal playbooks, negotiation guidelines, and agreements
by removing PII and confidential internal references while strictly preserving
legal intent, generic roles, and negotiation positions.

## When to Use

-   Sanitizing, anonymizing, cleaning, or redacting legal playbooks, agreements, or negotiation guidelines.
-   Removing individual names, personal contact details, internal URLs, systems, tools, or confidential thresholds for external sharing.
-   Preserving generic roles, authority structures, contractual obligations, rights, prohibitions, remedies, or governing law during sanitization.
-   Extracting, organizing, or summarizing negotiation positions (standard, fallback, escalation triggers) or compliance checklists from playbooks.
-   Fixing grammar, flow, and formatting post-sanitization and exporting clean Markdown (`sanitized_playbook.md`) with a change log / audit report.
-   Fetching and scrubbing legal documents from supported Gemini connectors.

## Core Pattern

1.  **Identify Source**: Use URL domain to determine the appropriate Native
    Gemini Connector.
2.  **Copy First (Workspace)**: ALWAYS create a duplicate of the target document
    within its native platform (e.g., "Make a copy" in Google Drive) before
    accessing it via native connectors to prevent accidental modifications to
    the original.
3.  **Pre-Flight Reading**: Perform a mandatory pre-flight reading across all
    attached deal files (.eml, .xlsx, .docx).
4.  **Sanitize Locally**: Save raw content from the copied document locally.
    Scrub PII (Personally Identifiable Information) and confidential internal
    data (like raw price floors or internal margin targets) while strictly
    PRESERVING standard commercial business terms (e.g., Net 30 payment terms,
    liability caps), legal obligations, penalties, and escalation requirements.
    Do not treat standard commercial terms as PII or confidential entity data.
5.  **Convert**: Export sanitized text to clean markdown with proper headers and
    tables (`sanitized_playbook.md`).
6.  **Update Copied Document**: Update the copied native document with the
    sanitized text.
7.  **Final Output**: ALWAYS print the comprehensive Audit Report directly in
    your final chat response to the user as a markdown table. Do NOT just
    summarize; you must provide the exact list of every single change made,
    including columns for `Original Text`, `Replacement`, and `Reason`.
    Additionally, provide a direct link to the newly copied workspace document.

## Quick Reference

Source Type                                                                                                           | Integration Method
--------------------------------------------------------------------------------------------------------------------- | ------------------
Google Workspace, Office365, Docusign, Relativity, NetDocuments, iManage, Ironclad, Harvey, Ever Law, Thomson Reuters | Native Gemini Connectors

## Implementation

**REQUIRED BACKGROUND:** You MUST read and strictly follow the rules in
`references/sanitization_rules.md`.

**Tone and Formatting:** You MUST maintain a professional legal tone in the
output. Do NOT use any emojis in your output or the sanitized playbook.

## Common Mistakes

-   **Modifying original document**: Failing to create a copy before fetching
    via native connectors.
-   **Altering legal intent**: Softening penalties or removing escalation
    requirements when anonymizing roles.
-   **Hallucinating content**: Proceeding to sanitization when the initial
    document fetch failed.
-   **Remote editing**: Attempting to sanitize the document chunk-by-chunk
    remotely instead of locally.