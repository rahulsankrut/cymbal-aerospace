# Icon Button (`<md-gb-icon-button>`)

The `<md-gb-icon-button>` component provides compact circular or square action buttons containing an icon, supporting standard, filled, tonal, and outlined variants across five height scales.

## Import

```javascript
import '@material/web/labs/gb/components/iconbutton/md-gb-icon-button.js';
import '@material/web/labs/gb/styles/icon/md-gb-icon.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `color` / `.color` | `'filled' \| 'tonal' \| 'outlined' \| 'standard'` | `'standard'` | Color variant. Note: `'elevated'` is **NOT** supported on icon buttons. |
| `size` / `.size` | `'xs' \| 'sm' \| 'md' \| 'lg' \| 'xl'` | `'sm'` | Container height scale: `xs` = 32px, `sm` = 40px (default), `md` = **56px** (large mobile bottom-bar icon buttons), `lg` = 96px, `xl` = 136px. |
| `square` / `.square` | `boolean` | `false` | Changes the geometry of the container from circular/pill to square. |
| `width` / `.width` | `'narrow' \| 'wide' \| ''` | `''` | Width modifier for narrow or pill-shaped icon buttons. |
| `type` / `.type` | `'submit' \| 'reset' \| 'button' \| 'toggle' \| 'link'` | `'submit'` | Behavior model. |
| `selected` / `.selected` | `boolean` | `false` | Active state when `type="toggle"`. |
| `href` / `.href` | `string` | `''` | Target URL when `type="link"`. |
| `target` / `.target` | `'_blank' \| '_parent' \| '_self' \| '_top' \| ''` | `''` | Target frame for `type="link"`. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables user interaction. |
| `soft-disabled` / `.softDisabled` | `boolean` | `false` | Disables activation while keeping focusability for screen readers. |

### Events

| Event | Type | Description |
| :--- | :--- | :--- |
| `@change` | `Event` | Fired when `type="toggle"` icon button selected state toggles. |

## Size Scale Details (`_icon-button-tokens.scss`)

* `size="xs"` = 32px height (20px icon) — compact inline/card/header actions.
* `size="sm"` = 40px height (24px icon, **default**) — standard toolbar actions.
* `size="md"` = **56px height** (24px icon) — large mobile bottom-bar icon buttons and FAB-like circular actions.
* `size="lg"` = 96px height (32px icon) — extra-large expressive hero controls.
* `size="xl"` = 136px height (40px icon) — giant display and kiosk controls.

> **CRITICAL SIZING & COLOR WARNINGS**:
> 1. `size="xl"` is 136px tall and `size="lg"` is 96px tall. ALWAYS use `size="md"` for 56px mobile action bar icon buttons. NEVER add outer Tailwind height utilities (`h-14`) directly to `<md-gb-icon-button>`.
> 2. `color="elevated"` is **INVALID** on `<md-gb-icon-button>`. To render a crisp white surface icon button on a tinted backdrop, use `color="tonal"` and override `--md-sys-color-secondary-container` on the host `style` attribute (e.g. `style="--md-sys-color-secondary-container: var(--md-sys-color-surface-container-lowest); --md-sys-color-on-secondary-container: var(--md-sys-color-on-surface);"`).

## CSS Classes & Utility Styling

```javascript
import iconButtonStylesheet from '@material/web/labs/gb/components/iconbutton/icon-button.css' with {type: 'css'};
```

* `.icon-btn`: Root icon button container.
* `.icon-btn-filled`, `.icon-btn-tonal`, `.icon-btn-outlined`, `.icon-btn-standard`: Color modifiers.
* `.icon-btn-xs`, `.icon-btn-sm`, `.icon-btn-md`, `.icon-btn-lg`, `.icon-btn-xl`: Size modifiers.
* `.icon-btn-square`, `.icon-btn-narrow`, `.icon-btn-wide`: Shape modifiers.
* `.icon-btn-unselected`, `.icon-btn-selected`: Toggle state classes.

## Usage Examples

### Color Variants

```html
<md-gb-icon-button color="standard" aria-label="Standard options">
  <md-gb-icon>more_vert</md-gb-icon>
</md-gb-icon-button>

<md-gb-icon-button color="filled" aria-label="Primary action">
  <md-gb-icon>edit</md-gb-icon>
</md-gb-icon-button>

<md-gb-icon-button color="tonal" aria-label="Voice search">
  <md-gb-icon>mic</md-gb-icon>
</md-gb-icon-button>

<md-gb-icon-button color="outlined" aria-label="Filter results">
  <md-gb-icon>filter_list</md-gb-icon>
</md-gb-icon-button>
```

### Height Scales

```html
<md-gb-icon-button size="xs" aria-label="Extra small 32px">
  <md-gb-icon>close</md-gb-icon>
</md-gb-icon-button>

<md-gb-icon-button size="sm" aria-label="Small 40px default">
  <md-gb-icon>settings</md-gb-icon>
</md-gb-icon-button>

<md-gb-icon-button size="md" aria-label="Medium 56px mobile bar">
  <md-gb-icon>add</md-gb-icon>
</md-gb-icon-button>
```

### White Surface Tonal Override

```html
<md-gb-icon-button color="tonal" style="--md-sys-color-secondary-container: var(--md-sys-color-surface-container-lowest); --md-sys-color-on-secondary-container: var(--md-sys-color-on-surface);" aria-label="Add favorite">
  <md-gb-icon>favorite</md-gb-icon>
</md-gb-icon-button>
```
