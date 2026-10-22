---
name: analyze-codebase
description: >
  Extract design system primitives from a frontend codebase — React, Vue, Svelte,
  Angular, plain HTML/CSS, or any web framework. Analyzes component files, stylesheets,
  Tailwind configs, theme definitions, and design tokens.
---

# Codebase Design System Analyzer

Extract foundational design tokens and self-contained HTML sticker sheet
artifacts from a frontend codebase following the universal requirements in
`SKILL.md`.

## Executor Contract

When invoked as an executor by `extract-design-system` (the orchestrator):

-   **Input**: A specific code directory path or set of files to analyze.
-   **Output**: Write artifacts directly to the workspace:
    -   `extracted-tokens-[source].md` — design tokens with source citations
    -   `[component-name].html` — self-contained HTML sticker sheets
-   **Completion**: Return a structured completion report listing all artifacts
    created, tokens extracted, components extracted, and any issues encountered.

--------------------------------------------------------------------------------

## When to Use

-   User provides a **git repo URL**.
-   User provides a **path to a local code directory**.
-   User provides **individual HTML/CSS/JS/TS files**.

--------------------------------------------------------------------------------

## Project Discovery

1.  **Clone or Locate Code**:
    -   For a git URL: `git clone --depth 1 <url> /tmp/design-extract-<hash>`
    -   For a local path: use directly and verify source files exist.
2.  **Detect Stack**: Inspect `package.json` and config files first:

Signal File                               | Framework / Tool
:---------------------------------------- | :-----------------
`package.json` with `react`               | React / Next.js
`package.json` with `vue`                 | Vue / Nuxt
`package.json` with `svelte`              | Svelte / SvelteKit
`package.json` with `@angular/core`       | Angular
`tailwind.config.js/ts`                   | Tailwind CSS
`postcss.config.js`                       | PostCSS pipeline
`styled-components` or `@emotion` in deps | CSS-in-JS
`.css` / `.scss` / `.less` files only     | Plain CSS / SASS
`theme.js` / `theme.ts` / `tokens.js`     | Design token files

3.  **Map Key Directories & Files**:
    -   Check `components/`, `src/components/`, `app/components/`, `styles/`,
        `css/`, `scss/`, `theme/`, `themes/`.
    -   Locate `tailwind.config.*`, `globals.css`, `app.css`, `theme.*`,
        `tokens.*`, `_variables.scss`.
4.  **Consult Framework Guidance**:
    -   React / Next.js / Tailwind: `references/react-tailwind.md`
    -   Vue / Nuxt: `references/vue.md`
    -   Svelte / SvelteKit: `references/svelte.md`
    -   Angular: `references/angular.md`
    -   Plain CSS / SASS: `references/plain-css.md`

--------------------------------------------------------------------------------

## Codebase Extraction Strategies

-   **Design Token Sources**:
    -   Inspect `tailwind.config.js/ts` (`theme.extend.colors`, spacing,
        borderRadius, boxShadow).
    -   Inspect `:root` CSS custom properties (`--color-*`, `--space-*`) in
        global stylesheets (`globals.css`, `app.css`).
    -   Inspect CSS-in-JS theme objects (`theme.ts`, `tokens.ts`) or exported
        JSON token manifests.
-   **Component Discovery & Conversion**:
    -   Inspect component interfaces and prop types (e.g., `interface
        ButtonProps`, `cva()`, `clsx()`) to identify all supported variants,
        sizes, and interactive states.
    -   Convert framework templates (React JSX/TSX, Vue, Svelte, Angular) into
        pure, standalone HTML5 markup with embedded `<style>` blocks for each
        discovered UI primitive (buttons, cards, inputs, modals, etc.).
-   **Anti-Hallucination & Source Citations**:
    -   Do not guess or invent token values or component styles from pre-trained
        parametric memory.
    -   Every extracted token and component sticker sheet artifact must cite the
        exact file path and line numbers (`path/to/file#L10-L20`) it was
        extracted from.
    -   Follow the **Extraction Goals** and **Expected Output** rules in
        `SKILL.md` to produce the design token markdown artifact and component
        sticker sheet artifacts.
