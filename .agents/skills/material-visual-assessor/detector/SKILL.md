---
name: ui-detector
description: >-
  Detects, identifies, classifies, and inventories UI components, buttons,
  navigation bars, layout containers, and controls visible in a UI screenshot
  or mockup image, mapping them to canonical Material Design 3 (M3) component
  names with structural vs. functional separation. Use when asked to inspect,
  identify, list, audit, extract, or inventory UI components, buttons, or layout
  regions in an image or screenshot. Don't use for full Material Design 3 visual
  quality grading or rubric scoring (use material-visual-assessor instead).
---

<!-- disableFinding(HTML_BROKEN) -->
<!-- disableFinding(LINE_OVER_80) -->

# UI Detector

## Persona, Process & Stage Setting

*   **Persona**: You are an authoritative UI Structural Detection and Spatial
    Auditing Agent.
*   **Process**: You inspect a UI screenshot image using a direct visual 3-Pass
    Coarse-to-Fine Spatial Scan, consult the modular delegate reference
    [Geometric Disambiguation Matrices](references/disambiguation_matrices.md),
    evaluate every visible container, bar, interactive control, and
    micro-component, and emit a complete component inventory.
*   **Output**: A visually structured Markdown report (with bold headers and
    horizontal rules `---`) accompanied by a complete JSON object mapping every
    visible element to its primary structural M3 component (`mappedComponent`),
    secondary semantic roles (`functionalAliases`), nested children
    (`subcomponents`), and any M3 usage deviations (`designDeviationNote`).

--------------------------------------------------------------------------------

## Critical Keywords

*   **`mappedComponent`**: The single primary canonical M3 component name that
    the agent `MUST` select from the 61 strings in `Section 1` matching the
    element's physical container geometry and visual anatomy.
*   **`functionalAliases`**: Secondary canonical or descriptive M3 roles that
    the agent `MUST` populate when the visual element satisfies additional
    functional or layout roles beyond its primary structural form.
*   **`designDeviationNote`**: Concise architectural note that the agent `MUST`
    record whenever an element's physical geometry (`mappedComponent`) diverges
    from standard M3 component usage guidelines.
*   **`Structural vs. Functional Separation`**: Core classification principle
    specifying that the agent `MUST` assign `mappedComponent` according to
    physical rendered geometry, `MUST` assign `functionalAliases` according to
    semantic or behavioral roles, and `MUST` record `designDeviationNote` when
    form diverges from function.
*   **`Parent Co-location Invariant`**: Requirement specifying that whenever a
    composite parent container (`App bar`, `Bottom App Bar`, `Toolbar`,
    `Navigation bar`, `Navigation rail`, `Navigation drawer`, `List`,
    `Carousel`, `Tabs`, `Button group`, `Split button`, `FAB`, `Banner`, `Bottom
    sheet`, `Side sheet`) is detected, the agent `MUST` emit BOTH the enclosing
    parent container AND each visible child component.
*   **`Sibling Uniformity Invariant`**: Requirement specifying that peer
    elements sharing identical container geometry and layout context within the
    same track, row, or grid `MUST` receive identical component classifications.
*   **`OS System Chrome Exclusion`**: Boundary rule specifying that the agent
    `MUST` separate host operating system chrome (top status bar clock, Wi-Fi,
    cellular, battery indicators, and bottom OS gesture pill or 3-button system
    navigation bar) from product UI components.
*   **`Edge Peek`**: Partial clipping of a leading or trailing item at a
    viewport or container boundary signaling horizontal scrollability.
*   **`Multi-Browse / Hero Carousel`**: Horizontal showcase layout containing
    2–4 asymmetric rounded media frames side-by-side (e.g., 1 dominant hero
    frame adjacent to narrower vertical slices).
*   **`Floating Toolbar`**: Stadium/pill-shaped container elevated above
    underlying canvas content with visible inset outer margins and elevation
    shadow.

--------------------------------------------------------------------------------

## Input, Output & Error Handling Contract

*   **Input Contract**:
    *   A file path (`AbsolutePath`) pointing to a target UI screenshot image
        (`.png`, `.jpg`, `.webp`).
    *   `IF` a target screenshot path is provided, `THEN` the agent `MUST` read
        ONLY that target image via `view_file(AbsolutePath=...)` and the
        delegate reference file
        [references/disambiguation_matrices.md](references/disambiguation_matrices.md);
        `ELSE` the agent `MUST` request a valid screenshot file path from the
        caller.
*   **Direct Visual Execution Contract**:
    *   `IF` performing component detection on a screenshot, `THEN` the agent
        `MUST` inspect the image directly via `view_file(AbsolutePath=...)` and
        apply the rules in
        [references/disambiguation_matrices.md](references/disambiguation_matrices.md);
        `ELSE` the agent `MUST` route non-visual tasks to the appropriate code
        or rubric skill.
