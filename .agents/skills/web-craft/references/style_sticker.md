---
name: Sticker
slug: sticker
register: expressive
mode: light
---

# Sticker

## Identity

**North Star: "Joyful Pop."** Die-cut sticker sheets and playful pop: hot pink,
grape purple, and sky blue on a pink-white page, with everything rounded into
pills and soft slabs that float on shadows tinted their own color. Heavy,
friendly geometric type and bouncy little reactions to every touch. Bold, fun,
energetic, and designed to delight — never childish clutter or washed-out
pastel.

-   **Mood**: playful, vibrant, upbeat, friendly.
-   **Inspired by**: die-cut sticker sheets, learning and habit apps, playful
    packaging, and toy-store signage.

## When to Use

-   **Best for**: learning and quiz tools for kids and families, habit and
    streak trackers, games and scoreboards, celebrations and invitations,
    consumer product explainers, lighthearted personal stats.
-   **Avoid for**: grief, health, legal, or financial-risk content, serious
    journalism and research, enterprise dashboards, anything that needs to feel
    sober or authoritative.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces */
  --background: #fef7ff;               /* pink-white page */
  --surface-container-low: #ffffff;    /* white: cards and floating panels */
  --surface-container: #f8eef8;        /* pale pink: input fills, inset wells */
  --surface-container-high: #f2e8f2;   /* deeper pink: tracks, hover fills */

  /* Ink */
  --on-surface: #2e1a28;               /* deep plum: headlines and body */
  --on-surface-variant: #604868;       /* dusty plum: captions, secondary text */

  /* Rules */
  --outline: #907898;                  /* mauve: input and control borders, never text */
  --outline-variant: #dcc8e0;          /* lilac: rare hairlines, gridlines, never text */

  /* Accents */
  --primary: #c2207f;                  /* hot pink: actions, links, the emphasis */
  --on-primary: #ffffff;
  --primary-container: #f080c0;        /* bubblegum: badges, selected chips */
  --on-primary-container: #2e1a28;
  --secondary: #7c52aa;                /* grape: secondary actions, tags, categories */
  --tertiary: #0096cc;                 /* sky blue: highlights and fills, never text */
  --error: #c53030;
  --on-error: #ffffff;

  /* Data series, in order of use */
  --data-1: #c2207f;                   /* hot pink */
  --data-2: #7c52aa;                   /* grape */
  --data-3: #0096cc;                   /* sky blue */
  --data-4: #d96a00;                   /* tangerine */
  --data-context: #c8b8d0;             /* context series */

  /* Fonts */
  --font-headline: 'DM Sans', sans-serif;
  --font-body: 'DM Sans', sans-serif;
  --font-label: 'DM Sans', sans-serif;

  /* Shape */
  --rounded: 1rem;
  --rounded-lg: 2rem;
  --rounded-full: 9999px;

  /* Style effects */
  --shadow-pink: 0 4px 16px rgb(224 64 160 / 0.2);
  --shadow-pink-deep: 0 10px 28px rgb(224 64 160 / 0.32);
  --shadow-grape: 0 4px 16px rgb(124 82 170 / 0.2);
  --shadow-sky: 0 4px 16px rgb(0 150 204 / 0.2);
  --pop-scale: scale(1.03);
  --lift: translateY(-4px);
  --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

## Color

-   **Proportions**: the pink-white page and white cards carry most of the
    surface; plum ink carries the words. The three accents are used freely but
    with purpose — together roughly 15–20% of what the reader sees, far more
    than a quiet style. Pink leads (the primary action, the emphasis word, the
    series that matters); grape is the second voice (secondary actions, tags,
    categories); sky blue is the bright highlight (fills, progress, a third
    category).
-   **Sky blue is never text.** At 3.2:1 it works for fills, bars, and chart
    marks only. Links and colored labels use hot pink or grape.
-   **Saturated, never washed out.** Pastels appear only as fills
    (`--primary-container`, `--surface-container`) under dark plum text; an
    accent is always full strength.
