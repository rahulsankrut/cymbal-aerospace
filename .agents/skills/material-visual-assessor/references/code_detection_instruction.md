<!-- disableFinding(HTML_BROKEN) -->
<!-- disableFinding(LINE_OVER_80) -->

# Codebase Component & Token Audit Guide

This delegate reference defines the rules for mapping source code selectors and
auditing Material Design 3 (M3) semantic token bindings across Web
(`@material/web`, gBreeze `<md-gb-*>`), Jetpack Compose, Android XML, and iOS.

--------------------------------------------------------------------------------

## 1. Cross-Platform M3 Component Mapping

`FOR EACH` UI element in the markup, template, or view hierarchy, the agent
`MUST` map framework-specific tags or composables to their exact canonical
`mappedComponent` string from `detector/SKILL.md`:

| Canonical         | Material Web (`@material/web`) &      | Jetpack Compose / Android XML /   |
: `mappedComponent` : gBreeze (`<md-gb-*>`)                 : iOS                               :
| :---------------- | :------------------------------------ | :-------------------------------- |
| **`App bar`**     | `<md-gb-top-app-bar>`,                | `CenterAlignedTopAppBar`,         |
:                   : `.md-top-app-bar`, sticky top         : `SmallTopAppBar`,                 :
:                   : `<header>`                            : `MediumTopAppBar`,                :
:                   :                                       : `LargeTopAppBar`,                 :
:                   :                                       : `MaterialToolbar`,                :
:                   :                                       : `UINavigationBar`                 :
| **`Navigation     | `<md-navigation-bar>`,                | `NavigationBar`,                  |
: bar` /            : `<md-navigation-tab>`,                : `NavigationBarItem`,              :
: `Navigation rail` : `<md-navigation-drawer>`              : `NavigationRail`,                 :
: / `Navigation     :                                       : `ModalNavigationDrawer`,          :
: drawer`**         :                                       : `PermanentNavigationDrawer`,      :
:                   :                                       : `UITabBar`                        :
| **`Tabs` &        | `<md-tabs>`, `<md-primary-tab>`,      | `PrimaryTabRow`,                  |
: `Tab`**           : `<md-secondary-tab>`                  : `SecondaryTabRow`,                :
:                   :                                       : `ScrollableTabRow`, `Tab`,        :
:                   :                                       : `TabLayout`                       :
| **`Filled button` | `<md-filled-button>`,                 | `Button`, `FilledTonalButton`,    |
: / `Filled tonal   : `<md-filled-tonal-button>`,           : `OutlinedButton`,                 :
: button` /         : `<md-outlined-button>`,               : `ElevatedButton`, `TextButton`,   :
: `Outlined button` : `<md-elevated-button>`,               : `MaterialButton`                  :
: / `Elevated       : `<md-text-button>`, `<md-gb-button>`  :                                   :
: button` / `Text   :                                       :                                   :
: button`**         :                                       :                                   :
| **`FAB` /         | `<md-fab>`, `<md-branded-fab>`,       | `FloatingActionButton`,           |
: `Extended FAB` /  : `<md-icon-button>`, `<md-gb-fab>`,    : `SmallFloatingActionButton`,      :
: `Icon button`**   : `<md-gb-icon-button>`                 : `LargeFloatingActionButton`,      :
:                   :                                       : `ExtendedFloatingActionButton`,   :
:                   :                                       : `IconButton`                      :
| **`Segmented      | `<md-outlined-segmented-button-set>`, | `SingleChoiceSegmentedButtonRow`, |
: button` / `Split  : `<md-outlined-segmented-button>`      : `MultiChoiceSegmentedButtonRow`,  :
: button` / `Button :                                       : `SplitButton`,                    :
: group`**          :                                       : `MaterialButtonToggleGroup`       :
| **`Card` / `List` | `<md-elevated-card>`,                 | `Card`, `ElevatedCard`,           |
: / `List item` /   : `<md-filled-card>`,                   : `OutlinedCard`, `LazyColumn`,     :
: `Divider`**       : `<md-outlined-card>`, `<md-gb-card>`, : `ListItem`, `HorizontalDivider`,  :
:                   : `<md-list>`, `<md-list-item>`,        : `VerticalDivider`                 :
:                   : `<md-gb-list>`, `<md-gb-list-item>`,  :                                   :
:                   : `<md-divider>`                        :                                   :
| **`Dialog` /      | `<md-dialog>`, `<md-menu>`,           | `AlertDialog`,                    |
: `Bottom sheet` /  : `<md-menu-item>`, `<md-sub-menu>`     : `ModalBottomSheet`,               :
: `Side sheet` /    :                                       : `BottomSheetScaffold`,            :
: `Menu` /          :                                       : `DropdownMenu`,                   :
: `Snackbar`**      :                                       : `DropdownMenuItem`,               :
:                   :                                       : `SnackbarHost`                    :
| **`Chip` / `Text  | `<md-assist-chip>`,                   | `AssistChip`, `FilterChip`,       |
: field` / `Search  : `<md-filter-chip>`,                   : `InputChip`, `SuggestionChip`,    :
: bar`**            : `<md-input-chip>`,                    : `OutlinedTextField`, `TextField`, :
:                   : `<md-suggestion-chip>`,               : `SearchBar`, `DockedSearchBar`    :
:                   : `<md-outlined-text-field>`,           :                                   :
:                   : `<md-filled-text-field>`              :                                   :
| **`Checkbox` /    | `<md-checkbox>`, `<md-gb-checkbox>`,  | `Checkbox`, `Switch`,             |
: `Switch` / `Radio : `<md-switch>`, `<md-gb-switch>`,      : `RadioButton`, `Slider`,          :
: button` /         : `<md-radio>`, `<md-slider>`,          : `RangeSlider`,                    :
: `Slider` /        : `<md-linear-progress>`,               : `LinearProgressIndicator`,        :
: `Progress         : `<md-circular-progress>`              : `CircularProgressIndicator`       :
: indicator`**      :                                       :                                   :

