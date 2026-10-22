---
name: google-material-3-web-prototype
description: Create professional grade web prototypes using Google Material 3(google-material-3) design system.
---

# Google Material 3 Web Prototype

This Skill guides LLMs in creating high-fidelity, production-grade web prototypes using the Google Material 3 (google-material-3) design system and gBreeze component library.

## Design System Overview

Google Material 3 is Google's flagship design system. It provides a flexible, expressive visual language built around dynamic color, modern adaptive typography, stateful interaction feedback, and responsive layout structures.

When prototyping for the web using Material 3:

* All UI styling is governed by Material Design System tokens (`--md-sys-*`). Hardcoding colors, font sizes, margins, or radii using raw literals is prohibited.
* UI components are built using gBreeze custom Lit elements (`<md-gb-*>`) and standard Material Web Component (`<md-*>`) fallbacks.
* Layouts respond dynamically across screen sizes using standard 8dp grid spacing units and adaptive navigation scaffolding.

## Core Concepts & Big Ideas

* **Token-Driven Architecture**: Visual style properties are defined through semantic design tokens as CSS variables (`--md-sys-color-*`, `--md-sys-typescale-*`, `--md-sys-space-*`, `--md-sys-shape-*`).
* **gBreeze Component Ecosystem**: gBreeze provides custom web components (`<md-gb-button>`, `<md-gb-card>`, `<md-gb-list>`, `<md-gb-app-bar>`, etc.) that natively consume Material tokens and support rapid interactive prototyping.
* **Dynamic Color Roles**: Surfaces and interactive controls derive colors from semantic roles (Primary, Secondary, Tertiary, Surface Container tiers) with built-in contrast compliance and light/dark theme support (`light-dark()`).
* **Expressive Variable Typography**: Typography scale uses `Google Sans` and `Google Sans Flex` variable fonts with pre-configured typescale tokens for Display, Headline, Title, Body, and Label roles.
* **Adaptive Navigation & Scaffolding**: Layouts adapt dynamically across device sizes using standard navigation components (Navigation Bar, Navigation Rail, Navigation Drawer).

## Tone

The tone of Material 3 web prototypes is modern, expressive, accessible, dynamic, clean, and unmistakably Google. Interfaces should feel intuitive, light, functional, and visually harmonious with subtle rounded corners and purposeful color accents.

## Guiding Principles

* **Use Design Tokens Exclusively**: Never use raw hex colors (`#0b57d0`), pixel font-sizes (`16px`), or arbitrary padding values in custom styles. Always use `--md-sys-*` tokens.
* **Maintain Color Role Semantics**: Foreground text and icons must always match the background role (e.g., place `--md-sys-color-on-primary` on `--md-sys-color-primary`, and `--md-sys-color-on-surface` on `--md-sys-color-surface`).
* **Prefer gBreeze Web Components**: Use gBreeze controls (`<md-gb-button>`, `<md-gb-card>`, `<md-gb-chip>`, etc.) for all primary interactions. Fall back to standard `@material/web` controls (`<md-outlined-text-field>`, `<md-dialog>`) when gBreeze equivalents do not exist.
* **Ensure Accessibility & Keyboard Focus**: Include proper ARIA attributes, semantic HTML markup, and interactive focus states via `<md-focus-ring>`.
* **Design for Adaptive Responsive Web**: Organize layouts using flexible flexbox and grid structures mapped to 8dp spacing tokens (`--md-sys-space-*`).

## How to Prototype

To generate a standalone Material 3 web prototype:

1. **Setup Document Structure**: Create a standard HTML5 document containing the required importmaps, stylesheet links, and script tags.
2. **Link Design System Bindings**: Copy `assets/design-system-bindings.css` into the user's project root and link it in `<head>`.
3. **Import gBreeze & Web Components**: Import required component JS modules in a `<script type="module">` tag.
4. **Construct Layout with Tokens**: Build the body structure using gBreeze components and custom HTML styled with `--md-sys-*` tokens.

### Prototyping Boilerplate

Use the following standard HTML boilerplate to initialize any Material 3 web prototype:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Material 3 Web Prototype</title>

  <!-- Importmap for @material/web, Lit, and dependencies -->
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

  <!-- Tailwind CSS setup -->
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

  <!-- Design system tokens & stylesheet bindings -->
  <link rel="stylesheet" href="./design-system-bindings.css">

  <!-- gBreeze Component Imports -->
  <script type="module">
    import '@material/web/labs/gb/components/button/md-gb-button.js';
    import '@material/web/labs/gb/components/iconbutton/md-gb-icon-button.js';
    import '@material/web/labs/gb/components/card/md-gb-card.js';
    import '@material/web/labs/gb/components/list/md-gb-list.js';
    import '@material/web/labs/gb/components/list/md-gb-list-item.js';
    import '@material/web/labs/gb/styles/icon/md-gb-icon.js';
  </script>

  <!-- Standard Material Web Component Fallbacks (if needed) -->
  <script type="module">
    import '@material/web/textfield/outlined-text-field.js';
    import '@material/web/dialog/dialog.js';
  </script>
