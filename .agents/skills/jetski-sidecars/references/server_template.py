"""Reference web server for Jetski UI sidecars.

This script starts a loopback web server to display custom HTML interfaces
inside the Jetski auxiliary panel. SidecarManager runs an authenticated gateway
that reverse-proxies remote Cloudtop and capsule browser requests to 127.0.0.1.
Built-in safeguards:
- Binds strictly to 127.0.0.1 so only local loopback processes can connect.
- Validates authentication tokens using constant-time byte comparison.
- Restricts CORS headers to authorized corporate and loopback origins.
- Strips URL query parameters so pages route reliably.
- Shuts down cleanly and closes the listening socket when stopped.
"""

import hmac
import http
import http.server
import logging
import os
from typing import TypeGuard
import urllib.parse

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("sidecar-server")

PORT = int(os.environ.get("ANTIGRAVITY_SIDECAR_WEB_PORT", "8080"))
UI_TOKEN = os.environ.get("ANTIGRAVITY_SIDECAR_UI_TOKEN")
HTML_PATH = os.path.join(os.path.dirname(__file__), "sample_explainer.html")

_ALLOWED_DOMAIN_SUFFIXES: tuple[str, ...] = (
    ".corp.google.com",
    ".c.googlers.com",
    ".proxy.googleprod.com",
    ".proxy.googlers.com",
    ".googleplex.com",
)

_ALLOWED_URI_SCHEMES: tuple[str, ...] = (
    "vscode-webview://",
    "vscode-file://",
)


def is_allowed_origin(origin: str | None) -> TypeGuard[str]:
  """Validates whether the requesting Origin header is authorized."""
  if not origin:
    return False
  if origin.startswith(_ALLOWED_URI_SCHEMES):
    return True
  try:
    parsed = urllib.parse.urlparse(origin)
  except ValueError:
    return False
  hostname = parsed.hostname
  if not hostname:
    return False
  if hostname in ("localhost", "127.0.0.1", "::1"):
    return parsed.scheme in ("http", "https")
  if parsed.scheme != "https":
    return False
  return any(
      hostname == suffix[1:] or hostname.endswith(suffix)
      for suffix in _ALLOWED_DOMAIN_SUFFIXES
  )


class SidecarHandler(http.server.BaseHTTPRequestHandler):
  """HTTP request handler for the UI sidecar server with security validation."""

  def log_message(self, message_format: str, *args: object) -> None:
    """Logs an HTTP access or error message to the module logger."""
    logger.info(message_format, *args)

  def _cors_headers(self) -> None:
    """Applies origin-restricted CORS headers to authorized callers."""
    origin = self.headers.get("Origin")
    if is_allowed_origin(origin):
      self.send_header("Access-Control-Allow-Origin", origin)
      self.send_header("Vary", "Origin")
      self.send_header(
          "Access-Control-Allow-Methods", "GET, POST, OPTIONS, HEAD"
      )
      self.send_header(
          "Access-Control-Allow-Headers",
          "Content-Type, Authorization, X-Requested-With, X-Sidecar-Token",
      )

  def _validate_token(self) -> bool:
    """Validates the security token using constant-time byte comparison."""
    if not UI_TOKEN:
      logger.warning("ANTIGRAVITY_SIDECAR_UI_TOKEN is unset. Failing closed.")
      return False

    expected_token_bytes = UI_TOKEN.encode("utf-8")

    header_token = self.headers.get("X-Sidecar-Token")
    if header_token and hmac.compare_digest(
        header_token.encode("utf-8"), expected_token_bytes
    ):
      return True

    parsed = urllib.parse.urlparse(self.path)
    query_params = urllib.parse.parse_qs(parsed.query)
    query_tokens = query_params.get("token", [])
    return any(
        hmac.compare_digest(
            candidate_token.encode("utf-8"), expected_token_bytes
        )
        for candidate_token in query_tokens
    )

  def _send_unauthorized(self) -> None:
    """Sends a 401 Unauthorized response for invalid security tokens."""
    self.send_response(http.HTTPStatus.UNAUTHORIZED)
    self.send_header("Content-Type", "text/plain; charset=utf-8")
    self._cors_headers()
    self.end_headers()
    self.wfile.write(b"401 Unauthorized: Invalid or missing security token\n")

  def do_OPTIONS(self) -> None:  # pylint: disable=invalid-name
    """Handles OPTIONS preflight requests."""
    self.send_response(http.HTTPStatus.NO_CONTENT)
    self._cors_headers()
    self.end_headers()

  def do_GET(self) -> None:  # pylint: disable=invalid-name
    """Handles GET requests for HTML rendering."""
    if not self._validate_token():
      self._send_unauthorized()
      return

    path = urllib.parse.urlparse(self.path).path

    if path in ("/", "/index.html"):
      try:
        with open(HTML_PATH, "rb") as html_file:
          body = html_file.read()
        self.send_response(http.HTTPStatus.OK)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header(
            "Cache-Control", "no-store, no-cache, must-revalidate, max-age=0"
        )
        self._cors_headers()
        self.end_headers()
        self.wfile.write(body)
      except OSError as error:
        logger.error("Failed to read HTML file: %s", error)
        self.send_error(
            http.HTTPStatus.INTERNAL_SERVER_ERROR,
            "Error loading explainer",
        )
    else:
      self.send_error(http.HTTPStatus.NOT_FOUND)


def main() -> None:
  """Main entrypoint for starting the loopback HTTP server."""
  logger.info("Starting sidecar on 127.0.0.1:%d", PORT)
  with http.server.ThreadingHTTPServer(
      ("127.0.0.1", PORT), SidecarHandler
  ) as server:
    logger.info("Serving on http://127.0.0.1:%d", PORT)
    try:
      server.serve_forever()
    except KeyboardInterrupt:
      logger.info("Received interrupt signal, shutting down server...")
      server.shutdown()


if __name__ == "__main__":
  main()
