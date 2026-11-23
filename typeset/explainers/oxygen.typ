// DRAFT: one-page explainer for a footer metric (oxygen). Reads data/explainers/oxygen.json.
// Compile: .venv/bin/python -c "import typst; typst.compile('typeset/explainers/oxygen.typ', output='build/explainer-oxygen.pdf', root='.')"
#let D = json("/data/explainers/oxygen.json")
#let cfg = json("/config.json")
#let P = cfg.page
#set page(width: P.width_mm * 1mm, height: P.height_mm * 1mm,
  margin: (inside: P.margin_inside_mm * 1mm, outside: P.margin_outside_mm * 1mm, top: 14mm, bottom: 16mm))
#set text(font: cfg.type.font, size: 8pt)
#set par(leading: 0.5em, spacing: 0.7em, justify: false)
#let grey = luma(110)
#let cites(keys) = keys.map(k => cite(label(k))).join()

// ---- chart geometry: x linear in time, y log10(% O2) ----
#let W = 100mm
#let H = 62mm
#let T0 = -4570000000
#let ymin = -5.0   // 10^-5 %
#let ymax = 2.0    // 100 %
#let xp(t) = W * (t - T0) / (0 - T0)
#let yp(v) = H * (1 - (calc.log(v, base: 10) - ymin) / (ymax - ymin))

#text(size: 14pt, weight: "bold")[#D.title]
#h(1fr) #text(size: 7.5pt, fill: grey)[Footer metric explainer · draft]
#v(1mm)
#line(length: 100%, stroke: 0.5pt)
#v(2mm)

#box(width: W + 14mm, height: H + 12mm, {
  let ox = 12mm
  place(dx: ox, dy: 0mm, box(width: W, height: H, {
    // grid lines at each power of ten
    for e in range(-5, 3) {
      let y = yp(calc.pow(10.0, e))
      place(line(start: (0mm, y), end: (W, y), stroke: 0.25pt + luma(200)))
    }
    // eon boundaries
    for b in (-4031000000, -2500000000, -538800000) {
      place(line(start: (xp(b), 0mm), end: (xp(b), H), stroke: (paint: luma(170), thickness: 0.3pt, dash: "dotted")))
    }
    for it in D.items {
      if it.kind == "ceiling" {
        let y = yp(it.hi)
        place(line(start: (xp(it.from), y), end: (xp(it.to), y), stroke: 1.4pt))
        let xm = (xp(it.from) + xp(it.to)) / 2
        place(line(start: (xm, y), end: (xm, y + 5mm), stroke: 0.8pt))
        place(dx: xm - 1.2mm, dy: y + 4mm, polygon(fill: black, (0mm, 0mm), (2.4mm, 0mm), (1.2mm, 1.8mm)))
        place(dx: xp(it.from), dy: y - 3.6mm, text(size: 6.5pt)[#it.label#cites(it.sources)])
      } else if it.kind == "floor" {
        let y = yp(it.lo)
        let x = xp(it.t)
        place(line(start: (x - 2mm, y), end: (x + 2mm, y), stroke: 1.4pt))
        place(line(start: (x, y), end: (x, y - 5mm), stroke: 0.8pt))
        place(dx: x - 1.2mm, dy: y - 6mm, polygon(fill: black, (0mm, 1.8mm), (2.4mm, 1.8mm), (1.2mm, 0mm)))
        place(dx: x + 2.5mm, dy: y - 1.5mm, text(size: 6.5pt)[#it.label#cites(it.sources)])
      } else if it.kind == "range" {
        place(dx: xp(it.from), dy: yp(it.hi), rect(width: xp(it.to) - xp(it.from), height: yp(it.lo) - yp(it.hi), fill: luma(215), stroke: none))
      } else if it.kind == "point" {
        place(dx: xp(it.t) - 0.9mm, dy: yp(it.v) - 0.9mm, circle(radius: 0.9mm, fill: black))
      } else if it.kind == "mark" {
        place(line(start: (xp(it.t), 0mm), end: (xp(it.t), H), stroke: 0.5pt + grey))
        place(dx: xp(it.t) - 2.6mm, dy: H - 2mm, rotate(-90deg, origin: bottom + left, reflow: false,
          text(size: 6pt, fill: grey)[#it.label#cites(it.sources)]))
      }
    }
    // today
    let yt = yp(D.today.v)
    place(dx: W - 1mm, dy: yt - 1mm, circle(radius: 1mm, fill: white, stroke: 1pt))
    place(dx: W - 26mm, dy: yt + 5mm, text(size: 6.5pt)[today 20.95%#cites(D.today.sources)])
    // frame
    place(rect(width: W, height: H, stroke: 0.6pt))
  }))
  // y labels
  for e in range(-5, 3) {
    let y = yp(calc.pow(10.0, e))
    let lab = if e >= 0 { str(calc.pow(10, e)) + "%" } else { "10" + super(str(e)) + "%" }
    place(dx: 0mm, dy: y - 1.4mm, box(width: ox - 1.5mm, align(right, text(size: 6pt)[#lab])))
  }
  // x labels
  for g in (4, 3, 2, 1, 0) {
    let x = ox + xp(-g * 1000000000)
    place(dx: x - 4mm, dy: H + 1.5mm, box(width: 8mm, align(center, text(size: 6pt)[#if g == 0 [now] else [−#g Ga]])))
  }
  place(dx: ox, dy: H + 6mm, text(size: 6pt, fill: grey)[Bars with arrows are upper or lower limits; grey band: range allowed by fossil charcoal.])
})

#v(2mm)
#for s in D.sections [
  #text(weight: "bold")[#s.head.] #s.text#cites(s.sources)

]
#v(2mm)
#text(size: 6.5pt, fill: grey)[In the timeline footer this metric would print a value only where a cited value or range exists; elsewhere it stays blank.]

#set text(size: 5.5pt)
#set par(leading: 0.35em, spacing: 0.4em)
#columns(2, gutter: 3mm, bibliography("/data/sources.bib", title: none, style: cfg.bibliography.style))
