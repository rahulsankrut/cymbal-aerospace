# Menu (`<md-gb-menu>`, `<md-gb-menu-group>`, `<md-gb-menu-item>`)

Menus (`<md-gb-menu>`, `<md-gb-menu-group>`, and `<md-gb-menu-item>`) display dropdown lists of actions, selection filters, or checkable items anchored to target elements or popovers.

## Import

```javascript
import '@material/web/labs/gb/components/menu/md-gb-menu.js';
import '@material/web/labs/gb/components/menu/md-gb-menu-group.js';
import '@material/web/labs/gb/components/menu/md-gb-menu-item.js';
```

## API Reference

### `<md-gb-menu>` Attributes and Properties

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `color` / `.color` | `'standard' \| 'vibrant'` | `'standard'` | Surface color styling variant. |

### `<md-gb-menu-group>` Attributes and Properties

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `checkable` / `.checkable` | `'single' \| 'multiple' \| null` | `null` | Defines single-select radio or multiple-select checkbox selection behavior for child menu items. |

### `<md-gb-menu-item>` Attributes and Properties

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `checked` / `.checked` | `boolean` | `false` | Selected check state for checkable menu items. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables user interaction. |

### `<md-gb-menu-item>` Slots

| Slot Name | Description |
| --- | --- |
| `(default)` | Primary menu item action label. |
| `slot="leading"` | Leading icon element preceding main text. |
| `slot="supporting-text"` | Secondary description text displayed below the label. |
| `slot="trailing-text"` | Keyboard shortcut hints (e.g. `Ctrl+C`) or metadata text. |
| `slot="trailing"` | Trailing icon or arrow indicator. |

### Events

| Event Name | Type | Description |
| --- | --- | --- |
| `@change` | `Event` | Fired when checkable item selection changes. |
| `@input` | `Event` | Fired when checkable item selection changes. |

### CSS Classes

```javascript
import menuStylesheet from '@material/web/labs/gb/components/menu/menu.css' with {type: 'css'};
```

| Class | Type | Description |
| --- | --- | --- |
| `.menu`, `.menu-vibrant` | Root / Modifier | Menu surface styles. |
| `.menu-item`, `.menu-item-content`, `.menu-item-leading`, `.menu-item-trailing`, `.menu-item-supporting-text`, `.menu-item-trailing-text` | Parts | Menu item parts. |

## Usage Examples

### Native Popover Anchor Menu

Use native HTML `popovertarget` to anchor `<md-gb-menu>` to a button trigger:

```html
<button popovertarget="workspace-menu" class="px-4 py-2 bg-surface-container rounded-lg border border-outline">
  Open Menu
</button>

<md-gb-menu id="workspace-menu">
  <md-gb-menu-item>
    <md-gb-icon slot="leading">edit</md-gb-icon>
    Edit Document
    <span slot="trailing-text">Ctrl+E</span>
  </md-gb-menu-item>

  <md-gb-menu-item>
    <md-gb-icon slot="leading">content_copy</md-gb-icon>
    Duplicate
    <span slot="supporting-text">Creates a copy in current workspace</span>
  </md-gb-menu-item>

  <md-gb-menu-item disabled>
    <md-gb-icon slot="leading">lock</md-gb-icon>
    Restricted Action
  </md-gb-menu-item>

  <!-- Single Selection Group (Radio Behavior) -->
  <md-gb-menu-group checkable="single">
    <md-gb-menu-item checked>Sort by Name</md-gb-menu-item>
    <md-gb-menu-item>Sort by Date</md-gb-menu-item>
  </md-gb-menu-group>

  <!-- Multiple Selection Group (Checkbox Behavior) -->
  <md-gb-menu-group checkable="multiple">
    <md-gb-menu-item checked>Show Hidden Files</md-gb-menu-item>
    <md-gb-menu-item>Compact Density</md-gb-menu-item>
  </md-gb-menu-group>
</md-gb-menu>
```
