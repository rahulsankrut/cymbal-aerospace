# Badge (`<md-gb-badge>`)

The `<md-gb-badge>` component displays small status indicators, alerts, or numerical notification counts on top of icons, navigation tabs, or list items.

## Import

```javascript
import '@material/web/labs/gb/components/badge/md-gb-badge.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `(default slot)` | `Slot` | `empty` | Badge numerical count or short text label. When empty, renders a small dot badge. |

## CSS Classes & Utility Styling

```javascript
import badgeStylesheet from '@material/web/labs/gb/components/badge/badge.css' with {type: 'css'};
```

* `.badge`: Root badge element class.
* `.badge-large`: Modifier class for badges containing text or numbers.

## Usage Examples

### Small Dot Badge

```html
<div style="position: relative; display: inline-block;">
  <md-gb-icon-button aria-label="Notifications">
    <md-gb-icon>notifications</md-gb-icon>
  </md-gb-icon-button>
  <md-gb-badge style="position: absolute; top: 4px; right: 4px;"></md-gb-badge>
</div>
```

### Numeric Badge

```html
<div style="position: relative; display: inline-block;">
  <md-gb-icon-button aria-label="Unread messages">
    <md-gb-icon>mail</md-gb-icon>
  </md-gb-icon-button>
  <md-gb-badge style="position: absolute; top: 2px; right: 2px;">3</md-gb-badge>
</div>

<div style="position: relative; display: inline-block;">
  <md-gb-icon-button aria-label="High notifications count">
    <md-gb-icon>notifications</md-gb-icon>
  </md-gb-icon-button>
  <md-gb-badge style="position: absolute; top: 2px; right: 2px;">99+</md-gb-badge>
</div>
```
