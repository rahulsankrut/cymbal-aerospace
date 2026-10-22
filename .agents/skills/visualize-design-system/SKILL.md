---
name: visualize-design-system
description: >-
  Create a self-contained desktop HTML stickersheet (1280x800) visualizing
  a design system: colors, typography levels, and key components with variants.
---

# Visualize Design System

## Goal

Create a single, self-contained desktop HTML stickersheet (`design-system.html`) that visualizes the design system with high craft.

- **Canvas Form Factor**: Desktop viewport 1280px wide (`w-[1280px]`).
- **Above the Fold**: The most important information (header/brand identity, core color palette, typography hierarchy snapshot, flagship CTA components) **MUST fit above the fold** (first 800px height).
- **Below the Fold**: Detailed color tokens, full typography scale, and key component variant showcases (scrolling permitted).

Write the output artifact to your own workspace root as `design-system.html`, then message the parent agent the absolute path to the file.

## Workflow

### 1. Read Inputs

Read all reference files for the design system:

- `DESIGN.md` (from path provided in prompt) — Overview, color tokens (Section 2), typography levels (Section 3), shape and elevation strategies.
- `tailwind.config.js` (from workspace) — Theme tokens (colors, fonts, sizes, radii).
- Component `.html` files (`button.html`, `card.html`, `input.html`, etc.) from the provided components directory.
- Unstyled layout template at `./references/template.html` (relative to this skill).

### 2. Prepare and Style the Template

Use `./references/template.html` as the layout skeleton so you do not need to invent layout composition:

- Preserve the 1280px width, grid layouts, and above-the-fold organization.
- Inject the theme config from `tailwind.config.js` into `<script>tailwind.config = { ... }</script>`.
- Add Google Fonts `<link>` tags for the font families declared in the design system.
- Set page background and base text colors using the design system's theme tokens.
- Style all template containers, cards, and section dividers using the design system's background/surface colors, borders, border radii, and elevation/depth tokens per `DESIGN.md`.

### 3. Populate Content

- **Colors (from `DESIGN.md`)**:
  - *Above the fold*: Core palette swatches (primary, secondary, key neutral/accent swatches as defined in the design system) with token names, hex codes, and text contrast previews.
  - *Below the fold*: Full palette of color tokens defined in the design system.
- **Typography Levels (from `DESIGN.md`)**:
  - *Above the fold*: Hierarchy snapshot (key heading and body levels defined in the design system) rendered in their respective styles.
  - *Below the fold*: Full typography scale with token names, metrics (font family, size, weight, line-height), and rendered sample text.
- **Key Components & Variants (strictly from component `.html` files)**:
  - Copy the exact HTML markup and classes from the component `.html` files. Do NOT invent new component markup.
  - Pick salient variants from each component file to showcase.
  - Place 1-2 flagship components in the above-the-fold preview slot; showcase remaining component categories in the below-the-fold showcase sections.

### 4. Output and Notify

1. Write an artifact `design-system.html`.
2.  Send a message to the parent agent with the absolute path to
    `design-system.html`.
