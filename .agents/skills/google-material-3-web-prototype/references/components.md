# gBreeze Component Library Reference

The official component library for Material 3 web prototyping is **gBreeze**. Downstream LLM agents generating prototypes MUST use gBreeze elements (`<md-gb-*>`) and standard Material Web Component fallbacks (`<md-*>`) rather than any other component set or raw unstyled HTML controls.

## Key Characteristics of gBreeze

* **Token-Bound Web Components**: Built on Lit and native Web Standards (Custom Elements, Shadow DOM). All visual styles are bound directly to Material 3 design system tokens (`--md-sys-*`).
* **Design System Integration**: Controls natively consume color roles (`--md-sys-color-*`), typescale tokens (`--md-sys-typescale-*`), 8dp spacing units (`--md-sys-space-*`), and corner radii (`--md-sys-shape-*`).
* **Encapsulated Styling**: Interactive states, elevation shadows, layout geometry, and hover state layers are managed inside the component shadow root or `@layer md`.
* **AI & Conversational Controls**: Native components for AI processing states (`<md-gb-processing-indicator>`), conversational suggestions (`<md-gb-suggestion>`), and surface energy glows (`<md-gb-energy>`).

## Setup & Initialization Instructions

To use gBreeze web components in a web prototype, include the following setup code in the HTML `<head>` section:

```html
<!-- 1. Install dependencies via unpkg importmap -->
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

<!-- 2. Configure Tailwind CSS with Material layer hierarchy -->
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

<!-- 3. Link design system token bindings stylesheet -->
<link rel="stylesheet" href="./design-system-bindings.css">

<!-- 4. Import required gBreeze components -->
<script type="module">
  import '@material/web/labs/gb/components/button/md-gb-button.js';
  import '@material/web/labs/gb/components/iconbutton/md-gb-icon-button.js';
  import '@material/web/labs/gb/components/card/md-gb-card.js';
  import '@material/web/labs/gb/components/list/md-gb-list.js';
  import '@material/web/labs/gb/components/list/md-gb-list-item.js';
  import '@material/web/labs/gb/styles/icon/md-gb-icon.js';
</script>

<!-- 5. Load Google-internal components bundle (for md-gb-processing-indicator, md-gb-suggestion, and md-gb-energy) -->
<script src="https://static.corp.google.com/material-web/gbreeze/latest/components/md-gb-all.js"></script>
```

> **STRICT API WARNING FOR DOWNSTREAM LLMs**: You **MUST NOT** guess component APIs, attributes, properties, events, or slot names. Before writing code for any component below, you MUST explicitly read its dedicated reference file. Guessing invalid attributes or slot names causes rendering failures and breaks prototype functionality.

## Available gBreeze Components

### Actions & Triggers

* **Button** (`<md-gb-button>`): Primary action buttons, links, and toggle controls across five visual emphasis levels and five height scales (`xs` 32px to `xl` 136px, with `md` = 56px for mobile CTAs).
  * **Pull [Button](components/button.md)** when using a button.

* **FAB** (`<md-gb-fab>`): Single prominent floating action button for the primary or most common action on a screen.
  * **Pull [FAB](components/fab.md)** when using a floating action button.

* **Icon Button** (`<md-gb-icon-button>`): Compact circular or square action buttons containing an icon with standard, filled, tonal, or outlined emphasis.
  * **Pull [Icon Button](components/iconbutton.md)** when using an icon button.

* **Split Button** (`<md-gb-split-button>`): Dual-function button pairing a primary action button with a secondary trailing trigger that toggles an attached option menu.
  * **Pull [Split Button](components/splitbutton.md)** when using a split button.

* **Button Group** (`<md-gb-button-group>`): Horizontal set of related buttons presented in standard or connected layout styles with single, multiple, or independent selection models.
  * **Pull [Button Group](components/buttongroup.md)** when using a button group.

* **Chip** (`<md-gb-chip>`): Compact interactive pills for selection, filtering, quick action triggers, or removable input tokens.
  * **Pull [Chip](components/chip.md)** when using a chip.

