# Layout Reference

This document provides a comprehensive guide to spatial structure, responsive breakpoint rules, surface shape and elevation tokens, layout containers, and responsive navigation patterns in the Workspace Design System (`workspace-design-system`).

## Layout System Overview

Layout in the Workspace Design System combines structured web component containers (`<md-gb-app-bar>`, `<md-gb-nav-rail>`, `<md-gb-nav-bar>`, `<md-gb-card>`, `<md-gb-list>`) with responsive grid layout utilities.

Key layout principles include:

- **Token-Driven Spatial Grid**: All padding, margin, and layout gaps follow an 8px grid system anchored by spatial custom properties and Tailwind utilities.
- **Component App Shell**: Application layouts use dedicated gBreeze custom elements for screen framing: top application bars, side navigation rails, bottom navigation bars, toolbars, and card containers.
- **Adaptive Breakpoints**: Interfaces adapt across five standard Material window size classes without requiring custom media queries.
- **Accessible Alignment**: Line lengths for body copy are constrained to standard character widths (`60ch` to `75ch`) for reading comfort.

## Surface Shape, Elevation, and Divider Tokens

Surfaces use native CSS custom properties for corner roundedness, elevation depth, and structural separation.

### Shape Tokens

Shape custom properties control corner radii across containers and interactive components:

- `--ws-sys-shape-corner-none`: `0`
- `--ws-sys-shape-corner-extra-small`: `4px` (`--ws-sys-shape-corner-extra-small-top`: `4px 4px 0 0`)
- `--ws-sys-shape-corner-small`: `8px`
- `--ws-sys-shape-corner-medium`: `12px` (default for cards, dialogs, and surface containers)
- `--ws-sys-shape-corner-large`: `16px` (`--ws-sys-shape-corner-large-top`: `16px 16px 0 0`, `--ws-sys-shape-corner-large-end`: `0 16px 16px 0`)
- `--ws-sys-shape-corner-extra-large`: `28px` (`--ws-sys-shape-corner-extra-large-top`: `28px 28px 0 0`)
- `--ws-sys-shape-corner-full`: `max(50cqw, 50cqh)` (used for buttons, search bars, chips, and pills)

Bound gBreeze shape variables: `--md-sys-shape-corner-xs`, `--md-sys-shape-corner-sm`, `--md-sys-shape-corner-md`, `--md-sys-shape-corner-lg`, `--md-sys-shape-corner-xl`, `--md-sys-shape-corner-full`.

Tailwind Utility Mapping: HTML containers can use standard Tailwind corner utilities `rounded-xs` (`4px`) through `rounded-4xl` (`28px`). Do NOT apply `rounded-*` directly to gBreeze components.

### Elevation Tokens

Elevation defines surface hierarchy using shadow custom properties:

- `--ws-sys-elevation-level0`: `0` (flat surface)
- `--ws-sys-elevation-level1`: `1px` (cards, low elevated surfaces)
- `--ws-sys-elevation-level2`: `3px` (hover states, small popovers)
- `--ws-sys-elevation-level3`: `6px` (dropdown menus, floating action buttons)
- `--ws-sys-elevation-level4`: `8px` (nav drawers, side sheets)
- `--ws-sys-elevation-level5`: `12px` (modal dialogs, prominent overlays)

Bound gBreeze elevation variables: `--md-sys-elevation-shadow-0` through `--md-sys-elevation-shadow-5`.

Tailwind Utility Mapping: `shadow-xs` (Level 1), `shadow-sm` (Level 2), `shadow-md` (Level 3), `shadow-lg` (Level 4), `shadow-xl` (Level 5).

> **PROHIBITED ELEVATION UTILITIES**: Do NOT use `shadow-2xs` or `shadow-2xl`. Both are unset to `initial` as Material does not define them. Do NOT add `shadow-*` directly to gBreeze custom elements.

### Divider and Border Tokens

Structural boundaries use two explicit color tokens:

- `--ws-sys-color-divider`: `#c4c7c5` (bound to `--md-sys-color-outline-variant` / `.border-outline-variant`). Use for passive section dividers, header rules, and item separators (`<md-gb-divider>`).
- `--ws-sys-color-outline`: `light-dark(#747775, #8e918f)` (bound to `--md-sys-color-outline` / `.border-outline`). Use for interactive boundaries, input field borders, outlined card borders, and chip outlines.

