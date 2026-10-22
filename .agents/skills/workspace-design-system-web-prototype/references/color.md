# Color Reference

This document provides a comprehensive guide to color usage, token naming, pairing rules, GenAI gradients, Gemini gems surfaces, and extended color palettes in the Workspace Design System (`workspace-design-system`).

## Design System Color Architecture

Color in Workspace Design System is organized into distinct semantic layers and functional roles:

- **Core System Colors**: Base UI roles (`primary`, `secondary`, `tertiary`) that define container fills, action buttons, borders, and main body text.
- **GenAI & Gemini Gems Palette**: AI-native surfaces, response indicators, prompt highlights, and gradient accents for intelligence features.
- **Extended Color Palette**: Nine hue families (blue, cyan, green, grey, orange, pink, purple, red, yellow) providing specialized feedback, category tags, and status states across solid fills, outlines, and tonal containers.
- **Premium Surface Palette**: Subtle blue gradient surface tones and typography accents for elevated surfaces.
- **Illustration Palette**: Brand-aligned vector colors, characters, skin tones, and thematic scene artwork.

All color tokens utilize the modern CSS `light-dark(#lightValue, #darkValue)` function declared under `:root, :host`. This enables automatic adaptive theme switching between light and dark modes based on system preferences without requiring duplicate CSS overrides.

## Key Color Roles and Pairing Rules

To ensure accessible contrast and visual consistency, surface tokens MUST be paired strictly with their corresponding `on-*` color tokens. Never pair text or icon colors with mismatched surface backgrounds.

### Core Color Roles & Token Reference

| Role / Intent | Surface / Accent Token | Content / On Token | Light Value | Dark Value |
| --- | --- | --- | --- | --- |
| Primary Actions & Key Buttons | `--ws-sys-color-primary` | `--ws-sys-color-on-primary` | `#0b57d0` / `#ffffff` | `#a8c7fa` / `#062e6f` |
| Primary Container Surfaces | `--ws-sys-color-primary-container` | `--ws-sys-color-on-primary-container` | `#d3e3fd` / `#041e49` | `#0842a0` / `#d3e3fd` |
| Secondary Accent Actions | `--ws-sys-color-secondary` | `--ws-sys-color-on-secondary` | `#00639b` / `#ffffff` | `#7fcfff` / `#003355` |
| Secondary Container / Tonal | `--ws-sys-color-secondary-container` | `--ws-sys-color-on-secondary-container` | `#c2e7ff` / `#001d35` | `#004a77` / `#c2e7ff` |
| Tertiary / Field Accents | `--ws-sys-color-tertiary` | `--ws-sys-color-on-tertiary` | `#146c2e` / `#ffffff` | `#6dd58c` / `#0a3818` |
| Tertiary Container Surfaces | `--ws-sys-color-tertiary-container` | `--ws-sys-color-on-tertiary-container` | `#c4eed0` / `#072711` | `#0f5223` / `#c4eed0` |
| Primary Body & Title Text | `--ws-sys-color-primary-text` | N/A | `#1f1f1f` | `#e3e3e3` |
| Secondary Subtitle Text | `--ws-sys-color-secondary-text` | N/A | `#ffffff` | `#003355` |
| Selected Item Containers | `--ws-sys-color-selected-container` | `--ws-sys-color-on-selected-container` | `#d3e3fd` / `#041e49` | `#0842a0` / `#d3e3fd` |
| Selected Container Variant | `--ws-sys-color-selected-container-variant` | N/A | `#0b57d0` | `#a8c7fa` |
| Inverse Primary Accents | `--ws-sys-color-inverse-primary` | N/A | `#a8c7fa` | `#0b57d0` |
| Structural Component Borders | `--ws-sys-color-outline` | N/A | `#747775` | `#8e918f` |
| Section Dividers & Rules | `--ws-sys-color-divider` | N/A | `#c4c7c5` | `#c4c7c5` |

### Pairing Guidelines

- **Primary Pairing**: Use `var(--ws-sys-color-primary)` for filled buttons, active chips, or focal icons, with text formatted in `var(--ws-sys-color-on-primary)`.
- **Container Surfaces**: Use `var(--ws-sys-color-primary-container)` or `var(--ws-sys-color-secondary-container)` for cards, drawers, side sheets, or hero banners, pairing internal text with `var(--ws-sys-color-on-primary-container)` or `var(--ws-sys-color-on-secondary-container)`.
- **Selected States**: Navigation items, selected list rows, and active tabs must apply `var(--ws-sys-color-selected-container)` with text in `var(--ws-sys-color-on-selected-container)`.
- **Borders & Dividers**: Use `var(--ws-sys-color-outline)` for interactive boundaries (text fields, cards, outlined buttons) and `var(--ws-sys-color-divider)` for horizontal or vertical content separators.

## GenAI Aurora Gradients and Gemini Gems Palette

Workspace Design System provides specialized tokens for AI user interfaces, smart features, prompt suggestion chips, and assistant surfaces.

### Aurora Gradients

Aurora gradients represent active AI processing, generation states, and spark animations.

