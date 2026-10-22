"""HTML template asset for GraphWorkspace sidecar UI."""

from .app_js import APP_JS
from .style_css import STYLE_CSS

_HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Graph Workspace (GraphWs)</title>
    <script type="text/javascript" src="/vis-network.js"></script>
    <script type="text/javascript">
__APP_JS_PLACEHOLDER__
    </script>
    <style>
__STYLE_CSS_PLACEHOLDER__
    </style>
</head>
<body>
    <div id="network-container">
        <div id="mynetwork"></div>
        <div id="status-message">Loading data...</div>
    </div>
    <div id="details-panel">
        <h2>GraphWorkspace</h2>
        <div id="conversation-info">ID: <span id="conversation-id-val"></span></div>
        <div id="toolbar">
            <button id="toggle-physics-btn" class="active" onclick="togglePhysics()">Physics: ON</button>
            <button onclick="stabilizeNetwork()">Stabilize Layout</button>
        </div>
        <div id="details-content">
            <p style="color: #666; font-style: italic; font-size: 0.9em; text-align: center; margin-top: 40px;">
                Click on a node or edge to inspect properties.
            </p>
        </div>
    </div>


</body>
</html>
"""

INDEX_HTML = _HTML_TEMPLATE.replace(
    "__STYLE_CSS_PLACEHOLDER__", STYLE_CSS
).replace("__APP_JS_PLACEHOLDER__", APP_JS)