## Spacing System

Spacing is based on an 8px unit scale defined by `--md-sys-space-unit: 8px`.

### Spacing Tokens Table

| Token Name | Value | Tailwind Class Suffix | Application Context |
| --- | --- | --- | --- |
| `--md-sys-space-0` | `0px` | `s0` | Zero margin or padding |
| `--md-sys-space-25` | `2px` | `s25` | Micro gaps between tight icon pairs |
| `--md-sys-space-50` | `4px` | `s50` | Compact inner padding, chip gaps |
| `--md-sys-space-75` | `6px` | `s75` | Dense item padding |
| `--md-sys-space-100` | `8px` | `s100` | Standard component element spacing |
| `--md-sys-space-125` | `10px` | `s125` | Medium control inner padding |
| `--md-sys-space-150` | `12px` | `s150` | Medium card inner padding |
| `--md-sys-space-175` | `14px` | `s175` | Container inset padding |
| `--md-sys-space-200` | `16px` | `s200` | Standard card and section padding |
| `--md-sys-space-250` | `20px` | `s250` | Large component gaps |
| `--md-sys-space-300` | `24px` | `s300` | Major layout container padding |
| `--md-sys-space-400` | `32px` | `s400` | Screen margins and section gutters |
| `--md-sys-space-450` | `36px` | `s450` | Large header margins |
| `--md-sys-space-500` | `40px` | `s500` | Hero section gaps |
| `--md-sys-space-600` | `48px` | `s600` | Prominent section dividers |
| `--md-sys-space-700` | `56px` | `s700` | Bottom bar height alignment |
| `--md-sys-space-800` | `64px` | `s800` | Major layout section padding |
| `--md-sys-space-900` | `72px` | `s900` | Full page header offsets |

### Applying Spacing Utilities

Apply spacing using either Material token classes (`.p-s*`, `.m-s*`, `.gap-s*`) or standard Tailwind 4px multiplier steps (`p-2`, `m-4`, `gap-6`):

```html
<!-- Material space token classes -->
<div class="p-s200 gap-s100 flex flex-col">
  <div class="p-s100 bg-surface-container rounded-sm">Item 1</div>
  <div class="p-s100 bg-surface-container rounded-sm">Item 2</div>
</div>

<!-- Tailwind standard 4px multiplier steps -->
<div class="p-4 gap-2 flex flex-col">
  <div class="p-2 bg-surface-container rounded-sm">Item 1</div>
</div>
```

> **PROHIBITED SPACING PRACTICE**: Do NOT add internal padding utilities (`p-*`) directly to gBreeze component hosts (`<md-gb-card>`, `<md-gb-button>`, `<md-gb-chip>`). Apply padding to inner container divs inside components.

## Responsive Design Approach

Workspace Design System uses five standard Material window size breakpoints to adapt layouts seamlessly from mobile screens to desktop displays.

### Material Window Size Breakpoints

| Window Class | Width Range | Tailwind Breakpoint | Primary Navigation & Layout Strategy |
| --- | --- | --- | --- |
| Compact | `< 600px` | (Default) | Bottom Navigation Bar (`<md-gb-nav-bar>`), Top App Bar (`<md-gb-app-bar size="sm">`), single-column stacked layout, full-width cards. |
| Medium | `600px - 839px` | `sm:` | Vertical Navigation Rail (`<md-gb-nav-rail>`), 2-column flex/grid layouts. |
| Expanded | `840px - 1199px` | `md:` | Vertical Navigation Rail or side drawer, multi-column master-detail layouts. |
| Large | `1200px - 1599px` | `lg:` | Navigation Rail with expanded side sheet, multi-pane dashboard grid matrices. |
| Extra Large | `>= 1600px` | `xl:` | Navigation Rail / Drawer, multi-pane layout constrained to max width (`max-w-7xl mx-auto`). |

### Breakpoint Rules and Prohibitions

- **Supported Breakpoints**: Always use `sm:` (600px), `md:` (840px), `lg:` (1200px), and `xl:` (1600px) for responsive design.
- **Strictly Prohibited `2xl:` Breakpoint**: Do NOT use `2xl:` in Tailwind class declarations. Material Design does not define a 2xl window size, so `2xl:` is reset to `initial` and fails silently.

## Responsive Navigation Patterns

