"""Shared helpers: paths, data loading, page math, layout estimation.

Every other tool imports this. Keep it dependency-light (stdlib + jsonschema).
"""
from __future__ import annotations

import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
BUILD = ROOT / "build"
MM_PER_PT = 25.4 / 72


# ---------- loading ----------

def load_json(path: Path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)



def load_tags() -> dict[str, str]:
    """Master tag list: {tag: description} from data/tags.json."""
    return load_json(DATA / "tags.json")["tags"]

def config() -> dict:
    return load_json(ROOT / "config.json")


def event_files() -> list[Path]:
    return sorted((DATA / "events").glob("*.json"))


def load_events() -> list[dict]:
    """All events from every file in data/events/, each tagged with its source file."""
    out = []
    for p in event_files():
        for ev in load_json(p):
            ev = dict(ev)
            ev["_file"] = p.name
            out.append(ev)
    out.sort(key=lambda e: e["t"])
    return out


# ---------- image credits (decision #40) ----------

LICENSE_NAMES = {
    "https://creativecommons.org/publicdomain/zero/1.0/": "CC0 1.0",
    "https://creativecommons.org/publicdomain/mark/1.0/": "Public Domain Mark 1.0",
    "https://creativecommons.org/licenses/by/3.0/": "CC BY 3.0",
    "https://creativecommons.org/licenses/by/4.0/": "CC BY 4.0",
    "https://creativecommons.org/licenses/by-sa/3.0/": "CC BY-SA 3.0",
    "https://creativecommons.org/licenses/by-sa/4.0/": "CC BY-SA 4.0",
}


def art_slug(file: str) -> str:
    """Event art file ('line/tiktaalik.svg') -> credits slug ('tiktaalik')."""
    return Path(file).stem


def taxon_rich(name: str) -> str:
    """Italicise genus/species names (_..._), not higher taxa such as Thysanoptera or Cyanobacteriota."""
    higher = ("ota", "ptera", "idae", "aceae", "ales", "ida", "phyta", "oidea", "formes")
    if " " not in name and name.endswith(higher):
        return name
    return f"_{name}_"


def load_credits() -> dict:
    """art/credits.json as {'by_slug': {slug: image record}, 'entries': {credit id: printable entry}}.
    A third-party image is its own credit entry (id = slug); shared entries (e.g. claude-drawings) come from 'shared'."""
    raw = load_json(ROOT / "art" / "credits.json")
    by_slug = {im["slug"]: im for im in raw["images"]}
    entries = {s["id"]: s for s in raw.get("shared", [])}
    for im in raw["images"]:
        if "credits" not in im:
            entries[im["slug"]] = {"id": im["slug"], "attribution": im.get("attribution", "Unknown"),
                                   "title": taxon_rich(im['taxon']), "url": im.get("url", ""),
                                   "license": im.get("license", ""), "note": ""}
    return {"by_slug": by_slug, "entries": entries}


def letter(i: int) -> str:
    """0 -> a, 25 -> z, 26 -> aa, ..."""
    s = ""
    i += 1
    while i:
        i, r = divmod(i - 1, 26)
        s = chr(97 + r) + s
    return s


def image_credits(events: list[dict]) -> tuple[dict, list[dict]]:
    """Letter every credit entry in book order (first use). Returns ({slug: [letters]}, [printable entries])."""
    cr = load_credits()
    order: list[str] = []
    for ev in sorted(events, key=lambda e: e["t"]):
        if "art" in ev:
            im = cr["by_slug"].get(art_slug(ev["art"]["file"]))
            for cid in (im.get("credits", [im["slug"]]) if im else []):
                if cid not in order:
                    order.append(cid)
    letters = {cid: letter(i) for i, cid in enumerate(order)}
    per_slug = {slug: [letters[c] for c in im.get("credits", [slug]) if c in letters]
                for slug, im in cr["by_slug"].items()}
    listing = []
    for cid in order:
        e = cr["entries"][cid]
        lic = LICENSE_NAMES.get(e.get("license", ""), e.get("license", ""))
        lic = lic[:1].upper() + lic[1:]
        url = re.sub(r"^https?://(www\.)?", "", e.get("url", "")).rstrip("/")
        who = e.get("attribution", "") or "Unknown"
        listing.append({"letter": letters[cid], "attribution": "Anonymous" if who in ("Unknown", "None") else who,
                        "title": e.get("title", ""), "note": e.get("note", ""), "url": url, "license": lic})
    return per_slug, listing


