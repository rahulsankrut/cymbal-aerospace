# Switch (`<md-gb-switch>`)

The Switch (`<md-gb-switch>`) toggles between selected and unselected states for a binary preference setting.

## Import

```javascript
import '@material/web/labs/gb/components/switch/md-gb-switch.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `selected` / `.selected` | `boolean` | `false` | Whether the switch toggle is active/selected. |
| `defaultselected` / `.defaultSelected` | `boolean` | `false` | Default selection state for form resets. |
| `required` / `.required` | `boolean` | `false` | Whether switch selection is required for form submission. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables user interaction. |

### Slots

| Slot Name | Description |
| --- | --- |
| `slot="off-icon"` | Icon displayed inside the switch handle when unselected. |
| `slot="on-icon"` | Icon displayed inside the switch handle when selected. |

### Events

| Event Name | Type | Description |
| --- | --- | --- |
| `@change` | `Event` | Fired when selection state changes. |
| `@input` | `Event` | Fired when selection state changes. |

### CSS Classes

```javascript
import switchStylesheet from '@material/web/labs/gb/components/switch/switch.css' with {type: 'css'};
```

| Class | Type | Description |
| --- | --- | --- |
| `.switch` | Root | Root switch class. |
| `.switch-icon-off`, `.switch-icon-on` | Parts | Handle icon parts. |

## Usage Examples

### Basic Toggle Switch

```html
<label class="flex items-center justify-between p-4 bg-surface-container rounded-lg cursor-pointer">
  <span class="typescale-body-medium text-on-surface">Enable notifications</span>
  <md-gb-switch selected></md-gb-switch>
</label>
```

### Switch with Custom On/Off Icons

```html
<label class="flex items-center justify-between p-4 bg-surface-container rounded-lg cursor-pointer">
  <span class="typescale-body-medium text-on-surface">Dark mode theme</span>
  <md-gb-switch selected>
    <md-gb-icon slot="off-icon">light_mode</md-gb-icon>
    <md-gb-icon slot="on-icon">dark_mode</md-gb-icon>
  </md-gb-switch>
</label>
```