</head>
<body style="background-color: var(--md-sys-color-surface); color: var(--md-sys-color-on-surface); margin: 0; font: var(--md-sys-typescale-body-medium);">
  
  <main style="padding: var(--md-sys-space-300);">
    <md-gb-card color="surface-container" style="padding: var(--md-sys-space-300); max-width: 600px; margin: 0 auto;">
      <h1 style="font: var(--md-sys-typescale-headline-medium); margin-top: 0; color: var(--md-sys-color-on-surface);">Welcome to Material 3</h1>
      <p style="font: var(--md-sys-typescale-body-large); color: var(--md-sys-color-on-surface-variant);">
        This prototype demonstrates Google Material 3 tokens bound to gBreeze elements.
      </p>
      <div style="display: flex; gap: var(--md-sys-space-100); margin-top: var(--md-sys-space-200);">
        <md-gb-button color="filled">Primary Action</md-gb-button>
        <md-gb-button color="outlined">Secondary Action</md-gb-button>
      </div>
    </md-gb-card>
  </main>

</body>
</html>
```

## Design System Bindings (`design-system-bindings.css`)

The file [design-system-bindings.css](assets/design-system-bindings.css) defines the core runtime CSS custom properties (`--md-sys-*`) for the Material 3 design system. It imports Google Sans fonts, Google Symbols icon fonts, gBreeze base styles, dynamic `light-dark()` color tokens, typescale values, spacing definitions, corner shape rules, and gBreeze CSS bindings.

### Setup & Project Linkage

When creating a standalone web prototype:

* Copy `assets/design-system-bindings.css` verbatim into the root directory of the user's generated project (as `design-system-bindings.css`).
* Link the file in the HTML `<head>` section: `<link rel="stylesheet" href="./design-system-bindings.css">`.

### LLM Context Guidance

* **DO NOT** attempt to read `assets/design-system-bindings.css` into context to look up CSS variable names.
* Rely on the structured token tables, rules, and breadcrumb references documented directly in `SKILL.md` and `references/*.md`.

## Primary Color Tokens Reference

Prototyping components consume Material tokens automatically. For custom styling or card containers, use these baseline color tokens:

### Accent Roles

* `--md-sys-color-primary`: Main theme accent for prominent buttons, active states, and key highlights.
* `--md-sys-color-on-primary`: Text/icon color on Primary background.
* `--md-sys-color-primary-container`: Soft highlighted background for key cards, badges, or selected items.
* `--md-sys-color-on-primary-container`: Text/icon color on Primary Container.
* `--md-sys-color-secondary`: Less prominent accent for secondary controls and filter chips.
* `--md-sys-color-on-secondary`: Text/icon color on Secondary background.
* `--md-sys-color-secondary-container`: Background for secondary containers and tonal buttons.
* `--md-sys-color-on-secondary-container`: Text/icon color on Secondary Container.
* `--md-sys-color-tertiary`: Vibrant contrasting accent for AI highlights, notifications, or callouts.
* `--md-sys-color-on-tertiary`: Text/icon color on Tertiary background.
* `--md-sys-color-tertiary-container`: Background for AI response boxes, prompt suggestions, or callout cards.
* `--md-sys-color-on-tertiary-container`: Text/icon color on Tertiary Container.

### Surface & Elevation Roles

* `--md-sys-color-surface`: Main screen background and default card surface.
* `--md-sys-color-on-surface`: Default text and dark icons on surface backgrounds.
* `--md-sys-color-on-surface-variant`: Muted text, subtitles, secondary icons, and disabled states.
* `--md-sys-color-surface-container-lowest`: Lowest surface container (pure white in light mode).
* `--md-sys-color-surface-container-low`: Low container elevation tier for grouped cards.
* `--md-sys-color-surface-container`: Standard container elevation tier for cards, dialogs, and side sheets.
* `--md-sys-color-surface-container-high`: High container elevation tier for top app bars or floating cards.
* `--md-sys-color-surface-container-highest`: Highest container elevation tier for active item backgrounds and search fields.

### Borders & Utility Roles

* `--md-sys-color-outline`: Standard boundary color for outlined text fields, card borders, and buttons (3:1 contrast ratio).
* `--md-sys-color-outline-variant`: Subtle divider color and card separators.
* `--md-sys-color-error`: Error color for invalid text fields, error badges, and alert banners.
* `--md-sys-color-on-error`: Text/icon color on Error background.
* `--md-sys-color-error-container`: Soft background for error banners and validation messages.
* `--md-sys-color-on-error-container`: Text/icon color on Error Container.

## Primary Typography Tokens Reference

Use the `font:` shorthand with typescale tokens to apply typography directly to HTML elements:

### Typescale Tokens

* `--md-sys-typescale-display-large`: Large display text (3.5625rem / 4rem line height, Google Sans).
* `--md-sys-typescale-display-medium`: Medium display text (2.8125rem / 3.25rem line height, Google Sans).
* `--md-sys-typescale-display-small`: Small display text (2.25rem / 2.75rem line height, Google Sans).
* `--md-sys-typescale-headline-large`: Large section title (2rem / 2.5rem line height, Google Sans).
* `--md-sys-typescale-headline-medium`: Medium section title (1.75rem / 2.25rem line height, Google Sans).
* `--md-sys-typescale-headline-small`: Small section title (1.5rem / 2rem line height, Google Sans).
* `--md-sys-typescale-title-large`: Card title / page header (1.375rem / 1.75rem line height, Google Sans).
* `--md-sys-typescale-title-medium`: Subhead / list title (1rem / 1.5rem line height, 500 weight, Google Sans Text).
* `--md-sys-typescale-title-small`: Dense list title (0.875rem / 1.25rem line height, 500 weight, Google Sans Text).
* `--md-sys-typescale-body-large`: Primary body copy (1rem / 1.5rem line height, Google Sans Text).
* `--md-sys-typescale-body-medium`: Standard body copy (0.875rem / 1.25rem line height, Google Sans Text).
* `--md-sys-typescale-body-small`: Caption / helper text (0.75rem / 1rem line height, Google Sans Text).
* `--md-sys-typescale-label-large`: Button text / tab label (0.875rem / 1.25rem line height, 500 weight, Google Sans Text).
* `--md-sys-typescale-label-medium`: Badge label / sub-caption (0.75rem / 1rem line height, 500 weight, Google Sans Text).
* `--md-sys-typescale-label-small`: Tiny status tag (0.6875rem / 1rem line height, 500 weight, Google Sans Text).

### Iconography Rules

* Use `<md-gb-icon>` elements for Material Symbols icons (e.g. `<md-gb-icon>search</md-gb-icon>`).
* Always size icons using the `--md-icon-size` custom property (e.g., `<md-gb-icon style="--md-icon-size: 24px">settings</md-gb-icon>`).
* **CRITICAL**: Do **NOT** apply `.typescale-*` utility classes or custom `font-family` CSS properties to icon elements (`<md-gb-icon>` or `.md-icon`). Doing so overrides the `Google Symbols` font family and renders icons as plain text ligatures instead of symbols.

## Primary Spacing, Shape & Elevation Tokens Reference

### Spacing Scale Tokens

* `--md-sys-space-0`: 0px
* `--md-sys-space-25`: 2px
* `--md-sys-space-50`: 4px
* `--md-sys-space-75`: 6px
* `--md-sys-space-100`: 8px (base unit)
* `--md-sys-space-125`: 10px
* `--md-sys-space-150`: 12px
* `--md-sys-space-200`: 16px
* `--md-sys-space-250`: 20px
* `--md-sys-space-300`: 24px
* `--md-sys-space-400`: 32px
* `--md-sys-space-500`: 40px
* `--md-sys-space-600`: 48px
* `--md-sys-space-800`: 64px

### Corner Shape Tokens

* `--md-sys-shape-corner-xs`: 4px (extra small - text fields, tooltips)
* `--md-sys-shape-corner-sm`: 8px (small - chips, snackbars)
* `--md-sys-shape-corner-md`: 12px (medium - cards, menus)
* `--md-sys-shape-corner-lg`: 16px (large - dialogs, floating panels)
* `--md-sys-shape-corner-xl`: 28px (extra large - side sheets, floating action buttons)
* `--md-sys-shape-corner-full`: Pill shape / fully rounded (buttons, search bars, badges)

### Elevation Tokens

* `--md-sys-elevation-level0`: Flat / flush surface (0px shadow)
* `--md-sys-elevation-level1`: Low elevation card / list item (1px shadow)
* `--md-sys-elevation-level2`: Hovered card / tonal container (3px shadow)
* `--md-sys-elevation-level3`: Dialog / popover menu (6px shadow)
* `--md-sys-elevation-level4`: Navigation bar / top bar (8px shadow)
* `--md-sys-elevation-level5`: Floating modal sheet / FAB menu (12px shadow)

## Reference Breadcrumbs

When deeper design system details or component documentation are required during prototyping, load the following references:

* **Pull [Color](references/color.md)** when designing custom color schemes, detailed tonal palettes, dynamic light/dark mode overrides, or specialized surface tinting.
* **Pull [Typography](references/typography.md)** when configuring custom font variation axes (`Google Sans Flex`), fine-tuning line heights/letter spacing, or setting up specialized editorial typography.
* **Pull [Layout](references/layout.md)** when building complex responsive layouts, breakpoint-specific navigation transitions, adaptive grid structures, or app scaffold architectures.
* **Pull [Components](references/components.md)** when looking up specific HTML tag syntax, component attributes, slots, events, gBreeze custom elements, or Material Web fallback controls.

## Reporting Issues

Report bugs or improvements for this skill at the
[GDP Skills](http://b/issues/new?component=2279477) component.
