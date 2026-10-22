# App Bar (`<md-gb-app-bar>`)

The `<md-gb-app-bar>` component provides top and bottom application bars for screen titles, navigation actions, search inputs, and contextual controls.

## Import

```javascript
import '@material/web/labs/gb/components/appbar/md-gb-app-bar.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `size` / `.size` | `'sm' \| 'md' \| 'lg'` | `'sm'` | Controls the height and layout density of the app bar. |
| `variant` / `.variant` | `'standard' \| 'search'` | `'standard'` | App bar mode. `'search'` turns the bar into an embedded search bar layout. |
| `scrolled` / `.scrolled` | `boolean` | `false` | Sets scrolled elevation/color treatment when container content scrolls under the bar. |

### Slots

| Slot Name | Description |
| :--- | :--- |
| `(default)` | Main screen title text or primary app bar heading. |
| `subtitle` | Secondary text displayed below the title (active in `md` and `lg` sizes). |
| `leading` | Leading icon button slot (e.g., navigation drawer trigger or back arrow). |
| `trailing` | Trailing action icons or contextual menu controls. |
| `search` | Embedded search input element when `variant="search"`. |

### Events

| Event | Type | Description |
| :--- | :--- | :--- |
| `@scrollstatechange` | `CustomEvent` | Fired when the app bar transitions between pinned and scrolled visual states. |

## CSS Classes & Utility Styling

```javascript
import appBarStylesheet from '@material/web/labs/gb/components/appbar/app-bar.css' with {type: 'css'};
```

* `.app-bar`: Root container class.
* `.app-bar-sm`: Small layout modifier.
* `.app-bar-md`: Medium layout modifier.
* `.app-bar-lg`: Large layout modifier.
* `.app-bar-with-subtitle`: Subtitle layout modifier.
* `.app-bar-search`: Search layout modifier.
* `.app-bar-scrolled`: Scrolled state class.

## Usage Examples

### Standard Small App Bar

```html
<md-gb-app-bar size="sm">
  <md-gb-icon-button slot="leading" aria-label="Open menu">
    <md-gb-icon>menu</md-gb-icon>
  </md-gb-icon-button>
  Agent Control Center
  <md-gb-icon-button slot="trailing" aria-label="Notifications">
    <md-gb-icon>notifications</md-gb-icon>
  </md-gb-icon-button>
</md-gb-app-bar>
```

### Medium App Bar with Subtitle

```html
<md-gb-app-bar size="md">
  <md-gb-icon-button slot="leading" aria-label="Go back">
    <md-gb-icon>arrow_back</md-gb-icon>
  </md-gb-icon-button>
  Fleet Overview
  <span slot="subtitle">12 active autonomous agents</span>
  <md-gb-icon-button slot="trailing" aria-label="Filter fleet">
    <md-gb-icon>filter_list</md-gb-icon>
  </md-gb-icon-button>
</md-gb-app-bar>
```

### Search Variant App Bar

```html
<md-gb-app-bar variant="search">
  <md-gb-icon-button slot="leading" aria-label="Search">
    <md-gb-icon>search</md-gb-icon>
  </md-gb-icon-button>
  <input slot="search" type="search" placeholder="Search prompts and logs..." style="background: transparent; border: none; font: var(--md-sys-typescale-body-large); color: var(--md-sys-color-on-surface); width: 100%; outline: none;" />
  <md-gb-icon-button slot="trailing" aria-label="Voice input">
    <md-gb-icon>mic</md-gb-icon>
  </md-gb-icon-button>
</md-gb-app-bar>
```
