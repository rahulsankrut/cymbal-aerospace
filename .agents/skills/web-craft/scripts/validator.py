"""Core verification modules for NotebookOS HTML Artifact Validator.

Uses only packages verified in sandbox.Dockerfile:
- bs4 (BeautifulSoup4)
- lxml
- PIL (Pillow)
- Standard library (re, json, os, subprocess, tempfile, dataclasses)
"""

from dataclasses import dataclass  # pylint: disable=g-importing-member
import json
import os
import re
import subprocess
import tempfile
import urllib.parse
import bs4

BeautifulSoup = bs4.BeautifulSoup

try:
  from PIL import Image, ImageStat  # pylint: disable=g-multiple-import,g-import-not-at-top
except ImportError:
  Image = None
  ImageStat = None

# Allowed values for the <meta name="artifact-type"> and
# <meta name="design-style"> tags that SKILL.md 5.1 asks for. The server parses
# these tags when an .html artifact is saved and logs any value not on its own
# list as `other`, so the two lists must match. DESIGN_STYLES must also match
# the references/style_<slug>.md files (enforced by test_validator.py).
# LINT.IfChange(artifact_meta_values)
ARTIFACT_TYPES = ('narrative', 'dashboard', 'tool')
DESIGN_STYLES = (
    'atelier',
    'aurora',
    'bauhaus',
    'briefing',
    'broadsheet',
    'canopy',
    'carbon',
    'charter',
    'deco',
    'figure',
    'handbook',
    'haven',
    'kiln',
    'maison',
    'moderne',
    'neon_noir',
    'nocturne',
    'raster',
    'riso',
    'showroom',
    'sonnet',
    'sticker',
    'terracotta',
    'vitals',
)
# LINT.ThenChange(//depot/google3/java/com/google/labs/language/tailwind/boqnodes/common/xbox/HtmlArtifactMeta.kt:artifact_meta_values)


@dataclass
class ValidationFinding:
  """Represents a single validation finding."""

  category: str
  message: str
  severity: str = 'ERROR'

  def __str__(self) -> str:
    return f'[{self.category}] {self.message}'


def check_html_structure(soup: BeautifulSoup) -> list[ValidationFinding]:
  """Checks HTML5 boilerplate, charset, viewport meta, and duplicate DOM IDs."""
  findings = []

  if not soup.find('head'):
    findings.append(
        ValidationFinding(
            'STRUCTURE', 'Missing <head> tag in document structure.'
        )
    )
  if not soup.find('body'):
    findings.append(
        ValidationFinding(
            'STRUCTURE', 'Missing <body> tag in document structure.'
        )
    )

  charset_meta = soup.find(
      'meta', attrs={'charset': re.compile(r'utf-8', re.I)}
  )
  if not charset_meta:
    findings.append(
        ValidationFinding(
            'STRUCTURE',
            'Missing <meta charset="UTF-8"> tag for proper character encoding.',
        )
    )

  viewport_meta = soup.find(
      'meta', attrs={'name': re.compile(r'^viewport$', re.I)}
  )
  if not viewport_meta:
    findings.append(
        ValidationFinding(
            'STRUCTURE',
            'Missing responsive <meta name="viewport"> tag for iframe scaling.',
        )
    )

  # Check for duplicate IDs across the entire DOM
  seen_ids = set()
  for el in soup.find_all(attrs={'id': True}):
    el_id = str(el.get('id', '')).strip()
    if not el_id:
      continue
    if el_id in seen_ids:
      findings.append(
          ValidationFinding(
              'DUPLICATE_ID', f'Duplicate DOM ID found: id="{el_id}".'
          )
      )
    seen_ids.add(el_id)

  return findings


def strip_js_comments(code: str) -> str:
  """Removes single-line and multi-line comments from JS while preserving strings."""
  pattern = r'(\".*?\"|\'.*?\'|`[\s\S]*?`)|(/\*[\s\S]*?\*/|//.*?$)'

  def _replace(match: re.Match[str]) -> str:
    if match.group(1):
      return match.group(1)
    matched_comment = match.group(2) or ''
    return '\n' if matched_comment.startswith('//') else ''

  return re.sub(pattern, _replace, code, flags=re.MULTILINE)


def check_js_targets_and_json(
    soup: BeautifulSoup, raw_html: str = ''
) -> list[ValidationFinding]:
  """Checks missing DOM targets and unescaped LaTeX in JS strings."""
  del raw_html  # Unused.
  findings = []
  dom_ids = {
      str(el.get('id', '')).strip()
      for el in soup.find_all(attrs={'id': True})
      if el.get('id')
  }

  for idx, script in enumerate(soup.find_all('script')):
    content = str(script.string or '')
    if not content.strip():
      continue

    clean_content = strip_js_comments(content)

    # 1. Check DOM ID references in getElementById or querySelector('#...')
    id_refs = re.findall(
        r"(?:getElementById|querySelector|querySelectorAll)\(\s*[\"']#?([a-zA-Z0-9_-]+)[\"']\s*\)",
        clean_content,
    )
    for ref in id_refs:
      if ref not in dom_ids:
        findings.append(
            ValidationFinding(
                'JS_TARGET_MISSING',
                f"JS (#script-{idx + 1}): References DOM ID '{ref}', but no"
                f' element with id="{ref}" exists in HTML.',
            )
        )

    # 2. Check for unescaped LaTeX math in JavaScript strings.
    # In JS/JSON strings, \f is Form Feed, \t is Tab, \n is Newline, \r is
    # Carriage Return, \b is Backspace, etc. In LaTeX, math commands like
    # \frac, \sqrt, \times, \theta, \alpha, \beta, \sum, \int, etc. must be
    # double-escaped as \\frac, \\sqrt, etc.
    # We inspect math blocks enclosed in $...$ or $$...$$ within individual
    # string literals, excluding ${...} template interpolations and currency
    # values, and match unescaped LaTeX commands.
    js_strings = re.findall(
        r'"(?:\\.|[^"\\\r\n])*"|\'(?:\\.|[^\'\\\r\n])*\'|`(?:\\.|[^`\\])*`',
        clean_content,
    )
    math_blocks = []
    for js_str in js_strings:
      math_blocks.extend(re.findall(r'\$\$(.+?)\$\$', js_str, flags=re.DOTALL))
      math_blocks.extend(
          re.findall(
              r'(?<!\$)\$(?!\{)([^\r\n$]+?)(?<!\\)\$(?![\$0-9])',
              js_str,
          )
      )
    offending_cmd = None
    for block in math_blocks:
      # Strip valid fixed-length JS Unicode/Hex escapes (\uXXXX, \u{...}, \xXX)
      # first so trailing alphanumeric characters (e.g. \u26636) are not
      # greedily merged into the escape token.
      cleaned_block = re.sub(
          r'(?<!\\)\\(?:u[0-9a-fA-F]{4}|u\{[0-9a-fA-F]+\}|x[0-9a-fA-F]{2})',
          '',
          block,
      )
      unescaped_cmds = re.findall(r'(?<!\\)\\([a-zA-Z]+)', cleaned_block)
      for cmd in unescaped_cmds:
        # Ignore standard 1-char JS string control escapes (n, t, r, f, b, v).
        if cmd not in ('n', 't', 'r', 'f', 'b', 'v'):
          offending_cmd = cmd
          break
      if offending_cmd:
        snippet = block if len(block) <= 40 else block[:37] + '...'
        findings.append(
            ValidationFinding(
                'JSON_LATEX_ESCAPING',
                f'JS (#script-{idx + 1}): Unescaped LaTeX command'
                f" '\\{offending_cmd}' in '${snippet}$' (e.g. '$\\frac'"
                " instead of '$\\\\frac'). LaTeX backslashes MUST be"
                ' double-escaped in JavaScript strings.',
            )
        )
        break

  return findings


