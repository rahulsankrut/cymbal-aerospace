<!-- disableFinding(LINE_OVER_80) -->

# GM3 Rubric (v2.9.0)

> **Single-Question Fast-Path Isolation Guard**: `IF` you are answering a single
> pointed visual question (`Yes` / `No` / `N/A`), `STOP`—`DO NOT` evaluate this
> 65-item full rubric; use `SKILL.md` `Step 2A` (`Sub-step 2A.1`) directly.

--------------------------------------------------------------------------------

## General

### Typography

> **Typography Scale Evaluation Rule (Items 2–16):**
>
> *   **Code / Hybrid Mode**: `IF` the specified M3 typescale role is present,
>     `THEN` it `MUST` exhibit exact multi-property conformance (font size,
>     line-height, font-weight, and `Google Sans` / `Google Sans Text` or `SF
>     Pro` on iOS); approximate sizes or unmapped system fonts (`Arial`,
>     `Times`, or `Roboto` where `Google Sans` is required) `MUST` be evaluated
>     as `"No"`.
> *   **Visual-Only Mode**: `IF` the specified M3 typescale role is visible on
>     screen, `THEN` evaluate whether its rendered scale hierarchy, line
>     spacing, weight, and `Google Sans` / `SF Pro` letterforms match the
>     specification (`"Yes"` or `"No"`); `IF` that typescale role is absent from
>     the screen, `THEN` mark it `"N/A"`.

1.  [ID: typography_sentence_case] Does system-provided UI text appear to comply
    with sentence case by only capitalizing the first word of a sentence in all
    headlines, body text, and labels? Exclude any user-generated content like
    reviews, article titles, article snippets, and text embedded in images.
    [Metric type: Adherence] [Weight: 10]

2.  [ID: typography_display_large] If Display Large
    (`sys.typescale.display-large`) is present, does it match font size
    57pt/57px (3.6rem), line height 64pt/64px (4.0rem), Regular (400) weight,
    and Google Sans (or SF Pro on iOS)? [Metric type: Adherence] [Weight: 3]

3.  [ID: typography_display_medium] If Display Medium
    (`sys.typescale.display-medium`) is present, does it match font size
    45pt/45px (2.8rem), line height 52pt/52px (3.3rem), Regular (400) weight,
    and Google Sans (or SF Pro on iOS)? [Metric type: Adherence] [Weight: 3]

4.  [ID: typography_display_small] If Display Small
    (`sys.typescale.display-small`) is present, does it match font size
    36pt/36px (2.3rem), line height 44pt/44px (2.8rem), Regular (400) weight,
    and Google Sans (or SF Pro on iOS)? [Metric type: Adherence] [Weight: 3]

5.  [ID: typography_headline_large] If Headline Large
    (`sys.typescale.headline-large`) is present, does it match font size
    32pt/32px (2.0rem), line height 40pt/40px (2.5rem), Regular (400) weight,
    and Google Sans (or SF Pro on iOS)? [Metric type: Adherence] [Weight: 3]

6.  [ID: typography_headline_medium] If Headline Medium
    (`sys.typescale.headline-medium`) is present, does it match font size
    28pt/28px (1.8rem), line height 36pt/36px (2.3rem), Regular (400) weight,
    and Google Sans (or SF Pro on iOS)? [Metric type: Adherence] [Weight: 3]

7.  [ID: typography_headline_small] If Headline Small
    (`sys.typescale.headline-small`) is present, does it match font size
    24pt/24px (1.5rem), line height 32pt/32px (2.0rem), Regular (400) weight,
    and Google Sans (or SF Pro on iOS)? [Metric type: Adherence] [Weight: 3]

8.  [ID: typography_title_large] If Title Large (`sys.typescale.title-large`) is
    present, does it match font size 22pt/22px (1.4rem), line height 28pt/28px
    (1.8rem), Regular (400) weight, and Google Sans (or SF Pro on iOS)? [Metric
    type: Adherence] [Weight: 3]

9.  [ID: typography_title_medium] If Title Medium (`sys.typescale.title-medium`)
    is present, does it match font size 16pt/16px (1.0rem), line height
    24pt/24px (1.5rem), Medium (500) weight, and Google Sans Text (or SF Pro on
    iOS)? [Metric type: Adherence] [Weight: 3]

