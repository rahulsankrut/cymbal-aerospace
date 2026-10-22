# Portfolio & Photography Design Guidelines

This reference covers creative portfolios, video editing showreels, photography
galleries, writer brainstorm / markdown tools, and student achievement
showcases.

--------------------------------------------------------------------------------

## 1. Scope & Taxonomy Coverage

-   **Avant-Garde & Editorial Visual Portfolios**: High-retention video
    showreels, creative direction, cinematography, oversized brutalist
    typography.
-   **Photography & Visual Arts Galleries**: Media-first masonry grids, lightbox
    viewers, metadata overlays (EXIF data: ISO, aperture, focal length).
-   **Writing & Markdown Brainstorming Tools**: Split mind-map canvas + full
    markdown manuscript view, focused writing pane.
-   **Student Achievement & Alumni Directories**: Student cohort profile
    directories, achievement showcases, 3-column student cards with clean photo
    avatars.

--------------------------------------------------------------------------------

## 2. Visual Architecture & Layout Rules

### A. Media-First Masonry & Bento Grid

-   **Dynamic Bento Box**: Combine wide showcase cards (`col-span-2 row-span-2`)
    with compact project thumbnails (`col-span-1 row-span-1`). Soft rounded
    corners (`rounded-2xl` / 16px).
-   **Minimalist Framing**: Let the visual artwork or video reel provide the
    primary color. Surfaces should remain crisp pure white, cool off-white, warm
    paper (for editorial monographs), or stark jet black (`#050505`).
-   **Fullscreen Lightbox / Modal**: Clicking any project tile opens an
    unobstructed high-resolution media viewer with clean title, date, client
    credits, and high-contrast close button (`ESC` or top-right `✕`).

### B. Split-Screen Hero & Oversized Typographic Impact

-   **Hero Split**: Left column holds the typographic hierarchy (kicker,
    headline, lead copy, primary CTA); right column holds one large visual
    container at matching height. Put key metrics (e.g., "12M+ Audience Reach",
    "800+ Hours Edited") in a full-width row below the split, not inside the
    left column.
-   **Section Dividers**: Subtle animated marquee text ribbons (e.g. repeating
    `"selected works · case studies · film & motion"`) acting as elegant section
    dividers.

### C. Student & Team Profiles Layout

-   **3-in-a-Row Grid**: On desktop ($1440\text{px}$), display clean horizontal
    rows of 3 student profile cards with consistent avatar sizing
    ($96\text{px}\times 96\text{px}$ or square $1:1$), roll number, discipline,
    and achievement highlights rendered as clean unboxed text with typographic
    separators (no pill enclosures).
-   **Modal Profile Expansion**: Clicking a profile opens a full achievement
    detail modal with student portfolio projects, bio, and awards.

--------------------------------------------------------------------------------

## 3. Typography & Color Strategies

-   **Typography**:
    -   Primary Headings: Bold architectural or geometric sans-serif (`Outfit`,
        `Bricolage Grotesque`, `Plus Jakarta Sans`, `Urbanist`, `Archivo`) with
        tight tracking (`tracking-tight`).
    -   Secondary / List Items: Expressive editorial serif (`Playfair Display`,
        `Fraunces`, `Cormorant Garamond`) creating a curated monograph
        aesthetic.
    -   Body Text: Clean, highly legible geometric sans (`Plus Jakarta Sans`,
        `DM Sans`, `Manrope`, `Public Sans`) at 14px–15px.
-   **60-30-10 Color Budget**:
    -   **60% Neutral Canvas**: Monochromatic stark black (`#050505`), crisp
        white, cool off-white, or warm paper for editorial portfolios.
    -   **30% Structural & Media Framing**: Clean card outlines (`#E4E4E7` /
        `#27272A`), high-resolution photo/video containers, and editorial grid
        dividers.
    -   **10% High-Contrast Focal Accent**: Single vibrant focal color for
        interactive links and primary action (mustard yellow `#F2B705`, electric
        cobalt `#2563EB`, or cinnabar red `#E11D48`).

--------------------------------------------------------------------------------

## 4. `generate_image` Recipes for Creative Portfolios

```typescript
// 1. Avant-Garde Video Director Hero
generate_image({
  Prompt: "Cinematic black-and-white editorial portrait of a creative film director behind a professional cinema camera, dramatic rim lighting, moody film grain texture, high-fashion magazine aesthetic.",
  ImageName: "hero_director_portrait",
  AspectRatio: "16:9"
});

// 2. High-Fashion Photography Showcase
generate_image({
  Prompt: "Avant-garde editorial fashion photograph with bold sculptural silhouettes, stark minimalist studio lighting, high contrast, elegant high-end fashion magazine spread.",
  ImageName: "portfolio_fashion_editorial",
  AspectRatio: "4:3"
});

// 3. Student / Creative Team Avatar
generate_image({
  Prompt: "Warm natural light studio portrait headshot of a young creative designer, neutral cream background, soft friendly expression, 8k commercial quality portrait.",
  ImageName: "avatar_student_designer",
  AspectRatio: "1:1"
});
```

--------------------------------------------------------------------------------

## 5. Anti-Patterns to Avoid

-   ❌ **No Watermark / Ghost Typography**: Absolutely prohibit placing large,
    low-opacity ghost words or phrases behind headings (e.g., giant faded `"MEET
    THE BATCH"` or `"PORTFOLIO"` text behind content).
-   ❌ **No Broken Image Placeholders**: When images are loading or unavailable,
    use elegant solid color blocks with subtle title text, never raw unstyled
    image boxes.
-   ❌ **No Over-Decorated Navigation**: Avoid cluttered navigation headers with
    multiple pills; stick to the clean 3-zone Top Bar Contract.
