---
name: workspace-design-system-web-prototype
description: Create professional grade web prototypes using Workspace Design System(workspace-design-system) design system.
---

# Workspace Design System Web Prototype Skill

This Skill guides LLM agents in generating professional-grade web prototypes that adhere strictly to the Workspace Design System (`workspace-design-system`).

## Core Concept and Big Ideas

Workspace Design System (`workspace-design-system`) is an AI-first web design system. Component primitives are powered by gBreeze, a set of Lit-based web components built on `@material/web` that consume design system tokens via CSS custom properties.

Key concepts include:

- Token-driven architecture: Design decisions are expressed via standard CSS custom properties prefixed with `--ws-sys-*` and automatically bound to `--md-sys-*`.
- Web Component primitives: Web prototyping relies on `<md-gb-*>` custom elements (e.g., `<md-gb-button>`, `<md-gb-card>`, `<md-gb-list>`).
- Fallback component model: When a specific `md-gb-*` element is unavailable, prototypes fall back to standard `@material/web` custom elements (`<md-*>`, e.g., `<md-outlined-text-field>`, `<md-dialog>`).
- AI-native UI surfaces: Integrated support for Gemini gems color schemes, Aurora gradients, AI status indicators (`<md-gb-processing-indicator>`), and follow-up prompt suggestions (`<md-gb-suggestion>`).

## Tone

The visual tone of Workspace Design System user interfaces is:

- Professional and clean: Structured layouts, crisp alignment, clear typographic hierarchy.
- Modern and fluid: Subtle motion transitions, rounded surface shapes, adaptive responsive layouts.
- Functional and accessible: High contrast text pairings, clear state indicators, structured keyboard focus rings.

## Guiding Principles

- Token First: Always use CSS design system variables (`var(--ws-sys-*)` or bound `var(--md-sys-*)`) rather than hardcoded hex codes, pixel font sizes, or inline magic values.
- Web Components First: Use `md-gb-*` custom elements as primary UI building blocks, falling back to standard `@material/web` components (`md-*`) when needed.
- No Manual CSS Reading: Rely on the token tables and guidance in `SKILL.md` and `references/*.md`. Do NOT read `assets/design-system-bindings.css` into context during prototype generation.
- Responsive Setup: Utilize Tailwind CSS classes alongside gBreeze Web Components for outer layout grids, flex containers, and responsive breakpoint alignment.

## How to Prototype

To generate a web prototype adhering to Workspace Design System:

- Include the complete HTML setup template in your prototype output.
- Always link `design-system-bindings.css` in the `<head>` block of your prototype document.
- Copy `assets/design-system-bindings.css` verbatim into the project root directory when producing standalone prototype builds.
- Rely on gBreeze custom elements (`<md-gb-button>`, `<md-gb-card>`, `<md-gb-icon-button>`, etc.) and standard Material Web fallbacks (`<md-outlined-text-field>`, `<md-dialog>`).
- Apply color, shape, typography, elevation, and motion using CSS variables (`var(--ws-sys-*)`).

## Design System Bindings

The file [design-system-bindings.css](assets/design-system-bindings.css) establishes all system design tokens as CSS variables under `:root, :host` and binds them directly to gBreeze `--md-sys-*` component variables.

When creating a full standalone prototype:

- Copy `assets/design-system-bindings.css` verbatim into the root directory of the user's project.
- Link the stylesheet in the HTML `<head>` block using `<link rel="stylesheet" href="./design-system-bindings.css">`.
- Do NOT instruct the LLM agent to read `assets/design-system-bindings.css` into context to look up variables; rely on the token tables and guidelines in `SKILL.md` and `references/*.md` instead.

## Prototype Starter Template

Use this HTML boilerplate as the starting structure for web prototypes:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Workspace Web Prototype</title>

  <!-- Import Map for gBreeze & Dependencies -->
  <script type="importmap">
  {
    "imports": {
      "@material/web/": "https://unpkg.com/@material/web@nightly/",
      "tslib": "https://unpkg.com/tslib/tslib.es6.js",
      "lit": "https://unpkg.com/lit",
      "lit/": "https://unpkg.com/lit/",
      "@lit/": "https://unpkg.com/@lit/",
      "@lit-labs/": "https://unpkg.com/@lit-labs/",
      "lit-html": "https://unpkg.com/lit-html",
      "lit-html/": "https://unpkg.com/lit-html/",
      "lit-element/": "https://unpkg.com/lit-element/",
      "safevalues/dom": "https://unpkg.com/safevalues/dist/mjs/dom/index.js"
    }
  }
  </script>

  <!-- Setup Tailwind CSS -->
  <script type="module" src="https://unpkg.com/@tailwindcss/browser"></script>
  <style type="text/tailwindcss">
    @layer properties, theme, base, md, components, utilities;
  </style>
  <script type="module">
    const response = await fetch('https://unpkg.com/@material/web@nightly/labs/gb/styles/tailwind.css');
    const style = document.createElement('style');
    style.type = 'text/tailwindcss';
    style.textContent = await response.text();
    document.head.appendChild(style);
  </script>

  <!-- Design System Token Bindings -->
  <link rel="stylesheet" href="./design-system-bindings.css">

  <!-- Import gBreeze Web Components -->
  <script type="module">
    import '@material/web/labs/gb/components/button/md-gb-button.js';
    import '@material/web/labs/gb/components/iconbutton/md-gb-icon-button.js';
    import '@material/web/labs/gb/components/card/md-gb-card.js';
    import '@material/web/labs/gb/components/list/md-gb-list.js';
    import '@material/web/labs/gb/components/list/md-gb-list-item.js';
    import '@material/web/labs/gb/styles/icon/md-gb-icon.js';
  </script>

  <!-- Google Internal / All Components Bundle -->
  <script src="https://static.corp.google.com/material-web/gbreeze/latest/components/md-gb-all.js"></script>
