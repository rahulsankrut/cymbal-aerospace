---
name: analyze-design-system-docs
description: >
  Extract visual styles, design tokens, and exhaustive component sticker sheets from a dedicated design system
  documentation site, brand guidelines site, or UI component library portal. 
---

# Design System Docsite Analyzer

Extract foundational design tokens and self-contained HTML sticker sheet
artifacts from a dedicated design system documentation portal, component library
website, or brand guidelines site following the universal requirements in
`SKILL.md`.

## Executor Contract

When invoked as an executor by `extract-design-system` (the orchestrator):

-   **Input**: A list of specific documentation page URLs to crawl (from the
    extraction plan).
-   **Output**: Write artifacts directly to the workspace:
    -   `extracted-tokens-[source].md` — design tokens with source citations
    -   `[component-name].html` — self-contained HTML sticker sheets
-   **Completion**: Return a structured completion report listing all artifacts
    created, tokens extracted, components extracted, and any issues encountered.

--------------------------------------------------------------------------------

## When to Use

-   User provides a URL pointing to a **design system documentation site**
    (e.g., Material Design, Carbon Design System, Atlassian Design, Shopify
    Polaris).
-   User provides a **component library documentation URL** or brand guidelines
    portal.

--------------------------------------------------------------------------------

## Hub Discovery & Navigation Architecture

1.  **Map Hub Navigation**:
    -   Fetch the main hub page using a browser tool to capture the fully-rendered
        HTML.
    -   Use a browser tool to extract all navigation links from the
        rendered page, including sidebar navigation, component lists, and
        documentation links.
    -   Parse navigation menus, sidebars, tables of contents, sitemaps, or
        navigation JSON bundles.
2.  **Categorize Sub-Pages**:
    -   **Foundations & Tokens**: `/colors`, `/typography`, `/spacing`,
        `/elevation`, `/shadows`, `/borders`, `/radii`, `/layout`, `/tokens`,
        `/theme`.
    -   **UI Components**: `/components/*`, `/ui/*`, `/patterns/*`, `/button`,
        `/card`, `/modal`, etc.
    -   Deduplicate alias pages (prioritize pages showing visual previews and
        code examples over API-only docs).
3.  **Extraction Manifest & Coverage Threshold**:
    -   Output an explicit manifest listing all discovered token/foundation URLs
        and UI component URLs before crawling.
    -   You MUST schedule crawling for all token/foundation pages + **EVERY
        component documentation pages**. Do not stop after 1–2 pages.

--------------------------------------------------------------------------------

## Docsite Crawling & Extraction Strategies

-   **Execution Model**:
    -   Process all assigned pages sequentially. The orchestrator
        (`extract-design-system`) handles parallelization by dispatching
        multiple executor instances — each executor focuses on its assigned
        subset of pages.
-   **Spec Table & Code Extraction**:
    -   **Spec Tables**: Extract token names, hex/rem values, and CSS custom
        property definitions from markdown/HTML tables on foundation pages.
    -   **Component Markups**: Locate live component iframes, preview
        containers, and syntax-highlighted code blocks (`<pre><code>`) showing
        HTML/CSS usage.
    -   **Interactive Playgrounds**: For embedded playgrounds (Sandpack,
        Storybook embeds, JSX editors), inspect `<pre>`, `<code>`, or JSON
        config strings in DOM.
    -   **Global Token Files**: Check `<head>` for links to standalone
        `tokens.css`, `theme.css`, or `design-tokens.json` files.
    -   **Multi-Theme Docs**: For sites supporting multiple themes
        (Light/Dark/High Contrast), document the primary/default theme first,
        then record switching overrides.
-   **Anti-Hallucination & Source Citations**:
    -   Do not guess or invent token hex codes or component markup from
        pre-trained parametric memory.
    -   Every generated HTML sticker sheet artifact must cite the exact
        documentation page URL and code block it was extracted from.
    -   Follow the **Extraction Goals** and **Expected Output** rules in
        `SKILL.md` to produce the design token markdown artifact and component
        sticker sheet artifacts.
