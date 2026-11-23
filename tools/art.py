#!/usr/bin/env python3
"""Art pipeline: fetch PhyloPic silhouettes and make consistent line-drawing variants.

    tools/art.py search "tyrannosaurus"           # list candidate images: uuid, license, attribution
    tools/art.py fetch <uuid> <slug>               # -> art/phylopic/<slug>.svg + art/credits.json record
    tools/art.py outline art/phylopic/<slug>.svg   # -> art/line/<slug>.svg (stroke-only rendering)

Every fetched image gets a record in art/credits.json (the image bibliography, decision #40); build.py letters it
automatically from the event's art.file. art.sources holds only the sources for the caption's facts.
Licenses are recorded; CC BY / BY-SA need attribution (printed in the Image credits list).
"""
import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(__file__))
import common as C  # noqa: E402

API = "https://api.phylopic.org"
UA = {"User-Agent": "book-build-script"}
LINE_STROKE = 70  # in PhyloPic/potrace path units (paths are scaled 0.1), ~ consistent line weight


def get(url: str) -> bytes:
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return r.read()


def build_index() -> int:
    return json.loads(get(API + "/"))["build"]


def search(name: str):
    b = build_index()
    q = urllib.parse.quote(name.lower())
    d = json.loads(get(f"{API}/images?build={b}&filter_name={q}&embed_items=true&page=0"))
    for it in d.get("_embedded", {}).get("items", []):
        L = it["_links"]
        print(it["uuid"], "|", L.get("license", {}).get("href"), "|", it.get("attribution"), "|",
              L.get("specificNode", {}).get("title"))


def fetch(uuid: str, slug: str):
    b = build_index()
    meta = json.loads(get(f"{API}/images/{uuid}?build={b}"))
    L = meta["_links"]
    svg = get(L["vectorFile"]["href"]).decode("utf-8")
    if re.search(r"<script|href\s*=", svg, re.I):
        sys.exit("refusing SVG with scripts/links")
    out = C.ROOT / "art" / "phylopic" / f"{slug}.svg"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg, encoding="utf-8")
    taxon = L.get("specificNode", {}).get("title", slug)
    lic = L.get("license", {}).get("href", "")
    who = meta.get("attribution") or "Unknown"
    page = f"https://www.phylopic.org/images/{uuid}"
    credits_p = C.ROOT / "art" / "credits.json"
    credits = C.load_json(credits_p)
    credits["images"] = [i for i in credits["images"] if i["slug"] != slug] + [{
        "slug": slug, "file": f"phylopic/{slug}.svg", "taxon": taxon, "attribution": who,
        "license": lic, "url": page}]
    credits_p.write_text(json.dumps(credits, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"-> {out}; credit record {slug} in art/credits.json")


def outline(src: str, stroke: int = LINE_STROKE):
    """Turn a filled silhouette into a line drawing: no fill, uniform stroke."""
    s = open(src, encoding="utf-8").read()
    s = re.sub(r'fill="#[0-9a-fA-F]{3,6}"\s+stroke="none"',
               f'fill="none" stroke="#000000" stroke-width="{stroke}" stroke-linejoin="round"', s)
    # Pad the canvas so strokes on silhouettes that touch the edge aren't clipped. Potrace paths sit in a
    # group scaled by 0.1, so the stroke is stroke/10 viewBox units wide; pad by that on every side.
    m = re.search(r'width="([\d.]+)pt" height="([\d.]+)pt" viewBox="([\d.\-]+) ([\d.\-]+) ([\d.]+) ([\d.]+)"', s)
    if m:
        w, h, x0, y0, vw, vh = map(float, m.groups())
        pad = stroke / 10
        s = s.replace(m.group(0), f'width="{w + 2 * pad:.6f}pt" height="{h + 2 * pad:.6f}pt" '
                                  f'viewBox="{x0 - pad:.6f} {y0 - pad:.6f} {vw + 2 * pad:.6f} {vh + 2 * pad:.6f}"')
    dst = C.ROOT / "art" / "line" / os.path.basename(src)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(s, encoding="utf-8")
    print(f"-> {dst}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("name")
    f = sub.add_parser("fetch"); f.add_argument("uuid"); f.add_argument("slug")
    o = sub.add_parser("outline"); o.add_argument("src"); o.add_argument("--stroke", type=int, default=LINE_STROKE)
    a = ap.parse_args()
    {"search": lambda: search(a.name), "fetch": lambda: fetch(a.uuid, a.slug),
     "outline": lambda: outline(a.src, a.stroke)}[a.cmd]()


if __name__ == "__main__":
    main()
