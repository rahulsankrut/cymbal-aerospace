---
name: hifi-mockup-kit
description: >-
    Generate high-fidelity static design mock-ups as self-contained HTML files,
    one per screen, composed from the project's Component Kit, and place them on
    the canvas. Use when the user asks to design a screen, page, view, or flow
    and the project has a Component Kit.
---

# Hi-Fi Design Mock-Up

## Overview

A hi-fi mock-up is a static, self-contained HTML snapshot of one screen in the
application's user journey. Use mock-ups to establish visual direction, product
user journey, and information hierarchy.

Produce screens a design lead would ship without rework:

-   **Consistent** — every screen in a set shares one shell and design system
    (colors, typography, spacing, components).
-   **Crafted** — nothing overlaps, overflows, or drifts off the spacing scale.
-   **Complete** — realistic content and user flow states.

## Workflow

1.  **Read context** — `DESIGN.md`, `tailwind.config.js`, and the Component Kit
    (`components/*.html`). These define every token and component you may use.
    If `DESIGN.md` and `tailwind.config.js` do not exist in the project root,
    create them first with the `design-system` skill. If the Component Kit
    (`components/*.html` and the `## Components` section in `DESIGN.md`) does
    not exist, create it first with the `component-kit` skill.
2.  **Plan the set** — For each screen decide its type and archetype and which
    states it must depict. Decide which screens share an app shell.
3.  **Generate serially** — Write one screen at a time.
    -   On the first screen of a shell group, establish the app shell — outer
        container and padding, header, navigation, footer.
    -   For every later screen in that group, copy the shell markup and swap the
        main content.
    -   Screens outside the shell keep their own framing: landing and marketing
        pages, auth, onboarding overlays. Choose their framing once, then hold
        it across the set.
4.  **Write the file** —
    `<workspace-root>/screens/<screen-id>/<ScreenTitle>.html`
5.  **Generate images (before adding to canvas)** — Run `html-image-pipeline`
    from the `generate-image` skill (`WaitMsBeforeAsync=10000`) to replace every
    `src="placeholder"` attribute in-place. Because `run_command` backgrounds
    commands after 10 seconds, if `run_command` returns that the command is
    running in the background, **do not call `stitch-design add` or end your
    turn yet** — wait for the background task completion notification (or verify
    that `src="placeholder"` has been replaced in the HTML file) before
    proceeding to Step 6. Pass `DESIGN.md` as context. Alternatively, generate
    the screen's images upfront with `generate-image --batch_json` into
    `images/` before writing the HTML.
6.  **Add to the canvas** — After all images are generated and the HTML file
    references real image files, add each screen with the `stitch-design-cli`
    skill.
7.  **Run the checklist** — Check every screen against the Checklist at the end.

## Screen Types and Archetypes

Classify every screen by:

-   **type**, which drives navigation and layout
-   **archetype**, which drives required content

### Type

Type            | Examples                       | Navigation                      | Layout
--------------- | ------------------------------ | ------------------------------- | ------
Destination     | Home, Explore, Profile         | Full shared nav, no back button | Standard app shell
Task Flow       | Checkout, Booking form, Editor | Back button, no root tabs       | Focused single-column
Modal / Overlay | Confirmation, Detail sheet     | No nav, floating container      | Centered overlay
Onboarding      | Welcome, Setup wizard          | No nav                          | Full-bleed, step-based
Landing         | Marketing, Product page        | Top site nav, footer            | Full-width sections
Auth            | Sign in, Sign up, Reset        | No app nav                      | Centered single card

The navigation rules are mutually exclusive. When ambiguous, prefer Task Flow —
it is better to omit navigation than to show irrelevant navigation.

### Archetype

