---
name: jetski-sidecars
description: >-
  Builds, configures, deploys, and troubleshoots custom Jetski sidecars,
  background services, and auxiliary pane UI web extensions. Use when a user
  asks to build an interactive HTML explainer, create a Jetski dashboard, deploy
  a background or UI sidecar, or embed Google Drive files in a side panel. Don't
  use for g3doc previews, generic Python server development, or non-Jetski web
  applications.
---

# Jetski Sidecars

## Developing a UI Sidecar

Create configuration and web server files inside the target sidecar directory:
`~/.gemini/config/sidecars/<sidecar_name>/`.

### 1. Sidecar Configuration (`sidecar.json`)

The configuration file defines how Jetski discovers, names, and renders the
sidecar. See the [reference sidecar manifest](references/sidecar_template.json)
for a complete example.

Key UI and naming fields:

*   `has_web_ui`: Set to `true` to enable web server port injection.
*   `display_name` (Top-Level): Friendly name displayed in the sidecars
    management/settings list and lifecycle logs.
*   `ui_config.display_name`: Label for the sidecar tab set header.
*   `ui_config.views[].title`: **Primary visible title** rendered directly on
    the auxiliary pane tab and extension dropdown menu in Jetski Web. Provide a
    concise, meaningful title (e.g., `"Explainer View"`).
*   `ui_config.views[].entrypoint`: Set to `"SIDECAR_UI_ENTRYPOINT_AUX_PANE"` to
    render in the auxiliary side panel.

### 2. Runtime Environment Injections

`SidecarManager` injects the following environment variables into every spawned
sidecar process:

*   `ANTIGRAVITY_SIDECAR_WEB_PORT`: Allocated port for HTTP server binding.
*   `ANTIGRAVITY_EXECUTABLE_DATA_DIR`: Persistent directory path for sidecar
    storage (`~/.gemini/jetski/sidecar_data/<sidecar_name>/data/`).
*   `ANTIGRAVITY_SIDECAR_UI_TOKEN`: Authentication token appended to iframe URL
    parameters and forwarded by the sidecar gateway in `X-Sidecar-Token`.
*   `ANTIGRAVITY_LS_ADDRESS`: Host address of the Language Server RPC service.
*   `ANTIGRAVITY_CSRF_TOKEN`: CSRF token for calling Language Server endpoints.
*   `PATH`: Prepended with `<appDataDir>/bin` containing the `agentapi` CLI.

### 3. Python Web Server (`server.py`)

Bind the web server strictly to loopback (`127.0.0.1`) on the port provided by
`ANTIGRAVITY_SIDECAR_WEB_PORT` and serve the UI routes declared in
`sidecar.json`. `SidecarManager` runs an authenticated gateway that
reverse-proxies remote Cloudtop and capsule browser requests to `127.0.0.1`,
keeping the inner server private to the host loopback interface. See the
[reference Python web server](references/server_template.py) for the full
implementation.

Implementation requirements:

*   **Loopback Binding**: Bind `ThreadingHTTPServer` strictly to `("127.0.0.1",
    PORT)` inside a `with` block so concurrent browser requests complete cleanly
    and only local loopback processes and `SidecarManager` can reach the
    listener.
*   **Security Token Authentication**: Validate `ANTIGRAVITY_SIDECAR_UI_TOKEN`
    on every request via `X-Sidecar-Token` or `?token=...` using constant-time
    UTF-8 byte comparison (`hmac.compare_digest`), returning `401 Unauthorized`
    when the token is absent or mismatched.
*   **Origin-Restricted CORS**: Validate incoming `Origin` headers against
    allowed Google corporate domains and loopback addresses, echoing only the
    validated origin with `Vary: Origin`.
*   **Query String Path Parsing**: Parse exact paths using
    `urllib.parse.urlparse(self.path).path` so appended Jetski Web parameters
    (e.g., `?token=...&conversationId=...`) route cleanly to `/` and
    `/index.html`.
*   **UTF-8 Encoding & Referrer Policy**: Set `Content-Type: text/html;
    charset=utf-8` and `Referrer-Policy: no-referrer` in HTTP headers, along
    with `<meta charset="utf-8">` and `<meta name="referrer"
    content="no-referrer">` in HTML files.

### 4. HTML Explainer & Google Drive Inline Rendering

The HTML file defines the UI layout. Jetski sidecars support inline rendering of
Google Drive files (Docs, Sheets, Slides) inside the auxiliary pane. See the
[sample HTML explainer](references/sample_explainer.html) for responsive layout
cards and embedded Google Drive iframes.

### Dark Mode CSS Fallbacks

Jetski Web embeds sidecar interfaces inside an iframe, where CSS theme variables
from the host editor may be absent.

*   **Explicit Fallbacks**: Always define fallback values on theme variables:
    `color: var(--vscode-foreground, #cccccc);`.
*   **Explicit Backgrounds**: Define a solid background (`background:
    var(--vscode-editor-background, #1e1e1e);`) so text remains legible across
    light and dark host themes.

## Deployment & UI Reloading

### Deployment Models (CitC Symlinks vs. Physical Copies)

