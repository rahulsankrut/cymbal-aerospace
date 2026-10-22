"""GraphWorkspace sidecar server."""

import http.server
import json
import os
import re
import urllib.parse

try:
  from google3.devtools.knowledge.jetski.sidecars.graphws_ui import assets  # pylint: disable=g-import-not-at-top
except ImportError:
  import assets  # pylint: disable=g-import-not-at-top  # pytype: disable=import-error

# Jetski assigns a dynamic port
PORT = int(os.environ.get("ANTIGRAVITY_SIDECAR_WEB_PORT", "8080"))
HOST = os.environ.get("ANTIGRAVITY_SIDECAR_HOST", "127.0.0.1")

# Health check response (Entrypoint 1 = AUX_PANE)
SIDECAR_UI_CONFIG = json.dumps({
    "display_name": "GraphWorkspace Panel",
    "views": [{"entrypoint": 1, "path": "/"}],
})


# We resolve the sidecar execution directory path (where sidecar.py is located)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_google3_root(path: str) -> str | None:
  """Returns the google3 root directory path."""
  while path != os.path.dirname(path):
    if os.path.basename(path) == "google3":
      return path
    path = os.path.dirname(path)
  return None


class SimpleHandler(http.server.BaseHTTPRequestHandler):
  """HTTP request handler for GraphWorkspace sidecar server."""

  def _send_js_response(self, content: bytes):
    self.send_response(200)
    self.send_header("Content-Type", "application/javascript; charset=utf-8")
    self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
    self.send_header("Pragma", "no-cache")
    self.send_header("Expires", "0")
    self.end_headers()
    self.wfile.write(content)

  def do_GET(self):  # pylint: disable=invalid-name
    """Handles GET requests to serve UI and APIs."""
    parsed_url = urllib.parse.urlparse(self.path)
    path = parsed_url.path

    # Mandatory Health Check Endpoint
    if path == "/config":
      self.send_response(200)
      self.send_header("Content-Type", "application/json")
      self.end_headers()
      self.wfile.write(SIDECAR_UI_CONFIG.encode("utf-8"))

    # API Endpoint for dynamic Graph Workspace JSON
    elif path == "/api/data":
      query_params = urllib.parse.parse_qs(parsed_url.query)
      conv_id = query_params.get("conversationId", [None])[0]

      if not conv_id:
        self.send_response(400)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"error": "Missing conversationId parameter"}')
        return

      if not re.fullmatch(r"[a-zA-Z0-9\-]+", conv_id):
        self.send_response(400)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"error": "Invalid conversationId parameter"}')
        return

      # Resolve state file path. Attempt to use ANTIGRAVITY_EXECUTABLE_DATA_DIR
      # first to support custom data directories (e.g. customized workspace
      # home or VM).
      app_data_dir = None
      executable_data_dir = os.environ.get("ANTIGRAVITY_EXECUTABLE_DATA_DIR")
      if executable_data_dir:
        # Move up 3 levels: sidecar_data/<sidecar_id>/data ->
        # sidecar_data/<sidecar_id> -> sidecar_data -> jetski
        app_data_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(executable_data_dir))
        )

      state_file = ""
      if app_data_dir:
        state_file = os.path.join(
            app_data_dir, "brain", conv_id, "graphws_state.json"
        )

      if not state_file or not os.path.exists(state_file):
        state_file = os.path.expanduser(
            f"~/.gemini/jetski/brain/{conv_id}/graphws_state.json"
        )

      if not os.path.exists(state_file):
        state_file = f"/tmp/jetski_brain/{conv_id}/graphws_state.json"

      if not os.path.exists(state_file):
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(b'{"nodes": {}, "edges": [], "tools": {}}')
        return

      self.send_response(200)
      self.send_header("Content-Type", "application/json; charset=utf-8")
      self.end_headers()
      with open(state_file, "rb") as f:
        self.wfile.write(f.read())

    # Serve Static HTML Page
    elif path in ("/", "/index.html"):
      self.send_response(200)
      self.send_header("Content-Type", "text/html; charset=utf-8")
      self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
      self.send_header("Pragma", "no-cache")
      self.send_header("Expires", "0")
      self.end_headers()
      self.wfile.write(assets.INDEX_HTML.encode("utf-8"))

    elif path == "/vis-network.js":
      root = get_google3_root(BASE_DIR)
      if root:
        vis_path = os.path.join(
            root, "third_party/javascript/vis_network/vis-network.min.js"
        )
        if not os.path.exists(vis_path):
          vis_path = os.path.join(
              root,
              "third_party/javascript/node_modules/vis_network/v9_1_2/standalone/umd/vis-network.min.js",
          )

        if os.path.exists(vis_path):
          with open(vis_path, "rb") as f:
            self._send_js_response(f.read())
          return
      self.send_error(404, "vis-network.js not found")

    else:
      self.send_error(404)


def main():
  """Runs the HTTP sidecar server."""
  server = http.server.HTTPServer((HOST, PORT), SimpleHandler)
  print(f"Serving on http://{HOST}:{PORT}")
  try:
    server.serve_forever()
  except KeyboardInterrupt:
    server.shutdown()


if __name__ == "__main__":
  main()
