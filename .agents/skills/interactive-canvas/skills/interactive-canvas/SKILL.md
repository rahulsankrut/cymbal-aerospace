---
name: interactive-canvas
description: Teaches the agent how to create and update rich, interactive Generative UI canvases that render in the Jetski Auxiliary Pane with buttons, text field dispatchers, and multimodal audio recording buttons that send instructions directly back to the agent with field attribution.
---

# Interactive Generative Canvas

Use this skill when you want to present an interactive graphical dashboard,
form, task board, control panel, workflow stepper, or multimodal recording
interface to the user with actionable buttons and text field dispatchers that
feed directly back into the conversation.

## Workflow

### 1. Write the Canvas HTML File

Always write the HTML file to the active conversation's scratch directory:
`<appDataDir>/brain/<conversation-id>/scratch/canvas.html`

Use standard HTML with Tailwind CSS and CSS variables. Canvases are strictly
conversation-scoped: each conversation owns its own canvas. Never write to
global paths or attempt to share a single canvas across multiple conversations.

#### HTML5 UTF-8 & Anti-FOUC Boilerplate Rules

*   **Complete HTML5 Document**: Always write a full HTML5 document with
    `<!DOCTYPE html>`, `<html lang="en">`, and `<meta charset="UTF-8">` to
    prevent UTF-8 emojis and icons from rendering as garbled mojibake.