-   **Shadows carry color too.** Elevation is tinted with the hue of the
    element it lifts (see Defining Treatments); there are no grey shadows.
-   **Outlines are for controls.** Mauve borders mark inputs and outlined
    controls; content is separated by space and white cards, not lines.

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display | DM Sans | 900 | Tracking −0.03em; line height 1.05–1.1. Optical size at its maximum. |
| Headlines | DM Sans | 700–800 | Tracking −0.02em. Sentence case. |
| Body | DM Sans | 400 | At least 16px; generous line height 1.6–1.7. |
| Labels, kickers | DM Sans | 500–600, uppercase | Label size, tracking 0.06–0.08em. |
| Buttons | DM Sans | 700 | Body size, sentence case. |
| Key figures | DM Sans | 800–900 | Tabular figures (`font-variant-numeric: tabular-nums`), tight tracking. |

One family carries everything; hierarchy comes from the big jump between a 900
display and 400 body, never from a second face. Headlines are sentence case and
never all caps; uppercase belongs only to small labels.

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies; use
it wherever the artifact has that place. When there is room for only a few, keep
the higher-ranked ones.

### 1. Tinted colorful shadows

Cards, the primary container, and filled buttons float on a soft shadow in
their own accent color at 15–20% opacity. Sibling cards in a row may rotate
pink, sky, and grape shadows; a pink button always gets a pink shadow. Hover
deepens the shadow.

```css
.card {
  background: var(--surface-container-low);
  border-radius: var(--rounded);
  box-shadow: var(--shadow-pink);
  padding: var(--space-lg);
}
.card:nth-child(3n+2) { box-shadow: var(--shadow-sky); }
.card:nth-child(3n+3) { box-shadow: var(--shadow-grape); }
.btn-primary { box-shadow: var(--shadow-pink); }
.btn-primary:hover { box-shadow: var(--shadow-pink-deep); }
```

### 2. Pills everywhere

Every control is fully rounded: buttons, badges, tags, inputs, segmented
controls, toggles, progress tracks. Cards take `--rounded`; a large opening
panel or the primary container takes `--rounded-lg`. No sharp corner appears
anywhere.

```css
.btn, .badge, .tag, input, select, .segmented, .progress {
  border-radius: var(--rounded-full);
}
.btn { padding: var(--space-sm) var(--space-lg); }
.hero-panel { border-radius: var(--rounded-lg); padding: var(--space-2xl) var(--space-xl); }
```

### 3. Heavy headline with a pop word

The title and section headlines are set heavy in plum, with the one word that
carries the point — a word already in the headline — in hot pink. One pop word
per headline at most; most section headings have none.

```css
.display {
  font-family: var(--font-headline);
  font-weight: 900;
  font-size: var(--display-size);
  letter-spacing: -0.03em;
  line-height: 1.05;
  color: var(--on-surface);
}
.display em { font-style: normal; color: var(--primary); }
```

### 4. Bouncy pop on interaction

Buttons and chips grow slightly with a springy overshoot; clickable cards lift.
Applies to interactive elements only, never to static content.

```css
.btn, .chip {
  transition: transform var(--dur-short) var(--ease-bounce),
              box-shadow var(--dur-short) var(--ease-out);
}
.btn:hover, .chip:hover { transform: var(--pop-scale); }
a.card, .card[role="button"] {
  transition: transform var(--dur-short) var(--ease-bounce);
}
a.card:hover, .card[role="button"]:hover { transform: var(--lift); }
```

### 5. Lollipop data marks

Charts and progress bars share the pill shape: bars with fully rounded ends,
thick lines with round caps and joins, and fat round dots at data points.

```css
.bar { rx: 999; fill: var(--data-1); }
.series-line {
  stroke: var(--data-1);
  stroke-width: 3.5;
  stroke-linecap: round;
  stroke-linejoin: round;
  fill: none;
}
.progress-fill { background: var(--tertiary); border-radius: var(--rounded-full); }
```

