# Button (`<md-gb-button>`)

The `<md-gb-button>` component provides action buttons, links, and toggle buttons across five visual emphasis levels and five container height scales.

## Import

```javascript
import '@material/web/labs/gb/components/button/md-gb-button.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `color` / `.color` | `'filled' \| 'elevated' \| 'tonal' \| 'outlined' \| 'text'` | `'text'` | Sets the color variant and emphasis level. |
| `size` / `.size` | `'xs' \| 'sm' \| 'md' \| 'lg' \| 'xl'` | `'sm'` | Button height scale: `xs` = 32px, `sm` = 40px (default), `md` = **56px** (mobile bottom-bar pills & primary CTAs), `lg` = 96px, `xl` = 136px. |
| `square` / `.square` | `boolean` | `false` | Changes the shape of the button container from fully rounded pill to square/rounded rect. |
| `type` / `.type` | `'submit' \| 'reset' \| 'button' \| 'toggle' \| 'link'` | `'submit'` | Behavior model of the button control. |
| `selected` / `.selected` | `boolean` | `false` | Selected toggle state when `type="toggle"`. |
| `href` / `.href` | `string` | `''` | Target URL when `type="link"`. |
| `target` / `.target` | `'_blank' \| '_parent' \| '_self' \| '_top' \| ''` | `''` | Target window/frame for `type="link"`. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables user interaction. |
| `soft-disabled` / `.softDisabled` | `boolean` | `false` | Disables activation while preserving focusability for accessibility. |

### Events

| Event | Type | Description |
| :--- | :--- | :--- |
| `@change` | `Event` | Fired when `type="toggle"` button toggles between selected and unselected states. |

## Size Scale Details (`_button-tokens.scss`)

* `size="xs"` = 32px height (20px icon) — compact inline, card, and header actions.
* `size="sm"` = 40px height (24px icon, **default**) — standard toolbar and secondary buttons.
* `size="md"` = **56px height** (24px icon, `title-md` label) — large mobile bottom-bar pills, FAB-like actions, and primary CTAs.
* `size="lg"` = 96px height (32px icon, `headline-sm` label) — extra-large expressive hero controls.
* `size="xl"` = 136px height (40px icon, `headline-lg` label) — giant display and kiosk controls.

> **CRITICAL SIZING WARNING**: `size="xl"` is 136px tall and `size="lg"` is 96px tall. ALWAYS use `size="md"` for 56px mobile action bar buttons and mobile primary CTAs. NEVER add outer Tailwind height utilities (such as `h-14`) directly to `<md-gb-button>`.

## Customizing Token Colors on Host

To customize surface or label colors on `<md-gb-button>` (for example, on `color="elevated"`), override the semantic `--md-sys-color-*` tokens consumed by that variant directly on the host `style` attribute:

```html
<md-gb-button color="elevated" style="--md-sys-color-surface-container-low: var(--md-sys-color-surface-container-lowest); --md-sys-color-primary: var(--md-sys-color-error);">
  Custom Elevated Action
</md-gb-button>
```

## CSS Classes & Utility Styling

```javascript
import buttonStylesheet from '@material/web/labs/gb/components/button/button.css' with {type: 'css'};
```

* `.btn`: Root container class.
* `.btn-filled`: Filled variant.
* `.btn-elevated`: Elevated variant.
* `.btn-tonal`: Tonal variant.
* `.btn-outlined`: Outlined variant.
* `.btn-text`: Text variant.
* `.btn-xs`, `.btn-sm`, `.btn-md`, `.btn-lg`, `.btn-xl`: Size modifier classes.
* `.btn-square`: Square shape modifier.
* `.btn-unselected`, `.btn-selected`: Toggle state classes.

## Usage Examples

### Visual Emphasis Variants

```html
<md-gb-button color="filled">Filled (High Emphasis)</md-gb-button>
<md-gb-button color="elevated">Elevated</md-gb-button>
<md-gb-button color="tonal">Tonal (Medium Emphasis)</md-gb-button>
<md-gb-button color="outlined">Outlined</md-gb-button>
<md-gb-button color="text">Text (Low Emphasis)</md-gb-button>
```

### Height Scales

```html
<md-gb-button color="filled" size="xs">Extra Small (32px)</md-gb-button>
<md-gb-button color="filled" size="sm">Small (40px - Default)</md-gb-button>
<md-gb-button color="filled" size="md">Medium (56px - Mobile Bottom Bar CTA)</md-gb-button>
<md-gb-button color="filled" size="lg">Large (96px)</md-gb-button>
<md-gb-button color="filled" size="xl">Extra Large (136px)</md-gb-button>
```

### Toggle Button

```html
<md-gb-button color="tonal" type="toggle">Unselected Toggle</md-gb-button>
<md-gb-button color="tonal" type="toggle" selected>Selected Toggle</md-gb-button>
```

### Link Button

```html
<md-gb-button color="outlined" type="link" href="https://material.io" target="_blank">
  Open Documentation
</md-gb-button>
```
