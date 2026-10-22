# App bars

> **App Bar Presence & Disambiguation Gate (`IF/THEN/ELSE`)**:
>
> *   **Bottom Sheet Header vs. Top App Bar**: `IF` a header (such as a location
>     or place title paired with Share and Close `'X'` icon buttons) sits inside
>     a **Bottom Sheet / Card** overlaid over a map canvas and no top-anchored
>     screen-level App Bar exists, `THEN` it is a **Bottom Sheet Header** (`MUST
>     NOT` be classified as an App Bar) and all App Bar questions below `MUST`
>     be answered **`"N/A"`**.
> *   **Exact-One Text Element Rule (`all_app_bars_one_text_element`)**:
>     Requires **EXACTLY ONE (`count == 1`)** canonical text element (`headline
>     [with optional subtitle]`, `search field hint text`, or `product brand
>     mark`) in the top app bar row (numeric reward/point pills or count badges
>     do NOT count as a canonical app bar text element). `IF` a mobile inbox
>     screen uses a top search bar (`"Search in mail"`) as its top app bar
>     container (`count == 1`), `THEN` `CONCLUDE` **`"Yes"`**. `IF` a top app
>     bar row contains **0** canonical headline text elements (e.g., only icons
>     +   a numeric point badge while the primary entity title and developer
>         name sit in the scrollable body below) or combines `>= 2` distinct
>         text elements, `THEN` `CONCLUDE` **`"No"`**.
> *   **Absent Sub-Elements**: `IF` an App Bar has no subtitle
>     (`all_app_bars_subtitle_line`), or `IF` no Search App Bar exists at the
>     top of the screen (for example, a screen that only has a `"Search"` tab in
>     the bottom Navigation Bar), `THEN` the corresponding question `MUST` be
>     answered **`"N/A"`** (`MUST NOT` answer `"No"`).

#### All App Bars

1.  [ID: all_app_bars_top_position] Does the “App bar” appear to be positioned
    at the top of its respective screen or pane, above all other elements in
    that area (ex. top of app, sheet, leading pane in a multi-pane layout)?
    [Metric type: Hygiene] [Weight: 5]

2.  [ID: all_app_bars_one_text_element] Does the App bar appear to contain
    EXACTLY ONE (`count == 1`) of the following canonical text elements: a
    headline (with an optional subtitle on a new line), search field hint text,
    or a product brand mark? (Numeric point/reward badges do not count; if the
    top app bar row has `0` canonical text elements—such as an icon-only bar
    above a scrollable body header—or combines `>= 2` text elements, evaluate as
    `"No"`; mobile inbox top search app bars with a single hint string have
    `count == 1` and evaluate to `"Yes"`; mark as N/A if no App bar exists.)
    [Metric type: Hygiene] [Weight: 3]

3.  [ID: all_app_bars_subtitle_line] If an App bar subtitle is present, are all
    subtitles contained in a single line? (Mark as N/A if no App bar or no
    subtitle is present.) [Metric type: Hygiene] [Weight: 3]

4.  [ID: all_app_bars_max_trailing] If an App bar is present, does it have a
    maximum of 3 trailing icon buttons, excluding any icons in the search bar or
    the account particle? (Mark as N/A if no App bar is present, such as when
    only a Bottom Sheet header exists.) [Metric type: Hygiene] [Weight: 3]

5.  [ID: all_app_bars_leading_icon_gm] If a leading navigation icon is present
    in the top app bar, is it implemented using standard GM3 navigation icons:
    arrow_back / arrow_back_ios (or platform equivalent system back arrow) on
    secondary screens, or menu on top-level screens, rendered at 24x24dp with a
    48x48dp interactive bounding touch target? [Metric type: Adherence] [Weight:
    10]

6.  [ID: all_app_bars_overflow_last_right] If there is an overflow icon, is it
    the last icon on the right, for screens in left-to-right languages? [Metric
    type: Hygiene] [Weight: 1]

#### iOS Platform Navigation Adherence

