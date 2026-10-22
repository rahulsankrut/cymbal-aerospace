"""house.charts — Level-5 editorial chart recipes.

Each recipe applies the house style and returns (fig, ax) (or fig for
multi-panel). Call house.theme.apply(...) first, or pass preset=.
Recipes: slopegraph, dumbbell, lollipop, bump, waterfall, bullet, ridgeline,
sparklines.
"""

from __future__ import annotations

from typing import Any

import color as C
import matplotlib.pyplot as plt
import numpy as np
import theme as T

# Prompt-shipped payload: concise docstrings; scipy imported lazily.
# pylint: disable=g-doc-args,g-doc-return-or-yield,g-bare-generic,g-complex-comprehension,g-import-not-at-top


def _new(
    preset: str = "report", figsize: tuple[float, float] | None = None
) -> tuple[Any, Any]:
  T.apply(preset)
  fig, ax = plt.subplots(figsize=figsize)
  return fig, ax


def _fmt(v: Any, fmt: str | None) -> str:
  return fmt.format(v) if fmt else (f"{v:,.0f}")


# --- Slopegraph ---------------------------------------------------------------
def slopegraph(
    data: dict[Any, Any],
    labels: tuple[str, str] = ("Before", "After"),
    hero: Any = None,
    fmt: str | None = None,
    preset: str = "report",
    ax: Any = None,
) -> tuple[Any, Any]:
  """data: {entity: (v1, v2)}. Shows change/rank-shuffle across 2 points.

  Gray by default; `hero` (name or list) gets accent color.
  """
  fig, ax = (ax.figure, ax) if ax is not None else _new(preset)
  heroes = {hero} if isinstance(hero, str) else set(hero or [])
  for name, (v1, v2) in data.items():
    is_hero = name in heroes
    col = C.OKABE_ITO[0] if is_hero else C.MUTE
    lw = 2.4 if is_hero else 1.4
    ax.plot(
        [0, 1],
        [v1, v2],
        color=col,
        lw=lw,
        marker="o",
        markersize=5,
        zorder=3 if is_hero else 2,
    )
    ax.text(
        -0.02,
        v1,
        f"{name}  {_fmt(v1, fmt)}",
        ha="right",
        va="center",
        fontsize=T.TYPE["annotation"],
        color=C.INK if is_hero else C.SUBTLE,
        fontweight="bold" if is_hero else "normal",
    )
    ax.text(
        1.02,
        v2,
        f"{_fmt(v2, fmt)}  {name}",
        ha="left",
        va="center",
        fontsize=T.TYPE["annotation"],
        color=C.INK if is_hero else C.SUBTLE,
        fontweight="bold" if is_hero else "normal",
    )
  allvals = [v for pair in data.values() for v in pair]
  ymax, ymin = max(allvals), min(allvals)
  pad = (ymax - ymin) * 0.12 or 1.0
  ax.set_ylim(ymin - pad, ymax + pad * 2.4)
  ax.text(
      0,
      ymax + pad * 1.5,
      labels[0],
      ha="center",
      va="bottom",
      fontweight="bold",
      fontsize=T.TYPE["axis_title"],
      color=C.INK,
  )
  ax.text(
      1,
      ymax + pad * 1.5,
      labels[1],
      ha="center",
      va="bottom",
      fontweight="bold",
      fontsize=T.TYPE["axis_title"],
      color=C.INK,
  )
  ax.set_xlim(-0.35, 1.35)
  ax.set_xticks([])
  for s in ("top", "right", "left", "bottom"):
    ax.spines[s].set_visible(False)
  ax.grid(False)
  ax.set_yticks([])
  ax.tick_params(length=0)
  return fig, ax


