# SaaS & Dashboard Design Guidelines

This reference covers enterprise SaaS products, business analytics platforms,
data spreadsheets, workflow & task managers, and admin consoles.

--------------------------------------------------------------------------------

## 1. Scope & Taxonomy Coverage

-   **Enterprise SaaS & Systems**: B2B platforms, user management, billing
    panels, team permissions.
-   **Data Spreadsheets & Normalization Tools**: Daily health/fitness habit
    logs, financial ledger sheets, multi-batch test analyzers.
-   **Task, Calendar & Mailbox Assistants**: Executive scheduling agents,
    morning/evening priority planners, queue management.
-   **Developer & Monitoring Consoles**: API usage monitors, log viewers,
    telemetry dashboards (e.g. environmental chamber runtime monitors, server
    metrics).

--------------------------------------------------------------------------------

## 2. Architectural & Visual Rules

### A. Layout Structure & Navigation

-   **Workspace Canvas**: Sidebar navigation ($240\text{px}$–$280\text{px}$
    width) + Top header with contextual breadcrumbs and account profile + Main
    content viewport.
-   **Top Bar Contract**: Breadcrumb trail (e.g. `Projects / Quality Lab /
    Chamber Beta`) on the left, at most 1–2 primary action buttons on the right
    (`whitespace-nowrap shrink-0`).
-   **Single-Elevation Depth**: Flat surfaces with subtle 1px border lines
    (`border border-neutral-200 dark:border-neutral-800`). Never nest cards
    within cards.
-   **High-Density Data Grids**: Compact row heights
    ($36\text{px}$–$44\text{px}$), clean column alignments (left for text, right
    for numeric data), subtle row hover highlights.

### B. Tabular Numerals & Metric Display

-   **Tabular Figures**: Every numeric value, timestamp, counter, and financial
    figure must use `font-variant-numeric: tabular-nums` or monospace font
    (`font-mono`) to prevent layout jitter and align decimal points vertically.
-   **Hardware & Segmented Displays**: When simulating physical instruments or
    testing hardware, use dedicated segmented font styles, high-contrast dark
    metallic casings, and realistic reset/timing controls.

### C. Feature Storytelling & Pricing Architecture

-   **Mechanism-to-Outcome Chain**: Every feature demonstration must link:
    $$\text{User Goal} \quad\longrightarrow\quad \text{Visible Interface
    Mechanism (real UI state)} \quad\longrightarrow\quad \text{Measurable
    Benefit}$$
-   **Pricing & Tier Cards**: Name each plan by target audience (`For
    early-stage teams`, `For scaling operations`), summarize price/billing
    cadence clearly, and use comparison matrices stating concrete limits and
    values rather than vague checkmark rows.

### D. State Completeness

Every data view must handle:

1.  **Populated State**: Rich, domain-grounded table rows or charts.
2.  **Empty State**: Clear explanation of what will appear once data is added,
    plus a primary action button (e.g., `"Log First Entry"`).
3.  **Loading / Pending State**: Clean skeleton placeholders matching table rows
    (geometry delta $\le 2\text{px}$).
4.  **Filtering / Search**: Live client-side search input, date range picker, or
    segmented status filter.

--------------------------------------------------------------------------------

## 3. Typography & Color Strategies

-   **Typography**: Clean, contemporary sans pairings — use `Plus Jakarta Sans`,
    `Outfit`, `Manrope`, or `Bricolage Grotesque` for crisp display structure
    and navigation, paired with `Public Sans`, `DM Sans`, or `Plus Jakarta Sans`
    for dense scannability at 12px–14px sizes. Never default to generic
    `Inter`/`Geist`. For data telemetry, timestamps, and financial metrics,
    strictly enforce monospace tabular figures (`JetBrains Mono`, `IBM Plex
    Mono`, `tabular-nums`).
-   **Color Palette**: Neutral dark slate (`#0F172A`), cool gray (`#1E293B`), or
    clean white (`#FFFFFF`) background. Semantic status colors used strictly for
    data state:
    -   Green (`#16A34A`): Active / Nominal / Normal operation
    -   Amber (`#D97706`): Approaching deadline / Warning
    -   Crimson (`#DC2626`): Alert / Error / Overdue

--------------------------------------------------------------------------------

## 4. `generate_image` Recipes for SaaS & Dashboards

```typescript
// 1. Dashboard User Avatars / Team Profiles
generate_image({
  Prompt: "Professional studio headshot portrait of a software engineer, neutral soft gray background, natural soft lighting, warm friendly expression, high resolution 1:1 avatar.",
  ImageName: "avatar_executive_user",
  AspectRatio: "1:1"
});

// 2. Hardware Dashboard Skeuomorphic Element (if requested)
generate_image({
  Prompt: "Brushed aluminum metallic texture with vintage dark bezel frame, industrial instrument panel texture, clean minimalist studio lighting.",
  ImageName: "texture_aluminum_panel",
  AspectRatio: "16:9"
});
```

--------------------------------------------------------------------------------

## 5. Anti-Patterns to Avoid

-   ❌ **No Hallucinated Scoreboards**: Never invent fake metrics like `"92/100
    INNOVATION SCORE"` or `"SYSTEM NOVELTY: 94%"` unless explicitly instructed
    by the prompt.
-   ❌ **No Bottom Telemetry Tickers**: Do not pin a bottom bar showing fake
    background worker IDs, fake latency logs (`"PING: 24ms"`), or simulated
    compiler output.
-   ❌ **No Cluttered Card Sandwiches**: Avoid wrapping every statistic in nested
    cards with drop shadows. Use simple clean tables and structured stat grids
    with subtle dividers.
