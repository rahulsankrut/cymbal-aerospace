# Material Design 3 Component Geometry & Bug Audit Quick Reference

This quick reference summarizes exact Material Design 3 (M3) component
geometries, token bindings, accessibility rules, and high-frequency compliance
violations across all canonical M3 component families.

--------------------------------------------------------------------------------

## 1. Action & Selection Components

*   **Common Buttons (`Filled`, `Elevated`, `Tonal`, `Outlined`, `Text`)**:
    *   *Geometry*: Default height `40dp` (Expressive sizes: XS `32dp`, M
        `48dp`, L `56dp`, XL `72dp`). Pill shape `--md-sys-shape-corner-full`
        default (square option: `12px` morphing to `8px` on press). Label uses
        `--md-sys-typescale-label-large` in **sentence case**. Horizontal
        padding `16dp` (`12dp` leading padding + `8dp` icon-to-label gap when
        leading icon is present).
    *   *Tokens*: Filled = `primary` / `on-primary`; Elevated =
        `surface-container-low` + `level1` shadow / `primary`; Tonal =
        `secondary-container` / `on-secondary-container`; Outlined = `1px
        outline` border / `primary`; Text = transparent / `primary`. At most
        **one Filled button** per view group (`color_gm_primary`).
*   **Floating Action Buttons (`FAB` & `Extended FAB`)**:
    *   *Geometry*: Standard `56dp x 56dp` (`28px` corner radius, `24dp` icon);
        Medium `80dp x 80dp` (`32px` radius, `28dp` icon); Large `96dp x 96dp`
        (`32px` radius, `36dp` icon). Extended FAB hugs content with `28px`
        radius, icon + 1-2 word label (`title-medium` or `label-large`).
    *   *Rules*: Uses `primary-container` / `on-primary-container` at `level3`
        resting elevation. Bottom-right placement with `16dp` margin on compact
        screens. **Never render a disabled FAB**—hide it if unavailable.
*   **Icon Buttons & Button Groups**:
    *   *Icon Buttons*: Sizes XS `32dp`, S `40dp` (default), M `56dp`, L `96dp`,
        XL `136dp`. Pill shape (`full`). Toggle icon buttons switch from
        outlined icon (unselected) to filled icon + filled container (selected).
        Enforce `48dp x 48dp` hit target.
    *   *Button Groups*: Standard groups separate peer buttons with animated
        width/shape morphing (`full` unselected, `12px` selected). Connected
        button groups (`40dp` height, `1px outline` border, `2dp` divider)
        append a leading checkmark icon on selected segments.
*   **Chips (`Assist`, `Filter`, `Input`, `Suggestion`)**:
    *   *Geometry*: Height `32dp` (`48dp` touch target), corner radius `8px`
        (`--md-sys-shape-corner-small`), label `label-large` (max 20 chars),
        leading icon `18dp` or avatar `24dp`, trailing close icon `18dp`.
        Unselected: `surface-container-low` or `1px outline-variant` with
        `on-surface-variant`. Selected filter chip: `secondary-container` /
        `on-secondary-container`.
*   **Checkboxes, Radio Buttons, Switches, & Sliders**:
    *   *Checkbox*: `18dp x 18dp` container, `2px` corner radius, `primary` fill
        when checked, `48dp` hit target.
    *   *Radio Button*: `20dp` outer ring diameter (`primary` selected,
        `on-surface-variant` unselected), `48dp` hit target.
    *   *Switch*: Track `52dp x 32dp` pill (`full`). Handle diameter: `16dp`
        unselected (`outline`), `24dp` selected (`on-primary`), `28dp` pressed.
        Track fill: `surface-container-highest` unselected, `primary` selected.
    *   *Slider*: Track heights XS `16dp`, S `24dp`, M `40dp`, L `56dp`, XL
        `96dp`. Active track `primary`, inactive track
        `surface-container-highest`, pill handle (`full`), `4dp` stop indicators
        required when inactive track contrast `< 3:1`.

