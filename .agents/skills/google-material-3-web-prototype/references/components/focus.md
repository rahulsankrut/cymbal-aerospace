# Focus Ring (`focus-ring` / `<md-focus-ring>`)

The focus ring system provides accessible, stateful focus indicators around custom interactive components and standard DOM elements during keyboard navigation.

## Import

```javascript
import '@material/web/labs/gb/components/focus/focus-ring.js';
import '@material/web/focus/md-focus-ring.js';
```

## CSS Classes & Utility Styling

```javascript
import focusRingStylesheet from '@material/web/labs/gb/components/focus/focus-ring.css' with {type: 'css'};
```

* `.focus-ring-outer`: Outer focus ring indicator class.
* `.focus-ring-inner`: Inner focus ring accent class.
* `.focus-ring-host`: Host modifier class.
* `.focus-ring-target`: Target element reference class.

## Usage Examples

### Custom Focus Target

```html
<button class="relative focus-ring-host">
  <md-focus-ring></md-focus-ring>
  Custom Interactive Button
</button>
```