10. [ID: typography_title_small] If Title Small (`sys.typescale.title-small`) is
    present, does it match font size 14pt/14px (0.9rem), line height 20pt/20px
    (1.3rem), Medium (500) weight, and Google Sans Text (or SF Pro on iOS)?
    [Metric type: Adherence] [Weight: 3]

11. [ID: typography_body_large] If Body Large (`sys.typescale.body-large`) is
    present, does it match font size 16pt/16px (1.0rem), line height 24pt/24px
    (1.5rem), Regular (400) weight, and Google Sans Text (or SF Pro on iOS)?
    [Metric type: Adherence] [Weight: 3]

12. [ID: typography_body_medium] If Body Medium (`sys.typescale.body-medium`) is
    present, does it match font size 14pt/14px (0.9rem), line height 20pt/20px
    (1.3rem), Regular (400) weight, and Google Sans Text (or SF Pro on iOS)?
    [Metric type: Adherence] [Weight: 3]

13. [ID: typography_body_small] If Body Small (`sys.typescale.body-small`) is
    present, does it match font size 12pt/12px (0.8rem), line height 16pt/16px
    (1.0rem), Regular (400) weight, and Google Sans Text (or SF Pro on iOS)?
    [Metric type: Adherence] [Weight: 3]

14. [ID: typography_label_large] If Label Large (`sys.typescale.label-large`) is
    present, does it match font size 14pt/14px (0.9rem), line height 20pt/20px
    (1.3rem), Medium (500) weight, and Google Sans Text (or SF Pro on iOS)?
    [Metric type: Adherence] [Weight: 3]

15. [ID: typography_label_medium] If Label Medium (`sys.typescale.label-medium`)
    is present, does it match font size 12pt/12px (0.8rem), line height
    16pt/16px (1.0rem), Medium (500) weight, and Google Sans Text (or SF Pro on
    iOS)? [Metric type: Adherence] [Weight: 3]

16. [ID: typography_label_small] If Label Small (`sys.typescale.label-small`) is
    present, does it match font size 11pt/11px (0.7rem), line height 16pt/16px
    (1.0rem), Medium (500) weight, and Google Sans Text (or SF Pro on iOS)?
    [Metric type: Adherence] [Weight: 3]

### Color

1.  [ID: color_drop_shadows] If elevation drop shadows are present, are they
    strictly mapped to standard GM3 elevation tokens (md.sys.elevation.level1
    through level5) on designated elevated components (e.g., Elevated Card,
    Modal Bottom Sheet, Dialog, FAB, floating carousel scroll-arrow buttons)
    rather than custom/arbitrary CSS box-shadow styles on inline elements?
    (Note: On a strictly flat light-mode utility/document editor canvas with
    zero visible drop shadows separating elements, evaluate drop shadow
    presence/separation as `"No"`, NOT `"Yes"`; on light-mode catalog or detail
    screens with subtle elevation drop shadows separating floating media
    carousel scroll arrows, floating action pills, or elevated cards from the
    canvas, evaluate as `"Yes"`; on dark-theme screens where shadows are not
    visually detectable, evaluate as `"N/A"`.) [Metric type: Hygiene] [Weight:
    10]

2.  [ID: color_error_alerts] Is color used to differentiate error or alert
    elements (such as error messages, input validation, system warnings, or
    notification badges) from standard body text? This applies specifically to
    system errors and critical alerts; do not include general status indicators
    such as stock fluctuations (up/down), flight delays, or price changes.
    [Metric type: Hygiene] [Weight: 3]

3.  [ID: color_surface_roles] Does the layout use standard surface color tokens
    to establish tonal hierarchy between body and navigation areas: body content
    container mapped to sys.color.surface (or surface-container-lowest in light
    mode), while navigation bars or rails are mapped to
    sys.color.surface-container / surface-container-high? [Metric type:
    Adherence] [Weight: 10]

4.  [ID: color_gm_primary] In static GM3 baseline color mode, is the
    sys.color.primary role (and sys.color.primary-container) strictly reserved
    solely for key focal elements: FABs, at most one filled button, primary
    action text labels, and active selection state indicators? (Evaluate as
    `"No"` if any other element—such as inline hyperlink/developer text or
    tinted rating stars like `"4.2 ★"`—uses the primary accent hue; evaluate as
    `"N/A"` on dynamic M3 tonal palettes or custom non-baseline themes.) [Metric
    type: Hygiene] [Weight: 10]

