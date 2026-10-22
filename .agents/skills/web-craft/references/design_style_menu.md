# Design Style Menu

The 24 visual styles an artifact can start from, in two registers. SKILL.md 4.1
covers how to choose one; this file is the menu.

--------------------------------------------------------------------------------

## Loading a Style

Each style is one file, `references/style_<slug>.md`. Load only the style you
choose. Its Setup section has the font `<link>` and the `:root` block; the rest
of the file says how the style looks: color proportions, type voice, ranked
defining treatments with CSS, composition, components, data visualization,
motion, and what to avoid. Complete `:root` with the shared tokens in
**references/design_foundation.md**.

Every style defines the same core token names (`--background`, `--on-surface`,
`--primary`, `--data-1`, and so on), so shared code and scaffolds work with any
of them.

--------------------------------------------------------------------------------

## Classic

Even-keeled and professional. Suits most content.

### Atelier

Light. "Restraint Is the Luxury." A culture magazine or gallery catalogue:
near-monochrome ink on warm white stone, one muted taupe, high-contrast Didone
headlines with a single italic word, widely tracked small caps, thin black
rules, and generous gallery margins.

-   **Best for**: culture and art, design and architecture, fashion, travel
    features, biographies and profiles, exhibition or collection guides, premium
    brand and product stories.
-   **Avoid for**: dense operational dashboards, urgent or safety content,
    playful or children's material, anything that needs loud color coding.
-   **File**: references/style_atelier.md

### Aurora

Dark. "Calm Under Northern Skies." A fatigue-free dark interface on soothing
oceanic mineral-slate surfaces: mist-white typography, glacier cyan for actions
and primary series, soft aurora sage for positive deltas, crisp sans headings,
and tonal vertical-gradient panels.

-   **Best for**: monitoring and live-status dashboards, market and trading
    screens, sleep and night-time tracking, energy and climate monitoring, and
    developer or technical tools.
-   **Avoid for**: formal historical or literary manuscripts, loud arcade games,
    ceremonial luxury invitations, anything meant to feel antique or
    paper-bound.
-   **File**: references/style_aurora.md

### Briefing

Light. "The Global Dossier." A worldly international affairs and urbanism
digest: warm stone-white paper, crisp bordered white figure cards, a signature
signal-gold dossier badge over a `1.5px` black section rule, editorial serif
headlines, and deep petrol-slate subheads.

-   **Best for**: policy, economics, and global affairs explainers; history and
    historical explainers; urbanism, transit, and infrastructure stories;
    comparative rankings and city/product indices; executive briefings and
    strategy summaries; modern journalism and research digests.
-   **Avoid for**: playful children's games, gothic or romantic poetry, neon
    nightlife, anything meant to feel raw, distressed, or unedited.
-   **File**: references/style_briefing.md

### Broadsheet

Light. "All the News, Weighed." The newspaper of record: warm ivory newsprint,
near-black ink, claret accents, bare teal tags, heavy slab-serif headlines
(`Bitter`) over a sober reading serif (`Source Serif 4`), hairline column
dividers, and a `3px double` masthead rule.

-   **Best for**: news explainers, history and historical explainers (timelines,
    wars, dynasties, genealogies), finance and markets, policy and economics,
    current events, briefings and analysis, reports that weigh evidence.
-   **Avoid for**: playful or children's content, lifestyle and wellness,
    product marketing, anything meant to feel soft, romantic, or futuristic.
-   **File**: references/style_broadsheet.md

### Canopy

Light. "Under the Garden Canopy." A kitchen-garden and permaculture almanac in
late afternoon: warm topsoil and loam cream layers, deep canopy green, harvest
ochre, a 12-month monospace phenology/cycle strip (`J F M A M J J A S O N D`),
soft `16px` organic card corners, and one pale-leaf highlight card.

-   **Best for**: gardening, agriculture, and botany; food, cooking, and
    seasonal recipes; nature, ecology, and sustainability; health, nutrition,
    and wellbeing; community and family guides; personal trackers, planners, and
    gentle how-to tools.
