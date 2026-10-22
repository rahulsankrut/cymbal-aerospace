---
name: ui-design
description: >-
  Gives general principles for designing web and app UIs and a workflow for new
  designs and redesigns. Covers deriving a visual direction from the audience
  and context, then color, typography, layout, shape, imagery, components, data
  visualization, motion, and accessibility, with clearly marked example
  defaults. The workflow covers screenshot baselines, agreeing on a direction,
  building design tokens, reviewing every interactive state, checking load
  performance on production builds, and sharing before/after results. Use when
  designing a new app or screen, redesigning, restyling, or modernizing a UI,
  choosing a palette, fonts, or theme, polishing UI across many pages, taking
  UI screenshots for review, or sharing before/after results in a CL. Don't use
  for critiquing a single mockup (use product-taste), full accessibility audits
  (use web-accessibility), or generating mockups in design tools.
metadata:
  icon: 🎨
---

# UI Design

Two parts: principles for making design decisions for any product, and a
workflow for building or redesigning it. The principles don't prescribe a style;
the audience, the context, and the brand do. Concrete values appear only in
[Example defaults](#example-defaults), as illustrations.

## Design principles

### Start from the audience and context

A design works for particular people in a particular setting. Before choosing
colors or fonts, find out the following, and ask the user when the request
doesn't say:

-   **Who**: experts or newcomers, daily or occasional users, age, languages,
    reading level, and comfort with technology.
-   **Where and how**: at a desk or outdoors, on a phone or a large screen, in
    bright sun or a dim room, on a fast or slow network, with touch, mouse,
    keyboard, or voice.
-   **What for**: the few tasks that matter most, and whether people mostly scan
    data, read, create, or converse.
-   **Constraints**: brand guidelines, an existing design system or component
    library, platforms, and languages. These override everything in this skill.

The answers drive every later choice. A dashboard that analysts use all day
calls for density, keyboard shortcuts, and a quiet palette. An assistant used on
a phone outdoors calls for large text and touch targets, strong contrast, plain
language, and pages that load on a slow connection.

### Write a design direction

Agree on these with the user, in a few lines, before styling anything. Each one
affects every screen, so changing it later is expensive:

-   **Personality**: two or three words, such as "calm, precise" or "warm,
    encouraging". Use them to settle later choices.
-   **Density**: base text size, control size, and spacing, set by the audience
    and device.
-   **Color**: a neutral family and its temperature, one main accent and where
    it comes from (the brand, the logo, or the users' world), and status colors.
-   **Type**: one or two families that fit the personality and cover every
    language needed.
-   **Shape**: how rounded corners are. Sharper reads precise; rounder reads
    friendly.
-   **Depth**: flat with borders, soft shadows, or strong elevation.
-   **Imagery**: the icon set and style, and whether illustrations or photos
    have a job.
-   **Motion**: minimal and functional, or more expressive.

### Color

-   Define colors by role (background, surface, text, muted text, border,
    accent, status), not as a loose list of hex values. Elements use roles, so
    changing the palette or adding a dark theme is a small edit.
-   Build each hue as a scale from light to dark in even steps. Pale steps are
    for backgrounds, middle steps for borders and fills, dark steps for text.
-   Give color a job: the primary action, selection, focus, status, a category,
    or brand identity. Color used everywhere stops carrying meaning. Brand-led
    products can use color boldly, but on purpose.
-   Use one main accent. Add another only for a distinct job, such as categories
    or data series.
-   Match the grays to the personality: cool grays read technical, warm grays
    read friendly and organic. Tinting grays slightly toward the accent makes
    the palette feel related.
-   Keep familiar status colors (green for success, amber for warnings, red for
    errors) unless the audience reads colors differently. If the accent shares a
    status hue, as a green brand does, make the two clearly different shades and
    label statuses with icons or text.
-   Pure black on pure white is harsh for long reading; very dark gray text is
    easier. In bright light, favor more contrast, not less.
-   Dark theme: dark gray rather than black, lighter surfaces instead of shadows
    for raised layers, and a lighter, less saturated accent.

### Typography and copy

-   Pick type for the personality and the reading conditions. Humanist sans
    faces feel friendly and stay legible when small, geometric sans faces feel
    modern, serifs feel editorial or traditional, and monospace suits code and
    aligned data.
-   Check that the font covers every language and script needed, has the weights
    you use, and isn't too heavy to download.
-   Set the base size from the audience: about 14 px for dense expert tools, 16
    px for most sites, and larger for phones, older users, or less confident
    readers.
-   Use one or two families and a short size scale. Build hierarchy with weight,
    color, and space before adding sizes.
-   Keep body line height around 1.5 and prose lines under about 75 characters.
-   Write in the users' words. Buttons say what happens ("Save changes"), errors
    say what went wrong and how to fix it, and empty screens say what to do
    next.
-   Align numbers in columns with tabular figures.

### Layout and spacing

-   Use one spacing scale built on a base unit (4 or 8 px), with more space
    between groups than within them.
-   Give each screen one main purpose, put the most important content and action
    first, and reveal detail on demand.
-   Group with space first, then dividers, then background tints. Avoid boxes
    inside boxes.
-   Align content to a few shared edges, and keep the page frame (header,
    navigation, margins) the same on every screen.
-   Design for the smallest screen people actually use, then add columns as
    space allows.
-   Fit navigation to the number of destinations: a few need tabs or a bottom
    bar; many need a sidebar or search. Frequent users benefit from keyboard
    shortcuts.
-   Long collections need a way to find things: search, filters, grouping, and
    counts.

### Shape, depth, and imagery

-   Use one corner radius scale that matches the personality, everywhere. A
    nested element's radius is the outer radius minus the gap between them.
-   Use one depth approach consistently. In any style, layers that float over
    the page (menus, dialogs, toasts) need clear separation from it.
-   Use one icon set in one style and stroke weight, at a few fixed sizes. Label
    icons unless the meaning is universal, and give icon-only buttons an
    accessible name.
-   Use illustrations and photos where they help: explaining a step, making
    onboarding or empty screens welcoming, or helping people who rely on
    pictures more than text. Keep one style. In dense work tools they usually
    compete with the content.

### Components and states

-   Make one action per screen the primary one and keep the others quieter.
    Destructive actions look different and ask for confirmation or offer undo.
-   Give every interactive element hover (for pointers), pressed, focus-visible,
    and disabled states, plus selected, loading, and error where they apply.
    Hover is subtler than selected.
-   Make touch targets at least 44 px on touch screens.
-   Acknowledge every action within about 100 ms, even if only with a progress
    indicator. Show loading content as placeholders shaped like the final
    layout.
-   Show errors next to their cause, in words people can act on.

### Data visualization

-   Pick the chart for the question: lines for trends over time, bars for
    comparisons, a table when exact values matter.
-   Highlight what matters and mute the rest: context in a quiet color, the
    focus in the accent.
-   Keep each series' color the same across screens, use palettes that stay
    distinct for color-blind users, and label lines directly where possible.
-   Keep grid lines faint, and pair charts with the key numbers they show.

### Motion

-   Use motion to explain a change: something opening, closing, moving, or
    loading. Keep it short (about 100–300 ms) and eased. Expressive brands can
    use more, but motion never makes people wait.
-   Animate opacity and transform, which stay smooth, and respect
    `prefers-reduced-motion`. Only loading indicators loop.

### Accessibility floor

These hold for every direction and brand:

-   Contrast: 4.5:1 for text; 3:1 for large text, icons, control borders, and
    focus indicators. Check each text and background pair, including tinted and
    hovered surfaces.
-   A visible focus indicator on every interactive element, and everything
    usable by keyboard.
-   Meaning never carried by color alone; pair it with text, an icon, or
    position.
-   Layouts that survive 200% zoom and longer translated text.
-   For a full audit, use
    [web-accessibility](/learning/gemini/agents/skills/accessibility/web_accessibility/SKILL.md).

### Common mistakes

-   A style reused from a template or another project that doesn't fit the
    audience.
-   Color without a job, or several accents competing.
-   Inconsistent corner radii, type sizes, spacing, or icon styles.
-   Decoration (gradients, glows, heavy shadows) competing with content.
-   Light gray text that looks refined and fails contrast.
-   Designing only for your own screen when people use phones, or the reverse.

## Example defaults

These show how the principles turn into values for two different briefs. They
are illustrations, not a house style: derive values from your own brief, and
replace anything that doesn't fit it.

**Brief A: an internal dashboard that engineers use all day.**

-   Direction: calm, precise, dense.
-   Color: cool grays tinted toward a brand blue. The blue marks only the active
    tab, links, focus, selection, and the highlighted chart series, and
    near-black primary buttons keep it rare.
-   Type: a neutral sans such as Inter (or Google Sans Text in Google products)
    at 14 px, plus a monospace for IDs and code.
-   Shape and depth: 6–8 px corners on controls and 12 px on cards; borders on
    flat surfaces and soft shadows only on menus and dialogs.
-   Components: 36 px buttons and inputs, 40 px table rows, tabs with a thin
    underline, and a faint gray hover tint.
-   Motion: quick fades of 120–260 ms.

**Brief B: a chat assistant that farmers use on their phones in the field.**

-   Direction: warm, plain, reassuring.
-   Color: warm grays and an accent from the users' world, such as a leaf green
    or a soil brown, with high contrast throughout for sunlight.
-   Type: a humanist sans at 17–18 px that covers the local languages, and short
    sentences.
-   Shape and depth: rounder corners (12–20 px) and large message bubbles that
    clearly separate the user from the assistant.
-   Components: 48 px touch targets, a large input with a voice button,
    suggested replies as chips, and pictures where they explain faster than
    words.
-   Performance: few fonts and small pages, since networks are slow.

A method to build a palette from any brand color, the full token set for brief
A, component sizes, and a contrast checker:
[references/tokens.md](references/tokens.md).

## Workflow for new designs and redesigns

1.  **Capture the baseline** before touching any code (redesigns).
2.  **Inventory** pages, states, components, and style sources (redesigns).
3.  **Agree on a direction** with the user, shown on one sample screen.
4.  **Build** tokens, then shared components, then screens.
5.  **Review** after each milestone: re-shoot, compare, check states.
6.  **Measure performance** on production builds.
7.  **Share** screenshots or a before/after report and a reviewable CL.

New designs start at step 3. Copy this checklist and keep it updated:

-   [ ] Redesigns: baseline screenshots of every page and state in `before/`
-   [ ] Redesigns: inventory and plan written; recolor or rebuild per component
-   [ ] Audience and context known; design direction approved on one screen
-   [ ] Tokens on `:root`; framework theme mapped to them
-   [ ] Shared components styled, then screens
-   [ ] Every screen and state shot and reviewed; hover and focus checked
-   [ ] Linters and type checks clean
-   [ ] Load metrics and bundle size measured on production builds
-   [ ] Screenshots or before/after report linked in the CL description

### 1. Capture the baseline first

Once styles change, the old UI is gone from your dev server. Getting it back
means stashing work or building an old revision, and every later comparison,
review, and report depends on these shots.

-   **Shot list**: every page or route, plus the states users see: hover,
    keyboard focus, selected, disabled, open menus, dialogs and side panels,
    loading, empty, error, long text, the largest real data set, and a narrow
    window.
-   **Fixed conditions**: the same viewport sizes (the ones people use, such as
    a laptop and a phone), device scale factor 1, and the same account and data
    for before and after. Pairs with different data can't be compared.
-   **Names**: `ui_shots/before/NN_page_state.png`, then `after_v1/`,
    `after_v2/`, with identical file names in every set so scripts can pair
    them. Never overwrite `before/`.
-   **Script it**: write one capture script that takes an output directory, so
    re-shooting after each milestone is one command.
-   **Access**: if the app needs sign-in or a backend, pick one way to reach it
    headlessly (corp auth, a local auth proxy, or fixture data) and use it for
    both sets.
-   **Late start**: if code already changed, capture the baseline from the
    deployed app or from a second workspace at the base revision.

Recipes for page, element, hover, focus, and menu shots, and for comparing sets:
[references/screenshots.md](references/screenshots.md).

### 2. Inventory before restyling

-   **Style sources**: list global stylesheets, theme and token files, component
    styles, framework theme settings, inline styles in templates, and font or
    icon loading in the HTML entry point.
-   **Hard-coded values**: search the client code for color literals outside the
    token files (regex `#[0-9a-fA-F]{3,8}\b|rgba?\(`), and likewise for shadows
    and font sizes. Token changes won't reach these, so plan to replace them.
-   **Shadow DOM**: in web-component apps, global selectors don't reach inside
    components, but CSS custom properties are inherited into them. Tokens are
    the lever; component internals change in each component's own styles.
-   **Recolor or rebuild**: rank components by how much users look at them. The
    top ones (the header and navigation, the main list, table, or conversation,
    pickers, charts) usually need a new layout, not new colors. A recolor alone
    leaves users saying "this didn't change".
-   **Plan**: write down the pages, the shared components with a recolor or
    rebuild decision for each, and the order of work. Share it with the user.

### 3. Agree on a direction early

-   Ask about the audience and context, then propose a
    [design direction](#write-a-design-direction) with a suggested choice and a
    one-line reason for each item. Ask for apps the user likes and, for
    redesigns, what must not change (layout, workflows, shortcuts).
-   Style one representative screen end to end and show it before rolling the
    style out. Changing direction after dozens of components is expensive.
-   Start a dev server now and share its link. Users find problems faster by
    clicking around than by reading summaries.
-   List open judgment calls as short questions (for example "primary buttons:
    near-black or accent?") so the user can answer them in one reply.

### 4. Build: tokens, shared components, then screens

-   **Tokens first**: turn the direction into tokens with
    [references/tokens.md](references/tokens.md). Define them on `:root`:
    dialogs, menus, tooltips, and toasts often render in an overlay container
    attached to `body`, outside the app element, and miss tokens defined lower.
-   **Framework theme**: point the component library's theme variables at your
    tokens instead of overriding component internals one by one.
-   **Order**: shared components (buttons, inputs, cards, tables, tabs, dialogs,
    empty and loading states), then screens. In redesigns, replace the
    hard-coded values from the inventory as you go.
-   **Rebuilds**: for components marked "rebuild", apply the layout and data
    visualization principles above, not just the new colors.
-   **Lint early**: run the project's linters and type checks after the first
    few components. Styling code often breaks project rules (no inline styles,
    typed or quoted style maps), and fixing a hundred files at the end is slow.

### 5. Review after each milestone

1.  **Confirm the served build has your change** before asking anyone to look:
    fetch the served CSS or JS and search for a new class or token, or `eval` a
    computed style. Stale bundles (another build writing the same output, a
    cache, a service worker) cause false "nothing changed" reports.
2.  **Re-shoot** into `after_vN/` with the capture script.
3.  **Compare** with side-by-side pairs and a contact sheet. Flag pairs with
    zero changed pixels: planned changes that didn't land.
4.  **Check states**: hover, focus, selected, and disabled on every interactive
    component. These are the most often missed.
5.  **Check the console**: a warning repeated thousands of times usually means a
    render loop or a per-row warning. Check whether it also appears in a
    production build before chasing it.
6.  **Update the user**: dev server link, the pairs, what changed, and open
    questions.

When the user reports a visual problem, ask for a screenshot and the exact page
and state, reproduce it in your capture, and re-shoot that state after the fix.

Keep a running list of changes per page and of judgment calls. The CL
description, the report, and status updates then become quick edits.

### 6. Measure performance on production builds

Visual work often slows the first load: new web fonts, a full icon font (several
MB), more CSS, heavier components. Dev servers serve unminified, uncompressed
code and misstate load time by seconds, so compare the baseline and your change
as production builds, on the same machine, taking the median of 3 runs.

Track first paint, LCP, and bytes (JS, CSS, fonts), and explain any growth.
Recipes and common fixes (static app shell, icon font subsetting, font loading):
[references/performance.md](references/performance.md).

### 7. Share the result

-   For redesigns, build a before/after page with one slider per page and a grid
    of states, and link it at the top of the CL description. For new designs,
    share the main screens and states the same way. See
    [references/report.md](references/report.md).
-   State what you verified and how: tests, linters, screenshot sets, and the
    performance table.
-   A restyle touches many files. Offer to split it: tokens and shared
    components first, then screens.

## Related skills

-   [gbrowser](/learning/gemini/agents/skills/gbrowser/SKILL.md): headless
    browser flags, auth modes, and batch actions.
-   [product-taste](/learning/gemini/agents/skills/product_taste/SKILL.md):
    critique of a single design or mockup.
-   [snipit](/learning/gemini/agents/skills/snipit/SKILL.md): upload one
    screenshot to share in chat or a bug.
