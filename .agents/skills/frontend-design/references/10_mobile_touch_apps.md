# Mobile & Touch-First Applications Design Reference

This guide covers design aesthetics, thumb-zone ergonomics, touch target
dimensions, card hierarchies, and mobile navigation patterns for smartphone
viewports (375px–430px) and responsive touch-first web applications.

--------------------------------------------------------------------------------

## 1. Aesthetic DNA & Ergonomic Principles

Mobile interfaces must optimize for **one-handed thumb navigation, rapid visual
scanning, and tactile feedback**.

-   **Mobile-First Responsive Viewport Canvas**: Support mobile touch ergonomics
    ($375\text{px}$ to $430\text{px}$) while expanding cleanly to a full
    multi-column desktop layout (`max-w-6xl` or `max-w-7xl` with 2–3 columns on
    `lg:`) on desktop viewports — never trap a "mobile-first web app" inside a
    narrow `max-w-md` strip floating in an empty 1440px desktop canvas.
-   **Surface Elevation & Radius**:
    -   Soft, friendly surface geometry: `rounded-2xl` ($16\text{px}$) to
        `rounded-3xl` ($24\text{px}$) for cards and modals.
    -   Layered elevation: Subtle backdrop blurs (`backdrop-blur-md bg-white/80
        dark:bg-slate-900/80`) for floating top bars and bottom sheets.
-   **Color & Contrast**: High-contrast foreground elements for outdoor daylight
    legibility, distinct semantic tint colors for categories and states.

--------------------------------------------------------------------------------

## 2. Touch Target & Thumb-Zone Specifications

Touch interfaces must prevent accidental mis-taps and reach fatigue.

-   **Minimum Touch Hitbox**:
    -   Every interactive element (buttons, icon triggers, list rows, tabs,
        checkboxes) MUST have an interactive hitbox of at least **$44 \times
        44\text{px}$** (or $48 \times 48\text{px}$ for primary CTAs).
    -   Even if the visual icon is $20\text{px}$, wrap it in a container with
        `min-h-[44px] min-w-[44px] flex items-center justify-center` or use
        negative margin tap expansions.
-   **Ergonomic Thumb Zones**:
    -   **Natural Reach Zone (Bottom 40% of screen)**: Place primary navigation
        tabs, key action buttons, and sheet triggers here.
    -   **Stretch Zone (Middle 30% of screen)**: Content feed, scrollable cards,
        and interactive lists.
    -   **Hard Reach Zone (Top 30% of screen)**: Page titles, search bar
        triggers, secondary info, and non-destructive filters.
-   **15% Aggregate Sticky Surface Cap**: The combined height of all fixed
    elements (top header + banner + bottom nav bar) must NEVER exceed **15% of
    the mobile viewport height**, leaving at least 85% of vertical space open
    for scrollable content.

```
[ MOBILE THUMB ZONE DISTRIBUTION ]

+-------------------------------------+  ^
| [Back]        Page Title      [···] |  | Hard Reach (Static Info & Top Bar)
|                                     |  v
+-------------------------------------+  ---
|  [ STAT RING ]     [ METRIC CARD ]  |  ^
|                                     |  |
|  • Active List Item 1               |  | Stretch Zone (Content & Data)
|  • Active List Item 2               |  |
|                                     |  v
+-------------------------------------+  ---
|  [       PRIMARY ACTION CTA       ] |  ^
|  ---------------------------------  |  | Natural Thumb Zone (Key Actions & Nav)
|  [Tab 1]   [Tab 2]   [Tab 3] [Tab 4]|  v
+-------------------------------------+
```

--------------------------------------------------------------------------------

## 3. Core Mobile Navigation Patterns

### Pattern 1: Fixed Bottom Tab Bar (Navigation Anchor)

-   **Structure**: Fixed bottom container (`fixed bottom-0 left-0 right-0 z-40
    bg-white/90 dark:bg-slate-900/90 backdrop-blur-md border-t border-slate-200
    dark:border-slate-800`).
-   **Tab Layout**: 3 to 5 evenly distributed tab destinations (`grid
    grid-cols-4 items-center h-16 pb-safe`).
-   **Tab Item Anatomy**: $22\text{px}$ icon stacked vertically above an
    $10\text{px}$–$11\text{px}$ caption (`text-[10px] font-medium tracking-tight
    mt-1`).
-   **Active State Indicator**: Solid filled icon with brand accent color,
    accompanied by a small active dot or accent label color.

### Pattern 2: Mobile Top App Bar

-   **Height**: Compact $52\text{px}$ to $56\text{px}$ sticky header (`sticky
    top-0 z-30`).
-   **Left Slot**: Back arrow button or brand avatar.
-   **Center Slot**: Truncated page title (`text-base font-semibold truncate`).
-   **Right Slot**: Single primary contextual action (e.g. filter icon, share
    button, or profile avatar).

### Pattern 3: Bottom Sheet / Action Drawer

-   **Sheet Container**: Rounded top corners (`rounded-t-3xl`), slide-up
    animation, full backdrop overlay (`bg-black/50 backdrop-blur-sm`).
-   **Drag Handle Affordance**: Centered grab handle bar at the top of the sheet
    (`w-10 h-1.5 bg-slate-300 dark:bg-slate-700 rounded-full mx-auto my-3`).
-   **Scrolling Behavior**: Scrollable body content with fixed action buttons
    pinned to the sheet bottom.

--------------------------------------------------------------------------------

## 4. Mobile Cards & Tracker Layouts

### Layout A: Daily Tracker & Stat Summary (e.g., Fitness, Habits, Sports)

-   **Top Metric Cards**: 2-column grid of compact summary cards with big
    numbers (`text-2xl font-bold`) and micro progress rings (SVG circle stroke).
-   **Horizontal Date Scroller**: Single-line horizontal carousel showing
    day-of-week abbreviations and day numbers (`M 14`, `T 15`, `W 16`) using
    interactive date selection buttons (`<button>` elements with active state
    `bg-slate-900 text-white rounded-full py-2 px-3`).

### Layout B: Interactive Tap List Rows

-   **Height**: Generous row height ($56\text{px}$–$68\text{px}$) with
    full-width row clickability.
-   **Anatomy**: Left category/status icon ($36\text{px}$ circular container) +
    Middle stacked title and subtitle + Right chevron disclosure icon or clean
    unboxed metric text.
-   **Hairline Dividers**: Subtle `border-b border-slate-100
    dark:border-slate-800` inset from the left icon margin.

### Layout C: Sticky Bottom CTA Bar

-   When a page requires a critical confirmation (e.g., checkout, save workout,
    submit review), anchor the button to the bottom viewport:
    -   Container: `fixed bottom-0 left-0 right-0 p-4 bg-gradient-to-t
        from-white via-white to-transparent dark:from-slate-950`.
    -   Full-width button: `w-full h-12 rounded-xl bg-slate-900 text-white
        font-medium text-sm flex items-center justify-center shadow-lg
        shadow-slate-900/10 active:scale-[0.98] transition-transform`.