# --- Dumbbell -----------------------------------------------------------------
def dumbbell(
    cats: Any,
    v1: Any,
    v2: Any,
    labels: tuple[str, str] = ("A", "B"),
    sort_by: str = "v2",
    colors: tuple[str, str] = (C.MUTE2, C.OKABE_ITO[0]),
    preset: str = "report",
    ax: Any = None,
) -> tuple[Any, Any]:
  """Gap between two values per category (before/after, actual/target)."""
  fig, ax = (ax.figure, ax) if ax is not None else _new(preset)
  v1 = np.asarray(v1, float)
  v2 = np.asarray(v2, float)
  cats = list(cats)
  key = v2 if sort_by == "v2" else (v2 - v1)
  order = np.argsort(key)
  cats = [cats[i] for i in order]
  v1 = v1[order]
  v2 = v2[order]
  y = np.arange(len(cats))
  ax.hlines(y, v1, v2, color=C.GRID, lw=3, zorder=1)
  ax.scatter(v1, y, s=70, color=colors[0], zorder=3)
  ax.scatter(v2, y, s=70, color=colors[1], zorder=3)
  ax.set_yticks(y)
  ax.set_yticklabels(cats)
  for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
  ax.spines["bottom"].set_color(C.SPINE)
  ax.grid(axis="x", color=C.GRID, lw=0.6)
  ax.tick_params(length=0)
  # Direct-label the two dots on the top row (editorial: no legend).
  top = len(cats) - 1
  ax.annotate(
      labels[0],
      (v1[top], top),
      xytext=(0, 11),
      textcoords="offset points",
      ha="center",
      color=colors[0],
      fontsize=T.TYPE["annotation"],
      fontweight="bold",
  )
  ax.annotate(
      labels[1],
      (v2[top], top),
      xytext=(0, 11),
      textcoords="offset points",
      ha="center",
      color=colors[1],
      fontsize=T.TYPE["annotation"],
      fontweight="bold",
  )
  ax.set_ylim(-0.6, top + 0.75)
  return fig, ax


# --- Lollipop -----------------------------------------------------------------
def lollipop(
    cats: Any,
    vals: Any,
    sort: bool = True,
    fmt: str | None = None,
    highlight_max: bool = True,
    preset: str = "report",
    ax: Any = None,
) -> tuple[Any, Any]:
  """Ranked categorical magnitude; lighter than bars. Baseline at 0."""
  fig, ax = (ax.figure, ax) if ax is not None else _new(preset)
  vals = np.asarray(vals, float)
  cats = list(cats)
  if sort:
    order = np.argsort(vals)
    cats = [cats[i] for i in order]
    vals = vals[order]
  y = np.arange(len(cats))
  cols = (
      C.highlight(vals, "max", C.OKABE_ITO[0], C.MUTE)
      if highlight_max
      else [C.OKABE_ITO[0]] * len(vals)
  )
  ax.hlines(
      y,
      0,
      vals,
      color=[C.GRID if c == C.MUTE else "#c9d7e6" for c in cols],
      lw=2.2,
      zorder=1,
  )
  ax.scatter(vals, y, s=90, color=cols, zorder=3)
  for yi, v in zip(y, vals):
    ax.text(
        v,
        yi,
        f"  {_fmt(v, fmt)}",
        va="center",
        ha="left",
        fontsize=T.TYPE["annotation"],
        color=C.INK,
    )
  ax.set_yticks(y)
  ax.set_yticklabels(cats)
  ax.set_xlim(0, vals.max() * 1.15)
  for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
  ax.spines["bottom"].set_color(C.SPINE)
  ax.grid(axis="x", color=C.GRID, lw=0.6)
  ax.tick_params(length=0)
  return fig, ax


# --- Bump chart ---------------------------------------------------------------
def bump(
    df: Any, hero: Any = None, preset: str = "wide", ax: Any = None
) -> tuple[Any, Any]:
  """df: rows=periods (index), cols=entities, values=metric.

  Ranks per period (1=best) and plots rank over time; rank 1 on top.
  """
  fig, ax = (ax.figure, ax) if ax is not None else _new(preset)
  ranks = df.rank(axis=1, ascending=False, method="min")
  heroes = {hero} if isinstance(hero, str) else set(hero or [])
  periods = list(df.index)
  x = np.arange(len(periods))
  for col in df.columns:
    is_hero = col in heroes
    color = C.OKABE_ITO[0] if is_hero else C.MUTE
    lw = 2.6 if is_hero else 1.6
    r = ranks[col].values
    ax.plot(
        x,
        r,
        color=color,
        lw=lw,
        marker="o",
        markersize=7,
        zorder=3 if is_hero else 2,
    )
    ax.text(
        x[0] - 0.06,
        r[0],
        f"{col}  ",
        ha="right",
        va="center",
        fontsize=T.TYPE["annotation"],
        color=C.INK if is_hero else C.SUBTLE,
        fontweight="bold" if is_hero else "normal",
    )
    ax.text(
        x[-1] + 0.06,
        r[-1],
        f"  {col}",
        ha="left",
        va="center",
        fontsize=T.TYPE["annotation"],
        color=C.INK if is_hero else C.SUBTLE,
        fontweight="bold" if is_hero else "normal",
    )
  ax.set_yticks(range(1, len(df.columns) + 1))
  ax.invert_yaxis()
  ax.set_xticks(x)
  ax.set_xticklabels(periods)
  ax.set_xlim(x[0] - 1.0, x[-1] + 1.0)
  for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
  ax.grid(False)
  ax.tick_params(length=0)
  ax.set_ylabel("Rank")
  return fig, ax


