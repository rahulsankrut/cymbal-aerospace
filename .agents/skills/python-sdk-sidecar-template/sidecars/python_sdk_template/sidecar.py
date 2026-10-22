import os
import sys
from google3.pyglib import resources
from google3.third_party.jetski.sidecar_sdk.python.sidecar.main import Response
from google3.third_party.jetski.sidecar_sdk.python.sidecar.main import SidecarApp

INDEX_HTML_PATH = "google3/third_party/jetski/plugins/templates/python_sdk_plugin/sidecars/python_sdk_template/index.html"
STYLES_CSS_PATH = "google3/third_party/jetski/plugins/templates/python_sdk_plugin/sidecars/python_sdk_template/styles.css"


def handle_home():
  try:
    html_path = resources.GetResourceFilename(INDEX_HTML_PATH)
    with open(html_path, "r", encoding="utf-8") as f:
      return f.read()
  except Exception as e:
    print(f"Error loading index.html: {e}", file=sys.stderr)
    return f"<h1>Error loading index.html: {e}</h1>"


def handle_styles(req_data):
  try:
    css_path = resources.GetResourceFilename(STYLES_CSS_PATH)
    with open(css_path, "r", encoding="utf-8") as f:
      return Response(f.read(), content_type="text/css")
  except Exception as e:
    print(f"Error loading styles.css: {e}", file=sys.stderr)
    return Response(
        f"/* Error loading styles.css: {e} */",
        content_type="text/css",
        status=500,
    )


def handle_hello(req_data):
  name = req_data.get("name", "World")
  return {"message": f"Hello, {name} from Python Sidecar (POST)!"}


def handle_hello_get(req_data):
  name = req_data.get("name", "World")
  return {"message": f"Hello, {name} from Python Sidecar (GET)!"}


def main():
  app = SidecarApp()
  app.page("/", handle_home)
  app.api("/styles.css", handle_styles, method="GET")
  app.api("/api/hello", handle_hello, method="POST")
  app.api("/api/hello_get", handle_hello_get, method="GET")
  app.run()


if __name__ == "__main__":
  main()
