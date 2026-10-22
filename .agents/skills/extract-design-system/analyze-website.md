---
name: analyze-website
description: >
  Extract design system primitives from a live website by crawling pages, extracting computed styles,
  and analyzing visual patterns.
---

# Analyze Website

Extract foundational design tokens and self-contained HTML sticker sheet
artifacts from a live, publicly accessible website following the universal
requirements in `SKILL.md`.

## Executor Contract

When invoked as an executor by `extract-design-system` (the orchestrator):

-   **Input**: A list of specific page URLs to crawl (from the extraction plan).
-   **Output**: Write artifacts directly to the workspace:
    -   `extracted-tokens-[source].md` — design tokens with source citations
    -   `[component-name].html` — self-contained HTML sticker sheets
-   **Completion**: Return a structured completion report listing all artifacts
    created, tokens extracted, components extracted, and any issues encountered.

--------------------------------------------------------------------------------

## When to Use

-   User provides a publicly accessible website URL.
-   User wants to capture the visual identity of an existing website or product.

--------------------------------------------------------------------------------

## Important Principles

-   **Go beyond the landing page.** Landing pages often have unique hero
    sections and marketing layouts that don't represent the actual product
    design. Follow links to **10-20 representative pages** that reveal the real
    product UI (dashboards, listing pages, detail pages, settings pages, forms).
-   **Capture the product, not the marketing.** Prioritize navigation to
    authenticated-looking pages, app-like interfaces, and content-heavy pages
    over splash screens and marketing carousels.

--------------------------------------------------------------------------------

## Page Discovery & Navigation Planning

1.  **Fetch Initial URL**: Use a browser tool to fetch the fully-rendered HTML
    (handles both static and client-side rendered pages) and extract all navigation links from the rendered page.
2.  **Identify Navigation Links**: Locate main navigation menus, sidebar links,
    footer links, and application paths (`/dashboard`, `/products`, `/settings`,
    `/docs`, `/profile`, `/list`).
3.  **Select 10-20 Representative Pages**: Pick product/app UI pages exhibiting
    diverse component usage (forms, lists, cards, data tables, modals, buttons).
4.  **Fetch Selected Pages**: Use a browser tool to retrieve the rendered HTML
    for each page. Use a browser evaluation tool to inspect computed CSS values
    (`getComputedStyle()`, such as colors, border-radius, spacing, font sizes) from
    specific elements.

--------------------------------------------------------------------------------

## Website Extraction Strategies

-   **CSS & Token Harvesting**:
    -   Parse inline `<style>` blocks, `<link rel="stylesheet">` files, style
        attributes, and CSS custom properties (`--color-*`, `--primary`,
        `--bg-*`, etc.) in `:root` or `html` selectors.
    -   Inspect `<meta name="theme-color">` tags and CDN stylesheet URLs.
-   **CSS Framework Recognition**:
    -   Identify utility-first or component library patterns from DOM class
        naming conventions (e.g., Tailwind `bg-blue-500 text-gray-700`,
        Bootstrap `btn btn-primary`, Material UI, Radix UI) and map them to
        explicit CSS rules.
-   **Cross-Page Synthesis**:
    -   Compare extracted styles across the 10-20 crawled pages. Deduplicate
        near-identical colors and spacing to separate global site foundations
        from page-specific overrides.
-   **Anti-Hallucination & Source Citations**:
    -   Do not guess or invent token hex codes or component styles from
        pre-trained parametric memory.
    -   Every extracted token and component sticker sheet artifact must cite the
        exact page URL and DOM selector it was extracted from.
    -   Follow the **Extraction Goals** and **Expected Output** rules in
        `SKILL.md` to produce the design token markdown artifact and component
        sticker sheet artifacts.
