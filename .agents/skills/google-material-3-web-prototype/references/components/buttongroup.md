# Button Group (`<md-gb-button-group>`)

The `<md-gb-button-group>` component presents a group of related buttons arranged horizontally in standard or connected layout styles with single, multiple, or independent selection models.

## Import

```javascript
import '@material/web/labs/gb/components/buttongroup/md-gb-button-group.js';
import '@material/web/labs/gb/components/button/md-gb-button.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `variant` / `.variant` | `'standard' \| 'connected'` | `'standard'` | Layout style. `'standard'` separates buttons with standard gaps; `'connected'` joins buttons into a continuous segmented layout with 2px gaps and morphing corner shapes. |
| `selection` / `.selection` | `'none' \| 'single' \| 'multiple'` | `'none'` | Selection behavior. `'single'` allows 0 or 1 active items; `'multiple'` allows independent toggles. |
| `required` / `.required` | `boolean` | `false` | In `'single'` selection mode, prevents deselecting the currently active button. |
| `disabled` / `.disabled` | `boolean` | `false` | Cascades disabled state to all child buttons. |
| `value` / `.value` | `string` | `''` | Value of the first selected button in DOM order. In `'single'` selection mode, setting this property updates selection. |
| `.values` | `string[]` | `[]` | Read-only array of all selected button values. |
| `.buttons` | `ButtonElement[]` | `[]` | Read-only array of child `<md-gb-button>` elements. |
| `.selectedButtons` | `ButtonElement[]` | `[]` | Read-only array of currently selected `<md-gb-button>` elements. |
| `.selectedIndex` | `number` | `-1` | Read-only index of first selected button in DOM order. |
| `.selectedIndices` | `number[]` | `[]` | Read-only array of indices for all selected buttons. |

### Events

| Event | Type | Description |
| :--- | :--- | :--- |
| `@input` | `InputEvent` | Fired when selection state changes via user interaction (bubbles, composed). |
| `@change` | `Event` | Fired when selection state changes via user interaction (bubbles). |

## Selection Semantics

* `selection="none"`: Child buttons act as standard independent buttons (`type="button"`). Link buttons (`href`) are supported.
* `selection="single"`: At most one button selected at a time. Clicking an unselected button selects it and deselects siblings. If `required` is set, clicking the active button will NOT deselect it.
* `selection="multiple"`: Zero or more buttons may be selected independently. `values` getter returns all selected values in DOM order.

## Layout, Spacing, and Tokens

* **Standard Variant Gaps**: XS: 18px, SM (default): 12px, MD / LG / XL: 8px.
* **Connected Variant Gaps**: 2px gap across all button sizes.
* **Connected Corner Radii Rules**:
  * Unselected connected buttons maintain outer rounded corners and subtle inner radii.
  * Selected connected buttons in any position (first, middle, last) morph dynamically to full pill corners (`calc(var(--container-height) / 2)`).
* **Outlined Selection Styling**:
  * Selected outlined buttons display an inverse surface background fill (`--md-sys-color-inverse-surface`) with no visible border outline.
  * Unselected outlined buttons display a transparent background with visible outline variant borders.

## Accessibility Requirements

* **Accessible Name**: Authors MUST provide an accessible name via `aria-label` or `aria-labelledby` on `<md-gb-button-group>` (e.g. `aria-label="Text formatting options"`).
* **Role**: Exposes `ElementInternals.role = 'toolbar'`.
* **Keyboard Navigation**: Defaults `focusgroup="toolbar wrap inline"` for horizontal arrow key navigation across group buttons.

## CSS Classes & Utility Styling

```javascript
import buttonGroupStylesheet from '@material/web/labs/gb/components/buttongroup/button-group.css' with {type: 'css'};
```

* `.btn-group`: Root group container.
* `.btn-group-standard`: Standard layout modifier.
* `.btn-group-connected`: Connected layout modifier.

## Usage Examples

### Standard Group

```html
<md-gb-button-group aria-label="Standard action items">
  <md-gb-button color="filled">Cut</md-gb-button>
  <md-gb-button color="filled">Copy</md-gb-button>
  <md-gb-button color="filled">Paste</md-gb-button>
</md-gb-button-group>
```

### Connected Single Selection Group

```html
<md-gb-button-group aria-label="View timeframe" variant="connected" selection="single" required>
  <md-gb-button color="outlined" value="day" selected>Day</md-gb-button>
  <md-gb-button color="outlined" value="week">Week</md-gb-button>
  <md-gb-button color="outlined" value="month">Month</md-gb-button>
  <md-gb-button color="outlined" value="year">Year</md-gb-button>
</md-gb-button-group>
```

### Multi-Selection Formatting Toolbar

```html
<md-gb-button-group aria-label="Text formatting" variant="connected" selection="multiple">
  <md-gb-button value="bold" aria-label="Bold text" selected>
    <md-gb-icon>format_bold</md-gb-icon>
  </md-gb-button>
  <md-gb-button value="italic" aria-label="Italic text" selected>
    <md-gb-icon>format_italic</md-gb-icon>
  </md-gb-button>
  <md-gb-button value="underline" aria-label="Underline text">
    <md-gb-icon>format_underlined</md-gb-icon>
  </md-gb-button>
</md-gb-button-group>
```
