# Material 3 Layout Reference

An overview of layout, adaptive design, responsive breakpoints, structural scaffolding, spatial arrangement, spacing, shape, elevation, motion, density, touch targets, and bidirectionality in the Google Material 3 design system.

## Layout Overview & Architectural Concepts

Material 3 approaches layout through a modular, adaptive scaffold that structures application windows into **Bars**, **Rails**, and **Panes**.

* **Single Window Framing**: UI applications are contained within a single window frame housing 1 to 3 adaptive content panes.
* **Layout Scaffold**:
  * **Bars**: Horizontal perimeter regions framing top and bottom application edges (Top App Bar, Bottom Navigation Bar).
  * **Rails**: Vertical perimeter regions surrounding content panes (Navigation Rail, Vertical Toolbar, Side Controls).
  * **Panes**: Structural container surfaces housing primary content, components, and interactive tools.
* **Grid & Alignment Rulers**: Layout elements align to a standard 8dp spatial grid (`--md-sys-measurement-space100: 8px`). Global alignment rulers establish consistent focal points for titles, lead content, and interactive controls.
* **Native Tokens & Bound Utility Classes**: Layout styling relies strictly on native custom property custom tokens (`--md-sys-measurement-space*`, `--md-sys-shape-corner-*`, `--md-sys-elevation-level*`) and bound gBreeze aliases (`--md-sys-space-*`, `--md-sys-shape-corner-*`).

**Pull [CanonicalLayouts](canonical_layouts.md)** when designing specific application patterns like list-detail views, feed grids, supporting-pane layouts, or layered task surfaces.

## Responsive Window Breakpoints

Material 3 defines five official window breakpoints (formerly window size classes). Web prototypes MUST adapt component selection, pane count, and spatial structure dynamically across these width thresholds.

### Window Breakpoints Reference Table

| Breakpoint | Window Width (dp / px) | Common Form Factors | Recommended Pane Count | Primary Navigation Component | Communication & Action Components |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Compact** | Under `600dp` | Mobile portrait, narrow split-screen | **1 Pane** | Navigation Bar, Modal Navigation Drawer | Full-screen Dialog, Modal Bottom Sheet |
| **Medium** | `600dp` – `839dp` | Tablet portrait, unfolded foldable portrait | **1 Pane** (or 2 low-density) | Navigation Rail (collapsed), Navigation Bar | Basic Dialog, Contextual Popover / Menu |
| **Expanded** | `840dp` – `1199dp` | Tablet landscape, laptop, desktop window | **2 Panes** (recommended) | Navigation Rail (collapsed or expanded) | Basic Dialog, Standard Side Sheet, Popover |
| **Large** | `1200dp` – `1599dp` | Desktop display, wide monitor | **2 Panes** (recommended) | Navigation Rail (expanded), Navigation Drawer | Basic Dialog, Standard Side Sheet, Popover |
| **Extra-large** | `1600dp+` | Ultra-wide desktop, multi-monitor display | **2 to 3 Panes** | Standard Expanded Navigation Rail | Basic Dialog, Standard Side Sheet |

### Adaptive Design Questions across Breakpoints

When adapting layout across breakpoints, apply these five adaptive transformations:

1. **What should be revealed?**: Uncover additional actions, persistent side sheets, or secondary panes that were hidden on narrow viewports.
2. **How should a screen be divided?**: Transition from 1 pane (Compact/Medium) to 2 panes (Expanded/Large) or 3 panes (Extra-large).
3. **What should be resized?**: Expand card widths, adjust list container padding, and enforce `60ch`–`75ch` line length constraints on text prose.
4. **What should be repositioned?**: Shift actions from bottom controls (Compact) to leading side rails or top toolbars (Medium/Expanded).
5. **What should be swapped?**: Exchange functionally equivalent components (e.g. swap Bottom Navigation Bar for Navigation Rail; swap Modal Bottom Sheet for Popover Menu).

## Layout Scaffold Architecture: Bars, Rails & Panes

The Material 3 layout scaffold organizes application structure into distinct spatial zones:

### 1. Bars

Horizontal framing regions placed at top and bottom window perimeters:

* **Top App Bar**: Houses page title, back navigation, search triggers, and top-level action icons. Placed adjacent to system UI safety regions. Height defaults to `56px` (`--md-sys-measurement-space700`).
* **Bottom Navigation Bar**: Provides quick switching between 3–5 top-level destinations on Compact and Medium viewports.
* **Safety Regions**: Margins reserved for system UI status bars, camera cutouts, and gesture navigation handles. Primary content MUST NOT bleed into safety regions.

