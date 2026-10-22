# Node.js SDK Template Plugin (`node_sdk_plugin`)

Starter template plugin demonstrating how to build an interactive UI plugin using the Node.js Sidecar SDK (`sidecar_sdk`).

## What's Included

*   `plugin.json`: Manifest declaring `"name": "node_sdk_plugin"` and starter `suggestedPrompts`.
*   `install.sh`: Setup script to copy plugin and sidecar files to `~/.gemini/config/plugins/node_sdk_plugin`.
*   `sidecars/node_sdk_template/`: Bundled template sidecar implementing:
    *   `main.mjs`: Node.js ESM backend with `SidecarApp` route handling.
    *   `index.html`: Web UI frontend connecting to `/preload.js` (`window.sidecar`).
    *   `styles.css`: Theme-adaptive styling.
    *   `sidecar.json`: Sidecar manifest configured with `"has_web_ui": true`.

## Runtime Compatibility

Compatible with both **Jetski Web** (internal) and the **Antigravity App** (external).

## How to Install into Your Config Directory

### Option 1: Automated Script (Recommended)

Run the included install script from your `google3` workspace:

```bash
bash third_party/jetski/plugins/templates/node_sdk_plugin/install.sh
```

### Option 2: Manual Installation

Create the target directory under `~/.gemini/config/plugins/node_sdk_plugin/` and copy the files:

```text
~/.gemini/config/plugins/
└── node_sdk_plugin/                  # Plugin directory
    ├── plugin.json
    └── sidecars/
        └── node_sdk_template/        # Sidecar directory
            ├── sidecar.json
            ├── main.mjs
            ├── index.html
            ├── styles.css
            └── package.json
```

Commands:
```bash
DEST=~/.gemini/config/plugins/node_sdk_plugin
mkdir -p "$DEST/sidecars/node_sdk_template"

cp third_party/jetski/plugins/templates/node_sdk_plugin/plugin.json "$DEST/"
cp -r third_party/jetski/plugins/templates/node_sdk_plugin/sidecars/node_sdk_template/* "$DEST/sidecars/node_sdk_template/"
```

## Enabling in Jetski Web

1. Open Jetski Web and click the **UI Plugins** tab on the left sidebar.
2. Toggle **`node_sdk_plugin`** (or `Node.js Template Sidecar`) to enabled.
3. In any conversation, open the **+** / **Plugins** menu in the header to launch the sidecar pane.