-   **Avoid for**: high-frequency financial trading consoles, urgent incident
    dashboards, nightlife, anything meant to feel sharp, metallic, or neon.
-   **File**: references/style_canopy.md

### Carbon

Light. "Productive Clarity." A systematic enterprise design system: pure white,
a disciplined gray surface ramp, one decisive blue, square corners, `2px`
bottom-ruled metric tiles, and a single technical sans paired with a monospace
data voice.

-   **Best for**: dashboards and analytics, admin and operations tools,
    technical reports, product and engineering documentation, data-dense tables,
    calculators and configurators, anything that must read as reliable.
-   **Avoid for**: personal or emotional stories, celebrations, lifestyle and
    hospitality, children's content, anything meant to feel warm, crafted, or
    playful.
-   **File**: references/style_carbon.md

### Charter

Light. "Stewardship in Navy and Brass." An institutional annual report or
executive charter: a full-bleed deep navy title band (`#14213d`) edged in
burnished brass over warm cream paper, upright Caslon headlines, brass-ruled
figure cards, and crisp tabular numerals.

-   **Best for**: reports, financial summaries, formal briefs, investment and
    portfolio reviews, legal or policy memos, board and strategy documents, KPI
    dashboards for an executive audience.
-   **Avoid for**: playful or children's content, consumer product launches,
    creative or cultural features, anything casual, loud, or experimental.
-   **File**: references/style_charter.md

### Figure

Light. "The Chart Does the Talking." An annotated journalistic figure or data
essay: a clean white page, a reading serif for the narrative, a heavy grotesk
for headlines, monospace for every number, gray context lines with one bright
focal series, and inline prose highlights matched to the series color.

-   **Best for**: data stories, explainers with charts, research summaries,
    elections, climate, economics, public-policy analysis, dashboards that need
    to explain as well as report.
-   **Avoid for**: content with no numbers to show, luxury or lifestyle brands,
    poetry and memoir, playful content for children.
-   **File**: references/style_figure.md

### Handbook

Light. "Plain, Direct, and Built for Everyone." A high-contrast, plain-language
reference handbook or step-by-step guide: black on white, deep navy and link
blue, a heavy `6px` top index rule with square numbered step badges, `5px`
left-bordered callouts, and a bright `#ffdd00` focus state.

-   **Best for**: step-by-step guides, checklists, eligibility checkers, civic
    and policy information, public notices, forms and calculators, explainers of
    rules, rights, procedures, or deadlines.
-   **Avoid for**: brand storytelling, luxury or fashion, literary or emotional
    narratives, playful or children's content, anything that wants atmosphere
    over clarity.
-   **File**: references/style_handbook.md

### Haven

Light. "Quiet Sufficiency." A calm, uncluttered domestic and everyday refuge:
cool pale mist-gray, soft black, muted slate and sage, light geometric
headlines, `1px` hairline card borders, small radii, and zero shadows.

-   **Best for**: lifestyle, wellbeing, home and interiors, how-to guides, calm
    planners and trackers, everyday utility tools, gentle explainers.
-   **Avoid for**: urgent or high-drama content, luxury or ceremonial occasions,
    loud marketing, content that needs a strong historical or literary voice.
-   **File**: references/style_haven.md

### Kiln

Light. "Quiet Craft, Fired in Stone." A craft monograph or ceramic studio
catalogue: warm unbleached washi paper, sumi-charcoal ink, quiet lichen-moss
green, upright `Shippori Mincho` headlines, pale washi-stone panels anchored by
a `2px` sumi left spine, and a vertical cinnabar seal stamp.

-   **Best for**: culinary craft, tea/coffee and food stories, architecture and
    interiors, travel and place guides, nature and gardens, mindfulness and
    wellbeing, cultural history, and calm personal tools or planners.
-   **Avoid for**: high-frequency trading or incident consoles, loud promotional
    campaigns, children's arcade games, anything that wants neon or glossy
    chrome.
-   **File**: references/style_kiln.md

### Maison

