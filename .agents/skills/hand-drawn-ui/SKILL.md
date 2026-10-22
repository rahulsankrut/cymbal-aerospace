---
name: hand-drawn-ui
description: >-
  Generates interactive prototypes that look hand-drawn, either from scratch or from an existing screenshot. Creates full page layouts, A2UI components, and agentic flows. Use for high-level concepting, storyboarding, and low-fidelity prototyping to focus on core ideas instead of design details. Don't use for pixel-perfect, production-ready code.
metadata:
  icon: ✏️
---

# Hand-Drawn Prototypes

See this deck for further details:
[Hand-drawn UI in Jetski](https://docs.google.com/presentation/d/1JVxkRxQPctYkGLGbO9SzNfR6gylXMQPDPpMLP5--oJk/edit?slide=id.g8c3962e100_1_116&pli=1)
screenshot.

## Direct Query & First-Time Nudge

-   **Visual Library:**
    [go/hand-drawn-skill-components](http://go/hand-drawn-skill-components).
-   **First-Time Nudge:** On the very first use of the skill in a brand-new
    session, you should append a tip letting them know about the visual
    component library and the skill instructions. You MUST append this tip
    specifically to the **confirmation message** you send to the user *after*
    effectively generating and creating their first page or component. You MUST
    format this tip using a standard GitHub markdown alert block EXACTLY like
    this: > [!TIP] > You can see the full visual library of hand-drawn
    components at go/hand-drawn-skill-components, and read the full skill
    instructions at go/hand-drawn-skill-instructions.

## Execution Steps

Before generating any code, you MUST process these exact execution steps:

1.  **Read Component Library (MANDATORY)**: Immediately use the `read_file` tool
    to read
    `/google/src/files/head/depot/google3/learning/gemini/agents/skills/ui_design/hand_drawn_ui/references/components.md`.
    Do this before answering the user or modifying any code.
2.  **Clarify Intent (MANDATORY)**: You MUST use the `ask_question` tool to
    gather setup parameters. **⚠️ CRITICAL QUESTIONING RULES:**
    -   **NEVER USE TEXT CHAT:** You are STRICTLY FORBIDDEN from typing setup
        questions as markdown text in the chat. You MUST invoke the
        `ask_question` tool so the user sees an interactive UI modal.
    -   **Literal Strings:** YOU ARE STRICTLY FORBIDDEN FROM PARAPHRASING. When
        using `ask_question`, you MUST pass the exact strings below for the
        question titles and options.
    -   **Strictly Sequential Modals:** You must ask these questions one at a
        time using the `ask_question` tool. Ask Step 1, STOP and WAIT for the
        user to submit the UI modal, and ONLY THEN ask Step 2 via a second
        `ask_question` tool call. Do not bundle them.

### Step 1: Mode Selection Popup (REQUIRED FOR CREATION)

> **EXCEPTION (UPDATE MODE):** If updating an existing file, SKIP Step 1 and 2.
> Ask what to update if unspecified. Locate the file (use code_search or hg
> status, NEVER recursive find/grep), follow guidelines, and edit it.

If the user is creating something new, you must ALWAYS trigger the
`ask_question` tool with this exact first question, unconditionally, even if the
user explicitly asks to create a "page" or "component". Do not assume their
intent and DO NOT improvise the options — force them to select from these three
exactly!

**You MUST use these EXACT arguments for the tool (DO NOT add "(Recommended)"
prefixes, DO NOT paraphrase, DO NOT change a single word):**

-   `question`: "What type of hand-drawn experience would you like to create?"
-   `options`: [ "Full page (standalone page with app bar and left nav)", "Page
    body only (no app bar or left nav, drop into your existing app shell)",
    "A2UI components (inline chat or canvas components)" ]

### Step 2: Mode-Specific Follow-Up Popup

After they select a mode, trigger `ask_question` again with the relevant
follow-up. Do NOT invent your own questions or options like "Dialog" or
"Callout"!

#### 🅰️ If Option 3 (A2UI components):

**You MUST use these EXACT arguments for the tool (DO NOT paraphrase or add
prefixes):**

-   `question`: "Should the initial component appear inline within the chat, or
    should it immediately pop open inside the canvas?"
-   `options`: ["Inline", "Canvas"]

#### 🅱️ If Option 1 (Full Page) or Option 2 (Page Body Only):

**You MUST use these EXACT arguments for the tool (DO NOT paraphrase or add
prefixes):**

-   `question`: "What layout width would you like for the page?"
-   `options`: ["Wide 1200px max width", "Narrow 840px max width"]

#### Final Topic (Pure Plain Text ONLY)

If the creative brief is still unclear after the modals finish, you may ask:
`"What is the main topic or purpose of the page?"`. **⚠️ CRITICAL:** You MUST
ask this final question using pure, normal conversational chat text! DO NOT use
the `ask_question` tool pop-up for this topic question! DO NOT invent
multiple-choice layout topics!

**🛑 SEQUENCING STOP:** If you need to ask this Final Topic question, you MUST
stop and wait for the user to answer it BEFORE you invoke the Project
Environment Check below. Do NOT trigger the Environment Check modal until the
Topic is fully resolved.

#### Project Environment Check (Conditional — ONLY if no React project is detected)

Check if your current working directory — OR any immediate subdirectories —
already contains an existing React/web project (`package.json` and `src/`). **To
do this safely without freezing the workspace, you MUST run:** `ls package.json
2>/dev/null || hg status -m -a -u | grep package.json || true`

-   **If the command outputs ANY package.json paths:** A React project IS
    detected! You are STRICTLY FORBIDDEN from asking the "Where would you like
    to build this prototype" question. Skip it entirely and proceed directly to
    Step 3! Do NOT modify their `vite.config.ts`, `index.html`, or `App.tsx`
    router (UNLESS you personally scaffolded this project earlier in the current
    chat session, in which case you MUST automatically add the new route to
    `App.tsx`).
-   **If NO React project is detected:** You MUST invoke the `ask_question` tool
    with these **EXACT** arguments (DO NOT paraphrase, DO NOT invent options,
    and DO NOT ask in text chat):
    -   `question`: "Where would you like to build this prototype?"
    -   `options`:
        1.  "Create a new project for me"
        2.  "Add to an existing project"
-   **If Option 2 ("Add to an existing project") is selected:**
    -   If the user did not already type the folder name or path in the "Other"
        write-in box, ask in pure plain chat text (do NOT use `ask_question`)
        with this **EXACT** phrasing (DO NOT paraphrase or invent questions):
        `"What is the name of your project folder (or paste its path here if you
        have it)?"`
    -   If they provide a folder name rather than a full path, automatically
        locate that folder in common directories (`~`, `~/Documents`,
        `~/Desktop`, `~/projects`) and treat it as an existing project.
-   **If Option 1 ("Create a new project for me") is selected:**
    -   Do NOT ask any follow-up question. Automatically name and scaffold a new
        Vite + React + TypeScript project folder based on the topic (e.g.,
        `./<topic>-prototype`). **CRITICAL**: You MUST use `npx --yes
        create-vite@latest <folder-name> --template react-ts --
        --no-interactive` to ensure the installation does not get permanently
        stuck waiting for interactive terminal prompts (like choosing a linter)!
        Scaffold it with:
        1.  **Cloudtop & Local Vite Config (`vite.config.ts`):** Configure
            `server: { host: '::', allowedHosts: true, port: 3000 }` so the
            preview URL works on both local machines and Google Cloudtop /
            ÜberProxy without 502 errors. (⚠️ **CRITICAL:** Do NOT change this
            to `0.0.0.0` or `true` when troubleshooting; UberProxy strictly
            requires IPv6 `::` bindings).
        2.  **Fonts, Icons & Tailwind (`index.html`):** Include Google Fonts
            `<link>` tags for `Architects Daughter` and `Material Symbols
            Outlined`, plus `<script
            src="https://cdn.tailwindcss.com"></script>` inside `<head>`.
        3.  **Reset Vite CSS (`src/App.css` & `src/index.css`):** You MUST
            completely empty (but DO NOT delete) `src/App.css` and
            `src/index.css` because Vite's default styles inject a global
            `text-align: center;` that breaks the layout! Keeping the files
            empty prevents Vite from crashing when `main.tsx` imports them.

        4.  **Automatic Route in `src/App.tsx`:** Set up a simple
            `window.location.pathname` router in `src/App.tsx` so every page or
            A2UI chat generated in this starter project automatically gets its
            own route path (e.g., `/manager-dashboard` or `/hand-drawn-chat`,
            with `/` also rendering the first page).
        5.  **Start Dev Server:** Automatically start the Vite dev server in the
            background so the user can view their page at the plain-text route
            URL immediately. **CRITICAL:** Before starting, check if a Vite
            server is already running (see Dev Server Port Reuse guardrail). If
            you do need to start it, you MUST set the `IsDaemon: true` parameter
            on the `run_command` tool when starting the server, otherwise it
            will permanently freeze the user's chat queue!

--------------------------------------------------------------------------------

### Step 3: Inject Dependencies (MANDATORY FOR ALL MODES)

**CRITICAL:** The hand-drawn aesthetic relies entirely on custom SVG filters and
a global CSS stylesheet. If this is the first time you are using this skill in
the user's project, you MUST use `read_file` to read the templates for
`/google/src/files/head/depot/google3/learning/gemini/agents/skills/ui_design/hand_drawn_ui/resources/hand-drawn.css`
and
`/google/src/files/head/depot/google3/learning/gemini/agents/skills/ui_design/hand_drawn_ui/resources/IconDefs.tsx`,
and then use `write_file` to write them into their project's source tree (e.g.,
inside `/src/styles` and `/src/components`).

Once scaffolded, you MUST ensure that any generated page correctly imports both
of these files, and explicitly renders `<IconDefs />` at the root of the layout.
Without `<IconDefs />`, none of the sketchy borders will successfully render!

### Step 4: Post-Generation CSS Sync (MANDATORY)

Because background file generation can sometimes silently fail to trigger the
user's Vite/Tailwind dev server to recompile the CSS, you MUST proactively wake
it up. **After you generate or edit any `.tsx` files, you MUST invoke the
`run_command` tool to run `touch <the-file-you-just-edited.tsx>` and `touch
package.json` (or similar root config) in the user's repository.** (⚠️ CRITICAL:
Run ONLY the `touch` commands here. Do NOT chain `&& npm run dev` onto this
command, as the server is already running independently). This forces the local
dev server to scan the new layout classes so the padding and gaps do not appear
squished.

