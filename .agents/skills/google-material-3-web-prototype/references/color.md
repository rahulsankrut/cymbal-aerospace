# Material 3 Color Reference

The Google Material 3 color system provides a dynamic, accessible, and expressive color architecture for web prototyping. It is built around semantic color roles, automated theme adaptation, and strict contrast guarantees.

## Color System Architecture

Material 3 shifts away from hardcoding fixed hex colors. Instead, UI components are styled using semantic color roles mapped to CSS custom properties (`--md-sys-color-*`).

### Core Concepts

* **Paint-by-Number Model**: UI elements are assigned semantic roles (such as Primary, Surface Container, or On Surface) rather than explicit color values. The underlying value changes automatically depending on the active color scheme or theme.
* **Dynamic & Static Color Schemes**:
  * **Static Baseline Scheme**: The default Google Material 3 color scheme (Baseline Blue), providing consistent, recognizable branding across light and dark modes.
  * **Dynamic User-Generated Color**: Color schemes extracted from a user's wallpaper using quantization algorithms.
  * **Dynamic Content-Based Color**: Color schemes extracted from in-app imagery (such as album art, hero banners, or media thumbnails) to create immersive content moments.
* **Native Runtime Theme Switching**: CSS custom properties in `design-system-bindings.css` utilize the CSS `light-dark(lightValue, darkValue)` color function. When the user toggles light or dark mode via browser settings or CSS `color-scheme: light dark`, all UI elements update instantly without JavaScript DOM manipulation.
* **HCT Color Space & Accessibility**: Color roles are defined in the Hue-Chroma-Tone (HCT) color space. The algorithm enforces specific lightness tone deltas between paired roles to guarantee minimum contrast ratios:
  * **3:1 Minimum Contrast**: Required for UI boundaries, container edges, and large display text.
  * **4.5:1 Minimum Contrast**: Required for standard body text, labels, and icons.

**Pull [ColorAdvanced](color_advanced.md)** when defining custom baseline schemes, adjusting color fidelity, harmonizing static/brand colors with dynamic primary accents, or creating custom color roles.

**Pull [ColorAI](color_ai.md)** when implementing Generative AI features, multi-stop AI gradients, or Gemini-branded components.

## Key Color Roles & Usage

Color roles are grouped into functional families based on their visual purpose and hierarchy.

### Accent Color Roles

Accent roles draw attention to key interactive components, state changes, and primary call-to-actions.

* **Primary (`--md-sys-color-primary`)**: High-emphasis fills, primary action buttons, active navigation indicators, and prominent UI highlights.
* **On Primary (`--md-sys-color-on-primary`)**: Text and icons displayed against `Primary` backgrounds.
* **Primary Container (`--md-sys-color-primary-container`)**: Standout background fill for key components like Floating Action Buttons (FABs) or selected item containers.
* **On Primary Container (`--md-sys-color-on-primary-container`)**: High-contrast text and icons displayed against `Primary Container` backgrounds.
* **Secondary (`--md-sys-color-secondary`)**: Accent for less prominent components, filter chips, or secondary controls.
* **On Secondary (`--md-sys-color-on-secondary`)**: Text and icons displayed against `Secondary` backgrounds.
* **Secondary Container (`--md-sys-color-secondary-container`)**: Low-emphasis container background for tonal buttons, selected filter chips, or badge backgrounds.
* **On Secondary Container (`--md-sys-color-on-secondary-container`)**: Text and icons displayed against `Secondary Container` backgrounds.
* **Tertiary (`--md-sys-color-tertiary`)**: Contrasting accent for special emphasis, badges, input field highlights, or balancing primary and secondary accents.
* **On Tertiary (`--md-sys-color-on-tertiary`)**: Text and icons displayed against `Tertiary` backgrounds.
* **Tertiary Container (`--md-sys-color-tertiary-container`)**: Container fill for callout cards, AI response containers, or prompt field suggestions.
* **On Tertiary Container (`--md-sys-color-on-tertiary-container`)**: Text and icons displayed against `Tertiary Container` backgrounds.
* **Error (`--md-sys-color-error`)**: Urgent attention-grabbing color for invalid form inputs, error badges, and destructive action triggers.
* **On Error (`--md-sys-color-on-error`)**: Text and icons displayed against `Error` backgrounds.
* **Error Container (`--md-sys-color-error-container`)**: Soft background container for error banners, validation alerts, and alert dialogs.
* **On Error Container (`--md-sys-color-on-error-container`)**: Text and icons displayed against `Error Container` backgrounds.

