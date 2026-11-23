#!/usr/bin/env python3
"""How full is the book? Lays out ALL content pages (no typesetting) and reports.

    tools/fullness.py            # writes build/fullness.md (+ .png) and appends build/fullness_history.csv
    tools/fullness.py --text     # print the markdown summary only (cheap for Claude to read)
    tools/fullness.py --emptiest 30

Fullness = estimated text height / body height (from common.layout_page).
>1.0 means the page overflows. The estimate will later be calibrated against Typst measurements.
"""
import argparse
import csv
import os
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))
import common as C  # noqa: E402

RAMP = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]
EMPTY = "#f0efec"
OVER = "#c62828"


def compute(cfg):
    by_page = C.page_entries(C.load_events(), cfg)
    ts = C.load_timescale()
    N = C.n_pages(cfg)
    full, count = {}, {}
    for n in range(1, N + 1):
        ents = by_page.get(n, [])
        top, bot = C.page_bounds(n, cfg)
        bounds = [C.boundary_entry(b, ts) for b in C.boundaries_in(top, bot, ts)]  # same input as build.py
        _, used = C.layout_page(ents + bounds, cfg) if ents else ([], 0.0)
        full[n], count[n] = used, len(ents)
    return N, full, count


def runs_of_empty(N, count):
    runs, start = [], None
    for n in range(1, N + 2):
        empty = n <= N and count[n] == 0
        if empty and start is None:
            start = n
        if not empty and start is not None:
            runs.append((n - start, start, n - 1))
            start = None
    return sorted(runs, reverse=True)


def summary_md(cfg, N, full, count, k):
    ts = C.load_timescale()
    lines = ["# Book fullness", "", f"_Generated {time.strftime('%Y-%m-%d %H:%M')}_", ""]
    nonempty = sum(1 for n in count if count[n])
    over = [n for n in full if full[n] > 1.0]
    lines += [f"- Content pages: **{N}**; with ≥1 entry: **{nonempty}** ({nonempty / N:.1%})",
              f"- Entries: **{sum(count.values())}**; mean fullness: **{sum(full.values()) / N:.1%}**",
              f"- Overflowing pages: {', '.join(map(str, over)) or 'none'}", "",
              "| Eon | Pages | Non-empty | Mean fullness |", "|---|---|---|---|"]
    for u in ts["eons"]:
        ps = [n for n in range(1, N + 1) if C.unit_at(sum(C.page_bounds(n, cfg)) // 2, [u])]
        if ps:
            ne = sum(1 for n in ps if count[n])
            lines.append(f"| {u['name']} | {len(ps)} | {ne} | {sum(full[n] for n in ps) / len(ps):.1%} |")
    lines += ["", f"## Longest empty stretches (top {k})", "", "| Pages | Years | Length |", "|---|---|---|"]
    for length, a, b in runs_of_empty(N, count)[:k]:
        lines.append(f"| {a}–{b} | {C.fmt_year(C.page_bounds(a, cfg)[0])} to "
                     f"{C.fmt_year(C.page_bounds(b, cfg)[1])} | {length} |")
    return "\n".join(lines) + "\n"


def plot(cfg, N, full, path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle

    cols = 50  # 250 Myr per row
    rows = (N + cols - 1) // cols
    fig, ax = plt.subplots(figsize=(11, 0.32 * rows + 1.4), dpi=150)
    for n in range(1, N + 1):
        r, c = divmod(n - 1, cols)
        f = full[n]
        color = EMPTY if f == 0 else RAMP[min(len(RAMP) - 1, int(min(f, 0.999) * len(RAMP)))]
        ax.add_patch(Rectangle((c, -r), 0.92, 0.85, facecolor=color,
                               edgecolor=OVER if f > 1 else "none", linewidth=1.2))
    for u in C.load_timescale()["eons"]:
        p = C.page_of(u["start"], cfg)
        r, c = divmod(p - 1, cols)
        ax.plot([c - 0.04, c - 0.04], [-r - 0.05, -r + 0.9], color="#222", lw=1.2)
        ax.text(c, -r + 0.95, u["name"], fontsize=6.5, color="#222", va="bottom")
    ax.set_yticks([-r + 0.42 for r in range(rows)])
    ax.set_yticklabels([f"p{r * cols + 1}  {C.fmt_year(C.page_bounds(r * cols + 1, cfg)[0])}" for r in range(rows)],
                       fontsize=6.5, color="#555")
    ax.set_xticks([])
    ax.set_xlim(-0.5, cols)
    ax.set_ylim(-rows + 0.5, 1.4)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(length=0)
    ax.set_title("Book fullness: one cell per page (5 Myr), 50 pages per row. Gray = empty, light→dark blue = fuller, "
                 "red outline = overflow", fontsize=8, color="#333", loc="left")
    fig.tight_layout()
    fig.savefig(path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", action="store_true", help="print summary only; no files")
    ap.add_argument("--emptiest", type=int, default=15)
    a = ap.parse_args()
    cfg = C.config()
    N, full, count = compute(cfg)
    md = summary_md(cfg, N, full, count, a.emptiest)
    if a.text:
        print(md)
        return
    C.BUILD.mkdir(exist_ok=True)
    (C.BUILD / "fullness.md").write_text(md, encoding="utf-8")
    plot(cfg, N, full, C.BUILD / "fullness.png")
    hist = C.BUILD / "fullness_history.csv"
    new = not hist.exists()
    with open(hist, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["timestamp", "entries", "nonempty_pages", "mean_fullness"])
        w.writerow([time.strftime("%Y-%m-%d %H:%M"), sum(count.values()),
                    sum(1 for v in count.values() if v), round(sum(full.values()) / N, 4)])
    print(md)
    print(f"-> {C.BUILD / 'fullness.md'}, {C.BUILD / 'fullness.png'}, {hist}")


if __name__ == "__main__":
    main()