def check_storage_and_shim_api(
    soup: BeautifulSoup, raw_html: str = ''
) -> list[ValidationFinding]:
  """Checks for unsupported browser storage and verifies <api-shim> presence."""
  findings = []
  has_api_shim_tag = bool(
      soup.find('api-shim')
      or (raw_html and re.search(r'<api-shim\b[^>]*>', raw_html, re.I))
  )
  has_notebook_api_usage = False
  has_set_app_state = False
  has_get_app_state = False
  has_get_app_state_without_await = False

  for idx, script in enumerate(soup.find_all('script')):
    content = str(script.string or '')
    if not content.strip():
      continue
    clean_content = strip_js_comments(content)

    # Check for unsupported browser storage APIs
    if re.search(
        r'\b(?:localStorage|sessionStorage|indexedDB)\b|\bdocument\.cookie\b',
        clean_content,
    ):
      findings.append(
          ValidationFinding(
              'UNSUPPORTED_STORAGE',
              f'JS (#script-{idx + 1}): Uses browser storage'
              ' (localStorage / sessionStorage / indexedDB / cookie),'
              ' which does not persist across sessions in the sandboxed'
              ' iframe. Use <api-shim></api-shim> and'
              ' window.notebookAppApi.setAppState() / getAppState()'
              ' instead.',
              severity='WARNING',
          )
      )

    if re.search(r'\bnotebookAppApi\b', clean_content):
      has_notebook_api_usage = True
    if re.search(r'\.setAppState\s*\(', clean_content):
      has_set_app_state = True
    if re.search(r'\.getAppState\s*\(', clean_content):
      has_get_app_state = True
      # Check for getAppState() without await — check each line
      for line in clean_content.splitlines():
        if re.search(r'\.getAppState\s*\(', line) and not re.search(
            r'\bawait\b', line
        ):
          has_get_app_state_without_await = True

  if has_notebook_api_usage and not has_api_shim_tag:
    findings.append(
        ValidationFinding(
            'MISSING_API_SHIM',
            'JavaScript references notebookAppApi, but the document is'
            ' missing the required <api-shim></api-shim> tag in <body>.',
            severity='ERROR',
        )
    )

  # Check for asymmetric state usage
  if has_set_app_state and not has_get_app_state:
    findings.append(
        ValidationFinding(
            'ASYMMETRIC_STATE_USAGE',
            'App calls setAppState() but never getAppState(). Saved state'
            ' is never restored — returning users will lose their previous'
            ' data on every visit.',
            severity='WARNING',
        )
    )
  elif has_get_app_state and not has_set_app_state:
    findings.append(
        ValidationFinding(
            'ASYMMETRIC_STATE_USAGE',
            'App calls getAppState() but never setAppState(). State is'
            ' loaded but never updated — the app will never remember'
            ' anything new.',
            severity='WARNING',
        )
    )

  # Check for missing await on getAppState()
  if has_get_app_state_without_await:
    findings.append(
        ValidationFinding(
            'MISSING_AWAIT_GET_STATE',
            'getAppState() returns a Promise. Without await, the variable'
            ' will be a Promise object (always truthy), not the actual'
            ' saved data.',
            severity='WARNING',
        )
    )

  return findings


def check_js_unterminated_strings(
    soup: BeautifulSoup, raw_html: str = ''
) -> list[ValidationFinding]:
  """Detects unterminated JS string literals caused by raw newlines in quotes."""
  findings = []

  for idx, script in enumerate(soup.find_all('script')):
    content = script.string or ''
    if not content.strip():
      continue

    base_line = 1
    if raw_html:
      script_start_idx = raw_html.find(content)
      if script_start_idx != -1:
        base_line = raw_html[:script_start_idx].count('\n') + 1

    # Character-by-character scan
    state = 'NORMAL'
    stack = []  # stack of ['TEMPLATE_LITERAL' | 'TEMPLATE_EXPR', brace_depth]
    in_regex_char_class = False

    line_num = 1
    col_num = 1
    str_start_line = 1
    str_snippet = ''

    i = 0
    n = len(content)

    while i < n:
      ch = content[i]
      next_ch = content[i + 1] if i + 1 < n else ''

      if ch == '\n':
        if state in ('IN_SINGLE_QUOTE', 'IN_DOUBLE_QUOTE'):
          quote_char = "'" if state == 'IN_SINGLE_QUOTE' else '"'
          # Check for valid JS line continuation (trailing unescaped backslash)
          line_prefix = content[:i]
          last_non_space = line_prefix.rstrip(' \t\r')
          is_escaped_continuation = False
          if last_non_space.endswith('\\'):
            backslash_count = 0
            for k in range(len(last_non_space) - 1, -1, -1):
              if last_non_space[k] == '\\':
                backslash_count += 1
              else:
                break
            if backslash_count % 2 == 1:
              is_escaped_continuation = True

          if is_escaped_continuation:
            line_num += 1
            col_num = 1
            i += 1
            continue

          # Raw unescaped newline in string literal -> fatal SyntaxError
          abs_line = base_line + str_start_line - 1

          clean_snippet = str_snippet.replace('\n', ' ').strip()
          if len(clean_snippet) > 50:
            clean_snippet = clean_snippet[:47] + '...'
          findings.append(
              ValidationFinding(
                  'JS_UNTERMINATED_STRING',
                  f'JS (#script-{idx + 1}): Unterminated string literal'
                  f' starting on line {str_start_line} (HTML L{abs_line}). Raw'
                  f' unescaped newline inside {quote_char}...{quote_char}'
                  ' string literal. In JavaScript, multi-line strings MUST use'
                  " backtick template literals (`...`) or explicit '\\n'"
                  f' escape sequences. String began: {clean_snippet!r}',
                  severity='ERROR',
              )
          )
          state = 'NORMAL'
          str_snippet = ''
        elif state == 'IN_LINE_COMMENT':
          state = 'NORMAL'
        elif state == 'IN_REGEX':
          state = 'NORMAL'
          in_regex_char_class = False

        line_num += 1
        col_num = 1
        i += 1
        continue

      if ch == '\r':
        col_num += 1
        i += 1
        continue

      if state == 'NORMAL':
        if ch == '/' and next_ch == '/':
          state = 'IN_LINE_COMMENT'
          i += 2
          col_num += 2
          continue
        elif ch == '/' and next_ch == '*':
          state = 'IN_BLOCK_COMMENT'
          i += 2
          col_num += 2
          continue
        elif ch == '"':
          state = 'IN_DOUBLE_QUOTE'
          str_start_line = line_num
          str_snippet = '"'
          i += 1
          col_num += 1
          continue
        elif ch == "'":
          state = 'IN_SINGLE_QUOTE'
          str_start_line = line_num
          str_snippet = "'"
          i += 1
          col_num += 1
          continue
        elif ch == '`':
          state = 'IN_TEMPLATE_LITERAL'
          stack.append(['TEMPLATE_LITERAL', 0])
          i += 1
          col_num += 1
          continue
        elif ch == '{':
          if stack and stack[-1][0] == 'TEMPLATE_EXPR':
            stack[-1][1] += 1
          i += 1
          col_num += 1
          continue
        elif ch == '}':
          if stack and stack[-1][0] == 'TEMPLATE_EXPR':
            stack[-1][1] -= 1
            if stack[-1][1] == 0:
              stack.pop()
              state = 'IN_TEMPLATE_LITERAL'
              i += 1
              col_num += 1
              continue
          i += 1
          col_num += 1
          continue
        elif ch == '/':
          # Check if division or regex literal
          prev_code = content[:i].rstrip(' \t\r\n')
          if not prev_code or prev_code[-1] in '=([:,!&|?;{}+-*%^~':
            state = 'IN_REGEX'
            in_regex_char_class = False
            i += 1
            col_num += 1
            continue
        i += 1
        col_num += 1
        continue

      elif state == 'IN_DOUBLE_QUOTE':
        str_snippet += ch
        if ch == '\\':
          i += 1
          col_num += 1
          if i < n:
            str_snippet += content[i]
            i += 1
            col_num += 1
          continue
        elif ch == '"':
          state = 'NORMAL'
          str_snippet = ''
          i += 1
          col_num += 1
          continue
        i += 1
        col_num += 1
        continue

      elif state == 'IN_SINGLE_QUOTE':
        str_snippet += ch
        if ch == '\\':
          i += 1
          col_num += 1
          if i < n:
            str_snippet += content[i]
            i += 1
            col_num += 1
          continue
        elif ch == "'":
          state = 'NORMAL'
          str_snippet = ''
          i += 1
          col_num += 1
          continue
        i += 1
        col_num += 1
        continue

      elif state == 'IN_TEMPLATE_LITERAL':
        if ch == '\\':
          i += 2
          col_num += 2
          continue
        elif ch == '$' and next_ch == '{':
          state = 'NORMAL'
          stack.append(['TEMPLATE_EXPR', 1])
          i += 2
          col_num += 2
          continue
        elif ch == '`':
          if stack and stack[-1][0] == 'TEMPLATE_LITERAL':
            stack.pop()
          if not stack:
            state = 'NORMAL'
          elif stack[-1][0] == 'TEMPLATE_LITERAL':
            state = 'IN_TEMPLATE_LITERAL'
          else:
            state = 'NORMAL'

          i += 1
          col_num += 1
          continue
        i += 1
        col_num += 1
        continue

      elif state == 'IN_REGEX':
        if ch == '\\':
          i += 2
          col_num += 2
          continue
        elif ch == '[' and not in_regex_char_class:
          in_regex_char_class = True
          i += 1
          col_num += 1
          continue
        elif ch == ']' and in_regex_char_class:
          in_regex_char_class = False
          i += 1
          col_num += 1
          continue
        elif ch == '/' and not in_regex_char_class:
          state = 'NORMAL'
          i += 1
          col_num += 1
          continue
        i += 1
        col_num += 1
        continue

      elif state == 'IN_BLOCK_COMMENT':
        if ch == '*' and next_ch == '/':
          state = 'NORMAL'
          i += 2
          col_num += 2
          continue
        i += 1
        col_num += 1
        continue

      elif state == 'IN_LINE_COMMENT':
        i += 1
        col_num += 1
        continue

  return findings


