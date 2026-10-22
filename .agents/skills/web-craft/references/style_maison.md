---
name: Maison
slug: maison
register: classic
mode: dark
---

# Maison

## Identity

**North Star: "Ivory on Espresso, After Dark."** A couture house's evening
issue: espresso-black ground, ivory type, and champagne hairlines. A thin
high-fashion display face over widely tracked small capitals, a centered
masthead, and a great deal of dark, quiet space. Hushed, expensive, and
nocturnal — never flashy, never gold-foil glitz.

-   **Mood**: hushed, luxurious, nocturnal, assured.
-   **Inspired by**: evening couture lookbooks, apothecary and fragrance
    ateliers, fine-horology archives, and nocturnal luxury editorials.

## When to Use

-   **Best for**: fashion, luxury goods, fine dining and menus, perfume, film,
    nightlife, premium culture (galleries, opera, archives), brand stories.
-   **Avoid for**: dense dashboards and operational tools, technical or
    scientific content, public services, children's material, anything that
    needs to feel cheerful, urgent, or plain.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Italiana&family=Jost:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: dark;

  /* Page and surfaces */
  --background: #15110e;               /* espresso black */
  --surface-container-low: #1f1915;    /* a step lifted, for inset panels */
  --surface-container: #2a231d;        /* roasted brown, for a rare filled panel */
  --surface-container-high: #352c25;   /* menus and popovers only */

  /* Type */
  --on-surface: #f1ebe1;               /* ivory: headlines and body */
  --on-surface-variant: #b3a693;       /* warm stone: ledes, captions, secondary text */

  /* Rules */
  --outline: #665943;                  /* champagne hairline (45% on espresso), never text */
  --outline-variant: #544937;          /* fainter champagne divider, never text */

  /* Accents */
  --primary: #f1ebe1;                  /* ivory: the primary action, the key value */
  --on-primary: #15110e;
  --primary-container: #2e271d;        /* selected rows, active nav */
  --on-primary-container: #f1ebe1;
  --secondary: #9a8a77;                /* taupe: tracked labels and tags */
  --tertiary: #c9b083;                 /* champagne: kickers, notable captions, links */
  --error: #e08a7e;                    /* muted rose-claret */
  --on-error: #15110e;

  /* Data series, in order of use */
  --data-1: #c9b083;                   /* champagne */
  --data-2: #f1ebe1;                   /* ivory */
  --data-3: #b98676;                   /* dusty rose */
  --data-4: #7f97a0;                   /* smoke blue */
  --data-context: #6e6256;             /* context series and baselines */

  /* Fonts */
  --font-headline: 'Italiana', serif;
  --font-body: 'Jost', sans-serif;
  --font-label: 'Jost', sans-serif;

  /* Shape */
  --rounded: 0;
  --rounded-lg: 0;
  --rounded-full: 0;                   /* square even for tags and pills */

  /* Style effects */
  --hairline: 1px solid var(--outline);
  --hairline-soft: 1px solid var(--outline-variant);
  --tracking-mast: 0.6em;              /* labels above headings */
  --tracking-label: 0.24em;            /* labels, kickers, chips */
  --tracking-button: 0.22em;
}
```

## Color

-   **Proportions**: espresso carries the page — roughly 85% of what the reader
    sees is dark ground. Ivory is the type. Champagne is the jewelry (under 5%):
    a label above the title (when used), the subline under the title, hairlines,
    a caption that deserves notice, and the series that matters. Taupe is the
    voice of small labels.
-   **The accent is champagne, not a hue.** There is no saturated color in
    this style. The primary action is ivory on espresso; emphasis comes from
    champagne and from scale, never from a bright fill.
-   **Rules are never text.** `--outline` and `--outline-variant` (under 3:1)
    are for hairlines only. Champagne `--tertiary` (9:1) and taupe
    `--secondary` (5.6:1 on the page, 4.6:1 on `--surface-container`) carry
    text; taupe never sits on `--surface-container-high`.
-   **Fills are rare.** Separate with space and champagne hairlines. Use
    `--surface-container-low` only for a panel that must read as an object (a
    form, a booking widget); never a light card on the dark page.

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display, headlines | Italiana | 400 (its only weight) | Large: step the display size up. Line height 1.02–1.1, tracking 0 to 0.01em. Never bold, never faux-italic. |
| Body | Jost | 400; 400 italic for emphasis | At least 17px for narrative. Line height 1.6–1.7. |
| Ledes, standfirsts | Jost | 300 | 1.1–1.2× body, in `--on-surface-variant`, centered measure of about 48ch. |
| Labels, kickers, chips | Jost | 400 uppercase | 0.75rem, tracking `var(--tracking-label)`; in `--secondary`, or `--tertiary` for the kicker. |
| Figures | Italiana for display values; Jost for tables | 400 | Key values in the display face; lining tabular figures (`tabular-nums`) in Jost for tables and axes. |

Headlines are title case or sentence case, never all caps — the capitals
belong to the small tracked labels. Contrast comes from a tall, thin display
face at large size against tiny, wide, upright labels; nothing in between.

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies; use
it wherever the artifact has that place. When there is room for only a few, keep
the higher-ranked ones.

### 1. Thin display title with champagne subline

The opening title and major section titles: Italiana, large and light on its
feet, centered, with the subtitle or dateline beneath it as a tracked
champagne capital line. The pairing — tall thin serif over tiny wide caps — is
the house voice.

```css
.title {
  font-family: var(--font-headline);
  font-weight: 400;
  font-size: var(--display-size);
  line-height: 1.02;
  letter-spacing: 0.01em;
  color: var(--on-surface);
  text-align: center;
}
.title + .subline {
  margin-top: var(--space-md);
  font-family: var(--font-label);
  font-size: var(--label-size);
  text-transform: uppercase;
  letter-spacing: var(--tracking-label);
  color: var(--tertiary);
  text-align: center;
}
```

### 2. Hairline-topped figures

Key figures, cards, and list entries are not boxes: each sits under a single
champagne hairline, centered, with no fill — a taupe label, the value in the
display face, a champagne caption. Use the same top rule for section openings
and chart blocks.

```css
.figure {
  border-top: var(--hairline);
  padding-top: var(--space-md);
  text-align: center;
  background: transparent;
}
.figure .value { font-family: var(--font-headline); font-size: var(--headline-size); color: var(--on-surface); }
.figure .caption { font-weight: 300; color: var(--tertiary); }
```

### 3. Wide-tracked small capitals

Every small piece of type — labels, kickers, tags, button text, table headers,
axis titles — is uppercase Jost at label size with wide tracking, in taupe.
This uniform small voice is what makes the page feel expensive.

```css
.label {
  font-family: var(--font-label);
  font-weight: 400;
  font-size: var(--label-size);
  text-transform: uppercase;
  letter-spacing: var(--tracking-label);
  color: var(--secondary);
}
```

## Composition

-   **Centered, like a house's title page.** Masthead, title block, key-figure
    rows, and button groups sit on the page's central axis. This overrides the
    general preference for asymmetry.
-   **Body text is not centered.** Paragraphs sit left-aligned in a centered
    measure of 58–64ch; only the lede is centered.
-   **Sparse and dark.** Wide margins and long pauses between sections; the
    dark ground is the luxury. Separation comes from space and hairlines —
    no fills, no shadows.
-   **Dashboards and tools** keep the centered masthead and title, but their
    grids are left-aligned, denser, and divided by `--hairline-soft`.

## Components

-   **Labels above headings** (when used): small Jost capitals in champagne,
    tracked 0.6em (`--tracking-mast`), centered, with a full-width champagne
    hairline beneath.
-   **Buttons**: square. Primary is an ivory fill with espresso text; secondary
    is a champagne hairline outline with champagne text. Labels in wide-tracked
    capitals (`--tracking-button`). Hover on primary shifts the fill to
    champagne; on secondary, it fills with `--primary-container`. No shadows.
-   **Key figures**: see treatment 2 — nothing around them but a top hairline.
-   **Tags / chips**: no box; a tracked taupe capital label, optionally with a
    champagne hairline beneath. Square if they must be outlined.
-   **Links**: champagne text with a 1px underline in `--outline`, offset 4px;
    hover brings the underline to champagne.
-   **Inputs**: transparent field with a hairline beneath; labels above in the
    small-caps voice; focus turns the line ivory and adds the focus ring.
-   **Tables**: no vertical lines and no zebra fills. A champagne hairline under
    the header, `--hairline-soft` between rows; header cells in the label voice;
    tabular figures in Jost.
-   **Navigation**: centered tracked capitals with generous gaps
    (`var(--space-xl)`), no separators; active item in ivory, others in taupe.

## Data Visualization

-   **Series**: `--data-1` (champagne) for the series that matters, then ivory,
    dusty rose, smoke blue. Everything else is `--data-context`.
-   **Lines and marks**: 1–1.5px lines, as thin as the hairlines; small square
    or hollow markers. No area gradients, glows, or 3D.
-   **Axes and gridlines**: axis labels in the label voice; gridlines in
    `--outline-variant`, horizontal only; no chart frame.
-   **Labels and annotations**: label series directly at their ends in Jost
    300; annotations in champagne with a hairline leader.
-   **Chart titles**: Italiana at subhead size, centered, under a hairline.

## Motion

Slow and composed, like house lights dimming: fade in with a slight upward
drift over `--dur-long` with `--ease-out`, gently staggered. No bounces,
springs, shimmers, or scale effects.

## Don'ts

-   No gold gradients, metallic foils, or glows; champagne is a flat hairline
    color, not bling.
-   No bold or faux-italic Italiana, and no Italiana for body or small text.
-   No light cards on the dark page, no rounded corners, no drop shadows.
-   Don't set labels in sentence case or tight tracking — untracked small type
    instantly reads as generic.
-   Don't add a saturated accent color; the palette is espresso, ivory,
    champagne, and taupe.
-   Don't center long paragraphs.

## If the User Asks for Light

Keep the roles on a pale ivory ground, as for a daytime edition:
`--background: #f6f1e8`, `--surface-container-low: #efe8dc`,
`--on-surface: #15110e`, `--on-surface-variant: #5b4f42`, `--primary: #15110e`
with `--on-primary: #f6f1e8` (espresso button), `--secondary: #6b5d4e`,
`--tertiary: #7a6136` (a deeper champagne that keeps 4.5:1 for text),
`--outline: #c9b083`, `--outline-variant: #e0d3bb`. Hairlines, tracking, and
composition stay the same.
