#!/usr/bin/env python3
"""Build the book (or part of it): data -> build/book.json -> Typst -> PDF/PNG.

    tools/build.py                       # whole book -> build/book.pdf
    tools/build.py --demo                # config.demo_pages -> build/demo.pdf
    tools/build.py --pages 1-15          # content pages 1..15 (+ front/back matter) -> build/partial.pdf
    tools/build.py --at -66043000        # just the page holding that year
    tools/build.py --pages 901 --content-only -o build/single.pdf   # exactly those pages, nothing else
    tools/build.py --pages 871-880 --footer checkin                 # override footer mode
    tools/build.py --pages 901 --png     # PNG per page in build/png/ (visual checks)

"Content page" n covers years [start + (n-1)*5e6, start + n*5e6); see tools/query.py --page-of YEAR.
Only selected pages are laid out and typeset, so partial builds are fast.
"""
import argparse
import json
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))
import common as C  # noqa: E402


def metrics_at(t: int, series: list[dict]) -> list[dict]:
    out = []
    for s in series:
        r = C.series_value(s, t)
        if r is None:
            continue
        v, srcs = r
        unit = s["unit"]
        value = f"{v:,.{s.get('decimals', 1)}f}" + ("" if unit.startswith("%") else "\u2009")
        out.append({"label": s["label"], "value": value, "unit": unit, "sources": srcs})
    return out


def foredge_slot(t: int, fe: dict):
    for b in fe["bands"]:
        if b["start"] <= t < b["end"]:
            return b["slot"]
    return None


def build_data(pages: list[int], cfg: dict, front: bool, back: bool, footer_mode: str) -> dict:
    events = C.load_events()
    ts = C.load_timescale()
    series = C.load_series()
    fe = C.load_foredge()
    credit_letters, credit_list = C.image_credits(events)
    for ev in events:
        if "art" in ev:
            ev["art"] = {**ev["art"], "letters": credit_letters.get(C.art_slug(ev["art"]["file"]), [])}
    by_page = C.page_entries(events, cfg)
    _, H = C.body_geometry(cfg)
    every = cfg["footer"]["checkin_every_years"]
    out_pages = []
    for n in pages:
        top, bot = C.page_bounds(n, cfg)
        mid = (top + bot) // 2
        bounds = [C.boundary_entry(b, ts) for b in C.boundaries_in(top, bot, ts)]
        placed, used = C.layout_page(by_page.get(n, []) + bounds, cfg)
        checkin = top % every == 0
        if footer_mode == "every":
            metrics = metrics_at(mid, series)
        else:
            metrics = metrics_at(top, series) if checkin else []
        out_pages.append({
            "n": n,
            "top": top, "bottom": bot,
            "top_label": C.fmt_year(top), "bottom_label": C.fmt_year(bot),
            "units": C.units_at(top, ts),
            "unit_starts": [u["name"] for lvl in ("eons", "eras") for u in ts.get(lvl, [])
                            if top <= u["start"] < bot],
            "events": [{"kind": e.get("kind", "event"), **{k: e[k] for k in ("id", "title", "when", "text", "sources", "importance",
                                          "art", "y_mm", "anchor_mm", "h_mm")}} for e in placed],
            "footer_mode": footer_mode,
            "checkin": checkin,
            "metrics": metrics,
            "foredge_slot": foredge_slot(mid, fe) if cfg["foredge"]["enabled"] else None,
            "fullness": round(used, 3),
        })
    return {"config": cfg, "body_height_mm": H, "front": front, "back": back,
            "total_content_pages": C.n_pages(cfg), "pages": out_pages,
            "foredge_slots": fe["slots"], "image_credits": credit_list, "built": time.strftime("%Y-%m-%d %H:%M")}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--pages", help="content page ranges, e.g. 1-15,900-914")
    g.add_argument("--demo", action="store_true", help="use config demo_pages")
    g.add_argument("--at", type=int, help="year; build only the page containing it")
    ap.add_argument("--no-front", action="store_true")
    ap.add_argument("--no-back", action="store_true", help="skip back matter other than the bibliography")
    ap.add_argument("--content-only", action="store_true",
                    help="output only the selected content pages (drops front matter and bibliography)")
    ap.add_argument("--footer", choices=["every", "checkin"], help="override config footer.mode")
    ap.add_argument("--png", action="store_true", help="render PNGs to build/png/ instead of a PDF")
    ap.add_argument("--ppi", type=int, default=110)
    ap.add_argument("-o", "--out", help="output PDF path")
    a = ap.parse_args()

    if subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "check.py"), "--quiet"]).returncode:
        print("check.py failed; fix data first", file=sys.stderr)
        return 1

    cfg = C.config()
    N = C.n_pages(cfg)
    if a.pages:
        pages, name = C.parse_ranges(a.pages, N), "partial"
    elif a.demo:
        pages, name = C.parse_ranges(cfg["demo_pages"], N), "demo"
    elif a.at is not None:
        pages, name = [C.page_of(a.at, cfg)], "partial"
    else:
        pages, name = list(range(1, N + 1)), "book"

    front = not (a.no_front or a.content_only)
    C.BUILD.mkdir(exist_ok=True)
    data = build_data(pages, cfg, front, not a.no_back, a.footer or cfg["footer"]["mode"])
    (C.BUILD / "book.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")

    import typst
    src = str(C.ROOT / "typeset" / "book.typ")
    t0 = time.time()
    if a.png:
        outdir = C.BUILD / "png"
        outdir.mkdir(exist_ok=True)
        for f in outdir.glob("*.png"):
            f.unlink()
        imgs = typst.compile(src, root=str(C.ROOT), format="png", ppi=a.ppi)
        imgs = imgs if isinstance(imgs, list) else [imgs]
        if a.content_only:
            imgs = imgs[:len(pages)]
        for i, b in enumerate(imgs, 1):
            (outdir / f"{name}-{i:04d}.png").write_bytes(b)
        print(f"{len(imgs)} PNGs -> {outdir}  ({time.time() - t0:.1f}s)")
        return 0

    out = a.out or str(C.BUILD / f"{name}.pdf")
    typst.compile(src, output=out, root=str(C.ROOT))
    if a.content_only:  # front matter is off, so content pages are the first len(pages) pages
        from pypdf import PdfReader, PdfWriter
        r, w = PdfReader(out), PdfWriter()
        for i in range(len(pages)):
            w.add_page(r.pages[i])
        w.write(out)
    print(f"{len(pages)} content pages -> {out}  ({time.time() - t0:.1f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