*   **Parent Co-location Rule**: `IF` a composite parent container (`<md-list>`,
    `NavigationBar`, `TopAppBar`, `PrimaryTabRow`) encloses child items, `THEN`
    the agent `MUST` emit BOTH the parent container (`List`, `Navigation bar`,
    `App bar`, `Tabs`) AND its child components (`List item`, `Icon button`,
    `Tab`).

--------------------------------------------------------------------------------

## 2. Semantic Token Binding Verification

When evaluating `rubric.md` (`Typography` Items 2-16, `Color` Items 1-36,
`Elevation` Items 1-3) and `quality.md` (`[Requires Code Inspection]`) in
`Code-Only` or `Hybrid` mode, `INSPECT` stylesheet declarations, `:root` / theme
scopes, and component props using these boolean evaluation rules:

1.  **Semantic Color Tokens (`Color` Items 8-36)**:
    *   `IF` a component's color declaration binds to its canonical M3 semantic
        token (`var(--md-sys-color-primary)`,
        `var(--md-sys-color-surface-container-high)`,
        `MaterialTheme.colorScheme.primary`, `?attr/colorPrimary`,
        `*Color.primary`) or a theme alias variable resolving to the specified
        GM3 baseline hex / HCT tonal step in
        [tokens/color_and_contrast.md](tokens/color_and_contrast.md), `THEN` the
        agent `MUST` evaluate that criterion as `"Yes"`; `ELSE IF` the style
        applies hardcoded raw hex/RGB literals (e.g., `background: #3b82f6;`),
        arbitrary gradients, or mismatched semantic pairings (e.g., `primary`
        text directly over `primary` container instead of `on-primary`), `THEN`
        the agent `MUST` evaluate that criterion as `"No"`; `ELSE` (`IF` the
        target color role is absent), the agent `MUST` evaluate it as `"N/A"`.
2.  **Typescale & Font Family Tokens (`Typography` Items 2-16)**:
    *   `IF` a text style binds to `--md-sys-typescale-*` /
        `MaterialTheme.typography.*` or specifies the exact `font-size`
        (`px`/`pt`/`rem`), `line-height`, `font-weight` (`400`/`500`), and
        `Google Sans` / `Google Sans Text` (or `SF Pro` on iOS) defined in
        [tokens/typography_and_shape.md](tokens/typography_and_shape.md), `THEN`
        the agent `MUST` evaluate that criterion as `"Yes"`; `ELSE IF` the style
        uses unscaled `px` sizes, wrong line-height/weight pairings, or unmapped
        system fonts (`Arial`, `Times`, `Roboto` where `Google Sans` is
        required), `THEN` the agent `MUST` evaluate that criterion as `"No"`;
        `ELSE` (`IF` that typescale role is absent), the agent `MUST` evaluate
        it as `"N/A"`.
