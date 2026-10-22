# List (`<md-gb-list>`, `<md-gb-list-item>`)

The `<md-gb-list>` and `<md-gb-list-item>` components render continuous vertical indexes of text, icons, avatars, overlines, supporting copy, and selection controls.

## Import

```javascript
import '@material/web/labs/gb/components/list/md-gb-list.js';
import '@material/web/labs/gb/components/list/md-gb-list-item.js';
```

## API Reference

### `<md-gb-list>` Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `segmented` / `.segmented` | `boolean` | `false` | When true, renders list items in a segmented container card style with rounded corners and item dividers. |

### `<md-gb-list-item>` Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `checked` / `.checked` | `boolean` | `false` | Selected state of the list item. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables interaction and dims item. |
| `static` / `.nonInteractive` | `boolean` | `false` | Removes hover/pressed interactive feedback when item is read-only content. |

### `<md-gb-list-item>` Slots

| Slot Name | Description |
| :--- | :--- |
| `(default)` | Headline / main text label of the list item. |
| `avatar` | 1-2 character text avatar or image thumbnail before main text. |
| `leading` | Leading icon or checkbox/radio control before main text. |
| `overline` | Small overline text displayed above main text. |
| `supporting-text` | Secondary description copy displayed below main text. |
| `trailing-text` | Metadata or timestamp text displayed at end of item. |
| `trailing` | Trailing action icon button or disclosure chevron. |

## CSS Classes & Utility Styling

```javascript
import listStylesheet from '@material/web/labs/gb/components/list/list.css' with {type: 'css'};
```

* `.list`: Root list container.
* `.list-segmented`: Segmented modifier.
* `.list-item`: Item container element.
* `.list-item-static`: Non-interactive item modifier.
* `.list-item-content`, `.list-item-leading`, `.list-item-trailing`, `.list-item-overline`, `.list-item-supporting-text`, `.list-item-trailing-text`, `.list-item-avatar`: Child element parts.

## Usage Examples

### Basic Interactive List

```html
<md-gb-list>
  <md-gb-list-item>
    <md-gb-icon slot="leading">inbox</md-gb-icon>
    Primary Inbox
    <span slot="trailing-text">24</span>
  </md-gb-list-item>

  <md-gb-list-item>
    <md-gb-icon slot="leading">star</md-gb-icon>
    Starred Prompts
  </md-gb-list-item>

  <md-gb-list-item disabled>
    <md-gb-icon slot="leading">block</md-gb-icon>
    Archived Workspace
    <span slot="supporting-text">Permission required</span>
  </md-gb-list-item>
</md-gb-list>
```

### Rich List Item with Avatar & Overline

```html
<md-gb-list>
  <md-gb-list-item style="align-items: start;">
    <span slot="avatar" class="bg-primary-container text-on-primary-container flex items-center justify-center rounded-full w-10 h-10 font-bold">A</span>
    <span slot="overline">SYSTEM ALERT</span>
    Agent Fleet Alpha
    <span slot="supporting-text">Autonomous optimization completed with 99.8% precision rate.</span>
    <span slot="trailing-text">2m ago</span>
    <md-gb-icon slot="trailing">chevron_right</md-gb-icon>
  </md-gb-list-item>
</md-gb-list>
```

### Segmented List Container

```html
<md-gb-list segmented>
  <md-gb-list-item checked>
    <md-gb-icon slot="leading">check_circle</md-gb-icon>
    Active Model: Gemini 1.5 Pro
  </md-gb-list-item>
  <md-gb-list-item>
    <md-gb-icon slot="leading">radio_button_unchecked</md-gb-icon>
    Fallback Model: Gemini 1.5 Flash
  </md-gb-list-item>
</md-gb-list>
```