*   **Tailwind Script & Anti-FOUC Inline Style**: You MUST use the internal gstatic Tailwind script
    (`https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js`). **NEVER use the public `https://cdn.tailwindcss.com`**.
    Because the script loads asynchronously, you MUST include an inline `<style>` tag in `<head>`
    *before* the `<script>` tag locking `background-color` and `color` to host
    CSS variables to prevent dark/light background flashing (FOUC) on
    hot-reloads:

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <style>
        html, body {
          background-color: var(--background, #f9fafb) !important;
          color: var(--foreground, #111827) !important;
        }
      </style>
      <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
    </head>
    <body>
      <!-- Canvas content -->
    </body>
    </html>
    ```

*   **Direct File Writes**: ALWAYS use `write_to_file` with `Overwrite: true` directly
    to create or update `canvas.html` (which automatically creates parent
    directories) without running `mkdir -p` beforehand. Do not use `Overwrite: false`.

*   **External Links**: For external links (such as `http://cl/...` or
    `http://b/...`), always include `target="_blank"` so they open in a new
    browser tab rather than navigating inside the sidecar iframe.

*   **Stateful Interactive Apps**: For interactive apps, dashboards, and games,
    always render the full application state inside `canvas.html` and update
    `canvas.html` on every turn rather than replying only in chat. When updating state,
    **rewrite the entire `canvas.html` file using `write_to_file`**. Do not write fragile Python regex scripts to mutate existing HTML.

*   **Compact UI & Horizontal Scrolling**: The Jetski Auxiliary Pane has a
    restricted width. To prevent horizontal scrolling, keep tab labels and
    button names extremely short (e.g., 1 word + a compact numerical badge like
    `Proposals 3`). Avoid verbose labels like "Requirements Ledger" if "Ledger"
    suffices.

### 2. Action Buttons & Programmatic Dispatch

Any button with `data-action="..."` or `data-prompt="..."` will automatically
send that text to the active conversation when clicked:

```html
<button
  data-action="Run blaze test //path/to:target"
  class="px-4 py-2 bg-[var(--primary,#0B57D0)] text-white font-medium rounded-lg hover:brightness-110 active:scale-95 transition-all">
  Run Target Tests
</button>
```

#### Programmatic JavaScript Dispatch (`window.sendToAgent`)

When client-side JavaScript needs to run custom logic before messaging the agent
(for example, removing a DOM item, running animations, or rolling dice before
dispatching the prompt), call the bridge helper directly instead of creating
hidden `<input>`/`<button>` DOM hacks:

```javascript
await window.sendToAgent(prompt, btnElement, targetConversationId);
```

*   `prompt` (`string`): The instruction text to send to the agent.
*   `btnElement` (`HTMLElement | null`, optional): The button element that
    triggered the action (used by the bridge to show loading/sent visual
    feedback).
*   `targetConversationId` (`string | undefined`, optional): Specific subagent
    conversation ID to route the message to; omit to send to the active main
    conversation.

### 3. Multiple Text Field Dispatchers (`data-field-name`)

When a canvas contains text fields or distinct command dispatchers, tag each
input with `data-field-name="..."` (or `data-field="..."` /
`data-source="..."`):

```html
<div data-dispatcher class="flex gap-2">
  <input
    type="text"
    data-field-name="Buganizer Triage"
    placeholder="e.g. b/123456789..."
    class="...">
  <button data-dispatcher-send class="...">Triage</button>
</div>
```

*   **Field Attribution**: When the user presses **Enter** or clicks the
    adjacent `data-dispatcher-send` button, the prompt sent to the agent is
    automatically attributed with the field identifier: `[Buganizer Triage]
    b/123456789`
*   **Custom Action Templates**: You can also provide
    `data-action-template="Please inspect bug {value}"` to format custom
    sentences.
*   **Auto-Clear**: The input field automatically clears upon sending.

### 4. Multimodal Audio Recording (`data-record-audio`)

To allow users to record spoken voice instructions directly from the canvas:

```html
<button
  data-record-audio
  data-field-name="Voice Task Dispatcher"
  class="px-4 py-2 bg-rose-600 hover:bg-rose-500 text-white rounded-xl">
  🎤 Record Voice Note
</button>
```

**How Voice Recording Operates:**

1.  Clicking toggles between Start and Stop with a live duration timer (`⏹ Stop
    (00:05)`).
2.  On stop, the recorded audio is saved to:
    `<appDataDir>/brain/<conversation-id>/scratch/recordings/audio_<timestamp>.webm`
3.  The bridge automatically sends an attributed prompt to the agent: `[Voice
    Input: <fieldName>] An audio message was recorded from the interactive
    canvas and saved to file://<absPath>. Please use the view_file tool to
    listen to and inspect this audio file, and respond to the user's request.`
4.  **Agent Action Required**: When this message arrives, the agent **MUST**
    call `view_file` on `file://<absPath>` (without `StartLine` or `EndLine`, as
    per binary audio rules) to listen to the user's audio and fulfill their
    request.

### 5. Target Specific Conversations (Subagents)

By default, all actions and messages triggered from the canvas are dispatched to
the active main conversation. If you have created subagents and want specific UI
elements to route instructions directly to them, add the
`data-target-conversation="<conversation-id>"` attribute to your interactive
elements.

**Action Buttons targeting a subagent:**

```html
<button data-action="Analyze these logs" data-target-conversation="subagent-id-1234">
  Send to Subagent
</button>
```

**Text Dispatchers targeting a subagent:**

```html
<input type="text" data-field-name="Query" data-target-conversation="subagent-id-1234">
```

**Audio Recording targeting a subagent:**

```html
<button data-record-audio data-target-conversation="subagent-id-1234">
  🎤 Voice for Subagent
</button>
```

#### Best Practice: Multi-Subagent Dashboard & Partials Architecture

When orchestrating multiple subagents or concurrent swarm workers that report
into a single unified dashboard:

> [!WARNING] **Concurrent Write Limitation:** Concurrent swarm workers must
> NEVER write directly to `canvas.html`. Writing concurrently causes race
> conditions resulting in corrupted HTML/JSON and triggering `cortex tool
> view_file` errors for other workers attempting to read it.

*   **Combine Preset Actions + Custom Dispatchers**: Include both preset
    `data-action` buttons (for common one-click commands) and a custom
    `data-dispatcher` text input on each subagent item card, all tagged with
    `data-target-conversation="<subagent-conversation-id>"`.

*   **Standardize the "Partials" Architecture**: In a swarm or concurrent
    execution context, workers should write their own isolated HTML fragments
    into a safe directory (e.g., `scratch/partials/<worker-id>.html`). The main
    parent orchestrator agent or a dedicated UI background loop is then solely
    responsible for safely stitching these fragments together and rendering the
    final `canvas.html` file to prevent write collisions. Have each subagent
    write its own standalone HTML card partial to its own sandboxed scratch
    directory:
    `<appDataDir>/brain/<subagent-conversation-id>/scratch/partials/<item-id>.html`.
    Then have the parent orchestrator's glue script read across subagent
    directories (running with `BypassSandbox: true`) to assemble the composite
    `<appDataDir>/brain/<parent-conversation-id>/scratch/canvas.html`.

*   **Idempotent Glue Writes**: In any background glue loop that combines
    partials into `canvas.html`, **always** compare the newly assembled HTML
    against the existing file content before writing (`if new_html !=
    existing_html:`). Only write `canvas.html` when content actually changes to
    prevent constant iframe reloads and UI flicker.

### 6. Mandatory Sidecar Pill Button

Whenever you create, update, or reference the interactive canvas, you **MUST**
include the one-click `sidecar://` pill button in your response scoped with the
active conversation ID so the Auxiliary Pane opens the canvas specifically for
the current conversation:

```markdown
[Interactive UI Canvas](sidecar://interactive-gen-ui/canvas/?conversationId=<conversation-id>)
```

Replace `<conversation-id>` with the active conversation ID. In the Jetski UI,
this markdown link renders as a clickable button/pill that toggles the panel
directly for that conversation.

*   **Never Replace the `sidecar://` Pill with a `file://` Link**: Never link to
    `file://.../scratch/canvas.html` in chat or create a `.url.json` artifact
    for `canvas.html` in place of `[Interactive UI
    Canvas](sidecar://interactive-gen-ui/canvas/?conversationId=<conversation-id>)`.

### 7. Automatic Hot-Reload

When you update `<appDataDir>/brain/<conversation-id>/scratch/canvas.html`, the
canvas automatically detects the modification and reloads the view in real-time.
You do not need to instruct the user to refresh.

### 8. Empty State On-Demand Request

When the user opens the Interactive UI Canvas panel and no canvas exists yet for
the active conversation, an empty state is displayed with a button to request
canvas creation. When the user clicks this button, an instruction message is
dispatched directly to the agent in the active conversation:

-   Informs the agent that the user requested an interactive canvas.
-   Specifies the exact target path
    (`<appDataDir>/brain/<conversation-id>/scratch/canvas.html`).
-   Details how to structure the HTML with interactive action buttons
    (`data-action`), text dispatchers (`data-dispatcher`), and audio recording
    (`data-record-audio`).

When you receive this instruction, promptly generate a relevant canvas for the
user's ongoing task.

### 9. Periodic Auto-Refresh (`canvas.config.json`)

Active dashboards can optionally be configured to periodically ping the agent to
refresh the dashboard data.

-   **Explicit User Opt-In Only**: **Never** create `canvas.config.json` by
    default. Only create or enable this file when the user explicitly asks for
    periodic dashboard updates (e.g., *"refresh this dashboard every 30
    minutes"*), or when a skill invoked by the user explicitly requires it.
-   **Config File Path**:
    `<appDataDir>/brain/<conversation-id>/scratch/canvas.config.json`
-   **Example Configuration (every 30 minutes)**:

```json
{
  "enabled": true,
  "intervalSeconds": 1800,
  "prompt": "[Interactive Canvas Auto-Refresh] Please refresh the dashboard data and update scratch/canvas.html."
}
```

-   **Fields**:
    -   `enabled` (`boolean`): Whether periodic auto-refresh pings are active
        for this conversation's dashboard. Set to `false` (or delete the file)
        when the user asks to stop auto-refreshing.
    -   `intervalSeconds` (`number`): How often to ping the agent in seconds
        (minimum `30` seconds; e.g. `1800` for 30 minutes). `intervalMinutes`
        (e.g. `30`) is also accepted as a convenience.
    -   `prompt` (`string`): The configurable instruction message sent to the
        agent when the interval elapses. Customize this prompt to match the
        specific dashboard's refresh workflow.
-   **How It Works**:
    -   The sidecar monitors active dashboards that have both
        `scratch/canvas.html` and an enabled `scratch/canvas.config.json`.
    -   The interval timer is measured from the latest of the last ping sent,
        the last `canvas.html` modification, or the last `canvas.config.json`
        modification (`Math.max(lastPingMs, canvasMtimeMs, configMtimeMs)`),
        preventing duplicate pings while a refresh is in progress.

### 10. File-Based JSON Event Queue (`scratch/inputs/`) & Pending State (`data-pending-*`)

For stateful dashboards where users may click multiple buttons or submit
multiple items rapidly while the agent is busy, use the file-based JSON event
queue (`data-event`) instead of direct chat messages. Every user click or input
submission is written to disk as a timestamped JSON event file in
`<appDataDir>/brain/<conversation-id>/scratch/inputs/`, and the agent receives a
debounced wakeup notification (`[Canvas Input Queue] New input event(s) arrived
in scratch/inputs/. Please process and delete them.`).

#### Mandatory Explicit `id` Attribute

Every interactive element that uses the file-based event queue **MUST** carry a
unique, explicit `id` attribute (e.g., `id="btn-approve-prop-1"` or
`id="input-feedback-prop-1"`). No fallback IDs are auto-generated: if an element
with `data-event` lacks an `id`, the bridge displays an error toast (`Element
requires a unique id attribute`) and `POST /api/event` rejects the request with
HTTP 400.

#### Queued Action Buttons & Dispatcher Inputs (`data-event`)

Add `data-event="<EventName>"` alongside a unique `id` on buttons or
`[data-dispatcher]` inputs:

```html
<!-- Queued Action Button -->
<button
  id="btn-approve-item-1"
  data-event="ApproveProposal"
  data-action="Approve proposal #1"
  class="px-4 py-2 bg-emerald-600 text-white rounded-lg">
  ✅ Approve Proposal #1
</button>

<!-- Queued Text Dispatcher -->
<div data-dispatcher class="flex gap-2">
  <input
    id="input-comment-item-1"
    type="text"
    data-event="ProposalComment"
    data-field-name="Proposal #1 Feedback"
    placeholder="Add feedback...">
  <button id="btn-send-comment-item-1" data-dispatcher-send>Send</button>
</div>
```

When triggered, the sidecar writes
`<appDataDir>/brain/<conversation-id>/scratch/inputs/event_<timestamp>_<safeId>.json`:

```json
{
  "id": "btn-approve-item-1",
  "eventName": "ApproveProposal",
  "timestamp": 1760000000000,
  "action": "Approve proposal #1",
  "fieldName": null,
  "inputValue": null,
  "payload": {}
}
```

#### Pending / Processing DOM State Synchronization (`data-pending-*`)

1.  **Immediate Tagging on Click**: As soon as the user clicks a `data-event`
    element (or submits a queued `data-dispatcher` input), the client bridge
    immediately sets `data-pending-state="processing"`,
    `data-pending-event="<eventName>"`, and `data-pending-ts="<timestamp>"` on
    that DOM element (`#<id>`) and on any ancestor card marked with
    `data-card-id`.
2.  **Automatic Hydration Across Reloads (`GET /api/inputs`)**: On page load and
    after every hot-reload, the bridge queries `GET
    /api/inputs?conversationId=<conversation-id>` to read all unprocessed
    `event_*.json` files still present in `scratch/inputs/`. For each pending
    event, it finds `document.getElementById(evt.id)` and re-applies
    `data-pending-state="processing"`, `data-pending-event`, and
    `data-pending-ts` so the "processing" visual indicator survives reloads
    until the agent finishes processing and deletes the event file.
3.  **Recommended CSS Styling**: Include a CSS rule in `<head>` to visually
    indicate elements that are queued and awaiting agent processing:

    ```css
    [data-pending-state="processing"] {
      opacity: 0.65 !important;
      pointer-events: none;
      position: relative;
      outline: 2px dashed #f59e0b;
    }
    ```

#### Agent Consumption & Cleanup Rules (`view_file` + Delete)

When you receive a `[Canvas Input Queue]` notification (or during a dashboard
refresh turn):

1.  **Inspect Pending Events Directly with `view_file`**: Wakeup pings contain
    the exact `file://` paths of pending events. Never run custom helper scripts
    to parse or discover queue items. Call `view_file` directly on the provided
    event paths in chronological (`timestamp`) order. Running `ls` on the queue
    directory is fine to verify that all event notifications were processed and
    deleted so none are forgotten or left behind.
2.  **Update `scratch/canvas.html` First**: Apply the state transitions
    requested by the events and write the updated
    `<appDataDir>/brain/<conversation-id>/scratch/canvas.html` first before
    deleting any processed event files.
3.  **Delete Processed Event Files & Verify with `ls`**: Immediately after
    updating `canvas.html`, delete the processed `event_*.json` files from
    `<appDataDir>/brain/<conversation-id>/scratch/inputs/` (e.g., via `rm`).
    Deleting a file removes it from `GET /api/inputs`, clearing the
    `data-pending-state="processing"` state on the hot-reloaded canvas.
    Running `ls` confirms that all notifications were processed and deleted and
    none were missed.