* **Badge** (`<md-gb-badge>`): Compact status indicators or numerical notification counts displayed on top of icons, navigation items, or list rows.
  * **Pull [Badge](components/badge.md)** when using a badge.

### Form Controls & Inputs

* **Checkbox** (`<md-gb-checkbox>`): Form checkbox control for multi-select choices, binary list toggles, or indeterminate parent selections.
  * **Pull [Checkbox](components/checkbox.md)** when using a checkbox.

* **Radio** (`<md-gb-radio>`): Form radio button control for mutually exclusive single selection within a group.
  * **Pull [Radio](components/radio.md)** when using a radio button.

* **Slider** (`<md-gb-slider>`): Numeric range selection control supporting single-handle, range selection, discrete ticks, and centered track variants.
  * **Pull [Slider](components/slider.md)** when using a slider.

* **Switch** (`<md-gb-switch>`): Visual toggle switch for binary on/off setting selection.
  * **Pull [Switch](components/switch.md)** when using a switch toggle.

### Layout, Containers & Navigation

* **App Bar** (`<md-gb-app-bar>`): Top or bottom application bar for screen titles, navigation triggers, search fields, and contextual controls.
  * **Pull [App Bar](components/appbar.md)** when using an app bar.

* **Card** (`<md-gb-card>`): Flexible container surface to visually group and display collections of related information, media, headlines, supporting copy, and actions.
  * **Pull [Card](components/card.md)** when using a card.

* **Divider** (`<md-gb-divider>`): Thin horizontal or vertical rule that visually separates content regions, card sections, or list items.
  * **Pull [Divider](components/divider.md)** when using a divider.

* **List** (`<md-gb-list>`, `<md-gb-list-item>`): Flexible vertical list container and list items supporting text, leading icons, avatars, overlines, supporting copy, trailing metadata, and segmented card layouts.
  * **Pull [List](components/list.md)** when using a list or list item.

* **Menu** (`<md-gb-menu>`, `<md-gb-menu-group>`, `<md-gb-menu-item>`): Popover action menus, checkable radio/checkbox groups, and selection items attached to trigger anchors using standard HTML popover attributes.
  * **Pull [Menu](components/menu.md)** when using a popover menu.

### AI State & Conversational Components

* **AI Processing Indicator** (`<md-gb-processing-indicator>`): AI status indicator displaying animated thinking dots or status label pills with optional source icons and energy glows.
  * **Pull [Processing Indicator](components/processingindicator.md)** when showing AI thinking or processing status.

* **AI Suggestion** (`<md-gb-suggestion>`, `<md-gb-suggestion-group>`): Post-generation AI reply buttons and prompt coordination containers supporting adaptive single, binary, and multiple-choice layouts.
  * **Pull [Suggestion](components/suggestion.md)** when building conversational AI follow-up suggestions or prompt replies.

### Building Blocks & Utilities

* **Focus Ring** (`focus-ring` / `<md-focus-ring>`): Accessible stateful focus outline indicators around custom interactive components and standard DOM elements during keyboard navigation.
  * **Pull [Focus Ring](components/focus.md)** when customizing focus states or accessibility focus rings.

* **Ripple** (`ripple` / `<md-ripple>`): Interactive surface effect that provides tactile visual feedback for touch, click, and pointer press events.
  * **Pull [Ripple](components/ripple.md)** when adding touch or click ripple effects to custom elements.

## Standard Material Web Component Fallbacks

When a component does not yet have a gBreeze (`md-gb-*`) implementation, fall back to the standard `@material/web` (MWC) custom element rather than raw HTML inputs:

* **Text Fields**: `<md-outlined-text-field>` or `<md-filled-text-field>` (`import '@material/web/textfield/outlined-text-field.js';`)
* **Select / Dropdown**: `<md-outlined-select>` or `<md-filled-select>` with `<md-select-option>` (`import '@material/web/select/outlined-select.js';`)
* **Dialogs**: `<md-dialog>` (`import '@material/web/dialog/dialog.js';`)
* **Progress Indicators**: `<md-linear-progress>` or `<md-circular-progress>` (`import '@material/web/progress/linear-progress.js';`)
* **Elevation**: `<md-elevation>` (`import '@material/web/elevation/elevation.js';`)