| Archetype   | Must include                                                   |
| ----------- | -------------------------------------------------------------- |
| Dashboard   | Glanceable top metrics; single-topic widget cards; quick       |
:             : actions; alert surface                                         :
| List / Feed | Item title and avatar; metadata or timestamp; row-level        |
:             : target; pagination affordance; **empty state**                 :
| Detail      | Entity title; grouped attributes; primary contextual action;   |
:             : back navigation                                                :
| Form        | Labeled inputs; hint text for constraints; primary submit;     |
:             : **one field in its error state**                               :
| Settings    | Grouped sections; toggles; destructive actions isolated at the |
:             : bottom; identity block at top                                  :
| Auth        | Email and password with reveal; forgot-password link; social   |
:             : alternatives; primary sign-in                                  :
| Onboarding  | Step indicator; skip; one value proposition; single primary    |
:             : next                                                           :
| Checkout    | Order summary with total; segmented card inputs; trust signal; |
:             : `Pay $X` button                                                :
| Profile     | Avatar; name and handle; bio; links; primary action            |
| Data table  | Distinct headers; sort and filter controls; uniform row        |
:             : padding; row action menu; pagination                           :

## HTML Boilerplate

Every file is a complete, self-contained HTML document. Always inline the full
`tailwind.config = { ... }` object directly in a `<script>` tag — **never** use
`<script type="module">import config from '../tailwind.config.js'` or
`'../../tailwind.config.js'` in screen HTML files, because relative ES module
imports fail when screens are rendered on the canvas.

```html
<html lang="en">
<head>
  <script src='https://cdn.tailwindcss.com?plugins=forms,container-queries'></script>
  <script>tailwind.config = { /* the object from tailwind.config.js, without `export default` */ }</script>
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet">
  <!-- REQUIRED: a <link> for every non-system fontFamily in the config -->
</head>
```

### Critical Layout Rule

Use `min-h-screen`, never `h-full` or `h-screen`, on `<body>`, root layout
elements, and persistent `<aside>` sidebars. In `srcdoc` iframes percentage
heights resolve to 0px because there is no fixed-height ancestor; `min-h-screen`
resolves to `100vh` and works.

Prefer `sticky top-0` over `fixed top-0` for top navigation bars so full-page
screenshots do not duplicate the header across scroll tiles. Never set initial
`opacity-0` on hero headings or primary content that relies on JavaScript timers
to become visible. Standard Tailwind `grid-cols-*` utilities only exist up to
`grid-cols-12`; for higher column counts (such as a 52-week heatmap), use
explicit arbitrary grid templates like `grid-cols-[repeat(52,minmax(0,1fr))]`.

## Responsive Design

Pick the primary viewport from the prompt: mobile-first (~390px) for phone and
app requests, desktop (~1280px) for dashboards and web apps. Default to mobile
when ambiguous.

Express breakpoint changes with Tailwind prefixes (`sm:`, `md:`, `lg:`, `xl:`),
not `@media` blocks. Going down from desktop, collapse multi-column grids to one
column, move sidebars behind a toggle, and switch to `-mobile` typography
tokens.

## Design Tokens Adherence

Follow instructions in `design-system` skill on how to use design systems.

Read `DESIGN.md` and embed the full `tailwind.config.js` in every file. Every
visual value comes from a token. Follow the prose in `DESIGN.md` (elevation
strategy, shape language, voice) as strictly as the tokens.

**Color.** Use named tokens (`bg-primary`, `text-on-primary`). Colors the system
defines per mode carry a `light-`/`dark-` prefix (`bg-light-surface`,
`text-dark-on-surface`). Never arbitrary hex (`bg-[#a3defe]`), never generic
Tailwind colors (`bg-emerald-400`).

**Typography.** Every text element gets one `font-<role>` class
(`font-headline`, `font-body`) and one `text-<level>` class (`text-headline-lg`,
`text-body-md`). Never arbitrary values (`text-[32px]`, `font-[Inter]`), never
generic classes (`text-2xl`, `font-sans`).

**Mobile typography.** Where a level has a `-mobile` counterpart
(`headline-lg-mobile`), you MUST use it on mobile screens and the base token on
desktop.