5.  [ID: color_disabled_elements] Are disabled or non-interactive elements
    visually muted or "grayed out" compared to active interactive elements?
    [Metric type: Hygiene] [Weight: 5]

6.  [ID: color_active_element] Is the currently selected or active item (like a
    tab or menu item) marked with a distinct container fill or high-contrast
    color? [Metric type: Hygiene] [Weight: 5]

7.  [ID: color_text_contrast] Are text labels and icons easily legible and
    high-contrast against their colored container backgrounds? [Metric type:
    Hygiene] [Weight: 5]

> **Semantic Color Role Evaluation Rule (Items 8–36):**
>
> *   **Code / Hybrid Mode**: `IF` the specified color role is present, `THEN`
>     it `MUST` bind to its canonical M3 token (`--md-sys-color-*`,
>     `colorScheme.*`, `*Color.*`, `?attr/color*`) or resolve to the specified
>     GM3 baseline hex / dynamic HCT tonal step without raw hardcoded color
>     overrides; unmapped custom hex literals or arbitrary gradients `MUST` be
>     evaluated as `"No"`.
> *   **Visual-Only Mode**: `IF` the UI element corresponding to that color role
>     is visible on screen, `THEN` evaluate whether its rendered fill, text, or
>     stroke matches the specified GM3 baseline hex or dynamic HCT tonal
>     hierarchy (`"Yes"` or `"No"`); `IF` that color role or element is absent
>     from the screen, `THEN` mark it `"N/A"`.

8.  [ID: color_primary] If Primary (`sys.color.primary` /
    `--md-sys-color-primary` / `colorScheme.primary` / `?attr/colorPrimary`) is
    present, does it match baseline hex `#0B57D0` (Light) / `#A8C7FA` (Dark) or
    dynamic Primary Tone 40 (Light) / Tone 80 (Dark)? [Metric type: Adherence]
    [Weight: 3]

9.  [ID: color_on_primary] If text or icons are placed over Primary containers
    (`sys.color.on-primary` / `--md-sys-color-on-primary` /
    `colorScheme.onPrimary` / `?attr/colorOnPrimary`), do they match baseline
    hex `#FFFFFF` (Light) / `#062E6F` (Dark) or dynamic Primary Tone 100 (Light)
    / Tone 20 (Dark)? [Metric type: Adherence] [Weight: 3]

10. [ID: color_primary_container] If Primary Container
    (`sys.color.primary-container` / `--md-sys-color-primary-container` /
    `colorScheme.primaryContainer` / `?attr/colorPrimaryContainer`) is present,
    does it match baseline hex `#D3E3FD` (Light) / `#0842A0` (Dark) or dynamic
    Primary Tone 90 (Light) / Tone 30 (Dark)? [Metric type: Adherence] [Weight:
    3]

11. [ID: color_on_primary_container] If text or icons are placed over Primary
    Container (`sys.color.on-primary-container` /
    `--md-sys-color-on-primary-container` / `colorScheme.onPrimaryContainer` /
    `?attr/colorOnPrimaryContainer`), do they match baseline hex `#041E49`
    (Light) / `#D3E3FD` (Dark) or dynamic Primary Tone 10 (Light) / Tone 90
    (Dark)? [Metric type: Adherence] [Weight: 3]

12. [ID: color_secondary] If Secondary (`sys.color.secondary` /
    `--md-sys-color-secondary` / `colorScheme.secondary` /
    `?attr/colorSecondary`) is present, does it match baseline hex `#00639B`
    (Light) / `#7FCFFF` (Dark) or dynamic Secondary Tone 40 (Light) / Tone 80
    (Dark)? [Metric type: Adherence] [Weight: 3]

13. [ID: color_on_secondary] If text or icons are placed over Secondary
    containers (`sys.color.on-secondary` / `--md-sys-color-on-secondary` /
    `colorScheme.onSecondary` / `?attr/colorOnSecondary`), do they match
    baseline hex `#FFFFFF` (Light) / `#003453` (Dark) or dynamic Secondary Tone
    100 (Light) / Tone 20 (Dark)? [Metric type: Adherence] [Weight: 3]

14. [ID: color_secondary_container] If Secondary Container
    (`sys.color.secondary-container` / `--md-sys-color-secondary-container` /
    `colorScheme.secondaryContainer` / `?attr/colorSecondaryContainer`, e.g.,
    selection chips, active nav pills) is present, does it match baseline hex
    `#C2E7FF` (Light) / `#004D74` (Dark) or dynamic Secondary Tone 90 (Light) /
    Tone 30 (Dark)? [Metric type: Adherence] [Weight: 3]

