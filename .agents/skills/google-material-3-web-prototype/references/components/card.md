# Card (`<md-gb-card>`)

The `<md-gb-card>` component provides a flexible container surface to group related content, media, headlines, supporting copy, and contextual actions.

## Import

```javascript
import '@material/web/labs/gb/components/card/md-gb-card.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `color` / `.color` | `'filled' \| 'elevated' \| 'outlined'` | `'outlined'` | Card surface variant. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables interactive states on the card. |
| `interactive` / `.interactive` | `boolean` | `false` | Enables hover/pressed ripple feedback across the whole card container. |

> **Nesting Guidance**: Bare `<md-gb-card>` defaults to `color="outlined"` (drawing a border line). Use `color="outlined"` ONLY for top-level cards on uniform surface backgrounds. For cards nested inside an already-bounded surface container, use `color="filled"` or `color="elevated"` so borders do not stack.

## Advanced Custom Fills, Radii, and Dashed Borders

When designs require custom container fills, radii, or dashed drop-zone borders, keep using `<md-gb-card>` instead of falling back to a plain `<div>`:

* **Custom Fill**: Slot a container `div` using `<div slot="container" class="bg-primary-container"></div>` or `style="background-color: var(--md-sys-color-primary-container)"`. Do NOT place `bg-*` directly on the `<md-gb-card>` host element.
* **Custom Corner Radius**: Override `--md-sys-shape-corner-md` directly on the `<md-gb-card>` host (e.g. `style="--md-sys-shape-corner-md: var(--md-sys-shape-corner-xl);"`).
* **Dashed Border**: Use `<md-gb-card color="filled">` and place the dashed border on the container `div` (e.g. `<div slot="container" class="border border-dashed border-outline-variant" style="border-radius: inherit"></div>`). Include `style="border-radius: inherit"` so corners follow the card shape.

## CSS Classes & Utility Styling

```javascript
import cardStylesheet from '@material/web/labs/gb/components/card/card.css' with {type: 'css'};
```

* `.card`: Root container element.
* `.card-filled`: Filled container modifier.
* `.card-elevated`: Elevated container modifier.
* `.card-outlined`: Outlined container modifier.
* `.card-btn`: Child action part.

## Usage Examples

### Standard Card Variants

```html
<md-gb-card color="outlined">
  <div class="p-s200">
    <h2 class="typescale-title-md">Outlined Card</h2>
    <p class="typescale-body-md text-on-surface-variant">Default top-level card with outline border.</p>
  </div>
</md-gb-card>

<md-gb-card color="filled">
  <div class="p-s200">
    <h2 class="typescale-title-md">Filled Card</h2>
    <p class="typescale-body-md text-on-surface-variant">Subtle surface container background fill.</p>
  </div>
</md-gb-card>

<md-gb-card color="elevated">
  <div class="p-s200">
    <h2 class="typescale-title-md">Elevated Card</h2>
    <p class="typescale-body-md text-on-surface-variant">Container with low elevation shadow.</p>
  </div>
</md-gb-card>
```

### Complex Action Card

```html
<md-gb-card color="elevated" style="max-width: 400px;">
  <div class="p-s300 flex flex-col gap-s200">
    <h2 class="typescale-headline-sm">Agent Overview</h2>
    <h3 class="typescale-title-sm text-on-surface-variant">Autonomous Task Dispatcher</h3>
    <p class="typescale-body-md text-on-surface-variant">
      Monitors incoming workflow requests and dispatches sub-tasks to specialized models in real time.
    </p>
    <div class="flex justify-end gap-s100 mt-s200">
      <md-gb-button color="outlined">Configure</md-gb-button>
      <md-gb-button color="filled">Launch Agent</md-gb-button>
    </div>
  </div>
</md-gb-card>
```

### Custom Fill and Corner Radius

```html
<md-gb-card color="filled" style="--md-sys-shape-corner-md: var(--md-sys-shape-corner-xl);">
  <div slot="container" class="bg-primary-container"></div>
  <div class="p-s300 text-on-primary-container">
    <h3 class="typescale-title-md">AI Insights Available</h3>
    <p class="typescale-body-md">Your weekly prompt activity summary is ready to review.</p>
  </div>
</md-gb-card>
```

### Dashed Drop-Zone Border Card

```html
<md-gb-card color="filled">
  <div slot="container" class="border border-dashed border-outline-variant" style="border-radius: inherit"></div>
  <div class="flex flex-col items-center gap-s200 p-s300 text-center">
    <md-gb-icon style="--md-icon-size: 32px;" class="text-on-surface-variant">upload_file</md-gb-icon>
    <p class="typescale-body-md text-on-surface-variant">Drag and drop document files here</p>
    <md-gb-button color="tonal">Browse Files</md-gb-button>
  </div>
</md-gb-card>
```
