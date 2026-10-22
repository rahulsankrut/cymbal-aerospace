# Google Sans Flex \& Editorial Typography Reference

This reference covers advanced variable font configurations using Google Sans Flex (GSF), variable font axis parameters, recommended axis combinations for editorial treatments, and performance guidelines.

## Google Sans Flex (GSF) Variable Font Axes

Google Sans Flex is a multi-axis variable font designed specifically for Google Material 3 experiences. It expands upon standard static font weights by allowing precise numerical tuning across 6 distinct axes:

1. **Roundness (`ROND`)**:
   
   * *Range*: `0` to `100`
   * *Purpose*: Controls the curvature and rounding of stroke terminals.
   * *Usage*: Applied in Material 3 **Emphasized** type styles (`ROND: 100`). Adds warmth, optimism, and alignment with rounded Material component shapes.

2. **Weight (`wght`)**:
   
   * *Range*: `1` to `1000`
   * *Purpose*: Defines stroke thickness from ultra-thin (`1`) to extra-bold (`1000`).
   * *Usage*: Baseline styles use `400` (regular) or `500` (medium). Emphasized styles increase weight to `500` or `600`.

3. **Width (`wdth`)**:
   
   * *Range*: `25` to `151` (default `100`)
   * *Purpose*: Adjusts horizontal character proportions.
   * *Usage*: Used functional for long localized text strings to prevent truncation, or in compact UI layouts. Do not compress width by more than 15 points below `100` to maintain legibility.

4. **Grade (`GRAD`)**:
   
   * *Range*: `0` to `100`
   * *Purpose*: Subtly increases visual density/weight without expanding character bounding boxes or altering line length.
   * *Usage*: Ideal for hover, focus, and active interactive states where changing `wght` would cause text container size shifts or layout jitter.

5. **Optical Size (`opsz`)**:
   
   * *Range*: `6` to `144` (in sp/pt units)
   * *Purpose*: Automatically adjusts letterform parameters (stroke contrast, counter space, spacing) based on rendering size.
   * *Usage*: At small optical sizes (6–18), characters have thicker strokes and open counters for maximum readability. At large optical sizes (36+), strokes become refined and expressive.

6. **Slant (`slnt`)**:
   
   * *Range*: `0` to `-12` (degrees)
   * *Purpose*: Adjusts italic angle from upright (`0`) to oblique (`-12`).

## Recommended Editorial Axis Combinations

Editorial treatments are standalone, content-focused moments (such as article hero titles, photo album covers, or personalized user voice highlights) where custom axis combinations are used for visual expression.

### 1. Stylistically Consistent with Baseline \& Emphasized

* **Clean Modern Title**: `'ROND' 0, 'wght' 400, 'wdth' 100, 'GRAD' 0`
* **Friendly Rounded Headline**: `'ROND' 100, 'wght' 500, 'wdth' 100, 'GRAD' 0`

### 2. Celebrating Content \& Hero Moments

* **Bold Expressive Display**: `'ROND' 100, 'wght' 700, 'wdth' 105, 'GRAD' 0`
* **Elegantly Refined Title**: `'ROND' 0, 'wght' 300, 'wdth' 100, 'GRAD' 0, 'slnt' -6`
* **Blocky High-Impact Header**: `'ROND' 0, 'wght' 800, 'wdth' 115, 'GRAD' 50`

### 3. Personalization \& User Voice

* **Playful Warmth**: `'ROND' 100, 'wght' 600, 'wdth' 110`
* **Focused Precision**: `'ROND' 0, 'wght' 500, 'wdth' 90`

## CSS Implementation of Custom Axes

Apply custom GSF axes using the CSS `font-variation-settings` property alongside `font`:

```css
.editorial-hero-header {
  font: var(--md-sys-typescale-display-large);
  font-variation-settings: 'ROND' 100, 'wght' 700, 'wdth' 105, 'GRAD' 0;
  color: var(--md-sys-color-primary);
  max-width: 20ch;
}
```

## Performance \& Axis Animation Rules

* **Animate Axes with Caution**: While CSS transition on `font-variation-settings` is supported in modern browsers, continuous web font axis recalculation can cause frame drops on low-power devices.
* **Avoid Animating `opsz` or `wdth` in Real-Time**: Limit animations to opacity, transform, or subtle `GRAD` transitions.
