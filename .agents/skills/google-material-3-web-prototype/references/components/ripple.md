# Ripple Effect (`ripple` / `<md-ripple>`)

The ripple system provides visual surface feedback for touch, click, and pointer press interactions on custom controls.

## Import

```javascript
import '@material/web/labs/gb/components/ripple/ripple.js';
import '@material/web/ripple/ripple.js';
```

## CSS Classes & Utility Styling

```javascript
import rippleStylesheet from '@material/web/labs/gb/components/ripple/ripple.css' with {type: 'css'};
```

* `.ripple`: Root ripple container class.
* `.ripple-host`: Ripple host element modifier.
* `.ripple-target`: Ripple target element part.

## Usage Examples

### Custom Interactive Container with Ripple

```html
<div class="relative overflow-hidden cursor-pointer p-s200 bg-surface-container rounded-md">
  <md-ripple></md-ripple>
  <span class="typescale-body-md">Custom Interactive Surface</span>
</div>
```
