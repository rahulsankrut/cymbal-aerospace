# E-Commerce & Retail Design Guidelines

This reference covers digital storefronts, product catalogs, marketplaces, and
luxury direct-to-consumer experiences.

--------------------------------------------------------------------------------

## 1. Scope & Taxonomy Coverage

-   **Furniture, Lighting & Interiors**: Architectural forms, tactile materials,
    spatial context, dimension callouts.
-   **Food & Drink Producers**: Artisanal producers, farm-to-table, bakeries,
    craft breweries, vineyards.
-   **Audio, Instruments & Hardware**: Studio equipment, marine propellers,
    precision parts, mechanical specifications.
-   **Beauty & Fragrance**: Minimalist skincare, organic cosmetics, luxury
    perfume notes, ingredient transparency.
-   **Watches & Jewellery**: High-contrast macro shots, precious metals,
    movement specifications, craftsmanship stories.
-   **Publishing & Books**: Editorial typography, cover art displays, table of
    contents previews, binding details.
-   **Sport, Clubs & Athletes**: Streetwear & athletic technical apparel,
    athletic footwear, sizing guides.
-   **Automotive & Mobility Retail**: Vehicle configurators, spare parts
    catalogs, technical breakdown sheets.

--------------------------------------------------------------------------------

## 2. Architectural & Visual Rules

### A. Layout Structure & Section Discipline

-   **Storefront Hero**: 1 bold campaign focal point with a direct route into
    the featured collection (split-screen or centered showcase with $16:9$ or
    $4:3$ imagery). Always keep search, categories, and shopping bag reachable
    in the first navigation layer.
-   **Featured Collection Grid**: 3-column (desktop) or 2-column (tablet)
    product grid with generous whitespace (`gap-6` to `gap-8`). Cards must
    maintain identical field order, uniform background tone, and $\le 1\%$
    aspect ratio variance across adjacent items.
-   **Contiguous Purchase Module (PDP)**: On product detail views, keep product
    title, price, selected variant, availability, and primary buy CTA in one
    stable contiguous purchase module (sticky gallery left, sticky purchase
    module right; sticky bottom buy bar on mobile).
-   **Cart & Checkout Drawer**: Slide-over drawer or dedicated view showing
    subtotal, itemized list, quantity steppers, and clear action button.
-   **Section Ceiling**: Max 3–4 sections on the homepage (Hero $\to$ Featured
    Products $\to$ Story / Craftsmanship $\to$ Footer). *Do not stack flash
    sales + lightning deals + top categories + recommended + just-for-you +
    recently viewed.*

### B. Product Cards & Visual Hierarchy

-   **Lead with Imagery**: Product image takes $65\%\text{--}75\%$ of card
    height on a neutral, solid backdrop (clean off-white, warm paper for
    luxury/artisanal goods, or charcoal `#18181B`).
-   **Clean Metadata**: Brand / Category in muted 12px uppercase, Product Name
    in 16px SemiBold, Price in 15px tabular numbers.
-   **Hover Micro-Interactions**: Subtle lift ($2\text{px}$ `translateY`) and
    soft shadow expansion on hover; optional secondary image reveal or subtle
    quick-add button.
-   **No Badge Spam**: Maximum 1 subtle text tag (e.g. `Limited Run` or `In
    Stock`), never colored pill badge clusters.

### C. Promotional Restraint & Checkout Trust

-   **Promotional Surface Governance**: At most one slim, dismissible top banner
    ($\le 40\text{px}$). Never fire email capture or discount popups on entry
    (require $\ge 10\text{s}$ dwell and active user scroll/intent; max 1 modal
    per session).
-   **Clear Payment Terms**: If Cash on Delivery (COD) is supported, prominently
    display total amount, free delivery threshold, and simple customer
    verification form (Name, Phone, Address, Postal Code).
-   **Order Tracking / Verification**: Include clear post-order state (e.g.,
    "Order #1042 Confirmed — Preparing Shipment") with receipt summary.

--------------------------------------------------------------------------------

## 3. Typography & Color Strategies

-   **Luxury / Boutique / Fragrance**: High-contrast serif display (`Playfair
    Display`, `Cormorant Garamond`, `Fraunces`, or `Bodoni Moda`) paired with
    clean refined body text (`Plus Jakarta Sans`, `DM Sans`, `Public Sans`,
    `Source Serif 4`). Warm paper or deep charcoal surfaces, chosen to fit the
    brand.
-   **Streetwear, Athletic & Urban Apparel**: Structured architectural or
    condensed grotesque display (`Outfit`, `Plus Jakarta Sans`, `Oswald`,
    `Barlow Condensed`, `Antonio`, `Archivo`, or `Bricolage Grotesque`) paired
    with clean geometric body text (`Plus Jakarta Sans`, `DM Sans`, `Manrope`,
    `Public Sans`). Keep display headlines in balanced proportions
    (`clamp(2.25rem, 4vw, 3.75rem)`) so they never clip or overflow split hero
    columns. Neutral dark slate or chalk backdrops with 1 disciplined accent
    (mustard yellow, cobalt blue, or crimson).
-   **Industrial / Hardware**: Technical mono numbers and structured sans (`Plus
    Jakarta Sans`, `Archivo`, `Outfit`, `IBM Plex Sans`, `Space Mono`). Steel
    grays and high-visibility status indicators.

--------------------------------------------------------------------------------

## 4. `generate_image` Recipes for Retail

```typescript
// 1. Luxury Skincare / Beauty
generate_image({
  Prompt: "Minimalist amber glass serum dropper bottle on a raw light travertine stone pedestal, soft morning sunlight, clean neutral stone background, luxury cosmetic product photography, 8k resolution.",
  ImageName: "product_serum_amber_bottle",
  AspectRatio: "4:3"
});

// 2. Streetwear / Fashion Collection
generate_image({
  Prompt: "Streetwear fashion editorial shot of high-end raw denim cargo pants and oversized heavy cotton hoodie, urban concrete backdrop, directional studio strobe lighting, high-contrast, commercial fashion photography.",
  ImageName: "product_streetwear_collection",
  AspectRatio: "4:3"
});

// 3. Furniture & Interior Lighting
generate_image({
  Prompt: "Modern sculptural oak lounge chair and brushed brass floor lamp in a sunlit architectural living room with polished concrete floors, minimalist Scandinavian aesthetic, architectural digest style.",
  ImageName: "hero_scandinavian_lounge",
  AspectRatio: "16:9"
});
```

--------------------------------------------------------------------------------

## 5. Anti-Patterns to Avoid

-   ❌ **No Cluttered Flash Sale Clones**: Avoid mimicking crowded discount
    marketplaces with countdown timers, spinning prize wheels, and neon discount
    badges.
-   ❌ **No Missing Pricing or Cart Feedback**: Every "Add to Cart" button must
    trigger visible cart feedback (numeric cart count increment or slide-out
    drawer).
-   ❌ **No Unresponsive Grid Wraps**: Product cards must maintain consistent
    aspect ratio and align price baselines across rows.
