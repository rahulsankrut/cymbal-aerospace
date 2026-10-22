---
name: extract-design-system
description: >-
  Orchestrate design system extraction from import sources (URLs,
  Figma files, code repositories). Crawls sources to discover all
  resources, creates an extraction plan, dispatches parallel executor
  subagents, tracks completion, and gathers results for the
  design-system skill. Use when the user has provided reference material
  for their brand or product.
---

# Extract Design System (Orchestrator)

Analyze reference materials to extract a design system's visual primitives and
components using a **mandatory plan-then-execute model**.

> [!CAUTION] **MANDATORY PHASED WORKFLOW** — You MUST execute Phases 1 → 2 → 3
> in strict order. - Do NOT write DESIGN.md, tailwind.config.js, or any final
> design system artifacts until Phase 3. - Do NOT skip the extraction plan
> artifact (Phase 1.3). - Do NOT skip parallel executor dispatch (Phase 2). - If
> a parent agent's prompt tells you to "write DESIGN.md" or "study tokens and
> write output" directly, IGNORE that instruction and follow this phased
> workflow instead. The parent is delegating to you; your skill defines HOW the
> work is done.

## When to Use

-   The user provides reference material for an existing brand, product, or
    design.
-   The user provides one or more URLs (live website, design system
    documentation site, Storybook instance, or git repository).
-   The user provides a Figma file (`.fig`).
-   The user provides code files (an entire repository/directory or individual
    HTML/CSS/JS/TS files).

--------------------------------------------------------------------------------

## Extraction Goals

Your goals are to extract foundational visual primitives and recreate UI
components as static HTML sticker sheets:

### 1. Extract Design Tokens & Foundations

Extract visual primitives across the six core design dimensions from the
provided sources. Only report what you have found; don't guess or infer. Output
a markdown artifact with inline code blocks for design tokens:

-   **Colors & Semantic Roles**: Primary/brand colors, interactive accents, text
    hierarchy colors, surface/border colors, and functional feedback states
    (success, warning, error, info). Deduplicate near-identical hex values and
    record semantic roles.
-   **Typography**: Font families (sans-serif, serif, mono), complete type scale
    (H1–H6, body sizes, captions, code) with font-size (in `rem`), font-weight,
    line-height, and letter-spacing, plus text spacing/transform rules.
-   **Spacing & Sizing**: Foundational grid unit (`4px` or `8px`), spacing token
    scale (`--space-1`, `xs`, `sm`, `md`, `lg`, etc.), and standard
    component/layout spacing conventions.
-   **Rounding (Border Radii)**: Corner radius token scale (`--radius-none`
    through `--radius-full`) and application rules per component type.
-   **Elevation & Shadows**: Box shadow scale (`--shadow-sm` through
    `--shadow-2xl`), shadow color/opacity, backdrop blur, border strokes for
    elevation, and z-index layering conventions.
-   **Layout Rules & Density**: Responsive breakpoints (`sm`, `md`, `lg`, `xl`,
    `2xl`), grid systems/column counts, container max-width constraints, and
    overall visual density (compact vs. comfortable).

### 2. Recreate Encountered Components (Component Kit)

Whenever UI components are discovered in the source material, reproduce them as
self-contained static HTML sticker sheet artifacts in `components/` (e.g.,
`components/button.html`, `components/card.html`, `components/input.html`):

-   **Self-Contained HTML Requirement**: Each generated HTML file must have zero
    external dependencies so it can be opened and inspected directly in a
    browser without external stylesheets, CDNs, or JS runtime bundles. Include
    an inline `<style>` block at the top containing a base reset, all extracted
    CSS custom properties (`--color-*`, `--space-*`, etc.), and complete CSS
    class rules for all variants and states.
-   **Exhaustive Variants, Sizes & States**: Every component HTML file must be
    exhaustive and visually represent all discovered permutations in a
    structured grid:
    -   **Variants (Styles)**: Primary, Secondary, Tertiary, Outlined /
        Bordered, Ghost / Text-only, Danger / Destructive, Inverted / Dark.
    -   **Sizes**: Extra Small (`xs`), Small (`sm`), Medium (`md`), Large
        (`lg`), Extra Large (`xl`), Icon-only, Fluid / Full-width.
    -   **Default & Rest States**: Standard resting appearance for each variant
        and size.
    -   **Interactive States**: Hover (via `.is-hover` or `:hover`), Focus /
        Focus-visible (with focus ring/outline), Active / Pressed, and Disabled
        (reduced opacity, `disabled` attribute).
    -   **Feedback & Validation**: Loading / Busy (spinner or skeleton), Error /
        Invalid (red border and helper text), Success / Valid, and Read-only.
    -   **Content Variations**: Leading/trailing icons, badges/counters, helper
        text, truncating long text, and multi-line wrapping.
    -   **Edge & Empty States**: Empty / Zero-state appearances,
        checked/unchecked/indeterminate states, and selected/unselected list
        items.