## Aesthetic & Color Guidelines

⚠️ **CRITICAL COLOR RULES**:

1.  **Lively UI & Dashboards:** Emulate a lively whiteboard by using semantic
    colored Badges for statuses so the page isn't just black/white/grey.
    **Metrics/KPIs:** You MAY also use the strictly defined GLOBAL COLOR PALETTE
    pastel backgrounds (`bg-[#DDE7FF]`, `bg-[#E6F4EA]`, etc.) on high-level
    Statistical Cards or KPI dashboard blocks to group data and make it visually
    distinct. (EXCEPTION: Image placeholders must ALWAYS remain structural grey
    wireframes and should NEVER be semantically colored).
2.  **NO THEMATIC HALLUCINATIONS:** LLMs constantly make the mistake of painting
    UI components to match the topic (e.g. making buttons pink for a flower app,
    brown for coffee). THIS IS STRICTLY FORBIDDEN. You are a UI engineer
    building a sterile wireframe. You MUST ONLY use the exact Tailwind color
    combinations explicitly provided in `components.md` for standard UI elements
    (Buttons, Badges, Alerts, Image Placeholders). A button is ALWAYS standard
    Light Blue or Outlined. An Image Placeholder is ALWAYS grey (`bg-gray-100
    border-gray-300`). NEVER invent custom colors to match the app's topic!
    -   **Buttons:** Buttons MUST ONLY be the standard Light Blue (`bg-[#DDE7FF]
        text-[#002D62]`), Outlined (`bg-white text-[#202124]`), or plain Text.
        No other button colors or "lively" themes are permitted.
    -   **List Items / Cards:** Do NOT randomly color the background of list
        items or cards (e.g., making one list item blue while others are white)
        to simulate an "active" state unless the user specifically asked you to
        show a selected item. All list rows should be uniform (e.g. `bg-white`
        or `bg-gray-50`) by default.