15. [ID: color_on_secondary_container] If text or icons are placed over
    Secondary Container (`sys.color.on-secondary-container` /
    `--md-sys-color-on-secondary-container` / `colorScheme.onSecondaryContainer`
    / `?attr/colorOnSecondaryContainer`), do they match baseline hex `#001D35`
    (Light) / `#C2E7FF` (Dark) or dynamic Secondary Tone 10 (Light) / Tone 90
    (Dark)? [Metric type: Adherence] [Weight: 3]

16. [ID: color_tertiary] If Tertiary accents (`sys.color.tertiary` /
    `--md-sys-color-tertiary` / `colorScheme.tertiary` / `?attr/colorTertiary`)
    are present, do they match baseline hex `#6F4EA1` (Light) / `#D0BCFF` (Dark)
    or dynamic Tertiary Tone 40 (Light) / Tone 80 (Dark)? [Metric type:
    Adherence] [Weight: 3]

17. [ID: color_on_tertiary] If text or icons are placed over Tertiary containers
    (`sys.color.on-tertiary` / `--md-sys-color-on-tertiary` /
    `colorScheme.onTertiary` / `?attr/colorOnTertiary`), do they match baseline
    hex `#FFFFFF` (Light) / `#381E72` (Dark) or dynamic Tertiary Tone 100
    (Light) / Tone 20 (Dark)? [Metric type: Adherence] [Weight: 3]

18. [ID: color_tertiary_container] If Tertiary Container
    (`sys.color.tertiary-container` / `--md-sys-color-tertiary-container` /
    `colorScheme.tertiaryContainer` / `?attr/colorTertiaryContainer`) is
    present, does it match baseline hex `#EBDDF7` (Light) / `#53378A` (Dark) or
    dynamic Tertiary Tone 90 (Light) / Tone 30 (Dark)? [Metric type: Adherence]
    [Weight: 3]

19. [ID: color_on_tertiary_container] If text or icons are placed over Tertiary
    Container (`sys.color.on-tertiary-container` /
    `--md-sys-color-on-tertiary-container` / `colorScheme.onTertiaryContainer` /
    `?attr/colorOnTertiaryContainer`), do they match baseline hex `#270D5C`
    (Light) / `#EBDDF7` (Dark) or dynamic Tertiary Tone 10 (Light) / Tone 90
    (Dark)? [Metric type: Adherence] [Weight: 3]

20. [ID: color_error] If Error state (`sys.color.error` / `--md-sys-color-error`
    / `colorScheme.error` / `?attr/colorError`) is present, does it match
    baseline hex `#B3261E` (Light) / `#F2B8B5` (Dark) or dynamic Error Tone 40
    (Light) / Tone 80 (Dark)? [Metric type: Adherence] [Weight: 3]

21. [ID: color_on_error] If text or icons are placed over Error containers
    (`sys.color.on-error` / `--md-sys-color-on-error` / `colorScheme.onError` /
    `?attr/colorOnError`), do they match baseline hex `#FFFFFF` (Light) /
    `#601410` (Dark) or dynamic Error Tone 100 (Light) / Tone 20 (Dark)? [Metric
    type: Adherence] [Weight: 3]

22. [ID: color_error_container] If Error Container (`sys.color.error-container`
    / `--md-sys-color-error-container` / `colorScheme.errorContainer` /
    `?attr/colorErrorContainer`, e.g., error banners, validation cards) is
    present, does it match baseline hex `#F9DEDC` (Light) / `#8C1D18` (Dark) or
    dynamic Error Tone 90 (Light) / Tone 30 (Dark)? [Metric type: Adherence]
    [Weight: 3]

23. [ID: color_on_error_container] If text or icons are placed over Error
    Container (`sys.color.on-error-container` /
    `--md-sys-color-on-error-container` / `colorScheme.onErrorContainer` /
    `?attr/colorOnErrorContainer`), do they match baseline hex `#410E0B` (Light)
    / `#F9DEDC` (Dark) or dynamic Error Tone 10 (Light) / Tone 90 (Dark)?
    [Metric type: Adherence] [Weight: 3]