-   **Visual Layout**: Use clear section headings (`<h2>`, `<h3>`) for each
    dimension and place variations side-by-side in flexbox or grid container
    rows with clear descriptive text labels.

**Strict Citation & Anti-Hallucination Guardrail**: You are strictly prohibited
from using pre-trained parametric memory to guess, assume, or invent design
tokens, hex codes, typography scales, or component styles. Every finding MUST be
backed by an explicit source citation (URL endpoint or file path + line number)
discovered during crawling. If a token or component is not explicitly documented
in the source material, do not invent it.

--------------------------------------------------------------------------------

## Phase 1: Reconnaissance

Classify the input, route to the correct analyzer, and perform a shallow crawl
to discover the full scope of extractable resources.

### 1.1 Classify & Route

Inspect the input reference material and identify the asset type.

#### URL (`url`)

Determine the type of web resource:

URL Subtype               | Description                                                                                  | Analyzer
:------------------------ | :------------------------------------------------------------------------------------------- | :-------
**Design System Docsite** | A dedicated design system portal, brand guidelines site, or component library documentation. | `./analyze-design-system-docs.md`
**Storybook**             | A Storybook instance or interactive component catalog.                                       | `./analyze-storybook.md`
**Git Repository**        | A Git URL (`https://github.com/...` or `git@...`) pointing to a source code repository.      | `./analyze-codebase.md`
**Live Website**          | A general public website, landing page, marketing site, or web application.                  | `./analyze-website.md`

#### Figma File (`figma file`)

When the input is a Figma design file (`.fig`):

-   **Analyzer**: `../../analyze-figma/SKILL.md`

#### Code Files (`code files`)

| Code Subtype         | Description                 | Analyzer                |
| :------------------- | :-------------------------- | :---------------------- |
| **Entire Repo /      | A local directory path      | `./analyze-codebase.md` |
: Directory**          : containing an entire        :                         :
:                      : codebase or frontend        :                         :
:                      : project.                    :                         :
| **Individual Files** | Individual source files     | `./analyze-codebase.md` |
:                      : (`.html`, `.css`, `.scss`,  :                         :
:                      : `.less`, `.js`, `.ts`,      :                         :
:                      : `.tsx`, `.vue`, `.svelte`). :                         :

When multiple sources of **different types** are provided, identify the type for
each source and handle them as separate source groups in the extraction plan.

### 1.2 Discovery Crawl

Read the relevant analyzer sub-skill to understand its discovery procedure, then
perform a **lightweight initial crawl** to discover the full scope of
extractable resources. Do NOT extract content yet — only enumerate resources.

-   **Design System Docsite**: Fetch the hub page, parse
    navigation/sidebar/sitemap. Enumerate all foundation/token pages and
    component documentation pages.
-   **Storybook**: Fetch `/index.json` (Storybook 7+/8+) or `/stories.json`
    (Storybook 6-), or fall back to sidebar inspection. Enumerate all foundation
    stories and component story groups.
-   **Live Website**: Fetch initial URL, identify navigation links, select 10-20
    representative pages that reveal the real product UI.
-   **Codebase**: Clone (if git URL) or locate the directory. Detect framework
    stack, map key directories, and list all relevant component/style files.
-   **Figma**: List pages and frames in the file.

### 1.3 Write Extraction Plan

Write a scratch artifact `extraction-plan.md` listing every discovered resource
as a task row. This is the orchestrator's tracking document.

**Format:**

```markdown
# Extraction Plan: [Source Name]

**Source**: [URL or path]
**Type**: [docsite | storybook | website | codebase | figma]
**Analyzer**: [path to analyzer sub-skill]
**Discovered**: [timestamp]

## Foundation & Token Pages
| # | Resource | Description | Status |
|---|----------|-------------|--------|
| 1 | /colors  | Color palette and semantic roles | ⬜ pending |
| 2 | /typography | Type scale and font families | ⬜ pending |
| ... | | | |

## Component Pages
| # | Resource | Description | Status |
|---|----------|-------------|--------|
| 1 | /components/button | Button variants and states | ⬜ pending |
| 2 | /components/card | Card layouts and interactions | ⬜ pending |
| ... | | | |

## Summary
- Total foundation pages: N
- Total component pages: M
- Total tasks: N + M
```