3.  **Valid Iconography ONLY:** You MUST exclusively use Material Symbols for
    icons (`<span className="material-symbols-outlined">...</span>`). **NEVER
    use Unicode emojis (like 📚 or 🍕) in the UI.** When using Material Symbols,
    you MUST ONLY use standard, real ligature names (e.g. `home`, `search`,
    `local_pizza`, `info`, `pets`). DO NOT hallucinate custom icon names (like
    `earlybirds` or `pizza_slice_icon`). If you invent an icon name that doesn't
    exist, the browser will catastrophically break the layout by rendering it as
    massive text!

## Scaffolding Modes

### Mode 1: Full page (standalone page with app bar and left nav)

Generic standalone boilerplate. ⚠️ CRITICAL RULES FOR APP BAR & LEFT NAV:

1.  **STRICTLY LOCKED STRUCTURE & ITEM COUNT:** You are FORBIDDEN from altering
    any HTML, CSS classes, inline styles, circles/icons, or layout structure in
    the App Bar block (`<div className="pr-8 bg-[#F8F9FA] ...">`) or the `Left
    Nav Rail` code block. You MUST keep the exact array count of 6 top-level nav
    items (`Home` + 5 items, each with 3 subnav items).
2.  **PERMITTED COPY CUSTOMIZATION (WITH STRICT CHARACTER LIMITS):** You MAY
    replace the placeholder text strings (`"Product name"`, `'Nav item'`, and
    `'Subnav item'`) to match the page context, ONLY if you strictly obey these
    length limits so the text never overflows:
    -   **App Bar Title (`"Product name"`)**: Replace with a concise **1–3
        word** application name (**max 20 characters**, e.g., `"Fleet
        Manager"`).
    -   **Left Nav Rail (`'Nav item'`)**: Keep the first item as `'Home'`. You
        may replace the other 5 `'Nav item'` labels with **single-word** labels
        of **max 9 characters** (e.g., `'Inventory'`, `'Security'`, `'Devices'`,
        `'Reports'`, `'Settings'`) so they fit inside the narrow `80px` rail
        without overflowing.
    -   **Subnav Drawer (`'Subnav item'`)**: You may replace each `'Subnav
        item'` string with a concise **1–3 word** label (**max 22 characters**).
3.  If you modify any HTML/CSS boilerplate code before the main content area,
    you will catastrophically break the layout. Copy the exact reference
    scaffolding provided below, including the top-right "Component Library" link
    button mapping to `http://go/hand-drawn-skill-components`.

Implement the chosen width using `mx-auto max-w-[840px]` or `max-w-[1200px]` on
the main content wrapper.

### MANDATORY EXACT BOILERPLATE FOR MODE 1 (DO NOT MODIFY STRUCTURE)

Use this exact skeleton structure when generating a Mode 1 (Full Page)
component. It integrates a generic Hand-Drawn App Bar and Left Nav Rail directly
into the file without relying on external UI components (meaning it works out of
the box in any project):