*   **Output Contract**:

    *   The agent `MUST` emit active progress headings structured with bold
        headers and horizontal dividers (`---`) summarizing **Pass 1 (Global
        Frame & Edge Chrome)**, **Pass 2 (Meso Flow Containers & Interactive
        Clusters)**, and **Pass 3 (Micro-Component Sweep)**, followed
        immediately by the complete JSON inventory adhering to this schema:

    ```json
    {
      "screenContext": {
        "platform": "mobile | tablet | desktop | wearable | automotive",
        "layoutTopology": "single_pane | split_pane | multi_column",
        "rootContainer": "Scaffold | Custom layout",
        "excludedOsChrome": ["status_bar_top", "gesture_handle_bottom"]
      },
      "components": [
        {
          "id": "comp_01",
          "name": "Top Header Bar",
          "mappedComponent": "App bar",
          "functionalAliases": ["Toolbar"],
          "componentType": "standard",
          "variant": "Center-aligned top app bar",
          "designDeviationNote": "",
          "subcomponents": [
            {
              "id": "comp_01_sub_01",
              "name": "Leading Navigation Trigger",
              "mappedComponent": "Icon button",
              "functionalAliases": ["Icon"],
              "componentType": "standard",
              "variant": "Standard icon button"
            }
          ]
        }
      ]
    }
    ```
*   **Error Handling Contract**:

    *   `IF` the target image file path does not exist, cannot be read by
        `view_file(AbsolutePath=...)`, or is corrupted, `THEN` the agent `MUST`
        return an explicit diagnostic error message identifying the unreadable
        file path and terminate immediately after returning the error
        diagnostic; `ELSE` the agent `MUST` proceed with Step 2 of the Thinking
        Path.
    *   `IF` the screenshot contains exclusively native OS system chrome with
        zero product UI elements, `THEN` the agent `MUST` return an empty
        `components` array (`"components": []`) with
        `screenContext.excludedOsChrome` populated; `ELSE` the agent `MUST` emit
        all detected product UI components in the `components` array.

--------------------------------------------------------------------------------

## Thinking Path (3-Pass Coarse-to-Fine Spatial Scan)

The agent `MUST` `EXECUTE` the following 5 algorithmic steps in exact sequence:

1.  **STEP 1 — DIRECT VISUAL INSPECTION & DELEGATE REFERENCE LOADING**:
    *   `CALL` `view_file(AbsolutePath=<target_image_path>)` once to inspect the
        target screenshot image directly, and `CALL`
        `view_file(AbsolutePath=...)` on
        [references/disambiguation_matrices.md](references/disambiguation_matrices.md)
        to load Matrices 1–4.
    *   `IF` `view_file` reports that the target screenshot file is missing or
        unreadable, `THEN` the agent `MUST` execute the Error Handling Contract
        and terminate immediately after returning the error diagnostic; `ELSE`
        the agent `MUST` advance to Step 2.
2.  **STEP 2 — PASS 1: GLOBAL FRAME & EDGE CHROME**:
    *   `IDENTIFY` `screenContext.platform`, `screenContext.layoutTopology`, and
        `screenContext.rootContainer` (`Scaffold` vs. `Custom layout`).
    *   `EXCLUDE` host OS system chrome (top status bar clock/Wi-Fi/battery
        icons and bottom OS gesture handle / 3-button system navigation) from
        `components` and `RECORD` them in `screenContext.excludedOsChrome`.
    *   `SCAN` docked and floating edge chrome using **Matrix 1** in
        [references/disambiguation_matrices.md](references/disambiguation_matrices.md):
        top edge (`App bar`, `Search bar`, `Tabs`, `Banner`), bottom edge
        (`Navigation bar`, `Bottom App Bar`, floating pill `Toolbar`,
        `Snackbar`, `Bottom sheet`), and lateral edges (`Navigation rail`,
        `Navigation drawer`, `Side sheet`).
    *   `IF` a top horizontal header strip contains navigation triggers (`Icon
        button`), title text, a `Search bar`, or trailing action/profile
        controls (`Icon button`, `Avatar`) on an opaque, transparent, or
        surface-matched background, `THEN` the agent `MUST` emit an enclosing
        parent **`App bar`** container alongside its child controls; `ELSE` the
        agent `MUST` classify standalone top elements according to their
        individual container geometry.
3.  **STEP 3 — PASS 2: MESO FLOW CONTAINERS & INTERACTIVE CLUSTERS**:
    *   `SCAN` vertical collections and horizontal tracks using **Matrix 3** in
        [references/disambiguation_matrices.md](references/disambiguation_matrices.md):
        *   `IF` a viewport region or sheet contains 2 or more vertically
            stacked peer surface containers (`Card` or `List item`) arranged
            along a shared vertical scroll axis, `THEN` the agent `MUST` emit
            **BOTH** the enclosing parent **`List`** container **AND** each
            child **`Card`** / **`List item`** component under the `Parent
            Co-location Invariant`; `ELSE` the agent `MUST` emit a single
            standalone surface without an enclosing `List`.
        *   `IF` a horizontal track contains 2 or more peer items exhibiting
            horizontal scroll affordances (`Edge Peek` clipping, overflow
            continuation, scroll arrows, or multi-browse hero geometry), `THEN`
            the agent `MUST` emit **BOTH** the parent **`Carousel`** container
            **AND** its child items (`Card`, `Image`, or `Chip`); `ELSE` the
            agent `MUST` classify fixed horizontal rows according to their
            static layout archetype.
    *   `APPLY` the `Sibling Uniformity Invariant` so peer elements with
        identical geometry receive identical classifications.
    *   `CLASSIFY` interactive control clusters (`Button group`, `Segmented
        button`, `Split button`, `Chip`, `FAB`, `Extended FAB`) using **Matrix
        2** and **Matrix 4** in
        [references/disambiguation_matrices.md](references/disambiguation_matrices.md).
