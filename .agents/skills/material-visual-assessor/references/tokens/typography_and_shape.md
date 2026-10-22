# Material Design 3 Typography Scale & Shape Corner System

Authoritative Material Design 3 (M3) typographic scale, font family rules,
corner radius tokens, interactive shape morphing rules, and nested concentric
corner geometry.

--------------------------------------------------------------------------------

## 1. Typography Scale & Font Families

Material 3 uses **Google Sans** for expressive, large-scale hierarchy
(`Display`, `Headline`, `Title Large`) and **Google Sans Text** for
high-legibility UI reading and controls (`Title Medium/Small`, `Body`, `Label`).
**Google Sans Flex (GSF)** is the preferred variable font supporting continuous
optical size and weight axes.

*   **Sentence Case & Font Family Exclusion Gate (`typography_sentence_case`)**:
    Exclude user-generated content, rasterized third-party promotional banners
    or media artwork, app icons, and regulatory/age-rating stamps (`"EVERYONE
    10+"`, `"ESRB"`) from **both** Sentence Case and `Google Sans` font family
    checks. When all native UI chrome uses `Google Sans` / `Google Sans Text`,
    conclude **`Answer: Yes`**; when native UI text uses a custom corporate or
    non-Google typeface, conclude **`Answer: No`**.

### Canonical Typescale Tokens

*   **`sys.typescale.display-large`** (`--md-sys-typescale-display-large`):
    Google Sans | Size `57pt / 57px` (`3.6rem`) | Line Height `64pt / 64px`
    (`4.0rem`) | Weight Regular (`400`).
*   **`sys.typescale.display-medium`** (`--md-sys-typescale-display-medium`):
    Google Sans | Size `45pt / 45px` (`2.8rem`) | Line Height `52pt / 52px`
    (`3.3rem`) | Weight Regular (`400`).
*   **`sys.typescale.display-small`** (`--md-sys-typescale-display-small`):
    Google Sans | Size `36pt / 36px` (`2.3rem`) | Line Height `44pt / 44px`
    (`2.8rem`) | Weight Regular (`400`).
*   **`sys.typescale.headline-large`** (`--md-sys-typescale-headline-large`):
    Google Sans | Size `32pt / 32px` (`2.0rem`) | Line Height `40pt / 40px`
    (`2.5rem`) | Weight Regular (`400`).
*   **`sys.typescale.headline-medium`** (`--md-sys-typescale-headline-medium`):
    Google Sans | Size `28pt / 28px` (`1.8rem`) | Line Height `36pt / 36px`
    (`2.3rem`) | Weight Regular (`400`).
*   **`sys.typescale.headline-small`** (`--md-sys-typescale-headline-small`):
    Google Sans | Size `24pt / 24px` (`1.5rem`) | Line Height `32pt / 32px`
    (`2.0rem`) | Weight Regular (`400`).
*   **`sys.typescale.title-large`** (`--md-sys-typescale-title-large`): Google
    Sans | Size `22pt / 22px` (`1.4rem`) | Line Height `28pt / 28px` (`1.8rem`)
    | Weight Regular (`400`).
*   **`sys.typescale.title-medium`** (`--md-sys-typescale-title-medium`): Google
    Sans Text | Size `16pt / 16px` (`1.0rem`) | Line Height `24pt / 24px`
    (`1.5rem`) | Weight Medium (`500`).
*   **`sys.typescale.title-small`** (`--md-sys-typescale-title-small`): Google
    Sans Text | Size `14pt / 14px` (`0.9rem`) | Line Height `20pt / 20px`
    (`1.3rem`) | Weight Medium (`500`).
*   **`sys.typescale.body-large`** (`--md-sys-typescale-body-large`): Google
    Sans Text | Size `16pt / 16px` (`1.0rem`) | Line Height `24pt / 24px`
    (`1.5rem`) | Weight Regular (`400`).
*   **`sys.typescale.body-medium`** (`--md-sys-typescale-body-medium`): Google
    Sans Text | Size `14pt / 14px` (`0.9rem`) | Line Height `20pt / 20px`
    (`1.3rem`) | Weight Regular (`400`).