### Surface & Container Roles

Surface roles establish layout regions, container hierarchy, and visual depth.

* **Surface (`--md-sys-color-surface`)**: Default full-screen background color and default card surface.
* **On Surface (`--md-sys-color-on-surface`)**: Primary text, titles, headlines, and high-emphasis icons on any surface or container background.
* **On Surface Variant (`--md-sys-color-on-surface-variant`)**: Secondary body copy, subtitles, helper captions, disabled text, and inactive icons on surface backgrounds.
* **Surface Variant (`--md-sys-color-surface-variant`)**: Alternate surface background used for active or selected states.

#### Tone-Based Surface Containers

Material 3 communicates elevation through tone-based surface container tiers rather than opacity tint overlays. Higher tiers represent higher elevation and emphasis.

* **Surface Container Lowest (`--md-sys-color-surface-container-lowest`)**: Lowest container elevation (pure white in light mode) for cards sitting inside grouped surfaces.
* **Surface Container Low (`--md-sys-color-surface-container-low`)**: Low-emphasis container background for grouped card containers or secondary side sheets.
* **Surface Container (`--md-sys-color-surface-container`)**: Standard container role for cards, dialogs, list item groups, and side sheets.
* **Surface Container High (`--md-sys-color-surface-container-high`)**: High-emphasis container background for top app bars, elevated cards, or popover menus.
* **Surface Container Highest (`--md-sys-color-surface-container-highest`)**: Highest-emphasis container role for search fields, text inputs, or highlighted interactive items.

#### Bright & Dim Surface Roles

Add-on surface roles that maintain relative lightness across Light and Dark themes:

* **Surface Dim (`--md-sys-color-surface-dim`)**: Surface color that remains dim across both light and dark themes.
* **Surface Bright (`--md-sys-color-surface-bright`)**: Surface color that remains bright across both light and dark themes.

#### Inverse Surface Roles

Inverse roles create high-contrast floating components that stand out against surrounding UI surfaces.

* **Inverse Surface (`--md-sys-color-inverse-surface`)**: Inverted dark surface for snackbars and dark popovers.
* **Inverse On Surface (`--md-sys-color-inverse-on-surface`)**: Light text and icons displayed against `Inverse Surface` backgrounds.
* **Inverse Primary (`--md-sys-color-inverse-primary`)**: Action buttons (e.g. "Undo" text button) displayed on `Inverse Surface` snackbars.

### Outline & Utility Roles

Boundary and overlay roles for structural lines, dividers, and floating overlays.

* **Outline (`--md-sys-color-outline`)**: Standard border color for text field outlines, outlined buttons, and high-contrast boundaries (guarantees a 3:1 contrast ratio).
* **Outline Variant (`--md-sys-color-outline-variant`)**: Subtle boundary color for card dividers, list separators, and non-structural element boundaries.
* **Scrim (`--md-sys-color-scrim`)**: Overlay color used behind modal dialogs and bottom sheets to darken obscured content.
* **Shadow (`--md-sys-color-shadow`)**: Shadow color applied to elevated cards and floating panels.

### Fixed Accent Roles

Fixed accent roles maintain constant tonal values across Light and Dark themes, preventing color shifts in special UI moments.

