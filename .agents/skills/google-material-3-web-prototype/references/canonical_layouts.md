# Material 3 Canonical Layouts Reference

Canonical layouts provide standard structural patterns for implementing the Google Material 3 layout scaffold across breakpoints. They give web prototypes proven layout compositions for common user workflows.

## Overview of Canonical Layouts

Material 3 defines three primary canonical layout patterns:

* **Feed**: Multi-column grid composition for rapid browsing and content discovery (news, social media, photo galleries, e-commerce listings).
* **List-Detail**: Two-pane parent-child pattern displaying explorable lists alongside selected item details (inbox + email, conversation list + chat thread, file browser + document view).
* **Supporting Pane**: Two-pane focus pattern prioritizing a primary work surface while pairing it with supporting contextual panels (document editing + comments, video player + playlist, analytics dashboard + inspector).

## 1. Feed Layout

The Feed layout uses flexible grid columns to display collections of cards or media items across viewports.

### Breakpoint Adaptation for Feed

* **Compact (<600dp)**:
  * Single column vertically stacked list of cards.
  * Cards fill 100% of the pane width (`margin: 16px` leading/trailing).

* **Medium (600–839dp)**:
  * 2-column or 3-column responsive grid.
  * `margin: 24px` leading/trailing, `gap: 16px` between grid items.

* **Expanded & Above (840dp+)**:
  * Multi-column grid (3 to 6 columns depending on card width constraints).
  * `margin: 24px` leading/trailing, `gap: 24px` between grid items.

### HTML/CSS Structural Pattern for Feed

```html
<div class="feed-container" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: var(--md-sys-space-200); padding: var(--md-sys-space-300);">
  <div class="feed-card" style="background-color: var(--md-sys-color-surface-container-low); border-radius: var(--md-sys-shape-corner-md); padding: var(--md-sys-space-200);">
    <!-- Card content -->
  </div>
</div>
```

## 2. List-Detail Layout

The List-Detail layout splits the window between an explorable item list and a detailed view pane.

### Breakpoint Adaptation for List-Detail

* **Compact (<600dp)**:
  * Single-pane display.
  * Navigating to an item replaces the list view with the detail view.
  * A Top App Bar in the detail view provides a back button (`<md-gb-icon>arrow_back</md-gb-icon>`) to return to the list view.

* **Medium (600–839dp)**:
  * Single-pane by default for dense lists.
  * Two-pane equal split (`50% / 50%`) when quick browsing across low-density items is required. Navigation uses a Bottom Navigation Bar or Modal Navigation Rail to preserve horizontal pane width.

* **Expanded, Large, & Extra-Large (840dp+)**:
  * Two-pane co-planar display.
  * Detail pane displays selected item details. If no item is selected, display a placeholder state in the detail pane.
  * Selected list item highlights using `var(--md-sys-color-secondary-container)` background fill.

### HTML/CSS Structural Pattern for List-Detail

```html
<div class="list-detail-scaffold" style="display: flex; width: 100%; height: 100vh;">
  <!-- List Pane (Fixed width or 50% flex) -->
  <aside class="list-pane" style="width: 360px; min-width: 320px; background-color: var(--md-sys-color-surface-container-low); border-inline-end: 1px solid var(--md-sys-color-outline-variant); overflow-y: auto;">
    <!-- Explorable List Items -->
  </aside>

  <!-- Detail Pane (Flexible remainder) -->
  <main class="detail-pane" style="flex: 1; background-color: var(--md-sys-color-surface); overflow-y: auto; padding: var(--md-sys-space-300);">
    <!-- Selected Item Detail Content -->
  </main>
</div>
```

## 3. Supporting Pane Layout

The Supporting Pane layout divides the window between a primary focus pane (occupying ~66% of screen width) and a secondary supporting pane (occupying ~33% or fixed 360dp/412dp width).

### Breakpoint Adaptation for Supporting Pane

* **Compact (<600dp)**:
  * Primary focus pane occupies full screen.
  * Supporting pane is stacked underneath or presented via a Modal Bottom Sheet.

* **Medium (600–839dp)**:
  * Primary focus pane occupies main area.
  * Supporting pane is positioned underneath or toggled as a docked bottom sheet.

* **Expanded & Above (840dp+)**:
  * Co-planar side-by-side arrangement.
  * Supporting pane sits on the trailing (or leading in RTL) side with a fixed width of `360px` (Expanded) or `412px` (Large/Extra-large).

### HTML/CSS Structural Pattern for Supporting Pane

```html
<div class="supporting-pane-scaffold" style="display: flex; width: 100%; height: 100vh;">
  <!-- Primary Focus Pane (Flexible main surface) -->
  <main class="focus-pane" style="flex: 1; background-color: var(--md-sys-color-surface); padding: var(--md-sys-space-300); overflow-y: auto;">
    <!-- Primary Content / Editor -->
  </main>

  <!-- Supporting Pane (Fixed trailing panel) -->
  <aside class="supporting-pane" style="width: 360px; background-color: var(--md-sys-color-surface-container-low); border-inline-start: 1px solid var(--md-sys-color-outline-variant); padding: var(--md-sys-space-300); overflow-y: auto;">
    <!-- Contextual / Auxiliary Controls -->
  </aside>
</div>
```

## Advanced Custom Layered Layouts

For complex task-oriented workflows (e.g. checkout drawers, comment threads, floating inspector tools):

* **Levitate Strategy**: Use floating or docked panes elevated at level 1 or level 2 (`--md-sys-elevation-level1` / `--md-sys-elevation-level2`) above main content surfaces.
* **Modal Scrim Overlay**: When levitated panes require exclusive user focus, place a backdrop scrim using `var(--md-sys-color-scrim)` at 32% opacity (`rgba(0, 0, 0, 0.32)`).