3.  **Elevation, Shape & Accessibility Attributes**:
    *   `IF` elevation declarations use `--md-sys-elevation-level0` through
        `level5` (with `0dp` / `none` on resting flat elements) and corner radii
        use `--md-sys-shape-corner-*` (`4px` Extra Small through `9999px` Full
        pill), `THEN` the agent `MUST` evaluate the corresponding elevation and
        shape criteria as `"Yes"`; `ELSE` the agent `MUST` evaluate arbitrary
        shadows or non-conforming radii as `"No"`.
    *   `FOR EACH` `[Requires Code Inspection]` item in `quality.md`, `IF` the
        required attribute or media query (`@media (prefers-color-scheme:
        dark)`, `@media (prefers-reduced-motion: reduce)`, `aria-label` /
        `contentDescription` / `accessibilityLabel`, or semantic input
        attributes `type="email"`, `inputmode`, `keyboardType`) is present on
        all applicable elements, `THEN` the agent `MUST` evaluate it as `"Yes"`;
        `ELSE` the agent `MUST` evaluate it as `"No"` (or `"N/A"` when no such
        element exists).
4.  **Material 3 on iOS & Liquid Glass Code Verification**:
    *   **Apple Native Controls on iOS (`ios_native_*`)**:
        *   `Checkbox`: `IF` iOS code uses `UITableViewCell.accessoryType =
            .checkmark`, native `List(selection: ...)`, or SF Symbol
            `Image(systemName: "checkmark")`, `THEN` evaluate as `"Yes"`; `ELSE
            IF` uses `MDCCheckbox`, Compose `Checkbox`, `<md-checkbox>`, or
            custom square boxes, `THEN` evaluate as `"No"`.
        *   `Switch`: `IF` uses `UISwitch` or `Toggle`, `THEN` evaluate as
            `"Yes"`; `ELSE IF` uses `MDCSwitch`, Compose `Switch`, or
            `<md-switch>`, `THEN` evaluate as `"No"`.
        *   `Segmented Control`: `IF` uses `UISegmentedControl` or
            `Picker(...).pickerStyle(.segmented)`, `THEN` evaluate as `"Yes"`;
            `ELSE IF` uses `MDCOutlinedSegmentedButton` or Compose segmented
            button rows, `THEN` evaluate as `"No"`.
        *   `App Bar`: `IF` uses `UINavigationBar`, `UINavigationController`, or
            SwiftUI `NavigationStack` / `.toolbar`, `THEN` evaluate as `"Yes"`;
            `ELSE IF` uses `MDCFlexibleHeaderView`, `MDCTopAppBar`, or Compose
            `TopAppBar`, `THEN` evaluate as `"No"`.
        *   `Menus & Action Sheets`: `IF` uses `UIAlertController(...,
            preferredStyle: .actionSheet)`, `UIContextMenuInteraction`, SwiftUI
            `.contextMenu`, or `.confirmationDialog`, `THEN` evaluate as
            `"Yes"`; `ELSE IF` uses `MDCMenu` or Compose `DropdownMenu`, `THEN`
            evaluate as `"No"`.
        *   `Date Pickers`: `IF` uses `UIDatePicker` or SwiftUI `DatePicker`,
            `THEN` evaluate as `"Yes"`; `ELSE IF` uses `MDCDatePicker` or
            Compose `DatePicker`, `THEN` evaluate as `"No"`.
        *   `Native Lists`: `IF` uses `UITableView`, `UICollectionView`, or
            SwiftUI `List`, `THEN` evaluate as `"Yes"`; `ELSE IF` uses custom
            non-native list wrappers, `THEN` evaluate as `"No"`.
    *   **Liquid Glass on iOS (`ios_lg_*`)**:
        *   **Always-On Glass (Functional Layer)**: `IF` component (`FAB`, `FAB
            Menu`, `NavigationBar`, `Dialog`, `BottomSheet`, `Toolbar`,
            `Snackbar`, `NavigationRail`) applies the Material Glass variant,
            `UIBlurEffect(style: .systemMaterial)` / `UIVisualEffectView`, or
            SwiftUI `.background(.ultraThinMaterial)` /
            `.background(.thinMaterial)`, `THEN` evaluate as `"Yes"`; `ELSE IF`
            locked to a solid opaque fill with zero blur/alpha, `THEN` evaluate
            as `"No"`.
        *   **Opt-In Glass (Functional vs. Content Layer)**: For `Buttons`,
            `Search`, `Tabs`, and `Banners`, `IF` placed on the Functional Layer
            (floating over content or docked) and binds to the `.glass` variant
            or blur modifier, `THEN` evaluate as `"Yes"`; `ELSE IF` placed on
            the Content Layer (inline scrolling content, forms, cards) and
            defaults to standard non-glass opaque/outlined/tonal variants,
            `THEN` evaluate as `"Yes"`; `ELSE` (`IF` variant is mismatched to
            layer context), `THEN` evaluate as `"No"`.