```tsx
import { useState, useRef } from 'react';
import './hand-drawn.css'; // Make sure this path is correct for the user's project
import { IconDefs } from './IconDefs'; // Ensure IconDefs is generated or available

export function MyHandDrawnPage() {
  const [activeNav, setActiveNav] = useState<string>('home');
  const [hoveredNav, setHoveredNav] = useState<string | null>(null);
  const [activeSubnav, setActiveSubnav] = useState<string | null>(null);
  const hoverTimeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  // ⚠️ CRITICAL: DO NOT CHANGE THE NUMBER OF ITEMS OR STRUCTURE OF THIS ARRAY.
  // You may ONLY customize the 'Nav item' (1 word, max 9 chars) and 'Subnav item' (1-3 words, max 22 chars) text strings.
  const navItems: { label: string; id: string; subnav?: string[]; isDivider?: boolean }[] = [
    { label: 'Home', id: 'home' },
    { label: 'Nav item', id: 'nav-1', subnav: ['Subnav item', 'Subnav item', 'Subnav item'] },
    { label: 'Nav item', id: 'nav-2', subnav: ['Subnav item', 'Subnav item', 'Subnav item'] },
    { label: 'Nav item', id: 'nav-3', subnav: ['Subnav item', 'Subnav item', 'Subnav item'] },
    { label: 'Nav item', id: 'nav-4', subnav: ['Subnav item', 'Subnav item', 'Subnav item'] },
    { label: 'Nav item', id: 'nav-5', subnav: ['Subnav item', 'Subnav item', 'Subnav item'] }
  ];

  const handleMouseEnter = (id: string) => {
    if (hoverTimeoutRef.current) clearTimeout(hoverTimeoutRef.current);
    setHoveredNav(id);
  };
  const handleMouseLeave = () => {
    hoverTimeoutRef.current = setTimeout(() => setHoveredNav(null), 150);
  };

  return (
    <div className="absolute inset-0 flex flex-col w-full bg-[#F8F9FA]" style={{ fontFamily: "'Architects Daughter', cursive, sans-serif" }}>
      <IconDefs />

      {/* ⚠️ CRITICAL AGENT INSTRUCTION: DO NOT MODIFY THE HTML OR CSS OF THIS APP BAR! Only the "Product name" text string (max 20 chars) may be customized. */}
      {/* Generic App Bar (Full Width) */}
      <div className="pr-8 bg-[#F8F9FA] flex items-center justify-between w-full h-[64px] shrink-0 z-50">
        <div className="flex items-center">
          <div className="flex justify-center shrink-0 items-center" style={{ width: '80px' }}>
            <div className="w-[28px] h-[28px] rounded-full bg-gradient-to-br from-purple-200 to-blue-200"></div>
          </div>
          {/* ⚠️ CRITICAL: Keep concise (1-3 words, max 20 chars) to match app context. */}
          <span className="text-[22px] -ml-1">Product name</span>
        </div>
        <div className="flex items-center gap-[18px]">
          <div className="w-[24px] h-[24px] rounded-full bg-gray-300"></div>
          <div className="w-[24px] h-[24px] rounded-full bg-gray-300"></div>
          <div className="w-[24px] h-[24px] rounded-full bg-gray-300"></div>
          <div className="w-[24px] h-[24px] rounded-full bg-gray-300"></div>
          <a href="http://go/hand-drawn-skill-components" target="_blank" rel="noreferrer" title="Component Library" className="w-8 h-8 rounded-full border border-gray-400 border-dashed bg-gray-200 overflow-hidden cursor-pointer flex items-center justify-center text-gray-500 shrink-0 ml-1">
            <span className="material-symbols-outlined text-[20px]" style={{ fontVariationSettings: "'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24" }}>person</span>
          </a>
        </div>
      </div>

      <div className="flex flex-1 min-h-0 relative">
        {/* ⚠️ CRITICAL AGENT INSTRUCTION: DO NOT MODIFY THE HTML OR CSS OF THIS LEFT NAV RAIL! */}
        {/* Generic Left Nav Rail mapped exactly to HandDrawnNavRail aesthetic */}
        <div className="relative z-50 shrink-0">
          <div className="h-full flex flex-col items-center py-4 px-2 bg-[#F8F9FA] " style={{ width: '80px' }}>
            <div className="flex flex-col items-center space-y-4 w-full pt-[2px]">
              {navItems.map((item) => item.isDivider ? (
                <div key={item.id} className="w-8 h-[1px] bg-black/20 my-2" />
              ) : (
                <div
                  key={item.id}
                  className="relative flex flex-col items-center w-full"
                  onMouseEnter={() => handleMouseEnter(item.id)}
                  onMouseLeave={handleMouseLeave}
                >
                  <div
                    onClick={() => setActiveNav(item.id)}
                    className={`flex flex-col items-center cursor-pointer p-1 rounded w-full px-2 ${activeNav === item.id ? 'bg-[#f1f3f4] border border-[#202124]/30 rounded-xl' : 'hover:bg-gray-200/60'}`}
                  >
                    <div className={`w-4 h-4 rounded-full ${activeNav === item.id ? 'bg-[#1a73e8]' : 'bg-[#202124]/40'} mb-1`}></div>
                    <span className="text-[12px] text-center whitespace-nowrap">{item.label}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Full Height Subnav Drawer */}
          {hoveredNav && navItems.find(i => i.id === hoveredNav)?.subnav && (
            <div
              className="absolute top-2 h-[calc(100%-8px)] w-[260px] bg-[#F8F9FA] shadow-[4px_0_16px_rgba(0,0,0,0.08)] z-[40] flex flex-col pt-4"
              style={{ left: '80px', clipPath: "polygon(0 0, 200% 0, 200% 100%, 0 100%)" }}
              onMouseEnter={() => handleMouseEnter(hoveredNav)}
              onMouseLeave={handleMouseLeave}
            >
              <div className="px-3 space-y-2">
                {navItems.find(i => i.id === hoveredNav)!.subnav!.map((subItem, idx) => {
                  const itemKey = `${hoveredNav}-${idx}`;
                  return (
                    <div
                      key={itemKey}
                      onClick={() => setActiveSubnav(itemKey)}
                      className={`px-4 py-4 rounded-[24px] cursor-pointer transition-colors ${activeSubnav === itemKey ? 'bg-[#C2E7FF] border border-[#0b57d0]' : 'border border-transparent hover:bg-black/5'} flex items-center`}
                    >
                      <span className="text-[14px] leading-[20px] text-[#1f1f1f]">{subItem}</span>
                    </div>
                  );
                })}
              </div>
            </div>
          )}
        </div>

        {/* Main Scrolling Content Area */}
        <div className="flex-1 overflow-y-auto pt-2">
          <div className="mx-auto w-full max-w-[1200px] /* Replace with max-w-[840px] if Narrow */ px-10 pt-6 pb-8 min-h-full">
            <h1 className="text-[30px]  mb-4">New Hand-Drawn Page</h1>
            {/* Generate user-requested sketchy content here! */}
          </div>
        </div>
      </div>
    </div>
  );
}
```

