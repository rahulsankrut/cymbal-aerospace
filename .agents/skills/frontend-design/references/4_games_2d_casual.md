# 2D & Casual Games Design Guidelines

This reference covers 2D web games, competitive card games, board games, chess
bots, word search & puzzle games, and arcade/defense mechanics.

--------------------------------------------------------------------------------

## 1. Scope & Taxonomy Coverage

-   **Competitive Card Games**: Trick-taking, shedding, and deck-builder games
    with trump mechanics and suit-matching rules.
-   **Board Games & AI Bots**: Standard chessboard with algebraic notation,
    legal move calculations, material evaluators, and checkmate/stalemate rules.
-   **Word Search & Puzzles for Seniors**: Large-type accessibility, multi-tier
    hint systems (letter reveal, orientation, column hint), high-contrast
    readability.
-   **2D Action & Defense Games**: Trench defenders, top-down shooters, resource
    loops (ammo, money, iron upgrades), sector progression.
-   **Kingdom / Decision Simulator**: Ruler choice engine with balancing
    resource meters (Gold, Food, Population, Happiness).

--------------------------------------------------------------------------------

## 2. Architectural & Visual Rules

### A. Game State Machine

Implement a clean, robust state machine to drive the user interface:

```typescript
type GameState = 'TITLE_MENU' | 'PLAYING' | 'PAUSED' | 'ROUND_SUMMARY' | 'GAME_OVER';
```

-   **Title Menu**: Clear game title, instructions / rules breakdown, difficulty
    or deck setup, and `"Start Game"` button.
-   **Active Play View**: Dedicated game canvas or card table layout with
    immediate response to user input (clicks, drags, keyboard shortcuts).
-   **End State / Victory Modal**: Final scores, breakdown of defeated
    cards/waves, and a single-line `"Play Again"` restart button that resets all
    state variables without reloading the page.

### B. HUD & Overlay Discipline

-   **Unobtrusive HUD**: Position key game meters (Score, Rounds, Resources,
    Health) in a tidy top or side header; never let status overlays cover active
    playing pieces or interaction zones.
-   **Card Game Tables**:
    -   Distinct zones: Player Hand (bottom), Opponent Hand / Bot Hand (top),
        Active Battle Zone (center), Trump & Draw Deck (side).
    -   Clear visual affordances: Highlight valid playable cards on turn; dim
        invalid cards.
    -   Suit & Rank Clarity: High-visibility suit icons (`♠`, `♥`, `♦`, `♣`) and
        bold ranks.
-   **Word Search Games (Senior Accessibility Focus)**:
    -   Large grid cells ($\ge 44\text{px}$ touch targets), high-contrast
        sans-serif letters, clear selection highlighting.
    -   4-Tier Hint System: 1 = Letter revealed, 2 = Orientation clue
        (Horizontal/Vertical/Diagonal), 3 = Column indicator, 4 = First letter
        highlight.
    -   Clear, unhurried typography; no small timers causing cognitive stress.

### C. Game Loop & Audio/Visual Feedback

-   **Sound Effects (Web Audio API / Synthesized FX)**: Use gentle audio
    feedback (using browser Web Audio API oscillator beeps/chimes) for moves,
    captures, hits, and victories.
-   **Animation & Transitions**: Smooth CSS compositor-only transforms
    (`transform`, `opacity`) for card dealing, tile flips, and attack
    animations. Keep routine moves $\le 200\text{ms}$ ($\le 300\text{ms}$ for
    complex board resets) so gameplay feels responsive and snappy.
-   **Non-Hue-Only Affordances**: Always combine turn indicators or health bars
    with explicit text states, icons, or numerical counts (e.g. `HP: 85/100 ·
    STABLE`).

--------------------------------------------------------------------------------

## 3. Typography & Color Strategies

Follow the **60-30-10 Color Budget**:

-   **60% Dominant Table / Arena Surface**: Classic felt green (`#0F5132`), deep
    mahogany (`#3E2723`), dark slate (`#1E293B`), or velvet navy (`#0A192F`).
-   **30% Structural Pieces & Cards**: Crisp white cards (`#FFFFFF`), neutral
    slate panels (`#334155`), high-contrast board squares.
-   **10% Focal Accent & State Cues**: Rich suit red (`#DC2626`), telemetry
    amber (`#F59E0B`), or turn emerald (`#10B981`).
-   **Senior Puzzle Typography**: High-contrast dark charcoal on off-white
    (`#F8FAFC`), large readable type (`Plus Jakarta Sans`, `System-UI`,
    `Outfit`, $\ge 20\text{px}$ grid letters). For thematic cards or kingdom
    games, pair with characterful display titles (`Cinzel`, `Fraunces`,
    `MedievalSharp`).

--------------------------------------------------------------------------------

## 4. `generate_image` Recipes for 2D Games

```typescript
// 1. Card Game Table Texture / Mascot
generate_image({
  Prompt: "Clean top-down view of a luxury green felt card game table surface with polished mahogany wooden trim, elegant studio lighting, minimalist casino table texture.",
  ImageName: "game_card_table_felt",
  AspectRatio: "16:9"
});

// 2. Kingdom Game Ruler / Character Portrait
generate_image({
  Prompt: "Thematic stylized portrait of a medieval king wearing a subtle gold crown and royal dark velvet mantle, clean painterly game art style, neutral dark background.",
  ImageName: "game_character_king",
  AspectRatio: "1:1"
});

// 3. 2D Soldier / Trench Defender Character
generate_image({
  Prompt: "Stylized vector game sprite of a heroic soldier in tactical gear holding a rifle, side profile, clean outline, video game concept art.",
  ImageName: "game_sprite_soldier",
  AspectRatio: "1:1"
});
```

--------------------------------------------------------------------------------

## 5. Anti-Patterns to Avoid

-   ❌ **No Missing Turn Logic**: In two-player/bot card or chess games, the bot
    must take its turn automatically with a realistic delay (500ms–1s) and
    display the resulting move clearly.
-   ❌ **No Unclickable Small Tiles**: Grid buttons in word search or board games
    must never be too small for easy mouse/touch targeting.
-   ❌ **No Dead End Game Loops**: Every game must allow immediate restart
    without leaving orphaned timers or broken audio loops.
