# Advanced Color Customizations

This reference provides detailed guidance on creating custom baseline color schemes, defining static and custom color roles, applying color fidelity, harmonizing colors, and harmonizing bitmap/vector images.

## Defining a Custom Baseline Scheme

When building a branded web prototype where colors should not change dynamically with user wallpaper, product creators define a custom static baseline scheme.

### Workflow

1. Select reference hex colors for Primary, Secondary, Tertiary, Neutral, and Neutral Variant palettes.
2. Input reference colors into the Material Theme Builder algorithm (Material Color Utilities).
3. The algorithm derives five key colors and corresponding 13-tone palettes (Tones 0 through 100).
4. Tonal tones are mapped to the standard semantic `--md-sys-color-*` tokens for both Light and Dark themes.

### Key Rules for Baseline Schemes

* Primary and Tertiary roles drive visual branding and accent emphasis.
* Secondary, Neutral, and Neutral Variant roles maintain lower chroma (saturation) to prevent visual noise.
* Custom baseline schemes must retain standard 3:1 (large text/UI elements) and 4.5:1 (body text) contrast ratios across all paired roles.

## Color Fidelity

Color fidelity is an algorithmic adjustment within Material Color Utilities that preserves the exact tone or lightness of an input brand color.

### Purpose

In standard dynamic color extraction, input colors may be darkened or shifted to fit strict contrast buckets. Color fidelity overrides standard bucket shifting when an exact brand hue/luminance match is required, adjusting adjacent paired tones to preserve contrast without altering the brand accent hue.

### Applying Color Fidelity in Web Prototypes

* Toggle color fidelity when generating CSS variables via Material Theme Builder.
* Always verify that the generated `on-*` color paired with a fidelity-adjusted container maintains a 3:1 minimum contrast ratio.

## Color Harmonization

Color harmonization adjusts the hue of static or semantic colors (such as custom badges or status indicators) to shift slightly toward the active Primary color theme.

### Purpose

When static brand or status colors sit alongside dynamic primary accents, unharmonized static colors can clash. Harmonization shifts the hue slightly warmer or cooler toward the primary accent while preserving the semantic meaning (e.g., maintaining distinguishable red for errors or green for success).

### Guidelines for Harmonization

* Harmonize custom semantic badge colors and secondary brand callouts.
* DO NOT harmonize strictly protected brand identity assets or logos where exact hex compliance is mandatory.

## Defining Custom Color Roles

If the standard 26+ Material color roles do not suffice for specialized domain UI (e.g., domain-specific status trackers or multi-tiered metrics), custom color roles can be added.

### Structure of a Custom Color Role

Each custom color role requires four paired tokens:

* `[role-name]`: Foreground or container fill color.
* `on-[role-name]`: High-contrast content color (text/icon) placed on `[role-name]`.
* `[role-name]-container`: Soft background container color.
* `on-[role-name]-container`: Content color placed on `[role-name]-container`.

## Image & Illustration Harmonization

Static vectors and bitmap illustrations within dynamically themed interfaces can feel disconnected if their color palette does not reflect the UI scheme.

### Vector Assets (SVG)

* Assign Material color tokens directly to SVG path fills and strokes (e.g., `fill="var(--md-sys-color-primary-container)"`).
* Use neutral surface tokens (`--md-sys-color-surface-container`) for background illustration elements and accent tokens (`--md-sys-color-primary`, `--md-sys-color-tertiary`) for key focal points.
* Do NOT apply dynamic color tokens to human skin tones or hair in illustrations; keep skin and hair tones static.

### Bitmap Assets (PNG / JPEG)

* Apply CSS overlay tinting or blend modes (e.g., `mix-blend-mode: color` with `--md-sys-color-surface-tint`) to subtly integrate photographic assets with the surrounding UI theme.
