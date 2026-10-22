---
name: Briefing
slug: briefing
register: classic
mode: light
---

# Briefing

## Identity

**North Star: "The Global Dossier."** A worldly international affairs and design
digest: warm stone-white paper, crisp ink rules, a signature signal-gold
dossier badge (`#f2b705`), and deep petrol-slate subheads (`#1f4e5f`). Combines
an authoritative editorial serif for headlines and key figures with a clean
modern sans for body copy and crisp monospace for reading times, section
indices, and metadata. Respectable, serious, and contemporary — never stuffy,
never antique.

-   **Mood**: worldly, composed, informed, modern-editorial.
-   **Inspired by**: international affairs and urbanism magazines, executive
    briefing books, global city indices, and annual survey digests.

## When to Use

-   **Best for**: policy, economics, and global affairs explainers; history and
    historical explainers; urbanism, transit, and infrastructure stories;
    comparative rankings and city/product indices; executive briefings and
    strategy summaries; modern journalism and research digests.
-   **Avoid for**: playful children's games, gothic or romantic poetry, neon
    nightlife, anything meant to feel raw, distressed, or unedited.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces: warm stone-white paper */
  --background: #faf9f5;               /* warm magazine stone-white */
  --surface-container-low: #ffffff;    /* crisp white for bordered figure cards and panels */
  --surface-container: #f1efe8;        /* warm sand-stone for sidebars and callout bands */
  --surface-container-high: #e6e2d6;   /* deeper stone: hover fills, table headers */

  /* Ink */
  --on-surface: #17181a;               /* rich editorial black: headlines and body */
  --on-surface-variant: #56585c;       /* warm slate: captions, secondary text */

  /* Rules */
  --outline: #17181a;                  /* crisp black section rules */
  --outline-variant: #dedad0;          /* stone border for cards and dividers, never text */

  /* Accents */
  --primary: #17181a;                  /* ink is the primary action fill */
  --on-primary: #faf9f5;
  --primary-container: #f2b705;        /* signal gold: dossier badge, highlight marker */
  --on-primary-container: #17181a;
  --secondary: #1f4e5f;                /* deep petrol slate: decks, subheads, links */
  --tertiary: #785008;                 /* dark amber-ochre: text-safe gold voice on light grounds */
  --error: #b42318;
  --on-error: #ffffff;

  /* Data series, in order of use */
  --data-1: #1f4e5f;                   /* petrol slate */
  --data-2: #d99000;                   /* dossier gold */
  --data-3: #2b6e52;                   /* civic pine */
  --data-4: #b84a39;                   /* brick red */
  --data-context: #c4bfb2;             /* context series and gridlines */

  /* Fonts */
  --font-headline: 'Source Serif 4', serif;
  --font-body: 'Plus Jakarta Sans', sans-serif;
  --font-label: 'Geist Mono', monospace;

  /* Shape */
  --rounded: 0.25rem;                  /* 4px buttons and inputs */
  --rounded-lg: 0.375rem;              /* 6px cards and panels */
  --rounded-full: 0.25rem;             /* squared dossier badges */

  /* Style effects */
  --section-rule: 1.5px solid var(--outline);
  --card-border: 1px solid var(--outline-variant);
  --badge-radius: 2px;
  --heading-tracking: -0.02em;
  --label-tracking: 0.08em;
}
```

## Color

-   **Proportions**: warm stone-white (`#faf9f5`), crisp white cards
    (`#ffffff`), and rich black ink (`#17181a`) carry roughly 88% of the page.
    Signal gold (`--primary-container: #f2b705`) is the unmistakable magazine
    signature (under 4%): the small dossier pill in the section bar, a key callout
    tag, or a highlight bar. Deep petrol slate (`--secondary: #1f4e5f`, 8.5:1)
    carries the deck/standfirst, links, and the primary chart series.
-   **Signal gold is a fill, never text on light.** Put `#17181a` ink text on top
    of `#f2b705` (10.8:1). When a small label needs a warm gold text color on
    white or stone, use `--tertiary` (`#785008`, 6.4:1).

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display, headlines | Source Serif 4 | 600 | Tracking `--heading-tracking`, line height 1.08–1.15. |
| Deck / standfirst | Plus Jakarta Sans | 600 | 1.05–1.15× body, in `--secondary` (`#1f4e5f`). |
| Body | Plus Jakarta Sans | 400; 600 for inline emphasis | 16–17px for narrative, 15px in dashboards/tools. Line height 1.6. |
| Dossier pill | Plus Jakarta Sans | 700, uppercase | `0.6875rem`, tracking `0.08em`, `#17181a` on `#f2b705`. |
| Metadata, indices, axes | Geist Mono | 500, uppercase | `0.72rem`, tracking `0.06em`, in `--on-surface-variant`. |
| Key figures | Source Serif 4 | 600 | Large, lining tabular figures (`font-variant-numeric: lining-nums tabular-nums`). |

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies;
use it wherever the artifact has that place.

### 1. Dossier section bar with signal-gold pill

