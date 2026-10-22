# Card (`<md-gb-card>`)

The Card (`<md-gb-card>`) provides flexible container surfaces to visually group related content, information displays, and actionable controls.

## Import

```javascript
import '@material/web/labs/gb/components/card/md-gb-card.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `color` / `.color` | `'filled' \| 'elevated' \| 'outlined'` | `'outlined'` | Card surface variant. |
| `disabled` / `.disabled` | `boolean` | `false` | Whether the card is disabled. |
| `interactive` / `.interactive` | `boolean` | `false` | Enables interactive hover, focus ring, and ripple state layers. |

> **IMPORTANT NESTING RULE**: `color` defaults to `'outlined'`, so a bare `<md-gb-card>` draws a stroke boundary. Use `'outlined'` only for top-level cards on uniform backgrounds. For cards nested inside an already-bounded container or drawer, use `color="filled"` or `color="elevated"` so outline strokes do not stack.

### Slots

| Slot Name | Description |
| --- | --- |
| `(default)` | Card body content, headers, text, and action rows. |
| `slot="container"` | Custom background container layer for custom fill colors or dashed border overlays. |

### Custom Styling Rules (Fill, Corner Radii, and Dashed Borders)

When a design calls for custom fills, unique corner roundedness, or dashed dropzones, keep using `<md-gb-card>` instead of raw HTML `<div>` elements:

- **Custom Fill**: Slot a `<div slot="container" class="bg-primary-container"></div>` inside the card. Do NOT place `bg-*` classes directly on the `<md-gb-card>` host element or default slot wrapper.
- **Custom Corner Radius**: Override `--md-sys-shape-corner-md` on the host element `style` attribute (e.g., `style="--md-sys-shape-corner-md: var(--md-sys-shape-corner-xl);"`). Do NOT place `rounded-*` classes directly on `<md-gb-card>`.
- **Dashed Border Dropzone**: Use `<md-gb-card color="filled">` with `<div slot="container" class="border border-dashed border-outline-variant" style="border-radius: inherit"></div>`. `color="filled"` prevents solid outline stacking. Keep content, padding, and buttons inside the default slot, NOT on the container `div`.

### CSS Classes

```javascript
import cardStylesheet from '@material/web/labs/gb/components/card/card.css' with {type: 'css'};
```

| Class | Type | Description |
| --- | --- | --- |
| `.card` | Root | Root card class. |
| `.card-filled` | Modifier | Filled surface color. |
| `.card-elevated` | Modifier | Elevated shadow surface. |
| `.card-outlined` | Modifier | Outlined border surface. |
| `.card-btn` | Part | Inner interactive button part. |

## Usage Examples

### Surface Color Variants

```html
<!-- Outlined (Default for top-level surfaces) -->
<md-gb-card color="outlined">
  <div class="p-4">Outlined Card Content</div>
</md-gb-card>

<!-- Elevated -->
<md-gb-card color="elevated">
  <div class="p-4">Elevated Card Content</div>
</md-gb-card>

<!-- Filled (Ideal for nested cards) -->
<md-gb-card color="filled">
  <div class="p-4">Filled Card Content</div>
</md-gb-card>
```

### Full Card Layout with Actions

```html
<md-gb-card color="elevated">
  <div class="p-6 space-y-4">
    <h2 class="typescale-headline-small text-on-surface">Agent Status Report</h2>
    <p class="typescale-body-medium text-on-surface-variant max-w-[65ch]">
      Detailed performance metrics for active autonomous execution threads.
    </p>
    <div class="flex gap-3 justify-end pt-2">
      <md-gb-button color="outlined">Dismiss</md-gb-button>
      <md-gb-button color="filled">View Metrics</md-gb-button>
    </div>
  </div>
</md-gb-card>
```

### Custom Fill and Custom Corner Radius

```html
<md-gb-card
  color="filled"
  style="--md-sys-shape-corner-md: var(--md-sys-shape-corner-xl);">
  <div slot="container" class="bg-primary-container"></div>
  <div class="p-6 text-on-primary-container">
    <h3 class="typescale-title-medium">Custom Primary Container Card</h3>
  </div>
</md-gb-card>
```

### Dashed File Upload Dropzone Card

```html
<md-gb-card color="filled">
  <div slot="container" class="border border-dashed border-outline-variant" style="border-radius: inherit"></div>
  <div class="flex flex-col items-center gap-4 p-8 text-center">
    <md-gb-icon class="text-on-surface-variant" style="--md-icon-size: 32px">cloud_upload</md-gb-icon>
    <p class="typescale-body-medium text-on-surface-variant">Drag and drop files here to upload</p>
    <md-gb-button color="tonal">Browse Files</md-gb-button>
  </div>
</md-gb-card>
```