Dark. "Ivory on Espresso, After Dark." A couture house's evening issue:
espresso-black ground, warm ivory type, champagne hairlines, a thin high-fashion
display face (`Italiana`) over widely tracked small caps, and a centered
masthead.

-   **Best for**: fashion, luxury goods, fine dining and menus, perfume, film,
    nightlife, premium culture (galleries, opera, archives), brand stories.
-   **Avoid for**: dense dashboards and operational tools, technical or
    scientific content, public services, children's material, anything that
    needs to feel cheerful, urgent, or plain.
-   **File**: references/style_maison.md

### Nocturne

Dark. "The Midnight Observatory." An astronomical logbook or nocturnal reading
room: deep Prussian-midnight surfaces, warm parchment-ivory type, burnished
celestial brass for actions and focal series, pale horizon-sky blue for
coordinates, classical old-style serif headlines (`EB Garamond`), and crisp
monospace readouts.

-   **Best for**: science, space, physics, and astronomy; deep-dive technical
    explainers; thoughtful analytics and metrics dashboards.
-   **Avoid for**: loud promotional launches, playful children's content,
    daylight-first civic or clinical forms, anything that wants bright pastel
    cheer.
-   **File**: references/style_nocturne.md

### Showroom

Light. "Quietly Premium." A sunlit industrial-design showroom or product
showcase: cool off-white, near-black text, one confident blue, big tightly
tracked `Inter Tight` headlines, centered compositions, pill actions, and large
borderless `20px` bento tiles.

-   **Best for**: product and how-it-works explainers, focused tools and
    calculators, onboarding and setup guides, feature overviews, launch or spec
    summaries.
-   **Avoid for**: literary, historical, or heritage content, dense multi-panel
    dashboards, anything that should feel handmade, raw, or playful.
-   **File**: references/style_showroom.md

### Terracotta

Light. "Sunlit Plaster and Courtyard Shade." A riad courtyard in late afternoon:
warm tadelakt lime-plaster surfaces, burnt terracotta clay, burnished brass
diamond rules, cool zellige emerald badges, and arched metric cards (`28px 28px
6px 6px`).

-   **Best for**: travel and place guides, food, wine, and hospitality,
    architecture and interiors, culture and craft stories, itinerary planners,
    lifestyle and reading-friendly explainers.
-   **Avoid for**: dense operational dashboards, urgent alerts or incident
    tools, highly technical or developer content, anything that should feel
    clinical, cold, or childlike.
-   **File**: references/style_terracotta.md

### Vitals

Light. "Calm Confidence." Clear human readings and reassuring guidance: clean
white, calm clinical teal, and healthy green set in a typeface designed for
legibility (`Atkinson Hyperlegible`), with `4px` status accent bars and target
reference-range bands.

-   **Best for**: health and wellness, test results and readings, benefits and
    insurance explainers, public-health information, care plans, personal
    finance or family guides, anything that needs to reassure and be very
    readable.
-   **Avoid for**: luxury, fashion, or nightlife; edgy or playful brands;
    literary or historical narratives; dense trading-style dashboards.
-   **File**: references/style_vitals.md

--------------------------------------------------------------------------------

## Expressive

A strong, distinctive voice. For content whose tone calls for it.

### Bauhaus

Light. "Form Follows Function." A modernist workshop primer or Bauhaus poster:
warm off-white stock, near-black ink, oversized geometric grotesk, `3px` solid
black borders, hard offset shadows, and flat blocks of primary yellow, red, and
blue.

-   **Best for**: design and architecture topics, manifestos and opinion pieces,
    explainers that should feel energetic, product and startup overviews,
    workshop and course material, bold data stories, tools that want a strong
    graphic voice.
-   **Avoid for**: grief, health, or other sensitive content; luxury or heritage
    brands; quiet literary reading; anything that should feel soft, calm, or
    intimate.
-   **File**: references/style_bauhaus.md

### Deco

Dark. "The Grand Salon After Dark." A jazz-age poster or 1930s ocean-liner
salon: deep emerald-black lacquer, burnished gold, and cream, with widely
tracked geometric all-caps headlines, double gold frames, vertical pinstripes,
and strict mirror symmetry.