* **Primary Fixed (`--md-sys-color-primary-fixed`)**: Primary fill that maintains constant light tone in both light and dark themes.
* **Primary Fixed Dim (`--md-sys-color-primary-fixed-dim`)**: Dimmer variant of Primary Fixed.
* **On Primary Fixed (`--md-sys-color-on-primary-fixed`)**: Text/icons on Primary Fixed fills.
* **On Primary Fixed Variant (`--md-sys-color-on-primary-fixed-variant`)**: Lower-emphasis text/icons on Primary Fixed fills.
* **Secondary Fixed (`--md-sys-color-secondary-fixed`)**: Secondary fill maintaining constant tone.
* **Secondary Fixed Dim (`--md-sys-color-secondary-fixed-dim`)**: Dimmer variant of Secondary Fixed.
* **On Secondary Fixed (`--md-sys-color-on-secondary-fixed`)**: Text/icons on Secondary Fixed fills.
* **On Secondary Fixed Variant (`--md-sys-color-on-secondary-fixed-variant`)**: Lower-emphasis text/icons on Secondary Fixed fills.
* **Tertiary Fixed (`--md-sys-color-tertiary-fixed`)**: Tertiary fill maintaining constant tone.
* **Tertiary Fixed Dim (`--md-sys-color-tertiary-fixed-dim`)**: Dimmer variant of Tertiary Fixed.
* **On Tertiary Fixed (`--md-sys-color-on-tertiary-fixed`)**: Text/icons on Tertiary Fixed fills.
* **On Tertiary Fixed Variant (`--md-sys-color-on-tertiary-fixed-variant`)**: Lower-emphasis text/icons on Tertiary Fixed fills.

## Color Token Reference Table

The table below lists all runtime CSS variables defined in `design-system-bindings.css`, including light/dark theme values and exact pairing rules.

