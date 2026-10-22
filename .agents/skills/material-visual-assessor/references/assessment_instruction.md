<!-- disableFinding(LINK_RELATIVE_G3DOC) -->
<!-- disableFinding(LINE_OVER_80) -->

# Material Design 3 Assessment Protocol

This delegate specification defines the **Two-Pass Evaluation Protocol**, the
authoritative **Component-to-Rubric Mapping**, the **Modality Evaluation
Matrix**, and the core compliance grading rules for full Material Design 3 (M3)
assessments.

--------------------------------------------------------------------------------

## 1. Two-Pass Evaluation Model

1.  **Pass 1 — Foundational Screen-Level Evaluation (`MANDATORY` for Full
    Audits)**:
    *   The agent `MUST` evaluate all 65 foundational criteria in
        [rubric.md](rubric.md) across `Typography`, `Color`, `Layout`,
        `Elevation`, and `Accessibility`.
    *   `IF` evaluating holistic application quality or design craft, `THEN` the
        agent `SHOULD` also evaluate the 28 supplemental criteria in
        [quality.md](quality.md).
2.  **Pass 2 — Component-Level Evaluation (`PER DETECTED COMPONENT`)**:
    *   `FOR EACH` component present in the verified component inventory, the
        agent `MUST` look up its primary structural `mappedComponent` (and any
        nested `subcomponents`) in the **Component-to-Rubric Mapping** below,
        `READ` the mapped `references/rubrics/<slug>.md` file, and `EVALUATE`
        every criterion in that file.
    *   The agent `MUST NOT` load or evaluate component rubric files for
        secondary `functionalAliases` or components absent from the screen.

--------------------------------------------------------------------------------

## 2. Component-to-Rubric Mapping

Use this mapping to identify which file to read for each detected component
type:

-   `App bar`, `Search App Bar`, `Small App Bar`, `Medium App Bar`, `Large App
    Bar` -> `references/rubrics/app-bars.md`
-   `Aurora`, `Aurora chat bubble`, `Aurora prompt field`, `Aurora response
    carousel`, `Aurora response list`, `Aurora suggestions` ->
    `references/rubrics/aurora.md`
-   `Badge` -> `references/rubrics/badge.md`
-   `Banner` -> `references/rubrics/banners.md`
-   `Bottom App Bar` -> `references/rubrics/bottom-app-bar.md`
-   `Bottom sheet` -> `references/rubrics/bottom-sheet.md`
-   `Button`, `Elevated button`, `Filled button`, `Filled tonal button`,
    `Outlined button`, `Text button` -> `references/rubrics/buttons.md`
-   `Button group` -> `references/rubrics/button-group.md`
-   `Card` -> `references/rubrics/card.md`
-   `Carousel` -> `references/rubrics/carousel.md`
-   `Checkbox` -> `references/rubrics/checkbox.md`
-   `Chip` -> `references/rubrics/chip.md`
-   `Data Table` -> `references/rubrics/data-table.md`
-   `Date picker` -> `references/rubrics/date-picker.md`
-   `Dialog` -> `references/rubrics/dialog.md`
-   `Divider` -> `references/rubrics/divider.md`
-   `FAB`, `Extended FAB` -> `references/rubrics/fabs.md`
-   `Icon button` -> `references/rubrics/icon-button.md`
-   `List`, `List item` -> `references/rubrics/list.md`
-   `Loading indicator` -> `references/rubrics/loading-indicator.md`
-   `Menu`, `Menu item` -> `references/rubrics/menu.md`
-   `Navigation bar` -> `references/rubrics/navigation-bars.md`
-   `Navigation drawer` -> `references/rubrics/navigation-drawer.md`
-   `Navigation rail` -> `references/rubrics/navigation-rail.md`
-   `Progress indicator` -> `references/rubrics/progress-indicator.md`
-   `Radio button` -> `references/rubrics/radio-button.md`
-   `Search`, `Search bar` -> `references/rubrics/search.md`
-   `Segmented button` -> `references/rubrics/segmented-button.md`
-   `Side sheet` -> `references/rubrics/side-sheet.md`
-   `Slider` -> `references/rubrics/slider.md`
-   `Snackbar` -> `references/rubrics/snackbar.md`
-   `Split button` -> `references/rubrics/split-button.md`
-   `Switch` -> `references/rubrics/switch.md`
-   `Tabs`, `Tab` -> `references/rubrics/tabs.md`
-   `Text field` -> `references/rubrics/text-field.md`
-   `Time picker` -> `references/rubrics/time-picker.md`
-   `Toolbar` -> `references/rubrics/toolbar.md`
-   `Tooltip` -> `references/rubrics/tooltip.md`

--------------------------------------------------------------------------------

## 3. Answer Values & Modality Evaluation Matrix

