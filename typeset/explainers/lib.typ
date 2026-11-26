// Shared frame for the one-page metric explainers (draft). Each explainer imports this, draws its own chart,
// then calls body(D). Page geometry comes from config.json so a page compiles at the book's trim size.
#let cfg = json("/config.json")
#let P = cfg.page
#let grey = luma(110)
#let light = luma(200)
#let W = 100mm   // chart width (text block is ~102.7 mm)

#let cites(keys) = keys.map(k => cite(label(k))).join()

// _underscores_ -> italics, as in event text.
#let rich(s) = {
  let parts = s.split("_")
  for (i, p) in parts.enumerate() { if calc.odd(i) { emph(p) } else { p } }
}

#let setup(doc) = {
  set page(width: P.width_mm * 1mm, height: P.height_mm * 1mm,
    margin: (inside: P.margin_inside_mm * 1mm, outside: P.margin_outside_mm * 1mm, top: 14mm, bottom: 16mm))
  set text(font: cfg.type.font, size: 8pt)
  set par(leading: 0.5em, spacing: 0.7em, justify: false)
  doc
}

#let header(title) = {
  text(size: 14pt, weight: "bold")[#title]
  h(1fr)
  text(size: 7.5pt, fill: grey)[Footer metric explainer · draft]
  v(1mm)
  line(length: 100%, stroke: 0.5pt)
  v(2mm)
}

// Time axis labels under a chart of width w spanning t0..t1 (years, negative); ticks = list of (t, label).
#let xlabels(xp, ticks, y) = for (t, lab) in ticks {
  place(dx: xp(t) - 5mm, dy: y, box(width: 10mm, align(center, text(size: 6pt)[#lab])))
}

#let ylabel-col(yp, ticks, w) = for (v, lab) in ticks {
  place(dx: 0mm, dy: yp(v) - 1.4mm, box(width: w - 1.5mm, align(right, text(size: 6pt)[#lab])))
}

#let hgrid(yp, vals, w) = for v in vals {
  place(line(start: (0mm, yp(v)), end: (w, yp(v)), stroke: 0.25pt + light))
}

// Short text label with a leader-free placement; `anchor` is the data point in chart coordinates.
#let note(x, y, body, dx: 1.5mm, dy: -1.6mm, size: 6pt, fill: black) = place(dx: x + dx, dy: y + dy, text(size: size, fill: fill, body))

#let sections(D) = {
  for s in D.sections [
    #text(weight: "bold")[#s.head.] #rich(s.text)#cites(s.sources)

  ]
}

#let biblio() = {
  set text(size: 5.5pt)
  set par(leading: 0.35em, spacing: 0.4em)
  columns(2, gutter: 3mm, bibliography("/data/sources.bib", title: none, style: cfg.bibliography.style))
}

// Open polyline and filled polygon (the old `path` element is gone in this Typst).
#let pline(pts, stroke: 0.8pt) = curve(stroke: stroke, fill: none, curve.move(pts.at(0)), ..pts.slice(1).map(p => curve.line(p)))
#let pfill(pts, fill: luma(220)) = polygon(fill: fill, stroke: none, ..pts)
