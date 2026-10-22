# Badge (`<md-gb-badge>`)

The Badge (`<md-gb-badge>`) provides compact status indicators or numeric notification counts displayed alongside icons, navigation items, or interactive controls.

## Import

```javascript
import '@material/web/labs/gb/components/badge/md-gb-badge.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `slot` (default) | `Slot` | `undefined` | Badge content. When empty, renders as a small indicator dot. When non-empty, renders numeric counts or labels. |

### CSS Classes

```javascript
import badgeStylesheet from '@material/web/labs/gb/components/badge/badge.css' with {type: 'css'};
```

| Class | Type | Description |
| --- | --- | --- |
| `.badge` | Root | Default badge styling. |
| `.badge-large` | Modifier | Large badge layout applied automatically when content is provided. |

## Usage Examples

### Small Dot Badge

An empty `<md-gb-badge>` renders as a small dot indicator.

```html
<div class="relative inline-flex">
  <md-gb-icon-button aria-label="Notifications">
    <md-gb-icon>notifications</md-gb-icon>
  </md-gb-icon-button>
  <md-gb-badge class="absolute top-1 right-1"></md-gb-badge>
</div>
```

### Numeric and Text Badges

Provide text or numeric content inside the badge default slot.

```html
<div class="relative inline-flex items-center gap-2">
  <md-gb-badge>3</md-gb-badge>
  <md-gb-badge>99+</md-gb-badge>
  <md-gb-badge>NEW</md-gb-badge>
</div>
```
