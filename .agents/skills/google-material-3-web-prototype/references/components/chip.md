# Chip (`<md-gb-chip>`)

The `<md-gb-chip>` component provides compact interactive pills for selection, filtering, quick action triggers, or removable input tokens.

## Import

```javascript
import '@material/web/labs/gb/components/chip/md-gb-chip.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `color` / `.color` | `'outlined' \| 'elevated' \| 'filled' \| 'tonal'` | `'outlined'` | Visual color variant of the chip. |
| `type` / `.type` | `'action' \| 'filter' \| 'toggle' \| 'link'` | `'action'` | Functional type of chip control. |
| `selected` / `.selected` | `boolean` | `false` | Selected state when `type="filter"` or `type="toggle"`. |
| `removable` / `.removable` | `boolean` | `false` | Displays a trailing remove button that fires `@remove` when clicked. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables user interaction. |
| `soft-disabled` / `.softDisabled` | `boolean` | `false` | Disables activation while preserving keyboard focusability. |
| `href` / `.href` | `string` | `''` | Target URL when `type="link"`. |
| `target` / `.target` | `'_blank' \| '_parent' \| '_self' \| '_top' \| ''` | `''` | Target window/frame for `type="link"`. |

### Slots

| Slot Name | Description |
| :--- | :--- |
| `(default)` | Visible chip text label. |
| `icon` | Leading icon or avatar slot. |
| `remove-icon` | Custom trailing remove icon when `removable` is active. |

### Events

| Event | Type | Description |
| :--- | :--- | :--- |
| `@change` | `Event` | Fired when filter/toggle chip selected state changes. |
| `@remove` | `Event` | Fired when user clicks the trailing remove button on a removable chip. |

## CSS Classes & Utility Styling

```javascript
import chipStylesheet from '@material/web/labs/gb/components/chip/chip.css' with {type: 'css'};
```

* `.chip`: Root chip element.
* `.chip-outlined`, `.chip-elevated`, `.chip-filled`, `.chip-tonal`: Color modifiers.
* `.chip-selected`: Active selection modifier.
* `.chip-filter`, `.chip-input`, `.chip-removable`: Type modifiers.
* `.chip-with-leading-icon`, `.chip-with-trailing-icon`, `.chip-with-avatar`: Slot layout modifiers.

## Usage Examples

### Color Variants

```html
<md-gb-chip color="outlined">Outlined</md-gb-chip>
<md-gb-chip color="elevated">Elevated</md-gb-chip>
<md-gb-chip color="tonal">Tonal</md-gb-chip>
<md-gb-chip color="filled">Filled</md-gb-chip>
```

### Filter Chips

```html
<div class="flex gap-s100">
  <md-gb-chip type="filter">Unselected Filter</md-gb-chip>
  <md-gb-chip type="filter" selected>
    <md-gb-icon slot="icon">check</md-gb-icon>
    Active Filter
  </md-gb-chip>
</div>
```

### Removable Input Chips

```html
<div class="flex gap-s100">
  <md-gb-chip removable color="tonal">
    <md-gb-icon slot="icon">person</md-gb-icon>
    Agent Alpha
    <md-gb-icon slot="remove-icon">close</md-gb-icon>
  </md-gb-chip>
  <md-gb-chip removable color="tonal">
    <md-gb-icon slot="icon">smart_toy</md-gb-icon>
    Gemini Flash
    <md-gb-icon slot="remove-icon">close</md-gb-icon>
  </md-gb-chip>
</div>
```
