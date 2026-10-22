# Google Slides Export (Detailed Reference)

Converting an HTML deck to Google Slides involves screenshotting each slide at
retina resolution and inserting them as full-bleed images. This produces a
pixel-perfect Google Slides deck that preserves all the visual design from the
HTML version.

## Step A: Prepare the HTML for screenshotting

Create temporary per-slide HTML files in the **same directory as the original
deck** (so image paths resolve). For each slide:

1.  Inject CSS to hide all UI chrome:

    ```css
    nav,.progress,.counter,.notes-panel,.home-btn {
      display:none!important;height:0!important;
      width:0!important;overflow:hidden!important
    }
    body::before,body::after{display:none!important}
    ```

2.  Change the `show(0)` call to `show(N)` (where N = slide index).

3.  Save as a temporary file (delete after screenshotting).

## Step B: Take retina screenshots

Use headless Chrome via `xvfb-run` at 2× device scale:

```bash
xvfb-run --auto-servernum \
  --server-args="-screen 0 2560x1440x24" \
  google-chrome-stable \
    --headless=new --no-sandbox --disable-gpu \
    --window-size=1280,720 \
    --force-device-scale-factor=2 \
    --force-color-profile=srgb \
    --screenshot=slide_00.png \
    --hide-scrollbars \
    --run-all-compositor-stages-before-draw \
    --virtual-time-budget=5000 \
    "file:///path/to/temp.html"
```

Key settings:

-   **Viewport** `1280×720` with `--force-device-scale-factor=2` produces a
    2560×1440 image (exactly 16:9). Text appears proportionally large and
    readable.
-   `--force-color-profile=srgb` ensures colors match the browser.
-   `--virtual-time-budget=5000` gives JavaScript 5 seconds of simulated time to
    render (important for animations/transitions).
-   `--run-all-compositor-stages-before-draw` forces a complete render before
    screenshotting.

> **Why 1280×720 and not 1920×1080?** At 1920×1080 with 2× scaling, the output
> is 3840×2160 — but text appears very small relative to the slide. The 1280×720
> viewport makes text fill more of the frame, which looks better when projected
> on a large screen in Google Slides.

## Step C: Crop the bottom strip

The progress bar and navigation area leave a thin strip at the bottom of each
screenshot, even when hidden via CSS (the fixed elements still reserve layout
space). Remove it by cropping:

```bash
convert slide_raw.png \
  -gravity South -chop 0x40 \
  -resize 2560x1440! \
  slide_final.png
```

This crops 40 pixels from the bottom and resizes back to exact 2560×1440 (16:9).
The slight vertical stretch is imperceptible and eliminates the strip cleanly.

## Step D: Create the Google Slides presentation

Use the `gslides` CLI (see the gslides skill for full reference):

```bash
GSLIDES=/google/bin/releases/gemini-agents-gslides/gslides

# Create presentation
$GSLIDES create --title "Your Deck Title"

# Add blank slides (N-1 since the first slide already exists)
for i in $(seq 1 $((SLIDE_COUNT - 1))); do
  $GSLIDES add-slide "$PRES_ID"
done

# Get slide IDs
$GSLIDES list-slides "$PRES_ID" --json
```

## Step E: Populate each slide with the screenshot

For each slide, the process is:

1.  **Delete all default elements** (title/body placeholders):

    ```bash
    $GSLIDES get-page "$PRES_ID" "$SLIDE_ID" --json
    # For each element: $GSLIDES delete-element "$PRES_ID" "$ELEMENT_ID"
    ```

2.  **Insert the screenshot image**:

    ```bash
    $GSLIDES insert-image-from-file "$PRES_ID" \
      --slide "$SLIDE_ID" --file slide_00.png
    ```

3.  **Move to origin and resize to fill the slide**:

    The `gslides` `resize-element` command uses **scale factors**, not absolute
    dimensions. The image inserts at a tiny base size (typically 32000×18000
    EMU). You must calculate scale factors to reach the full slide dimensions:

    ```
    Slide width  = 9,144,000 EMU  (10 inches × 914,400 EMU/inch)
    Slide height = 5,143,500 EMU  (5.625 inches × 914,400 EMU/inch)
    ```

    ```python
    # Get the element's base size from get-page JSON
    base_w = element["size"]["width"]["magnitude"]   # e.g., 32000
    base_h = element["size"]["height"]["magnitude"]  # e.g., 18000
    scale_x = 9144000 / base_w  # e.g., 285.75
    scale_y = 5143500 / base_h  # e.g., 285.75
    ```

    ```bash
    $GSLIDES move-element "$PRES_ID" "$ELEM_ID" --x 0 --y 0
    $GSLIDES resize-element "$PRES_ID" "$ELEM_ID" \
      --width "$SCALE_X" --height "$SCALE_Y"
    ```

    > **Critical**: Do NOT pass absolute pixel or point dimensions to
    > `resize-element`. The values are **multiplied** against the base size.
    > Passing `720` and `405` would make the image 720× larger than its base —
    > massively oversized and cropped.

4.  **Set speaker notes**:

    ```bash
    $GSLIDES set-notes "$PRES_ID" \
      --slide "$SLIDE_ID" --text "Speaker notes here..."
    ```

## Step F: Handle transient API failures

The Google Slides API frequently returns `Error 400: There was a problem
retrieving the image` for `createImage` calls. These are **transient** — the
same call usually succeeds on retry.

Build retry logic into your pipeline:

-   Track which slide indices failed.
-   After completing the first pass through all slides, wait 2 seconds, then
    retry all failures.
-   If any still fail after the first retry, retry again.
-   In practice, 1-2 retries resolves all failures.

## Complete pipeline summary

```
Screenshot → Crop → Create Deck → Add Slides → For Each Slide:
  Delete Elements → Insert Image → Move(0,0) → Resize(scale) → Set Notes
  → Retry failures
```

A 30-slide deck takes approximately 15-20 minutes end-to-end (\~3 seconds per
screenshot + \~30 seconds per slide API calls).
