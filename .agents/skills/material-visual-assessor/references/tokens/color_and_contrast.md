# Material Design 3 Color Roles, Contrast Rules, & Generative AI Tokens

Authoritative Material Design 3 (M3) semantic color roles, surface hierarchy,
WCAG 2.1 AA / GAR contrast rules, and Generative AI (Aurora) tokens.

--------------------------------------------------------------------------------

## 1. Semantic Color Roles & Baseline Mappings

Bind UI elements to semantic color tokens (`sys.color.<role>` / CSS
`--md-sys-color-<role>`), never hardcoded hexes:

> **Primary Color Roles "Solely" Restriction Gate (`color_gm_primary`)**:
>
> *   `IF` asked whether `primary` and `primary-container` are used **solely**
>     for FABs, at most one filled button (such as `"Install"`), button text
>     labels, and active selection states (such as an active `"Search"` nav
>     pill):
>     *   `IF` **any** other element uses the primary accent hue—including
>         inline hyperlink/developer text or tinted rating stars (such as blue
>         `"4.2 ★"`)—`THEN` `CONCLUDE` **`Answer: No`**.
>     *   `ELSE IF` the UI uses dynamic M3 tonal theming (such as a warm/tinted
>         inbox palette) or a custom non-baseline theme, `THEN` `CONCLUDE`
>         **`Answer: N/A`**.
>     *   `ELSE` (`IF` restricted exclusively to those 4 focal classes), `THEN`
>         `CONCLUDE` **`Answer: Yes`**.

*   **`sys.color.primary`**: Light `#0B57D0` (P-T40) | Dark `#A8C7FA` (P-T80).
    High-emphasis fills, active states, FABs, primary text actions.

*   **`sys.color.on-primary`**: Light `#FFFFFF` (P-T100) | Dark `#062E6F`
    (P-T20). Text/icons on `primary`.

*   **`sys.color.primary-container`**: Light `#D3E3FD` (P-T90) | Dark `#0842A0`
    (P-T30). Standout fill for FABs and key controls.

*   **`sys.color.on-primary-container`**: Light `#041E49` / `#0842A0` (P-T10) |
    Dark `#D3E3FD` (P-T90). Text/icons on `primary-container`.

*   **`sys.color.secondary`**: Light `#00639B` (S-T40) | Dark `#7FCFFF` (S-T80).
    Medium-emphasis accent controls.

*   **`sys.color.on-secondary`**: Light `#FFFFFF` (S-T100) | Dark `#003355` /
    `#003453` (S-T20). Text/icons on `secondary`.

*   **`sys.color.secondary-container`**: Light `#C2E7FF` (S-T90) | Dark
    `#004A77` / `#004D74` (S-T30). Tonal buttons, selected chips, nav pills.

*   **`sys.color.on-secondary-container`**: Light `#001D35` / `#004A77` (S-T10)
    | Dark `#C2E7FF` (S-T90). Text/icons on `secondary-container`.

*   **`sys.color.tertiary`**: Light `#146C2E` / `#6F4EA1` (T-T40) | Dark
    `#6DD58C` / `#D0BCFF` (T-T80). Complementary accents, badges, callouts.

*   **`sys.color.on-tertiary`**: Light `#FFFFFF` (T-T100) | Dark `#0A3818` /
    `#381E72` (T-T20). Text/icons on `tertiary`.

*   **`sys.color.tertiary-container`**: Light `#C4EED0` / `#EBDDF7` (T-T90) |
    Dark `#0F5223` / `#53378A` (T-T30). Vibrant banners, tertiary containers.

*   **`sys.color.on-tertiary-container`**: Light `#0F5223` / `#270D5C` (T-T10) |
    Dark `#C4EED0` / `#EBDDF7` (T-T90). Text/icons on `tertiary-container`.

*   **`sys.color.error`**: Light `#B3261E` (E-T40) | Dark `#F2B8B5` (E-T80).
    System errors, invalid inputs, notification badges.

*   **`sys.color.on-error`**: Light `#FFFFFF` (E-T100) | Dark `#601410` (E-T20).
    Text/icons on `error` fills.

*   **`sys.color.error-container`**: Light `#F9DEDC` (E-T90) | Dark `#8C1D18`
    (E-T30). Error banners, validation alert cards.

*   **`sys.color.on-error-container`**: Light `#410E0B` / `#8C1D18` (E-T10) |
    Dark `#F9DEDC` (E-T90). Text/icons on `error-container`.

--------------------------------------------------------------------------------

## 2. Neutral Surface Hierarchy & Outline Roles

M3 replaces drop shadows with a 5-step tonal surface container hierarchy
(`--md-sys-color-<role>`):

*   **`sys.color.surface`**: Light `#FFFFFF` (N-T98-100) | Dark `#131314`
    (N-T6). Root screen canvas.
