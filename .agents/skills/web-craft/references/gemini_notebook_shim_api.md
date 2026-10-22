{{#if enableHtmlNappsShimApi}}

# Gemini Notebook Shim API — State Persistence

When generating HTML artifacts, your code runs inside a sandboxed iframe.
Browser storage APIs (`localStorage`, `sessionStorage`, `IndexedDB`, cookies)
**will NOT persist** across sessions. Instead, use the `notebookAppApi` shim.

**CRITICAL REQUIREMENT:** To enable this API, you MUST include the tag
`<api-shim></api-shim>` inside the `<body>` of your generated HTML (place it
just before your main `<script>` block). The host system will dynamically
replace this tag with the JavaScript shim that provides `window.notebookAppApi`.

<!-- LINT.IfChange(shim_api) -->

## Available APIs

```
window.notebookAppApi = {
  API_VERSION: '1.0',
  clientType: 'notebooklm-web' | 'notebooklm-mobile',

  // --- State Persistence (drop-in replacement for localStorage) ---
  setAppState(state: object): Promise<void>
  getAppState(): Promise<object | null>

  // --- Lifecycle ---
  notifyAppReady(): void

  // --- File Export ---
  triggerFileDownload({ content, contentType, encoding, filename }): void
}
```

<!-- LINT.ThenChange(//depot/google3/labs/language/tailwind/frontend/shared/components/app_viewer/app_viewer_component_store.ts:html_file_artifact_allowed_actions) -->

## State Persistence — CRITICAL

Use `setAppState` / `getAppState` instead of any browser storage. This is a
free-form key-value store: you decide the schema at generation time based on
what the app needs (e.g., user progress, completed modules, quiz scores,
checklist selections, customized calculator inputs, simulation save states).

**Pattern — always load state on startup, save on change:**

```javascript
// On app initialization
const state = await window.notebookAppApi.getAppState();
if (state) {
  // Restore: e.g., state.currentCard, state.score, state.completedLessons, state.userEdits
  restoreFromState(state);
}

// Whenever state/progress changes (e.g., user answers a question, checks a box, moves to next card)
await window.notebookAppApi.setAppState({
  currentCard: 3,
  score: 7,
  completedLessons: ['intro', 'module_1'],
  userEdits: { ... }
});
```

`setAppState()` accepts lightweight JSON-serializable state objects (strings,
numbers, booleans, arrays, nested objects) up to **256 KiB** with a maximum
nesting depth of **32**. You define the schema based on what the app needs.

**Payload Restrictions — NEVER store images or binary data in `setAppState()`:**

*   The host and backend strictly reject payloads containing raster images or
    binary blobs:
    *   `data:image/*` (except vector `image/svg+xml`) or
        `data:application/octet-stream` data URIs
    *   Base64-, base64url-, double-base64-, or hex-encoded image binaries (PNG,
        JPEG, GIF, WebP, BMP, ICO, AVIF, TIFF)
    *   Raw byte arrays (`[137, 80, 78, 71, ...]`) or binary string buffers
*   Instead of calling `canvas.toDataURL()`, `FileReader.readAsDataURL()`, or
    saving encoded image strings into `setAppState()`, persist compact
    **structural parameters** (e.g., coordinates, stroke paths, color tokens,
    selected icon IDs, or configuration state) and re-render visuals on load.

**Always design for two states:** an **empty state** for first-time visitors (a
short explanation of what will appear and a clear first-entry prompt) and a
**populated state** for returning users (history feed, trend charts, streak
counters, quick-add actions). Consider offering a simple "Export Data" or
"Reset" option.

**Do NOT use:** `localStorage`, `sessionStorage`, `IndexedDB`, `document.cookie`
— they will not persist across sessions in the sandbox.

## App Ready Signal

Call `notifyAppReady()` after your app has fully rendered. The host shows a
loading spinner until this is called:

```javascript
// After all DOM setup
window.notebookAppApi.notifyAppReady();
```

## Platform Detection

Use `clientType` to adjust layout for mobile vs web:

```javascript
if (window.notebookAppApi.clientType === 'notebooklm-mobile') {
  // Adjust touch targets, font sizes, etc.
}
```

## File Export

Trigger a download for the user:

```javascript
window.notebookAppApi.triggerFileDownload({
  content: csvString,
  contentType: 'text/csv',
  encoding: 'UTF-8',
  filename: 'results.csv'
});
```

Allowed content types: `text/plain`, `text/csv`, `image/png`. Allowed encodings:
`UTF-8`, `base64`.

{{/if}}
