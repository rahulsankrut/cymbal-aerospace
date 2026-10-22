---
title: Closure Templates (Soy) & Closure UI Accessibility Guidance
shortname: gar-web-framework-soy-closure
priority: MANDATORY_CRITICAL
---

# Closure Templates (Soy) & Closure Library Rules

Follow these template localization, attribute delegation, and layer-boundary
rules when authoring or fixing accessibility in **Closure Templates (`.soy`)**
and **Closure Library / Guts (`.js`, `.ts`)** components.

## 1. Target File Extensions & Scope

-   Applies to `.soy` templates and `.js` / `.ts` controllers using Closure
    Library (`goog.ui.*`), Guts (`guts.components.*`), or Material Soy templates
    (`materialMenuButton`, `materialTextButton`).

## 2. Attribute Binding & Localization (`i18n`)

-   **Mandatory `{msg}` Blocks in Soy:** Never hardcode English strings directly
    into `aria-label` or template parameters inside `.soy` files. Wrap every
    user-facing accessible string in `{msg desc="..."}...{/msg}`:

```soy
{let $filterAriaLabel kind="text"}
  {msg desc="Accessible label for the network filter dropdown button."}
    Filter network items
  {/msg}
{/let}
<button type="button" aria-label="{$filterAriaLabel}">...</button>
```

-   **Dynamic & Repeating Links (`gar-web-clear-purpose` /
    `google-link-purpose`):**
    -   **Rank 1 (Ideal — Prose Sentences, Footers & Space Permits):** Always
        replace vague stop words (`"here"`, `"click here"`, `"link"`, or bare
        `"link 2"`) inside prose sentences or footers with descriptive visible
        link text wrapped in `{msg desc="..."}` (e.g., `"download the full CSV
        archive"` or `"retention policy"`). Never leave `"here"` or `"link 2"`
        as the visible text in a prose paragraph and attach `aria-describedby`.
    -   **Rank 2 (Space-Constrained Repeating Card/Table Links):** Only when
        visual layout space is strictly constrained (such as compact cards or
        narrow table cells with `"Learn more"`), keep the concise visual link
        text and reference the card/banner message ID via `aria-describedby`:

```soy
<!-- GOOD (Rank 1 - Space Permits): Topic-prefixed visible link text -->
{for $link, $index in $links}
  {if $index > 0}
    <a href="{$link}">
      {msg desc="Secondary link for a specific billing topic."}
        {$topic} link {formatNum($index + 1)}
      {/msg}
    </a>
  {/if}
{/for}

<!-- GOOD (Rank 2 - Space Constrained): Connect concise link to topic ID via aria-describedby -->
<span id="topic-{$topicId}">{$topicTitle}</span>
{for $link, $index in $links}
  {if $index > 0}
    <a href="{$link}" aria-describedby="topic-{$topicId}">
      {msg desc="Numbered secondary link connected to topic heading."}
        link {formatNum($index + 1)}
      {/msg}
    </a>
  {/if}
{/for}
```

## 3. Component Library Gotchas & Container Traps

-   **Menu & Popup Trigger Attribute Delegation (`materialMenuButton`):**
    -   When rendering menu buttons in Soy, attach
        `materialMenuButton.buttonAttributes` (which provides `aria-haspopup`
        and `aria-expanded`) directly to the inner interactive
        `materialTextButton.buttonText` call—never to an outer `<span>` or
        `<div>` wrapper container:

```soy
// GOOD: Menu trigger attributes delegated directly to the interactive button
{call materialMenuButton.button}
  {param content kind="html"}
    {call materialTextButton.buttonText}
      {param label: $label /}
      {param attributes kind="attributes"}
        {call materialMenuButton.buttonAttributes /}
      {/param}
    {/call}
  {/param}
  {param menu kind="html"}
    {call menuTemplates.menu}
      ...
    {/call}
  {/param}
{/call}
```

-   **Custom Selectable Listboxes (`aria-allowed-attr`,
    `aria-prohibited-attr`):**

    -   When rendering selectable items with `aria-selected="..."` on custom
        `<div>` or `<li>` elements in Soy, each item must declare
        `role="option"` and keyboard focusability (`tabindex="0"` or roving
        `tabindex`), and its parent container must declare `role="listbox"` with
        a localized `aria-label` wrapped in `{msg desc="..."}` (or
        `aria-labelledby`).
    -   Never leave `aria-label` on a decorative `<svg aria-hidden="true">` when
        visible status text is already rendered beside the icon; remove the
        prohibited `aria-label` so the SVG stays cleanly hidden.

-   **Target Application Wrappers, Not Core Base Libraries:**

    -   When fixing accessibility in a product component that wraps Closure UI
        (e.g., `guts.components.ClosureDropdown` wrapping `goog.ui.Select`),
        modify the application wrapper component or its opt-in flags (such as
        `add_aria_pos_size = true` for `aria-posinset`/`aria-setsize`) rather
        than editing shared base classes in `//third_party/javascript/closure/`.

## 4. Focus & Async Lifecycle Management

-   **Closure Control & Dialog Focus Restoration:** When closing a
    `goog.ui.Dialog` or custom Closure popup, restore focus in the after-hide
    event handler (`goog.ui.PopupBase.EventType.HIDE` /
    `Dialog.EventType.AFTER_HIDE`) rather than before the overlay is hidden in
    the DOM.
