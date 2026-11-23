#!/usr/bin/env python3
"""Rough sketches of front-of-book diagram ideas (black/grey only), drawn from data/timescale.json.

    .venv/bin/python docs/sketches/front_diagrams.py   # -> docs/sketches/front-diagram-ideas.png
"""
import math
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle, Wedge  # noqa: E402

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
import common as C  # noqa: E402

cfg = C.config()
ts = C.load_timescale()
T0 = -cfg["time"]["start_year"]  # 4.57e9
EONS = [(u["name"], -u["start"], -u["end"]) for u in ts["eons"]]  # name, from (ya), to (ya)
GREYS = ["#d9d9d9", "#a6a6a6", "#6e6e6e", "#303030"]
INK = "#222"


def frac(ya):  # years-ago -> 0..1 from book start
    return 1 - ya / T0


fig, axs = plt.subplots(2, 3, figsize=(15, 9.5), dpi=130)
for ax in axs.flat:
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)

# 1. Clock: all of time = 24 hours
ax = axs[0, 0]
ax.set_title("A · The 24-hour clock", loc="left", fontsize=11, color=INK)
for i, (n, a, b) in enumerate(EONS):
    th0, th1 = 90 - 360 * frac(b), 90 - 360 * frac(a)
    ax.add_patch(Wedge((0, 0), 1, th0, th1, width=0.35, facecolor=GREYS[i], edgecolor="white", lw=1.5))
    mid = math.radians((th0 + th1) / 2)
    ax.text(1.12 * math.cos(mid), 1.12 * math.sin(mid), n, ha="center", va="center", fontsize=8, color=INK)
ax.plot([0, 0], [0.95, 1.27], color=INK, lw=1)
ax.text(0, 1.3, "midnight = now\nhumans: last ~6 seconds", ha="center", va="bottom", fontsize=7.5, color=INK)
ax.set_xlim(-1.45, 1.45); ax.set_ylim(-1.35, 1.6); ax.set_aspect("equal")

# 2. Spiral: time unwinds outward; the present is the outer tip
ax = axs[0, 1]
ax.set_title("B · Spiral of time", loc="left", fontsize=11, color=INK)
turns, N = 4, 1200
for i, (n, a, b) in enumerate(EONS):
    f0, f1 = frac(a), frac(b)
    fs = [f0 + (f1 - f0) * k / 200 for k in range(201)]
    xs = [(0.15 + f) * math.cos(2 * math.pi * turns * f) for f in fs]
    ys = [(0.15 + f) * math.sin(2 * math.pi * turns * f) for f in fs]
    ax.plot(xs, ys, color=GREYS[i], lw=9, solid_capstyle="butt")
    fm = (f0 + f1) / 2
    ax.text((0.15 + fm) * math.cos(2 * math.pi * turns * fm) * 1.0, (0.15 + fm) * math.sin(2 * math.pi * turns * fm) + 0.07,
            n, fontsize=7.5, ha="center", color=INK)
ax.annotate("now", xy=(1.15, 0), xytext=(1.3, -0.25), fontsize=8, arrowprops=dict(arrowstyle="-", color=INK))
ax.set_xlim(-1.4, 1.5); ax.set_ylim(-1.4, 1.4); ax.set_aspect("equal")

# 3. Nested zoom: each bar is the last tenth of the one above
ax = axs[0, 2]
ax.set_title("C · Powers-of-ten zoom", loc="left", fontsize=11, color=INK)
span = T0
for row in range(6):
    y = -row * 1.0
    if row == 0:
        for i, (n, a, b) in enumerate(EONS):
            ax.add_patch(Rectangle((frac(a), y), frac(b) - frac(a), 0.45, facecolor=GREYS[i], edgecolor="white"))
    else:
        ax.add_patch(Rectangle((0, y), 1, 0.45, facecolor="#e6e6e6", edgecolor=INK, lw=0.6))
    label = f"last {span:,.0f} years" if span >= 1 else ""
    ax.text(0, y + 0.55, label, fontsize=7.5, color=INK)
    ax.add_patch(Rectangle((0.9, y), 0.1, 0.45, facecolor="none", edgecolor=INK, lw=1))
    if row < 5:
        ax.plot([0.9, 0], [y, y - 0.55], color="#888", lw=0.6)
        ax.plot([1.0, 1.0], [y, y - 0.55], color="#888", lw=0.6)
    span /= 10