### 2. Rails

Vertical perimeter regions bordering content panes:

* **Leading Navigation Rail**: Houses top-level app navigation, branding logos, and Floating Action Buttons (FABs). Width defaults to `72px` (`--md-sys-measurement-space900`) collapsed, or `240px`–`280px` expanded.
* **Trailing Rail**: Houses contextual controls, comment feeds, filter sliders, or side sheet triggers.

### 3. Panes

Panes are the fundamental container surfaces holding application content:

* **Pane Types**:
  * **Fixed Pane**: Maintains a fixed width across viewport scaling (default `360px` on Expanded; `412px` on Large / Extra-large).
  * **Flexible Pane**: Grows and shrinks dynamically with viewport width. Every multi-pane layout MUST contain at least one flexible pane.
* **Pane Display Modes**:
  * **Co-Planar**: Panes sit side-by-side on the same z-index plane.
  * **Floating**: Temporary task pane elevated above main content (e.g. floating inspector card or non-modal tool panel).
  * **Docked**: Secondary pane anchored to a window edge (e.g. docked side sheet or bottom sheet).
* **Pane Resizing & Drag Handles**:
  * Panes can be resized or collapsed using vertical **Drag Handles**.
  * **Persistent Resizing**: Remembers user-selected pane width across breakpoint changes.
  * **Temporary Resizing**: Resets pane widths back to default defaults upon closing or reopening.

## Adaptive Component Strategies

Material 3 components adapt across viewports using three core strategies:

* **Show and Hide**: Revealing or collapsing UI elements (e.g. collapsing navigation drawer labels on narrow screens).
* **Levitate**: Elevating temporary floating surfaces with or without a backdrop scrim (`--md-sys-color-scrim` at 32% opacity).
* **Reflow**: Reorganizing horizontally adjacent cards or panes into vertical stacks when horizontal space is constrained.

## Spacing, Measurement & Grid System

Spacing in Material 3 is measured on an **8dp linear scale** where 1 spacing unit (`--md-sys-measurement-space100`) equals **8px**.

### Spacing Token Reference Table

The table below lists native measurement tokens, bound gBreeze aliases, exact values, and usage guidelines.

| Native CSS Measurement Token | Bound gBreeze Alias Token | Value (dp / px) | Usage Guidance & Application |
| :--- | :--- | :--- | :--- |
| `--md-sys-measurement-space0` | `--md-sys-space-0` | `0` | Zero margin or zero padding reset. |
| `--md-sys-measurement-space25` | `--md-sys-space-25` | `2px` | Hairline gaps, inner border offsets. |
| `--md-sys-measurement-space50` | `--md-sys-space-50` | `4px` | Micro gaps between tight text/icons, badge inner padding. |
| `--md-sys-measurement-space75` | `--md-sys-space-75` | `6px` | Compact list item spacing, filter chip vertical padding. |
| `--md-sys-measurement-space100` | `--md-sys-space-100`, `--md-sys-space-unit` | `8px` | **Base spacing unit**. Default gaps, button horizontal icon gaps, search bar inner padding. |
| `--md-sys-measurement-space125` | `--md-sys-space-125` | `10px` | Compact control vertical padding. |
| `--md-sys-measurement-space150` | `--md-sys-space-150` | `12px` | Card internal padding, search field vertical gap. |
| `--md-sys-measurement-space175` | `--md-sys-space-175` | `14px` | Medium card inner padding. |
| `--md-sys-measurement-space200` | `--md-sys-space-200` | `16px` | **Compact window margins**, standard card padding, list item horizontal padding. |
| `--md-sys-measurement-space250` | `--md-sys-space-250` | `20px` | Medium card content padding, dialog inner gap. |
| `--md-sys-measurement-space300` | `--md-sys-space-300`, `--md-icon-size` | `24px` | **Medium/Expanded layout margins**, pane spacers, default icon size (`24px`). |
| `--md-sys-measurement-space400` | `--md-sys-space-400` | `32px` | Major section gaps, hero section padding. |
| `--md-sys-measurement-space450` | `--md-sys-space-450` | `36px` | Top padding offset for navigation rails. |
| `--md-sys-measurement-space500` | `--md-sys-space-500` | `40px` | Large hero card spacing. |
| `--md-sys-measurement-space600` | `--md-sys-space-600` | `48px` | **Minimum interactive touch target size** (`48px`). |
| `--md-sys-measurement-space700` | `--md-sys-space-700` | `56px` | Standard Top App Bar height, small FAB dimension. |
| `--md-sys-measurement-space800` | `--md-sys-space-800` | `64px` | Standard FAB dimension (`64px`), drawer width offset. |
| `--md-sys-measurement-space900` | `--md-sys-space-900` | `72px` | Collapsed navigation rail width, hero avatar sizing. |