-   **Best for**: history (especially 1900–1940), storytelling, events,
    invitations and galas, food and drink, hospitality, travel and transport
    history, architecture.
-   **Avoid for**: dense operational dashboards, technical or product
    documentation, health and safety content, anything somber, urgent, or aimed
    at young children.
-   **File**: references/style_deco.md

### Moderne

Light. "Optimism, Moulded." Warm mid-century modern print: cream stock, flat
inks of mustard, teal, and burnt orange, a bold display serif, asymmetric
leaf-cornered cards (`2.25rem 0.5rem`), and overlapping multiply-blended ink
circles.

-   **Best for**: design and culture history, food and recipes, home and
    interiors, friendly explainers, product and object stories, light personal
    planners and trackers.
-   **Avoid for**: somber or sensitive subjects, dense financial or technical
    dashboards, legal or medical content, anything that must feel neutral or
    institutional.
-   **File**: references/style_moderne.md

### Neon Noir

Dark. "Electric Nightscape." A rain-slicked metropolis after midnight:
blue-black sky, signage in hot pink and cyan bleeding diffused light into the
dark, gradient geometric headlines, and a monospace HUD readout.

-   **Best for**: gaming, music and nightlife, esports and streaming stats, tech
    launches and developer tools, sci-fi and cyberpunk topics, hackathons, dense
    dark dashboards and monitoring views.
-   **Avoid for**: formal, institutional, medical, or financial reporting; grief
    or quiet personal stories; content for young children; anything that should
    feel calm, warm, or traditional.
-   **File**: references/style_neon_noir.md

### Raster

Light. "Grid, Type, Signal." Named for the Swiss typographic *Rastersystem*
(grid system): an International Typographic Style poster on off-white stock with
one heavy grotesk set huge and lowercase, a full-bleed signal-red index column,
and exposed `2px` black grid rules.

-   **Best for**: data stories, urbanism and transit, architecture and design,
    timelines and histories of systems, explainers built around a few strong
    numbers, clean dashboards.
-   **Avoid for**: intimate or sentimental content (letters, memorials,
    weddings), children's content, anything that should feel soft, handmade, or
    luxurious.
-   **File**: references/style_raster.md

### Riso

Light. "Two Inks, Slightly Off." A risograph print from an indie studio: fluoro
pink and riso blue on warm halftone-dotted paper, a navy third drum for the
words, a flood of yellow, and misregistered offset shadows where the drums don't
quite line up.

-   **Best for**: science for curious minds, arts and culture, community
    projects and events, education and explainers, small-press or studio
    content.
-   **Avoid for**: formal finance, legal, or medical content, grief or somber
    subjects, luxury brands, dense operational dashboards that need a neutral
    ground.
-   **File**: references/style_riso.md

### Sonnet

Light. "Ink, Candlelight, and Gilt Edges." A cloth-bound volume of the Romantic
poets: aged ivory paper with a warm vignette, iron-gall ink, deep oxblood drop
caps, double antique-gold frames, and italic old-style serifs.

-   **Best for**: poetry and literature, letters and memoir, literary history,
    weddings and anniversaries, heartfelt personal stories, reading guides.
-   **Avoid for**: dense dashboards and data tools, technical or product
    content, anything urgent, playful, or aimed at young children.
-   **File**: references/style_sonnet.md

### Sticker

Light. "Joyful Pop." Die-cut sticker sheets and playful pop: hot pink, grape
purple, and sky blue on a pink-white page, with everything rounded into pills
and soft slabs that float on shadows tinted their own color.

-   **Best for**: learning and quiz tools for kids and families, habit and
    streak trackers, games and scoreboards, celebrations and invitations,
    consumer product explainers, lighthearted personal stats.
-   **Avoid for**: grief, health, legal, or financial-risk content, serious
    journalism and research, enterprise dashboards, anything that needs to feel
    sober or authoritative.
-   **File**: references/style_sticker.md