# Mirrors the CSP connect-src allowlist in csp_allowlist_config.gcl
# (enforced by test_validator.py).
_ALLOWED_CONNECT_HOSTS = {
    'cdn.tailwindcss.com',
    'fonts.googleapis.com',
    'maps.googleapis.com',
    '*.gstatic.com',
    'cdn.jsdelivr.net',
    'cdnjs.cloudflare.com',
    'unpkg.com',
    'cdn.plot.ly',
}


def _is_allowed_connect_host(hostname: str | None) -> bool:
  """Checks if a hostname is within the CSP connect-src allowlist."""
  if not hostname:
    return True
  hostname = hostname.lower()
  if hostname in _ALLOWED_CONNECT_HOSTS:
    return True
  for allowed in _ALLOWED_CONNECT_HOSTS:
    if allowed.startswith('*.') and hostname.endswith(allowed[1:]):
      return True
  return False


def check_map_tile_providers(soup: BeautifulSoup) -> list[ValidationFinding]:
  """Flags raster map tiles, which are banned outright.

  There is no approved tile server. Maps must be built from public-domain
  vector geometry (Natural Earth / US Census TopoJSON) rendered via Leaflet
  GeoJSON layers, Plotly geo traces, D3, or ECharts. See references/maps.md.

  Args:
    soup: The parsed HTML document to inspect.

  Returns:
    A finding for every raster tile layer or tile-backed Plotly trace found.
  """
  findings = []
  # Every L.tileLayer call is banned regardless of URL, so the first branch
  # keys on the call itself and the string literal is optional. The second
  # branch still catches a bare tile template assigned elsewhere, including
  # protocol-relative forms.
  tile_pattern = re.compile(
      r"""(?:L\.tileLayer(?:\.\w+)?\s*\((?:\s*['"`]([^'"`]*)['"`])?"""
      r"""|['"`]((?:https?:)?//[^'"`]*\{[xyz]\}[^'"`]*)['"`])""",
      re.I,
  )
  # Plotly trace/layout types that are tile-backed rather than vector.
  mapbox_pattern = re.compile(
      r"""['"`]?(scattermapbox|densitymapbox|choroplethmapbox)['"`]?""", re.I
  )

  for script in soup.find_all('script'):
    code = script.string or script.get_text() or ''
    if not code.strip():
      continue
    clean_code = strip_js_comments(code)

    seen = set()
    for match in tile_pattern.finditer(clean_code):
      tile_url = match.group(1) or match.group(2) or 'L.tileLayer(...)'
      if tile_url in seen:
        continue
      seen.add(tile_url)
      findings.append(
          ValidationFinding(
              'RASTER_MAP_TILES_BANNED',
              f"Raster map tile layer found: '{tile_url}'. Map tiles are"
              ' banned — there is no approved tile server (not'
              ' OpenStreetMap, CartoDB, Stadia/Stamen, Mapbox, or Esri).'
              ' Build the map from public-domain vector geometry instead:'
              ' fetch world-atlas/us-atlas TopoJSON from cdn.jsdelivr.net and'
              ' render it with L.geoJSON(), or use a Plotly'
              " 'choropleth'/'scattergeo' trace. See references/maps.md.",
              severity='ERROR',
          )
      )

    for match in mapbox_pattern.finditer(clean_code):
      trace = match.group(1)
      findings.append(
          ValidationFinding(
              'RASTER_MAP_TILES_BANNED',
              f"Plotly '{trace}' is tile-backed and therefore banned. Use the"
              " vector equivalents instead: 'scattergeo' for points/routes and"
              " 'choropleth' for region shading. See references/maps.md.",
              severity='ERROR',
          )
      )

  return findings