def load_timescale() -> dict:
    return load_json(DATA / "timescale.json")


# Footer slots (decision #45): two every-page lines (sky + air; life) and a 100 Myr check-in box.
FOOTER_SLOTS = ("sky", "air", "life", "checkin")
CHECKIN_EVERY = 100_000_000  # years; check-in box on pages whose bottom year is a multiple of this


def load_series() -> list[dict]:
    """Footer series, in print order ("order" field)."""
    ss = [load_json(p) for p in sorted((DATA / "series").glob("*.json"))]
    return sorted(ss, key=lambda s: s.get("order", 99))


def load_foredge() -> dict:
    p = DATA / "foredge.json"
    return load_json(p) if p.exists() else {"slots": 1, "bands": [], "sources": []}


def load_timescale_names() -> dict:
    """Back-matter explainer of eon/era names (data/explainers/timescale-names.json)."""
    return load_json(DATA / "explainers" / "timescale-names.json")


def bib_keys() -> set[str]:
    text = (DATA / "sources.bib").read_text(encoding="utf-8")
    return set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", text))


# ---------- page math ----------
# Content page n (1-based) covers [start + (n-1)*ypp, start + n*ypp). Top of page = older.

def n_pages(cfg: dict) -> int:
    t = cfg["time"]
    return math.ceil((t["end_year"] - t["start_year"]) / t["years_per_page"])


