# Motion and Shape Reference

This reference provides detailed token values and guidelines for shapes, elevations, and motion transitions in the Workspace Design System.

## Shape Tokens

Corner shapes control surface roundedness across components:

- `--ws-sys-shape-corner-none`: `0`
- `--ws-sys-shape-corner-extra-small`: `4px`
- `--ws-sys-shape-corner-extra-small-top`: `4px 4px 0 0`
- `--ws-sys-shape-corner-small`: `8px`
- `--ws-sys-shape-corner-medium`: `12px`
- `--ws-sys-shape-corner-large`: `16px`
- `--ws-sys-shape-corner-large-top`: `16px 16px 0 0`
- `--ws-sys-shape-corner-large-end`: `0 16px 16px 0`
- `--ws-sys-shape-corner-extra-large`: `28px`
- `--ws-sys-shape-corner-extra-large-top`: `28px 28px 0 0`
- `--ws-sys-shape-corner-full`: `max(50cqw, 50cqh)` (used for buttons, badges, chips, search bars)

## Elevation Tokens

Elevation defines surface hierarchy using shadow tokens:

- `--ws-sys-elevation-level0`: `0`
- `--ws-sys-elevation-level1`: `1px`
- `--ws-sys-elevation-level2`: `3px`
- `--ws-sys-elevation-level3`: `6px`
- `--ws-sys-elevation-level4`: `8px`
- `--ws-sys-elevation-level5`: `12px`

## Motion Duration Tokens

Duration tokens control transition timing:

- Short durations: `--ws-sys-motion-duration-short1` (50ms), `--ws-sys-motion-duration-short2` (100ms), `--ws-sys-motion-duration-short3` (150ms), `--ws-sys-motion-duration-short4` (200ms)
- Medium durations: `--ws-sys-motion-duration-medium1` (250ms), `--ws-sys-motion-duration-medium2` (300ms), `--ws-sys-motion-duration-medium3` (350ms), `--ws-sys-motion-duration-medium4` (400ms)
- Long durations: `--ws-sys-motion-duration-long1` (450ms), `--ws-sys-motion-duration-long2` (500ms), `--ws-sys-motion-duration-long3` (550ms), `--ws-sys-motion-duration-long4` (600ms)
- Extra long durations: `--ws-sys-motion-duration-extra-long1` (700ms), `--ws-sys-motion-duration-extra-long2` (800ms), `--ws-sys-motion-duration-extra-long3` (900ms), `--ws-sys-motion-duration-extra-long4` (1000ms)

## Motion Easing Tokens

Easing tokens define motion curves for standard and emphasized transitions:

- Standard easing: `--ws-sys-motion-easing-standard` (`cubic-bezier(0.2, 0.0, 0.0, 1.0)`)
- Standard accelerate: `--ws-sys-motion-easing-standard-accelerate` (`cubic-bezier(0.3, 0.0, 1.0, 1.0)`)
- Standard decelerate: `--ws-sys-motion-easing-standard-decelerate` (`cubic-bezier(0.0, 0.0, 0.0, 1.0)`)
- Emphasized easing: `--ws-sys-motion-emphasized`
- Emphasized accelerate: `--ws-sys-motion-easing-emphasized-accelerate` (`cubic-bezier(0.3, 0.0, 0.8, 0.15)`)
- Emphasized decelerate: `--ws-sys-motion-easing-emphasized-decelerate` (`cubic-bezier(0.05, 0.7, 0.1, 1.0)`)
- Linear easing: `--ws-sys-motion-easing-linear` (`cubic-bezier(0.0, 0.0, 1.0, 1.0)`)
