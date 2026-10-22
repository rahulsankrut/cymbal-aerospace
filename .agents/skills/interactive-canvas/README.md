# Interactive Generative UI Plugin

A general-purpose **Interactive Generative UI** plugin for Jetski and
Antigravity that renders agent-generated HTML in the Auxiliary Pane
(`SIDECAR_UI_ENTRYPOINT_AUX_PANE`) and connects button clicks back into the
agent conversation loop.

## Architecture

1.  **Sidecar Web Server (`sidecars/canvas/`)**:
    -   Listens on the port assigned by Jetski (`ANTIGRAVITY_SIDECAR_WEB_PORT`).
    -   Automatically injects the frontend bridge (`preload.js` + action event
        interceptor).
    -   Serves the active conversation's canvas from:
        `~/.gemini/jetski/brain/<conversationId>/scratch/canvas.html`
    -   Automatically polls modification timestamps and hot-reloads the view
        whenever the agent rewrites `canvas.html`.
2.  **Action Interceptor (`data-action`)**:
    -   Intercepts clicks on `<button data-action="...">` or `<button
        data-prompt="...">`.
    -   Dispatches the prompt directly via
        `window.sidecar.agent.sendMessage(actionPrompt)`.
    -   Posts to `/_sidecar/send-message`, which invokes `agentapi send-message
        <convId>` to prompt the agent.
3.  **Companion Skill (`skills/interactive-canvas/`)**:
    -   Instructs the agent on structuring HTML, designing Tailwind UI with host
        theme variables, adding action buttons, and emitting
        `sidecar://interactive-gen-ui/canvas/?conversationId=<conversationId>`
        links.
    -   Enforces strict conversation isolation: every canvas is uniquely scoped
        to its conversation and never leaks to other conversations.
4.  **Configurable Periodic Auto-Refresh (`scratch/canvas.config.json`)**:

    -   When explicitly requested by the user, an active dashboard can have an
        associated config file at
        `~/.gemini/jetski/brain/<conversationId>/scratch/canvas.config.json`:

        ```json
        {
          "enabled": true,
          "intervalSeconds": 1800,
          "prompt": "[Interactive Canvas Auto-Refresh] Please refresh the dashboard data and update scratch/canvas.html."
        }
        ```

    -   The sidecar periodically pings the conversation with the configured
        `prompt` once `intervalSeconds` (e.g., `1800`s = 30 minutes) has elapsed
        since the last update or ping.

## Quick Start

1.  Open the **UI Plugins** tab on the left sidebar in Jetski Web or Antigravity
    and toggle **Interactive Generative UI** to **Enabled**.
2.  Open the Auxiliary Pane by clicking **+** (Plugins) -> **Interactive UI** ->
    **Canvas**, or click `[Open Interactive
    Canvas](sidecar://interactive-gen-ui/canvas/?conversationId=<conversationId>)`.
3.  When the agent writes `canvas.html`, the canvas updates immediately and
    buttons trigger live agent actions.
