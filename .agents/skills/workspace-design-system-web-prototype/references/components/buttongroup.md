# Button Group (`<md-gb-button-group>`)

The Button Group (`<md-gb-button-group>`) presents a set of related action buttons or toggle controls in standard or connected horizontal layouts with single, multiple, or no selection management.

## Import

```javascript
import '@material/web/labs/gb/components/buttongroup/md-gb-button-group.js';
import '@material/web/labs/gb/components/button/md-gb-button.js';
```

## API Reference

### Attributes and Properties

|API|Type|Default|Description|
|---|---|---|---|
|`variant` / `.variant`|`'standard' \| 'connected'`|`'standard'`|Group presentation layout. `standard` uses spaced buttons; `connected` merges buttons into a joined segment bar.|
|`selection` / `.selection`|`'none' \| 'single' \| 'multiple'`|`'none'`|Selection mode. When set to `single` or `multiple`, cascades `type="toggle"` down to child `<md-gb-button>` elements.|
|`required` / `.required`|`boolean`|`false`|In `single` selection mode, prevents deselecting the active button.|
|`disabled` / `.disabled`|`boolean`|`false`|Disables all child buttons in the group while preserving individual state records.|
|`value` / `.value`|`string`|`''`|Value of the first selected button in DOM order. Setting this in `single` mode updates the active selection.|
|`.values`|`string[]`|`[]`|**Read-only getter**. Array of values for all currently selected buttons in DOM order.|
|`.buttons`|`ButtonElement[]`|`[]`|**Read-only getter**. Array of child `md-gb-button` elements assigned to the group.|
|`.selectedButtons`|`ButtonElement[]`|`[]`|**Read-only getter**. Array of currently selected `md-gb-button` elements.|
|`.selectedIndex`|`number`|`-1`|**Read-only getter**. Index of first selected button in DOM order.|
|`.selectedIndices`|`number[]`|`[]`|**Read-only getter**. Indices of all selected buttons in DOM order.|

### Events

|Event Name|Type|Description|
|---|---|---|
|`@input`|`InputEvent`|Fired when selection changes from user interaction (bubbles, composed).|
|`@change`|`Event`|Fired when selection changes from user interaction (bubbles).|

## Selection Semantics and Layout Behavior

### Selection Modes

- **`selection="none"`**: Child buttons act as independent standard action triggers (`type="button"`). Link buttons (`href`) are supported.
- **`selection="single"`**: Enforces zero or one selected button. Clicking an unselected button selects it and deselects siblings. Clicking the active button deselects it unless `required` is true.
- **`selection="multiple"`**: Allows zero or more buttons to be toggled independently. Access `.values` for an array of selected payloads.

### Spacing and Gap Matrix

- **Standard Variant**: XS: `18px` gap; SM: `12px` gap; MD / LG / XL: `8px` gap.
- **Connected Variant**: Enforces a continuous `2px` gap across all button sizes.

### Outlined Selection Styling

When child buttons use `color="outlined"` inside a connected group:

- **Selected Buttons**: Render with inverse-surface background fill (`--md-sys-color-inverse-surface`) and transparent borders to prevent layout shift.
- **Unselected Buttons**: Render with transparent backgrounds and visible outlined borders (`--md-sys-color-outline-variant`).

## Accessibility Requirements

- **Accessible Name**: Authors **MUST** provide an `aria-label` or `aria-labelledby` on `<md-gb-button-group>` (e.g., `aria-label="Text formatting options"`).
- **ARIA Role**: Exposes `role="toolbar"`.
- **Keyboard Navigation**: Defaults to `focusgroup="toolbar wrap inline"` for horizontal arrow key navigation across group buttons.

## CSS Classes

```javascript
import buttonGroupStylesheet from '@material/web/labs/gb/components/buttongroup/button-group.css' with {type: 'css'};
```

|Class|Type|Description|
|---|---|---|
|`.btn-group`|Root|Component root.|
|`.btn-group-standard`|Modifier|Standard layout spacing.|
|`.btn-group-connected`|Modifier|Connected segmented bar layout.|

## Usage Examples

### Standard Action Group

```html
<md-gb-button-group aria-label="Standard actions">
  <md-gb-button color="filled">Cut</md-gb-button>
  <md-gb-button color="filled">Copy</md-gb-button>
  <md-gb-button color="filled">Paste</md-gb-button>
</md-gb-button-group>
```

### Connected Single Selection Segmented Bar

```html
<md-gb-button-group
  aria-label="View mode"
  variant="connected"
  selection="single">
  <md-gb-button color="outlined" value="day" selected>Day</md-gb-button>
  <md-gb-button color="outlined" value="week">Week</md-gb-button>
  <md-gb-button color="outlined" value="month">Month</md-gb-button>
  <md-gb-button color="outlined" value="year">Year</md-gb-button>
</md-gb-button-group>
```

### Connected Required Single Selection (Map Style)

```html
<md-gb-button-group
  aria-label="Map style"
  variant="connected"
  selection="single"
  required>
  <md-gb-button color="outlined" value="map" selected>Map</md-gb-button>
  <md-gb-button color="outlined" value="satellite">Satellite</md-gb-button>
  <md-gb-button color="outlined" value="terrain">Terrain</md-gb-button>
</md-gb-button-group>
```

### Multi-Selection Formatting Toolbar with Icons

```html
<md-gb-button-group
  aria-label="Alignment options"
  variant="connected"
  selection="single"
  required>
  <md-gb-button color="outlined" value="left" aria-label="Align left" selected>
    <md-gb-icon>format_align_left</md-gb-icon>
  </md-gb-button>
  <md-gb-button color="outlined" value="center" aria-label="Align center">
    <md-gb-icon>format_align_center</md-gb-icon>
  </md-gb-button>
  <md-gb-button color="outlined" value="right" aria-label="Align right">
    <md-gb-icon>format_align_right</md-gb-icon>
  </md-gb-button>
</md-gb-button-group>
```