**Spacing, sizing, and radius.** Take every value from the design system's
scale. Never invent an arbitrary pixel value (`p-[13px]`, `gap-[11px]`,
`rounded-[14px]`). Where the system defines no token for what you need, stay on
its grid step. When nesting a rounded element inside a padded container, step
the inner radius down — inner ≈ outer − padding.

**Dark mode.** Every `dark:` color class needs an unconditional class for the
same property on the same element: e.g. `bg-light-surface dark:bg-dark-surface`.

## Component Adherence

Look for the appropriate component in the component kit (see `component-kit`
skill).

-   **Copy verbatim by default; explicit user prompt constraints win.** Change
    only text content and placement by default. Never arbitrarily edit a
    component's structure and attributes. However, if the user's prompt
    explicitly requires or forbids specific UI sub-elements, states, or layout
    details (for example, forbidding a search bar or notification icon, or
    requiring a specific empty/zero-value card border), adapt or trim the
    component markup so every explicit prompt constraint is satisfied. If you
    need a component the Kit lacks, build it from the established design
    language and reuse existing parts as much as possible.
-   **Keep the data attributes.** Preserve `data-component-id`,
    `data-component-type`, and `data-component-variant`. Wrap every visible text
    node in an element carrying `data-design-text-token` for the typography
    token used, e.g. `<span data-design-text-token="label-lg">Submit</span>`.

## Consistency Contract

All screens must have internal and cross-screen consistency.

-   **Same component, same rendering.** Elements sharing a `data-component-id`
    must have identical dimensions and styling.
-   **Same text token, same type.** Elements sharing a `data-design-text-token`
    render at the same size and weight everywhere.
-   **Same shell.** Header, navigation, footer, outer container, and page
    padding are identical across every screen in a shell group.
-   **Same world.** User names, balances, dates, tickers, and every other domain
    entity stay consistent from screen to screen.

## Layout and Composition

**Grid first.** Build page layout, column splits, and card collections with CSS
Grid. Use subgrid where tracks must line up across nested containers. Reach for
grid before stacking flex wrappers.

**Space with `gap`, not margins.** Siblings are spaced by `gap-*` on their grid
or flex parent, never by `mt-*` / `mb-*` on the children.

**Align every row.** Horizontal flex rows holding icons, labels, or controls get
`items-center`, or `items-baseline` for text-only headers.

**Let content size the box.** Never set a fixed height on a container holding
text; use `min-h-*` if you need a floor. A box that overflows itself was sized
from the outside.

**Equal-height rows.** Card rows use `grid grid-cols-* items-stretch` with
`h-full` on the cards, so siblings match without hand-tuning.

**Layer deliberately.** Sticky headers, fixed docks, and floating buttons need
an explicit `z-index` and matching offset padding on the content beneath.

## Typography

**Line length** — Body copy runs 45-75 characters. Bound it with `max-w-prose`
or a grid track.

**No runts, no wraps** — Add `text-balance` to multi-line headings and
`text-pretty` to body paragraphs so no single word is stranded on the last line.
Keep button, chip, and badge labels short enough not to wrap.

**Numbers** — Currency, percentages, metrics, timestamps, and table figures
carry `tabular-nums`. Number and date formats stay identical across screens.

## Color and Contrast

**Use matching foreground and background color pairs.** **Pair surfaces with
their `on-` tokens.** Each surface token has a matching foreground token; use
the pair. Never place a `text-*` token on an unrelated `bg-*` — that is where
contrast failures come from.

**Semantic colors mean something.** Success, warning, and error hues carry state
only. Never use them decoratively.

**Elevation steps outward** — `surface` → `surface-container-low` →
`surface-container`. In dark mode use deep neutrals, never pure `#000000`, which
makes light text halate.

## Content and States

**Use Semantic HTML.** Use `<header>`, `<footer>`, `<nav>`, `<main>`,
`<section>`, etc.

**Write real content.** No `Lorem ipsum`, no `John Doe`, no `example.com`, no
repeated copy across sibling cards. Every card in a collection gets its own
domain-authentic text and plausible numbers.

