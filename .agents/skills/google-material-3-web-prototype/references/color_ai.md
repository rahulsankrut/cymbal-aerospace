# Generative AI Color & Gradient Guidance

This reference defines the color ecosystem, baseline color values, dynamic generation rules, and gradient application patterns for Generative AI components in Google Material 3.

## AI Color System Overview

Generative AI features use distinct color palettes derived from the Gemini branding ecosystem. These colors signal AI capabilities (such as thinking, generating, summarizing, and prompt suggestions) while integrating smoothly with Material 3 token structures.

## Baseline AI Color Values

For products operating on a static baseline scheme or requiring standard Google AI styling, six dedicated AI color tokens are defined:

* `AI Main`: `#217BFE` (Core vibrant blue accent)
* `AI Analog`: `#078EFB` (Cyan-blue transition accent)
* `AI Complement`: `#AC87EB` (Soft purple accent)
* `AI Main Variant`: `#D7E6FF` (Light blue surface fill)
* `AI Analog Variant`: `#C7E4FF` (Light cyan surface fill)
* `AI Complement Variant`: `#DCE2FF` (Light lavender surface fill)

## Dynamic AI Color Roles

In dynamic color schemes (wallpaper or content-derived), AI components map to key dynamic palette tones rather than hardcoded hex values:

1. `Primary`: Main vibrant focal point.
2. `Primary T80`: Soft primary tone for gradient highlights.
3. `Tertiary T80`: Vibrant contrasting accent tone.
4. `Primary Container`: Container fill accent.
5. `Secondary Container`: Neutral container accent.
6. `Tertiary Container`: Expressive container fill.

## Gradient Application Rules

AI state indicators, shimmer fields, and container backgrounds MUST use animated or static multi-stop linear/conic gradients. Never use single flat colors for active AI states.

### Surface Fills (Behind Text)

When applying gradients behind text (e.g. prompt fields, AI response cards, suggestion chips), use lighter variant tones to guarantee a minimum 3:1 contrast ratio for body text:

* Fill Combination A: Gradient stop mix of `AI Main Variant` (`#D7E6FF`) -> `AI Analog Variant` (`#C7E4FF`) -> `AI Complement Variant` (`#DCE2FF`).
* Fill Combination B: Soft radial fade from `AI Main Variant` transitioning to `--md-sys-color-surface-container-low`.

### Outlines & Focus Rings

For high-emphasis boundaries, shimmer borders, and active focus rings, use rich chroma tones in a specific six-stop linear sequence:

1. `AI Main` (`#217BFE`)
2. `AI Analog` (`#078EFB`)
3. `AI Complement Variant` (`#DCE2FF`)
4. `Surface` (`var(--md-sys-color-surface)`)
5. `AI Analog` (`#078EFB`)
6. `AI Main` (`#217BFE`)

### CSS Gradient Implementation Example

```css
.md-ai-gradient-border {
  border: 2px solid transparent;
  background-image: linear-gradient(var(--md-sys-color-surface), var(--md-sys-color-surface)), 
                    linear-gradient(135deg, #217bfe, #078efb, #dce2ff, var(--md-sys-color-surface), #078efb, #217bfe);
  background-origin: border-box;
  background-clip: padding-box, border-box;
}

.md-ai-gradient-surface {
  background: linear-gradient(135deg, #d7e6ff 0%, #c7e4ff 50%, #dce2ff 100%);
  color: var(--md-sys-color-on-surface);
}
```

## AI Usage Best Practices

* Use moving gradients exclusively for active thinking, loading, or generating states.
* Once generation completes, transition AI output cards to standard Material surface tokens (`--md-sys-color-surface-container` or `--md-sys-color-tertiary-container`).
* Do NOT apply AI baseline colors to standard non-AI icons or buttons.
