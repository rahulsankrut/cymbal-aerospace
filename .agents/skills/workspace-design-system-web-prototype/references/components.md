# Component Reference

This document defines the web component library for Workspace Design System prototypes.

> **MANDATORY COMPONENT LIBRARY DIRECTIVE**: When generating web prototypes for Workspace Design System, you **MUST** strictly use the **gBreeze** component library (`md-gb-*` custom elements) and standard `@material/web` fallbacks as specified in this reference. Do NOT use standard unstyled HTML elements, generic third-party UI libraries (Bootstrap, Material-UI, Chakra), or custom element names from other design systems.

> **STRICT API GUIDANCE & WARNING**:
> **DO NOT GUESS COMPONENT APIS, ATTRIBUTES, SLOTS, OR EVENT NAMES.** gBreeze custom elements have precise attribute types, slot names, and sizing rules that differ from standard HTML and other web component libraries. Before generating code for any component, you **MUST** explicitly pull and read its dedicated reference file. Guessing component APIs leads to broken UI layout, unrendered slots, and invalid markup.

## Component Library Overview

**gBreeze** is a set of Lit-based web components in `@material/web/labs/gb` designed for high-fidelity AI-assisted web prototyping.

Key characteristics of gBreeze:

- **Custom Element Prefix**: All gBreeze components use the `md-gb-` tag prefix (e.g., `<md-gb-button>`, `<md-gb-card>`, `<md-gb-list>`).
- **Token-Bound Styling**: gBreeze elements do NOT define fixed design values internally. They consume Workspace Design System tokens via CSS custom properties (`--md-sys-*` bound to `--ws-sys-*`).
- **Composable Layers**: Components use native shadow DOM with standard `<slot>` elements, `@layer` blocks, and `::part()` selectors.
- **Fallback Architecture**: When a specific gBreeze element is not available, prototypes fall back to standard `@material/web` elements (`<md-outlined-text-field>`, `<md-dialog>`, `<md-circular-progress>`).
- **AI-Native Surfaces**: Built-in support for AI status indicators (`<md-gb-processing-indicator>`), prompt suggestions (`<md-gb-suggestion>`), and aurora energy surfaces (`<md-gb-energy>`).

## Complete Prototype Setup Instructions

When creating a full standalone prototype, initialize your document with the importmaps, Tailwind stylesheet imports, design token bindings, and component script dependencies shown below.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Workspace Web Prototype</title>

  <!-- Install gBreeze Dependencies via CDN Importmap -->
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

  <!-- Setup Tailwind CSS Browser Build -->
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

  <!-- Link Workspace Design System Token Bindings -->
  <link rel="stylesheet" href="./design-system-bindings.css">

  <!-- Import Standard gBreeze Modules -->
  <script type="module">
    import '@material/web/labs/gb/components/button/md-gb-button.js';
    import '@material/web/labs/gb/components/iconbutton/md-gb-icon-button.js';
    import '@material/web/labs/gb/components/card/md-gb-card.js';
    import '@material/web/labs/gb/components/list/md-gb-list.js';
    import '@material/web/labs/gb/components/list/md-gb-list-item.js';
    import '@material/web/labs/gb/styles/icon/md-gb-icon.js';
  </script>

  <!-- Google-Internal Self-Registering Bundle (md-gb-processing-indicator, md-gb-suggestion, md-gb-energy) -->
  <!-- Always load with plain <script src>, NEVER inside type="module" or importmap -->
  <script src="https://static.corp.google.com/material-web/gbreeze/latest/components/md-gb-all.js"></script>
</head>
<body class="bg-surface text-on-surface min-h-screen p-6">
  <main class="max-w-4xl mx-auto">
    <md-gb-card>
      <div class="p-6">
        <h1 class="typescale-headline-medium text-primary">Prototype Active</h1>
      </div>
    </md-gb-card>
  </main>
