---
title: Media, Captions, Transcripts & Audio Control (gar-web-captions-transcripts, gar-web-pause-audio)
shortname: gar-web-captions-transcripts
priority: HIGH
---

# Media: Captions, Transcripts & Audio Control

All multimedia content must be perceivable without hearing or vision and must
never play unpausable audio automatically. This file covers
[Captions & Transcripts](http://go/gar-web-captions-transcripts) and
[Pause Audio](http://go/gar-web-pause-audio).

## 1. GAR Checkpoints & Core Rules

-   **Captions, Transcripts & Audio Descriptions
    (`gar-web-captions-transcripts`):**
    -   **Synchronized Video Captions:** Every `<video>` containing speech or
        meaningful audio must include synchronized `<track kind="captions">`.
    -   **Audio-Only Transcripts:** Every audio-only clip (`<audio>`, podcast,
        voice note) must provide an adjacent link or expandable region with a
        full text transcript.
    -   **Audio Descriptions:** When video conveys essential visual information
        not spoken in the dialogue (e.g., silent charts or on-screen text),
        provide `<track kind="descriptions">` or an audio-described track.
-   **Audio Control & No Uncontrolled Autoplay (`gar-web-pause-audio`):**
    -   **No Unpausable Autoplay (>3s):** Audio must not play automatically for
        more than 3 seconds unless a keyboard-accessible Pause/Stop/Mute control
        is immediately reachable at the top of the page.
    -   **Accessible Player Controls:** Native `controls` (or custom player
        buttons with explicit `aria-label`s for Play/Pause, Mute, Volume, and
        Captions) must be operable via keyboard without trapping `Tab` focus.

## 2. Decision Matrix

Media Type                          | Required Accessibility Elements                                                                   | GAR 2027 Criterion
:---------------------------------- | :------------------------------------------------------------------------------------------------ | :-----------------
**Video with Dialogue**             | `<video controls>` + `<track kind="captions">` + `<track kind="descriptions">` + transcript link. | `gar-web-captions-transcripts`
**Audio-Only Clip / Podcast**       | `<audio controls>` + visible link/disclosure to full text transcript.                             | `gar-web-captions-transcripts`
**Silent Looping Background Video** | `muted` attribute + visible Pause/Stop `<button>` (`gar-web-motion-stoppable`).                   | `gar-web-pause-audio`, `gar-web-motion-stoppable`

## 3. Implementation Patterns

### Accessible Video Player with Captions, Descriptions & Transcript

```html
<!-- GOOD: Native controls, synchronized caption and description tracks, and transcript link -->
<figure>
  <video controls preload="metadata">
    <source src="overview.mp4" type="video/mp4">
    <track kind="captions" src="captions_en.vtt" srclang="en" label="English" default>
    <track kind="descriptions" src="descriptions_en.vtt" srclang="en" label="Audio Description">
  </video>
  <figcaption>
    <a href="/overview-transcript.html">Read video transcript (HTML)</a>
  </figcaption>
</figure>

<!-- BAD: Autoplaying video with unmuted audio and no caption tracks -->
<video src="overview.mp4" autoplay></video>
```

### Accessible Audio Player with Text Transcript

```html
<!-- GOOD: Keyboard-accessible audio controls paired with a text transcript -->
<figure>
  <audio controls src="episode-12.mp3"></audio>
  <figcaption>
    <a href="/episode-12-transcript.html">Read Episode 12 Transcript</a>
  </figcaption>
</figure>
```

## 4. Blockers (Auto-Fail)

1.  **Missing Video Captions (`video-caption`):** `<video>` elements with audio
    tracks that omit `<track kind="captions">`.
2.  **Audio Without Transcript:** `<audio>` players with no accompanying text
    transcript.
3.  **Uncontrolled Autoplay (`no-autoplay-audio`):** Media that auto-plays sound
    for `> 3 seconds` without an immediately accessible Pause/Mute control.
4.  **Player Keyboard Trap:** Media player widgets that capture `Tab` focus and
    prevent keyboard users from exiting the player.
