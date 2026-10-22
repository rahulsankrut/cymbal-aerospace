# Icon Button (`<md-gb-icon-button>`)

The Icon Button (`<md-gb-icon-button>`) provides compact icon-only triggers for toolbar actions, toggle controls, navigation headers, and modal actions across filled, tonal, outlined, and standard variants.

## Import

```javascript
import '@material/web/labs/gb/components/iconbutton/md-gb-icon-button.js';
import '@material/web/labs/gb/styles/icon/md-gb-icon.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `color` / `.color` | `'filled' \| 'tonal' \| 'outlined' \| 'standard'` | `'standard'` | Color style variant. Note: `'elevated'` is **NOT** supported on `<md-gb-icon-button>`. |
| `size` / `.size` | `'xs' \| 'sm' \| 'md' \| 'lg' \| 'xl'` | `'sm'` | Size scale variant (see Size Scale Matrix below). |
| `square` / `.square` | `boolean` | `false` | When true, renders with square shape instead of circular. |
| `width` / `.width` | `'narrow' \| 'wide' \| ''` | `''` | Controls width proportion of the button container. |
| `type` / `.type` | `'submit' \| 'reset' \| 'button' \| 'toggle' \| 'link'` | `'submit'` | Behavior type. |
| `selected` / `.selected` | `boolean` | `false` | Toggle selection state when `type="toggle"`. |
| `href` / `.href` | `string` | `''` | Navigation target URL when `type="link"`. |
| `target` / `.target` | `'_blank' \| '_parent' \| '_self' \| '_top' \| ''` | `''` | Navigation browsing context when `type="link"`. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables button and removes from tab order. |
| `soft-disabled` / `.softDisabled` | `boolean` | `false` | Disables activation while keeping the button focusable. |

### Events

| Event Name | Type | Description |
| --- | --- | --- |
| `@change` | `Event` | Fired when a `type="toggle"` icon button changes selection state. |

### Size Scale Matrix

| Size Variant | Outer Height / Width | Icon Size | Usage Context |
| --- | --- | --- | --- |
| `size="xs"` | `32px` | `20px` | Compact inline card or table row action icons |
| `size="sm"` | `40px` | `24px` | Standard header, app bar, and toolbar actions (Default) |
| `size="md"` | `56px` | `24px` | **Large 56px mobile action bar** and FAB-like circular triggers |
| `size="lg"` | `96px` | `32px` | Hero display or touch kiosk triggers |
| `size="xl"` | `136px` | `40px` | Giant display controls |

> **IMPORTANT SIZE & COLOR WARNING**:
> - `size="md"` is the **56px height** variant. Always use `size="md"` for 56px action bar triggers.
> - `color="elevated"` is INVALID on `<md-gb-icon-button>`. To achieve an elevated crisp white icon button, use `color="tonal"` and override CSS variables on the host element: `style="--md-sys-color-secondary-container: var(--md-sys-color-surface-container-lowest); --md-sys-color-on-secondary-container: var(--md-sys-color-on-surface);"`.

### Icon Sizing Rules

ALWAYS size slotted `<md-gb-icon>` elements using `--md-icon-size` CSS variable, e.g.:
`<md-gb-icon style="--md-icon-size: 20px">search</md-gb-icon>`.
**CRITICAL**: Do NOT place `.typescale-*` classes on `<md-gb-icon>` as it overwrites `font-family: "Google Symbols"` with `"Google Sans Flex"` and breaks icon rendering.

### CSS Classes

```javascript
import iconButtonStylesheet from '@material/web/labs/gb/components/iconbutton/icon-button.css' with {type: 'css'};
```

| Class | Type | Description |
| --- | --- | --- |
| `.icon-btn` | Root | Root icon button class. |
| `.icon-btn-filled`, `.icon-btn-tonal`, `.icon-btn-outlined`, `.icon-btn-standard` | Modifiers | Color style variants. |
| `.icon-btn-xs`, `.icon-btn-sm`, `.icon-btn-md`, `.icon-btn-lg`, `.icon-btn-xl` | Modifiers | Size scale classes. |
| `.icon-btn-square`, `.icon-btn-narrow`, `.icon-btn-wide` | Modifiers | Shape and width modifiers. |
| `.icon-btn-unselected`, `.icon-btn-selected` | Modifiers | Toggle state modifier classes. |

## Usage Examples

### Standard Icon Button

```html
<md-gb-icon-button aria-label="More options">
  <md-gb-icon>more_vert</md-gb-icon>
</md-gb-icon-button>
```

### Color Style Variants

```html
<div class="flex gap-2">
  <md-gb-icon-button aria-label="Filled button" color="filled">
    <md-gb-icon>favorite</md-gb-icon>
  </md-gb-icon-button>
  <md-gb-icon-button aria-label="Tonal button" color="tonal">
    <md-gb-icon>favorite</md-gb-icon>
  </md-gb-icon-button>
  <md-gb-icon-button aria-label="Outlined button" color="outlined">
    <md-gb-icon>favorite</md-gb-icon>
  </md-gb-icon-button>
  <md-gb-icon-button aria-label="Standard button" color="standard">
    <md-gb-icon>favorite</md-gb-icon>
  </md-gb-icon-button>
</div>
```

### Toggle Icon Button

```html
<md-gb-icon-button aria-label="Bookmark" type="toggle" color="tonal">
  <md-gb-icon>bookmark_border</md-gb-icon>
</md-gb-icon-button>

<md-gb-icon-button aria-label="Bookmark" type="toggle" color="tonal" selected>
  <md-gb-icon>bookmark</md-gb-icon>
</md-gb-icon-button>
```
