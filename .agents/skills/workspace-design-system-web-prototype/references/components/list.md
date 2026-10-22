# List (`<md-gb-list>` & `<md-gb-list-item>`)

Lists (`<md-gb-list>` and `<md-gb-list-item>`) organize related data, options, actions, and settings in single or multi-line vertical rows.

## Import

```javascript
import '@material/web/labs/gb/components/list/md-gb-list.js';
import '@material/web/labs/gb/components/list/md-gb-list-item.js';
```

## API Reference

### `<md-gb-list>` Attributes and Properties

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `segmented` / `.segmented` | `boolean` | `false` | When true, renders list items as separated, rounded segmented blocks. |

### `<md-gb-list-item>` Attributes and Properties

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `checked` / `.checked` | `boolean` | `false` | Selected state of the list item. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables interaction and darkens text contrast. |
| `static` / `.nonInteractive` | `boolean` | `false` | Disables hover and active state layers for non-interactive list content. |

### `<md-gb-list-item>` Slots

| Slot Name | Description |
| --- | --- |
| `(default)` | Primary list item headline text. |
| `slot="avatar"` | Avatar graphic, user initials (1-2 characters), or thumbnail image. |
| `slot="leading"` | Leading icon or graphic element preceding primary text. |
| `slot="overline"` | Small uppercase header text displayed above the main text. |
| `slot="supporting-text"` | Secondary description text displayed below the main text. |
| `slot="trailing-text"` | Timestamp, count, or metadata text aligned to the trailing end. |
| `slot="trailing"` | Trailing action icon button, checkbox, radio, or switch control. |

### CSS Classes

```javascript
import listStylesheet from '@material/web/labs/gb/components/list/list.css' with {type: 'css'};
```

| Class | Type | Description |
| --- | --- | --- |
| `.list` | Root | List container class. |
| `.list-segmented` | Modifier | Segmented list layout modifier. |
| `.list-item` | Root | List item row class. |
| `.list-item-static` | Modifier | Non-interactive row modifier. |
| `.list-item-content`, `.list-item-leading`, `.list-item-trailing`, `.list-item-overline`, `.list-item-supporting-text`, `.list-item-trailing-text`, `.list-item-avatar` | Parts | Structural child parts. |

## Usage Examples

### Basic and Rich Content List Items

```html
<md-gb-list>
  <!-- Basic Item -->
  <md-gb-list-item>Basic Text Item</md-gb-list-item>

  <!-- Leading Icon -->
  <md-gb-list-item>
    <md-gb-icon slot="leading">star</md-gb-icon>
    Starred Item
  </md-gb-list-item>

  <!-- Avatar & Supporting Text -->
  <md-gb-list-item>
    <span slot="avatar" class="w-10 h-10 rounded-full bg-primary-container text-on-primary-container flex items-center justify-center font-medium">
      JD
    </span>
    Jane Doe
    <span slot="supporting-text">Agent Manager • Active</span>
  </md-gb-list-item>

  <!-- Overline, Supporting Text, Trailing Metadata, and Action -->
  <md-gb-list-item style="align-items: start;">
    <md-gb-icon slot="leading">folder</md-gb-icon>
    <span slot="overline">SYSTEM LOGS</span>
    Autonomous Thread Activity
    <span slot="supporting-text">Executed 142 background processing tasks</span>
    <span slot="trailing-text">2m ago</span>
    <md-gb-icon slot="trailing">chevron_right</md-gb-icon>
  </md-gb-list-item>

  <!-- Selected Item -->
  <md-gb-list-item checked>
    <md-gb-icon slot="leading">check</md-gb-icon>
    Selected Row Item
  </md-gb-list-item>
</md-gb-list>
```

### Segmented List Variant

```html
<md-gb-list segmented>
  <md-gb-list-item>
    <md-gb-icon slot="leading">wifi</md-gb-icon>
    Wi-Fi Network
    <span slot="supporting-text">Connected to Workspace-5G</span>
  </md-gb-list-item>
  <md-gb-list-item>
    <md-gb-icon slot="leading">bluetooth</md-gb-icon>
    Bluetooth
    <span slot="supporting-text">On</span>
  </md-gb-list-item>
</md-gb-list>
```