*   **`sys.color.surface-container-lowest`**: Light `#FFFFFF` (N-T100) | Dark
    `#0E0E0E` (N-T4). Recessed canvas / lowest card.
*   **`sys.color.surface-container-low`**: Light `#F8FAFD` (N-T96) | Dark
    `#1A1C1E` / `#1B1B1B` (N-T10). Elevated cards/buttons, unselected chips.
*   **`sys.color.surface-container`**: Light `#F0F4F9` / `#F3F5F6` (N-T94) |
    Dark `#1E1F20` / `#212328` (N-T12). Filled cards, nav bars/rails, scrolled
    app bars, menus.
*   **`sys.color.surface-container-high`**: Light `#DEE1E3` / `#E9EEF6` (N-T92)
    | Dark `#282A2C` / `#2B2D31` (N-T17). Bottom/side sheets, dialogs, surface
    FABs. In Light Mode, a bottom sheet (`"Ask Gemini"` sheet) matching
    `#FFFFFF` `surface` (relying only on a drop shadow) violates tonal elevation
    (`No`).
*   **`sys.color.surface-container-highest`**: Light `#DDE3EA` / `#E1E3E1`
    (N-T90) | Dark `#333537` / `#33353A` (N-T22). Search bars, filled inputs,
    unselected tracks.
*   **`sys.color.on-surface`**: Light `#1F1F1F` (N-T10) | Dark `#E1E2E8` /
    `#E3E3E3` (N-T90). Primary body text, headlines, active icons.
*   **`sys.color.on-surface-variant`**: Light `#444746` / `#44474E` (NV-T30) |
    Dark `#C4C7C5` / `#C4C7D0` (NV-T80). Secondary text, captions, unselected
    icons.
*   **`sys.color.outline`**: Light `#747775` / `#74777F` (NV-T50) | Dark
    `#8E918F` / `#8E919A` (NV-T60). Essential interactive borders (text fields,
    buttons).
*   **`sys.color.outline-variant`**: Light `#C4C7C5` / `#C4C7D0` (NV-T80) | Dark
    `#444746` / `#44474E` (NV-T30). Decorative 1dp dividers, outlined cards.
*   **`sys.color.inverse-surface`**: Light `#303030` (N-T20) | Dark `#E3E2E6` /
    `#E3E3E3` (N-T90). Snackbars, plain tooltips.
*   **`sys.color.inverse-on-surface`**: Light `#F2F0F4` / `#F2F2F2` (N-T95) |
    Dark `#2F3033` / `#303030` (N-T20). Text/icons on `inverse-surface`.
*   **`sys.color.inverse-primary`**: Light `#A8C7FA` (P-T80) | Dark `#0B57D0`
    (P-T40). Action text inside `inverse-surface`.
*   **`sys.color.scrim`**: Light/Dark `#000000` (32% alpha). Modal backdrop
    dimming layer.

--------------------------------------------------------------------------------

## 3. WCAG 2.1 AA & GAR Contrast Compliance Rules

*   **Standard Text (`>= 4.5:1`)**: Normal body, label, and caption text under
    `18pt` (`24px`) regular or `14pt` (`18.67px`) bold requires **>= 4.5:1**
    contrast.
*   **Large Text & Essential Boundaries (`>= 3.0:1`)**: Display/headline text
    (`>= 18pt` regular / `>= 14pt` bold), active icons, and essential
    interactive borders (text fields, radio/checkbox rings, slider stop dots)
    require **>= 3.0:1** contrast.
*   **Text Over Imagery**: Text over photos/imagery requires a translucent
    scrim, gradient, or surface container ensuring **4.5:1** legibility.
*   **Dark Theme Shadow Rule**: Drop shadows are imperceptible on dark surfaces
    (`#131314`). Elevation relies on tonal surface steps
    (`surface-container-low` to `highest`); evaluate shadow-only criteria as
    **N/A** in Dark Theme.

--------------------------------------------------------------------------------

## 4. Generative AI (Aurora) Color & Gradient Tokens

AI colors signal active user-initiated Generative AI computation via animated
counter-clockwise rotation (never static decoration on resting controls):

*   **Core Tokens**: `--md-sys-color-ai-main` (`#217BFE`),
    `--md-sys-color-ai-analog` (`#078EFB`), `--md-sys-color-ai-complement`
    (`#AC87EB`).
*   **Soft Variant Fills (Under Text)**: `--md-sys-color-ai-main-variant`
    (`#D7E6FF`), `--md-sys-color-ai-analog-variant` (`#C7E4FF`),
    `--md-sys-color-ai-complement-variant` (`#DCE2FF`) preserve `>= 4.5:1` text
    contrast.
*   **Animated Border Stop Sequence**: `AI main` -> `AI analog` -> `AI
    complement-variant` -> `Surface` -> `AI analog` -> `AI main`.