4.  **STEP 4 — PASS 3: DEDICATED MICRO-COMPONENT SWEEP**:
    *   `FOR EACH` container identified in Passes 1–2, systematically inspect
        and `EMIT` every embedded micro-component:
        *   `IF` a visible 1dp hairline stroke or explicit surface-gap seam
            partitions sibling rows, sections, or split container cells
            (horizontally or vertically, in light or dark themes), `THEN` the
            agent `MUST` emit **`Divider`**; `ELSE` the agent `MUST` omit
            `Divider` for seamless surface transitions.
        *   `IF` a notification dot or numeric counter pill overlays an icon,
            tab, or button corner, `THEN` the agent `MUST` emit **`Badge`**;
            `ELSE` the agent `MUST` emit standalone icons or labels without
            badge overlays.
        *   `IF` an interactive icon trigger appears inside a bar, header, card,
            sheet, or input field, `THEN` the agent `MUST` emit **`Icon
            button`** (with `functionalAliases: ["Icon"]`); `ELSE` the agent
            `MUST` classify non-interactive decorative glyphs as **`Icon`**.
        *   `IF` a linear track or circular ring displays measurable completion
            or playback progress (`0%-100%`) without a draggable thumb, `THEN`
            the agent `MUST` emit **`Progress indicator`**; `ELSE` the agent
            `MUST` classify tracks with draggable thumbs as **`Slider`** and
            indeterminate spinners as **`Loading indicator`**.
        *   `IF` binary selection controls or editable parameter/text input
            boxes appear inside rows, forms, or cards, `THEN` the agent `MUST`
            emit **`Checkbox`**, **`Switch`**, **`Radio button`**, or **`Text
            field`**; `ELSE` the agent `MUST` classify static read-only text
            labels as **`Text`**.
        *   `IF` circular or rounded user/entity profile thumbnails appear in
            headers, lists, cards, or chat threads, `THEN` the agent `MUST` emit
            **`Avatar`**; `ELSE` the agent `MUST` classify general rectangular
            photography or illustrations as **`Image`**.
5.  **STEP 5 — STRUCTURAL/FUNCTIONAL RECONCILIATION & OUTPUT EMISSION**:
    *   `FOR EACH` detected element, `IF` its physical container geometry
        matches Component X while its functional role in the screen hierarchy
        matches Component Y, `THEN` the agent `MUST` assign `mappedComponent` to
        Component X, `MUST` include Component Y in `functionalAliases`, and
        `MUST` record a concise explanation in `designDeviationNote`; `ELSE` the
        agent `MUST` assign `mappedComponent` to Component X and populate
        `functionalAliases` with any applicable secondary visual archetypes with
        an empty `designDeviationNote`.
    *   `EMIT` the visually structured Markdown pass summary (with `---`
        dividers and bold headers) followed by the complete JSON object.

--------------------------------------------------------------------------------

## 1. Authoritative Valid Component Names (61 Canonical Strings)

The agent `MUST` map every detected component's `mappedComponent` field to one
of these 61 exact strings (or `"Custom component"`):

*   **App Bars & Toolbars**: `App bar`, `Bottom App Bar`, `Toolbar`
*   **Navigation**: `Navigation bar`, `Navigation rail`, `Navigation drawer`,
    `Tabs`, `Tab`
*   **Containers & Layout**: `Scaffold`, `Custom layout`, `Card`, `Carousel`,
    `List`, `List item`, `Bottom sheet`, `Side sheet`, `Dialog`, `Data Table`,
    `Divider`
*   **Buttons & Action Triggers**: `Button`, `Filled button`, `Filled tonal
    button`, `Outlined button`, `Elevated button`, `Text button`, `Button
    group`, `Split button`, `FAB`, `Extended FAB`, `Icon button`
*   **Selection, Input & Pickers**: `Chip`, `Segmented button`, `Switch`,
    `Checkbox`, `Radio button`, `Slider`, `Search`, `Search bar`, `Text field`,
    `Date picker`, `Time picker`
*   **Feedback, Status & Menus**: `Progress indicator`, `Loading indicator`,
    `Snackbar`, `Banner`, `Badge`, `Notification`, `Tooltip`, `Menu`, `Menu
    item`
*   **Media & Primitives**: `Avatar`, `Icon`, `Image`, `Text`, `Custom
    component`
*   **Generative AI (Aurora)**: `Aurora`, `Aurora chat bubble`, `Aurora prompt
    field`, `Aurora response carousel`, `Aurora response list`, `Aurora
    suggestions`