**Label actions with verbs.** `Export CSV Report`, `Transfer $2,400` — not
`Submit`, `OK`, or `Continue`.

**Vary the rhythm.** Not every section at the same height, density, and layout.

### Images

Every image starts as a placeholder that the image pipeline fills in. Each one
needs a placeholder source plus three attributes:

-   **`data-alt`** — the generation prompt. 3-5 sentences, 50-100 words.
-   **`data-aspect-ratio`** — one of `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `9:16`,
    `16:9`.
-   **`data-img-id`** — a stable, unique, kebab-case id (`hero-image`,
    `card-thumbnail-yoga`). Reusing an id preserves an already-generated image
    across iterations instead of regenerating it.

```html
<img src="placeholder"
     data-alt="A detailed 50-100 word prompt..."
     data-aspect-ratio="16:9"
     data-img-id="hero-mountain-sunrise"
     class="w-full h-64 object-cover rounded-xl">
```

For a background image, put `style="background-image: url('placeholder')"` on
the element and add the same three attributes. Without a placeholder source the
injection pipeline cannot find the element.

**Writing `data-alt`.** This is a generation prompt, not alt text. Describe
subject, setting, mood, lighting, and visual style, concretely. Prompts are
generated independently and in parallel, so decide one visual style statement
for the screen — for example "flat illustration, warm earth tones, light cream
background" — and embed it in *every* prompt on the page. Subjects must fit the
product's domain and intent.

-   Too short: `"A minimalist digital art installation."`
-   Right: `"A striking digital installation art piece featuring glowing,
    generative geometric shapes suspended in a vast, minimalist gallery space.
    The room is lit by high-key, soft white light for a bright, modern
    light-mode aesthetic. The palette is deep blacks and pristine whites,
    punctuated by intense accents of vibrant red. The mood is serene yet
    technologically advanced."`

**Never reference an external image URL** — no stock photo or placeholder
service of any kind. They do not render in the sandboxed environment. **Never
emit `data:image/...` URIs**. Use Tailwind gradient and pattern utilities for
decorative fills.

### Icons

Material Symbols is loaded. Use `<span
class="material-symbols-outlined">icon_name</span>`, adding
`style="font-variation-settings: 'FILL' 1;"` for the filled state. Keep fill and
weight uniform within a screen. Never use an emoji as an icon.

### Motion

Animate `transform`, `opacity`, and color only. Never put `transition-all` on an
element that also sets geometry (`w-*`, `h-*`, `max-w-*`, `top`, `left`) — it
animates layout. Animated SVG children (`<circle>`, `<path>`, `<rect>`, `<g>`)
need `style="transform-box: fill-box; transform-origin: center;"`.

## Avoid These Defaults

These are the patterns a generator reaches for unprompted. None belong in a
crafted screen:

*   Purple-to-blue or indigo-cyan gradients
*   Neon glow blobs on dark surfaces
*   Gradient text on headings (`bg-clip-text text-transparent`)
*   Uppercase eyebrow chip above every section
*   Decorative `01 / 02 / 03` numbered badges
*   `border-l-4` accent stripes on cards
*   Symmetric three-column icon-title-description card grids
*   Containers nested more than two levels deep
*   Hairline borders paired with heavy shadows
*   Buzzword copy ("Reimagine", "Seamlessly", "Elevate")
*   Pulsing dots that signify nothing

## Checklist

1.  **Shell parity** — does this screen's header, navigation, footer, and page
    padding match the rest of its shell group exactly?
2.  **Token adherence** — any arbitrary hex, pixel, or generic Tailwind value,
    or a class that is not in `tailwind.config.js`?
3.  **Content realism** — any placeholder names, repeated card copy, or
    suspiciously round numbers?
4.  **State completeness** — does this archetype need a state that is missing?
5.  **Archetype coverage** — is every "must include" item present?
6.  **Slop scan** — anything from *Avoid These Defaults*?
7.  **Canvas** — is every new screen on the canvas?