- **Bold Aurora Gradient**: `linear-gradient(135deg, var(--ws-sys-color-genai-bold-gradient01), var(--ws-sys-color-genai-bold-gradient02), var(--ws-sys-color-genai-bold-gradient03))`
- **Muted Aurora Gradient**: `linear-gradient(135deg, var(--ws-sys-color-genai-muted-gradient01), var(--ws-sys-color-genai-muted-gradient02), var(--ws-sys-color-genai-muted-gradient03))`
- **Text Aurora Gradient**: Gradient stops using `--ws-sys-color-genai-text-gradient01` (`#3186ff`), `--ws-sys-color-genai-text-gradient02` (`#346bf1`), and `--ws-sys-color-genai-text-gradient03` (`#4fa0ff`).

### Gemini Gems Surface Palette

Gemini Gems are color-coded thematic containers for categorized AI prompts, assistants, and custom agents.

| Gem Theme | Surface Token | Text / Icon Token | Light Surface / Text | Dark Surface / Text |
| --- | --- | --- | --- | --- |
| Blue Gem | `--ws-sys-color-genai-gems-blue` | `--ws-sys-color-genai-on-gems-blue` | `#bedcff` / `#00629e` | `#003d64` / `#60a9ed` |
| Cyan Gem | `--ws-sys-color-genai-gems-cyan` | `--ws-sys-color-genai-on-gems-cyan` | `#92e5ff` / `#00677d` | `#00404e` / `#25b2d4` |
| Grey Gem | `--ws-sys-color-genai-gems-grey` | `--ws-sys-color-genai-on-gems-grey` | `#d9d9d9` / `#5e5e5e` | `#3a3a3a` / `#a4a4a4` |
| Orange Gem | `--ws-sys-color-genai-gems-orange` | `--ws-sys-color-genai-on-gems-orange` | `#ffcfb4` / `#96490a` | `#612b00` / `#ec8c4c` |
| Pink Gem | `--ws-sys-color-genai-gems-pink` | `--ws-sys-color-genai-on-gems-pink` | `#ffcbda` / `#984062` | `#60263d` / `#db8da7` |
| Purple Gem | `--ws-sys-color-genai-gems-purple` | `--ws-sys-color-genai-on-gems-purple` | `#f2ccff` / `#9700d2` | `#55226e` / `#c88ee1` |
| Teal Gem | `--ws-sys-color-genai-gems-teal` | `--ws-sys-color-genai-on-gems-teal` | `#93e7eb` / `#00696d` | `#004144` / `#00b6bc` |
| Violet Gem | `--ws-sys-color-genai-gems-violet` | `--ws-sys-color-genai-on-gems-violet` | `#d9d4ff` / `#5132ff` | `#372d80` / `#a299f3` |
| Yellow Gem | `--ws-sys-color-genai-gems-yellow` | `--ws-sys-color-genai-on-gems-yellow` | `#ffd289` / `#7e5700` | `#4f3500` / `#d89800` |

## Extended Color Palette Reference

The extended palette provides functional colors organized across nine hue families. Each hue offers three operational variations:

- **Fill (`*-fill`)**: High-emphasis solid fills paired with `*-on-*-fill`.
- **Outline (`*-outline`)**: Stroke borders and low-contrast borders paired with `*-on-*-outline`.
- **Tonal (`*-tonal`)**: Soft container backgrounds paired with `*-on-*-tonal`.

### Extended Palette Tokens Table

