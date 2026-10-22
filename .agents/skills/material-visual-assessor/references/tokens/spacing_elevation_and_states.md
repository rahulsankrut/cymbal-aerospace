# Material Design 3 Spacing, Adaptive Layout, Elevation, & Interaction States

Authoritative Material Design 3 (M3) 4px/8px measurement scale, touch target
accessibility rules, responsive window size classes, tonal elevation levels
(`0-5`), and interaction state layer opacities.

--------------------------------------------------------------------------------

## 1. Spacing & Measurement Scale

Padding, margins, component heights, and layout gaps follow a strict 4px/8px
grid (`sys.measurement.<step>` / CSS `--md-sys-measurement-<step>`; `2px`
half-steps reserved for micro-alignment):

*   **`sys.measurement.space0`**: `0px` - Flush edges, zero-margin containers.
*   **`sys.measurement.space25`**: `2px` - Connected button group internal
    segment divider gap.
*   **`sys.measurement.space50`**: `4px` - Tight inline icon/badge
    micro-spacing.
*   **`sys.measurement.space75`**: `6px` - Compact component internal offset.
*   **`sys.measurement.space100`**: `8px` - Base grid unit; button icon-to-label
    gap; plain tooltip padding; max card grid gap.
*   **`sys.measurement.space125`**: `10px` - Compact control padding.
*   **`sys.measurement.space150`**: `12px` - Button leading-icon side padding;
    3-line list top alignment margin; rich tooltip top padding.
*   **`sys.measurement.space175`**: `14px` - Intermediate control inset.
*   **`sys.measurement.space200`**: `16px` - Standard button/card/text-field
    horizontal padding; Compact screen edge margin; FAB screen margin.
*   **`sys.measurement.space250`**: `20px` - Medium container padding.
*   **`sys.measurement.space300`**: `24px` - Dialog all-around padding; Expanded
    screen layout margin; list trailing element right padding.
*   **`sys.measurement.space400`**: `32px` - Extra-small button height (`32dp`);
    standard chip height (`32dp`); switch track height (`32dp`).
*   **`sys.measurement.space450`**: `36px` - Desktop AI Assist Chip height
    (`36dp`).
*   **`sys.measurement.space500`**: `40px` - Standard button height (`40dp`);
    small icon button (`40dp`); connected button group height (`40dp`).
*   **`sys.measurement.space600`**: `48px` - **Minimum interactive touch target
    (`48dp x 48dp`)**; medium button height (`48dp`).
*   **`sys.measurement.space700`**: `56px` - Small Top App Bar height (`56dp`
    Wiz); standard FAB (`56dp`); 1-line list height; large button (`56dp`).
*   **`sys.measurement.space800`**: `64px` - Android Top App Bar height
    (`64dp`); Navigation Bar height (`64dp`).
*   **`sys.measurement.space900`**: `72px` - 2-line list item height (`72dp`);
    extra-large button height (`72dp`); time picker input height.
*   **Mandatory Touch Target Rule (`48dp x 48dp`)**: Every interactive control
    (buttons, icon buttons, chips, checkboxes, radio buttons, switches, tabs)
    must maintain at least a `48dp x 48dp` active hit target (`44pt x 44pt` on
    iOS). Visual containers smaller than `48dp` (e.g., `32dp` chips or `18dp`
    checkboxes) must expand their invisible touch bounds to `48dp`.

--------------------------------------------------------------------------------

## 2. Adaptive Window Size Classes & Pane Limits

*   **Portrait Orientation (`layout_portrait_pane`)**: Maximum **1 layout pane**
    on phone, tablet, or foldable portrait viewports.
*   **Landscape Orientation (`layout_landscape_max_panes`)**: Maximum **2 layout
    panes** on phone, tablet, or foldable landscape viewports.
*   **Desktop / Ultra-Wide (`layout_desktop_max_panes`)**: Maximum **3 layout
    panes** with `24dp` (`--md-sys-measurement-space300`) outer layout margins.
*   **Containment & Whitespace (`layout_whitespace_division`,
    `elevation_tonal_variations`)**: Divide distinct content regions using
    negative space and surface container tonal steps (`surface-container-lowest`
    through `highest`) rather than 1px hairline border dividers.

--------------------------------------------------------------------------------

## 3. Elevation System (`level0` to `level5`) & Drop Shadow Presence Gate

Elevation in M3 is expressed through tonal surface container shifts and/or
subtle ambient/key drop shadows on designated floating/elevated components:

> **Drop Shadow Presence vs. M3 Tonal Elevation Gate (`color_drop_shadows`)**:
>
> *   `IF` asked *"If drop shadows are present, are they used to separate and
>     emphasize elements..."* on a **Light Theme** UI:
>     *   `IF` the UI is a strictly flat utility/document editor canvas with
>         **zero visible drop shadows** on toolbars, tabs, or sheets, `THEN`
>         `CONCLUDE` **`Answer: No`**.
>     *   `ELSE IF` subtle elevation drop shadows visibly separate floating
>         carousel scroll-arrow buttons (`elevation level 2`), elevated cards,
>         floating action pills, or FABs from the background, `THEN` `CONCLUDE`
>         **`Answer: Yes`**.
> *   `ELSE IF` rendered in **Dark Theme** (`#131314`) where shadows are
>     imperceptible, `THEN` `CONCLUDE` **`Answer: N/A`**.

*   **`sys.elevation.level0`** (`--md-sys-elevation-level0`, `0px` shadow): Flat
    inline elements—Filled/Outlined/Text buttons, Filled/Outlined cards, lists,
    text fields, resting Top App Bars.
*   **`sys.elevation.level1`** (`--md-sys-elevation-level1`, `1px` shadow):
    Elevated cards, Elevated buttons, standard bottom sheets.
*   **`sys.elevation.level2`** (`--md-sys-elevation-level2`, `3px` shadow):
    Scrolled Top App Bars, floating toolbars, dropdown menus.
*   **`sys.elevation.level3`** (`--md-sys-elevation-level3`, `6px` shadow):
    Standard FABs at rest, modal dialogs, date/time pickers.
*   **`sys.elevation.level4`** (`--md-sys-elevation-level4`, `8px` shadow):
    Hovered standard FABs.
*   **`sys.elevation.level5`** (`--md-sys-elevation-level5`, `12px` shadow):
    Pressed standard FABs.

--------------------------------------------------------------------------------

## 4. Interaction States & State Layer Opacities

Interactive components overlay a semi-transparent **State Layer** matching the
foreground content color role (`on-primary`, `on-surface`, `primary`, etc.) over
the container fill:

*   **Enabled (Resting)**: `0%` state layer overlay | Resting elevation level.
    Baseline component styling.
*   **Hover**: `8%` foreground overlay | Resting + 1 level. Subtle pointer hover
    tint; plain tooltips appear after `1.5s`.
*   **Focus**: `12%` foreground overlay | Resting level. High-visibility
    keyboard focus ring (`2dp` outline) bounds the control.
*   **Pressed (Ripple)**: `12%` foreground overlay | Resting + 1 level (or
    flat). Expanding radial ripple originating from pointer/touch coordinates.
*   **Dragged**: `16%` foreground overlay | Resting + 2 levels. Element lifts
    with shadow above peer containers.
*   **Disabled**: No state layer (Direct gray) | `level0` (`0px`). Container
    fill opacity drops to **12%** (`on-surface` at `12%`); text/icon opacity
    drops to **38%** (`on-surface` at `38%`). Non-interactive.
