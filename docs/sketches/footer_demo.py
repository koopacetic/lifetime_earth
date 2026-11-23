#!/usr/bin/env python3
"""Footer design sketch: slots (demo A) vs every-page line + 100 Myr check-in box (demo B).

    .venv/bin/python docs/sketches/footer_demo.py   -> docs/sketches/footer-demo.pdf, footer-demo-strips.png

Real page bodies (tools/build.py layout) with MOCK footer values. The footer numbers below are
illustrative placeholders, rounded from memory of the literature: NOT cited, NOT for the book.
Production code (typeset/book.typ, tools/build.py) is not changed; the footer function is swapped in a copy.
"""
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import build  # noqa: E402
import common as C  # noqa: E402

OUT = ROOT / "docs" / "sketches"
PAGES = [314, 794, 821, 854, 855, 905, 914]   # 314, 794, 854, 914 end on a round 100 Myr -> check-in

# ---- mock values (illustrative only) ----
# slot items: SKY (whole book), AIR (whole book where known), LIFE (changes by era)
MOCK = {
    314: dict(sky=["Sun 79%"], air=["O₂ <0.0002%"], life=["Largest: microbes ~0.01 mm"],
              check=[("Ice", "none")]),
    794: dict(sky=["Sun 95%", "Day 21.9 h", "Year 400 d"], air=["O₂ <4%"], life=["Largest: seaweeds ~1 cm"],
              check=[("Moon", "371,000 km (97%)"), ("Ice", "none")]),
    821: dict(sky=["Sun 96%", "Day 22.4 h", "Year 391 d"], air=["O₂ 13%", "CO₂ 9×", "Temp +8 °C"],
              life=["Families: sea 500 (45%)", "Plants: spores only"]),
    854: dict(sky=["Sun 97%", "Day 23.0 h", "Year 381 d"], air=["O₂ 25%", "CO₂ 1.3×", "Temp +3 °C"],
              life=["Families: sea 450 (40%), land 50 (10%)", "Plants: seed 60%"],
              check=[("Sea giant", "fish 7 m"), ("Land giant", "~300 kg"), ("Flier", "70 cm wings"),
                     ("Ice", "150%"), ("Moon", "375,000 km (98%)"), ("Sea level", "+50 m")]),
    855: dict(sky=["Sun 97%", "Day 23.0 h", "Year 381 d"], air=["O₂ 24%", "CO₂ 1.5×", "Temp +3 °C"],
              life=["Families: sea 440 (40%), land 55 (11%)", "Plants: seed 62%"]),
    905: dict(sky=["Sun 100%", "Day 23.8 h", "Year 368 d"], air=["O₂ 20%", "CO₂ 3.6×", "Temp +9 °C"],
              life=["Families: sea 1,000 (85%), land 300 (60%)", "Plants: flowering 75%"]),
    914: dict(sky=["Sun 100%", "Day 24.0 h", "Year 365 d"], air=["O₂ 21%", "CO₂ 1.0×", "Temp ±0 °C"],
              life=["Families: sea 1,200 (100%), land 500 (100%)", "Plants: flowering 90%"],
              check=[("Sea giant", "blue whale 30 m"), ("Land giant", "elephant 6 t"), ("Flier", "albatross 3.5 m wings"),
                     ("Ice", "100%"), ("Moon", "384,400 km"), ("Sea level", "0 m")]),
}

