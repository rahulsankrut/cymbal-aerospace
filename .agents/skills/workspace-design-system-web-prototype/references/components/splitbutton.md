# Split Button (`<md-gb-split-button>`)

The Split Button (`<md-gb-split-button>`) combines a primary action button with an adjacent dropdown menu trigger for secondary option selection.

## Import

```javascript
import '@material/web/labs/gb/components/splitbutton/md-gb-split-button.js';
import '@material/web/labs/gb/components/menu/md-gb-menu.js';
import '@material/web/labs/gb/components/menu/md-gb-menu-item.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `color` / `.color` | `'filled' \| 'elevated' \| 'tonal' \| 'outlined'` | `'filled'` | Color style variant. |
| `size` / `.size` | `'xs' \| 'sm' \| 'md' \| 'lg' \| 'xl'` | `'sm'` | Size scale variant. |
| `selected` / `.selected` | `boolean` | `false` | Reflects whether the associated secondary menu is currently open. |

### Slots

| Slot Name | Description |
| --- | --- |
| `slot="leading"` | Primary action `<button>` element. |
| `slot="trailing"` | Secondary menu toggle `<button>` element configured with `popovertarget`. |

### CSS Classes

```javascript
import splitButtonStylesheet from '@material/web/labs/gb/components/splitbutton/split-button.css' with {type: 'css'};
```

| Class | Type | Description |
| --- | --- | --- |
| `.split-btn` | Root | Root split button class. |
| `.split-btn-selected` | Modifier | Applied when the secondary menu is open. |

## Usage Examples

### Basic Split Button with Attached Dropdown Menu

```html
<md-gb-split-button color="filled">
  <button slot="leading">Publish Document</button>
  <button slot="trailing" popovertarget="publish-options-menu" aria-label="More publishing options"></button>
  
  <md-gb-menu id="publish-options-menu">
    <md-gb-menu-item>Publish as Draft</md-gb-menu-item>
    <md-gb-menu-item>Schedule Publication...</md-gb-menu-item>
    <md-gb-menu-item>Export as PDF</md-gb-menu-item>
  </md-gb-menu>
</md-gb-split-button>
```