### Answer Value Contract (`"Yes"`, `"No"`, or `"N/A"`)

*   **Presence Identification Questions**: `IF` a criterion asks whether a
    component or sub-element is present (e.g., *"Is there a Button...?"*),
    `THEN` the agent `MUST` answer `"Yes"` or `"No"`, and `MUST NOT` answer
    `"N/A"`.
*   **Compliance & Styling Questions**: `IF` the target component, variant, or
    UI state is absent from the inspected screen/codebase, `THEN` the agent
    `MUST` answer `"N/A"`; `ELSE` the agent `MUST` answer `"Yes"` when all
    specified requirements are satisfied and `"No"` when any requirement is
    violated.
*   **Component Category Boundaries**:
    *   `IF` a detected action control is a `FAB`, `Extended FAB`, or `Icon
        button`, `THEN` the agent `MUST` route it exclusively to
        `references/rubrics/fabs.md` or `references/rubrics/icon-button.md` and
        `SKIP` `references/rubrics/buttons.md`; `ELSE` (`IF` the control is a
        standard `Button`, `Filled button`, `Elevated button`, `Filled tonal
        button`, `Outlined button`, or `Text button`), the agent `MUST` evaluate
        it under `references/rubrics/buttons.md`.
    *   `IF` a navigation or action item is nested inside a top `App bar` or
        `Tabs` strip, `THEN` the agent `MUST` route it exclusively to
        `references/rubrics/app-bars.md` or `references/rubrics/tabs.md` and
        `SKIP` `references/rubrics/navigation-bars.md`; `ELSE` (`IF` the
        destination is inside a bottom `Navigation bar`), the agent `MUST`
        evaluate it under `references/rubrics/navigation-bars.md`.

### Modality Evaluation Matrix

| Input Modality    | Source of Truth | Criteria Answered | Criteria Answered `"N/A"`                      |
:                   :                 : `"Yes"` / `"No"`  :                                                :
| :---------------- | :-------------- | :---------------- | :--------------------------------------------- |
| **`Visual-Only`** | Rendered        | All visual        | Criteria explicitly tagged `[Requires Code     |
: (Screenshot /     : pixels,         : layout, geometry, : Inspection]` or absent components/variants     :
: Image)            : geometry,       : contrast,         :                                                :
:                   : contrast, and   : typography        :                                                :
:                   : light/dark      : scale/letterform, :                                                :
:                   : tonal hierarchy : and tonal color   :                                                :
:                   :                 : role checks       :                                                :
| **`Code-Only`**   | DOM structure,  | All token         | Purely visual rendering checks requiring       |
: (HTML / CSS /     : component       : binding,          : photographic imagery or hardware bezels        :
: Compose / XML /   : selectors,      : typography        : (`accessibility_text_legibility_over_imagery`, :
: Tokens)           : `--md-sys-*` /  : specification,    : `layout_hardware_clipping`) when absent from   :
:                   : `MaterialTheme` : component         : code                                           :
:                   : tokens, and CSS : structure, and    :                                                :
:                   : declarations    : layout rules      :                                                :
| **`Hybrid`**      | Code wins for   | All foundational, | Only criteria for components, variants, or     |
: (Screenshot +     : exact token     : quality, and      : states absent from both visual and code        :
: Codebase)         : bindings and    : present component :                                                :
:                   : `px`/`rem`      : criteria          :                                                :
:                   : values; Visual  :                   :                                                :
:                   : wins for        :                   :                                                :
:                   : rendered        :                   :                                                :
:                   : contrast,       :                   :                                                :
:                   : overlap, and    :                   :                                                :
:                   : clipping        :                   :                                                :

--------------------------------------------------------------------------------

## 4. Core M3 Compliance Principles

*   **Static Baseline vs. Dynamic Color (`color_gm_primary` & `Color` Items
    8-36)**:
    *   `IF` the UI uses static GM3 baseline colors or a structured M3 tonal
        palette, `THEN` evaluate `color_gm_primary` (`"Yes"` if
        `sys.color.primary` / `primary-container` fill is reserved for focal
        CTAs, FABs, at most one primary Filled button, and active state
        indicators; `"No"` if multiple competing actions share primary fills).
    *   `IF` the UI uses unstructured non-Material custom branding where M3
        primary color roles do not exist, `THEN` mark `color_gm_primary` as
        `"N/A"`.
*   **Flat Design vs. Missing Elevation (`color_drop_shadows` &
    `elevation_modal_separation`)**:
    *   `IF` the UI is intentionally flat with zero overlapping modals/sheets
        and uses clean tonal surface separation, `THEN` answer `"Yes"` for
        `color_drop_shadows` and `"N/A"` for `elevation_modal_separation`.
    *   `IF` floating overlays (`Dialog`, `Bottom sheet`, `Menu`, `FAB`) lack
        both a scrim and elevation/tonal separation from underlying content,
        `THEN` answer `"No"` for `elevation_modal_separation`.
    *   `IF` the UI is in dark theme where drop shadows are not visually
        detectable, `THEN` answer `"N/A"` for `color_drop_shadows`.
