// The Lifetime of the Earth: main Typst document.
// Reads build/book.json, written by tools/build.py. Don't compile directly;
// run tools/build.py so the data and page selection are fresh.
//
// Sides: content page 1 is a right-hand page (recto). Odd content pages = recto: foredge on the RIGHT.
// Even = verso: foredge on the LEFT. The ruler, time labels and foredge band always sit on the foredge side.

#let D = json("/build/book.json")
#let cfg = D.config
#let P = cfg.page
#let FE = cfg.foredge
#let PW = P.width_mm * 1mm
#let PH = P.height_mm * 1mm
#let H = D.body_height_mm * 1mm
#let W = (P.width_mm - P.margin_inside_mm - P.margin_outside_mm) * 1mm
#let rw = cfg.layout.ruler_width_mm * 1mm
#let grey = luma(90)
#let small = 6.8pt

#set document(title: cfg.title)
#set page(width: PW, height: PH, margin: (
  inside: P.margin_inside_mm * 1mm, outside: P.margin_outside_mm * 1mm,
  top: P.margin_top_mm * 1mm, bottom: P.margin_bottom_mm * 1mm,
))
#set text(font: cfg.type.font, size: cfg.type.size_pt * 1pt, lang: "en")
#set par(leading: 0.55em, spacing: 0.6em)

// Ordinary page number: deliberately quieter than the time labels and metrics.
#let physical-folio = context text(size: 6.5pt, fill: luma(140))[#here().page()]

// ---------------- front matter ----------------
#if D.front {
  page(margin: 25mm)[
    #v(1fr)
    #align(center)[
      #text(size: 24pt)[#cfg.title]
      #v(6mm)
      #text(size: 11pt, style: "italic")[#cfg.subtitle]
    ]
    #v(2fr)
    #align(center, text(size: 7pt, fill: grey)[Build #D.built · #D.pages.len() of #D.total_content_pages content pages])
  ]
  page(footer: align(center, physical-folio))[
    #heading(level: 1, outlined: false)[Contents]
    #v(4mm)
    #context {
      let marks = query(<unit-start>)
      if marks.len() == 0 [_No unit boundaries in this build._]
      for m in marks [
        #box(width: 1fr)[#m.value.name #box(width: 1fr, repeat[.])] #counter(page).at(m.location()).first() \
      ]
    }
    #v(8mm)
    #heading(level: 2, outlined: false)[How to read this book]
    Each page covers five million years. Time runs down the page and forward through the book:
    the number at the top of a page is the moment it begins; the number at the bottom, the moment it ends
    (in years relative to the present). Superscript numbers refer to the bibliography; superscript italic letters
    beside drawings refer to the image credits.
  ]
  pagebreak(to: "odd", weak: true)
}

// ---------------- content pages ----------------
#let cites(keys) = keys.map(k => cite(label(k))).join()
// Minimal markup for data text: _Genus species_ -> italics.
#let rich(s) = s.split("_").enumerate().map(((i, x)) => if calc.odd(i) { emph(x) } else { [#x] }).join()
// Image credits (decision #40): italic superscript letters after the caption's numbered cites -> Image credits list.
#let art-letters(art) = {
  let ls = art.at("letters", default: ())
  if ls.len() > 0 { super[#if art.sources.len() > 0 [,]#emph(ls.join(","))] }
}

// Mirror helper: a = item for the foredge side, b = item for the spine side.
#let sides(recto, fore, spine) = if recto {
  grid(columns: (1fr, auto), align: (left + bottom, right + bottom), spine, fore)
} else {
  grid(columns: (auto, 1fr), align: (left + bottom, right + bottom), fore, spine)
}

