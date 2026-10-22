# GraphWorkspace UI Sidecar

This plugin provides a dynamic graph visualization of your Jetski agent's
reasoning process and `GraphWorkspace` state.

## Prerequisites

### 1. Enable Sidecar Mendel Flags

Web UI extensions and sidecars are disabled by default behind Mendel feature
flags. Run this utility script on your Cloudtop to force-enable the required
flags for 24 hours:

```bash
/google/src/files/head/depot/google3/prototypes/projects/pixel_ui_sidecar/tools/enable_sidecar_flags.sh
```

### 2. Enable Developer Mode on Jetski Hub

To display custom UI panels in the Jetski Web interface, the Jetski Hub must run
in developer mode. This is a one-time setup:

```bash
mkdir -p ~/.config/jetski
echo 'LAUNCHER_EXTRA_FLAGS=--dev_mode' > ~/.config/jetski/hub.env
systemctl --user restart jetski-hub.service
```

Verify the hub is running cleanly:

```bash
systemctl --user status jetski-hub.service
```

## Installation

1.  Navigate to the sidecars directory in your workspace:

    ```bash
    cd devtools/knowledge/jetski/sidecars/
    ```

2.  Create the local sidecar configuration directory if it does not already
    exist:

    ```bash
    mkdir -p ~/.gemini/config/sidecars/graphws_ui/
    ```

3.  Copy only the `sidecar.json` file to your local configuration:

    ```bash
    cp graphws_ui/sidecar.json ~/.gemini/config/sidecars/graphws_ui/
    ```

4.  The Jetski hub server will automatically detect the new `sidecar.json` file
    and launch the `sidecar.py` script directly from the head snapshot.

## Usage

1.  Open your [Jetski Web](https://jetski.corp.google.com) interface.
2.  Expand the **Extensions** menu in the left sidebar.
3.  Click on **"GraphWorkspace Panel"** to open the panel in the Auxiliary Pane
    (right side).
4.  The UI will automatically poll the active conversation's graph state and
    render it in real-time.

## Configuration

The sidecar is configured via `sidecar.json`. It serves an HTTP web server that
responds to:

-   `/config`: A health check endpoint that returns the sidecar's dynamic UI
    config.
-   `/api/data`: An endpoint that returns the latest GraphWorkspace state for
    the current conversation.
-   `/`: The main HTML entrypoint.

## Development

This sidecar relies on `vis-network.min.js`. Due to Google3 JavaScript policies,
new `.js` files are prohibited in the codebase. Therefore, we serve the minified
library dynamically from the `//third_party/javascript/vis_network/` package
using an absolute path fallback in Python.