To maintain usability across mobile and desktop devices, switch navigation components responsively:

- **Compact Screens (<600px)**: Use a bottom navigation bar (`<md-gb-nav-bar>`) fixed to the screen bottom, combined with a top application bar (`<md-gb-app-bar size="sm">`).
- **Medium to Large Screens (>=600px)**: Hide the bottom navigation bar (`class="block sm:hidden"`) and show a vertical navigation rail (`<md-gb-nav-rail class="hidden sm:block"`) docked to the left side of the screen.

```html
<div class="flex flex-col h-screen bg-surface">
  <!-- Top App Bar -->
  <md-gb-app-bar size="sm">
    <md-gb-icon-button slot="leading" aria-label="Menu">
      <md-gb-icon>menu</md-gb-icon>
    </md-gb-icon-button>
    <span>Workspace Dashboard</span>
  </md-gb-app-bar>

  <div class="flex flex-1 overflow-hidden">
    <!-- Desktop Side Navigation Rail (Hidden on mobile) -->
    <md-gb-nav-rail class="hidden sm:block">
      <md-gb-nav-rail-item active icon="home" label="Home"></md-gb-nav-rail-item>
      <md-gb-nav-rail-item icon="search" label="Explore"></md-gb-nav-rail-item>
      <md-gb-nav-rail-item icon="settings" label="Settings"></md-gb-nav-rail-item>
    </md-gb-nav-rail>

    <!-- Main Content Area -->
    <main class="flex-1 overflow-y-auto p-s300 space-y-s200">
      <md-gb-card color="filled">
        <div class="p-s300 space-y-s200">
          <h1 class="typescale-headline-sm text-on-surface">Welcome Back</h1>
          <p class="typescale-body-md text-on-surface max-w-[65ch]">
            Main dashboard surface content automatically adjusts padding and navigation structures across breakpoints.
          </p>
        </div>
      </md-gb-card>
    </main>
  </div>

  <!-- Mobile Bottom Navigation Bar (Hidden on desktop) -->
  <md-gb-nav-bar class="block sm:hidden">
    <md-gb-nav-bar-item active icon="home" label="Home"></md-gb-nav-bar-item>
    <md-gb-nav-bar-item icon="search" label="Explore"></md-gb-nav-bar-item>
    <md-gb-nav-bar-item icon="settings" label="Settings"></md-gb-nav-bar-item>
  </md-gb-nav-bar>
</div>
```

## Multi-Column Grid Layouts

Use Tailwind grid utilities with Material breakpoints for structured responsive grids:

```html
<!-- Responsive Card Grid: 1 column on mobile, 2 on medium, 3 on large -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-s200">
  <md-gb-card color="filled">
    <div class="p-s200 space-y-s100">
      <h3 class="typescale-title-md text-on-surface">Card 1</h3>
      <p class="typescale-body-sm text-on-surface-variant">Card content passage.</p>
    </div>
  </md-gb-card>

  <md-gb-card color="filled">
    <div class="p-s200 space-y-s100">
      <h3 class="typescale-title-md text-on-surface">Card 2</h3>
      <p class="typescale-body-sm text-on-surface-variant">Card content passage.</p>
    </div>
  </md-gb-card>

  <md-gb-card color="filled">
    <div class="p-s200 space-y-s100">
      <h3 class="typescale-title-md text-on-surface">Card 3</h3>
      <p class="typescale-body-sm text-on-surface-variant">Card content passage.</p>
    </div>
  </md-gb-card>
</div>
```

## Readability Line Length Limits

To maintain typographic readability, always cap multi-line body paragraphs and long prose containers to a `max-width` between **`60ch` and `75ch`** (`max-w-[65ch]` in Tailwind or `max-width: 65ch;` in CSS). Never specify a `min-width` on body containers.

```html
<article class="max-w-[65ch] space-y-s200">
  <h2 class="typescale-title-lg text-on-surface">Readable Article Layout</h2>
  <p class="typescale-body-lg text-on-surface">
    This paragraph container is constrained to a maximum width of 65 characters per line, preventing text lines from becoming too long on wide monitors.
  </p>
</article>
```

**Pull [LayoutPatterns](layout-patterns.md)** when implementing complex multi-pane application shells, dashboard grid matrices, master-detail split views, or collapsible side sheet layouts.
