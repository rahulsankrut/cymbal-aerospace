# FAB (`<md-gb-fab>`)

The Floating Action Button (`<md-gb-fab>`) performs the primary or most important action on a screen.

## Import

```javascript
import '@material/web/labs/gb/components/fab/md-gb-fab.js';
import '@material/web/labs/gb/styles/icon/md-gb-icon.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `color` / `.color` | `'primary' \| 'primary-container' \| 'secondary' \| 'secondary-container' \| 'tertiary' \| 'tertiary-container'` | `'primary-container'` | Color scheme container surface. |
| `size` / `.size` | `'default' \| 'md' \| 'lg'` | `'default'` | Size variant. |

### Slots

| Slot Name | Description |
| --- | --- |
| `(default)` | Slotted `<md-gb-icon>` element, plus optional extended text label. |

### CSS Classes

```javascript
import fabStylesheet from '@material/web/labs/gb/components/fab/fab.css' with {type: 'css'};
```

| Class | Type | Description |
| --- | --- | --- |
| `.fab` | Root | Root FAB class. |
| `.fab-primary`, `.fab-primary-container` | Modifiers | Primary color surface variants. |
| `.fab-secondary`, `.fab-secondary-container` | Modifiers | Secondary color surface variants. |
| `.fab-tertiary`, `.fab-tertiary-container` | Modifiers | Tertiary color surface variants. |
| `.fab-md`, `.fab-lg` | Modifiers | Size modifiers. |

## Usage Examples

### Icon-Only FAB

```html
<md-gb-fab aria-label="Compose new message">
  <md-gb-icon>add</md-gb-icon>
</md-gb-fab>
```

### Extended FAB with Text Label

```html
<md-gb-fab color="primary-container">
  <md-gb-icon>edit</md-gb-icon>
  New Task
</md-gb-fab>
```

### Color Container Variants

```html
<div class="flex gap-4">
  <md-gb-fab color="primary-container" aria-label="Primary action">
    <md-gb-icon>add</md-gb-icon>
  </md-gb-fab>
  <md-gb-fab color="secondary-container" aria-label="Secondary action">
    <md-gb-icon>add</md-gb-icon>
  </md-gb-fab>
  <md-gb-fab color="tertiary-container" aria-label="Tertiary action">
    <md-gb-icon>add</md-gb-icon>
  </md-gb-fab>
</div>
```
