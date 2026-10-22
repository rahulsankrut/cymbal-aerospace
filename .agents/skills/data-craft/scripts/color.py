"""house.color — colorblind-safe palettes and semantic color helpers.

All palettes are chosen for colorblind safety (deutan/protan/tritan) and print
legibility. Hex values are lowercase, 6-digit.
"""

from __future__ import annotations

from typing import Any

# Prompt-shipped payload: keep concise docstrings and lazy imports.
# pylint: disable=g-doc-args,g-doc-return-or-yield,g-short-docstring-punctuation,g-bare-generic,g-import-not-at-top

# --- Categorical: Okabe-Ito (8), the reference colorblind-safe qualitative set.
# Order tuned so the first few are maximally distinct.
OKABE_ITO = [
    "#0072b2",  # blue
    "#e69f00",  # orange
    "#009e73",  # bluish green
    "#d55e00",  # vermillion
    "#cc79a7",  # reddish purple
    "#56b4e9",  # sky blue
    "#f0e442",  # yellow
    "#000000",  # black
]

# --- Paul Tol 'bright' (7) — an alternative qualitative set, softer than Okabe.
TOL_BRIGHT = [
    "#4477aa",
    "#ee6677",
    "#228833",
    "#ccbb44",
    "#66ccee",
    "#aa3377",
    "#bbbbbb",
]

# --- Neutrals for the "quiet frame" and de-emphasis.
INK = "#222222"  # titles / strong marks (~12.6:1 on white)
LABEL = "#333333"  # axis titles
TICK = "#4d4d4d"  # tick labels
SUBTLE = "#555555"  # subtitles / dek
SOURCE = "#888888"  # source / footnote line
MUTE = "#bdbdbd"  # de-emphasized ("mute") series
MUTE2 = "#999999"  # secondary de-emphasis
GRID = "#e6e6e6"  # gridlines
SPINE = "#cccccc"  # any retained spine
PANEL = "#ffffff"  # panel background

# --- Semantic (still colorblind-distinguishable by hue+lightness).
POSITIVE = "#009e73"  # green (gains)
NEGATIVE = "#d55e00"  # vermillion (losses) — avoids pure red/green clash
WARNING = "#e69f00"  # amber
REFERENCE = "#8a8a8a"  # target / benchmark lines

# --- Sequential & diverging ramp NAMES (matplotlib built-ins).
SEQUENTIAL = "viridis"  # magnitude, one-directional
SEQUENTIAL_ALT = "cividis"  # colorblind-optimized sequential
DIVERGING = "RdBu_r"  # centered data (correlation, +/- change)


def categorical(n: int, palette: list[str] | None = None) -> list[str]:
  """Return n distinct colorblind-safe colors, cycling if needed."""
  pal = palette or OKABE_ITO
  if n <= len(pal):
    return pal[:n]
  reps = (n // len(pal)) + 1
  return (pal * reps)[:n]


def stable_map(
    categories: Any, palette: list[str] | None = None
) -> dict[str, str]:
  """Deterministic category->color map (sorted keys) so a given category keeps

  the same color across every chart in a report.
  """
  cats = sorted({str(c) for c in categories})
  pal = categorical(len(cats), palette)
  return {c: pal[i] for i, c in enumerate(cats)}


def hero_mute(
    categories: Any, hero: Any, accent: str = "#0072b2", mute: str = MUTE
) -> dict[str, str]:
  """Color map that accents ONE hero category and mutes the rest to gray.

  Use only when a single series carries the story.
  """
  hero = str(hero)
  return {str(c): accent if str(c) == hero else mute for c in categories}


def value_encode(values: Any, cmap: str = SEQUENTIAL) -> list[str]:
  """Map a numeric sequence to colors via a perceptually-uniform ramp.

  Returns a list of hex strings. Use for magnitude/heat encoding.
  """
  import matplotlib as mpl
  import numpy as np

  v = np.asarray(values, dtype=float)
  lo, hi = float(np.nanmin(v)), float(np.nanmax(v))
  span = (hi - lo) or 1.0
  norm = (v - lo) / span
  m = mpl.colormaps[cmap]
  return [mpl.colors.to_hex(m(x)) for x in norm]


def highlight(
    values: Any,
    mode: str = "max",
    accent: str = NEGATIVE,
    base: str = "#9ecae1",
) -> list[str]:
  """Return per-bar colors highlighting the max or min value; rest muted-blue."""
  import numpy as np

  v = np.asarray(values, dtype=float)
  idx = int(np.argmax(v)) if mode == "max" else int(np.argmin(v))
  return [accent if i == idx else base for i in range(len(v))]
