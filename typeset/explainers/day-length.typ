// DRAFT one-page explainer: length of day and Earth–Moon distance.
// Reads the footer series data/series/day_length.json and moon_distance.json plus data/explainers/day-length.json.
// Compile: .venv/bin/python -c "import typst; typst.compile('typeset/explainers/day-length.typ', output='build/explainer-day-length.pdf', root='.')"
#import "lib.typ": *
#show: setup
#let D = json("/data/explainers/day-length.json")
#let DAY = json("/data/series/day_length.json")
#let MOON = json("/data/series/moon_distance.json")

#let T0 = -2600000000
#let xp(t) = W * (t - T0) / (0 - T0)
#let H1 = 46mm
#let dmin = 15.0
#let dmax = 25.0
#let yD(v) = H1 * (1 - (v - dmin) / (dmax - dmin))
#let H2 = 20mm
#let mmin = 310000
#let mmax = 390000
#let yM(v) = H2 * (1 - (v - mmin) / (mmax - mmin))

#header(D.title)

#let ox = 10mm
#box(width: W + 12mm, height: H1 + H2 + 14mm, {
  // ---- day length ----
  place(dx: ox, box(width: W, height: H1, {
    hgrid(yD, (16, 18, 20, 22, 24), W)
    // stall band
    let s = D.stall
    place(dx: xp(s.from), dy: yD(s.v + 0.4), rect(width: xp(s.to) - xp(s.from), height: yD(s.v - 0.4) - yD(s.v + 0.4), fill: luma(225), stroke: none))
    note(xp(s.from), yD(s.v + 0.4), [#s.label#cites(s.sources)], dx: 0mm, dy: -3mm)
    // cyclostratigraphy points (footer series), joined
    let pts = DAY.points.map(p => (xp(p.t), yD(p.v)))
    place(pline(pts, stroke: 0.7pt))
    for p in DAY.points { place(dx: xp(p.t) - 0.9mm, dy: yD(p.v) - 0.9mm, circle(radius: 0.9mm, fill: black)) }
    // rhythmites
    for r in D.rhythmites {
      let x = xp(r.t)
      if "t_err" in r { place(line(start: (xp(r.t - r.t_err), yD(r.v)), end: (xp(r.t + r.t_err), yD(r.v)), stroke: 0.4pt)) }
      place(dx: x - 0.9mm, dy: yD(r.v) - 0.9mm, circle(radius: 0.9mm, fill: white, stroke: 0.6pt))
    }
    note(xp(-2460000000), yD(16.98), [16.9 h, 2.46 Ga#cites(("lantink2022",))], dx: 1.5mm, dy: 0mm)
    note(xp(-1400000000), yD(18.7), [18.7 h#cites(("meyers2018",))], dx: 1mm, dy: 0.4mm)
    note(xp(-900000000), yD(18.9), [tidal layers, Utah#cites(("sonett1998",))], dx: -4mm, dy: 1.6mm)
    note(xp(-620000000), yD(21.9), [Elatina#cites(("williams2000",))], dx: -10mm, dy: -3.4mm)
    note(xp(0), yD(24), [24 h], dx: -6mm, dy: -3.4mm)
    place(rect(width: W, height: H1, stroke: 0.6pt))
  }))
  ylabel-col(yD, ((16, "16 h"), (18, "18"), (20, "20"), (22, "22"), (24, "24")), ox)
  // ---- Moon distance ----
  place(dx: ox, dy: H1 + 2mm, box(width: W, height: H2, {
    hgrid(yM, (320000, 350000, 380000), W)
    let pts = MOON.points.map(p => (xp(p.t), yM(p.v)))
    place(pline(pts, stroke: 0.7pt))
    for p in MOON.points { place(dx: xp(p.t) - 0.8mm, dy: yM(p.v) - 0.8mm, circle(radius: 0.8mm, fill: black)) }
    place(rect(width: W, height: H2, stroke: 0.6pt))
  }))
  place(dy: H1 + 2mm, ylabel-col(yM, ((320000, "320k"), (350000, "350k"), (380000, "380k km")), ox + 1mm))
  place(dx: ox + 1.5mm, dy: H1 + 2.5mm, text(size: 6pt, weight: "bold")[Moon's distance])
  xlabels(t => ox + xp(t), ((-2500000000, "−2.5 Ga"), (-2000000000, "−2.0"), (-1500000000, "−1.5"), (-1000000000, "−1.0"), (-500000000, "−0.5"), (0, "now")), H1 + H2 + 3mm)
  place(dx: ox, dy: H1 + H2 + 8mm, box(width: W, text(size: 6pt, fill: grey)[Filled dots: Milankovitch-cycle values, all recomputed with one tidal model#cites(("farhat2022",)) (the footer uses these). Open dots: tidal-layer counts. Straight lines between dots are interpolation, not data.]))
})

#v(1mm)
#sections(D)
#v(1mm)
#biblio()