### Spacing Rules & Best Practices

* **Padding and Gaps First**: Prefer `padding` (internal space) and `gap` (flex/grid gutter) before applying `margin` (external space).
* **Logical Spacing Properties**: Use logical CSS property syntax (`padding-inline-start`, `padding-inline-end`, `margin-block-start`, `gap`) to ensure automatic bidirectional support in Right-to-Left (RTL) viewports.

## Shape Corner Scale & Optical Roundness

Material 3 defines a 10-step corner scale to standardize corner roundness across containers and interactive controls.

### Shape Token Reference Table

The table below lists native corner custom properties, bound gBreeze aliases, exact values, and target component assignments.

| Native CSS Corner Property | Bound gBreeze Corner Alias | Corner Value | Target Component Assignments & Usage |
| :--- | :--- | :--- | :--- |
| `--md-sys-shape-corner-none` | - | `0` | Full-screen pages, flush banners, divider lines. |
| `--md-sys-shape-corner-extra-small` | `--md-sys-shape-corner-xs` | `4px` | Tooltips, text fields (bottom active indicator), snackbars. |
| `--md-sys-shape-corner-small` | `--md-sys-shape-corner-sm` | `8px` | Filter chips, elevated chips, search bar corners, text field containers. |
| `--md-sys-shape-corner-medium` | `--md-sys-shape-corner-md` | `12px` | Cards (filled/outlined), popover menus, small dialogs. |
| `--md-sys-shape-corner-large` | `--md-sys-shape-corner-lg` | `16px` | Navigation drawers, floating side sheets, large cards. |
| `--md-sys-shape-corner-large-increased` | `--md-sys-shape-corner-lg-increased` | `20px` | Increased large containers, expressive card frames. |
| `--md-sys-shape-corner-extra-large` | `--md-sys-shape-corner-xl` | `28px` | Modal dialogs, side sheets, search view panels, FAB containers. |
| `--md-sys-shape-corner-extra-large-increased` | `--md-sys-shape-corner-xl-increased` | `32px` | Prominent modal containers, hero dialogs. |
| `--md-sys-shape-corner-extra-extra-large` | `--md-sys-shape-corner-xxl` | `48px` | Extra-large modal cards, spatial containers. |
| `--md-sys-shape-corner-full` | - | `max(50cqw, 50cqh)` | Badges, buttons, pill buttons, icon buttons, sliders, switches. |

### Directional & Asymmetrical Corner Tokens

* Top Corners: `--md-sys-shape-corner-extra-small-top` (`4px 4px 0 0`), `--md-sys-shape-corner-large-top` (`16px 16px 0 0`), `--md-sys-shape-corner-extra-large-top` (`28px 28px 0 0`).
* Side Corners: `--md-sys-shape-corner-large-start` (`16px 0 0 16px`), `--md-sys-shape-corner-large-end` (`0 16px 16px 0`).

### Optical Roundness Formula

When nesting a rounded card or button inside a rounded container, adjust inner corner radii to avoid optical misalignment:

$$\text{Inner Radius} = \text{Outer Radius} - \text{Padding}$$

Example: An outer container with `28px` radius (`--md-sys-shape-corner-extra-large`) and `12px` inner padding uses an inner child radius of $28\text{px} - 12\text{px} = 16\text{px}$ (`--md-sys-shape-corner-large`).

## Elevation & Depth System

Elevation in Material 3 is depicted through **Tone-Based Surface Containers** and soft CSS box shadows across 6 z-axis levels (`level0` to `level5`).

### Elevation Tokens Reference Table

The table below lists native elevation custom properties, exact DP height values, and component resting assignments.

