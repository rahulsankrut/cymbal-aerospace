# Landing Pages & Marketing Design Guidelines

This reference covers corporate landing pages, creative agency showcases, lead
generation funnels, product drops, and B2B service websites.

--------------------------------------------------------------------------------

## 1. Scope & Taxonomy Coverage

-   **Creative & Digital Marketing Agencies**: Growth agencies, video production
    studios, performance marketing, automation consultancies.
-   **Automotive & Mobility Marketing**: Electric vehicles, luxury fleet
    leasing, custom performance engineering.
-   **Hardware & Manufacturing OEM/ODM**: Precision fabrication, industrial
    component suppliers, supply chain solutions.
-   **Product Drops & SaaS Pre-launches**: Conversion-focused single pages,
    waitlists, interactive feature demos.
-   **Lead Generation & Service Portfolios**: Specialized development
    consultants, technical service providers, professional practices.

--------------------------------------------------------------------------------

## 2. Architectural & Visual Rules

### A. Section Flow & Visual Storytelling

Sequence sections as a cohesive argument rather than an inventory of widgets:
$$\text{Proposition} \quad\longrightarrow\quad \text{Mechanism / Capabilities}
\quad\longrightarrow\quad \text{Proof / Evidence} \quad\longrightarrow\quad
\text{Conversion / Action}$$

1.  **Hero Section**: Single dominant focal carrier (high-impact $16:9$ visual
    asset or typographic statement) with an unmistakable headline sized
    `clamp(2.25rem, 4vw, 3.75rem)` ($36\text{–}60\text{px}$), concrete value
    proposition, and a uniquely primary CTA.
2.  **Core Capabilities / Services**: Asymmetric bento-grid or numbered service
    list (e.g. `01. Search Strategy & Analytics`, `02. Workflow Automation`)
    detailing real business outcomes using clean human editorial numbering (no
    mechanical comment slashes `//`).
3.  **Proof of Impact / Case Studies**: 2–3 in-depth project cards with
    concrete, quantified metrics (e.g., `+140% Qualified Inbound Leads in 6
    Months`, `\$2.4M Pipeline Generated`), placed immediately adjacent to the
    capability claims they substantiate.
4.  **Interactive Lead Capture / Contact**: Minimalist form with clean input
    borders, validated fields, and immediate submission feedback.
5.  **Quiet Footer**: Wordmark, navigation mirror, legal notices, and contact
    info.

### B. Copywriting & CTA System

-   **Ban Generic SaaS Buzzwords**: Replace words like *"supercharge"*,
    *"empower"*, *"unlock"*, and *"elevate"* with plain, concrete descriptions
    of what the service delivers (e.g., *"We build lead generation engines and
    automated sales pipelines for local businesses"*).
-   **Single-Line Action Labels**: CTA buttons must state the exact outcome:
    `"Schedule Discovery Call"`, `"Download Rate Card"`, `"Request Manufacturing
    Quote"`.
-   **CTA Restraint**: At most one primary CTA per decision block; repeat the
    primary action only after major proof or objection-handling sections.

### C. Bento-Grid & Asymmetric Hierarchy

-   Use dynamic column spans (`col-span-2` alongside `col-span-1`) to give
    prominence to marquee capabilities.
-   Inner surfaces should use subtle hairline borders (`border
    border-neutral-200 dark:border-neutral-800`) rather than heavy drop shadows.
-   Avoid the cliché symmetrical 3-column feature triad (icon-on-top + title +
    generic 2-line paragraph).

--------------------------------------------------------------------------------

## 3. Typography & Color Strategies

-   **Agencies, AI Studios & Modern Tech Marketing**: Crisp geometric display
    (`Plus Jakarta Sans`, `Outfit`, `Bricolage Grotesque`, `Urbanist`, or
    `Manrope`) in tight tracking (`tracking-tight`), paired with refined body
    text (`Plus Jakarta Sans`, `DM Sans`, `Manrope`, `Public Sans`). Clean
    neutral canvas (crisp off-white or deep obsidian `#0A0A0A`) with one focused
    accent (e.g., electric cobalt `#1E40AF` or warm marigold `#F59E0B`).
-   **Fitness, Performance & High-Energy Brands**: Tall, disciplined athletic
    condensed display (`Oswald`, `Barlow Condensed`, `Antonio`, or `Archivo`)
    paired with `DM Sans`, `Public Sans`, or `Plus Jakarta Sans` body copy.
-   **Manufacturing & Industrial**: Trustworthy corporate palette (deep navy
    `#0F172A`, cool slate `#334155`, steel blue `#0284C7`). Clean structured
    headings (`Plus Jakarta Sans`, `Outfit`, `Archivo`, `Manrope`) paired with
    high-legibility body text (`Public Sans`, `DM Sans`, `Plus Jakarta Sans`).
-   **Regional & B2B Trust Signals**: Regional division subtitles and facility
    markers (e.g., *Regional Facility*, *ISO 9001 Certified*, *Made in Germany*)
    belong in the **Hero Section**, **About Section**, or **Footer**. Never
    append them to the Top Bar brand lockup.

--------------------------------------------------------------------------------

## 4. `generate_image` Recipes for Marketing

```typescript
// 1. Digital Marketing Agency Hero
generate_image({
  Prompt: "Cinematic wide-angle view of a modern creative marketing studio with large glass architectural windows, minimalist oak conference table, designer ambient lighting, sleek and professional atmosphere, 8k resolution.",
  ImageName: "hero_marketing_studio",
  AspectRatio: "16:9"
});

// 2. High-Tech Manufacturing / OEM Facility
generate_image({
  Prompt: "Clean industrial precision manufacturing facility with automated robotic assembly arms, pristine epoxy floor, high-tech cleanroom lighting, high-end OEM production environment.",
  ImageName: "hero_oem_manufacturing",
  AspectRatio: "16:9"
});

// 3. Automotive / Mobility Showcase
generate_image({
  Prompt: "Futuristic sleek electric vehicle concept parked inside an ultra-modern concrete minimalist architectural pavilion at twilight, subtle glowing taillights, photorealistic automotive design render.",
  ImageName: "hero_automotive_mobility",
  AspectRatio: "16:9"
});
```

--------------------------------------------------------------------------------

## 5. Anti-Patterns to Avoid

-   ❌ **No Floating Stat Pills in Headers**: Do not stick arbitrary percentage
    chips (e.g. `"99.9% UPTIME"`, `"5.0 RATED"`) directly next to the brand
    logo.
-   ❌ **No Brand Subtitle Clutter**: Keep the top navigation brand wordmark as a
    single clean text element; do not append location chips or division subtext
    to the logo in the top bar.
-   ❌ **No Decorative Feature Sprawl**: Avoid stuffing pages with fake roadmap
    accordions, mock star reviews from "John Doe", or generic spinning logo
    carousels.
-   ❌ **No Missing Form Validation**: Every lead capture form must validate
    email/phone format and provide a clear confirmation state upon submission.