### Mode 2: Page body only

Direct HTML/CSS component injection without `AppLayout.tsx` or GM3 slot
assumptions. You use their existing page body container and directly add the
requested components into it. Apply the chosen max-width restriction.

-   **CRITICAL SCROLLBAR DELEGATION:** For "Page body only" pages, to ensure the
    scrollbar mounts flush to the far right edge of the screen natively, you
    MUST NOT place `overflow-y-auto` inside your component! The parent wrapper
    of their application already manages the native page scroll. Injecting
    `overflow-y-auto` locally creates a nested, floating scrollbar constraint.
    Use EXACTLY this structure without bounding scroll constraints:

```tsx
return (
  <div className="w-full min-h-screen bg-gray-50 z-[1]" style={{ fontFamily: "'Architects Daughter', cursive, sans-serif" }}>
    <div className="w-full mx-auto max-w-[1200px] /* Replace with max-w-[840px] if Narrow */ flex flex-col p-6 px-10 pt-4 min-h-0">
       <IconDefs />
       {/* Generate user-requested sketchy content here! */}
    </div>
  </div>
);
```

DO NOT place `overflow-y-auto` on the inner `max-w` container or anywhere deeper
in the tree for Mode 2.

### Mode 3: A2UI components

Build the widget based on the user's topic and Inline/Canvas preference.
**CRITICAL GLOBAL SCENARIO REQUIREMENT:** Because external users do not have a
chat UI to host these widgets, the very first time you generate an A2UI
component in their project, you MUST *simultaneously* scaffold
`HandDrawnChat.tsx` directly into the user's project by using the `read_file`
tool to read the template for
`/google/src/files/head/depot/google3/learning/gemini/agents/skills/ui_design/hand_drawn_ui/resources/HandDrawnChat.tsx`
and then using `write_file` to write it directly into their `/src` components or
pages folder. Ensure imported dependencies are updated for their project.

**SAFE USER EXPERIENCE RULE:** Do NOT automatically wire the new chat interface
into their app's navigation or routing. Every codebase is different, and
guessing their router will cause destructive breakages. Simply scaffold the
`.tsx` file into their `/components` or `/pages` folder and wait for them to ask
for help!

**A2UI Implementation Differences:**

> ⚠️ **CRITICAL CHAT INITIALIZATION RULE**: `messages` inside
> `HandDrawnChat.tsx` MUST initialize as an empty array
> (`useState<Message[]>([])`). Do NOT hardcode or pre-populate initial user or
> assistant messages in the state, and NEVER add an `initialPrompt` prop or a
> `useEffect` hook that automatically calls `handleSend` on mount! The chat
> stream MUST start completely empty on page load. The generated component MUST
> ONLY be injected inside the `handleSend` / `setTimeout` response matcher
> block, so that the component ONLY displays when the user manually types the
> trigger prompt into the prompt bar.

-   **CRITICAL FILE INTEGRITY RULE:** When injecting your mocked behaviors into
    `HandDrawnChat.tsx`, you MUST NEVER delete, alter, or omit the Top Header
    layout block (`<div className="h-[60px]..."><span...Hand-drawn
    chat...<button>Clear chat...`). You MUST NEVER add any "suggested prompt
    chips", suggestion buttons, or custom UI elements above, below, or inside
    the text input prompt bar. Inject your mock logic STRICTLY into the
    `setTimeout` block (and `Right-Hand Sliding Canvas Panel` container if
    applicable). Do not touch the rest of the scaffolding!
-   **Inline:** If the user selected Inline, generate a compact, stateful React
    component (or JSX element) and pass it into the `component` property of the
    mock AI message inside `HandDrawnChat.tsx` (rendered inside its
    `max-w-[420px]` wrapper). Because the inline widget lives inside a narrow
    `420px` chat column, keep the inline card compact and focused (e.g., a
    concise summary list, status card, or compact interactive form/action card)
    — NEVER cram a sprawling multi-column dashboard into the inline bubble. **DO
    NOT** include a `canvasLauncher` property on the mock AI message. The
    separate `canvasLauncher` pill is strictly forbidden for Inline components
    and must ONLY appear when the user selects a Canvas component.
-   **Canvas:** If the user selected Canvas, you MUST generate the UI as a
    completely standalone `.tsx` React component file. Then, in
    `HandDrawnChat.tsx`:
    1.  Inject a `canvasLauncher` property into the mock AI message inside
        `setMessages` (with a custom `url` and `icon`). **⚠️ CRITICAL: You MUST
        include this property on the message object, otherwise the launcher
        button will not render in the chat stream and the user won't be able to
        re-open the canvas if they dismiss it!**
    2.  Auto-trigger the panel by calling `setActiveCanvas(...)` inside the
        `setTimeout`.
    3.  Conditionally render the imported custom component inside the Right-Hand
        Sliding Canvas Panel block (e.g., `{activeCanvas.url === 'your-url' ?
        <YourNewWidget /> : null}`).
    4.  The `canvasLauncher` pill container inside `HandDrawnChat.tsx` MUST span
        full width (`w-full`); do NOT apply restrictive `max-w-[440px]` classes
        to it.
