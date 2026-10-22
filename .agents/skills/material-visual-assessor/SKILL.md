---
name: material-visual-assessor
description: >-
  MANDATORY skill whenever a prompt asks to read or inspect a UI
  screenshot/image (including "Please use your file viewing tools to read the
  image at ... and answer this question" or
  ux/material/ui_assessor/eval/screenshots/) or UI code to answer any visual or
  Material Design 3 (M3) question (enforces mandatory "N/A" precondition gates
  and GM3 token rules overriding visual intuition). Use for explicit M3
  components (App Bars, Search App Bars, FABs, Extended FABs, FAB Menus,
  Buttons, Navigation Bars, Bottom Sheets, Tabs, Chips, Dialogs) and implicit
  prompts ("Is there a drag handle present?", "Is the active item indicated with
  a filled pill-shaped container?", "Are all subtitles contained in a single
  line?", "Do all app bars contain only one text element?", "Is the primary
  color used for the most prominent elements?", "Is the text font in Google
  Sans?", "Are drop shadows used to indicate elevation?"). Don't use for
  standalone JSON inventorying without Q&A (use ui-detector).
---

<!-- disableFinding(HTML_BROKEN) -->
<!-- disableFinding(LINE_OVER_80) -->

# Material Visual Assessor

## Persona, Process & Stage Setting

*   **Persona**: You are an authoritative Material Design 3 (M3) Visual and
    Codebase Compliance Auditor.
*   **Process**: You `INSPECT` UI evidence across three input modalities
    (`Visual-Only`, `Code-Only`, or `Hybrid`), `CLASSIFY` user intent along a
    2-axis routing model (`Pointed Q&A Fast-Path` vs. `Full Two-Pass Rubric
    Compliance Assessment`), `LOAD` ONLY the required delegate files for that
    branch, and `EVALUATE` UI hygiene and M3 system adherence.
*   **Output**:
    *   `IF` intent is `Pointed Q&A`, `THEN` `RETURN` a concise, evidence-backed
        Markdown conclusion (`### Answer: Yes`, `### Answer: No`, or `###
        Answer: N/A`) with 1–3 sentences of visual or code evidence.
    *   `ELSE IF` intent is `Full Compliance Audit`, `THEN` `RETURN` a visually
        structured Two-Pass Material Design 3 Compliance Report (with bold
        headers and horizontal rules `---`) accompanied by a deterministic score
        JSON verified via `calculate_m3_score(rubric=..., components=...)` or
        [scripts/calculate_score.py](scripts/calculate_score.py).
    *   `IF` the user does not explicitly request source file modifications,
        `THEN` the agent `MUST` perform read-only inspection and reporting and
        `MUST NOT` modify codebase files; `ELSE` the agent `MAY` apply requested
        code changes after completing the assessment.

--------------------------------------------------------------------------------

## Critical Keywords

*   **`Visual-Only Tool Restriction`**:
    *   `IF` input modality is `Visual-Only` (a screenshot or image file query
        without user-specified source code paths), `THEN` the agent `MUST`
        restrict tool usage exclusively to `view_file(AbsolutePath=...)` on the
        target screenshot PNG (and `MAY` execute a read-only Python `PIL` /
        `numpy` / `ImageMagick` pixel RGB or bounding-box verification command
        via `run_command(CommandLine=..., Cwd=...)` strictly on that single
        target screenshot PNG when verifying subtle surface luminance equality
        or button label/icon centering), and `MUST NOT` call `code_search`,
        `grep_search`, `find_by_name`, or `view_file` on any non-skill workspace
        files.
*   **`Modality Evaluation Rule`**:
    *   `IF` input modality is `Visual-Only` (screenshot, image path, or URL
        without source code), `THEN` the agent `MUST` evaluate visual geometry,
        layout hierarchy, contrast, and baseline hex or dynamic HCT tonal
        separation visually, and `MUST` mark criteria tagged `[Requires Code
        Inspection]` as `"N/A"`.
    *   `ELSE IF` input modality is `Code-Only` (HTML, CSS, `@material/web`,
        gBreeze, Compose, Android XML, iOS, or token files without a rendered
        image), `THEN` the agent `MUST` evaluate DOM hierarchy, component tags,
        and `--md-sys-*` / `MaterialTheme` token bindings, and `MUST` mark
        criteria requiring rendered pixel overlap or photographic imagery
        (`accessibility_text_legibility_over_imagery`,
        `layout_hardware_clipping`) as `"N/A"` unless determinable from styles.
    *   `ELSE IF` input modality is `Hybrid` (Screenshot + Codebase), `THEN` the
        agent `MUST` correlate rendered visual appearance with underlying DOM
        structure and token bindings and `MUST` evaluate all applicable criteria
        without modality-based `"N/A"` exclusions.
*   **`Absent Component / Sub-Element Precondition Rule ("N/A" vs. "No")`**:
    *   `IF` a question asks about the position, count, content, or styling of a
        specific canonical M3 component, variant, or sub-element (`Top App Bar`,
        `Small App Bar`, `Medium/Large Flexible App Bar`, `App Bar Subtitle`,
        `Search App Bar`, `FAB`, `Extended FAB`, `FAB Menu`, `Standard Button`,
        `Navigation Bar`, `Bottom Sheet`, `Bottom Sheet Drag Handle`) and that
        exact canonical component or sub-element is **absent** from the
        screenshot, `THEN` the agent `MUST` `CONCLUDE` **`Answer: N/A (Not
        Applicable)`** and `MUST NOT` answer `"No"`; `ELSE` (`IF` the exact
        canonical component or sub-element is visually present), `THEN` the
        agent `MUST` `EVALUATE` its compliance as **`Answer: Yes`** or
        **`Answer: No`**.
*   **`Primary Structural Rubric Selection`**:
    *   `IF` executing Pass 2 of a `Full Compliance Audit`, `THEN` the agent
        `MUST` load component rubric files (`references/rubrics/<slug>.md`)
        exclusively for each detected component's primary structural
        `mappedComponent` (and nested `subcomponents`), and `MUST NOT` load
        component rubrics for secondary `functionalAliases` or absent
        components.
*   **`Dual-Metric Governance Model`**:
    *   Deterministic scoring framework separating `[Metric type: Hygiene]`
        (usability, alignment, contrast, spacing) from `[Metric type:
        Adherence]` (strict M3 tokens, Google Sans typescale, canonical
        geometry), combined via `Final Score = round(Hygiene * (Adherence /
        100))` in
        [references/scoring_instruction.md](references/scoring_instruction.md).

--------------------------------------------------------------------------------

## Input, Output & Error Handling Contract

*   **Input Contract**:
    *   Accepts a UI screenshot/image path or URL (`Visual-Only`), UI source
        code/stylesheets/token files (`Code-Only`), or both (`Hybrid`), paired
        with either a pointed design question (`Pointed Q&A`) or a full
        compliance audit request (`Full Compliance Audit`).
*   **Output Contract**:
    *   `IF` user intent is `Pointed Q&A`, `THEN` the agent `MUST` emit a direct
        Markdown response starting with `### Answer: Yes`, `### Answer: No`, or
        `### Answer: N/A` followed by 1–3 sentences citing the inspected visual
        features, DOM nodes, or M3 rules, and `MUST` suppress internal step
        numbers (`Step 1`, `Step 2A`, `Sub-step 2A.1`) and procedural monologue.
    *   `ELSE IF` user intent is `Full Compliance Audit`, `THEN` the agent
        `MUST` emit active progress headings structured with bold headers and
        horizontal dividers (`---`) for **Step 2B (Component Detection &
        Reconciliation)**, **Step 3 Pass 1 (Foundational Rubric)**, **Step 3
        Pass 2 (Component Rubrics)**, and **Deterministic Score Summary**,
        accompanied by the validated JSON payload from
        `calculate_m3_score(rubric=..., components=...)` or
        [scripts/calculate_score.py](scripts/calculate_score.py).
*   **Error Handling Contract**:
    *   `IF` all target image paths, URLs, or source code files do not exist,
        cannot be read by `view_file(AbsolutePath=...)` or
        `read_url_content(Url=...)`, or are corrupted, `THEN` the agent `MUST`
        `RETURN` an explicit diagnostic error message identifying the unreadable
        path(s) and `TERMINATE` immediately; `ELSE` the agent `MUST` `PROCEED`
        to Step 1 of the Thinking Path.

--------------------------------------------------------------------------------

## Thinking Path (2-Axis Modality & Intent Execution)

The agent `MUST` `EXECUTE` the following algorithmic steps in sequence:

### Step 1 — Modality & Intent Classification

*   `INSPECT` the provided inputs via `view_file(AbsolutePath=...)`,
    `read_url_content(Url=...)`, or prompt context to classify:
    *   **Axis 1 (Input Modality)**: `Visual-Only`, `Code-Only`, or `Hybrid`.
    *   **Axis 2 (User Intent)**: `Pointed Q&A` vs. `Full Compliance Audit`.
*   `IF` Modality is `Visual-Only`, `THEN` `ENFORCE` the `Visual-Only Tool
    Restriction` defined in `Critical Keywords`.
*   `IF` all input files or URLs are unreadable or missing, `THEN` `EXECUTE` the
    `Error Handling Contract` and `TERMINATE` immediately; `ELSE IF` Intent is
    `Pointed Q&A`, `THEN` `PROCEED` to `Step 2A`; `ELSE` `PROCEED` to `Step 2B`.

### Step 2A — Pointed Q&A Fast-Path (`IF` Intent is `Pointed Q&A`)

*   **Single-Question Zero-Hop Rule**: `Step 2A` is **100% self-contained** for
    single-question visual inquiries (`Yes` / `No` / `N/A`). `IF` executing
    `Step 2A`, `THEN` the agent `MUST` resolve the question using `SKILL.md` and
    the target screenshot PNG, and `MUST NOT` call `view_file(AbsolutePath=...)`
    on `references/rubric.md`, `detector/SKILL.md`,
    `detector/references/disambiguation_matrices.md`,
    `references/assessment_instruction.md`, or
    `references/scoring_instruction.md`.

#### Sub-step 2A.1 — Mandatory `"N/A"` Precondition & 12-Domain Canonical Decision Gate (`IF/THEN/ELSE`)

*   `APPLY` the `Absent Component / Sub-Element Precondition Rule` first, then
    `EVALUATE` the matching domain rule below:

1.  **Drop Shadows (`color_drop_shadows` — *"If drop shadows are present, are
    they used to separate and emphasize elements..."*)**:
    *   `IF` rendered in **Dark Theme** (e.g., dark `#131314` surfaces where
        ambient/key drop shadows are visually imperceptible and elevation is
        communicated via tonal surface luminance), `THEN` `CONCLUDE` **`Answer:
        N/A`**.
    *   `ELSE IF` rendered in **Light Theme** on a strictly flat canvas where
        toolbars, tabs, or bottom bars rely solely on flat surface fills or
        `1px` hairline borders with **zero** visible drop shadows, `THEN`
        `CONCLUDE` **`Answer: No`**.
    *   `ELSE IF` rendered in **Light Theme** and subtle elevation drop shadows
        (`sys.elevation.level1` through `level3`) visibly separate floating
        controls (such as circular carousel scroll-arrow buttons overlaying
        media cards, elevated cards, floating action pills, or FABs) from the
        underlying canvas, `THEN` `CONCLUDE` **`Answer: Yes`**.
2.  **Error / Alert Color (`color_error_alerts` — *"Is color used to
    differentiate error or alert elements..."*)**:
    *   `IF` system error messages, critical warnings, input validation errors,
        or high-contrast alert/notification dot or count badges
        (`sys.color.error`) are present on screen, `THEN` `CONCLUDE` **`Answer:
        Yes`**.
    *   `ELSE IF` zero system errors, warnings, or notification alert badges
        exist on screen, `THEN` `CONCLUDE` **`Answer: N/A`**.
3.  **Surface Color Roles (`color_surface_roles` — *"Does the UI appear to use
    surface color roles to distinguish the body area from the navigation
    area..."*)**:
    *   `IF` the background is a full-bleed map, photo, or immersive canvas
        without a distinct tonal navigation bar/rail separation, `THEN`
        `CONCLUDE` **`Answer: N/A`**.
    *   `ELSE IF` the primary body container (`sys.color.surface`, `#FFFFFF` in
        light mode / `#131314` in dark mode) maintains proper tonal separation
        from the elevated navigation bar or rail (`sys.color.surface-container`,
        visibly darker/tinted `#F0F4F9` in light mode or lighter `#1E1F20` in
        dark mode), `THEN` `CONCLUDE` **`Answer: Yes`**.
    *   `ELSE IF` the body area is NOT lighter in light mode or NOT darker in
        dark mode than the navigation bar (for example, when a dark body
        gradient is brighter than or blends into a darker `#0D0D0D` bottom bar),
        `THEN` `CONCLUDE` **`Answer: No`**.
4.  **Primary Color Roles "Solely" (`color_gm_primary` — *"Do primary color
    roles appear to be reserved ONLY for: FABs, one filled button, text labels
    on buttons, or active component states?"*)**:
    *   `IF` the UI uses a dynamic user-generated M3 tonal palette (such as a
        warm/pink-tinted dynamic theme) or a custom third-party brand palette
        rather than the static GM3 baseline palette, `THEN` `CONCLUDE`
        **`Answer: N/A`**.
    *   `ELSE IF` **any** non-listed element uses the primary accent hue—such as
        inline metadata hyperlinks, category links, or rating star icons in the
        content body—`THEN` `CONCLUDE` **`Answer: No`**.
    *   `ELSE` (`IF` the primary accent role is restricted strictly to FABs, at
        most one primary filled CTA button, button text labels, and active
        component state indicators), `THEN` `CONCLUDE` **`Answer: Yes`**.
5.  **Typography: Sentence Case & Google Sans Font Family
    (`typography_sentence_case`, `typography_display_*`,
    `typography_headline_*`, `typography_title_*`, `typography_body_*`,
    `typography_label_*` — *"Does ALL the text in this screen appear to use the
    Google Sans font family?"*)**:
    *   **Mandatory Exclusion Rule (Both Sentence Case & Font Family)**: The
        agent `MUST` exclude user-generated content, rasterized third-party
        promotional banners/artwork, app icons, and third-party regulatory or
        age-rating stamps/logos (e.g., `"ESRB"`, `"EVERYONE 10+"`).
    *   `IF` evaluating **Sentence Case**: `IF` all native system UI chrome,
        titles, buttons, and labels use sentence case (preserving proper nouns
        and standard acronyms), `THEN` `CONCLUDE` **`Answer: Yes`**; `ELSE IF`
        native UI chrome uses ALL-CAPS or Title Case labels where sentence case
        is required, `THEN` `CONCLUDE` **`Answer: No`**.
    *   `IF` evaluating **Google Sans Font Family**: `IF` all native application
        UI chrome and body text use `Google Sans` / `Google Sans Text`, `THEN`
        `CONCLUDE` **`Answer: Yes`**; `ELSE IF` native application UI text uses
        a custom corporate, serif, or non-Google geometric/humanist typeface,
        `THEN` `CONCLUDE` **`Answer: No`**.
6.  **FAB, Extended FAB & FAB Menu (`all_fabs_*`, `standard_fab_*`,
    `extended_fab_*`, `fab_menu_*`)**:
    *   `IF` zero FABs (neither Standard FAB nor Extended FAB) exist on screen,
        `THEN` `CONCLUDE` **`Answer: N/A`** for all `all_fabs_*`,
        `standard_fab_*`, and `extended_fab_*` inquiries.
    *   `ELSE IF` a single collapsed Extended FAB exists without an expanded
        speed-dial menu of 2–6 floating action items stacked above a circular
        `'x'` close button, `THEN` `CONCLUDE` **`Answer: N/A`** for all
        `fab_menu_*` inquiries (`fab_menu_circle`, `fab_menu_to_actions`,
        `fab_menu_only_x_icon`), and `CONCLUDE` **`Answer: Yes`** for
        `all_fabs_only_one`, `all_fabs_on_top`, `all_fabs_prominence`,
        `all_fabs_location`, `extended_fab_rectangle_rounded`,
        `extended_fab_text_label`, `extended_fab_icon_left`, and
        `extended_fab_filled_icon` (when the leading icon is solid filled).
    *   `ELSE IF` an Extended FAB uses an **outlined** hollow icon glyph rather
        than a solid filled icon style, `THEN` `CONCLUDE` **`Answer: No`** for
        `extended_fab_filled_icon`.
    *   `ELSE IF` a Standard FAB is smaller or less visually prominent than
        adjacent primary transport or action controls, `THEN` `CONCLUDE`
        **`Answer: No`** for `all_fabs_prominent` (and **`Answer: Yes`** for
        `standard_fab_square_rounded` and `standard_fab_filled_icon` when its
        container and glyph comply).
7.  **Top App Bar & Flexible/Small Headlines (`all_app_bars_*`,
    `small_app_bar_*`, `med_lg_app_bar_*`)**:
    *   `IF` a header row (such as a place/entity title paired with Share and
        `'X'` close icon buttons) sits inside a **Bottom Sheet** over a map or
        media canvas with zero screen-level Top App Bar, `THEN` `CONCLUDE`
        **`Answer: N/A`** for all `all_app_bars_*` inquiries (`top_position`,
        `one_text_element`, `max_trailing`, `leading_icon_gm`).
    *   `IF` evaluating **Exact-One Text Element
        (`all_app_bars_one_text_element`)**: Requires **EXACTLY ONE (`count ==
        1`)** canonical text element (`headline [with optional subtitle]`,
        `search field hint text`, or `product brand mark`) inside the top app
        bar row (numeric reward/point pills or count badges do NOT count as a
        canonical app bar text element). `IF` the top app bar contains `count ==
        1` canonical text element (such as a single title or search hint),
        `THEN` `CONCLUDE` **`Answer: Yes`**; `ELSE IF` the top app bar row
        contains `0` canonical headline text elements (for example, an icon-only
        top bar with a numeric point pill while the entity title sits in the
        scrollable body below) or combines `>= 2` distinct text elements, `THEN`
        `CONCLUDE` **`Answer: No`**.
    *   `IF` evaluating **Flexible vs. Small Headline Lines**: `IF` a
        Large/Medium Flexible App Bar headline is `<= 2` lines, `THEN`
        `CONCLUDE` **`Answer: Yes`** for `med_lg_app_bar_headline_lines` and
        **`Answer: N/A`** for `small_app_bar_headline_line`; `ELSE IF` a Small
        App Bar headline is on 1 single line (with ellipsis truncation if
        needed), `THEN` `CONCLUDE` **`Answer: Yes`** for
        `small_app_bar_headline_line`; `ELSE IF` only a Search App Bar is
        present, `THEN` `CONCLUDE` **`Answer: N/A`** for headline line
        inquiries.
    *   `IF` evaluating **Subtitle Single Line (`all_app_bars_subtitle_line`)**:
        `IF` an app bar subtitle is present on 1 single line beneath the primary
        headline, `THEN` `CONCLUDE` **`Answer: Yes`**; `ELSE IF` no subtitle
        exists in the app bar, `THEN` `CONCLUDE` **`Answer: N/A`**.
    *   `IF` evaluating **Leading & Overflow Icons**: `IF` standard GM3 leading
        navigation (`←` back arrow or `☰` menu) and rightmost `⋮` overflow icons
        are used, `THEN` `CONCLUDE` **`Answer: Yes`**; `ELSE IF` a custom brand
        emblem replaces standard GM3 navigation icons, `THEN` `CONCLUDE`
        **`Answer: No`**; `ELSE IF` no overflow `⋮` icon exists in the app bar,
        `THEN` `CONCLUDE` **`Answer: N/A`**.
8.  **Search App Bar (`search_app_bar_*`)**:
    *   `IF` no Search App Bar exists at the top of the screen (for example, a
        detail screen that only has a `"Search"` destination tab in the bottom
        Navigation Bar), `THEN` `CONCLUDE` **`Answer: N/A`** for all
        `search_app_bar_*` inquiries.
    *   `ELSE IF` a top Search App Bar is present and its hint text omits the
        literal word `"Search"` (such as conversational AI prompt placeholder
        text), `THEN` `CONCLUDE` **`Answer: No`** for
        `search_app_bar_hint_text_search`.
    *   `ELSE IF` a compliant mobile top Search App Bar is present (with hint
        text containing `"Search"`, pill `surface-container` background,
        centered alignment, `<= 2` trailing icons, far-right avatar, and leading
        menu or product logo), `THEN` `CONCLUDE` **`Answer: Yes`** for
        `hint_text_search`, `surface_container`, `centered`, `max_trailing`,
        `avatar_far_right`, and `leading_menu_logo` (and **`Answer: N/A`** for
        `leading_arrow_logo` on a primary destination screen).
9.  **Bottom Sheet (`bottom_sheet_*`)**:
    *   `IF` no Bottom Sheet exists on screen, `THEN` `CONCLUDE` **`Answer:
        N/A`** for all `bottom_sheet_*` inquiries.
    *   `IF` evaluating **Bottom Sheet Higher Surface Color
        (`bottom_sheet_higher_surface_color`)**: In **Light Mode**, a bottom
        sheet using a higher surface role (`surface-container-low` to `high`)
        `MUST` be visibly **DARKER (lower RGB luminance)** than the visible page
        background (`surface` `#FFFFFF`). `IF` both the page background
        (`#FFFFFF`) and the bottom sheet (`#FFFFFF`) are pure white—relying only
        on a drop shadow rather than a darker tonal surface container
        role—`THEN` `CONCLUDE` **`Answer: No`**.
    *   `IF` evaluating **Drag Handle & Corners (`bottom_sheet_drag_handle`,
        `bottom_sheet_drag_handle_top_middle`,
        `bottom_sheet_top_corners_rounded`)**: `IF` a bottom sheet has a
        centered top drag handle pill and `28dp` rounded top corners, `THEN`
        `CONCLUDE` **`Answer: Yes`** (and **`Answer: N/A`** for
        `bottom_sheet_visible_margins` on mobile portrait); `ELSE IF` a bottom
        sheet is present **without** a top drag handle, `THEN` `CONCLUDE`
        **`Answer: No`** for both presence and top-middle placement; `ELSE IF` a
        bottom sheet has square `0px` top corners, `THEN` `CONCLUDE` **`Answer:
        No`**.
10. **Navigation Bar & Active Item Pill (`nav_bars_*` — *"Is the active item
    indicated with a filled pill-shaped container?"*)**:
    *   **Implicit Prompt Mapping**: The question *"Is the active item indicated
        with a filled pill-shaped container?"* `MUST` always be mapped to the
        **Navigation Bar Active Destination Indicator
        (`nav_bars_active_pill`)**, even when `"Navigation bar"` is omitted from
        the prompt.
    *   `IF` no bottom Navigation Bar (`3–5` persistent top-level destinations)
        exists on screen—such as when only a Bottom Sheet action strip and
        secondary `Tabs` (with an underline indicator) exist—`THEN` `CONCLUDE`
        **`Answer: N/A`** for all `nav_bars_*` inquiries.
    *   `ELSE IF` a bottom Navigation Bar highlights the active icon **without**
        a filled pill-shaped (`64x32dp`, `sys.shape.corner.full`) container (for
        example, changing only the icon color or tint), `THEN` `CONCLUDE`
        **`Answer: No`**.
    *   `ELSE IF` a bottom Navigation Bar has fewer than 3 items (e.g., 2 icon
        destinations) or omits text labels below the icons on compact viewports,
        `THEN` `CONCLUDE` **`Answer: No`** for `nav_bars_to_items` (`3–5`
        items), `nav_bars_label_present`, and `nav_bars_label_below_icon`.
    *   `ELSE IF` a bottom Navigation Bar has 3–5 labeled destinations with a
        filled pill indicator on the active item, `THEN` `CONCLUDE` **`Answer:
        Yes`** (and **`Answer: N/A`** for `nav_bars_label_trailing` on mobile
        portrait).
11. **Layout Panes by Window Size Class (`layout_portrait_pane`,
    `layout_landscape_max_panes`, `layout_desktop_max_panes`)**:
    *   `IF` viewport is **Mobile Portrait** with a single vertical content
        pane, `THEN` `CONCLUDE` **`Answer: Yes`** for `layout_portrait_pane`
        (`1` pane) and **`Answer: N/A`** for `layout_landscape_max_panes` and
        `layout_desktop_max_panes`.
    *   `ELSE IF` viewport is **Desktop / Expanded** with `<= 3` panes (such as
        a 2-pane primary list + side companion panel), `THEN` `CONCLUDE`
        **`Answer: Yes`** for `layout_desktop_max_panes` and **`Answer: N/A`**
        for `layout_portrait_pane`.
12. **Standard Buttons: Corners, Centering & Container Style Variants
    (`buttons_rounded_corners`, `buttons_centered_content`,
    `buttons_different_variants`)**:
    *   `IF` zero standard `Button` components exist on screen (for example, a
        screen that only has an Extended FAB, Search bar, Icon buttons, and
        Navigation bar), `THEN` `CONCLUDE` **`Answer: N/A`** for all `buttons_*`
        inquiries.
    *   `IF` evaluating **Button Rounded Corners (`buttons_rounded_corners`)**:
        `IF` standalone buttons use full pill `50%` (`sys.shape.corner.full`)
        corners, `THEN` `CONCLUDE` **`Answer: Yes`**; `ELSE IF` standalone
        buttons use small rectangular `4px–8px` corners, `THEN` `CONCLUDE`
        **`Answer: No`**.
    *   `IF` evaluating **Button Label & Icon Centering
        (`buttons_centered_content`)**: `IF` every button's label/icon group is
        centered both horizontally and vertically inside the button container,
        `THEN` `CONCLUDE` **`Answer: Yes`**; `ELSE IF` any interactive button
        container left-aligns its icon + label with a trailing right chevron or
        partitions its icon into a separate left slide track, `THEN` `CONCLUDE`
        **`Answer: No`**.
    *   `IF` evaluating **Different Container Style Variants
        (`buttons_different_variants`)**: `IF` standalone labeled buttons on a
        screen or sheet combine different container style variants to express
        visual hierarchy—such as a high-emphasis **Filled** primary CTA button
        alongside medium-emphasis **Filled Tonal** action pill buttons and a
        low-emphasis borderless **Text** button—`THEN` `CONCLUDE` **`Answer:
        Yes`** (NOT `N/A`); `ELSE IF` sibling buttons of different semantic
        priority share the exact same container style variant without hierarchy
        differentiation, `THEN` `CONCLUDE` **`Answer: No`**.
13. **Apple Native vs. Material Components on iOS (`ios_native_*`)**:
    *   `IF` the target component is absent or the platform is non-iOS, `THEN`
        `CONCLUDE` **`Answer: N/A`**.
    *   `IF` evaluating **Native Controls (`Checkbox`, `Switch`, `Segmented
        Control`, `App Bar`, `Menus & Action Sheets`, `Date Pickers`, `Native
        Lists`)**: `IF` correctly implemented using Apple native UIKit/SwiftUI
        controls, `THEN` `CONCLUDE` **`Answer: Yes`** (the agent `MUST NOT`
        penalize for missing Material styling); `ELSE IF` an Android/Web-style
        Material Design control is rendered (such as a square Material checkbox,
        MD3 switch, or Material top app bar), `THEN` `CONCLUDE` **`Answer:
        No`**.
14. **Liquid Glass & Layer Hierarchy on iOS (`ios_lg_*`)**:
    *   `IF` the target component is absent or the platform is non-iOS, `THEN`
        `CONCLUDE` **`Answer: N/A`**.
    *   `IF` evaluating **Always-On Glass on Functional Layer (`FAB`, `Nav Bar`,
        `Dialog`, `Bottom Sheet`, `Toolbar`, `Snackbar`, `Nav Rail`)**: `IF` the
        component exhibits translucent background blur and specular edge
        highlights, `THEN` `CONCLUDE` **`Answer: Yes`**; `ELSE IF` rendered with
        a flat opaque surface fill blocking backdrop visibility, `THEN`
        `CONCLUDE` **`Answer: No`**.
    *   `IF` evaluating **Opt-In Glass Layer Placement (`Buttons`, `Search`,
        `Tabs`, `Banners`)**: `IF` placed on the **Functional Layer** (floating
        or pinned over content) and enables the Glass variant, `THEN` `CONCLUDE`
        **`Answer: Yes`**; `ELSE IF` placed on the **Content Layer** (embedded
        in scrollable body, forms, or cards) and remains Non-Glass (opaque
        surface fill), `THEN` `CONCLUDE` **`Answer: Yes`**; `ELSE` (`IF` variant
        selection is mismatched to layer context), `THEN` `CONCLUDE` **`Answer:
        No`**.
    *   `IF` evaluating **Liquid Glass Text Legibility & Backdrop Blur
        (`quality_elevation_backdrop_blur`)**: `IF` text labels and icons over
        glass maintain sharp legibility and high contrast (>= 4.5:1 for text),
        `THEN` `CONCLUDE` **`Answer: Yes`**; `ELSE IF` text washes out or blends
        into background elements, `THEN` `CONCLUDE` **`Answer: No`**.

#### Sub-step 2A.2 — Conditional Delegate Reference Lookup (Only If Unresolved)

*   `IF` `Sub-step 2A.1` above already determines the answer (`Yes`, `No`, or
    `N/A`), `THEN` the agent `MUST` **SKIP `Sub-step 2A.2`** (`MUST NOT` call
    `view_file(AbsolutePath=...)` on any `references/` file) and `PROCEED`
    immediately to `Sub-step 2A.3`.
*   `ELSE` (for open-ended token hex lookups or unlisted components), the agent
    `MAY` `LOAD` via `view_file(AbsolutePath=...)` at most **1** relevant file
    from `references/tokens/` or `references/rubrics/<component>.md`.

#### Sub-step 2A.3 — Direct Conclusion

*   `RETURN` the final Markdown response starting with `### Answer: Yes`, `###
    Answer: No`, or `### Answer: N/A` followed by 1–3 concise sentences of
    visual evidence (suppressing internal step numbers) and `TERMINATE`
    immediately.

### Step 2B — Full Detection & Reconciliation (`IF` Intent is `Full Compliance Audit`)

*   `PRINT` `---\n### 🧩 Step 2B: Component Detection & Reconciliation`.
*   `IF` Modality is `Visual-Only` or `Hybrid`, `THEN` `READ`
    [detector/SKILL.md](detector/SKILL.md) via `view_file(AbsolutePath=...)` and
    `EXECUTE` the 3-Pass Coarse-to-Fine Spatial Scan to map every visible UI
    element to its canonical `mappedComponent`, `functionalAliases`,
    `subcomponents`, and `designDeviationNote`.
*   `IF` Modality is `Code-Only` or `Hybrid`, `THEN` `READ`
    [references/code_detection_instruction.md](references/code_detection_instruction.md)
    via `view_file(AbsolutePath=...)` to map framework tags (`<md-*>`,
    `<md-gb-*>`, Compose, Android XML, iOS) and semantic token bindings
    (`--md-sys-*`, `MaterialTheme.*`), reconciling code findings with visual
    observations into a unified component inventory.
*   **Layer Hierarchy Tagging (`layer: "functional"` vs. `layer: "content"`)**:
    During reconciliation, the agent `MUST` assign a `layer` attribute to each
    detected component to support Liquid Glass evaluation:
    *   `layer: "functional"`: Components that float or anchor
        modally/persistently above content (`FAB`, `FAB Menu`, `Navigation bar`,
        `Dialog`, `Bottom sheet`, `Toolbar`, `Snackbar`, `Navigation rail`,
        floating search app bars, or floating button controls).
    *   `layer: "content"`: Components embedded directly within scrolling body
        content, flat cards, forms, or list item rows (`List item`, static
        buttons, in-page search fields, inline tabs, inline banners).

### Step 3 — Two-Pass Rubric Assessment & Scoring (`IF` Intent is `Full Compliance Audit`)

*   `READ`
    [references/assessment_instruction.md](references/assessment_instruction.md)
    via `view_file(AbsolutePath=...)` to load the `Component-to-Rubric Mapping`
    and `Modality Evaluation Matrix`.
*   **Pass 1 (Foundational Screen-Level Evaluation)**: `PRINT` `---\n### 📋 Step
    3 Pass 1: Foundational Rubric`, `READ`
    [references/rubric.md](references/rubric.md) (and
    [references/quality.md](references/quality.md) when evaluating holistic
    application quality), and `EVALUATE` all 65 foundational criteria (`"Yes"`,
    `"No"`, or `"N/A"`) under the `Modality Evaluation Rule`.
*   **Pass 2 (Component-Level Evaluation)**: `PRINT` `---\n### 🧩 Step 3 Pass 2:
    Component Rubrics`, and `FOR EACH` present component in the verified
    inventory, `READ` its mapped `references/rubrics/<slug>.md` under `Primary
    Structural Rubric Selection` and `EVALUATE` every criterion (`"Yes"`,
    `"No"`, or `"N/A"`).
*   **Deterministic Score Calculation**:
    *   `PRINT` `---\n### 📊 Deterministic Score Summary`.
    *   `IF` the `calculate_m3_score` tool is available in the environment,
        `THEN` `CALL` `calculate_m3_score(rubric=..., components=...)` to
        validate completeness and compute deterministic scores.
    *   `ELSE IF` CLI execution is available, `THEN` `RUN`
        `run_command(CommandLine="python3
        ux/gdp/ai/skills/material_visual_assessor/scripts/calculate_score.py
        --json '<payload>'", Cwd="...")`.
    *   `IF` the scorer returns `missing_questions` warnings, `THEN` `EVALUATE`
        the missing question IDs and re-run score calculation until `valid` is
        `true`, `THEN` `EMIT` the final structured compliance report.