def page_of(t: int, cfg: dict) -> int:
    tc = cfg["time"]
    n = int((t - tc["start_year"]) // tc["years_per_page"]) + 1
    return min(max(n, 1), n_pages(cfg))


def page_bounds(n: int, cfg: dict) -> tuple[int, int]:
    tc = cfg["time"]
    top = tc["start_year"] + (n - 1) * tc["years_per_page"]
    return top, top + tc["years_per_page"]


def frac_in_page(t: int, n: int, cfg: dict) -> float:
    top, bot = page_bounds(n, cfg)
    return (t - top) / (bot - top)


def parse_ranges(spec: str, maxn: int) -> list[int]:
    """'1-4,13,900-902' -> sorted unique page list."""
    pages: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            pages.update(range(int(a), int(b) + 1))
        else:
            pages.add(int(part))
    return sorted(p for p in pages if 1 <= p <= maxn)


# ---------- formatting ----------

MINUS = "−"


def fmt_year(t: int) -> str:
    s = f"{abs(t):,}"
    return (MINUS + s) if t < 0 else s


def fmt_when(ev: dict) -> str:
    s = fmt_year(ev["t"])
    if ev.get("t_err"):
        s += f" ± {ev['t_err']:,}"
    return s


# ---------- timescale / series lookup ----------

def unit_at(t: int, units: list[dict]) -> str | None:
    for u in units:
        if u["start"] <= t < u["end"]:
            return u["name"]
    return None


def series_value(series: dict, t: int):
    """Value of a footer series at year t, or None.
    Model series (\"model\": name) are computed by tools/models.py; point series are linearly
    interpolated inside their data range and never extrapolated."""
    if series.get("model"):
        from models import MODELS
        v = MODELS[series["model"]](t)
        return None if v is None else (v, series["sources"])
    pts = sorted(series["points"], key=lambda p: p["t"])
    if not pts or t < pts[0]["t"] or t > pts[-1]["t"]:
        return None
    for a, b in zip(pts, pts[1:]):
        if a["t"] <= t <= b["t"]:
            f = 0 if b["t"] == a["t"] else (t - a["t"]) / (b["t"] - a["t"])
            v = a["v"] + f * (b["v"] - a["v"])
            srcs = sorted(set(a["sources"]) | set(b["sources"]))
            return v, srcs
    p = pts[-1]
    return p["v"], p["sources"]


HOLOCENE_START = -11_700  # years; a series' latest point counts as "today" if it is this young


def series_now(series: dict):
    """Present-day value of a series, used by relative footer formats: the value at t = 0 for models,
    else the latest point if it lies in the Holocene (stage data such as PhanDA end at the Holocene mean age)."""
    if series.get("model"):
        r = series_value(series, 0)
        return None if r is None else r[0]
    pts = series.get("points") or []
    if not pts:
        return None
    p = max(pts, key=lambda p: p["t"])
    return p["v"] if p["t"] >= HOLOCENE_START else None


UNIT_LEVELS = ("eons", "eras", "periods", "epochs")
LEVEL_NAMES = {"eons": "Eon", "eras": "Era", "periods": "Period", "epochs": "Epoch"}


def units_at(t: int, ts: dict) -> list[str]:
    """Hierarchy of named units at year t, e.g. ['Phanerozoic', 'Cenozoic', 'Paleogene', 'Paleocene']."""
    return [n for n in (unit_at(t, ts.get(lvl, [])) for lvl in UNIT_LEVELS) if n]


def boundaries_in(top: int, bot: int, ts: dict) -> list[dict]:
    """Unit starts strictly inside a page (not at its top edge): drawn as marks on the ruler."""
    out = {}
    for lvl in UNIT_LEVELS:
        for u in ts.get(lvl, []):
            if top < u["start"] < bot:
                out.setdefault(u["start"], []).append({**u, "rank": LEVEL_NAMES[lvl]})
    return [{"t": t, "units": units} for t, units in sorted(out.items())]


def boundary_entry(b: dict, ts: dict) -> dict:
    """Printable entry for unit starts at one instant: bold title, description of the largest unit."""
    units = b["units"]
    names = [f"{u['name']} {u['rank']}" for u in units]
    title = (names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]) + \
        (" begins" if len(names) == 1 else " begin")
    desc = next((u["description"] for u in units if u.get("description")), "")
    return {"kind": "boundary", "id": f"boundary-{b['t']}", "t": b["t"], "title": title,
            "when": fmt_year(b["t"]), "text": desc, "sources": ts["sources"],
            "importance": 0, "art": None, "fixed": True}


# ---------- page entries & layout ----------

def fmt_duration(years: int) -> str:
    """Plain-language length: 'about 57 million years', '750,000 years'."""
    y = abs(years)
    for unit, name in ((1_000_000_000, "billion"), (1_000_000, "million")):
        if y >= unit:
            v = y / unit
            s = f"{v:.0f}" if v >= 10 or v == int(v) else f"{v:.1f}".rstrip("0").rstrip(".")
            return f"about {s} {name} years"
    return f"about {y:,} years"


def span_marks(ev: dict, cfg: dict) -> list[str]:
    """Which entries a span prints (decision #33): its start and its end, unless both fall on the same
    page (then one entry at the midpoint). An explicit `mention` list overrides."""
    if "mention" in ev:
        return ev["mention"]
    s, e = sorted(ev["span"])
    return ["mid"] if page_of(s, cfg) == page_of(e, cfg) else ["start", "end"]


