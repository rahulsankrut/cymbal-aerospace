---
name: python-sdk-sidecar-template
description: >-
  Official starter template plugin demonstrating how to build an interactive UI
  Sidecar plugin in Python (plugin.json, sidecar.json, sidecar.py, index.html,
  styles.css) connecting to /preload.js and window.sidecar.
---

# Python SDK Template Plugin (`python_sdk_plugin`)

Starter template plugin demonstrating how to build an interactive UI plugin using the Python Sidecar SDK (`sidecar_sdk.python`).

## What's Included

*   `plugin.json`: Manifest declaring `"name": "python_sdk_plugin"` and starter `suggestedPrompts`.
*   `install.sh`: Setup script to build the `.par` binary and copy plugin/sidecar files to `~/.gemini/config/plugins/python_sdk_plugin`.
*   `sidecars/python_sdk_template/`: Bundled template sidecar implementing:
    *   `sidecar.py`: Python backend with `SidecarApp` route handling and hermetic static resource loading via `pyglib.resources`.
    *   `index.html`: Web UI frontend connecting to `/preload.js` (`window.sidecar`).
    *   `styles.css`: Theme-adaptive styling.
    *   `sidecar.json`: Sidecar manifest configured with `"has_web_ui": true`.

## Runtime Compatibility

Compatible with **Jetski Web** (internal).

## How to Install into Your Config Directory

### Option 1: Automated Script (Recommended)

Run the included install script from your `google3` workspace (this builds the `.par` archive with Blaze and sets up the config folder):

```bash
bash third_party/jetski/plugins/templates/python_sdk_plugin/install.sh
```

### Option 2: Manual Installation

1. Build the executable archive (`.par`) from your `google3` workspace root:
   ```bash
   blaze build //third_party/jetski/plugins/templates/python_sdk_plugin/sidecars/python_sdk_template:sidecar.par
   ```

2. Create the target directory under `~/.gemini/config/plugins/python_sdk_plugin/` and copy the files:

```text
~/.gemini/config/plugins/
└── python_sdk_plugin/                # Plugin directory
    ├── plugin.json
    └── sidecars/
        └── python_sdk_template/      # Sidecar directory
            ├── sidecar.json
            └── sidecar.par           # Compiled binary
```

Commands:
```bash
DEST=~/.gemini/config/plugins/python_sdk_plugin
mkdir -p "$DEST/sidecars/python_sdk_template"

cp third_party/jetski/plugins/templates/python_sdk_plugin/plugin.json "$DEST/"
cp third_party/jetski/plugins/templates/python_sdk_plugin/sidecars/python_sdk_template/sidecar.json "$DEST/sidecars/python_sdk_template/"
cp blaze-bin/third_party/jetski/plugins/templates/python_sdk_plugin/sidecars/python_sdk_template/sidecar.par "$DEST/sidecars/python_sdk_template/"
chmod +x "$DEST/sidecars/python_sdk_template/sidecar.par"
```

## Enabling in Jetski Web

1. Open Jetski Web and click the **UI Plugins** tab on the left sidebar.
2. Toggle **`python_sdk_plugin`** (or `Python Template Sidecar`) to enabled.
3. In any conversation, open the **+** / **Plugins** menu in the header to launch the sidecar pane.
