# Hand-Drawn Component Library & GM3 Equivalents

-   **Visual Component Library:** <http://go/hand-drawn-skill-components>
-   **Usage Guide & Instructions:** <http://go/hand-drawn-skill-instructions>

This document defines the strictly ALLOWED components when building UI with the
`hand-drawn-ui` skill. You MUST NOT invent any other components or styling
wrappers. Always use the structural representations defined here.

## Base CSS Utilities

When starting a Hand-Drawn page, always include these utilities (usually within
a `<style>` block):

```css
.sketchy-box {
  position: relative;
  border-radius: 24px;
  box-shadow: 0px 1px 2px 0px rgba(0, 0, 0, 0.30), 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
  background: #FFFFFF;
}
.sketchy-box::before,
.sketchy-box-flat::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 24px;
  padding: 1px;
  background: linear-gradient(145deg, rgba(32, 33, 36, 0.65) 0%, rgba(32, 33, 36, 0.15) 100%);
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  z-index: 10;
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}
.sketchy-box-flat {
  position: relative;
  border-radius: 24px;
}
.sketchy-box-pill {
  position: relative;
  border-radius: 9999px;
}
.sketchy-box-pill::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9999px;
  padding: 1px;
  background: linear-gradient(145deg, rgba(32, 33, 36, 0.65) 0%, rgba(32, 33, 36, 0.15) 100%);
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  z-index: 10;
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}
.sketchy-btn {
  position: relative;
  border-radius: 24px;
  transition: all 0.1s ease;
  cursor: pointer;
  padding: 8px 20px;
  font-weight: normal;
}
.sketchy-btn::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 24px;
  padding: 1px;
  background: linear-gradient(145deg, rgba(32, 33, 36, 0.65) 0%, rgba(32, 33, 36, 0.15) 100%);
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  z-index: 10;
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}
.sketchy-btn:active {
  transform: translateY(1px);
}

.sketchy-line {
  height: 1px;
  background: linear-gradient(145deg, rgba(32, 33, 36, 0.35) 0%, rgba(32, 33, 36, 0.10) 100%);
}
.gm3-callouts-container *,
.gm3-callouts-container *::before,
.gm3-callouts-container *::after {
  box-shadow: none !important;
  filter: none !important;
  border: none !important;
  border-bottom: none !important;
  border-top: none !important;
  outline: none !important;
}
.gm3-section, .gm3-section * {
  font-family: 'Google Sans Text', 'Google Sans', sans-serif !important;
}
.gm3-label-large {
  font-family: 'Google Sans Text', 'Google Sans', sans-serif !important;
  font-weight: 500 !important;
  font-size: 14px !important;
  line-height: 20px !important;
}
.sketchy-body-medium {
  font-family: 'Architects Daughter', cursive, sans-serif;
  font-size: 14px;
  line-height: 20px;
}
```

## Base SVG Definitions

For hand-drawn gradients and SVG elements, include `IconDefs`:

```tsx
export const IconDefs = () => (
  <svg width="0" height="0" className="absolute pointer-events-none">
    <defs>
      <linearGradient id="sketchGradient" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stopColor="#202124" stopOpacity="0.65" />
        <stop offset="100%" stopColor="#202124" stopOpacity="0.15" />
      </linearGradient>
    </defs>
  </svg>
);
```

## The Component Library

### 0. Page Layout & Backgrounds

> ⚠️ **CRITICAL BORDER RULE**: NEVER attempt to fake a sketchy aesthetic by
> manually applying native CSS borders like `border-dashed` or `border-dotted`
> to buttons, dropdowns, inputs, or layouts. Doing so creates rigid, geometric
> lines that conflict with the organic hand-drawn style. You MUST strictly use
> `.sketchy-box`, `.sketchy-box-flat`, `.sketchy-box-pill`, or `.sketchy-btn`
> because they natively simulate pencil strokes via SVG masks. `border-dashed`
> is strictly reserved ONLY for empty wireframe Image placeholders or explicit
> dividers.