def check_map_zoom_resolution(soup: BeautifulSoup) -> list[ValidationFinding]:
  """Flags vector basemaps whose resolution is too coarse for their zoom.

  Unlike raster tiles, vector geometry has a fixed resolution. A map that
  opens at zoom 6 or higher with only country-level geometry puts the whole
  viewport inside a single polygon, so it renders as one flat fill with no
  borders and no console error. See references/maps.md.

  Args:
    soup: The parsed HTML document to inspect.

  Returns:
    A finding if coarse geometry is paired with a high opening zoom.
  """
  findings = []
  # Country-level datasets: national borders only, nothing finer.
  coarse_pattern = re.compile(r'countries-(110|50)m\.json', re.I)
  # Opening zoom, as set in L.map options or via setView.
  zoom_option_pattern = re.compile(r'\bzoom\s*:\s*(\d+(?:\.\d+)?)')
  set_view_pattern = re.compile(
      r'\.setView\s*\(\s*\[[^\]]*\]\s*,\s*(\d+(?:\.\d+)?)'
  )
  # Minimum zoom at which each dataset stops producing visible geometry.
  min_broken_zoom = {'110': 6, '50': 7}

  for script in soup.find_all('script'):
    code = script.string or script.get_text() or ''
    if not code.strip():
      continue
    clean_code = strip_js_comments(code)

    coarse = coarse_pattern.search(clean_code)
    if not coarse:
      continue
    # A finer dataset in the same file means the coarse one is likely an
    # intentional overview layer, so do not second-guess it.
    if re.search(r'(states|counties)-10m\.json', clean_code, re.I):
      continue

    resolution = coarse.group(1)
    threshold = min_broken_zoom[resolution]

    zooms = [
        float(m.group(1)) for m in zoom_option_pattern.finditer(clean_code)
    ]
    zooms += [float(m.group(1)) for m in set_view_pattern.finditer(clean_code)]
    # maxZoom/minZoom are bounds, not the opening view; ignore those keys.
    zooms = [z for z in zooms if z > 0]
    if not zooms:
      continue

    deepest_zoom = max(zooms)
    if deepest_zoom < threshold:
      continue

    findings.append(
        ValidationFinding(
            'MAP_ZOOM_EXCEEDS_GEOMETRY',
            f"Map reaches zoom {deepest_zoom:g} using 'countries-{resolution}m'"
            ' geometry, which only contains national borders. At this zoom the'
            ' viewport sits inside a single polygon, so the basemap renders as'
            ' one flat fill with no visible borders or coastline. Load finer'
            " geometry — 'us-atlas@3/states-10m.json' for multi-state views or"
            " 'us-atlas@3/counties-10m.json' for a state or metro area — or"
            ' zoom out. See references/maps.md.',
            severity='ERROR',
        )
    )

  return findings


def _balanced_brace_block(text: str, start: int) -> str:
  """Returns the first balanced ``{...}`` block beginning near ``start``.

  Args:
    text: Source text to scan.
    start: Index to begin searching from. The opening brace must appear within a
      few characters of this index, so an unrelated later block is not picked up
      when the expected object literal is absent.

  Returns:
    The block including its outer braces, or '' if there is none nearby or the
    braces are unbalanced.
  """
  open_idx = text.find('{', start)
  if open_idx == -1 or open_idx - start > 40:
    return ''
  depth = 0
  for i in range(open_idx, len(text)):
    if text[i] == '{':
      depth += 1
    elif text[i] == '}':
      depth -= 1
      if depth == 0:
        return text[open_idx : i + 1]
  return ''


# Leaflet path options that leave a layer see-through.
_FILL_TRANSPARENT_JS = re.compile(
    r"""fill\s*:\s*(?:false|['"`]none['"`])"""
    r"""|fillOpacity\s*:\s*0(?:\.0+)?\s*[,}]""",
    re.I,
)
# Leaflet path options that paint a solid area.
_FILL_OPAQUE_JS = re.compile(
    r"""fill\s*:\s*(?:true|['"`](?!none)[^'"`]+['"`])"""
    r"""|fillOpacity\s*:\s*(?:0\.\d*[1-9]\d*|[1-9]\d*)""",
    re.I,
)
# CSS declarations that leave an SVG path see-through.
_FILL_TRANSPARENT_CSS = re.compile(
    r'fill\s*:\s*(?:none|transparent)'
    r'|fill-opacity\s*:\s*0(?:\.0+)?\s*(?:;|!|$)',
    re.I,
)
# A CSS `fill:` declaration, excluding the `fill-opacity` longhand.
_FILL_DECL_CSS = re.compile(r'(?<!-)\bfill\s*:\s*([^;}!]+)', re.I)


def check_map_outline_layer_fill(
    soup: BeautifulSoup,
) -> list[ValidationFinding]:
  """Flags a stacked outline layer that is not transparent.

  Pattern 9 draws county detail and then a state outline on top of it. The
  top layer has to be transparent or it covers the geometry underneath, and
  the map renders as one flat fill with no error. The subtle case is styling
  via `className`: `fill: false` only makes Leaflet write a `fill="none"`
  presentation attribute, which any CSS `fill` declaration overrides. See
  references/maps.md.

  Args:
    soup: The parsed HTML document to inspect.

  Returns:
    A finding per outline layer that will paint over the layer beneath it.
  """
  findings = []
  css = '\n'.join(
      style.string or style.get_text() or '' for style in soup.find_all('style')
  )

  def exact_class_rule(class_name: str) -> str | None:
    """Returns the body of the rule whose selector is exactly this class.

    Compound selectors such as `.basemap-state.is-overlay` need a second class
    to be applied, so they do not describe the layer's resting state.

    Args:
      class_name: Class to look up, without the leading dot.

    Returns:
      The declaration body, or None when no such rule exists.
    """
    for rule in re.finditer(r'([^{}]+)\{([^{}]*)\}', css):
      if rule.group(1).strip() == '.' + class_name:
        return rule.group(2)
    return None

  for script in soup.find_all('script'):
    code = script.string or script.get_text() or ''
    if not code.strip():
      continue
    clean_code = strip_js_comments(code)
    # Only a concern when a detail layer sits underneath the outline.
    if not re.search(r'objects\.counties', clean_code, re.I):
      continue

    # counties-10m exposes objects.states and objects.nation, so a page can
    # stack more than one outline layer. Check each of them.
    for assignment in re.finditer(
        r'(?:const|let|var)\s+(\w+)\s*=\s*topojson\.feature\s*\([^)]*'
        r'objects\.(states|nation)\b',
        clean_code,
        re.I,
    ):
      outline_var, outline_object = assignment.group(1), assignment.group(2)

      call = re.search(
          r'L\.geojson\s*\(\s*' + re.escape(outline_var) + r'\s*,',
          clean_code,
          re.I,
      )
      if not call:
        continue
      options = _balanced_brace_block(clean_code, call.end())
      if not options:
        continue

      class_match = re.search(
          r"""className\s*:\s*['"`]([^'"`]+)['"`]""", options
      )
      if class_match:
        settled = False
        for class_name in class_match.group(1).split():
          body = exact_class_rule(class_name)
          if body is None:
            continue
          if _FILL_TRANSPARENT_CSS.search(body):
            settled = True
            break
          declaration = _FILL_DECL_CSS.search(body)
          if declaration:
            findings.append(
                ValidationFinding(
                    'MAP_OUTLINE_LAYER_OPAQUE_FILL',
                    f"The '{outline_object}' outline layer is styled by CSS"
                    f" rule '.{class_name}', which sets"
                    f" 'fill: {declaration.group(1).strip()}'. A CSS fill"
                    ' overrides the fill="none" attribute Leaflet writes for'
                    " 'fill: false', so this layer paints over the county"
                    ' geometry beneath it and the map renders as a flat fill.'
                    f" Add 'fill: none' to '.{class_name}'. See"
                    ' references/maps.md.',
                    severity='ERROR',
                )
            )
            settled = True
            break
        if settled:
          continue

      if _FILL_TRANSPARENT_JS.search(options):
        continue
      if _FILL_OPAQUE_JS.search(options):
        findings.append(
            ValidationFinding(
                'MAP_OUTLINE_LAYER_OPAQUE_FILL',
                f"The '{outline_object}' outline layer is drawn over county"
                ' geometry with an opaque fill, so it hides every county'
                " boundary beneath it. Give the top layer 'fill: false'. See"
                ' references/maps.md.',
                severity='ERROR',
            )
        )

  return findings


