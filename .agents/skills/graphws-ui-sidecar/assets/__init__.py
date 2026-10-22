"""Package containing modularized static web assets for the GraphWorkspace sidecar UI."""

from .app_js import APP_JS
from .index_html import INDEX_HTML
from .style_css import STYLE_CSS

__all__ = [
    "INDEX_HTML",
    "STYLE_CSS",
    "APP_JS",
]