> ⚠️ **CRITICAL PAGE WRAPPER RULE**: Do NOT use `.sketchy-box` or
> `.sketchy-box-flat` as the main page wrapper or page background container. The
> hand-drawn borders and drop shadows are strictly for individual UI components
> (buttons, cards, inputs). For **ALL** layouts (both "Full Page" and "Page Body
> Only"), you MUST explicitly set the outermost wrapper background to a light
> grey (`bg-[#F8F9FA]` or `bg-gray-50`) AND you MUST apply `min-h-screen` to
> ensure the grey background stretches all the way to the bottom of the viewport
> (e.g., `<div className="bg-gray-50 min-h-screen ...">`). Do NOT use
> `bg-white`, and do NOT leave it transparent. We need the white cards to
> visibly pop against the grey backdrop, regardless of what color canvas the
> host application uses!

> ⚠️ **LARGE CONTENT GROUPING EXCEPTION**: If the page contains a sprawling,
> data-dense block that spans the full width of the main content area (e.g., a
> Calendar Grid, a large multi-field Form, or a Data Table), you MUST group that
> entire block inside a full-width outlined card (using `<div
> className="sketchy-box-flat bg-white p-4 w-full">`). This visually anchors
> complex content into a cohesive, readable unit while anchoring the section
> against the light-grey backdrop.

> ⚠️ **IFRAME HEIGHT CONSTRAINT**: Because these prototypes often render inside
> a sandboxed iframe in Jetski's Generative UI, height constraints require
> specific strategies: (1) For standard scrolling "Full page" layouts, do NOT
> use `h-screen`, `h-[100vh]`, or `overflow-hidden` on the main page wrapper.
> You MUST ALWAYS use `min-h-screen` and allow natural scrolling. (2) For
> Fixed-Viewport Apps (like Chat UIs where the prompt bar must stay pinned to
> the bottom), `min-h-screen` will fail. You MUST inject an invisible structural
> shim (`<div style={{height:'600px', width:'100vw',
> visibility:'hidden'}}></div>`) exactly before the outermost `<div
> className="absolute inset-0 flex flex-col w-full overflow-hidden">` wrapper.
> The inner content area then uses `flex-1 overflow-y-auto` while
> footers/headers remain outside the scroll boundary, firmly pinned within the
> absolute frame.

### 1. Typography

**Hand-Drawn:** `fontFamily: "'Architects Daughter', cursive, sans-serif"`
globally on the main container.

> ⚠️ **CRITICAL RULE**: NEVER apply `font-sans`, `font-serif`, or `font-mono`
> tailwind classes to any text elements (paragraphs, spans, divs). Doing so
> overrides the inherited sketchy font and breaks the hand-drawn illusion. ⚠️
> **CRITICAL WEIGHT RULE**: NEVER use `font-bold`, `font-semibold`,
> `font-medium`, or `<strong>` tags. The Architects Daughter font does not
> support thicker weights natively, and browsers will badly blur the text in an
> attempt to fake it. Distinguish text hierarchy strictly using font sizes like
> `text-2xl` and `text-lg` instead.

-   Headline medium: `<p className="text-[30px]">`
-   Headline small: `<p className="text-2xl">`
-   Title medium: `<p className="text-lg">`
-   Body large: `<p className="text-base">`
-   Body medium: `<p className="text-sm">` (or use `.sketchy-body-medium`)

**GM3 Equivalent:** Wrapped in `<div className="gm3-section">`

-   Headline Medium: `<p className="text-[28px] leading-[36px] text-[#1f1f1f]">`
-   Headline Small: `<p className="text-2xl font-normal text-[#1f1f1f]">`
-   Title Medium: `<p className="text-lg text-[#1f1f1f]">`
-   Body Large: `<p className="text-base font-normal text-[#1f1f1f]">`
-   Label Large: `<p className="gm3-label-large text-on-surface">`
-   Body Medium: `<p className="gm3-body-medium text-on-surface">`

### 2. Buttons

**Hand-Drawn:** ⚠️ **CRITICAL COLOR RULE**: You MUST explicitly use the EXACT
class strings below for buttons. NEVER use standard Tailwind colors (e.g.
`bg-blue-500`, `bg-blue-600`, `text-white`, `bg-gray-100`, `bg-gray-200`) for
button backgrounds. NEVER apply Tailwind borders (e.g. `border border-blue-600
rounded-full`).

-   Outlined (White): `<button className="sketchy-btn bg-white text-[#202124]">`
    (Only grey outline exists. NEVER use `bg-gray-100` or `bg-gray-200`).
-   Filled (Light Blue): `<button className="sketchy-btn bg-[#DDE7FF]
    text-[#002D62]">` (This is the ONLY allowed colored button. NEVER use dark
    blue `bg-blue-500` or `bg-blue-600`).
-   Text only: `<button className="w-fit text-[#1a73e8] hover:underline
    cursor-pointer text-base">`

> ⚠️ **CRITICAL RULE**: NEVER place icons inside of buttons. Buttons must ONLY
> contain text. Do not add Material Symbols inside button wrappers. ⚠️
> **CRITICAL RULE**: ALL buttons (whether outlined, filled, or text-only) MUST
> always be left-aligned within their flex or grid container. NEVER use
> `justify-center`, `justify-end`, `text-center`, or `text-right` for button
> placement. Use `justify-start` instead. ⚠️ **IMPORTANT**: Do not allow
> `.sketchy-btn` to stretch vertically inside flexbox containers (e.g. `flex`
> without `items-center` or `items-start`). Stretching the button increases its
> height, which breaks its baked-in 24px border radius and causes it to lose its
> fully rounded pill shape. Ensure buttons maintain their default intrinsic
> padding!

**GM3 Equivalent (gm3-vibe):**

-   `<Button variant="outlined" className="!rounded-full">`
-   `<Button variant="filled" className="!rounded-full">`
-   `<Button variant="text" className="!rounded-full">`

### 3. Cards

**CRITICAL RULE:** The Outlined Card is the default card standard for the
Hand-Drawn design system. Always use the Outlined Card variant unless the user
explicitly requests an Elevated Card.

> ⚠️ **CRITICAL SPARING COLOR RULE**: All cards, grid containers, and sub-panels
> MUST use a clean white background (`bg-white`) by default. NEVER use grey
> backgrounds (e.g. `bg-gray-50`, `bg-gray-100`) for cards, and NEVER paint
> entire card backgrounds with full colored pastel tints (e.g. `bg-blue-50`).
> Color MUST be used sparingly and strictly reserved ONLY for: 1. **Status
> Badges & Chips** (e.g., `bg-[#E6F4EA] text-[#137333]`). 2. **Primary Action
> Buttons** (e.g., `bg-[#DDE7FF] text-[#002D62]`). 3. **Small Icon Circles**. 4.
> **Selected/Active States** (e.g., `bg-[#C2E7FF]`). 5. **Data Visualizations**
> (charts, progress bars). 6. **KPI/Statistical Metric Cards**. ⚠️ **GLOBAL
> COLOR PALETTE**: When you DO use color for ANY of the exceptions above
> (especially data vis, charts, and progress bars), you MUST strictly limit your
> color choices to the exact hex codes used in our Badges palette (`[#002D62]` &
> `[#DDE7FF]`, `[#137333]` & `[#E6F4EA]`, `[#B06000]` & `[#FEF7E0]`, `[#C5221F]`
> & `[#FCE8E6]`). **CRITICAL PASTEL FILL RULE**: For progress bars, charts, and
> infographics, you MUST ONLY use the LIGHT PASTEL hex codes (`bg-[#DDE7FF]`,
> `bg-[#E6F4EA]`, `bg-[#FEF7E0]`, `bg-[#FCE8E6]`) for the shapes, bars, and
> fills. The dark hex codes (like `#137333`) are STRICTLY RESERVED for text or
> icons. NEVER use them as a background fill! NEVER invent or fallback to
> standard Tailwind class colors (like `bg-purple-300` or `bg-green-400`). The
> entire application must cleanly share this single strict hex palette!

**Hand-Drawn:**

-   Outlined: `<div className="sketchy-box-flat h-32 bg-white"></div>` (DEFAULT
    FOREVER. Do NOT apply Tailwind `rounded-*`, `border-*`, or `shadow-*`
    classes to this!)
-   Elevated: `<div className="sketchy-box h-32 bg-white"></div>` (FORBIDDEN
    unless specifically asked. Do NOT apply Tailwind `rounded-*` or `shadow-*`
    to this!)

**GM3 Equivalent:**

-   `<Card variant="elevated" className="h-32 bg-white" />`
-   `<Card variant="outlined" className="h-32 bg-white" />`

### 4. Text Fields

**Hand-Drawn:**

-   Single Line: `<div className="w-full sketchy-box-flat bg-white flex
    items-center"><input type="text" className="w-full h-full bg-transparent
    px-4 py-4 outline-none text-base text-[#202124] placeholder:text-gray-400"
    placeholder="..." /></div>`
-   Multi-line: `<div className="w-full h-32 sketchy-box-flat bg-white flex
    flex-col justify-start items-start"><textarea className="w-full h-full
    bg-transparent p-4 outline-none resize-none text-base text-[#202124]
    placeholder:text-gray-400" placeholder="..." /></div>` > ⚠️ **CRITICAL INPUT
    RULE**: Do NOT apply `.sketchy-box` or `.sketchy-box-flat` directly to
    `<input>` or `<textarea>` elements! CSS `::before` pseudo-element strokes
    will not render on inputs. You MUST always use an outer wrapper `div` with
    the sketchy classes, and place a completely unstyled `bg-transparent
    outline-none` `<input>` inside of it.

**GM3 Equivalent:**

-   `<TextField noLabel placeholder="..." />`
-   `<TextField noLabel multiline rows={4} placeholder="..." />`

### 4b. Search Bar

**Hand-Drawn:**

-   `<div className="w-full p-4 sketchy-box-pill bg-white text-base
    text-[#202124] flex items-center">`
    -   Internal layout: `<span className="material-symbols-outlined
        text-gray-500 mr-2">search</span><div className="opacity-50">...</div>`

**GM3 Equivalent:**

-   `<TextField noLabel leadingIcon={<Icon>search</Icon>}
    className="[&_div.gm3-text-field\_\_container]:!rounded-full"
    placeholder="..." />`

### 5. Selection Controls (Checkboxes, Radio, Chips, Dropdown)

**Hand-Drawn:**

-   Checkbox: `<svg viewBox="0 0 18 18" width="18" height="18" fill="none"
    className="overflow-visible inline-block"><rect x="1" y="1" width="16"
    height="16" rx="2" stroke="url(#sketchGradient)" strokeWidth="1.5" />{/* If
    checked, add this polyline: */}<polyline points="3.5 9.5 7.5 13.5 19 -1.5"
    stroke="#1a73e8" strokeWidth="2.2" fill="none" strokeLinecap="round"
    strokeLinejoin="round" /></svg>`
-   Radio Button: `<svg viewBox="0 0 18 18" width="18" height="18" fill="none"
    className="inline-block"><circle cx="9" cy="9" r="8"
    stroke="url(#sketchGradient)" strokeWidth="1.5" />{/* If checked, add this
    inner circle: */}<circle cx="9" cy="9" r="4.5" fill="#1a73e8" /></svg>`
-   Chips: `<button className="sketchy-btn bg-[#DDE7FF] ...">`
-   Dropdown: `<div className="sketchy-box-flat pl-4 pr-3 py-3 bg-white flex
    items-center justify-between text-sm cursor-pointer">`

**GM3 Equivalent:**

-   `<Checkbox />`, `<RadioButton />`
-   `<Chip variant="filter" className="!rounded-lg" />`
-   Dropdown: `<TextField readOnly trailingIcon={<Icon>arrow_drop_down</Icon>}
    />`

### 6. Callouts

**Hand-Drawn:**

-   Banner wrapper: `<div className="sketchy-box-pill bg-[COLOR] p-4 px-6 flex
    items-center justify-between gap-4">`
-   Colors: Info (bg-[#F4F9F5], text-[#137333]), Success (bg-[#F0F4FC],
    text-[#1a73e8]), Caution (bg-[#FEFCEE], text-[#b06000]), Error
    (bg-[#FDF4F4], text-[#c5221f]).

**GM3 Equivalent:**

-   `<Banner open={true} showDivider={false} className="![BG_COLOR] rounded-lg
    shadow-none !border-0" ... />` wrapped in `<div
    className="gm3-callouts-container">`. (Use !bg-[#d3e3fd] for info,
    !bg-[#ceead6] for success, !bg-[#fef1c7] for caution, !bg-[#fad2cf] for
    error).

### 7. Nav Drawer / Nav Rail / Flyout

**Hand-Drawn:**

-   App Bar: `<div className="pr-8 bg-[#F8F9FA] flex items-center
    justify-between w-full h-[64px] shrink-0 z-50">`
    -   Logo wrapper: `<div className="w-[80px] flex items-center justify-center
        shrink-0">` (⚠️ CRITICAL: DO NOT add `h-[64px]`, `border-r`, or any grey
        stroke outlines to this wrapper. Must include `items-center`)
    -   Logo pill: `w-[28px] h-[28px] rounded-full bg-gradient-to-br
        from-purple-200 to-blue-200`
    -   Title: `<span className="text-[22px] -ml-1 pt-1">Product name</span>`
        (⚠️ CRITICAL: NEVER replace "Product name" with the real page title).
-   Attached Nav Rail & Subnav layout:
    -   Base Layout: `<div className="flex flex-1 min-h-0">` containing both the
        Nav Rail and Subnav Drawer.
    -   Rail Wrapper: `<div className="relative z-50 shrink-0"><div
        className="w-[80px] h-full flex flex-col items-center py-4 px-2
        bg-[#F8F9FA]">`
    -   Active nav item label: `text-[12px]`
    -   Active nav item box: `bg-[#f1f3f4] border border-[#202124]/30
        rounded-xl`
    -   Subnav Flyout: Mounted adjacent to the rail using `<div
        className="absolute left-[80px] top-2 h-[calc(100%-8px)] w-[260px]
        bg-[#F8F9FA] shadow-[4px_0_16px_rgba(0,0,0,0.08)] z-[40] flex flex-col
        pt-4" style={{ clipPath: "polygon(0 0, 200% 0, 200% 100%, 0 100%)" }}>`

**GM3 Equivalent:**

-   Nav Drawer: `<LeftNav>` and `<LeftNavItem>` components from `gm3-vibe`.
-   Nav Rail: `<NavigationRail>` and `<NavigationRailItem>` components from
    `gm3-vibe`.
-   Flyout Drawer: `<NavigationDrawerItem>` components wrapped in a layout div.

### 8. App Bar

**Hand-Drawn:**

-   Wrapper: `<div className="px-4 bg-[#F8F9FA] flex items-center
    justify-between w-full h-[64px]">`
-   Top-Level Brand: `<div className="w-[28px] h-[28px] rounded-full
    bg-gray-300"></div>` + `text-[22px] pt-1`
-   Child-Page Brand: `<span className="material-symbols-outlined text-[26px]
    text-[#444746] font-light cursor-pointer pt-0.5">arrow_back</span>` +
    `text-[22px] pt-1`
-   Quick Icons: Use grey circles `<div className="w-[24px] h-[24px]
    rounded-full bg-gray-300"></div>`
-   Profile Avatar (Component Library Link): `<a
    href="http://go/hand-drawn-skill-components" target="_blank" className="w-8
    h-8 rounded-full border border-gray-400 border-dashed bg-gray-200..."><span
    className="material-symbols-outlined">person</span></a>`

**GM3 Equivalent:**

-   Use `<AppBarDesktop>` component from `gm3-vibe`.

### 9. Dialogs

**Hand-Drawn:**

-   Wrapper: `<div className="sketchy-box p-6 bg-white max-w-sm w-full
    mx-auto">` (often centered in a `fixed inset-0` overlay)
-   Actions: `<div className="flex justify-end gap-2 mt-6">`

**GM3 Equivalent:**

-   Real rendering: `<Dialog open={isOpen} onClose={...}>` from `gm3-vibe`.
-   Inline GM3 Mockup: `<div className="bg-surface-container-high rounded-[28px]
    max-w-[320px] shadow-none...">` (Do NOT use `Card variant="outlined"` to
    mock a Dialog!)

### 10. Dividers

**Hand-Drawn:** `<div className="sketchy-line w-full"></div>`

> ⚠️ **CRITICAL RULE**: ALWAYS use a dedicated empty DOM element for dividers.
> NEVER attach `border-b`, `border-dashed`, or any native Tailwind border rules
> to a content wrapper to separate list items. You MUST strictly use an empty
> `<div className="sketchy-line w-full"></div>` between every single row in a
> list or table to ensure visual consistency!

**GM3 Equivalent:** `<div className="border-b border-outline-variant
w-full"></div>` or `<Divider />`

### 11. Icons

**Hand-Drawn:** `<span className="material-symbols-outlined text-gray-700"
style={{ fontVariationSettings: "'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24"
}}>eco</span>`

> ⚠️ **CRITICAL RULE**: Icons must ALWAYS be verified strings from the **Google
> Material Symbols library** (e.g. use `eco`, never guess `leaf`). They must
> ALWAYS be rendered at the standard **default size of 24px** (do not shrink
> them with Tailwind `text-sm` or `text-base` classes). They must ALWAYS use the
> standard bold Material **weight of 400** (`wght: 400`), never light flaky
> weights like 200. Guessing names breaks the UI and shrinking them hurts
> legibility. Do not use an imaginary `<Icon>` component, use the `<span>`
> syntax above.

**GM3 Equivalent:** `<Icon>icon_name</Icon>`

### 12. Tabs

**Hand-Drawn:**

-   Container: `<div className="flex items-end border-b border-gray-300">`
-   Tab Item: `<button className="inline-flex flex-col cursor-pointer px-6 pt-2
    pb-0 bg-transparent border-none [text-[#1a73e8] FOR ACTIVE, text-[#202124]
    FOR INACTIVE]">`
    -   Text: `<span className="text-lg">Selected</span>`
    -   Active underline: `<div className="w-full h-[2.5px] bg-gradient-to-r
        from-[#1a73e8]/85 to-[#1a73e8]/35 rounded-full mt-1
        translate-y-[1px]"></div>`
    -   Inactive spacer (to prevent jumping): `<div className="w-full h-[2.5px]
        mt-1 opacity-0 pointer-events-none"></div>`

**GM3 Equivalent:** Use standard `<TabRow>` and `<Tab>` components from
`gm3-vibe`.

### 13. Paragraph text

**Hand-Drawn:** You MUST invent and write contextual, realistic text for
paragraphs and body copy. Do not use fake placeholder squiggly lines or generic
lorem ipsum text.

**GM3 Equivalent:** Real text wrapped in `gm3-body-medium` or `body-medium`.

### 14. Badges

**Hand-Drawn:**

⚠️ **CRITICAL RULE FOR ALL STATUSES AND LABELS**: You MUST use these exact Badge
components for ALL statuses, tags, labels, and small indicators. DO NOT invent
your own tailwind status tags (e.g. `bg-green-100 p-1 rounded`). You MUST
strictly use the `uppercase tracking-wider rounded-full` pill structure with the
exact hex codes below. ⚠️ **CRITICAL**: Prefer using semantic colored badges
instead of just grey, to add color to the page.

-   Grey: `<span className="text-xs uppercase tracking-wider text-[#202124]
    bg-[#F1F3F4] px-2 py-0.5 rounded-full">Badge</span>`

-   Blue: `<span className="text-xs uppercase tracking-wider text-[#002D62]
    bg-[#DDE7FF] px-2 py-0.5 rounded-full">Badge</span>`

-   Green: `<span className="text-xs uppercase tracking-wider text-[#137333]
    bg-[#E6F4EA] px-2 py-0.5 rounded-full">Badge</span>`

-   Yellow: `<span className="text-xs uppercase tracking-wider text-[#B06000]
    bg-[#FEF7E0] px-2 py-0.5 rounded-full">Badge</span>`

-   Red: `<span className="text-xs uppercase tracking-wider text-[#C5221F]
    bg-[#FCE8E6] px-2 py-0.5 rounded-full">Badge</span>`

**GM3 Equivalent:**

-   Import and use the appropriate GM3 component directly: `import { UeBadge }
    from 'ue-vibe';`
-   `<UeBadge color="grey" variant="tonal">BADGE</UeBadge>` (supported colors:
    `grey`, `blue`, `yellow`, `red`, `green`).

### 15. Avatar

**Hand-Drawn:**

-   Uses a dashed border block with a light gray background and dynamically
    scaling text initials (`BF`, `JK`, etc.).
-   Utilizes CSS container queries (`containerType: 'inline-size'`) on the
    wrapper and `40cqi` for the text to instantly respond to bounding-box
    sizing.
-   Scribing colors: Default to `bg-gray-100`, `border-gray-300`, text initials
    `#b0b3b8`.
-   **Colored Avatars**: If you decide to color-code multiple avatars in a list,
    you MUST strictly adhere to the GLOBAL COLOR PALETTE using the exact pastel
    background hex codes (`bg-[#DDE7FF]`, `bg-[#E6F4EA]`, `bg-[#FEF7E0]`,
    `bg-[#FCE8E6]`) and matching darker text (`text-[#002D62]`,
    `text-[#137333]`, `text-[#B06000]`, `text-[#C5221F]`). NEVER use standard
    Tailwind color classes.
-   Example: `<div className="w-24 h-24"><div style={{ containerType:
    'inline-size' }} className="w-full h-full rounded-full border
    border-gray-300 border-dashed bg-gray-100 flex items-center
    justify-center"><span className="text-[#b0b3b8] tracking-widest uppercase"
    style={{ fontSize: '40cqi' }}>BF</span></div></div>`

**GM3 Equivalent:**

-   Standard solid-background round element scaling similarly via container
    queries.
-   `<div className="w-24 h-24"><div style={{ containerType: 'inline-size' }}
    className="w-full h-full rounded-full bg-[#f1f3f4] flex items-center
    justify-center text-[#1f1f1f]"><span className="font-normal uppercase"
    style={{ fontSize: '40cqi' }}>BF</span></div></div>`

### 16. Image

**Hand-Drawn:**

-   Simple grey wireframe box with rounded corners and dashed borders mimicking
    low-fidelity empty states.
-   Class setup: `<div className="w-full h-full bg-gray-100 rounded-xl border
    border-gray-300 border-dashed flex items-center justify-center
    text-gray-400" />`
-   **CRITICAL**: You MUST ALWAYS use neutral grey coloring (`bg-gray-100`,
    `border-gray-300`, `text-gray-400`) for image placeholders and their icons.
    You are strictly forbidden from applying semantic or theme colors (e.g., no
    pink, blue, or yellow placeholders). Image placeholders must remain
    structural wireframes.

**GM3 Equivalent:**

-   Solid block without dashed borders.
-   Class setup: `<div className="w-full h-full bg-[#f1f3f4] rounded-lg" />`

> [!CRITICAL] CSS Container Rule You are STRICTLY FORBIDDEN from using standard
> geometric border classes (e.g., `rounded-lg`, `rounded-md`, `border`,
> `shadow-sm`) on cards, panels, or buttons. You MUST ALWAYS apply
> `.sketchy-box-flat`, `.sketchy-box`, or `.sketchy-btn` to every single
> container you generate. If you use standard web borders, it destroys the
> hand-drawn illusion.

### 17. Lists / Data Tables

**Hand-Drawn:**

-   Table Wrapper: To prevent columns from squishing and buttons from
    overflowing off the screen on narrow windows or side panels, you MUST wrap
    the entire list/table container in a responsive scroll shell: `<div
    className="w-full overflow-x-auto pb-4"><div className="min-w-[700px] flex
    flex-col w-full">` (⚠️ CRITICAL: always enforce a min-width on lists so
    columns don't crush. DO NOT use percentages for small buttons/icons columns
    without a min-w fallback).
-   Between Rows: Use `<div className="sketchy-line w-full"></div>` to separate
    items. Do not use `.sketchy-list-item` (it is deprecated).

**GM3 Equivalent:**

-   Standard HTML `<table>` or CSS grid, wrapped in an `overflow-x-auto` shell.

### 18. Chat Interfaces / Prompt Bars

**Hand-Drawn:**

-   DO NOT generate "suggested prompt" buttons, recommendation chips, or
    floating action pills above the chat input bar! These often clutter the
    minimalist hand-drawn aesthetic. You MUST strictly generate ONLY the prompt
    input pill itself unless the user *explicitly* asks for suggested prompts.

**GM3 Equivalent:**

-   Standard `<TextField>` wrapped in a generic container.

### 19. Data Visualization & Progress Bars

**Hand-Drawn:**

⚠️ **CRITICAL PASTEL RULE**: All charts, progress bars, and infographics MUST
use the light pastel hex codes (`bg-[#DDE7FF]`, `bg-[#E6F4EA]`, `bg-[#FEF7E0]`,
`bg-[#FCE8E6]`) for their fills/bars to maintain a light, sketchy aesthetic.
NEVER use the dark text hexes (e.g., `#137333`) for background fills.

*   **Progress Bar:**
    *   Track: `<div className="w-full h-4 sketchy-box-pill bg-white flex
        items-center p-0.5">`
    *   Fill: `<div className="h-full bg-[#E6F4EA] rounded-full" style={{ width:
        '70%' }}></div>`
*   **Bar Chart / Infographic Shapes:** Wrap the shapes in `.sketchy-box` or
    `.sketchy-box-flat` to give them a sketched outline, and fill them strictly
    with the pastel colors.

**GM3 Equivalent:**

*   Use standard `<LinearProgress />` or semantic color tokens.
