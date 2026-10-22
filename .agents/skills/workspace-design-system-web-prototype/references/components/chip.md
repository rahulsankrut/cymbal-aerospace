# Chip (`<md-gb-chip>`)

The Chip (`<md-gb-chip>`) provides compact interactive pills used for filtering, selection, tags, quick actions, or input tokens.

> **AI Suggestion Carve-Out**: For conversational AI follow-up prompts and suggested replies, use `<md-gb-suggestion>` inside `<md-gb-suggestion-group>` instead of buttons or chips.

## Import

```javascript
import '@material/web/labs/gb/components/chip/md-gb-chip.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `color` / `.color` | `'outlined' \| 'elevated' \| 'filled' \| 'tonal'` | `'outlined'` | Chip surface color variant. |
| `type` / `.type` | `'action' \| 'filter' \| 'toggle' \| 'link'` | `'action'` | Chip functional behavior mode. |
| `selected` / `.selected` | `boolean` | `false` | Selected state when `type="filter"` or `type="toggle"`. |
| `removable` / `.removable` | `boolean` | `false` | Enables a trailing dismiss/remove button. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables user interaction and focusability. |
| `soft-disabled` / `.softDisabled` | `boolean` | `false` | Disables interaction while preserving keyboard focusability. |
| `href` / `.href` | `string` | `''` | Target link URL when `type="link"`. |
| `target` / `.target` | `'_blank' \| '_parent' \| '_self' \| '_top' \| ''` | `''` | Navigation target context when `type="link"`. |

### Slots

| Slot Name | Description |
| --- | --- |
| `(default)` | Chip label text content. |
| `slot="icon"` | Leading icon element or avatar graphic. |
| `slot="remove-icon"` | Trailing remove icon element (used when `removable` is active). |

### Events

| Event Name | Type | Description |
| --- | --- | --- |
| `@change` | `Event` | Fired when a filter or toggle chip selected state changes. |
| `@remove` | `Event` | Fired when a removable chip close icon is clicked or activated. |

### CSS Classes

```javascript
import chipStylesheet from '@material/web/labs/gb/components/chip/chip.css' with {type: 'css'};
```

| Class | Type | Description |
| --- | --- | --- |
| `.chip` | Root | Root chip element class. |
| `.chip-outlined`, `.chip-elevated`, `.chip-filled`, `.chip-tonal` | Modifiers | Color style variants. |
| `.chip-selected` | Modifier | Applied when selected is true. |
| `.chip-filter`, `.chip-input`, `.chip-removable` | Modifiers | Behavioral variants. |
| `.chip-with-leading-icon`, `.chip-with-trailing-icon`, `.chip-with-avatar` | Modifiers | Layout modifiers based on slotted content. |

## Usage Examples

### Surface Color Variants

```html
<div class="flex flex-wrap gap-2">
  <md-gb-chip color="outlined">Outlined</md-gb-chip>
  <md-gb-chip color="elevated">Elevated</md-gb-chip>
  <md-gb-chip color="tonal">Tonal</md-gb-chip>
  <md-gb-chip color="filled">Filled</md-gb-chip>
</div>
```

### Filter Chips

```html
<div class="flex gap-2">
  <md-gb-chip type="filter">All Results</md-gb-chip>
  <md-gb-chip type="filter" selected>Active Agents</md-gb-chip>
  <md-gb-chip type="filter">Archived</md-gb-chip>
</div>
```

### Removable Input Chip with Leading Icon

```html
<md-gb-chip removable color="tonal">
  <md-gb-icon slot="icon">person</md-gb-icon>
  Agent Alpha
  <md-gb-icon slot="remove-icon">close</md-gb-icon>
</md-gb-chip>
```