</head>
<body class="bg-[var(--ws-sys-color-primary-text)]/5 text-[var(--ws-sys-color-primary-text)] min-h-screen p-6">
  <main class="max-w-4xl mx-auto space-y-6">
    <md-gb-card>
      <div class="p-6 space-y-4">
        <h1 class="font-['Google_Sans'] text-2xl font-medium text-[var(--ws-sys-color-primary)]">
          Prototype Overview
        </h1>
        <p class="font-['Google_Sans_Text'] text-body-md text-[var(--ws-sys-color-primary-text)]">
          Welcome to the Workspace Design System prototype.
        </p>
        <div class="flex gap-3">
          <md-gb-button color="filled">Primary Action</md-gb-button>
          <md-gb-button color="outlined">Secondary Action</md-gb-button>
        </div>
      </div>
    </md-gb-card>
  </main>
</body>
</html>
```

## Primary Color Roles Overview

Prototyping components consume Material tokens out of the box. For standard UI layouts, use the key color roles below:

| Color Role Token | Usage & Context | Value |
| --- | --- | --- |
| `--ws-sys-color-primary` | Main accent and action color for buttons, active states, key headings | `light-dark(#0b57d0, #a8c7fa)` |
| `--ws-sys-color-on-primary` | Text & icons displayed on top of `--ws-sys-color-primary` fill | `light-dark(#ffffff, #062e6f)` |
| `--ws-sys-color-primary-container` | Standout background container for key components & cards | `light-dark(#d3e3fd, #0842a0)` |
| `--ws-sys-color-on-primary-container` | Text & icons displayed on top of primary container | `light-dark(#041e49, #d3e3fd)` |
| `--ws-sys-color-secondary` | Secondary emphasis actions, badges, tonal accents | `light-dark(#00639b, #7fcfff)` |
| `--ws-sys-color-on-secondary` | Text & icons displayed on top of secondary fill | `light-dark(#ffffff, #003355)` |
| `--ws-sys-color-secondary-container` | Less prominent container surface (tonal buttons, chips) | `light-dark(#c2e7ff, #004a77)` |
| `--ws-sys-color-on-secondary-container` | Text & icons displayed on top of secondary container | `light-dark(#001d35, #c2e7ff)` |
| `--ws-sys-color-tertiary` | Alternative highlight color for inputs or special status accents | `light-dark(#146c2e, #6dd58c)` |
| `--ws-sys-color-tertiary-container` | Input container backgrounds and soft callouts | `light-dark(#c4eed0, #0f5223)` |
| `--ws-sys-color-primary-text` | Default body and headline text color | `light-dark(#1f1f1f, #e3e3e3)` |
| `--ws-sys-color-secondary-text` | Subtitles, captions, and secondary metadata text | `light-dark(#ffffff, #003355)` |
| `--ws-sys-color-outline` | Borders and outlines for fields, cards, chips, and dividers | `light-dark(#747775, #8e918f)` |
| `--ws-sys-color-divider` | Layout borders and section dividers | `#c4c7c5` |

**Pull [Color](references/color.md)** when you need extended color palettes (blue, cyan, green, grey, orange, pink, purple, red, yellow), GenAI aurora gradients (`--ws-sys-color-genai-*`), Gemini gems surfaces (`--ws-sys-color-genai-gems-*`), illustration color schemes, or dark mode pairing details.

## Primary Typographic Roles Overview

Typography uses two main font families: `Google Sans` for brand display and headings, and `Google Sans Text` for body and UI controls.

| Typescale Token | Font Family | Size / Line Height | Role & Application |
| --- | --- | --- | --- |
| `--ws-sys-typescale-display-large` | `Google Sans` | `3.5625rem / 4rem` | Hero headlines and splash titles |
| `--ws-sys-typescale-display-medium` | `Google Sans` | `2.8125rem / 3.25rem` | Primary landing page headlines |
| `--ws-sys-typescale-display-small` | `Google Sans` | `2.25rem / 2.75rem` | Major section headers |
| `--ws-sys-typescale-headline-large` | `Google Sans` | `2rem / 2.5rem` | Screen and modal header titles |
| `--ws-sys-typescale-headline-medium` | `Google Sans` | `1.75rem / 2.25rem` | Card and drawer titles |
| `--ws-sys-typescale-headline-small` | `Google Sans` | `1.5rem / 2rem` | Sub-section headings |
| `--ws-sys-typescale-title-large` | `Google Sans` | `1.375rem / 1.75rem` | Container titles & dialog titles |
| `--ws-sys-typescale-title-medium` | `Google Sans Text` | `500 1rem / 1.5rem` | List item titles & group headers |
| `--ws-sys-typescale-title-small` | `Google Sans Text` | `500 0.875rem / 1.25rem` | Dense list headers & subtitles |
| `--ws-sys-typescale-body-large` | `Google Sans Text` | `1rem / 1.5rem` | Long-form body paragraph text |
| `--ws-sys-typescale-body-medium` | `Google Sans Text` | `0.875rem / 1.25rem` | Standard body copy & descriptions |
| `--ws-sys-typescale-body-small` | `Google Sans Text` | `0.75rem / 1rem` | Helper text & inline captions |
| `--ws-sys-typescale-label-large` | `Google Sans Text` | `500 0.875rem / 1.25rem` | Button text & tab labels |
| `--ws-sys-typescale-label-medium` | `Google Sans Text` | `500 0.75rem / 1rem` | Chip text & navigation labels |
| `--ws-sys-typescale-label-small` | `Google Sans Text` | `500 0.6875rem / 1rem` | Badges & tiny metadata labels |

### Iconography Guidance

- Render icons using `<md-gb-icon>` loaded from `@material/web/labs/gb/styles/icon/md-gb-icon.js`.
- Always size `<md-gb-icon>` using the `--md-icon-size` CSS variable, e.g.:
  `<md-gb-icon style="--md-icon-size: 20px">search</md-gb-icon>`
- **CRITICAL**: Do NOT place `.typescale-*` classes on `<md-gb-icon>`. Typescale classes set `font-family: "Google Sans Flex"`, which overwrites `font-family: "Google Symbols"` and renders icons as raw text glyphs.

**Pull [Typography](references/typography.md)** when you need complete letter-spacing / tracking values, font weight options, typescale shorthand breakdowns, or custom font loader imports.

## Layout, Shape, and Motion Overview

- **Shape**: Surface corners use `--ws-sys-shape-corner-*` tokens. Standard components use `--ws-sys-shape-corner-medium` (`12px`) for cards, `--ws-sys-shape-corner-large` (`16px`) for drawers, and `--ws-sys-shape-corner-full` for pills and buttons.
- **Elevation**: Shadow depth uses `--ws-sys-elevation-level0` (`0`) to `--ws-sys-elevation-level5` (`12px`).
- **Motion**: Transitions use `--ws-sys-motion-duration-*` (short, medium, long, extra-long) paired with `--ws-sys-motion-easing-standard` or `--ws-sys-motion-emphasized`.

**Pull [Layout](references/layout.md)** when building multi-column application shells, top app bars, navigation rails, bottom navigation bars, or responsive breakpoint grid systems.

**Pull [Motion and Shape](references/motion-and-shape.md)** when customizing corner roundedness, top/end corner clippings, elevation levels, motion duration scales, or easing curves.

## Component Library Overview

gBreeze custom elements provide out-of-the-box styling bound to Workspace Design System tokens. Primary component categories include:

- Actions: `<md-gb-button>`, `<md-gb-icon-button>`, `<md-gb-fab>`, `<md-gb-split-button>`, `<md-gb-button-group>`, `<md-gb-chip>`, `<md-gb-badge>`
- Form Controls: `<md-gb-checkbox>`, `<md-gb-radio>`, `<md-gb-slider>`, `<md-gb-switch>`
- Layout & Containers: `<md-gb-app-bar>`, `<md-gb-card>`, `<md-gb-divider>`, `<md-gb-list>`, `<md-gb-menu>`, `<md-gb-nav-bar>`, `<md-gb-nav-rail>`, `<md-gb-tabs>`
- AI & Status: `<md-gb-processing-indicator>`, `<md-gb-suggestion>`, `<md-gb-suggestion-group>`
- MWC Fallbacks: `<md-outlined-text-field>`, `<md-filled-text-field>`, `<md-outlined-select>`, `<md-dialog>`, `<md-circular-progress>`, `<md-linear-progress>`

**Pull [Components](references/components.md)** when implementing specific component variations, slot parameters, event handlers, or detailed component code examples.

## Reporting Issues

Report bugs or improvements for this skill at the
[GDP Skills](http://b/issues/new?component=2279477) component.
