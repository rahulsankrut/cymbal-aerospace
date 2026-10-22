# Building the Component Kit

The Component Kit is a set of **self-contained HTML files**, one for each kind
of component in the design system, written to `<workspace-root>/components/`
(e.g. `components/button.html`, `components/card.html`,
`components/input-field.html`).

This set of HTML files is the **canonical visual reference** for all components.
When generating screens later, you MUST read these files and copy the exact HTML
structure and Tailwind classes for any component you use.

## Choosing Components

Decide which components to include. Every design system needs the basics —
buttons and typography. Beyond that, judge from the brand and the product's
requirements.

Component names come from the list in
[Available References](#available-references) below. A name that is not on that
list still works; you get a generic skeleton instead of a specific one.

## The Loop

Build **one component at a time**. Finish one before you scaffold the next. Do
not chain scaffold commands.

1.  **Scaffold it.** Run the pre-installed global command
    `scaffold-component-kit`:

    ```bash
    scaffold-component-kit --component button \
      --out <workspace-root>/components/
    ```

    The command writes `components/button.html` with the page boilerplate and
    every variant skeleton already in place, and prints the component reference
    to you.

2.  **Read what it printed.** That is the component's definition, its variants,
    its states, and its design checklist. You need all of it for the next three
    steps.

3.  **Fill in the prose placeholders.** The scaffold leaves two kinds of TODO:
    one under the page heading for what the component is and what it is for, and
    one under each variant heading for when to use that variant. Replace both.

4.  **Apply Tailwind classes** from the design system tokens. Do NOT change the
    structure, the `data-*` attributes, or the ARIA attributes — they encode the
    component's semantics and accessibility.

5.  **Work through the printed checklist** and confirm each item is either
    represented in the sticker sheet or consciously skipped.

## Page Structure

Each HTML file in `components/` loads the Tailwind CDN and imports
`../tailwind.config.js` as an ES module. The `scaffold-component-kit` script
emits this boilerplate for component files automatically.

> **Important:** Only `components/*.html` files import `../tailwind.config.js`
> as an ES module. When you later build screen HTML files under `screens/`, you
> **must** inline the `tailwind.config = { ... }` object directly inside a
> `<script>` tag and **never** use `<script type="module">import config from
> '.../tailwind.config.js'`, because screens are rendered as standalone HTML
> documents where relative ES module imports fail.

## Component Sections

Organize component variations inside each HTML file into `<section>` elements.
Each section has:

-   A heading naming the variant or size
-   A short line saying when to use that variant
-   Rendered examples of every state, wrapped in a flex container
-   HTML comments marking each component: `<!-- COMPONENT: component-name -->`

### Component Metadata

Every component root element MUST carry metadata for the component:

-   `data-component-id` — Matches the `<!-- COMPONENT: xxx -->` marker name
    (e.g., `"button-primary"`, `"card-metric"`).
-   `data-component-type` — Semantic category (e.g., `"button"`, `"card"`,
    `"chip"`).
-   `data-component-variant` — Variant (e.g., `"primary"`, `"ghost"`,
    `"filled"`).

Every visible text node inside a component MUST be wrapped in an element with
`data-design-text-token` set to the typography token used (e.g., `"label-lg"`,
`"body-md"`, `"headline-lg"`).

## Component References

The scaffold script ships a reference for each component below. It writes the
structural skeleton straight into the HTML file, then prints:

-   **Guidance** — what each scaffolded variant is for, further variants worth
    adding, and the interaction states to cover.
-   **A design quality checklist**: what the component is, and the design best
    practices for it.

The skeleton gives you the correct semantic HTML element for the root, the ARIA
roles and properties the pattern needs, and the required data attributes —
`data-component-id`, `data-component-type`, `data-component-variant`, and
`data-design-text-token`.

Skeletons carry no styles. They are structural blueprints only. Apply the design
system's Tailwind tokens and visual language to style each component.

Pass any name you like to `--component`. A name that is not on the list below
still produces a page and a generic skeleton, but no guidance or checklist — you
design that structure yourself.

### Available References

-   Actions: `button`, `chip`, `dropdown-menu`
-   Forms: `input-field`, `select`, `checkbox`, `radio`, `toggle`, `slider`,
    `stepper`, `date-picker`, `searchbar`
-   Containment: `card`, `accordion`, `modal`, `drawer`, `table`, `list`
-   Navigation: `tabs`, `breadcrumb`, `carousel`
-   Feedback: `alert`, `banner`, `toast`, `tooltip`, `badge`, `loading`,
    `skeleton`
-   Content: `typography`, `icon`, `avatar`

## Rendering Rules

1.  **Use ONLY named design token classes** from tailwind.config.js. Do NOT use
    generic Tailwind classes like `bg-blue-500` or `text-gray-700`. Use
    `bg-primary`, `text-on-surface`, `rounded-lg`, `text-label-lg`, etc.

2.  **Keep the page minimal.** Keep everything outside of the components as
    simple as possible, and focus on producing high-quality components. The
    Component Kit shows structure, not content.

3.  **Show states inline.** Place default and hover/disabled/active variants
    side-by-side in the same flex row so they can be compared visually. Mark
    state variants with a small label above or below:

    ```html
    <div class="flex flex-col items-center gap-1">
      <span class="text-label-sm text-outline">Disabled</span>
      <!-- COMPONENT: button-primary-disabled -->
      <button class="..." disabled>Disabled</button>
    </div>
    ```

4.  **Include HTML comments** on the line immediately before each component:
    `<!-- COMPONENT: kebab-case-name -->`. This allows the screen-generation
    agent to search for specific components by name.

5.  **Include interaction transitions.** All interactive components should have
    reflect accurate hover, focus, and active states.