-   **Proactive Progressive Disclosure:** When building an **Inline** component,
    you MUST proactively generate interactive deep links whenever possible (e.g.
    clicking a list item, a "View Details" button, or an expansion link) by
    adding `onClick={() => window.postMessage({ type: 'OPEN_CANVAS', payload: {
    url: 'my-details', name: 'Details', icon: 'info' } }, '*')}` (or calling
    `setActiveCanvas(...)`) on the interactive JSX elements. You MUST then
    simultaneously generate a standalone React component and conditionally
    render it when `activeCanvas.url === 'my-details'` in the
    `HandDrawnChat.tsx` pane.
    *   **⚠️ CRITICAL ANTI-LAZINESS RULE:** You MUST fully flush out the
        generated Canvas React component! DO NOT generate lazy, sterile stub
        components (e.g. "More details will appear here"). This secondary canvas
        component must be just as incredibly detailed, highly-styled, and filled
        with rich mock data as the primary inline component.

**A2UI Chat Reset Tip:** When you finish generating any A2UI component,
proactively append EXACTLY this note to your final confirmation message:

`After entering your prompt, use the 'Clear chat' button in the upper right
corner of the chat to reset the chat before entering another prompt!`

## Guardrails

-   **Dev Server Port Reuse:** If you need to start a dev server or provide a
    URL to the user, you MUST first check if a Vite server is already running in
    the background (e.g., using `ps aux | grep vite` or `lsof -i -P -n | grep
    LISTEN`). If a Vite server is already running, DO NOT start a new one.
    Extract and reuse the port it is currently using for your URL. This prevents
    port incrementing (5173 -> 5174) when the user opens multiple chats in the
    same workspace.
-   **Reading Step:** Mandatory `components.md` reading step prior to UI
    generation.
-   **Un-bolded Typography Rule:** NEVER use `font-bold` or `font-semibold`
    anywhere in the app. The Architects Daughter font does not support bold
    weights natively, so it defaults to a forced thick stroke. Use sizes like
    `text-[22px]` and `text-lg` to create visual hierarchy instead of weights.
-   **A2UI Title Layout Rule:** NEVER place badges, chips, buttons, or other
    floating action elements on the same horizontal flex row as the main title
    header of an A2UI component. Floating right-aligned chips force the title
    container to narrow, causing titles to brutally text-wrap onto multiple
    lines and breaking the layout. Place badges and secondary chips strictly in
    the body, subtitle, or bottom of the component so the main title always has
    100% of the horizontal width.
-   **Button Whitespace Wraps:** Button copy must remain strictly on one line.
    Keep text extremely concise and structurally enforce this by applying the
    `whitespace-nowrap` tailwind class to buttons in constrained spaces so they
    do not break their vertical pill boundaries.
-   **ZERO Custom DOM Deviation:** DO NOT stick an `<Icon>` inside an Image
    block because you think it looks nice. DO NOT mix structural hand-drawn
    classes (like `.sketchy-box`) with `absolute` positioning, as this breaks
    the SVGs. NEVER apply native CSS borders (like `border-dotted`,
    `border-l-4`, `border-[#1a73e8]`) to fake a sketchy look. You MUST strictly
    use the `.sketchy-box` classes for all cards and inputs. Native borders
    break the aesthetic.
-   **Small Image/Icon Wrappers:** NEVER apply `.sketchy-box` or
    `.sketchy-box-flat` to small thumbnail wrappers (e.g. `w-10 h-10`). Because
    the hand-drawn mask has a static 24px border-radius, placing it on a small
    square forces it to warp into a circular stroke. STRICTLY use the standard
    "Image" wrapper from `components.md` (e.g. `border-dashed border-gray-300`)
    without ANY `.sketchy-box` classes.
-   **Dense Data Tables:** When generating Data Tables, you MUST enforce extreme
    condensation to prevent vertical bloating: use `py-1` padding for table
    rows, shrink native text to `text-sm` or `text-xs`, constrain row avatars to
    `w-[28px] h-[28px]`, and aggressively squeeze row-level buttons (`!px-2
    !py-1`) so they don't stretch the row height.
-   **Card Backgrounds & Defaults:** Always default to using the **Outlined
    Card** variant with a STRICTLY clean white background (`bg-white`). Never
    use the Elevated Card unless explicitly requested. NEVER paint entire card
    backgrounds with colored pastel tints (e.g. `bg-blue-50`, `bg-purple-50`).
    Color MUST be used sparingly and strictly reserved ONLY for: 1.
    **Badges/Chips**,
    2.  **Primary Action Buttons**, 3. **Small Icon Circles**, 4.
        **Selected/Active States**,
    3.  **Data Visualizations**, and 6. **KPI/Statistical Metric Cards**.
-   **Dynamic Page Title:** Every generated hand-drawn page (Mode 1 or 2) MUST
    include a `useEffect` hook setting `document.title = '<Page Title>';` on
    mount so the browser tab title dynamically reflects the active page name.
-   **NO TAILWIND HALLUCINATIONS:** You are strictly forbidden from chaining
    Tailwind utility classes to invent unsupported UI components (e.g. manually
    crafting blue pill buttons or green status boxes using `border
    border-blue-500 rounded-full`). If a component variant does not explicitly
    exist in `components.md`, you MUST fallback to the closest supported sketchy
    variant.
