---
title: Media & Audio (GAR 1.4, 2.2)
shortname: gar-web-media
priority: HIGH
---

# Media: Captions, Transcripts, & Control

Audio/Video MUST be accessible without hearing or seeing.

## 1. Captions & Transcripts (MANDATORY)

-   **Captions:** All video with spoken dialogue MUST have synchronized
    captions.
-   **Transcripts:** All audio-only content (podcasts) MUST have a text
    transcript available.
-   **Audio Description:** If visual-only information is critical (e.g., a
    silent chart shown in a video), it MUST be described in the audio track or a
    separate track.

## 2. Audio Control (No Autoplay)

-   **User Control:** Audio MUST NOT play automatically for >3 seconds.
-   **Pause/Stop:** If audio plays automatically, there MUST be a mechanism to
    pause or stop it *independent* of system volume.
-   **Volume:** The user MUST be able to adjust the volume of the specific media
    element.

## 3. Implementation Patterns

### Accessible Video Player

```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="captions" src="captions_en.vtt" srclang="en" label="English">
  <track kind="descriptions" src="descriptions_en.vtt" srclang="en" label="Audio Description">
</video>
<a href="/transcript.html">Read Transcript</a>
```

### Audio Player with Transcript

```html
<figure>
  <audio controls src="podcast.mp3"></audio>
  <figcaption>
    <a href="/podcast-transcript">Download Transcript</a>
  </figcaption>
</figure>
```

## 4. Blockers (Auto-Fail)

1.  **Missing Tracks:** `<video>` elements without a `<track kind="captions">`.
2.  **Unstoppable Audio:** Background music that loops infinitely with no pause
    button.
3.  **Trap:** A video player that traps keyboard focus (user cannot Tab out).