ax.text(0.02, -5.25, "…continue to the last 45 years", fontsize=7, color="#555")
ax.set_xlim(-0.05, 1.05); ax.set_ylim(-5.5, 1.2)

# 4. The book itself: foredge to scale (pages per eon), as the reader will see it
ax = axs[1, 0]
ax.set_title("D · This book's foredge, to scale", loc="left", fontsize=11, color=INK)
pages = {n: 0 for n, _, _ in EONS}
for p in range(1, C.n_pages(cfg) + 1):
    mid = sum(C.page_bounds(p, cfg)) // 2
    pages[C.unit_at(mid, ts["eons"]) or "Hadean"] += 1
leaf_mm = 0.11  # 24 lb paper, approx
x = 0
ax.add_patch(Rectangle((-4, 0), 4, 4, facecolor="#f4f4f4", edgecolor=INK, lw=0.5))
ax.text(-2, 2, "front\nmatter", ha="center", va="center", fontsize=6.5, rotation=90)
for i, (n, _, _) in enumerate(EONS):
    w = pages[n] / 2 * leaf_mm
    ax.add_patch(Rectangle((x, 0), w, 4, facecolor="white", edgecolor=INK, lw=0.5))
    ax.add_patch(Rectangle((x, 3 - i * 0.9), w, 0.8, facecolor=GREYS[3], edgecolor="none"))
    ax.text(x + w / 2, -0.3, f"{n}\n{pages[n]} pp · {w:.0f} mm", ha="center", va="top", fontsize=6.8)
    x += w
ax.text(x / 2, 4.4, f"≈{x:.0f} mm of timeline; Phanerozoic (all complex life) is the last {pages['Phanerozoic'] / 2 * leaf_mm:.0f} mm",
        ha="center", fontsize=7.5)
ax.set_xlim(-6, x + 3); ax.set_ylim(-1.6, 5)

# 5. One calendar year
ax = axs[1, 1]
ax.set_title("E · Earth's history as one year", loc="left", fontsize=11, color=INK)
days = 365
MONTH_END = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
for d in range(days):
    ya = T0 * (1 - (d + 0.5) / days)
    e = C.unit_at(-int(ya), ts["eons"]) or "Hadean"
    i = [n for n, _, _ in EONS].index(e)
    m = next(k for k in range(12) if d < MONTH_END[k])
    dd = d - (MONTH_END[m - 1] if m else 0)
    ax.add_patch(Rectangle((dd, -m), 0.9, 0.8, facecolor=GREYS[i], edgecolor="none"))
for m, name in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()):
    ax.text(-0.8, -m + 0.4, name, ha="right", va="center", fontsize=7)
ax.text(0, -12.4, "1 day ≈ 12.5 million years · animals appear mid-November ·\nlast non-avian dinosaurs Dec 26 · humans: final ~35 minutes of Dec 31",
        fontsize=7, va="top")
ax.set_xlim(-3, 31); ax.set_ylim(-13.6, 1)

# 6. Single ribbon with callouts (classic linear timeline, fold-out style)
ax = axs[1, 2]
ax.set_title("F · One ribbon with callouts", loc="left", fontsize=11, color=INK)
for i, (n, a, b) in enumerate(EONS):
    ax.add_patch(Rectangle((frac(a), 0), frac(b) - frac(a), 0.25, facecolor=GREYS[i], edgecolor="white"))
    ax.text((frac(a) + frac(b)) / 2, 0.32, n, ha="center", fontsize=7.5)
for f, txt, up in [(frac(4.51e9), "Moon", 1), (frac(2.32e9), "oxygen", -1), (frac(538.8e6), "animals", 1),
                   (frac(66e6), "Chicxulub", -1), (1.0, "now", 1)]:
    y1 = 0.75 if up > 0 else -0.45
    ax.plot([f, f], [0.25 if up > 0 else 0, y1], color=INK, lw=0.6)
    ax.text(f, y1 + (0.03 if up > 0 else -0.1), txt, ha="center", fontsize=7)
ax.text(0, -0.9, "Could be a fold-out or the endpapers; page numbers marked along the bottom edge.", fontsize=7)
ax.set_xlim(-0.05, 1.08); ax.set_ylim(-1.1, 1.1)

fig.suptitle("Front-of-book diagram ideas (rough sketches; black and grey only)", fontsize=13, x=0.01, ha="left", color=INK)
fig.tight_layout()
out = os.path.join(os.path.dirname(__file__), "front-diagram-ideas.png")
fig.savefig(out)
print(out)
