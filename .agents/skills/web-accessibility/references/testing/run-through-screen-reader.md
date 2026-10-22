---
title: "Final Run Through: Without Screen Visible (With Screen Reader)"
gar_id: "Web 1.16(c)"
shortname: gar-web-run-through-screen-reader
keywords: [screen reader, blind, low vision, non-visual access, keyboard navigation, ChromeVox, VoiceOver, NVDA, JAWS]
---

     | Taglist
---- | -------------------------------------------
tags | #screen-reader-focused #based-in-en-301-549

# Final Run Through: Without Screen Visible (With Screen Reader)

GAR 2026 | Formerly Web 1.16(c)

Can a user navigate and interact using only a screen reader and keyboard,
without needing to see the screen?

`Shortname`: gar-web-run-through-screen-reader

### **Potential user impact of failing**

More details on the potential user impact of failing

*   **Risk: Unusable Product** <br/>
    If your content cannot be accessed or interacted with by screen readers,
    users who rely on screen readers will be excluded from using your product.

## **Overview of Final Run Through: Without Screen Visible**

Goal: Ensure that your application is usable by people who can’t see the screen
and/or people who use screen readers.

**Ensure that your application is usable without looking at the screen, using
the following required platforms:**

1.  On ChromeOS, test using the pre-installed screen reader
    [ChromeVox](http://www.chromevox.com/).
2.  On Mac, using their pre-installed screen reader
    [VoiceOver](http://help.apple.com/voiceover/info/guide/10.8/English.lproj/index.html),
    test on Chrome.
    *   Optional: Also test on Safari.
3.  On Windows:
    *   With Chrome, using the latest versions of both
        [NVDA](http://www.nvaccess.org/) and
        [JAWS](https://docs.google.com/document/d/1wnlua0BnlFf7Mz9dRku7vXxLy11ozqzXDsNYWik_KAY/edit#).
        (You must do a full pass with both screen readers.)
    *   With Firefox, using the latest versions of
        [NVDA](http://www.nvaccess.org/) and
        [JAWS](https://docs.google.com/document/d/1wnlua0BnlFf7Mz9dRku7vXxLy11ozqzXDsNYWik_KAY/edit#).
        *   It is recommended to do a full pass with both screen readers.
            However, you may split your use cases between these two screen
            readers. You can only do this split testing if you either:
            *   Create a plan to alternate the screen reader and use case
                combinations in different releases and regression testing so
                that you aren't repeatedly testing the same use cases with the
                same screen reader, or
            *   Commit to have someone revisit the combinations used in previous
                testing and use new testing combinations in the next round.

### Good Code Examples

```html
<!-- Semantic HTML for structure -->
<nav aria-label="Main Navigation">
  <ul>
    <li><a href="/home">Home</a></li>
    <li><a href="/about">About Us</a></li>
  </ul>
</nav>
<main>
  <h1>Page Title</h1>
  <p>Some content...</p>
  <button>Click Me</button>
</main>

<!-- Proper labels for form controls -->
<label for="username">Username:</label>
<input type="text" id="username" name="username">

<button aria-label="Search all products">
  <svg role="presentation"><!-- search icon --></svg>
</button>

<!-- ARIA live region for dynamic updates -->
<div aria-live="polite" id="status-update">
  <!-- Content updated by JS -->
</div>

<!-- Accessible names for images -->
<img src="logo.png" alt="Company Logo">
<img src="decorative.png" alt=""> <!-- Decorative image -->

<!-- Keyboard accessible custom controls -->
<div role="button" tabindex="0" onclick="doSomething()" onkeydown="handleKeydown()">
  Custom Button
</div>
```

### Code Examples to Avoid

```html
<!-- Using divs for everything without roles -->
<div> <!-- Should be <nav> -->
  <div><a href="/home">Home</a></div>
</div>
<div> <!-- Should be <main> -->
  <div class="heading">Page Title</div> <!-- Should be <h1> -->
  <div onlick="doSomething()">Click Me</div> <!-- Not keyboard accessible, should be <button> -->
</div>

<!-- Missing form labels -->
<input type="text" name="email" placeholder="Email"> <!-- Placeholder is not a label -->

<!-- Unlabeled icon buttons -->
<button>
  <svg role="presentation"><!-- info icon --></svg>
  <!-- No aria-label -->
</button>

<!-- Dynamic updates not announced -->
<div id="status">
  <!-- JS updates this, but screen reader doesn't know -->
</div>

<!-- Images without alt text -->
<img src="important.jpg">

<!-- Links that look like buttons / Buttons that look like links -->
<a href="#" onclick="doAction(); return false;">Looks like Button</a>
<span class="button-like" onclick="location.href='...'">Looks like Link</span>
```

### **Testers: How to test Final Run Through: Without Screen Visible**

[The Basics Of Testing Web Content With Voiceover video](https://broadcast.corp.google.com/ui/player/6eab708a-46ed-4589-a648-0500b2b3b0c0)
(4 minutes 2 seconds)

[The Basics Of Using JAWS To Test Web Content video](https://broadcast.corp.google.com/ui/player/cc50b9e0-e202-42be-8554-3b85bf39c0d4)
(6 minutes 30 seconds)

[Testing Basic Web Content Using NVDA video](https://broadcast.corp.google.com/ui/player/df3fa140-c3db-4981-9bb3-f078b5bd9797)
(3 minutes 55 seconds)

[Testing Forms Using VoiceOver video](https://broadcast.corp.google.com/ui/player/bbc027f1-b507-471e-8b94-faf521faf003)
(2 minutes 19 seconds)

[Testing Forms Using Chromevox](https://broadcast.corp.google.com/ui/player/56994038-3315-4b9c-a3ac-70e53b14398b)
(2 minutes 25 seconds)

[Testing User Input Controls And Dynamic Content With JAWS video](https://broadcast.corp.google.com/ui/player/87146b4d-855e-49ce-b38a-6013b26c5691)
(10 minutes 58 seconds)

[Using NVDA To Test Dynamic Content video](https://broadcast.corp.google.com/ui/player/49cab406-9c7f-4d94-89c9-da90fa0f8cee)
(2 minutes 25 seconds)

[The Basics Of Using ChromeVox To Test Web Content video](https://broadcast.corp.google.com/ui/player/2429c18d-49a2-4aec-b0e0-cee2eb51c9b8)
(3 minutes 2 seconds)

*   Enable a screen reader and run through the user flow. Ensure there are no
    issues that prevent your ability to complete the user flow and that you have
    enough product-provided `context` for the user to understand and navigate
    your application.
*   We strongly recommend that you test your application without looking at the
    screen or by turning off the screen and only using a keyboard (don't use a
    mouse).
