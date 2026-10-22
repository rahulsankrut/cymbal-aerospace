# Screenshots for UI work

Use gbrowser (headless Chrome) for all captures. Flags, auth modes, and the full
list of batch actions are in the
[gbrowser skill](/learning/gemini/agents/skills/gbrowser/SKILL.md).

## Settings

Use the same settings for every set:

-   `--width 1440 --height 900 --device-scale-factor 1`, a common laptop size.
    Scale 1 keeps files small and makes pairs line up.
-   `--width 390 --height 844`, a common phone size: the main size for
    phone-first apps, and one extra pass per page for the rest.
-   `--wait-for "{ready_selector}"` (or `--wait-time 3s`): shots don't catch
    spinners.

gbrowser captures the viewport only. For long pages, raise `--height` (for
example to 2400) or scroll and take several shots. Local dev servers may need
`--no-proxy-server`; sites behind corp SSO need `--corp`.

## Capture script

Keep one script per app so every set is taken the same way. Page shots use
`screenshot`; state shots use batch files that write to the placeholder
`OUT_DIR`:

```bash
#!/bin/bash
# Usage: ./capture.sh ui_shots/after_v1
# Narrow pass: WIDTH=390 HEIGHT=844 ./capture.sh ui_shots/after_v1_narrow
set -euo pipefail
out="$1"
w="${WIDTH:-1440}"
h="${HEIGHT:-900}"
mkdir -p "$out"

shot() {  # shot FILE_NAME URL
  /google/bin/releases/gemini-agents-gbrowser/gbrowser screenshot \
    --no-proxy-server --width "$w" --height "$h" --device-scale-factor 1 \
    --wait-time 3s --timeout 60s "$2" "$out/$1.png"
}

shot 01_home_default "{base_url}/"
shot 02_settings_default "{base_url}/settings"

for f in states/*.json; do
  sed "s#OUT_DIR#$out#g" "$f" |
    /google/bin/releases/gemini-agents-gbrowser/gbrowser batch \
      --no-proxy-server --width "$w" --height "$h" -
done
```

To shoot one element instead of the viewport, add `--selector "{css_selector}"`
to `screenshot`.

## State shots

One batch session per page keeps state across steps. Every value must be a
string. Example `states/03_list.json`:

```json
[
  {"action": "navigate", "url": "{base_url}/list"},
  {"action": "wait", "selector": "{ready_selector}"},
  {"action": "mouse_event", "type": "mouseMoved", "x": "{x}", "y": "{y}"},
  {"action": "sleep", "duration": "400ms"},
  {"action": "screenshot", "file": "OUT_DIR/03_list_row_hover.png"},
  {"action": "mouse_event", "type": "mouseMoved", "x": "0", "y": "0"},
  {"action": "key_down", "key": "Tab"},
  {"action": "key_up", "key": "Tab"},
  {"action": "sleep", "duration": "300ms"},
  {"action": "screenshot", "file": "OUT_DIR/03_list_focus.png"},
  {"action": "eval", "expression": "document.querySelector('{menu_button}').click(), 'ok'"},
  {"action": "sleep", "duration": "400ms"},
  {"action": "screenshot", "file": "OUT_DIR/03_list_menu_open.png"}
]
```

-   **Hover coordinates**: get the element's center at the same viewport size,
    then pass it to `mouse_event`:

    ```bash
    /google/bin/releases/gemini-agents-gbrowser/gbrowser eval \
      --no-proxy-server --width 1440 --height 900 --wait-for "{selector}" \
      "{url}" "JSON.stringify((r => ({x: Math.round(r.x + r.width / 2),
        y: Math.round(r.y + r.height / 2)}))(document.querySelector(
        '{selector}').getBoundingClientRect()))"
    ```

-   **Move the mouse away** (to `0,0`) before the next shot, or the hover state
    leaks into it.

-   **Keyboard focus**: `Tab` key presses give real `:focus-visible` rings.
    Calling `focus()` from script after a mouse interaction does not.

-   **Clicks**: use `eval` with `el.click()` rather than the `click` action. On
    pages with `scroll-behavior: smooth`, a coordinate-based click can land
    where the element was before scrolling finished. `eval` fails on an
    `undefined` result, so end the expression with `, 'ok'`.

-   **Transitions**: sleep 300–500 ms after each interaction so animations
    finish; otherwise pairs differ by animation frame.

-   **Lazy content**: images and sections that load on scroll render only after
    they enter the viewport. Use the `scroll` action and wait before capturing.

-   **Fonts**: headless Linux Chrome lacks macOS and Windows system fonts, so
    stacks that start with `system-ui`, SF, or Segoe render in a Linux fallback
    font (often DejaVu Sans). Load a web font, or tell the user the shots won't
    match their screen exactly.

## Compare sets

Build side-by-side pairs, count changed pixels per page, and make a contact
sheet:

```bash
mkdir -p ui_shots/pairs
for f in ui_shots/before/*.png; do
  n=$(basename "$f" .png)
  magick \( "$f" -resize 50% \) \( "ui_shots/after_v1/$n.png" -resize 50% \) \
    +append -quality 85 "ui_shots/pairs/$n.jpg"
  printf '%s ' "$n"
  magick compare -metric AE -fuzz 2% "$f" "ui_shots/after_v1/$n.png" null: 2>&1
  echo
done
magick montage ui_shots/after_v1/*.png -tile 4x -geometry 360x+8+8 \
  ui_shots/contact_after_v1.jpg
```

-   A changed-pixel count of `0` means the page looks exactly as before: a
    planned change didn't land, or the server is stale.
-   Review the 50% JPEG pairs rather than full-size PNGs. A pair costs much less
    context than two full screenshots and shows the difference directly.
-   If two sets were captured at different sizes or scales, resize them to the
    same scale before pairing or cropping, or the comparison misleads.