-   **NEVER INVENT CSS OR COMPONENTS:** You are strictly forbidden from writing
    custom generic HTML UI layouts or inventing fake, hardcoded CSS border
    manipulations (e.g. `border-radius: 18px 22px 20px 24px/22px 18px 24px
    20px`). You MUST strictly rely on `hand-drawn.css` classes. If you need a
    card, a button, a badge, or an input field, you MUST look up its exact
    structure in `components.md` and reconstruct it flawlessly.
-   **Inner Padding on Text Containers:** NEVER place text inside an outlined
    box, custom background container, or image placeholder without applying
    explicit padding (e.g., `p-4` or `px-4`). When padding text containers,
    generally default to left-aligning the text (`justify-start`) rather than
    centering it, as left-aligned text behaves and reads much better when it
    wraps.
-   **Transparent Page Backgrounds:** For both "Full Page" and "Page Body Only"
    layouts, DO NOT apply a white background (`bg-white`) to the root page
    container. Components must float transparently on top of the default grey
    page layout background. (Note: A2UI inline chat widgets still require white
    root cards).
-   **Large Content Grouping:** If a page contains a sprawling, data-dense block
    that spans the full width of the main content area (e.g., a Calendar Grid, a
    large Form, or a Data Table), you MUST group that entire block inside a
    full-width outlined card (using `<div className="sketchy-box-flat bg-white
    p-4 w-full">`). This visually anchors complex content into a readable unit
    instead of leaving it floating disconnected on the grey background.
-   **Realistic Copy:** You must invent and write contextual, realistic text
    paragraphs for all mockups. Do NOT use generic placeholder squiggly lines or
    lorem ipsum text.
-   **Nested List Items Styling:** When structuring list items inside an outer
    outlined card wrapper, do NOT apply border or stroke classes (like
    `.sketchy-box` or `.sketchy-list-item`) to the individual rows. Instead,
    keep the list items transparent and borderless, and explicitly separate them
    using a sketchy horizontal divider (`<div className="sketchy-line
    w-full"></div>`) between each row. Apply adequate padding to each row (e.g.,
    `className="pl-5 pr-3 py-2 bg-transparent"`).
-   **Hyper-Condensed Density:** Always scaffold layouts using extreme
    hyper-condensed vertical spacing to minimize excess whitespace. Shrink all
    container paddings (strictly use `p-3` or `p-2` instead of p-6) and squeeze
    vertical flex gaps down to `gap-2` or `gap-3`.
-   **Generative UI Iframe / Canvas rules:**
    -   DO NOT invent generic HTML UI layouts. Translate perfectly manually from
        `/google/src/files/head/depot/google3/learning/gemini/agents/skills/ui_design/hand_drawn_ui/references/components.md`
        into raw HTML equivalents.
    -   For inline widgets, actively apply `overflow: hidden;` to restrict
        scroll bars.
    -   For Canvas full-pane layouts, enforce robust layout boundaries
        (`min-w-0`), zero spurious top padding (`pt-4`), and no massive left
        columns. All top-level canvas widget content must be housed inside a
        main sketchy card container using `h-fit` (NOT `h-full`) so the card
        dynamically hugs its content and doesn't stretch to the bottom of the
        canvas.
    -   **NO HORIZONTAL SCROLLING IN CANVAS RULE:** Horizontal scrolling
        (`overflow-x-auto`, `overflow-x-scroll`, or `flex-nowrap` scroll
        containers) is **STRICTLY FORBIDDEN** inside Canvas components. In the
        narrow Canvas side-panel, chip filters, category tags, and buttons MUST
        wrap naturally onto multiple lines (`flex-wrap gap-2`). Never create
        horizontal scrollbars inside the Canvas panel.
    -   **CRITICAL A2UI HTML HEIGHT RULE**: When translating the chat simulator
        into standalone HTML for GenUI preview, YOU MUST explicitly inject a
        `<div style="height: 600px; width: 100vw; visibility: hidden;"></div>`
        structural shim just before the main layout container, and change the
        main layout container's classes to `absolute inset-0 flex...`. Do NOT
        use `min-h-screen` or `h-screen`, otherwise the chat input bar will
        disappear off the bottom of the iframe.
    -   **CRITICAL A2UI CANVAS/INLINE PREVIEW RULE**:
        -   **For Canvas Components:** When generating a Canvas layout (where
            the primary widget lives in the right-hand panel), triggering the
            prompt in `handleSend` MUST set `activeCanvas` to the component so
            the right-hand panel opens automatically when the component responds
            in chat.
        -   **For Inline Components:** When generating an Inline card layout
            (where the primary widget lives in the chat message stream),
            `activeCanvas` MUST initialize as `null` (closed). The canvas panel
            should ONLY open when the user explicitly clicks a deep-link button
            or launcher inside the inline card.