24. [ID: color_surface] If base Surface (`sys.color.surface` /
    `--md-sys-color-surface` / `colorScheme.surface` / `?attr/colorSurface`) is
    present, does it match baseline hex `#FFFFFF` (Light) / `#131314` (Dark) or
    dynamic Neutral Tone 98–100 (Light) / Tone 6 (Dark)? [Metric type:
    Adherence] [Weight: 3]

25. [ID: color_surface_container_lowest] If lowest surface layer
    (`sys.color.surface-container-lowest` /
    `--md-sys-color-surface-container-lowest` /
    `colorScheme.surfaceContainerLowest`) is present, does it match baseline hex
    `#FFFFFF` (Light) / `#0E0E0E` (Dark) or dynamic Neutral Tone 100 (Light) /
    Tone 4 (Dark)? [Metric type: Adherence] [Weight: 3]

26. [ID: color_surface_container_low] If low surface card
    (`sys.color.surface-container-low` / `--md-sys-color-surface-container-low`
    / `colorScheme.surfaceContainerLow`) is present, does it match baseline hex
    `#F8FAFD` (Light) / `#1A1C1E` (Dark) or dynamic Neutral Tone 96 (Light) /
    Tone 10 (Dark)? [Metric type: Adherence] [Weight: 3]

27. [ID: color_surface_container] If standard surface container
    (`sys.color.surface-container` / `--md-sys-color-surface-container` /
    `colorScheme.surfaceContainer`) is present, does it match baseline hex
    `#F3F5F6` (Light) / `#212328` (Dark) or dynamic Neutral Tone 94 (Light) /
    Tone 12 (Dark)? [Metric type: Adherence] [Weight: 3]

28. [ID: color_surface_container_high] If elevated surface container
    (`sys.color.surface-container-high` /
    `--md-sys-color-surface-container-high` /
    `colorScheme.surfaceContainerHigh`, e.g., bottom sheets, app bars) is
    present, does it match baseline hex `#DEE1E3` (Light) / `#2B2D31` (Dark) or
    dynamic Neutral Tone 92 (Light) / Tone 17 (Dark)? [Metric type: Adherence]
    [Weight: 3]

29. [ID: color_surface_container_highest] If highest surface container
    (`sys.color.surface-container-highest` /
    `--md-sys-color-surface-container-highest` /
    `colorScheme.surfaceContainerHighest`, e.g., modals, search bars) is
    present, does it match baseline hex `#E1E3E1` (Light) / `#33353A` (Dark) or
    dynamic Neutral Tone 90 (Light) / Tone 22 (Dark)? [Metric type: Adherence]
    [Weight: 3]

30. [ID: color_on_surface] If body typography or primary icons are rendered on
    surface containers (`sys.color.on-surface` / `--md-sys-color-on-surface` /
    `colorScheme.onSurface` / `?attr/colorOnSurface`), do they match baseline
    hex `#1F1F1F` (Light) / `#E1E2E8` (Dark) or dynamic Neutral Tone 10 (Light)
    / Tone 90 (Dark)? [Metric type: Adherence] [Weight: 3]

31. [ID: color_on_surface_variant] If secondary text, captions, or muted icons
    are rendered (`sys.color.on-surface-variant` /
    `--md-sys-color-on-surface-variant` / `colorScheme.onSurfaceVariant` /
    `?attr/colorOnSurfaceVariant`), do they match baseline hex `#44474E` (Light)
    / `#C4C7D0` (Dark) or dynamic Neutral-Variant Tone 30 (Light) / Tone 80
    (Dark)? [Metric type: Adherence] [Weight: 3]

32. [ID: color_outline] If component borders or text field outlines are present
    (`sys.color.outline` / `--md-sys-color-outline` / `colorScheme.outline` /
    `?attr/colorOutline`), do they match baseline hex `#74777F` (Light) /
    `#8E919A` (Dark) or dynamic Neutral-Variant Tone 50 (Light) / Tone 60
    (Dark)? [Metric type: Adherence] [Weight: 3]

33. [ID: color_outline_variant] If subtle dividers or inactive card outlines are
    present (`sys.color.outline-variant` / `--md-sys-color-outline-variant` /
    `colorScheme.outlineVariant` / `?attr/colorOutlineVariant`), do they match
    baseline hex `#C4C7D0` (Light) / `#44474E` (Dark) or dynamic Neutral-Variant
    Tone 80 (Light) / Tone 30 (Dark)? [Metric type: Adherence] [Weight: 3]