def check_unapproved_network_requests(
    soup: BeautifulSoup,
) -> list[ValidationFinding]:
  """Detects network requests (fetch, d3.json, axios) to unapproved external domains."""
  findings = []
  fetch_pattern = re.compile(
      r"""(?:fetch\s*\(\s*['"`](https?://[^'"`\s]+)['"`]|d3\.(?:json|csv|tsv|text)\s*\(\s*['"`](https?://[^'"`\s]+)['"`]|axios\.(?:get|post)\s*\(\s*['"`](https?://[^'"`\s]+)['"`]|\$\.(?:get|getJSON|ajax)\s*\(\s*['"`](https?://[^'"`\s]+)['"`])""",
      re.I,
  )

  for script in soup.find_all('script'):
    code = script.string or script.get_text() or ''
    if not code.strip():
      continue
    clean_code = strip_js_comments(code)
    for match in fetch_pattern.finditer(clean_code):
      url_str = (
          match.group(1) or match.group(2) or match.group(3) or match.group(4)
      )
      if not url_str:
        continue
      parsed = urllib.parse.urlparse(url_str)
      host = (parsed.hostname or '').lower()
      if host and not _is_allowed_connect_host(host):
        findings.append(
            ValidationFinding(
                'UNAPPROVED_NETWORK_REQUEST',
                f"Unauthorized network request to '{url_str}'. The sandbox CSP"
                ' connect-src only allows requests to: cdn.jsdelivr.net,'
                ' unpkg.com, cdnjs.cloudflare.com, cdn.plot.ly,'
                ' cdn.tailwindcss.com, fonts.googleapis.com, and'
                ' maps.googleapis.com (no other googleapis.com subdomain).'
                ' Map geometry must come from world-atlas/us-atlas on'
                ' cdn.jsdelivr.net (see references/maps.md); other external'
                ' datasets (like GeoJSON) must be loaded from allowlisted CDNs'
                ' or inlined in JS.',
                severity='ERROR',
            )
        )

  return findings


def check_resources(
    soup: BeautifulSoup, artifacts_dir: str | None = None
) -> list[ValidationFinding]:
  """Checks for insecure HTTP CDN URLs and verifies local artifact references."""
  findings = []

  for tag in soup.find_all(['script', 'link', 'img', 'a', 'audio', 'video']):
    url = tag.get('src') or tag.get('href')
    if not url:
      continue
    url_str = str(url).strip()

    if url_str.startswith('http://'):
      findings.append(
          ValidationFinding(
              'INSECURE_URL',
              f'Insecure HTTP URL found (must use HTTPS): {url_str}',
          )
      )

    if (
        artifacts_dir
        and url_str.startswith('/api/artifacts/')
        and '?' in url_str
    ):
      filename = url_str.split('?')[0].replace('/api/artifacts/', '').strip()
      local_path = os.path.join(artifacts_dir, filename)
      if not os.path.exists(local_path):
        findings.append(
            ValidationFinding(
                'MISSING_RESOURCE',
                f"Referenced artifact file missing on disk: '{filename}'"
                f" (checked '{local_path}').",
            )
        )

  return findings


def check_headless_render(filepath: str) -> list[ValidationFinding]:
  """Renders HTML via wkhtmltoimage and checks for WSOD / blank screen with Pillow."""
  findings = []
  if Image is None or ImageStat is None:
    return findings

  with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
    tmp_img = tmp.name

  try:
    proc = subprocess.run(
        [
            'wkhtmltoimage',
            '--quiet',
            '--load-error-handling',
            'ignore',
            '--load-media-error-handling',
            'ignore',
            '--format',
            'png',
            filepath,
            tmp_img,
        ],
        capture_output=True,
        timeout=10,
        check=False,
    )

    if os.path.exists(tmp_img) and os.path.getsize(tmp_img) > 0:
      with Image.open(tmp_img) as img:
        width, height = img.size
        if height < 20 or width < 20:
          findings.append(
              ValidationFinding(
                  'RENDER_ERROR',
                  'Collapsed viewport layout (rendered image size only'
                  f' {width}x{height}px).',
              )
          )
        else:
          stat = ImageStat.Stat(img.convert('L'))
          # stddev approaching 0 indicates a 100% solid/blank image (WSOD)
          if stat.stddev[0] < 1.0:
            findings.append(
                ValidationFinding(
                    'WSOD_BLANK_PAGE',
                    'White-Screen-of-Death detected (rendered image is 100%'
                    ' blank/solid color).',
                )
            )
    else:
      err_msg = proc.stderr.decode('utf-8', errors='replace').strip()
      findings.append(
          ValidationFinding(
              'RENDER_ERROR',
              'wkhtmltoimage failed to produce an output image file:'
              f' {err_msg}',
          )
      )
  except FileNotFoundError:
    # wkhtmltoimage CLI not installed on this machine; skip silently
    pass
  except subprocess.TimeoutExpired:
    findings.append(
        ValidationFinding(
            'RENDER_ERROR',
            'Page rendering timed out (>10s) - possible infinite loop in'
            ' script.',
        )
    )
  finally:
    if os.path.exists(tmp_img):
      try:
        os.unlink(tmp_img)
      except OSError:
        pass

  return findings


def check_js_runtime(
    filepath: str,
) -> list[ValidationFinding]:
  """Runs dynamic JS error checking via Node.js + jsdom if available in the environment."""
  script_dir = os.path.dirname(os.path.abspath(__file__))
  checker_path = os.path.join(script_dir, 'js_error_checker.js')
  if not os.path.exists(checker_path):
    return []

  try:
    proc = subprocess.run(
        ['node', checker_path, filepath],
        capture_output=True,
        text=True,
        timeout=15,
        check=False,
    )
    if proc.returncode != 0 or not proc.stdout.strip():
      return [
          ValidationFinding(
              category='VALIDATOR_ENVIRONMENT_WARNING',
              message=(
                  f'Node.js execution failed (return code {proc.returncode}).'
                  ' Dynamic JS error checking disabled.'
              ),
              severity='WARNING',
          )
      ]
    data = json.loads(proc.stdout)
    findings = []
    for item in data.get('findings', []):
      cat = item.get('category', 'JS_RUNTIME_ERROR')
      msg = item.get('message', 'JavaScript execution error')
      line = item.get('line')
      if line:
        msg = f'Line {line}: {msg}'
      findings.append(
          ValidationFinding(
              category=cat,
              message=msg,
              severity=item.get('severity', 'ERROR'),
          )
      )
    return findings
  except FileNotFoundError:
    # Node.js binary not installed in this environment; skip gracefully.
    return [
        ValidationFinding(
            category='VALIDATOR_ENVIRONMENT_WARNING',
            message=(
                'Node.js binary not installed. Dynamic JS error checking is'
                ' disabled.'
            ),
            severity='WARNING',
        )
    ]
  except subprocess.TimeoutExpired:
    return [
        ValidationFinding(
            'JS_RUNTIME_ERROR',
            'JavaScript execution timed out (>15s) in sandbox — possible'
            ' infinite loop.',
        )
    ]
  except Exception:  # pylint: disable=broad-except
    return []


