# Buttons

> **Standard Button Presence Gate (`IF/THEN/ELSE`)**:
>
> *   `IF` the screen contains **zero** standard `Button` components (`Filled`,
>     `Elevated`, `Filled Tonal`, `Outlined`, or `Text` buttons)—for example, a
>     mobile inbox screen that only contains an Extended FAB (`"Compose"`), a
>     top Search bar, and a bottom Navigation Bar—`THEN` all standard Button
>     questions below (including `buttons_centered_content`) `MUST` be answered
>     **`"N/A"`** (an Extended FAB `MUST` be evaluated under `fabs.md`, `MUST
>     NOT` be evaluated as a standard `Button`).

1.  [ID: buttons_rounded_corners] If standalone buttons with a container
    (Filled, Elevated, Filled Tonal, or Outlined) are present, do they comply
    with the specification: container height of 40dp and a fully rounded pill
    corner radius of 20dp / 50% (sys.shape.corner.full /
    md.sys.shape.corner.full)? [Metric type: Adherence] [Weight: 10]

2.  [ID: buttons_centered_content] For all standard buttons with a visible
    container (excluding FABs, Extended FABs, Chips, and Navigation Bar pills),
    does the button label or icon (or the combined group if both are present)
    appear to be centered BOTH horizontally and vertically within the container?
    (If any interactive button container left-aligns its icon+label with a
    trailing chevron such as `"Vehicle location >"` or partitions its icon into
    a left cell such as `"Slide to start vehicle"`, evaluate as `"No"`; mark as
    N/A if no standard buttons are present on the screen.) [Metric type:
    Hygiene] [Weight: 3]

3.  [ID: buttons_different_variants] If multiple labeled buttons are present
    (note: not a connected “Button group” component), do they use different
    container style variants to indicate their hierarchy (e.g., a horizontal
    place-sheet action strip combining a high-emphasis `"Directions"` Filled
    button alongside medium-emphasis `"Start"` / `"Ask"` / `"Call"` / `"Save"`
    Filled Tonal buttons and a `"Suggest an edit"` Text button evaluates to
    `"Yes"`, whereas sibling buttons sharing identical dark filled containers
    such as `"Lock"` and `"Unlock"` evaluate to `"No"`)? [Metric type:
    Adherence] [Weight: 3]

4.  [ID: buttons_max_one_filled] Within any single viewport, dialog, or distinct
    card/sheet container, is there at most ONE high-emphasis filled button
    (FilledButton / container fill mapped to sys.color.primary), with all other
    actions using Outlined, Tonal, or Text button variants? [Metric type:
    Hygiene] [Weight: 10]

5.  [ID: buttons_sentence_case] Do text labels on buttons appear to comply with
    sentence case capitalization (only capitalizing the first word and proper
    nouns)? [Metric type: Hygiene] [Weight: 1]

6.  [ID: buttons_icon_leading] If a button contains both an icon and a text
    label, is the icon placed in the leading position (to the left of the text
    label in LTR)? [Metric type: Hygiene] [Weight: 1]

7.  [ID: buttons_disabled_muted] If a disabled button is present, are its
    container fill and text label visually muted compared to active interactive
    buttons? [Metric type: Hygiene] [Weight: 3]

8.  [ID: buttons_labels_single_line] Are button text labels presented on a
    single line without wrapping? [Metric type: Hygiene] [Weight: 5]

9.  [ID: ios_lg_buttons_layer_adherence] On iOS, for standard buttons (Label
    buttons, Elevated, Filled, Tonal, Outlined), does the button correctly
    enable the Liquid Glass variant when placed on the Functional Layer
    (floating over content or docked in floating bars), and default to Non-Glass
    (opaque/outlined/tonal) when placed on the Content Layer? (Pass with "Yes"
    if layer placement matches glass/non-glass variant; fail with "No" if
    mismatched; mark as "N/A" if absent or non-iOS.) [Metric type: Adherence]
    [Weight: 5]