| Native CSS Elevation Token | DP Height / Shadow Offset | Component Resting Assignments & Interactions |
| :--- | :--- | :--- |
| `--md-sys-elevation-level0` | `0` | Unscrolled app bars, filled/tonal/outlined buttons, filled/outlined cards, lists, tabs, navigation rail, sliders, icon buttons. |
| `--md-sys-elevation-level1` | `1px` | Elevated buttons, elevated cards, elevated chips, modal bottom sheet, modal navigation drawer, modal side sheet, banners. |
| `--md-sys-elevation-level2` | `3px` | Scrolled Top App Bar, popover menus, navigation bar, rich tooltips, toolbars. |
| `--md-sys-elevation-level3` | `6px` | Modal dialogs, FABs, Extended FABs, search bar, date/time pickers. |
| `--md-sys-elevation-level4` | `8px` | Hovered FABs, hovered elevated cards, hovered buttons (+1 level hover elevation shift). |
| `--md-sys-elevation-level5` | `12px` | Focused, dragged, or actively manipulated interactive components. |

### Surface Separation Rules

* **Tone-Based Containers**: Separate overlapping surfaces using tone-based color roles (`var(--md-sys-color-surface-container-lowest)` through `var(--md-sys-color-surface-container-highest)`) rather than opacity overlays.
* **Deprecated Tint Overlays**: DO NOT use opacity tint overlays for elevation in web prototypes.
* **Backdrop Scrims**: Use `var(--md-sys-color-scrim)` at 32% opacity (`rgba(0, 0, 0, 0.32)`) behind modal dialogs and bottom sheets.

## Motion Physics, Durations & Focus Indicators

### Motion Durations & Easings Reference

* **Durations**:
  * Short: `--md-sys-motion-duration-short1` (`50ms`), `--md-sys-motion-duration-short2` (`100ms`), `--md-sys-motion-duration-short3` (`150ms`), `--md-sys-motion-duration-short4` (`200ms`).
  * Medium: `--md-sys-motion-duration-medium1` (`250ms`), `--md-sys-motion-duration-medium2` (`300ms`), `--md-sys-motion-duration-medium3` (`350ms`), `--md-sys-motion-duration-medium4` (`400ms`).
  * Long: `--md-sys-motion-duration-long1` (`450ms`), `--md-sys-motion-duration-long2` (`500ms`), `--md-sys-motion-duration-long3` (`550ms`), `--md-sys-motion-duration-long4` (`600ms`).
  * Extra-long: `--md-sys-motion-duration-extra-long1` (`700ms`) through `--md-sys-motion-duration-extra-long4` (`1000ms`).
* **Easings**:
  * Standard: `var(--md-sys-motion-easing-standard)` (`cubic-bezier(0.2, 0.0, 0.0, 1.0)`).
  * Emphasized: `var(--md-sys-motion-easing-emphasized)`.
  * Linear: `var(--md-sys-motion-easing-linear)`.

### Focus Indicator Tokens

All interactive elements MUST implement accessible keyboard focus indicators using native state tokens:

* Thickness: `--md-sys-state-focus-indicator-thickness` (`3px`).
* Inner Offset: `--md-sys-state-focus-indicator-inner-offset` (`-3px`).
* Outer Offset: `--md-sys-state-focus-indicator-outer-offset` (`2px`).

```css
.interactive-element:focus-visible {
  outline: var(--md-sys-state-focus-indicator-thickness) solid var(--md-sys-color-primary);
  outline-offset: var(--md-sys-state-focus-indicator-outer-offset);
}
```

## Information Density & Touch Target Constraints

* **Density Scaling Scale**: Density ranges from `0` (default) down to `-1`, `-2`, `-3` by reducing vertical padding/height in `4dp` decrements.
* **Strict Touch Target Rule**:
  * ALL interactive elements (buttons, icon triggers, list rows, form inputs) MUST maintain a minimum interactive touch target of **48px x 48px** (`min-width: 48px; min-height: 48px`).
  * Even when visual icons are smaller (e.g. `24px`), expand touch target bounds using transparent padding or pseudo-elements (`::before` / `::after`).
* **Density Opt-in**: NEVER enable dense layouts by default if target dimensions fall below 48px x 48px.

## Bidirectionality & Right-To-Left (RTL) Support

* **RTL Mirroring**: In RTL language contexts (Arabic, Hebrew, Farsi), navigation drawers, side rails, and back actions mirror to the right edge of the screen.
* **Logical Properties Mandatory**: ALWAYS write layout CSS using logical properties (`margin-inline-start`, `padding-inline-end`, `inset-inline-start`, `border-inline-start`) instead of directional properties (`margin-left`, `padding-right`, `left`).

## Reference Breadcrumbs

**Pull [CanonicalLayouts](canonical_layouts.md)** when designing specific application patterns like list-detail views, feed grids, supporting-pane layouts, or layered task surfaces.