# Inline event handler attribute names to scan.
_EVENT_ATTRS = frozenset({
    'onclick',
    'ondblclick',
    'onmousedown',
    'onmouseup',
    'onmouseover',
    'onmouseout',
    'onmousemove',
    'onmouseenter',
    'onmouseleave',
    'onkeydown',
    'onkeyup',
    'onkeypress',
    'onfocus',
    'onblur',
    'onchange',
    'oninput',
    'onsubmit',
    'onreset',
    'onselect',
    'onscroll',
    'onresize',
    'onload',
    'onerror',
    'onunload',
    'onbeforeunload',
    'ondrag',
    'ondragstart',
    'ondragend',
    'ondragover',
    'ondragenter',
    'ondragleave',
    'ondrop',
    'ontouchstart',
    'ontouchmove',
    'ontouchend',
    'ontouchcancel',
    'oncontextmenu',
    'onwheel',
    'onanimationstart',
    'onanimationend',
    'onanimationiteration',
    'ontransitionend',
    'onpointerdown',
    'onpointerup',
    'onpointermove',
    'onpointerenter',
    'onpointerleave',
    'onpointercancel',
    'ontoggle',
    'onclose',
})

# Browser globals / JS keywords that should never be flagged.
_JS_BUILTINS = frozenset({
    # Browser APIs
    'alert',
    'confirm',
    'prompt',
    'setTimeout',
    'setInterval',
    'clearTimeout',
    'clearInterval',
    'requestAnimationFrame',
    'cancelAnimationFrame',
    'fetch',
    'parseInt',
    'parseFloat',
    'isNaN',
    'isFinite',
    'encodeURIComponent',
    'decodeURIComponent',
    'encodeURI',
    'decodeURI',
    'atob',
    'btoa',
    'open',
    'close',
    'print',
    'scroll',
    'scrollTo',
    'scrollBy',
    'getComputedStyle',
    'matchMedia',
    'addEventListener',
    'removeEventListener',
    'dispatchEvent',
    'postMessage',
    'structuredClone',
    'queueMicrotask',
    'requestIdleCallback',
    'cancelIdleCallback',
    'eval',
    'Function',
    # Constructors & namespaces
    'JSON',
    'Math',
    'Date',
    'Array',
    'Object',
    'String',
    'Number',
    'Boolean',
    'RegExp',
    'Map',
    'Set',
    'WeakMap',
    'WeakSet',
    'Promise',
    'Error',
    'TypeError',
    'RangeError',
    'SyntaxError',
    'Symbol',
    'Proxy',
    'Reflect',
    'URL',
    'URLSearchParams',
    'Headers',
    'Request',
    'Response',
    'FormData',
    'Blob',
    'File',
    'FileReader',
    'Image',
    'Audio',
    'MutationObserver',
    'IntersectionObserver',
    'ResizeObserver',
    'AbortController',
    'TextEncoder',
    'TextDecoder',
    'Worker',
    'WebSocket',
    'EventSource',
    'BroadcastChannel',
    'Notification',
    'CSSStyleSheet',
    'CSS',
    'customElements',
    'Intl',
    # Global objects
    'console',
    'document',
    'window',
    'self',
    'globalThis',
    'history',
    'location',
    'navigator',
    'screen',
    'performance',
    'crypto',
    'localStorage',
    'sessionStorage',
    # Literals & special identifiers
    'this',
    'event',
    'arguments',
    'undefined',
    'null',
    'true',
    'false',
    'Infinity',
    'NaN',
})

_JS_KEYWORDS = frozenset({
    'if',
    'else',
    'for',
    'while',
    'do',
    'switch',
    'case',
    'break',
    'continue',
    'return',
    'throw',
    'try',
    'catch',
    'finally',
    'with',
    'new',
    'typeof',
    'instanceof',
    'void',
    'delete',
    'in',
    'of',
    'class',
    'super',
    'extends',
    'import',
    'export',
    'from',
    'as',
    'default',
    'debugger',
    'yield',
    'await',
    'async',
    'let',
    'const',
    'var',
    'function',
})


def check_inline_handler_functions(
    soup: BeautifulSoup,
) -> list[ValidationFinding]:
  """Checks that functions called in inline event handlers are defined."""
  findings = []

  # 1. Collect function definitions from all <script> blocks.
  defined_functions: set[str] = set()
  for script in soup.find_all('script'):
    content = script.string or ''
    if not content.strip():
      continue

    # function foo(
    for m in re.finditer(
        r'\bfunction\s+([a-zA-Z_$][a-zA-Z0-9_$]*)\s*\(', content
    ):
      defined_functions.add(m.group(1))

    # const/let/var foo = function|( | async function|( | x =>
    for m in re.finditer(
        r'\b(?:const|let|var)\s+([a-zA-Z_$][a-zA-Z0-9_$]*)\s*='
        r'\s*(?:async\s+)?(?:function[\s(]|\([^)]*\)\s*=>|'
        r'[a-zA-Z_$][a-zA-Z0-9_$]*\s*=>)',
        content,
    ):
      defined_functions.add(m.group(1))

    # window.foo = function|( | arrow
    for m in re.finditer(
        r'\bwindow\.([a-zA-Z_$][a-zA-Z0-9_$]*)\s*='
        r'\s*(?:async\s+)?(?:function[\s(]|\([^)]*\)\s*=>|'
        r'[a-zA-Z_$][a-zA-Z0-9_$]*\s*=>)',
        content,
    ):
      defined_functions.add(m.group(1))

  # 2. Scan inline event handlers for function calls.
  flagged_functions: set[str] = set()
  for el in soup.find_all(True):
    for attr_name, attr_value in el.attrs.items():
      if attr_name.lower() not in _EVENT_ATTRS:
        continue
      handler_code = str(attr_value).strip()
      if not handler_code:
        continue

      # Match function calls: identifier( — but not .identifier(
      calls = re.findall(
          r'(?:^|[^.\w$])([a-zA-Z_$][a-zA-Z0-9_$]*)\s*\(',
          handler_code,
      )
      for func_name in calls:
        if func_name in _JS_KEYWORDS:
          continue
        if func_name in _JS_BUILTINS:
          continue
        if func_name in defined_functions:
          continue
        if func_name in flagged_functions:
          continue  # already reported
        flagged_functions.add(func_name)
        findings.append(
            ValidationFinding(
                'UNDEFINED_HANDLER_FN',
                f"Inline {attr_name} references '{func_name}()' but no "
                f"function '{func_name}' is defined in any <script> block. "
                f"(Static check \u2014 if '{func_name}' is provided by an "
                f'external <script src="...">, this is a false positive '
                f'and can be ignored. Otherwise, add the missing function '
                f'definition.)',
            )
        )

  return findings


_CHART_MAP_ID_REGEX = re.compile(
    r'(?:^|[-_])(map|chart|plot|plotly|echart|leaflet|graph|canvas)(?:$|[-_])',
    re.I,
)