FOOTERS = r'''
#let slot-name(s) = text(size: 5pt, fill: luma(140), tracking: 0.08em, upper(s))
#let slot-items(xs) = if xs.len() == 0 { text(fill: luma(170))[–] } else { xs.join(" · ") }
#let SLOTS = (("sky", "Sky"), ("air", "Air & climate"), ("life", "Life"))
// Fixed-height footer, top-aligned: the bottom time label stays right under the ruler whatever is below it.
#let FH = (P.margin_bottom_mm - 2) * 1mm
#let label-row(p, recto) = sides(recto, text(weight: "bold", size: 9pt)[#p.bottom_label], physical-folio)

// Demo A: three fixed slots with tiny names, every page.
#let footer-a(p, recto) = block(height: FH, {
  label-row(p, recto)
  v(1.2mm)
  set text(size: small, fill: grey)
  set par(leading: 0.35em)
  grid(columns: (34%, 30%, 1fr), column-gutter: 2.5mm, row-gutter: 0.6mm,
    ..SLOTS.map(((k, n)) => slot-name(n)),
    ..SLOTS.map(((k, n)) => slot-items(p.demo.at(k))))
})

// Demo B: two plain lines every page (sky + air; life), plus a boxed check-in strip
// on pages that end on a round 100 Myr (every 20 pages: 14, 34, 54 ... 914).
#let bar = box(height: 0.7em, inset: (x: 1.2mm), line(angle: 90deg, length: 0.7em, stroke: 0.3pt + luma(150)))
#let footer-b(p, recto) = block(height: FH, {
  label-row(p, recto)
  v(1mm)
  {
    set text(size: small, fill: grey)
    set par(leading: 0.4em)
    let d = p.demo
    let row1 = (d.sky, d.air).filter(xs => xs.len() > 0).map(xs => xs.join(" · ")).join(bar)
    [#row1 \ #d.life.join(" · ")]
  }
  let ck = p.demo.at("check", default: none)
  if ck != none {
    v(1mm)
    set text(size: 6.2pt, fill: luma(40))
    block(width: 100%, stroke: 0.4pt + luma(120), inset: (x: 1.6mm, y: 1.1mm), radius: 0.6mm,
      grid(columns: 9, column-gutter: (2.5mm, 1mm, 3.5mm, 1mm, 3.5mm, 1mm, 3.5mm, 1mm), row-gutter: 0.9mm,
        grid.cell(rowspan: 2, align: horizon, text(size: 5pt, fill: luma(110), tracking: 0.08em, upper[100 Myr\ check-in])),
        ..ck.map(((k, v)) => (text(fill: luma(110))[#k], v)).flatten()))
  }
})

#let page-footer(p, recto) = if p.demo.variant == "A" { footer-a(p, recto) } else { footer-b(p, recto) }
'''


def main() -> int:
    cfg = C.config()
    data = build.build_data(PAGES, cfg, front=False, back=False)
    pages = []
    for variant in ("A", "B"):
        for p in data["pages"]:
            m = MOCK[p["n"]]
            demo = {"variant": variant, "sky": m["sky"], "air": m["air"], "life": m["life"]}
            if variant == "B" and "check" in m:
                demo["check"] = [list(x) for x in m["check"]]
            pages.append({**p, "metrics": [], "demo": demo})
    data["pages"] = pages
    (C.BUILD / "footer_demo.json").write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    src = (ROOT / "typeset" / "book.typ").read_text(encoding="utf-8")
    src = src.replace('json("/build/book.json")', 'json("/build/footer_demo.json")')
    src, n = re.subn(r"#let page-footer\(p, recto\) = .*?\n\}\)?\n", lambda _: FOOTERS, src, flags=re.S)
    assert n == 1, "page-footer not found in book.typ"
    tmp = ROOT / "typeset" / "_footer_demo.typ"
    tmp.write_text(src, encoding="utf-8")
    import typst
    try:
        from pypdf import PdfReader, PdfWriter
        pdf = C.BUILD / "footer_demo_full.pdf"
        typst.compile(str(tmp), output=str(pdf), root=str(ROOT))
        r, w = PdfReader(pdf), PdfWriter()
        for i in range(len(pages)):
            w.add_page(r.pages[i])
        w.write(OUT / "footer-demo.pdf")
        imgs = typst.compile(str(tmp), root=str(ROOT), format="png", ppi=200)[:len(pages)]
    finally:
        tmp.unlink()

    # Contact sheet of the bottom of each page: column A | column B, one row per page.
    from PIL import Image, ImageDraw
    ims = [Image.open(io.BytesIO(b)).convert("RGB") for b in imgs]
    w, h = ims[0].size
    strip_h = int(h * 0.16)
    k = len(PAGES)
    sheet = Image.new("RGB", (2 * w + 30, k * (strip_h + 12) + 50), "white")
    d = ImageDraw.Draw(sheet)
    d.text((10, 10), "A: slots every page", fill="black")
    d.text((w + 40, 10), "B: line every page + check-in box on round 100 Myr pages", fill="black")
    for i in range(k):
        for j in range(2):
            sheet.paste(ims[j * k + i].crop((0, h - strip_h, w, h)), (j * (w + 30), 40 + i * (strip_h + 12)))
    sheet.save(OUT / "footer-demo-strips.png")
    for i, im in enumerate(ims):
        im.save(C.BUILD / "png" / f"footer-demo-{'AB'[i // k]}-{PAGES[i % k]}.png") if (C.BUILD / "png").exists() else None
    print(f"{len(pages)} pages -> docs/sketches/footer-demo.pdf, footer-demo-strips.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