</body>
</html>
```

### Script Tag Loading Rules

- **Importmap Modules**: Load public gBreeze elements (`<md-gb-button>`, `<md-gb-card>`, `<md-gb-list>`, `<md-gb-icon>`) via `<script type="module">` importing from `@material/web/labs/gb/...`.
- **Google-Internal Bundle**: Load internal bundle components (`<md-gb-processing-indicator>`, `<md-gb-suggestion>`, `<md-gb-suggestion-group>`, `<md-gb-energy>`) using a plain `<script src="https://static.corp.google.com/material-web/gbreeze/latest/components/md-gb-all.js"></script>`. Never load `md-gb-all.js` inside an importmap or `type="module"`.
- **Icon Sizing Rules**: ALWAYS size `<md-gb-icon>` using the `--md-icon-size` CSS property (e.g. `<md-gb-icon style="--md-icon-size: 20px">search</md-gb-icon>`). Never place `.typescale-*` classes on `<md-gb-icon>`.

## Available Component Directory

Below is the complete list of available gBreeze components. Before using any component in a prototype, read its dedicated reference file.

### Actions

- **Button (`<md-gb-button>`)**: Filled, elevated, tonal, outlined, and text action buttons, link buttons, and toggle controls with 5 height scales (`xs` 32px, `sm` 40px, `md` 56px, `lg` 96px, `xl` 136px).
  - **Pull [Button](components/button.md)** when using a button.

- **FAB (`<md-gb-fab>`)**: Prominent floating action button for primary screen triggers in primary, secondary, and tertiary container styles.
  - **Pull [FAB](components/fab.md)** when using a floating action button.

- **Icon Button (`<md-gb-icon-button>`)**: Compact circular or square icon buttons in filled, tonal, outlined, and standard variants.
  - **Pull [IconButton](components/iconbutton.md)** when using an icon button.

- **Split Button (`<md-gb-split-button>`)**: Dual-action button combining a primary button trigger with an adjacent dropdown menu trigger.
  - **Pull [SplitButton](components/splitbutton.md)** when using a split button.

- **Button Group (`<md-gb-button-group>`)**: Container arranging related buttons in standard or connected segmented bar layouts with single, multiple, or no selection management.
  - **Pull [ButtonGroup](components/buttongroup.md)** when using a button group.

- **Chip (`<md-gb-chip>`)**: Compact interactive tags or filter pills for filter selection, input tokens, or dismissible tags.
  - **Pull [Chip](components/chip.md)** when using a chip.

- **Badge (`<md-gb-badge>`)**: Small dot indicators or numeric badge overlays for notifications and status counts on icons and navigation items.
  - **Pull [Badge](components/badge.md)** when using a badge.

### Form Controls

- **Checkbox (`<md-gb-checkbox>`)**: Form checkbox for multiple selection, checked, unchecked, indeterminate, and error validation states.
  - **Pull [Checkbox](components/checkbox.md)** when using a checkbox.

- **Radio (`<md-gb-radio>`)**: Radio selection control for mutually exclusive single option selection within a named group.
  - **Pull [Radio](components/radio.md)** when using a radio button.

- **Slider (`<md-gb-slider>`)**: Continuous or discrete value scale sliders supporting single values, range selection spans, tick marks, value tooltips, and inset icons.
  - **Pull [Slider](components/slider.md)** when using a slider.

- **Switch (`<md-gb-switch>`)**: Binary toggle switch for turning settings on or off with optional custom handle icons.
  - **Pull [Switch](components/switch.md)** when using a switch.

### Layout & Containers

- **App Bar (`<md-gb-app-bar>`)**: Top or bottom application header for screen titles, leading navigation icons, search inputs, and trailing actions.
  - **Pull [AppBar](components/appbar.md)** when using an app bar.

- **Card (`<md-gb-card>`)**: Surface container for grouping related content, headlines, images, and action buttons in outlined, filled, or elevated styles.
  - **Pull [Card](components/card.md)** when using a card.

- **Divider (`<md-gb-divider>`)**: Thin horizontal or vertical structural line for separating layout sections or list items.
  - **Pull [Divider](components/divider.md)** when using a divider.

- **List & List Item (`<md-gb-list>`, `<md-gb-list-item>`)**: Vertical list container and items supporting leading icons, avatars, overline text, supporting copy, trailing text, and segmented layouts.
  - **Pull [List](components/list.md)** when using a list or list items.

- **Menu & Menu Item (`<md-gb-menu>`, `<md-gb-menu-group>`, `<md-gb-menu-item>`)**: Popover dropdown menu container and checkable item groups attached to target buttons via native popover targets.
  - **Pull [Menu](components/menu.md)** when using a menu or dropdown items.

- **Toolbar (`<md-gb-toolbar>`)**: Contextual floating or docked action bar container (`@material/web/labs/gb/components/toolbar/md-gb-toolbar.js`).

- **Navigation Bar (`<md-gb-nav-bar>`, `<md-gb-nav-bar-item>`)**: Bottom navigation bar container and item destinations for compact mobile screens (`@material/web/labs/gb/components/navbar/md-gb-nav-bar.js`).

- **Navigation Rail (`<md-gb-nav-rail>`, `<md-gb-nav-rail-item>`)**: Vertical side navigation rail container and item destinations for medium and expanded screens (`@material/web/labs/gb/components/navrail/md-gb-nav-rail.js`).

- **Tabs (`<md-gb-tabs>`, `<md-gb-tab>`)**: Horizontal tab row and individual tab triggers for switching sub-views (`@material/web/labs/gb/components/tabs/md-gb-tabs.js`).

### Feedback & Overlay

- **Snackbar (`<md-gb-snackbar>`)**: Brief auto-dismissing toast notifications with optional text actions (`@material/web/labs/gb/components/snackbar/md-gb-snackbar.js`).

### AI & Status

- **Processing Indicator (`<md-gb-processing-indicator>`)**: Animated AI thinking dots or status label pills with overlapping source icons for showing background model activity.
  - **Pull [ProcessingIndicator](components/processingindicator.md)** when using an AI processing status indicator.

- **Suggestion & Suggestion Group (`<md-gb-suggestion>`, `<md-gb-suggestion-group>`)**: Post-generation AI prompt reply buttons and responsive prompt reply groups supporting single, 50/50 binary, and multiple-choice layouts.
  - **Pull [Suggestion](components/suggestion.md)** when presenting AI prompt suggestions or follow-up choices.

- **Energy (`<md-gb-energy>`)**: Animated Material AI surfaces, auroras, and Gemini glows loaded via `md-gb-all.js` or the `gbreeze-energy` skill.

### Building Blocks

- **Focus Ring (`focus-ring` / `<md-focus-ring>`)**: Keyboard focus outline primitive and utility classes (`.focus-ring-outer`, `.focus-ring-inner`).
  - **Pull [Focus](components/focus.md)** when setting up custom keyboard accessibility focus outlines.

- **Ripple (`ripple` / `<md-ripple>`)**: Material touch and pointer ripple surface feedback primitive and classes (`.ripple`, `.ripple-host`).
  - **Pull [Ripple](components/ripple.md)** when adding ripple state layers to custom containers.

### Standard MWC Fallback Components

When a specific gBreeze element is not yet defined, rely on standard `@material/web` custom elements rather than raw HTML inputs or unstyled divs:

- **Text Fields**: `<md-outlined-text-field>`, `<md-filled-text-field>` (`@material/web/textfield/outlined-text-field.js`, `@material/web/textfield/filled-text-field.js`)
- **Select Dropdowns**: `<md-outlined-select>`, `<md-filled-select>`, `<md-select-option>` (`@material/web/select/outlined-select.js`, `@material/web/select/filled-select.js`, `@material/web/select/select-option.js`)
- **Modal Dialogs**: `<md-dialog>` (`@material/web/dialog/dialog.js`)
- **Progress Bars**: `<md-linear-progress>`, `<md-circular-progress>` (`@material/web/progress/linear-progress.js`, `@material/web/progress/circular-progress.js`)
- **Elevation Layer**: `<md-elevation>` (`@material/web/elevation/elevation.js`)