def check_chart_and_map_container_heights(
    soup: BeautifulSoup,
) -> list[ValidationFinding]:
  """Checks that chart and map container divs declare an explicit height or min-height."""
  findings = []
  for div in soup.find_all(['div', 'section']):
    div_id = div.get('id', '')
    classes = div.get('class', [])
    if isinstance(classes, str):
      classes = classes.split()

    if not div_id and not any(_CHART_MAP_ID_REGEX.search(c) for c in classes):
      continue
    if div_id and not _CHART_MAP_ID_REGEX.search(div_id):
      continue

    has_flex_grow = any(c in ('flex-grow', 'grow', 'flex-1') for c in classes)
    has_full_w_or_h = any(c in ('w-full', 'h-full') for c in classes)

    has_explicit_tw_height = any(
        re.match(r'^(min-h|h)-(?:[0-9]+|\[.+\]|screen)', c)
        for c in classes
        if c not in ('h-full', 'h-auto', 'h-fit')
    )
    style = div.get('style', '')
    has_style_height = bool(
        re.search(r'\b(?:min-)?height\s*:\s*(?!0|auto)[^;]+', style, re.I)
    )

    if (has_flex_grow or has_full_w_or_h) and not (
        has_explicit_tw_height or has_style_height
    ):
      is_empty_or_canvas = (
          not div.text.strip() or div.find('canvas') is not None
      )
      if is_empty_or_canvas:
        target_name = f'#{div_id}' if div_id else f'.{".".join(classes[:2])}'
        findings.append(
            ValidationFinding(
                'CHART_CONTAINER_ZERO_HEIGHT',
                f'Chart/map container {target_name} lacks an explicit height'
                ' (e.g. min-h-[400px], h-96, or style="min-height: 400px;").'
                ' Flex children with flex-grow or w-full evaluate to 0px'
                ' height before browser layout, causing Plotly, Leaflet,'
                ' ECharts, or Chart.js to fail to render.',
                severity='ERROR',
            )
        )

  return findings


def check_module_script_inline_handlers(
    soup: BeautifulSoup,
) -> list[ValidationFinding]:
  """Detects <script type="module"> used alongside inline HTML event handlers."""
  findings = []
  module_scripts = soup.find_all('script', type=re.compile(r'\bmodule\b', re.I))
  if not module_scripts:
    return findings

  inline_handlers = []
  for tag in soup.find_all(True):
    for attr in tag.attrs:
      if attr.lower() in _EVENT_ATTRS:
        inline_handlers.append((tag.name, attr, tag.attrs[attr]))

  if inline_handlers:
    examples = [
        f'{tag_name}[{attr}="{str(val)[:20]}..."]'
        for tag_name, attr, val in inline_handlers[:2]
    ]
    findings.append(
        ValidationFinding(
            'INLINE_HANDLER_MODULE_SCOPE',
            '<script type="module"> is used alongside inline HTML event'
            f' handlers ({", ".join(examples)}). Module scripts do not expose'
            ' top-level functions to global window scope, causing "Uncaught'
            ' ReferenceError: <func> is not defined" when clicked. Use regular'
            ' <script> (non-module) for artifacts with inline event handlers.',
            severity='ERROR',
        )
    )

  return findings


_FAKE_CHROME_REGEX = re.compile(
    r'\b(?:v\d+\.\d+(?:\.\d+)?|version\s+\d+\.\d+|system\s+version|admin'
    r'\s+console|ceo\s+command\s+shell|\[classified\]|terminal\s+prompt)\b',
    re.I,
)


def _is_app_header_selector(sel: str) -> bool:
  """Returns True if selector targets app header (not table headers or toolbars)."""
  if any(
      k in sel
      for k in ('th', 'thead', 'table', 'filter', 'toolbar', 'toc', 'sidebar')
  ):
    return False
  return bool(
      re.search(
          r'(?:^|[\s>+~])(?:header|\.header|#header|\.page-header|\.app-header)(?:$|[\s.\[:#>+~])',
          sel,
      )
  )


def _check_sticky_headers(soup: BeautifulSoup) -> list[ValidationFinding]:
  """Checks for sticky or fixed positioning on headers."""
  findings = []
  for header in soup.find_all('header'):
    classes = header.get('class', [])
    if isinstance(classes, str):
      classes = classes.split()
    if any(
        c in {'sticky', 'fixed'}
        or c.endswith(':sticky')
        or c.endswith(':fixed')
        for c in classes
    ):
      findings.append(
          ValidationFinding(
              'COSMETIC_STICKY_HEADER',
              'Header uses sticky/fixed positioning class. Headers must be'
              ' position: static so they do not permanently block viewport'
              ' space.',
              severity='COSMETIC',
          )
      )
    style_attr = str(header.get('style', ''))
    if re.search(r'\bposition\s*:\s*(?:sticky|fixed)\b', style_attr, re.I):
      findings.append(
          ValidationFinding(
              'COSMETIC_STICKY_HEADER',
              'Header uses inline position: sticky/fixed. Headers must be'
              ' position: static so they do not permanently block viewport'
              ' space.',
              severity='COSMETIC',
          )
      )

  for style_tag in soup.find_all('style'):
    css_text = style_tag.string or ''
    if not css_text.strip():
      continue
    css_clean = re.sub(r'/\*.*?\*/', '', css_text, flags=re.DOTALL)
    for rule_match in re.finditer(r'([^{}:;]+)\s*\{([^{}]+)\}', css_clean):
      selectors = rule_match.group(1).strip().lower()
      declarations = rule_match.group(2)
      sel_list = [s.strip() for s in selectors.split(',') if s.strip()]
      if any(_is_app_header_selector(s) for s in sel_list):
        if re.search(
            r'\bposition\s*:\s*(?:sticky|fixed)\b', declarations, re.I
        ):
          findings.append(
              ValidationFinding(
                  'COSMETIC_STICKY_HEADER',
                  f'CSS rule for "{selectors}" sets position: sticky/fixed on'
                  ' header. Headers must be position: static.',
                  severity='COSMETIC',
              )
          )
  return findings


_SCROLLY_OVERFLOW_ANCESTORS = (
    '.page-grid',
    '.scrolly',
    'main',
    'section',
    '.container',
    '.wrapper',
    '.layout',
    '.content',
    '.page',
)


def _is_scrolly_ancestor_selector(selector: str) -> bool:
  """Returns whether a CSS selector targets a scrollytelling wrapper ancestor.

  Args:
    selector: A single, lowercased CSS selector (one entry of a comma list).

  Returns:
    True if the selector matches one of `_SCROLLY_OVERFLOW_ANCESTORS` exactly or
    as the leading compound/descendant/child token, else False.
  """
  for anc in _SCROLLY_OVERFLOW_ANCESTORS:
    if selector == anc or selector.startswith(
        (anc + ' ', anc + '.', anc + ':', anc + '>')
    ):
      return True
  return False