def page_entries(events: list[dict], cfg: dict) -> dict[int, list[dict]]:
    """Map page -> list of entries to print. Spans print at their start and end (decision #33)."""
    by_page: dict[int, list[dict]] = {}
    for ev in events:
        marks = [("mid", ev["t"])]
        if "span" in ev:
            s, e = sorted(ev["span"])
            marks = [(m, {"start": s, "mid": ev["t"], "end": e}[m]) for m in span_marks(ev, cfg)]
        for kind, t in marks:
            n = page_of(t, cfg)
            entry = {
                "id": ev["id"],
                "t": t,
                "title": ev["title"],
                "when": fmt_when(ev),
                "text": ev["text"],
                "sources": ev["sources"],
                "importance": ev.get("importance", 3),
                "art": ev.get("art"),
            }
            if "span" in ev and kind != "mid":
                span_when = f"{fmt_year(s)} to {fmt_year(e)}"
                if kind == "start":  # full entry, with art, where the phenomenon begins
                    entry.update(title=ev["title"] + " (begins)", when=span_when)
                else:  # short reminder where it ends
                    entry.update(title=ev["title"] + " (ends)", when=fmt_year(e), art=None,
                                 text=f"Began at {fmt_year(s)}; lasted {fmt_duration(e - s)}.")
            elif "span" in ev:  # midpoint entry for a short span: show the range
                entry["when"] = f"{fmt_year(s)} to {fmt_year(e)}"
            by_page.setdefault(n, []).append(entry)
    return by_page


def body_geometry(cfg: dict) -> tuple[float, float]:
    p = cfg["page"]
    h = p["height_mm"] - p["margin_top_mm"] - p["margin_bottom_mm"]
    w = p["width_mm"] - p["margin_inside_mm"] - p["margin_outside_mm"]
    return w, h


def estimate_height_mm(entry: dict, cfg: dict) -> float:
    """Rough rendered height. Calibrate later against Typst's measured sizes."""
    w, _ = body_geometry(cfg)
    ty, lay = cfg["type"], cfg["layout"]
    char_mm = ty["size_pt"] * lay["avg_char_width_em"] * MM_PER_PT
    cpl = max(10, int((w - lay["ruler_width_mm"]) / char_mm))
    line_mm = ty["size_pt"] * ty["leading_factor"] * MM_PER_PT
    head = len(entry["title"]) + len(entry["when"]) + 3
    body = len(entry["text"]) + 5 * len(entry["sources"])
    lines = math.ceil(head / cpl) + math.ceil(body / cpl)
    art = (lay["art_height_mm"] + 1.5) if entry.get("art") else 0
    return lines * line_mm + art


def layout_page(entries: list[dict], cfg: dict) -> tuple[list[dict], float]:
    """Place entries near their exact time. Entries with "fixed": True (unit boundaries) stay at their
    anchor; others are pushed down past earlier entries, then pulled up from the bottom/fixed entries.
    Returns (placed entries with y_mm/anchor_mm/h_mm, used fraction of body height)."""
    _, H = body_geometry(cfg)
    gap = cfg["layout"]["event_gap_mm"]
    placed = []
    for e in sorted(entries, key=lambda e: (e["t"], not e.get("fixed", False))):
        h = estimate_height_mm(e, cfg)
        anchor = frac_in_page(e["t"], page_of(e["t"], cfg), cfg) * H
        y = min(anchor, H - h) if e.get("fixed") else anchor
        placed.append({**e, "anchor_mm": anchor, "y_mm": y, "h_mm": h})
    cursor = 0.0  # push down
    for e in placed:
        if not e.get("fixed"):
            e["y_mm"] = max(e["y_mm"], cursor)
        cursor = e["y_mm"] + e["h_mm"] + gap
    limit = H  # pull up; fixed entries (unit labels) yield too when there is no room below them
    for e in reversed(placed):
        if e["y_mm"] + e["h_mm"] > limit:
            e["y_mm"] = max(0.0, limit - e["h_mm"])
        limit = e["y_mm"] - gap
    cursor = 0.0  # final push down: unit labels may also slide down past entries that could not move up
    for e in placed:
        e["y_mm"] = max(e["y_mm"], cursor)
        cursor = e["y_mm"] + e["h_mm"] + gap
    used = sum(e["h_mm"] + gap for e in placed) / H
    if cursor - gap > H + 0.01:  # ran off the bottom
        used = max(used, 1.01)
    overlap = any(b["y_mm"] < a["y_mm"] + a["h_mm"] - 0.01 for a, b in zip(placed, placed[1:]))
    if overlap:  # entries could not all fit: report as overflow even if the height sum is < 1
        used = max(used, 1.01)
    return placed, min(used, 9.99)