| CSS Variable Token | Light Value | Dark Value | Description & Pairing Guidance |
| :--- | :--- | :--- | :--- |
| `--md-sys-color-primary` | `#0b57d0` | `#a8c7fa` | Main accent for primary buttons & active states. Pair with `on-primary`. |
| `--md-sys-color-on-primary` | `#ffffff` | `#062e6f` | Text and icons placed on `primary` backgrounds. |
| `--md-sys-color-primary-container` | `#d3e3fd` | `#0842a0` | Soft highlight fill for FABs, key cards, badges. Pair with `on-primary-container`. |
| `--md-sys-color-on-primary-container` | `#0842a0` | `#d3e3fd` | Text and icons placed on `primary-container`. |
| `--md-sys-color-primary-fixed` | `#d3e3fd` | `#d3e3fd` | Fixed light primary fill across themes. Pair with `on-primary-fixed`. |
| `--md-sys-color-primary-fixed-dim` | `#a8c7fa` | `#a8c7fa` | Dimmer fixed primary fill across themes. |
| `--md-sys-color-on-primary-fixed` | `#041e49` | `#041e49` | Text and icons placed on `primary-fixed`. |
| `--md-sys-color-on-primary-fixed-variant` | `#0842a0` | `#0842a0` | Secondary emphasis text/icons on `primary-fixed`. |
| `--md-sys-color-secondary` | `#00639b` | `#7fcfff` | Accent for filter chips and secondary controls. Pair with `on-secondary`. |
| `--md-sys-color-on-secondary` | `#ffffff` | `#003355` | Text and icons placed on `secondary` backgrounds. |
| `--md-sys-color-secondary-container` | `#c2e7ff` | `#004a77` | Fill for tonal buttons and selected filter chips. Pair with `on-secondary-container`. |
| `--md-sys-color-on-secondary-container` | `#004a77` | `#c2e7ff` | Text and icons placed on `secondary-container`. |
| `--md-sys-color-secondary-fixed` | `#c2e7ff` | `#c2e7ff` | Fixed light secondary fill across themes. Pair with `on-secondary-fixed`. |
| `--md-sys-color-secondary-fixed-dim` | `#7fcfff` | `#7fcfff` | Dimmer fixed secondary fill across themes. |
| `--md-sys-color-on-secondary-fixed` | `#001d35` | `#001d35` | Text and icons placed on `secondary-fixed`. |
| `--md-sys-color-on-secondary-fixed-variant` | `#004a77` | `#004a77` | Secondary emphasis text/icons on `secondary-fixed`. |
| `--md-sys-color-tertiary` | `#146c2e` | `#6dd58c` | Contrasting accent for special callouts & input highlights. Pair with `on-tertiary`. |
| `--md-sys-color-on-tertiary` | `#ffffff` | `#0a3818` | Text and icons placed on `tertiary` backgrounds. |
| `--md-sys-color-tertiary-container` | `#c4eed0` | `#0f5223` | Fill for AI response cards and suggestion chips. Pair with `on-tertiary-container`. |
| `--md-sys-color-on-tertiary-container` | `#0f5223` | `#c4eed0` | Text and icons placed on `tertiary-container`. |
| `--md-sys-color-tertiary-fixed` | `#c4eed0` | `#c4eed0` | Fixed light tertiary fill across themes. Pair with `on-tertiary-fixed`. |
| `--md-sys-color-tertiary-fixed-dim` | `#6dd58c` | `#6dd58c` | Dimmer fixed tertiary fill across themes. |
| `--md-sys-color-on-tertiary-fixed` | `#072711` | `#072711` | Text and icons placed on `tertiary-fixed`. |
| `--md-sys-color-on-tertiary-fixed-variant` | `#0f5223` | `#0f5223` | Secondary emphasis text/icons on `tertiary-fixed`. |
| `--md-sys-color-surface` | `#ffffff` | `#131314` | Standard screen background and default card surface. Pair with `on-surface`. |
| `--md-sys-color-on-surface` | `#1f1f1f` | `#e3e3e3` | Main body text, headlines, and primary icons on surface. |
| `--md-sys-color-on-surface-variant` | `#444746` | `#c4c7c5` | Muted captions, subtitles, helper text, and secondary icons. |
| `--md-sys-color-surface-variant` | `#e1e3e1` | `#444746` | Alternate surface background for active or selected states. |
| `--md-sys-color-surface-container-lowest` | `#ffffff` | `#0e0e0e` | Lowest container elevation tier (e.g. cards on low backgrounds). |
| `--md-sys-color-surface-container-low` | `#f8fafd` | `#1b1b1b` | Low container elevation tier for card groupings. |
| `--md-sys-color-surface-container` | `#f0f4f9` | `#1e1f20` | Standard container tier for cards, dialogs, and side sheets. |
| `--md-sys-color-surface-container-high` | `#e9eef6` | `#282a2c` | High container tier for top app bars and elevated popovers. |
| `--md-sys-color-surface-container-highest` | `#dde3ea` | `#333537` | Highest container tier for search fields and active selection fills. |
| `--md-sys-color-surface-dim` | `#d3dbe5` | `#131314` | Surface dim role across light and dark themes. |
| `--md-sys-color-surface-bright` | `#ffffff` | `#37393b` | Surface bright role across light and dark themes. |
| `--md-sys-color-surface-tint` | `#6991d6` | `#d1e1ff` | Tint overlay reference color. |
| `--md-sys-color-surface-tint-color` | `#0b57d0` | `#a8c7fa` | Base color for surface tinting. |
| `--md-sys-color-error` | `#b3261e` | `#f2b8b5` | Main error fill and icon accent. Pair with `on-error`. |
| `--md-sys-color-on-error` | `#ffffff` | `#601410` | Text and icons placed on `error` backgrounds. |
| `--md-sys-color-error-container` | `#f9dedc` | `#8c1d18` | Soft background for error banners and validation cards. Pair with `on-error-container`. |
| `--md-sys-color-on-error-container` | `#8c1d18` | `#f9dedc` | Text and icons placed on `error-container`. |
| `--md-sys-color-outline` | `#747775` | `#8e918f` | Standard 3:1 contrast boundary for text fields and outlined buttons. |
| `--md-sys-color-outline-variant` | `#c4c7c5` | `#444746` | Subtle divider and card separator line color. |
| `--md-sys-color-inverse-surface` | `#303030` | `#e3e3e3` | Inverted surface for snackbars and floating alert panels. Pair with `inverse-on-surface`. |
| `--md-sys-color-inverse-on-surface` | `#f2f2f2` | `#303030` | Text and icons placed on `inverse-surface`. |
| `--md-sys-color-inverse-primary` | `#a8c7fa` | `#0b57d0` | Action text button color placed on `inverse-surface`. |
| `--md-sys-color-scrim` | `#000000` | `#000000` | Backdrop overlay for modal dialogs and side sheets. |
| `--md-sys-color-shadow` | `#000000` | `#000000` | Elevation shadow color. |
| `--md-sys-color-background` | `#ffffff` | `#131314` | Legacy background role (use `surface` instead). |
| `--md-sys-color-on-background` | `#1f1f1f` | `#e3e3e3` | Legacy text color on background (use `on-surface` instead). |