#let page-header(p, recto) = {
  set text(size: 7.5pt)
  sides(recto,
    text(weight: "bold", size: 9pt)[#p.top_label],
    text(style: "italic", fill: grey)[#p.units.join(" · ")],
  )
}

#let metric(m) = [#m.label #m.value#m.unit#cites(m.sources)]
#let in-slot(p, k) = p.metrics.filter(m => m.at("slot", default: "sky") == k)
#let rule-bar = box(height: 0.7em, inset: (x: 1.2mm), line(angle: 90deg, length: 0.7em, stroke: 0.3pt + luma(150)))

// Footer (decision #45): fixed height and top-aligned, so the bottom time label always sits right under the ruler.
// Line 1 = sky · air, line 2 = life (each only where values exist); on pages ending on a round 100 Myr,
// a boxed check-in strip below.
#let page-footer(p, recto) = block(height: (P.margin_bottom_mm - 2) * 1mm, {
  sides(recto, text(weight: "bold", size: 9pt)[#p.bottom_label], physical-folio)
  v(1mm)
  {
    set text(size: small, fill: grey)
    set par(leading: 0.4em)
    let groups = ("sky", "air").map(k => in-slot(p, k)).filter(ms => ms.len() > 0)
    let life = in-slot(p, "life")
    if groups.len() > 0 { groups.map(ms => ms.map(metric).join[ · ]).join(rule-bar) }
    if life.len() > 0 { linebreak(); life.map(metric).join[ · ] }
  }
  let ck = in-slot(p, "checkin")
  if p.at("checkin", default: false) and ck.len() > 0 {
    v(1mm)
    set text(size: 6.2pt, fill: luma(40))
    block(width: 100%, stroke: 0.4pt + luma(120), inset: (x: 1.6mm, y: 1.1mm), radius: 0.6mm,
      grid(columns: 9, column-gutter: (2.5mm, 1mm, 3.5mm, 1mm, 3.5mm, 1mm, 3.5mm, 1mm), row-gutter: 0.9mm,
        grid.cell(rowspan: calc.max(1, calc.ceil(ck.len() / 4)), align: horizon,
          text(size: 5pt, fill: luma(110), tracking: 0.08em, upper[100 Myr\ check-in])),
        ..ck.map(m => (text(fill: luma(110))[#m.label], [#m.value#m.unit#cites(m.sources)])).flatten()))
  }
})

// Foredge band label: lines stacked and centred, scaled down (never up) so the rotated block is at most
// `len` long (along the edge) and `across` deep (into the page), then rotated by `angle`.
#let fe-label(lines, len, across, angle) = context {
  let body(sz) = grid(align: center, row-gutter: 0.18em,
    ..lines.map(l => text(size: sz, fill: white, weight: "bold", l)))
  let base = FE.label_size_pt * 1pt
  let m = measure(body(base))
  let s = calc.min(1.0, len / m.width, across / m.height)
  rotate(angle, reflow: true, body(base * s))
}

// Foredge band + trim ticks, drawn on the full page (background layer, outside the margins).
#let page-background(p, recto) = {
  let bw = FE.band_width_mm * 1mm
  let trim = FE.trim_mm * 1mm
  if p.foredge_slot != none {
    let span = PH - (FE.inset_top_mm + FE.inset_bottom_mm) * 1mm
    let sh = span / D.foredge_slots
    let y = FE.inset_top_mm * 1mm + sh * p.foredge_slot
    let x = if recto { PW - bw } else { -3mm }   // bleed off the page edge
    place(top + left, dx: x, dy: y, rect(width: bw + 3mm, height: sh, fill: luma(FE.grey), stroke: none))
    // Label: white, set vertically in the part of the band that survives the trim. Tops of the letters
    // face the foredge on both sides (recto reads downward, verso upward). Shrunk to fit the slot.
    let vis = bw - trim
    let lx = if recto { PW - bw } else { trim }
    place(top + left, dx: lx, dy: y, box(width: vis, height: sh, align(center + horizon,
      fe-label(p.foredge_label, sh * 0.9, vis * 0.8, if recto { 90deg } else { -90deg }))))
  }
  // trim ticks (top & bottom) where the plough will cut
  let tx = if recto { PW - trim } else { trim }
  for (y0, y1) in ((0mm, 5mm), (PH - 5mm, PH)) {
    place(top + left, line(start: (tx, y0), end: (tx, y1), stroke: 0.3pt + luma(120)))
  }
}

#let ruler-x(recto) = if recto { W - rw * 0.45 } else { rw * 0.45 }
#let ruler(recto) = {
  let x = ruler-x(recto)
  let dir = if recto { 1 } else { -1 }   // ticks point toward the foredge
  place(top + left, line(start: (x, 0pt), end: (x, H), stroke: 0.7pt))
  for i in range(0, 51) {           // tick every 100,000 years
    let y = H * i / 50
    let len = if calc.rem(i, 10) == 0 { rw * 0.45 } else if calc.rem(i, 5) == 0 { rw * 0.3 } else { rw * 0.15 }
    place(top + left, line(start: (x, y), end: (x + dir * len, y), stroke: 0.35pt))
  }
}

#let event-block(e) = {
  if e.at("kind", default: "event") == "boundary" [
    #text(weight: "bold")[#e.title]
    #h(0.3em) #box(text(size: 0.85em, fill: grey)[#e.when])\
    #text(size: 0.85em, style: "italic")[#e.text#cites(e.sources)]
  ] else [
    #text(weight: "bold")[#rich(e.title)]
    #h(0.3em) #box(text(size: 0.85em, fill: grey)[#e.when])\
    #rich(e.text)#cites(e.sources)
    #if e.art != none {
      v(1mm)
      grid(columns: (auto, 1fr), column-gutter: 3mm, align: (left + top, left + horizon),
        image("/art/" + e.art.file, height: cfg.layout.art_height_mm * 1mm),
        text(size: 0.8em, fill: luma(60))[#rich(e.art.at("caption", default: ""))#cites(e.art.sources)#art-letters(e.art)])
    }
  ]
}

#for p in D.pages {
  let recto = calc.odd(p.n)
  let (ml, mr) = if recto { (P.margin_inside_mm, P.margin_outside_mm) } else { (P.margin_outside_mm, P.margin_inside_mm) }
  page(
    margin: (left: ml * 1mm, right: mr * 1mm, top: P.margin_top_mm * 1mm, bottom: P.margin_bottom_mm * 1mm),
    header: page-header(p, recto), header-ascent: 2.5mm,
    footer: page-footer(p, recto), footer-descent: 2mm,
    background: page-background(p, recto),
  )[
    #block(width: 100%, height: H, {
      ruler(recto)
      let rx = ruler-x(recto)
      for u in p.unit_starts [#metadata((name: u, n: p.n))<unit-start>]
      let col-w = W - rw - 1.5mm
      let col-x = if recto { 0mm } else { rw + 1.5mm }
      let edge = if recto { col-w } else { col-x }   // text edge nearest the ruler
      for e in p.events {
        let ay = e.anchor_mm * 1mm
        let ey = e.y_mm * 1mm
        let boundary = e.at("kind", default: "event") == "boundary"
        if boundary {   // heavy tick across the ruler
          place(top + left, line(start: (rx - rw * 0.45, ay), end: (rx + rw * 0.45, ay), stroke: 1.2pt))
        }
        // leader ends level with the anchor when the block spans it, else at the block's nearest end
        let ty = calc.max(ey + 1.6mm, calc.min(ay, ey + e.h_mm * 1mm - 1.6mm))
        place(top + left, line(start: (rx, ay), end: (edge, ty), stroke: 0.4pt + if boundary { grey } else { black }))
        place(top + left, dx: col-x, dy: ey, box(width: col-w, event-block(e)))
      }
    })
  ]
}

// ---------------- back matter ----------------
// The bibliography is always typeset (Typst requires it whenever anything is cited). full: true lists every
// source, so partial builds still show the whole list. Dense: two columns, small type.
#set page(footer: align(center, physical-folio), margin: (inside: 16mm, outside: 12mm, top: 14mm, bottom: 14mm))

// One-page explainer of the eon and era names (data/explainers/timescale-names.json), in foredge-tab order.
#if D.at("timescale_names", default: none) != none {
  let X = D.timescale_names
  set text(size: 8pt)
  set par(leading: 0.5em, spacing: 0.8em)
  text(size: 14pt, weight: "bold")[#X.title]
  v(1mm)
  line(length: 100%, stroke: 0.5pt)
  v(1mm)
  for para in X.paragraphs { par[#rich(para.text)#cites(para.sources)] }
  v(2mm)
  let tab = box(width: 4mm, height: 2.6mm, baseline: 0.3mm, fill: luma(FE.grey))
  let cells = ()
  for r in X.rows {
    let eon = r.rank == "eon"
    let has-tab = D.at("foredge_bands", default: ()).contains(r.unit)
    cells += (
      if has-tab { tab } else [],
      if eon { text(weight: "bold")[#r.unit Eon] } else { h(3mm) + [#r.unit Era] },
      text(fill: grey, size: 0.9em)[#r.start_label],
      [#rich(r.meaning)#cites(r.sources)],
    )
  }
  table(columns: (auto, auto, auto, 1fr), stroke: none, inset: (x: 1.2mm, y: 1.1mm),
    align: (left + top, left + top, right + top, left + top),
    table.header(
      [], text(size: 0.9em, style: "italic")[Unit], text(size: 0.9em, style: "italic")[Began (years)],
      text(size: 0.9em, style: "italic")[Meaning]),
    table.hline(stroke: 0.4pt),
    ..cells)
  v(1mm)
  text(size: 0.9em, fill: grey)[Grey marks show which units have a foredge tab; the rows run in the same order as the
    tabs, top to bottom. The Precambrian era names add a prefix to their eon: _Eo-_ dawn, _Paleo-_ old, _Meso-_ middle,
    _Neo-_ new.]
  pagebreak()
}

#{
  set text(size: cfg.bibliography.size_pt * 1pt)
  set par(leading: 0.4em, spacing: 0.45em)
  show heading: set text(size: 11pt)
  heading(level: 1, outlined: false)[Bibliography]
  columns(cfg.bibliography.columns, gutter: 4mm,
    bibliography("/data/sources.bib", title: none, full: true, style: cfg.bibliography.style))
  // Image credits: a separate, lettered list built by tools/build.py from art/credits.json (all images in the book).
  if D.at("image_credits", default: ()).len() > 0 {
    v(4mm)
    heading(level: 1, outlined: false)[Image credits]
    [Drawings are cited by superscript italic letters. Unless noted, each is a silhouette from PhyloPic, redrawn here
    as an outline; the link is its page there.]
    v(1mm)
    columns(cfg.bibliography.columns, gutter: 4mm,
      grid(columns: (auto, 1fr), column-gutter: 1.5mm, row-gutter: 0.6em,
        ..D.image_credits.map(c => (
          emph(c.letter),
          [#c.attribution. #rich(c.title).#if c.note != "" [ #c.note.]#if c.license != "" [ #box(c.license.replace(" ", "\u{a0}")).]#if c.url != "" [\ #text(size: 0.85em, fill: luma(90), c.url)]],
        )).flatten()))
  }
}