Choose between two deployment strategies based on development phase:

1.  **Active Development (CitC Workspace Symlink)**

    *   **Procedure:** Symlink the project directory
        (`/google/src/cloud/<user>/<client>/google3/.../sidecar`) directly into
        `~/.gemini/config/sidecars/<sidecar_name>`.
    *   **Mechanism:** `SidecarManager` resolves directory symlinks via
        `os.Stat`. Source code edits and `blaze build` generated artifacts (such
        as `blaze-bin/` runfiles and compiled Python protobufs) immediately
        execute upon configuration reload.
    *   **Workspace Lifecycle:** Keep the backing CitC client active while the
        symlinked sidecar is enabled; pruning or deleting the CitC client turns
        the symlink target into a missing path (`ENOENT`) and halts startup.

2.  **Stable Deployment (Physical Directory Copy)**

    *   **Procedure:** Copy self-contained source files (`sidecar.json`,
        `server.py`, static web assets) physically into
        `~/.gemini/config/sidecars/<sidecar_name>/`.
    *   **Mechanism:** Decouples execution from CitC FUSE mounts and client
        lifecycles, guaranteeing persistence across workspace cleanups.

**Mutable CitC Workspace Requirement:** Point active development symlinks
exclusively at a mutable CitC workspace directory
(`/google/src/cloud/<user>/<client>/google3/...`). Read-only Piper snapshot
mounts (`/google/src/files/head/...`) omit `blaze-bin/` runfiles, compiled
Python protobuf modules (such as `codeium_common_pb2`, which fail with
`ModuleNotFoundError` or `ImportError`), and writable runtime directories.

### Deployment & UI Reload Procedure

1.  **Deploy**: Save `sidecar.json`, `server.py`, and HTML assets in
    `~/.gemini/config/sidecars/<sidecar_name>/` (or create a CitC directory
    symlink). `SidecarManager` detects new sidecars within 10 seconds.
2.  **Logs**: Inspect stdout/stderr logs at
    `~/.gemini/jetski/sidecar_data/<sidecar_name>/logs/`.
3.  **Force Reloading (Version Increment Procedure)**: Increment the version
    indicator in the `description` field of `sidecar.json` whenever server code
    or frontend assets change on disk to trigger a process restart and iframe
    reload:

    ```json
    {
      "display_name": "Custom Dashboard",
      "description": "Interactive visualization dashboard (v0.2)",
      "ui_config": {
        "views": [
          {
            "path": "/",
            "entrypoint": "SIDECAR_UI_ENTRYPOINT_AUX_PANE",
            "title": "Custom Dashboard"
          }
        ]
      }
    }
    ```

### Reloading Sidecar Views in the Browser

*   **Version Bump Reloads the Iframe:** Incrementing the version indicator in
    the `sidecar.json` `description` field restarts the backend process and
    reloads the embedded sidecar iframe; browser tab hard-refresh (`Cmd+Shift+R`
    or `F5`) leaves the sidecar process unchanged.

### Critical Implementation Rules

*   **Resolving `"No extensions available"` (`bypassUserConfig` Enforcement)**:
    If the auxiliary pane reads *"No extensions available"*, register and enable
    the sidecar in `~/.gemini/config/config.json`:

    ```json
    "sidecars": {
      "<sidecar_name>": {
        "enabled": true
      }
    }
    ```

    Trigger reload using the version-increment procedure in `sidecar.json`.

*   **`0x0` Iframe Resize Timing**: The DOM ready event fires before the flex
    container expands (`clientWidth = 0`). Verify `width > 10 && height > 10` or
    use a `ResizeObserver` before initializing canvas rendering buffers.

## Visual QA & Verification

Inspect rendered pages using headless browser screenshots before hand-off:

1.  **Capture Headless Screenshot**: Capture screenshots using the
    [headless browser CLI][gbrowser] (with `BypassSandbox: true` when running
    inside a shell sandbox so Chrome can reach host loopback):

    ```bash
    /google/bin/releases/gemini-agents-gbrowser/gbrowser screenshot \
      --width 1280 --height 800 \
      "http://127.0.0.1:<PORT>/index.html?token=<TOKEN>" \
      <appDataDir>/brain/<conversation-id>/scratch/sidecar_qa.png
    ```

    Direct the output image and any log redirects exclusively to
    `<appDataDir>/brain/<conversation-id>/scratch/` so every file path stays
    inside the agent workspace sandbox boundary.

2.  **Inspect Visual Artifact**: Verify box model padding, borders, theme
    tokens, and dropdown clipping.

## References

*   [Reference sidecar manifest](references/sidecar_template.json) - Example
    `sidecar.json` configuration for auxiliary pane views.
*   [Reference Python web server](references/server_template.py) - Loopback HTTP
    server handling token auth, CORS validation, and query strings.
*   [Sample HTML explainer](references/sample_explainer.html) - Explainer layout
    featuring Google Drive inline rendering.
*   [Headless browser skill][gbrowser] - `gbrowser` CLI usage for navigation and
    screenshots.

[gbrowser]: http://google3/learning/gemini/agents/skills/gbrowser/SKILL.md