## Color Pairing & Prototyping Rules

When writing HTML and CSS for web prototypes, follow these pairing and mapping rules.

### Strict Pairing Rules

* **Always Pair "On" Roles with Fill Roles**: Text or icons placed inside a filled element MUST use the matching "On" role token.
  * Correct: `<div style="background-color: var(--md-sys-color-primary); color: var(--md-sys-color-on-primary);">`
  * Incorrect: `<div style="background-color: var(--md-sys-color-primary); color: var(--md-sys-color-surface);">`
* **Container Role Pairing**:
  * On `primary-container` -> use `on-primary-container`.
  * On `secondary-container` -> use `on-secondary-container`.
  * On `tertiary-container` -> use `on-tertiary-container`.
  * On `error-container` -> use `on-error-container`.
* **Surface Text Hierarchy**:
  * High-emphasis text and titles -> use `on-surface`.
  * Secondary body text, captions, and subtitles -> use `on-surface-variant`.

### Component Color Mapping Rules

Standard web components and gBreeze controls map to specific color roles:

* **Buttons**:
  * **Filled Button**: Background `var(--md-sys-color-primary)`, Text/Icon `var(--md-sys-color-on-primary)`.
  * **Tonal Button**: Background `var(--md-sys-color-secondary-container)`, Text/Icon `var(--md-sys-color-on-secondary-container)`.
  * **Outlined Button**: Border `var(--md-sys-color-outline)`, Text/Icon `var(--md-sys-color-primary)`.
  * **Text Button**: Background transparent, Text/Icon `var(--md-sys-color-primary)`.
* **Cards**:
  * **Filled Card**: Surface `var(--md-sys-color-surface-container-highest)` or `var(--md-sys-color-surface-container)`.
  * **Elevated Card**: Surface `var(--md-sys-color-surface-container-low)` with level 1 shadow.
  * **Outlined Card**: Surface `var(--md-sys-color-surface)`, Border `var(--md-sys-color-outline-variant)`.
* **Form Controls**:
  * **Filled Text Field**: Container `var(--md-sys-color-surface-container-highest)`, Active line `var(--md-sys-color-primary)`, Text `var(--md-sys-color-on-surface)`, Label `var(--md-sys-color-on-surface-variant)`.
  * **Outlined Text Field**: Border `var(--md-sys-color-outline)` (active `var(--md-sys-color-primary)`), Label `var(--md-sys-color-on-surface-variant)`.
  * **Switch**: Active track `var(--md-sys-color-primary)`, Inactive track `var(--md-sys-color-surface-container-highest)`.
* **Navigation Components**:
  * **Top App Bar**: Background `var(--md-sys-color-surface)` or `var(--md-sys-color-surface-container-high)`.
  * **Navigation Bar**: Container `var(--md-sys-color-surface-container)`, Active indicator `var(--md-sys-color-secondary-container)`, Active icon `var(--md-sys-color-on-secondary-container)`.
  * **Navigation Drawer**: Container `var(--md-sys-color-surface-container-low)` or `var(--md-sys-color-surface)`.
* **Notification Banners & Snackbars**:
  * **Snackbar**: Background `var(--md-sys-color-inverse-surface)`, Text `var(--md-sys-color-inverse-on-surface)`, Action `var(--md-sys-color-inverse-primary)`.

### Deprecated Elevation Tint Overlays

Material 3 explicitly deprecates surface elevation tint overlays (opacity overlay fills at +1 to +5 levels). Web prototypes MUST NOT use opacity tint overlays to convey elevation. Use tone-based surface container tiers (`surface-container-lowest` to `surface-container-highest`) and CSS box shadows instead.
