# FAB (`<md-gb-fab>`)

The `<md-gb-fab>` component provides Floating Action Buttons for the primary or most important action on a screen.

## Import

```javascript
import '@material/web/labs/gb/components/fab/md-gb-fab.js';
import '@material/web/labs/gb/styles/icon/md-gb-icon.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `color` / `.color` | `'primary' \| 'primary-container' \| 'secondary' \| 'secondary-container' \| 'tertiary' \| 'tertiary-container'` | `'primary-container'` | Color role variant. |
| `size` / `.size` | `'default' \| 'md' \| 'lg'` | `'default'` | Size scale of the FAB container. |

## CSS Classes & Utility Styling

```javascript
import fabStylesheet from '@material/web/labs/gb/components/fab/fab.css' with {type: 'css'};
```

* `.fab`: Root FAB container class.
* `.fab-primary`, `.fab-primary-container`, `.fab-secondary`, `.fab-secondary-container`, `.fab-tertiary`, `.fab-tertiary-container`: Color modifiers.
* `.fab-md`, `.fab-lg`: Size modifiers.

## Usage Examples

### Icon-Only FAB

```html
<md-gb-fab aria-label="Add new item">
  <md-gb-icon>add</md-gb-icon>
</md-gb-fab>
```

### Extended FAB (Icon + Text Label)

```html
<md-gb-fab color="primary-container">
  <md-gb-icon>add</md-gb-icon>
  Compose Prompt
</md-gb-fab>
```

### Color Role Variants

```html
<div class="flex gap-s200 items-center">
  <md-gb-fab color="primary" aria-label="Primary action">
    <md-gb-icon>edit</md-gb-icon>
  </md-gb-fab>

  <md-gb-fab color="secondary-container" aria-label="Secondary action">
    <md-gb-icon>navigation</md-gb-icon>
  </md-gb-fab>

  <md-gb-fab color="tertiary-container" aria-label="AI action">
    <md-gb-icon>auto_awesome</md-gb-icon>
  </md-gb-fab>
</div>
```

### Size Scales

```html
<div class="flex gap-s200 items-center">
  <md-gb-fab size="default" aria-label="Standard FAB">
    <md-gb-icon>add</md-gb-icon>
  </md-gb-fab>

  <md-gb-fab size="md" aria-label="Medium FAB">
    <md-gb-icon>add</md-gb-icon>
  </md-gb-fab>

  <md-gb-fab size="lg" aria-label="Large FAB">
    <md-gb-icon>add</md-gb-icon>
  </md-gb-fab>
</div>
```