-   **Natural Assistant Persona (Mode 3):** When crafting the mocked
    \`assistantMsg.text\` for A2UI components in \`HandDrawnChat.tsx\`, the AI
    MUST speak completely naturally as if just answering the user's question,
    and MUST NEVER mention or draw attention to the UI widget itself. Do not say
    "Click any of them to see details", "I have generated a widget for you", or
    "Check out this interactive interface." Simply answer the question
    conversationally (e.g., "I found 3 great adoptable kittens near you!").

## Final Handoff & Preview

1.  **Communication & Preview Rule:** When you finish, you must clearly explain
    the output to the user.
    -   **For A2UI Components (Mode 3):** You MUST keep your output extremely
        concise. DO NOT explain how you built the code or what logic you
        injected.

        *   **If in an EXISTING project**, use this exact template:

            *"I built your new A2UI component and chat interface! I saved the
            files to
            [`<insert-relative-file-path>`](file:///<insert-absolute-file-path>).*

            *Let me know where you'd like it added to your app, or just ask me
            for a direct link! Once you can view the chat interface in your app,
            try typing '<insert-exact-trigger-prompt-here>' into the prompt bar
            to view your new component!* **[IF INLINE COMPONENT WITH CANVAS
            DEEPLINK ADD: *Click on '<insert-simulated-button-or-row-name>' in
            the component to open details in the canvas!*]**"

        *   **If adding to a starter project YOU created earlier in this
            session**, automatically update the routing and use this exact
            template:

            *"I built your new component and saved the files to
            [`<insert-relative-file-path>`](file:///<insert-absolute-file-path>)—you
            can view it live here:
            [<insert-plain-text-page-url>](insert-plain-text-page-url)
            *(Right-click or Cmd/Ctrl+click to view in a new tab)*.*

            *Once you open the link, try typing
            '<insert-exact-trigger-prompt-here>' into the prompt bar to view
            your new component!* **[IF INLINE COMPONENT WITH CANVAS DEEPLINK
            ADD: *Click on '<insert-simulated-button-or-row-name>' in the
            component to open details in the canvas!*]**"

        *   **If in a NEWLY CREATED starter project** (where routing and the dev
            server were set up automatically), use this exact template:

            *"I created a new project for you
            ([`<insert-project-folder-name>`](file:///<insert-absolute-project-path>)),
            started a background dev server, and created your A2UI chat
            interface! I saved the files to
            [`<insert-relative-file-path>`](file:///<insert-absolute-file-path>)—you
            can view the live prototype here:
            [<insert-plain-text-page-url>](insert-plain-text-page-url)
            *(Right-click or Cmd/Ctrl+click to view in a new tab)*.*

            *Once you open the link, try typing
            '<insert-exact-trigger-prompt-here>' into the prompt bar to view
            your new component!* **[IF INLINE COMPONENT WITH CANVAS DEEPLINK
            ADD: *Click on '<insert-simulated-button-or-row-name>' in the
            component to open details in the canvas!*]**"

        *   *(Note: Immediately after the Mode 3 template, ALWAYS append the
            A2UI Chat Reset Tip first, followed by a blank line and the
            first-time nudge `> [!TIP]` alert block if this is the first run in
            the session!)*
    -   **For Full Page (Mode 1) & Page Body (Mode 2) & UPDATE MODE:** You MUST
        keep your output extremely concise. DO NOT explain how you built the
        page, what layout mode you used, or enumerate the components you
        injected.

        *   **If you were explicitly asked to UPDATE or EDIT an existing page**
            (using the UPDATE MODE exception in Step 1), simply output: *"I have
            made the updates and saved the changes to
            [`<insert-relative-file-path>`](file:///<insert-absolute-file-path>)—your
            dev server should automatically refresh to show the updates!"*
        *   **If creating a new page in an EXISTING project**, simply output:
            *"I built your new page and saved the file to
            [`<insert-relative-file-path>`](file:///<insert-absolute-file-path>).
            Let me know where you'd like it added to your app, or just ask me
            for a direct link!"*
        *   **If adding a page to a starter project YOU created earlier in this
            session**, automatically update the routing and simply output: *"I
            built your new page and saved the file to
            [`<insert-relative-file-path>`](file:///<insert-absolute-file-path>)—you
            can view it live here:
            [<insert-plain-text-page-url>](insert-plain-text-page-url)
            *(Right-click or Cmd/Ctrl+click to view in a new tab)*."*
        *   **If in a NEWLY CREATED starter project** (where routing and the dev
            server were set up automatically), simply output: *"I created a new
            project for you
            ([`<insert-project-folder-name>`](file:///<insert-absolute-project-path>)),
            started a background dev server, and built your new page! I saved
            the file to
            [`<insert-relative-file-path>`](file:///<insert-absolute-file-path>)—you
            can view the live prototype here:
            [<insert-plain-text-page-url>](insert-plain-text-page-url)
            *(Right-click or Cmd/Ctrl+click to view in a new tab)*."*
        *   Always include a blank line followed by the visual library `>
            [!TIP]` alert block on the first run in a session, but DO NOT add
            any other conversational bloat.
        *   **CRITICAL ARTIFACT RULE:** You MUST NEVER generate a `.url.json`
            URL Artifact (bookmark) that links to a dev server or preview url.
            Only provide the plain-text root URL (e.g., `http://host:5173/`) in
            the chat. NEVER provide a URL with a deep path (e.g., `/chat`), as
            UberProxy has a known bug that strips port numbers off deep links.
2.  **No HTML Previews & No Code Walls:** You MUST ONLY generate raw `.tsx` code
    files. NEVER generate standalone `.html` files, never create side panel UI
    artifacts, and never use `generative_ui` or `<agent-embed>` to mock or
    preview the UI in the chat. NEVER dump raw Markdown code blocks (```tsx)
    into your chat response. You must exclusively use your file-writing tools to
    generate the output so it surfaces as clean file attachments without
    cluttering the chat. The user will compile and view the code within their
    own local web app environment.
3.  **🛑 CRITICAL TERMINATION RULE:**

    *   You MUST output the confirmation template as the **ABSOLUTE FINAL
        ACTION** of your turn. Do not output the template and then continue
        making tool calls or checking the dev server status. If you need to
        verify a task, do it *before* outputting the template.
    *   If you receive an asynchronous background notification (e.g., that the
        Vite server has started) *after* you have already output the
        confirmation template, you MUST silently acknowledge it by ending your
        turn without generating any additional conversational text.
