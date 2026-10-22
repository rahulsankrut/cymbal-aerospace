# App Bar (`<md-gb-app-bar>`)

The App Bar (`<md-gb-app-bar>`) provides top or bottom application bars for screen titles, navigation actions, search inputs, and contextual controls.

## Import

```javascript
import '@material/web/labs/gb/components/appbar/md-gb-app-bar.js';
```

When using icon buttons within the app bar, also import `<md-gb-icon-button>` and `<md-gb-icon>`:

```javascript
import '@material/web/labs/gb/components/iconbutton/md-gb-icon-button.js';
import '@material/web/labs/gb/styles/icon/md-gb-icon.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `size` / `.size` | `'sm' \| 'md' \| 'lg'` | `'sm'` | Height and typographic scale variant. |
| `variant` / `.variant` | `'standard' \| 'search'` | `'standard'` | Display mode variant. |
| `scrolled` / `.scrolled` | `boolean` | `false` | Reflects whether the container is scrolled, updating container surface styling. |

### Slots

| Slot Name | Description |
| --- | --- |
| `(default)` | Primary title text for the screen or section. |
| `slot="subtitle"` | Subtitle text displayed beneath title (supported in `md` and `lg` sizes). |
| `slot="leading"` | Leading navigation icon button (e.g. menu or back button). |
| `slot="trailing"` | Trailing action controls or icon buttons. |
| `slot="search"` | Slotted search field container when `variant="search"`. |

### Events

| Event Name | Type | Description |
| --- | --- | --- |
| `@scrollstatechange` | `CustomEvent` | Fired when the app bar scroll elevation state changes. |

### CSS Classes

```javascript
import appBarStylesheet from '@material/web/labs/gb/components/appbar/app-bar.css' with {type: 'css'};
```

| Class | Type | Description |
| --- | --- | --- |
| `.app-bar` | Root | Component root style. |
| `.app-bar-sm` | Modifier | Small size variant. |
| `.app-bar-md` | Modifier | Medium size variant. |
| `.app-bar-lg` | Modifier | Large size variant. |
| `.app-bar-with-subtitle` | Modifier | Applied when subtitle slot is populated. |
| `.app-bar-search` | Modifier | Search variant styling. |
| `.app-bar-scrolled` | Modifier | Scrolled surface elevation style. |

## Usage Examples

### Standard Small App Bar

```html
<md-gb-app-bar size="sm">
  <md-gb-icon-button slot="leading" aria-label="Open menu">
    <md-gb-icon>menu</md-gb-icon>
  </md-gb-icon-button>
  Agent Control Center
  <div slot="trailing" class="flex gap-1">
    <md-gb-icon-button aria-label="Notifications">
      <md-gb-icon>notifications</md-gb-icon>
    </md-gb-icon-button>
    <md-gb-icon-button aria-label="Settings">
      <md-gb-icon>settings</md-gb-icon>
    </md-gb-icon-button>
  </div>
</md-gb-app-bar>
```

### Medium App Bar with Subtitle

```html
<md-gb-app-bar size="md">
  <md-gb-icon-button slot="leading" aria-label="Back">
    <md-gb-icon>arrow_back</md-gb-icon>
  </md-gb-icon-button>
  Fleet Overview
  <span slot="subtitle">12 active autonomous agents</span>
  <md-gb-icon-button slot="trailing" aria-label="Filter">
    <md-gb-icon>filter_list</md-gb-icon>
  </md-gb-icon-button>
</md-gb-app-bar>
```

### Search Variant App Bar

```html
<md-gb-app-bar variant="search">
  <md-gb-icon-button slot="leading" aria-label="Back">
    <md-gb-icon>arrow_back</md-gb-icon>
  </md-gb-icon-button>
  <div slot="search" class="w-full">
    <input type="text" placeholder="Search workspace..." class="w-full bg-transparent outline-none text-on-surface" />
  </div>
  <md-gb-icon-button slot="trailing" aria-label="Clear search">
    <md-gb-icon>close</md-gb-icon>
  </md-gb-icon-button>
</md-gb-app-bar>
```