def _check_scrolly_sticky_overflow(
    soup: BeautifulSoup,
) -> list[ValidationFinding]:
  """Flags a scrollytelling sticky graphic under a block-axis overflow ancestor.

  `position: sticky` is silently disabled when any ancestor between the sticky
  element and the scroll root has `overflow` other than `visible` on the block
  axis (`overflow` or `overflow-y` = hidden|clip|auto|scroll). This makes the
  pinned scrollytelling graphic scroll away after the first beat, leaving a
  blank graphic column. `overflow-x: clip` alone is safe (it does not create a
  scroll container) and is not flagged.

  Args:
    soup: Parsed BeautifulSoup document for the HTML artifact.

  Returns:
    A list with one ValidationFinding per offending ancestor CSS rule; empty
    when no scrollytelling graphic is present or no ancestor clips the block
    axis.
  """
  findings = []
  # Only relevant when a scrollytelling sticky graphic is present.
  if not (soup.find(class_='scrolly-graphic') or soup.find(class_='scrolly')):
    return findings

  block_overflow = re.compile(
      r'\boverflow(?:-y)?\s*:\s*(?:hidden|clip|auto|scroll)\b', re.I
  )
  for style_tag in soup.find_all('style'):
    css_text = style_tag.string or ''
    if not css_text.strip():
      continue
    css_clean = re.sub(r'/\*.*?\*/', '', css_text, flags=re.DOTALL)
    for rule_match in re.finditer(r'([^{}]+?)\s*\{([^{}]+)\}', css_clean):
      selectors = rule_match.group(1).strip().lower()
      declarations = rule_match.group(2)
      sel_list = [s.strip() for s in selectors.split(',') if s.strip()]
      is_ancestor = any(_is_scrolly_ancestor_selector(sel) for sel in sel_list)
      if is_ancestor and block_overflow.search(declarations):
        findings.append(
            ValidationFinding(
                'SCROLLY_STICKY_OVERFLOW_ANCESTOR',
                f'CSS rule for "{selectors}" sets a block-axis overflow'
                ' (overflow / overflow-y = hidden|clip|auto|scroll) on an'
                ' ancestor of the scrollytelling sticky graphic. This silently'
                ' disables position: sticky, so the graphic scrolls away after'
                ' the first beat. Use overflow-x: clip instead to guard'
                ' horizontal blowout without breaking the pin.',
                severity='WARNING',
            )
        )
  return findings


def _check_pulse_dots(soup: BeautifulSoup) -> list[ValidationFinding]:
  """Checks for small pulsing status indicator dots."""
  findings = []
  for el in soup.find_all(True):
    classes = el.get('class', [])
    if isinstance(classes, str):
      classes = classes.split()
    style_attr = str(el.get('style', ''))

    has_circle = 'rounded-full' in classes or re.search(
        r'\bborder-radius\s*:\s*(?:50%|100%|9999px)\b', style_attr, re.I
    )
    has_pulse = any(
        'animate-pulse' in c or 'pulse' in c or 'blink' in c for c in classes
    ) or re.search(
        r'\banimation(?:-name)?\s*:[^;]*(?:pulse|blink)', style_attr, re.I
    )

    if has_circle and has_pulse:
      findings.append(
          ValidationFinding(
              'COSMETIC_PULSE_DOT',
              f'Element <{el.name}> combines circular border-radius with'
              ' pulse/blink animation to create a status dot. Use text labels'
              ' with colored backgrounds instead.',
              severity='COSMETIC',
          )
      )
  return findings


_BADGE_KEYWORDS = ('badge', 'version', 'chrome', 'status', 'system')


def _is_badge_or_chrome_el(el_id: str, classes: list[str]) -> bool:
  for k in _BADGE_KEYWORDS:
    if k in el_id:
      return True
    for c in classes:
      if k in c.lower():
        return True
  return False


def _check_fake_chrome(soup: BeautifulSoup) -> list[ValidationFinding]:
  """Checks for fake application chrome, version badges, and role labels."""
  findings = []
  for el in soup.find_all(['title', 'h1', 'h2', 'h3', 'header', 'span', 'div']):
    is_heading = el.name in {'title', 'h1', 'h2', 'h3', 'header'}
    classes = el.get('class', [])
    if isinstance(classes, str):
      classes = classes.split()
    el_id = str(el.get('id', '')).lower()
    is_badge = _is_badge_or_chrome_el(el_id, classes)
    if not (is_heading or is_badge):
      continue

    text = el.get_text(separator=' ', strip=True)

    m = _FAKE_CHROME_REGEX.search(text)
    if m:
      has_child_match = False
      for child in el.find_all(True):
        if child != el and _FAKE_CHROME_REGEX.search(
            child.get_text(separator=' ', strip=True)
        ):
          has_child_match = True
          break
      if has_child_match:
        continue
      findings.append(
          ValidationFinding(
              'COSMETIC_FAKE_CHROME',
              f'Element <{el.name}> contains fake application chrome or version'
              f' label "{m.group(0)}". Use plain descriptive headings without'
              ' fake system badges or version numbers.',
              severity='COSMETIC',
          )
      )
  return findings


def check_cosmetics(soup: BeautifulSoup) -> list[ValidationFinding]:
  """Checks cosmetic rules (sticky headers, pulse dots, fake chrome)."""
  findings = []
  findings.extend(_check_sticky_headers(soup))
  findings.extend(_check_scrolly_sticky_overflow(soup))
  findings.extend(_check_pulse_dots(soup))
  findings.extend(_check_fake_chrome(soup))

  return findings


def check_artifact_meta(soup: BeautifulSoup) -> list[ValidationFinding]:
  """Checks the artifact-type / design-style meta tags.

  Findings are COSMETIC (non-blocking): a missing or unknown tag only degrades
  logging (the server records it as `unset` / `other`); the page still works.

  Args:
    soup: Parsed artifact.

  Returns:
    A list of findings; empty when both tags are present with known values.
  """
  findings = []
  for name, allowed in (
      ('artifact-type', ARTIFACT_TYPES),
      ('design-style', DESIGN_STYLES),
  ):
    allowed_str = ', '.join(allowed)
    tag = soup.find('meta', attrs={'name': name})
    if tag is None:
      findings.append(
          ValidationFinding(
              category='ARTIFACT_META_MISSING',
              message=(
                  f'No <meta name="{name}"> tag. Add <meta name="{name}"'
                  f' content="..."> to <head>, using one of: {allowed_str}.'
              ),
              severity='COSMETIC',
          )
      )
      continue
    value = str(tag.get('content') or '').strip()
    if value not in allowed:
      findings.append(
          ValidationFinding(
              category='ARTIFACT_META_UNKNOWN_VALUE',
              message=(
                  f'<meta name="{name}"> has content "{value}". Use one of:'
                  f' {allowed_str}.'
              ),
              severity='COSMETIC',
          )
      )
  return findings


def validate_html_artifact(
    filepath: str,
    artifacts_dir: str | None = None,
) -> list[ValidationFinding]:
  """Runs all HTML artifact checks against a target file."""
  if not os.path.exists(filepath):
    return [
        ValidationFinding(
            'FILE_NOT_FOUND', f'Target HTML file does not exist: {filepath}'
        )
    ]

  with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

  soup = BeautifulSoup(content, 'lxml')

  findings = []
  findings.extend(check_html_structure(soup))
  findings.extend(check_js_targets_and_json(soup))
  findings.extend(check_storage_and_shim_api(soup, raw_html=content))
  findings.extend(check_js_unterminated_strings(soup, raw_html=content))
  findings.extend(check_js_runtime(filepath))
  findings.extend(check_resources(soup, artifacts_dir=artifacts_dir))
  findings.extend(check_map_tile_providers(soup))
  findings.extend(check_map_zoom_resolution(soup))
  findings.extend(check_map_outline_layer_fill(soup))
  findings.extend(check_unapproved_network_requests(soup))
  findings.extend(check_inline_handler_functions(soup))
  findings.extend(check_module_script_inline_handlers(soup))
  findings.extend(check_chart_and_map_container_heights(soup))
  findings.extend(check_cosmetics(soup))
  findings.extend(check_artifact_meta(soup))
  findings.extend(check_headless_render(filepath))

  return findings
