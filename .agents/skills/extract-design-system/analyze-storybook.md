---
name: analyze-storybook
description: >
  Extract visual styles, design tokens, and exhaustive component sticker sheets from a Storybook instance
  or interactive UI component catalog.
---

# Storybook & Component Catalog Analyzer

Extract foundational design tokens and self-contained HTML sticker sheet
artifacts from a live Storybook instance or interactive UI component catalog
following the universal requirements in `SKILL.md`.

## Executor Contract

When invoked as an executor by `extract-design-system` (the orchestrator):

-   **Input**: A list of specific Storybook story group IDs to crawl (from the
    extraction plan).
-   **Output**: Write artifacts directly to the workspace:
    -   `extracted-tokens-[source].md` — design tokens with source citations
    -   `[component-name].html` — self-contained HTML sticker sheets
-   **Completion**: Return a structured completion report listing all artifacts
    created, tokens extracted, components extracted, and any issues encountered.

--------------------------------------------------------------------------------

## When to Use

-   User provides a URL pointing to a **Storybook instance** (e.g.,
    `https://.../storybook/`).
-   User provides an **interactive UI component catalog** or preview playground.

--------------------------------------------------------------------------------

## Hub Discovery & Story Tree Identification

Storybook instances use an iframe-based architecture separating the manager UI
from the story renderer (`iframe.html`). Systematically discover all stories
before crawling.

1.  **Locate Metadata Manifest (Recommended)**:
    -   Storybook 7+/8+: Fetch `/index.json` (a static JSON file) to retrieve
        `entries` containing every story ID, title, name, importPath, and type
        (`docs` vs `story`).
    -   Storybook 6-: Fetch `/stories.json` for legacy story manifests.
2.  **Sidebar Navigation Fallback**:
    -   If JSON manifests are unavailable, use a browser tool to render the
        Storybook UI and inspect the sidebar DOM (`#storybook-explorer-tree` or
        `data-item-id`) to extract story IDs and categories.
3.  **Categorize & Group by Component Kind**:
    -   **Foundations & Theme Docs**: Entries under `Docs/`, `Foundations/`,
        `Tokens/`, `Theme/`, `Colors/`, `Typography/`, `Spacing/`, `Icons/`.
    -   **UI Components**: Entries under `Components/*`, `UI/*`, `Elements/*`
        (e.g., `button--primary`, `button--secondary`).
    -   **Group by Parent Kind**: Combine all story IDs belonging to the same
        component kind (e.g., all `button--*` stories) so they are synthesized
        into a single Component Kit HTML artifact.
4.  **Extraction Manifest & Coverage Threshold**:
    -   Output an explicit manifest listing all discovered foundation story IDs
        and UI component story groups before crawling.
    -   You MUST schedule crawling for all foundation stories + **EVERY
        component story group**. Do not stop after 1–2 stories.

--------------------------------------------------------------------------------

## Storybook Crawling & Extraction Strategies

-   **Use Clean Iframe Endpoints**: Never fetch the main Storybook wrapper URL
    for extraction. Fetch directly from iframe rendering endpoints:
    -   Docs Pages: `/iframe.html?viewMode=docs&id=<component-id>--docs`
    -   Isolated Stories: `/iframe.html?viewMode=story&id=<story-id>`
-   **Execution Model**:
    -   Process all assigned story groups sequentially. The orchestrator
        (`extract-design-system`) handles parallelization by dispatching
        multiple executor instances — each executor focuses on its assigned
        subset of story groups.
-   **Storybook-Specific Token & Component Rules**:
    -   **Controls & ArgTypes**: Inspect Storybook Controls tables or ArgTypes
        in the iframe DOM/JSON to discover all prop values (`variant`, `size`,
        `disabled`, `state`).
    -   **Theme Addons & Dark Mode**: Check toolbar addons (`addon-themes`,
        `data-theme`, `<body class="dark">`) to capture both light and dark mode
        tokens.
    -   **Global Decorators**: Inspect `<head>` of `/iframe.html` for font
        imports, CSS resets, and root variable blocks; include them in component
        inline `<style>` blocks.
-   **Anti-Hallucination & Source Citations**:
    -   Do not guess or invent story prop values or component classes from
        pre-trained parametric memory.
    -   Every generated HTML sticker sheet artifact must cite the exact
        Storybook `/iframe.html?viewMode=story&id=...` URL it was extracted
        from.
    -   Follow the **Extraction Goals** and **Expected Output** rules in
        `SKILL.md` to produce the design token markdown artifact and component
        sticker sheet artifacts.
