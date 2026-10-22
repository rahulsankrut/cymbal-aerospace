# Split Button (`<md-gb-split-button>`)

The `<md-gb-split-button>` component combines a primary action button with a secondary trailing arrow button that toggles an attached option menu.

## Import

```javascript
import '@material/web/labs/gb/components/splitbutton/md-gb-split-button.js';
import '@material/web/labs/gb/components/menu/md-gb-menu.js';
import '@material/web/labs/gb/components/menu/md-gb-menu-item.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `color` / `.color` | `'filled' \| 'elevated' \| 'tonal' \| 'outlined'` | `'filled'` | Color role variant. |
| `size` / `.size` | `'xs' \| 'sm' \| 'md' \| 'lg' \| 'xl'` | `'sm'` | Container height scale. |
| `selected` / `.selected` | `boolean` | `false` | Whether or not the split button's option menu is open. |

### Slots

| Slot Name | Description |
| :--- | :--- |
| `leading` | Primary action button trigger. |
| `trailing` | Secondary menu toggle trigger with `popovertarget`. |

## CSS Classes & Utility Styling

```javascript
import splitButtonStylesheet from '@material/web/labs/gb/components/splitbutton/split-button.css' with {type: 'css'};
```

* `.split-btn`: Root split button container.
* `.split-btn-selected`: Active menu state modifier.

## Usage Examples

### Standard Split Button with Popover Menu

```html
<md-gb-split-button color="filled">
  <button slot="leading">Run Pipeline</button>
  <button slot="trailing" popovertarget="split-menu" aria-label="More launch options"></button>
  <md-gb-menu id="split-menu">
    <md-gb-menu-item>Run with Debug Logging</md-gb-menu-item>
    <md-gb-menu-item>Run Async in Background</md-gb-menu-item>
    <md-gb-menu-item>Schedule Recurring Run</md-gb-menu-item>
  </md-gb-menu>
</md-gb-split-button>
```
