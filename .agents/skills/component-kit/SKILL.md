---
name: component-kit
description: >-
  Builds and uses the Component Kit of a design system: self-contained HTML
  sticker sheets, one per component kind, that screens copy verbatim. Use after
  `design-system` has produced `DESIGN.md` and `tailwind.config.js`, and before
  generating screens with `hifi-mockup-kit`.
---

# Component Kit

The Component Kit makes a design system concrete for day-to-day design work. It
is a set of **self-contained HTML files**, one for each kind of component, in
`<workspace-root>/components/` (e.g. `components/button.html`,
`components/card.html`, `components/input-field.html`). `DESIGN.md` lists them
in its `## Components` section.

Requires an existing `DESIGN.md` and `tailwind.config.js` from the
`design-system` skill.

--------------------------------------------------------------------------------

## Using the Component Kit

Read the `## Components` section of `DESIGN.md` for every component file and the
marker names inside it. Note the state variants each component provides (empty,
loading, error, disabled): screens compose their states from these, so confirm
the ones you need exist before composing a screen.

When you generate a screen, for each component you need:

1.  **Read** the relevant component HTML file from the workspace.
2.  **Find** the component by searching for its `<!-- COMPONENT: name -->`
    comment.
3.  **Copy** the entire element (the HTML tag and all its classes) into your
    screen.
4.  **Change only the content** and layout placement (e.g., which grid cell it
    sits in) by default. Do NOT arbitrarily modify the component's classes,
    structure, or state behavior — except when the user's prompt explicitly
    requires or forbids specific sub-elements, states, or attributes, in which
    case explicit user prompt constraints take precedence.
5.  If you need a component that doesn't exist in the Component Kit, adhere to
    the established design language in `DESIGN.md` and existing component files,
    and reuse parts of the components as much as possible.

--------------------------------------------------------------------------------

## Building the Component Kit

Work through these steps in order.

### Step 1: Build the components

Follow `references/create-component-kit.md` in this skill's directory.

### Step 2: Append the Components section to DESIGN.md

Open every file you wrote in `<workspace-root>/components/` and read the
`<!-- COMPONENT: name -->` markers out of it. Copy the names verbatim — do not
describe the file from memory, and do not list a file you did not write.

Write one bullet per file: the plural component name, an `@`-reference to the
file, then every marker name in that file, in the order they appear.

```markdown
## Components

Component implementations live as individual HTML sticker sheet files in
`components/`. Each file contains the canonical, styled HTML components with
`<!-- COMPONENT: name -->` comment markers. Read each file before use.

- **Buttons** → `@components/button.html`: `button-primary`,
  `button-secondary`, `button-tertiary`, `button-icon`
- **Cards** → `@components/card.html`: `card-elevated`, `card-outlined`
```

This keeps DESIGN.md the single source of truth for what components exist, while
the `.html` files stay the canonical implementations. It also gives the
screen-generation agent the exact marker names to search for, so it does not
have to open every file to find them.

### Step 3: Visualize the design system

After producing all Component Kit HTML files and updating the Components section
in `DESIGN.md`, fork a subagent to visualize the design system.

Call `invoke_subagent` with a single entry in the `Subagents` array:

-   **TypeName**: `self`
-   **Role**: `Design System Visualizer`
-   **Prompt**: `"Follow the visualize-design-system skill
    (/home/stitch_design/skills/experiment/hiro/visualize-design-system/SKILL.md).
    DESIGN.md: /workspace/DESIGN.md. Components: /workspace/components/.
    Generate the design system visualization HTML artifact in your workspace and
    message the parent agent the absolute path to the artifact."`

Fire-and-forget. Proceed with the next step without waiting for the subagent.