*   **`sys.typescale.body-small`** (`--md-sys-typescale-body-small`): Google
    Sans Text | Size `12pt / 12px` (`0.8rem`) | Line Height `16pt / 16px`
    (`1.0rem`) | Weight Regular (`400`).
*   **`sys.typescale.label-large`** (`--md-sys-typescale-label-large`): Google
    Sans Text | Size `14pt / 14px` (`0.9rem`) | Line Height `20pt / 20px`
    (`1.3rem`) | Weight Medium (`500`).
*   **`sys.typescale.label-medium`** (`--md-sys-typescale-label-medium`): Google
    Sans Text | Size `12pt / 12px` (`0.8rem`) | Line Height `16pt / 16px`
    (`1.0rem`) | Weight Medium (`500`).
*   **`sys.typescale.label-small`** (`--md-sys-typescale-label-small`): Google
    Sans Text | Size `11pt / 11px` (`0.7rem`) | Line Height `16pt / 16px`
    (`1.0rem`) | Weight Medium (`500`).
*   **Emphasized Variants**: M3 Expressive emphasized tokens (e.g.,
    `--md-sys-typescale-emphasized-body-large`,
    `--md-sys-typescale-emphasized-label-large`) elevate font weight to Medium
    (`500`) or Bold (`700`) to signal active selection, unread items, or focal
    hierarchy.

--------------------------------------------------------------------------------

## 2. Shape Scale & Corner Radius Tokens

All Material 3 containers map to a 9-step corner radius scale:

*   **`sys.shape.corner.none`** (`--md-sys-shape-corner-none`): `0px`.
    Full-screen dialogs, edge-to-edge square banners, bottom sheet base edges.
*   **`sys.shape.corner.extra-small`** (`--md-sys-shape-corner-extra-small`):
    `4px` (`2px` checkbox). Outlined text fields (`4px`), checkboxes (`2px`),
    primary tab indicators, AI prompt chip top-right corner.
*   **`sys.shape.corner.small`** (`--md-sys-shape-corner-small`): `8px`.
    Assist/Filter/Input/Suggestion chips, large badges, pressed square buttons.
*   **`sys.shape.corner.medium`** (`--md-sys-shape-corner-medium`): `12px`.
    Standard cards (Elevated, Filled, Outlined), menus, square button options.
*   **`sys.shape.corner.large`** (`--md-sys-shape-corner-large`): `16px`. Modal
    side sheets, navigation drawers, large cards.
*   **`sys.shape.corner.large-increased`**
    (`--md-sys-shape-corner-large-increased`): `20px`. Expressive medium card
    variants and expanded action containers.
*   **`sys.shape.corner.extra-large`** (`--md-sys-shape-corner-extra-large`):
    `28px`. Bottom sheets (top corners), basic dialogs, standard FABs (`56dp`),
    Extended FABs, carousels, round banners.
*   **`sys.shape.corner.extra-large-increased`**
    (`--md-sys-shape-corner-extra-large-increased`): `32px`. Medium (`80dp`) and
    Large (`96dp`) FABs, extra-large expressive buttons.
*   **`sys.shape.corner.full`** (`--md-sys-shape-corner-full`): `9999px` /
    `max(50cqw, 50cqh)`. Pill geometry: common buttons, icon buttons, floating
    toolbars, switches, slider handles, search bars.

--------------------------------------------------------------------------------

## 3. Shape Morphing & Concentric Nested Geometry

*   **Interactive Shape Morphing**: In M3 Expressive button groups and
    interactive controls, pressing or selecting an element dynamically morphs
    corner radius (e.g., square buttons at `--md-sys-shape-corner-medium`
    (`12px`) morph to `--md-sys-shape-corner-small` (`8px`) on press; standard
    button groups pair `full` pill unselected peers with `medium` `12px`
    selected buttons).
*   **Concentric Nested Corner Formula**: When a rounded child element sits
    inside a padded parent container, their radii must be concentric to avoid
    visual pinching: `R_outer = R_inner + Padding`. For example, a child card
    with `12px` radius inside a container with `16px` padding requires an outer
    container radius of `28px` (`--md-sys-shape-corner-extra-large`).