The opening header and major section dividers start with a horizontal dossier
bar underlined by a `1.5px` black rule (`--section-rule`), pairing a small
signal-gold pill (`DOSSIER 01`, `BRIEFING`, `INDEX`) with `Geist Mono` topic
and reading-time metadata.

```css
.dossier-bar {
  display: flex;
  align-items: center;
  gap: var(--space-sm);
  border-bottom: var(--section-rule);
  padding-bottom: var(--space-sm);
  margin-bottom: var(--space-md);
}
.dossier-pill {
  background: var(--primary-container);
  color: var(--on-primary-container);
  font-family: var(--font-body);
  font-weight: 700;
  font-size: 0.6875rem;
  letter-spacing: var(--label-tracking);
  text-transform: uppercase;
  padding: 0.1875rem 0.5rem;
  border-radius: var(--badge-radius);
}
.dossier-meta {
  font-family: var(--font-label);
  font-size: var(--label-size);
  color: var(--on-surface-variant);
  text-transform: uppercase;
}
```

### 2. Editorial serif headline with petrol-slate standfirst

Below the dossier bar, set the headline in `Source Serif 4` 600 and the
analytical deck/standfirst immediately beneath it in `Plus Jakarta Sans` 600 in
deep petrol slate (`--secondary`).

```css
.title {
  font-family: var(--font-headline);
  font-weight: 600;
  letter-spacing: var(--heading-tracking);
  line-height: 1.08;
  color: var(--on-surface);
}
.standfirst {
  font-family: var(--font-body);
  font-weight: 600;
  color: var(--secondary);
  margin-top: var(--space-xs);
}
```

### 3. Crisp white bordered figure cards on warm stone

Key figures, rankings, and interactive modules sit on crisp `#ffffff`
(`--surface-container-low`) with a `1px` `--outline-variant` border (`#dedad0`)
and `6px` radius against the `#faf9f5` stone-white page.

```css
.figure-card {
  background: var(--surface-container-low);
  border: var(--card-border);
  border-radius: var(--rounded-lg);
  padding: var(--space-md) var(--space-lg);
}
.figure-card .value {
  font-family: var(--font-headline);
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}
```

### 4. Numbered index badges (`01`, `02`, `03`)

Lists, rankings, and multi-part takeaways use `Geist Mono` two-digit index
numbers (`01`, `02`, `03`) in `--secondary` or on a subtle `--surface-container`
square so the page reads like a structured intelligence digest.

```css
.index-num {
  font-family: var(--font-label);
  font-weight: 600;
  font-size: var(--label-size);
  color: var(--secondary);
}
```

### 5. Warm stone sidebar / methodology callouts

 methodology notes, definitions, and secondary filters sit in
`--surface-container` (`#f1efe8`) with a `1.5px` black top rule.

```css
.aside-box {
  background: var(--surface-container);
  border-top: var(--section-rule);
  padding: var(--space-md);
}
```

## Composition

-   **Clean, magazine-grid discipline.** Flush-left headers, clear column
    guides, and a natural balance between narrative prose (`Plus Jakarta Sans`),
    serif headlines (`Source Serif 4`), and structured white data cards.
-   **Versatile across forms.** Equally at home in a long-form policy explainer,
    a city comparison dashboard, or an interactive ranking/calculator tool.

## Components

-   **Buttons**: `4px` radius (`--rounded`), `Plus Jakarta Sans` 600. Primary is
    an ink fill (`#17181a`) with stone-white text; secondary is white with a
    `1px` `#c8c4b8` border and ink text.
-   **Tags and chips**: squared `4px` tags in `#f5e6c4` with `--tertiary`
    (`#785008`) text, or `-- primary-container` (`#f2b705`) for the single lead
    dossier pill.
-   **Tables**: crisp white background, `1.5px` black rule under the header,
    `1px` `--outline-variant` between rows, `Geist Mono` uppercase headers, and
    tabular numbers.

## Data Visualization

-   **Series**: `--data-1` (petrol slate `#1f4e5f`) for the primary series,
    `--data-2` (dossier gold `#d99000`) for the focal comparison, `--data-3`
    (civic pine `#2b6e52`), and `--data-4` (brick red `#b84a39`). Context series
    in `--data-context`.
-   **Furniture**: chart sits inside a crisp white `.figure-card`; title in
    `Source Serif 4` 600, subtitle and axes in `Geist Mono`.

## Motion

Crisp and editorial: quick fades over `--dur-short` with `--ease-out`.

## Don'ts

-   Never use `#f2b705` signal gold as text on light backgrounds — always pair
    it with `#17181a` ink text inside a pill or bar.
-   No heavy drop shadows, gradients, or antique ornaments.

## If the User Asks for Dark

Keep the dossier architecture on warm charcoal-slate: `--background: #121417`,
`--surface-container-low: #181b1f`, `--surface-container: #20242a`,
`--on-surface: #f2f0ea`, `--on-surface-variant: #9ea4ad`,
`--outline: #f2f0ea`, `--outline-variant: #2c313a`, `--primary: #f2f0ea`,
`--on-primary: #121417`, `--primary-container: #f2b705`,
`--on-primary-container: #121417`, `--secondary: #7cc4e8`,
`--tertiary: #f2b705`.