| Hue Family | Variant | Token Name | Matching Content Token | Light Value | Dark Value |
| --- | --- | --- | --- | --- | --- |
| Blue | Fill | `--ws-sys-color-extended-blue-fill` | `--ws-sys-color-extended-on-blue-fill` | `#1157ce` | `#a1c9ff` |
| Blue | Outline | `--ws-sys-color-extended-blue-outline` | `--ws-sys-color-extended-on-blue-outline` | `#d0e4ff` | `#04409f` |
| Blue | Tonal | `--ws-sys-color-extended-blue-tonal` | `--ws-sys-color-extended-on-blue-tonal` | `#d0e4ff` | `#04409f` |
| Cyan | Fill | `--ws-sys-color-extended-cyan-fill` | `--ws-sys-color-extended-on-cyan-fill` | `#00687c` | `#acedff` |
| Cyan | Outline | `--ws-sys-color-extended-cyan-outline` | `--ws-sys-color-extended-on-cyan-outline` | `#acedff` | `#004e5d` |
| Cyan | Tonal | `--ws-sys-color-extended-cyan-tonal` | `--ws-sys-color-extended-on-cyan-tonal` | `#d8f6ff` | `#004e5d` |
| Green | Fill | `--ws-sys-color-extended-green-fill` | `--ws-sys-color-extended-on-green-fill` | `#006c35` | `#80da88` |
| Green | Outline | `--ws-sys-color-extended-green-outline` | `--ws-sys-color-extended-on-green-outline` | `#beefbb` | `#00522c` |
| Green | Tonal | `--ws-sys-color-extended-green-tonal` | `--ws-sys-color-extended-on-green-tonal` | `#beefbb` | `#00522c` |
| Grey | Fill | `--ws-sys-color-extended-grey-fill` | `--ws-sys-color-extended-on-grey-fill` | `#5e5e5e` | `#c7c7c7` |
| Grey | Outline | `--ws-sys-color-extended-grey-outline` | `--ws-sys-color-extended-on-grey-outline` | `#e3e3e3` | `#474747` |
| Grey | Tonal | `--ws-sys-color-extended-grey-tonal` | `--ws-sys-color-extended-on-grey-tonal` | `#e3e3e3` | `#474747` |
| Orange | Fill | `--ws-sys-color-extended-orange-fill` | `--ws-sys-color-extended-on-orange-fill` | `#ff8d41` | `#ffb683` |
| Orange | Outline | `--ws-sys-color-extended-orange-outline` | `--ws-sys-color-extended-on-orange-outline` | `#ffdcc3` | `#753403` |
| Orange | Tonal | `--ws-sys-color-extended-orange-tonal` | `--ws-sys-color-extended-on-orange-tonal` | `#ffdcc3` | `#753403` |
| Pink | Fill | `--ws-sys-color-extended-pink-fill` | `--ws-sys-color-extended-on-pink-fill` | `#b60d6e` | `#ffaee4` |
| Pink | Outline | `--ws-sys-color-extended-pink-outline` | `--ws-sys-color-extended-on-pink-outline` | `#ffd8ef` | `#8d0053` |
| Pink | Tonal | `--ws-sys-color-extended-pink-tonal` | `--ws-sys-color-extended-on-pink-tonal` | `#ffd8ef` | `#8d0053` |
| Purple | Fill | `--ws-sys-color-extended-purple-fill` | `--ws-sys-color-extended-on-purple-fill` | `#7438d2` | `#d9bafd` |
| Purple | Outline | `--ws-sys-color-extended-purple-outline` | `--ws-sys-color-extended-on-purple-outline` | `#eedcfe` | `#5629a4` |
| Purple | Tonal | `--ws-sys-color-extended-purple-tonal` | `--ws-sys-color-extended-on-purple-tonal` | `#eedcfe` | `#5629a4` |
| Red (Error) | Fill | `--ws-sys-color-extended-red-fill` | `--ws-sys-color-extended-on-red-fill` | `#b3251e` | `#ffb3ae` |
| Red (Error) | Outline | `--ws-sys-color-extended-red-outline` | `--ws-sys-color-extended-on-red-outline` | `#ffdadc` | `#8a1a16` |
| Red (Error) | Tonal | `--ws-sys-color-extended-red-tonal` | `--ws-sys-color-extended-on-red-tonal` | `#ffdadc` | `#8a1a16` |
| Yellow | Fill | `--ws-sys-color-extended-yellow-fill` | `--ws-sys-color-extended-on-yellow-fill` | `#fcbd00` | `#ffe07c` |
| Yellow | Outline | `--ws-sys-color-extended-yellow-outline` | `--ws-sys-color-extended-on-yellow-outline` | `#ffe07c` | `#8f4e06` |
| Yellow | Tonal | `--ws-sys-color-extended-yellow-tonal` | `--ws-sys-color-extended-on-yellow-tonal` | `#fff2b4` | `#8f4e06` |

## Premium Surface Tokens

For elevated header surfaces, premium product banners, or special feature highlights:

- Surface Accent 01: `--ws-sys-color-premium-surface-accent01` (`light-dark(#a8dbff, #0f6bcb)`)
- Surface Accent 02: `--ws-sys-color-premium-surface-accent02` (`light-dark(#89b8ff, #5f90f8)`)
- Container Accent 01: `--ws-sys-color-premium-surface-container-accent01` (`light-dark(#8cd1ff, #196fcf)`)
- Container Accent 02: `--ws-sys-color-premium-surface-container-accent02` (`light-dark(#7aadf7, #5f90f8)`)
- Premium Text Gradient Stops: `--ws-sys-color-premium-text-gradient01` (`light-dark(#1f1f1f, #e3e3e3)`) and `--ws-sys-color-premium-text-gradient02` (`light-dark(#6286ff, #86a4ff)`)

## Dark Mode and Dynamic Adaptation

The Workspace Design System handles light and dark mode dynamically:

- **Automatic Theme Resolution**: Tokens use native CSS `light-dark()` functions inside `:root, :host`. When the browser or system prefers dark mode (`prefers-color-scheme: dark`), values switch automatically without manual class toggles.
- **Explicit Theme Forcing**: To force dark mode on a container, apply `color-scheme: dark` in standard CSS.
- **gBreeze Internal Mapping**: Standard Lit gBreeze components automatically receive color variables bound to `--md-sys-color-*`. Custom HTML layout containers should use `var(--ws-sys-color-*)` tokens directly.

## Illustration Colors Guidance

**Pull [IllustrationColors](illustration-colors.md)** when rendering vector illustrations, brand artwork, avatar graphics, skin tones, or thematic spot graphics.