34. [ID: color_inverse_surface] If transient overlay containers
    (`sys.color.inverse-surface` / `--md-sys-color-inverse-surface` /
    `colorScheme.inverseSurface`, e.g., Snackbars, tooltips) are present, do
    they match baseline hex `#303030` (Light) / `#E3E2E6` (Dark) or dynamic
    Neutral Tone 20 (Light) / Tone 90 (Dark)? [Metric type: Adherence] [Weight:
    3]

35. [ID: color_inverse_on_surface] If text or icons are placed inside inverse
    surface containers (`sys.color.inverse-on-surface` /
    `--md-sys-color-inverse-on-surface` / `colorScheme.inverseOnSurface`), do
    they match baseline hex `#F2F0F4` (Light) / `#2F3033` (Dark) or dynamic
    Neutral Tone 95 (Light) / Tone 20 (Dark)? [Metric type: Adherence] [Weight:
    3]

36. [ID: color_inverse_primary] If interactive action labels are rendered inside
    inverse surfaces (`sys.color.inverse-primary` /
    `--md-sys-color-inverse-primary` / `colorScheme.inversePrimary`), do they
    match baseline hex `#A8C7FA` (Light) / `#0B57D0` (Dark) or dynamic Primary
    Tone 80 (Light) / Tone 40 (Dark)? [Metric type: Adherence] [Weight: 3]

### Layout

1.  [ID: layout_portrait_pane] For a portrait orientation screen (phone, tablet,
    or foldable), is there ONLY 1 layout pane? [Metric type: Hygiene] [Weight:
    5]

2.  [ID: layout_landscape_max_panes] For a landscape orientation screen (phone,
    tablet, foldable), are there a maximum of 2 layout panes? [Metric type:
    Hygiene] [Weight: 5]

3.  [ID: layout_desktop_max_panes] For a desktop or ultra-wide screen, are there
    a maximum of 3 layout panes? [Metric type: Hygiene] [Weight: 5]

4.  [ID: layout_visual_alignment] Are related UI elements aligned cleanly along
    shared vertical or horizontal axes? [Metric type: Hygiene] [Weight: 1]

5.  [ID: layout_whitespace_division] Is negative space (whitespace) used to
    divide distinct content blocks rather than relying heavily on line dividers?
    [Metric type: Hygiene] [Weight: 5]

6.  [ID: layout_interactive_separation] Are interactive elements spaced
    appropriately so they don't overlap or collide visually? [Metric type:
    Hygiene] [Weight: 5]

7.  [ID: layout_hardware_clipping] Does the content avoid clipping or
    overlapping device hardware features (like camera notches or home
    indicators)? [Metric type: Hygiene] [Weight: 5]

### Elevation

1.  [ID: elevation_modal_separation] Do floating or temporary modal elements
    (like dialogs, FABs, or toolbars) appear distinctly separated from the
    background content via shadows or scrims? [Metric type: Hygiene] [Weight: 5]

2.  [ID: elevation_tonal_variations] Are adjacent content panes, side sheets,
    and modal containers visually distinguished using M3 surface tonal tokens
    (sys.color.surface-container-lowest through
    sys.color.surface-container-highest) rather than 1px hairline border
    dividers? [Metric type: Hygiene] [Weight: 10]

3.  [ID: elevation_avoid_inline_shadows] Do flat inline elements (standard list
    items, text buttons, outlined buttons, uncontained cards) maintain an
    elevation of 0dp (sys.elevation.level0 / zero box-shadow) in their default
    resting state? [Metric type: Hygiene] [Weight: 10]

### Accessibility

1.  [ID: accessibility_color_alone] Does the UI avoid using color alone to
    convey meaning, state changes, or interactivity (e.g., using redundant cues
    like icons, text labels, or distinct shapes)? [Metric type: Hygiene]
    [Weight: 5]

2.  [ID: accessibility_interactive_boundaries] Do interactive elements maintain
    sufficient visual boundaries and separation to suggest they are easily
    actionable? [Metric type: Hygiene] [Weight: 5]

3.  [ID: accessibility_text_legibility_over_imagery] If text is layered over
    complex imagery or photos, does a translucent scrim, shadow, or container
    ensure the text remains clearly legible? [Metric type: Hygiene] [Weight: 5]