*   **Native Contrast & Legibility (`color_text_contrast`)**:
    *   Evaluate text-on-surface and icon-on-container contrast directly against
        the WCAG/GAR thresholds (`4.5:1` body text, `3:1` large text and active
        UI graphics) defined in
        [tokens/color_and_contrast.md](tokens/color_and_contrast.md).
*   **Component Geometry & Touch Target Modality Rule**:
    *   `IF` evaluating component rubric criteria that specify exact `dp`
        dimensions (`40dp`, `56dp`, `12dp`, `28dp`, `48x48dp touch target`) or
        `sys.shape.*` / `sys.color.*` tokens in `Code-Only` or `Hybrid` mode,
        `THEN` the agent `MUST` verify exact `dp`/`px`/`rem` values and
        `--md-sys-*` / `MaterialTheme` token bindings.
    *   `IF` evaluating those criteria in `Visual-Only` mode (screenshot),
        `THEN` the agent `MUST` verify proportional visual geometry (e.g., full
        pill/capsule vs. rounded rectangle radius, unobstructed `~48dp` hit
        spacing around interactive icons, and canonical tonal/color role
        appearance).

--------------------------------------------------------------------------------

## 5. Material 3 on iOS & Liquid Glass Compliance Protocol

Referencing the authoritative **GM3: Liquid Glass + Material Glass Component
Catalog**:

1.  **Apple Native vs. Material Components on iOS**:

    *   **Mandatory Native Apple Controls**: On iOS, applications `MUST` render
        designated controls using Apple native UIKit / SwiftUI controls rather
        than custom Material components:
        *   `Checkbox` -> Native list checkmarks
            (`UITableViewCell.accessoryType = .checkmark`, native `List`
            selection, or SF Symbol checkmarks).
        *   `Switch` -> Native `UISwitch` / `Toggle`.
        *   `Segmented Control` -> Native `UISegmentedControl` /
            `Picker.pickerStyle(.segmented)`.
        *   `App Bar` -> Native `UINavigationBar` / `NavigationStack` /
            `.toolbar`.
        *   `Menus & Action Sheets` -> Native `UIContextMenuInteraction` /
            `UIAlertController(style: .actionSheet)`.
        *   `Date Pickers` -> Native `UIDatePicker` / `DatePicker`.
        *   `Native Lists` -> Native `UITableView` / `UICollectionView` /
            `List`.
        *   `Transitions` -> Native iOS platform view transitions.
    *   **Pass Criterion (`"Yes"`)**: `IF` an iOS app correctly uses the native
        Apple component, it `MUST` pass with **`"Yes"`** (the assessor `MUST
        NOT` penalize for missing Material styling such as missing Material
        container fills or non-Material corner radii).
    *   **Fail Criterion (`"No"`)**: `IF` an iOS app incorrectly uses an
        Android/Web-style Material component where native is required (such as a
        square Material checkbox or Material switch), it `MUST` be penalized
        with **`"No"`**.
    *   **Absent Component Gate (`"N/A"`)**: `IF` the component is absent from
        the view or codebase, evaluate strictly as **`"N/A"`**.

2.  **Liquid Glass & Layer Hierarchy**:

    *   **Always-On Glass (Functional Layer)**:
        *   Components designated for the functional layer (`FAB`, `FAB Menu`,
            `Nav Bar (Docked)`, `Bottom Sheet`, `Dialog`, `Toolbar
            (Standard/Vibrant)`, `Snackbar`, `Nav Rail`) reside persistently or
            modally above content and `MUST` always have the translucent Liquid
            Glass / Material Glass effect (translucent backdrop blur and
            specular edge highlights) applied.
        *   `IF` any functional layer component uses a solid opaque surface fill
            blocking backdrop visibility, evaluate as **`"No"`**.
    *   **Opt-In Glass (Functional Layer vs. Content Layer)**:
        *   Components supporting opt-in glass (`Buttons (Label)`, `Icon
            Buttons`, `Split Button`, `Button Group (Standard & Connected)`,
            `Search App Bar`, `Search`, `Tabs`, `Banner`):
        *   `IF` placed on the **Functional Layer** (floating over content or
            docked in floating headers/bars), they `MUST` explicitly enable the
            Glass variant.
        *   `IF` placed on the **Content Layer** (embedded inside scrollable
            body content, forms, lists, or standard cards), they `MUST` remain
            **Non-Glass** (default opaque surface fills) to preserve legibility
            and prevent visual mud.
        *   `IF` variant selection does not match layer context, evaluate as
            **`"No"`**.