# --- Waterfall ----------------------------------------------------------------
def waterfall(
    labels: Any,
    deltas: Any,
    start: float = 0.0,
    start_label: str = "Start",
    total_label: str = "End",
    fmt: str | None = None,
    preset: str = "report",
    ax: Any = None,
) -> tuple[Any, Any]:
  """Bridge from start to end via signed contributions.

  Green up / vermillion down (with signed labels so hue isn't load-bearing);
  totals in gray.
  """
  fig, ax = (ax.figure, ax) if ax is not None else _new(preset)
  labels = list(labels)
  deltas = list(deltas)
  xs = [start_label] + labels + [total_label]
  x = np.arange(len(xs))
  # start total bar
  ax.bar(0, start, color=C.MUTE2, width=0.6, zorder=2)
  running = start
  levels = [start]  # running-total after each bar (index 0 = start bar top)
  for i, d in enumerate(deltas, start=1):
    bottom = running if d >= 0 else running + d
    color = C.POSITIVE if d >= 0 else C.NEGATIVE
    lbl = fmt.format(d) if fmt else f"{d:+,.0f}"
    ax.bar(i, abs(d), bottom=bottom, color=color, width=0.6, zorder=2)
    ax.annotate(
        lbl,
        xy=(i, bottom + abs(d)),
        xytext=(0, 4),
        textcoords="offset points",
        ha="center",
        fontsize=T.TYPE["annotation"] - 0.5,
        color=color,
        fontweight="bold",
    )
    running += d
    levels.append(running)
  total = running
  ax.bar(len(xs) - 1, total, color=C.MUTE2, width=0.6, zorder=2)
  # connector lines linking each bar top to the next bar's baseline
  for k, lvl in enumerate(levels):
    ax.plot(
        [k + 0.3, k + 1 - 0.3],
        [lvl, lvl],
        color=C.MUTE2,
        lw=0.8,
        linestyle=(0, (3, 2)),
        zorder=1,
    )
  ax.set_xticks(x)
  ax.set_xticklabels(xs, rotation=0)
  ax.set_ylim(0, max(start, total) * 1.2)
  for s in ("top", "right"):
    ax.spines[s].set_visible(False)
  ax.spines["left"].set_visible(False)
  ax.spines["bottom"].set_color(C.SPINE)
  ax.grid(axis="y", color=C.GRID, lw=0.6)
  ax.tick_params(length=0)
  return fig, ax


# --- Bullet chart -------------------------------------------------------------
def bullet(
    items: Any, preset: str = "report", ax: Any = None
) -> tuple[Any, Any]:
  """items: list of (label, value, target, [band_max...]).

  One KPI vs target with qualitative gray bands. Compact gauge replacement.
  """
  fig, ax = (ax.figure, ax) if ax is not None else _new(preset)
  n = len(items)
  y = np.arange(n)
  band_cols = ["#f0f0f0", "#dadada", "#bdbdbd"]
  for i, it in enumerate(items):
    value, target = it[1], it[2]
    bands = it[3] if len(it) > 3 else [value * 1.5]
    prev = 0
    for j, b in enumerate(bands):
      ax.barh(
          i,
          b - prev,
          left=prev,
          height=0.55,
          color=band_cols[min(j, len(band_cols) - 1)],
          zorder=1,
      )
      prev = b
    ax.barh(i, value, height=0.22, color=C.INK, zorder=3)
    ax.plot(
        [target, target], [i - 0.3, i + 0.3], color=C.NEGATIVE, lw=2.5, zorder=4
    )
  ax.set_yticks(y)
  ax.set_yticklabels([it[0] for it in items])
  for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
  ax.spines["bottom"].set_color(C.SPINE)
  ax.grid(axis="x", color=C.GRID, lw=0.6)
  ax.tick_params(length=0)
  return fig, ax


