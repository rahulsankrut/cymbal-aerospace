# Menu (`<md-gb-menu>`, `<md-gb-menu-group>`, `<md-gb-menu-item>`)

The `<md-gb-menu>` suite displays popover action menus, checkable options, or selection items attached to anchor triggers using standard HTML Popover attributes (`popovertarget`).

## Import

```javascript
import '@material/web/labs/gb/components/menu/md-gb-menu.js';
import '@material/web/labs/gb/components/menu/md-gb-menu-group.js';
import '@material/web/labs/gb/components/menu/md-gb-menu-item.js';
```

## API Reference

### `<md-gb-menu>` Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `color` / `.color` | `'standard' \| 'vibrant'` | `'standard'` | Menu container color theme. |

### `<md-gb-menu-group>` Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `checkable` / `.checkable` | `'single' \| 'multiple' \| null` | `null` | Selection model for group items. `'single'` creates radio selection; `'multiple'` creates checkbox multi-select. |

### `<md-gb-menu-item>` Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `checked` / `.checked` | `boolean` | `false` | Checked state of checkable item. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables menu item. |

### `<md-gb-menu-item>` Slots

| Slot Name | Description |
| :--- | :--- |
| `(default)` | Item label text. |
| `leading` | Leading icon before label. |
| `supporting-text` | Secondary text under main label. |
| `trailing-text` | Keyboard shortcut string or trailing metadata. |
| `trailing` | Trailing action icon or submenu chevron. |

### Events

| Event | Type | Description |
| :--- | :--- | :--- |
| `@change` | `Event` | Fired when checkable menu item checked state toggles. |
| `@input` | `Event` | Fired during state change. |

## CSS Classes & Utility Styling

```javascript
import menuStylesheet from '@material/web/labs/gb/components/menu/menu.css' with {type: 'css'};
```

* `.menu`: Root menu container.
* `.menu-vibrant`: Vibrant color modifier.
* `.menu-item`: Root menu item element.
* `.menu-item-content`, `.menu-item-leading`, `.menu-item-trailing`, `.menu-item-supporting-text`, `.menu-item-trailing-text`: Menu item child parts.

## Usage Examples

### Standard Popover Menu with Groups

```html
<md-gb-icon-button popovertarget="demo-menu" aria-label="Open menu">
  <md-gb-icon>more_vert</md-gb-icon>
</md-gb-icon-button>

<md-gb-menu id="demo-menu">
  <md-gb-menu-item>
    <md-gb-icon slot="leading">edit</md-gb-icon>
    Edit Prompt
    <span slot="trailing-text">⌘E</span>
  </md-gb-menu-item>

  <md-gb-menu-item disabled>
    <md-gb-icon slot="leading">share</md-gb-icon>
    Share Link
  </md-gb-menu-item>

  <md-gb-menu-group checkable="single">
    <md-gb-menu-item checked>High Precision (Pro)</md-gb-menu-item>
    <md-gb-menu-item>Fast Speed (Flash)</md-gb-menu-item>
  </md-gb-menu-group>

  <md-gb-menu-group checkable="multiple">
    <md-gb-menu-item checked>Include Search Grounding</md-gb-menu-item>
    <md-gb-menu-item>Enable Code Interpreter</md-gb-menu-item>
  </md-gb-menu-group>
</md-gb-menu>
```
