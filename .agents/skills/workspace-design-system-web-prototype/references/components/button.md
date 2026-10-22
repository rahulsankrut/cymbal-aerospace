# Button (`<md-gb-button>`)

The Button (`<md-gb-button>`) represents interactive actions, form submit triggers, toggle controls, and links with filled, elevated, tonal, outlined, and text emphasis styles.

> **AI Suggestion Carve-Out**: For conversational AI follow-up prompts and suggested replies, use `<md-gb-suggestion>` inside `<md-gb-suggestion-group>` instead of buttons or chips.

## Import

```javascript
import '@material/web/labs/gb/components/button/md-gb-button.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `color` / `.color` | `'filled' \| 'elevated' \| 'tonal' \| 'outlined' \| 'text'` | `'text'` | Color emphasis variant. |
| `size` / `.size` | `'xs' \| 'sm' \| 'md' \| 'lg' \| 'xl'` | `'sm'` | Height scale variant (see Size Scale below). |
| `square` / `.square` | `boolean` | `false` | When true, renders with square corners instead of standard pill shape. |
| `type` / `.type` | `'submit' \| 'reset' \| 'button' \| 'toggle' \| 'link'` | `'submit'` | Behavior type. |
| `selected` / `.selected` | `boolean` | `false` | Selected toggle state when `type="toggle"`. |
| `href` / `.href` | `string` | `''` | Navigation target URL when `type="link"`. |
| `target` / `.target` | `'_blank' \| '_parent' \| '_self' \| '_top' \| ''` | `''` | Target browsing context when `type="link"`. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables the button and removes it from tab order. |
| `soft-disabled` / `.softDisabled` | `boolean` | `false` | Disables interaction while keeping the button focusable for accessibility. |

### Events

| Event Name | Type | Description |
| --- | --- | --- |
| `@change` | `Event` | Fired when a `type="toggle"` button toggles state. |

### Size Scale Matrix

| Size Variant | Height | Icon Size | Label Typescale | Usage Context |
| --- | --- | --- | --- | --- |
| `size="xs"` | `32px` | `20px` | `label-medium` | Compact inline, card, or header actions |
| `size="sm"` | `40px` | `24px` | `label-large` (Default) | Standard toolbars, forms, and secondary buttons |
| `size="md"` | `56px` | `24px` | `title-medium` | **Primary 56px CTAs**, mobile bottom action bars, FAB-like pills |
| `size="lg"` | `96px` | `32px` | `headline-small` | Extra-large expressive hero controls |
| `size="xl"` | `136px` | `40px` | `headline-large` | Giant kiosk or display controls |

> **CRITICAL SIZE WARNING**: `size="md"` produces a **56px height button**. Do NOT use `size="lg"` or `size="xl"` for 56px mobile action bars.

### Customizing Colors via CSS Tokens

To customize surface or label colors on `<md-gb-button>` (for example, customizing `color="elevated"`), override the semantic `--md-sys-color-*` token consumed by that variant directly on the host `style` attribute:

```html
<md-gb-button
  color="elevated"
  style="--md-sys-color-surface-container-low: var(--md-sys-color-surface-container-lowest); --md-sys-color-primary: var(--md-sys-color-error);">
  Custom Elevated
</md-gb-button>
```

### CSS Classes

```javascript
import buttonStylesheet from '@material/web/labs/gb/components/button/button.css' with {type: 'css'};
```

| Class | Type | Description |
| --- | --- | --- |
| `.btn` | Root | Root button class. |
| `.btn-filled` | Modifier | Filled color variant. |
| `.btn-elevated` | Modifier | Elevated color variant. |
| `.btn-tonal` | Modifier | Tonal color variant. |
| `.btn-outlined` | Modifier | Outlined color variant. |
| `.btn-text` | Modifier | Text color variant. |
| `.btn-xs`, `.btn-sm`, `.btn-md`, `.btn-lg`, `.btn-xl` | Modifiers | Size scale classes. |
| `.btn-square` | Modifier | Square corner shape. |
| `.btn-unselected`, `.btn-selected` | Modifiers | Toggle state modifier classes. |

## Usage Examples

### Color Variations

```html
<div class="flex flex-wrap gap-2">
  <md-gb-button color="filled">Filled</md-gb-button>
  <md-gb-button color="elevated">Elevated</md-gb-button>
  <md-gb-button color="tonal">Tonal</md-gb-button>
  <md-gb-button color="outlined">Outlined</md-gb-button>
  <md-gb-button color="text">Text</md-gb-button>
</div>
```

### Size Scale Matrix

```html
<div class="flex items-center gap-3">
  <md-gb-button color="filled" size="xs">Extra Small (32px)</md-gb-button>
  <md-gb-button color="filled" size="sm">Small (40px Default)</md-gb-button>
  <md-gb-button color="filled" size="md">Medium (56px Primary CTA)</md-gb-button>
</div>
```

### Toggle Buttons

```html
<md-gb-button color="tonal" type="toggle">Unselected Toggle</md-gb-button>
<md-gb-button color="tonal" type="toggle" selected>Selected Toggle</md-gb-button>
```

### Link Buttons

```html
<md-gb-button color="outlined" type="link" href="https://workspace.google.com" target="_blank">
  Open Workspace
</md-gb-button>
```
