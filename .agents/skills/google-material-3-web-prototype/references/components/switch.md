# Switch (`<md-gb-switch>`)

The `<md-gb-switch>` component provides a visual toggle switch for binary on/off settings.

## Import

```javascript
import '@material/web/labs/gb/components/switch/md-gb-switch.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `selected` / `.selected` | `boolean` | `false` | Whether or not the switch handle is selected (ON). |
| `defaultselected` / `.defaultSelected` | `boolean` | `false` | Initial default selected state. |
| `required` / `.required` | `boolean` | `false` | Marks switch as required in form contexts. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables interaction. |

### Slots

| Slot Name | Description |
| :--- | :--- |
| `off-icon` | Optional icon element rendered inside handle when unselected (OFF). |
| `on-icon` | Optional icon element rendered inside handle when selected (ON). |

### Events

| Event | Type | Description |
| :--- | :--- | :--- |
| `@change` | `Event` | Fired when selected state toggles. |
| `@input` | `Event` | Fired during user toggle. |

## CSS Classes & Utility Styling

```javascript
import switchStylesheet from '@material/web/labs/gb/components/switch/switch.css' with {type: 'css'};
```

* `.switch`: Root switch container.
* `.switch-icon-off`, `.switch-icon-on`: Icon handle child parts.

## Usage Examples

### Basic Switch

```html
<label class="flex items-center justify-between p-s200 bg-surface-container rounded-md">
  <span class="typescale-body-md">Enable Dark Theme</span>
  <md-gb-switch selected></md-gb-switch>
</label>
```

### Switch with Custom State Icons

```html
<label class="flex items-center justify-between p-s200 bg-surface-container rounded-md">
  <span class="typescale-body-md">Notifications</span>
  <md-gb-switch selected>
    <md-gb-icon slot="off-icon">close</md-gb-icon>
    <md-gb-icon slot="on-icon">check</md-gb-icon>
  </md-gb-switch>
</label>
```