--------------------------------------------------------------------------------

## 2. Navigation, Containment, & Feedback Components

*   **Top App Bars & Navigation**:
    *   *App Bars*: Small `56dp` (Wiz) / `64dp` (Android) with `title-large`;
        Medium Flexible `112dp` -> `56dp` (`headline-small`); Large Flexible
        `152dp` -> `56dp` (`headline-large`). Resting surface is `surface`
        (`level0`, **no drop shadow**); scrolled state shifts to
        `surface-container` (`level2`).
    *   *Tabs*: Label-only `47dp` tall; Icon + Label `63dp` tall (`48dp` minimum
        touch target). Primary tab indicator is `3dp` tall (`3px 3px 0 0`
        corners) matching label width; Secondary tab indicator is `2dp` full tab
        width. Max 4 fixed tabs on compact mobile screens before requiring
        scrollable tabs.
    *   *Floating Toolbars*: Must use full pill geometry
        (`--md-sys-shape-corner-full`), never square corners.
*   **Cards, Carousels, & Lists**:
    *   *Cards*: Corner radius `12px` (`--md-sys-shape-corner-medium`), `16dp`
        internal side padding, max `8dp` grid gap. Elevated =
        `surface-container-low` + `level1` shadow; Filled = `surface-container`
        (`level0`, no shadow); Outlined = `surface` + `1px outline-variant`
        (`level0`, no shadow).
    *   *Carousels*: Item radius `28px` (`extra-large`), small preview items
        `40dp-56dp` wide. On vertically scrolling screens, horizontal carousels
        **must provide a "Show All" or peer list view** to avoid keyboard traps.
    *   *Lists & Dividers*: Heights `56dp` (1-line, middle-aligned), `72dp`
        (2-line, middle-aligned), `88dp+` (3-line, top-aligned with `12dp` top
        margin). Padding: `16dp` left, `24dp` right. Dividers are `1dp` thick
        `outline-variant` with `16dp` inset.
*   **Dialogs, Sheets, Banners, Snackbars, Tooltips, & Badges**:
    *   *Dialogs*: Basic dialog width `280dp-560dp`, radius `28px`, padding
        `24dp`, headline-to-body gap `16px`, body-to-actions gap `24dp`, backed
        by `32%` `#000000` scrim. Confirming action on far right.
    *   *Bottom & Side Sheets*: Bottom sheet max width `640dp`, top corners
        `28px` (bottom corners `0px`), centered horizontal pill drag handle with
        `48dp` interactive header plus single-pointer dismiss option. Modal side
        sheet width `360dp` (max `400dp`), `16px` radius.
    *   *Banners & Snackbars*: Snackbars use `inverse-surface` /
        `inverse-on-surface` with `inverse-primary` action text; **actionable
        snackbars on web must never auto-dismiss**.
    *   *Tooltips & Badges*: Plain tooltip `24dp` tall (`8dp` padding,
        `body-small`, `inverse-surface`). Small badge = `6dp` dot; Large badge =
        `16dp` tall, `8px` radius, max 4 chars (`999+`), `error` / `on-error`.
    *   *Progress & Loading Indicators*: Linear/Circular track `4dp` thick
        (`primary`), `4dp` end stop dot if contrast `< 3:1`. Expressive Loading
        Indicator morphs across 7 M3 shapes for `< 5s` waits.
*   **Generative AI (Aurora) Components**:
    *   *AI Assist Chips*: `32dp` mobile / `36dp` desktop with leading Spark
        icon; generating state removes border, applies rotating AI gradient, and
        updates label to `"Generating..."`.
    *   *AI Suggestion (Prompt) Chips*: Asymmetric corners—top-right corner is
        `4px` (`extra-small`), remaining three corners are half-height rounded
        (`16px` mobile / `18dp` desktop).
    *   *AI Outlined Buttons & Inputs*: Generating state replaces border with
        animated counter-clockwise AI gradient fill (`primary` text for `>=
        4.5:1` contrast) or `2dp` animated input outline.