# --- Ridgeline ----------------------------------------------------------------
def ridgeline(
    groups: dict[Any, Any],
    overlap: float = 0.7,
    cmap: str | None = None,
    preset: str = "report",
    xlabel: str | None = None,
) -> tuple[Any, Any]:
  """groups: {name: 1d-array}. Compares distribution *shape* across groups.

  Ordered as given (order meaningfully before calling).
  """
  from scipy.stats import gaussian_kde

  T.apply(preset)
  names = list(groups.keys())
  n = len(names)
  fig, ax = plt.subplots(figsize=(T.ASPECT[preset][0], max(4, n * 0.7)))
  allv = np.concatenate([np.asarray(v, float) for v in groups.values()])
  xs = np.linspace(allv.min(), allv.max(), 400)
  step = 1.0
  colors = C.value_encode(range(n), cmap or C.SEQUENTIAL)
  for i, name in enumerate(reversed(names)):
    v = np.asarray(groups[name], float)
    kde = gaussian_kde(v)
    d = kde(xs)
    d = d / d.max() * (1 + overlap) * step
    base = i * step
    ax.fill_between(
        xs,
        base,
        base + d,
        color=colors[i],
        alpha=0.85,
        zorder=n - i,
        linewidth=0,
    )
    ax.plot(xs, base + d, color="white", lw=0.9, zorder=n - i)
    ax.text(
        -0.012,
        base,
        name,
        transform=ax.get_yaxis_transform(),
        va="bottom",
        ha="right",
        fontsize=T.TYPE["annotation"],
        color=C.INK,
        fontweight="bold",
    )
  ax.set_yticks([])
  span = allv.max() - allv.min()
  ax.set_xlim(allv.min() - span * 0.02, allv.max() + span * 0.02)
  for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
  ax.spines["bottom"].set_color(C.SPINE)
  ax.grid(False)
  ax.tick_params(length=0)
  if xlabel:
    ax.set_xlabel(xlabel)
  return fig, ax


# --- Sparklines (small multiples) --------------------------------------------
def sparklines(
    series: dict[Any, Any],
    ncols: int = 1,
    preset: str = "report",
    value_fmt: str | None = None,
) -> tuple[Any, Any]:
  """series: {name: 1d-array}. Tiny trend lines; mark last + min/max.

  Values secondary. Shared y within the grid for honest shape comparison.
  """
  T.apply(preset)
  names = list(series.keys())
  n = len(names)
  nrows = int(np.ceil(n / ncols))
  fig, axes = plt.subplots(
      nrows,
      ncols,
      figsize=(T.ASPECT[preset][0], max(3, n * 0.6)),
      squeeze=False,
      sharex=True,
  )
  ymin = min(np.min(v) for v in series.values())
  ymax = max(np.max(v) for v in series.values())
  for k, name in enumerate(names):
    r, c = divmod(k, ncols)
    ax = axes[r][c]
    y = np.asarray(series[name], float)
    x = np.arange(len(y))
    ax.plot(x, y, color=C.MUTE2, lw=1.4)
    ax.scatter([x[-1]], [y[-1]], s=18, color=C.OKABE_ITO[0], zorder=3)
    imax, imin = int(np.argmax(y)), int(np.argmin(y))
    ax.scatter([x[imax]], [y[imax]], s=14, color=C.POSITIVE, zorder=3)
    ax.scatter([x[imin]], [y[imin]], s=14, color=C.NEGATIVE, zorder=3)
    ax.set_ylim(ymin, ymax)
    ax.set_ylabel(
        name,
        rotation=0,
        ha="right",
        va="center",
        fontsize=T.TYPE["annotation"],
        color=C.INK,
    )
    lbl = value_fmt.format(y[-1]) if value_fmt else f"{y[-1]:,.0f}"
    ax.text(
        1.02,
        0.5,
        lbl,
        transform=ax.transAxes,
        va="center",
        ha="left",
        fontsize=T.TYPE["annotation"],
        color=C.OKABE_ITO[0],
        fontweight="bold",
    )
    for s in ("top", "right", "left", "bottom"):
      ax.spines[s].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)
  return fig, axes