1.  [ID: ios_native_app_bar_usage] In this iOS application, is the top
    navigation bar rendered using Apple native navigation bar chrome
    (UINavigationBar or SwiftUI NavigationStack/toolbar) rather than a custom
    Android/Web-style Material Top App Bar? (Pass with "Yes" if correctly using
    native Apple navigation chrome without penalizing for missing Material
    styling; fail with "No" if incorrectly using a custom Material Top App Bar;
    mark as "N/A" if no top app bar exists or non-iOS.) [Metric type: Adherence]
    [Weight: 10]

2.  [ID: ios_native_app_bar_actions] In this iOS application, if action items
    are present in the top navigation bar, are they rendered as standard
    platform bar button items (`UIBarButtonItem` or SwiftUI `.toolbar` /
    `ToolbarItem`—which on iOS 26+ naturally group inside a shared system Liquid
    Glass pill/circle platter, and on iOS 18 and below appear as plain
    borderless icons) rather than custom Material buttons (`M3CButton`) or a
    Material Button Group (`StandardButtonGroup` / `ConnectedButtonGroup`)?
    (Pass with "Yes" if top navigation actions use standard iOS bar button items
    or the native iOS system Liquid Glass bar platter; fail with "No" if they
    use custom Material button containers, segmented inner-seam radii, or
    `M3CButton`/`ButtonGroup` inside the navigation bar; mark as "N/A" if no top
    bar actions exist or non-iOS.) [Metric type: Adherence] [Weight: 5]

#### Medium flexible + Large flexible App Bars

1.  [ID: med_lg_app_bar_headline_lines] If a Medium or Large flexible app bar is
    present, is the headline text contained in 2 lines or less? [Metric type:
    Hygiene] [Weight: 3]

#### Small App Bars

1.  [ID: small_app_bar_headline_line] If a Small app bar is present, is the
    headline text contained in a single line (e.g., no text wrapping)? [Metric
    type: Hygiene] [Weight: 3]

#### Search App Bar

1.  [ID: search_app_bar_hint_text_search] If a Search app bar is present, does
    the search element contain clear hint text that includes the literal word
    “Search”? (If the hint text uses an AI prompt such as `"Ask Gemini: 'Find
    Sarah's flight'..."` that omits the word `"Search"`, evaluate as `"No"`;
    mark as N/A if no Search app bar is present.) [Metric type: Hygiene]
    [Weight: 3]

2.  [ID: search_app_bar_surface_container] If a Search app bar is present at the
    top of the screen, does the search element appear to use the “surface
    container” color role or a variant (e.g., “surface bright”) to distinguish
    it from the background? (Mark as N/A if no top Search app bar is present,
    even if a “Search” destination tab exists in the bottom Navigation bar.)
    [Metric type: Hygiene] [Weight: 3]

3.  [ID: search_app_bar_centered] If a Search app bar is present, is the search
    bar centered within the app bar? [Metric type: Hygiene] [Weight: 3]

4.  [ID: search_app_bar_max_trailing] If a Search app bar is present and
    trailing icons are used in the search element, are there at most 2 icons
    present? [Metric type: Hygiene] [Weight: 3]

5.  [ID: search_app_bar_avatar_far_right] If a Search app bar is present and a
    user avatar is included, is it placed to the far right of the screen?
    [Metric type: Hygiene] [Weight: 3]

6.  [ID: search_app_bar_leading_menu_logo] If a Search app bar is present on a
    primary/top-level screen, is the leading icon a menu or product logo?
    [Metric type: Hygiene] [Weight: 3]

7.  [ID: search_app_bar_leading_arrow_logo] If a Search app bar is present on a
    secondary screen, is the leading icon an arrow pointing left or a product
    logo? [Metric type: Hygiene] [Weight: 3]

8.  [ID: ios_lg_search_app_bar_layer_adherence] On iOS, if a Search App Bar is
    present, does it correctly enable the translucent Liquid Glass variant when
    placed on the Functional Layer (floating or pinned over content), and remain
    Non-Glass when placed on the Content Layer? (Pass with "Yes" if layer
    placement matches the glass/non-glass variant; fail with "No" if mismatched;
    mark as "N/A" if absent or non-iOS.) [Metric type: Adherence] [Weight: 5]