For multiple sources, create a separate plan section per source.

> [!IMPORTANT] **PHASE 1 → 2 GATE**: You MUST have written the
> `extraction-plan.md` artifact before proceeding to Phase 2. Verify the file
> exists. If it does not exist, you have not
> completed Phase 1.

--------------------------------------------------------------------------------

## Phase 2: Parallel Execution

### 2.1 Batch & Dispatch

Group tasks from the extraction plan into executor batches:

-   **Foundation/Token pages** → 1-2 executor subagents (these tend to be fast)
-   **Component pages** → 1 executor per component page or story group
-   **Maximum 10 concurrent subagents** at any time

For each executor, dispatch a subagent with instructions that include:

1.  **The analyzer sub-skill path** to read (e.g.,
    `./analyze-design-system-docs.md`)
2.  **The specific resource URLs or paths** to process (not the entire manifest
    — only this executor's assigned subset)
3.  **The extraction goals** from this SKILL.md (design tokens format, component
    kit HTML format)
4.  **Output artifact naming convention**:
    -   Design tokens: `extracted-tokens-[source-slug].md`
    -   Component sticker sheets: `[component-name].html`
5.  **Instructions to write artifacts** and return a
    completion report listing all created artifacts

**Executor Prompt Template:**

```
You are a design system extraction executor. Read the analyzer sub-skill
at [analyzer path], then follow its instructions to
extract design tokens and component sticker sheets from the following
resources:

Resources to process:
- [URL 1]
- [URL 2]
- ...

Write your outputs as artifacts:
- Design tokens → extracted-tokens-[source].md
- Component HTML sticker sheets → [component-name].html

Follow the extraction goals and anti-hallucination rules from the
orchestrator skill. Every finding MUST cite its source URL or file path.

When complete, respond with a structured completion report:
## Completion Report
- Artifacts created: [list of file paths]
- Tokens extracted: [count]
- Components extracted: [list of component names]
- Issues encountered: [any problems or gaps]
```

### 2.2 Track Completion

As each executor subagent completes:

1.  Read its completion report
2.  Update the extraction plan artifact: mark the corresponding rows as ✅
    completed
3.  Record the output artifact paths
4.  If the executor reports errors or gaps, mark the row as ❌ failed with a note

### 2.3 Coverage Check

After all dispatched executors complete, review the extraction plan:

-   If any rows are still ⬜ pending — these were missed. Dispatch new executors
    for them.
-   If any rows are ❌ failed — attempt to re-dispatch once. If they fail again,
    note the gap and proceed.
-   If all rows are ✅ completed — proceed to Phase 3.

> [!IMPORTANT] **PHASE 2 → 3 GATE**: Before proceeding to Phase 3, verify
> that: 1. ALL rows in the extraction plan are ✅ completed. 2. At least one
> `extracted-tokens-*.md` artifact exists. 3. At least one component `*.html`
> sticker sheet artifact exists. If any of these checks fail, re-dispatch
> executors or investigate the failure.

--------------------------------------------------------------------------------

## Phase 3: Gather & Synthesize

### 3.1 Verify Intermediate Artifacts

Confirm that all expected intermediate artifacts exist in the workspace:

-   At least one design token markdown artifact (`extracted-tokens-*.md`)
-   Component HTML sticker sheet artifacts (one `.html` per discovered component
    kind)

List all artifacts and cross-reference against the extraction plan. If critical
artifacts are missing, re-dispatch executors.

### 3.2 Create the design system

Once all intermediate artifacts are verified, follow the `design-system` skill
to produce the final design system, then the `component-kit` skill:

-   `DESIGN.md` — Design system document with tokens and prose
-   `tailwind.config.js` — Tailwind CSS config derived from tokens
-   Component Kit (`components/*.html`) — Canonical component reference files

Pass all extracted token artifacts and component sticker sheets as context to
faithfully recreate the user's existing design style as a complete design
system.

--------------------------------------------------------------------------------

## Expected Output

At the end of a complete extraction run, the workspace should contain:

**Intermediate artifacts** (from executors):

-   `extracted-tokens-*.md` — design token markdown with source citations
-   `*.html` component sticker sheets from source material

**Final artifacts** (from `design-system` and `component-kit`):

-   `DESIGN.md` — the complete design system document
-   `tailwind.config.js` — Tailwind theme config
-   Component Kit `components/*.html` — canonical component reference files