## Composition

-   **Flush-left and lively.** Title blocks, headings, and grids align left;
    card grids mix sizes (a wide card beside two small ones) so the page has
    rhythm. This follows the skill's preference for asymmetry.
-   **Separation by floating objects.** Groups sit on white cards with tinted
    shadows over the pink-white page; space does the rest. Avoid hairline
    dividers and cards inside cards.
-   **Medium density, generous padding.** Cards get roomy padding and
    `--space-lg` gaps; sections breathe with `--space-2xl` between them.
-   **Narratives** run a single column of prose with cards and figures breaking
    out wider; **dashboards and tools** use the same cards in a tighter grid
    with `--space-md` gaps, keeping the shadows and pills.

## Components

-   **Buttons**: pills. Primary is a solid hot-pink fill with white text and a
    pink shadow; secondary is a solid grape fill with white text and a grape
    shadow; a quiet action is pink text with no fill. Hover pops and deepens
    the shadow; active presses to `scale(0.97)`.
-   **Cards**: white, `--rounded`, tinted shadow, no border.
-   **Key figures**: on a card — a small uppercase label in dusty plum, the
    value at 800–900 in plum or hot pink, a short caption below.
-   **Badges and tags**: pills. Badges are bubblegum (`--primary-container`)
    with bold plum text; category tags are a grape outline with grape text.
-   **Links**: hot pink, 600 weight, 2px underline offset 3px.
-   **Inputs**: pill-shaped, pale-pink fill (`--surface-container`), mauve
    border; focus turns the border hot pink and adds the focus ring.
-   **Tables**: on a white card; header row in the label voice on
    `--surface-container`; rows separated by an alternating pale fill rather
    than lines; tabular figures.
-   **Segmented controls and toggles**: a pill track in
    `--surface-container-high` with a white or hot-pink pill thumb that slides
    with the bounce easing.

## Data Visualization

-   **Series**: `--data-1` (hot pink) for the series that matters, then grape,
    sky blue, tangerine. Everything that is context is `--data-context`.
-   **Marks**: rounded-end bars, 3–4px round-capped lines, large round dots.
    Flat color; area fills at 15–20% of the series color. No 3D, no gradients
    on marks.
-   **Axes and gridlines**: axis labels in `--font-label`, 500, dusty plum;
    gridlines dashed in `--outline-variant`; no axis lines or chart border.
-   **Labels**: label series directly at their ends in bold — in the series
    color for pink and grape, in plum for sky and tangerine (which are not text
    colors). Tooltips are white pills with a tinted shadow.
-   **Charts sit on cards**, with the chart title as a 700-weight headline on
    the same card.

## Motion

Bouncy and quick. Interactions use `--ease-bounce` over `--dur-short`; entries
fade in and rise with a small overshoot over `--dur-long`, staggered across
sibling cards. Key figures may count up to their value once. Keep every motion
under half a second, and never loop.

## Don'ts

-   No sharp corners, square buttons, or hairline-boxed cards.
-   No grey or black drop shadows; a shadow is always tinted, and never
    stronger than about 35% opacity.
-   No washed-out pastels as text or as accents; no sky-blue text.
-   Don't stack all three accents on one element or rainbow a headline; one
    pop word per headline.
-   No second typeface, no thin display weights, no all-caps headlines.
-   No neon glows, gradient text, or glossy bevels; Sticker is flat color on soft
    shadow.

## If the User Asks for Dark

Keep the same roles on a midnight-plum ground: `--background: #1e1420`,
`--surface-container-low: #2a1e2c` (cards), `--on-surface: #f6e9f4`,
`--on-surface-variant: #cdb6d0`, `--primary: #ff7ac4` with `--on-primary:
#2e1a28`, `--secondary: #c8a8e8`, `--tertiary: #40c0ee` (which now passes as
text). Raise shadow opacity to 30–40% so the tint still reads; keep the pills
and the bounce.
