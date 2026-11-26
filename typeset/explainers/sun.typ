// DRAFT one-page explainer: solar luminosity over 4.57 Gyr (Gough 1981 formula, as in the footer).
// Reads data/explainers/sun.json. The curve is computed here from the same formula as tools/models.py.
// Compile: .venv/bin/python -c "import typst; typst.compile('typeset/explainers/sun.typ', output='build/explainer-sun.pdf', root='.')"
#import "lib.typ": *
#show: setup
#let D = json("/data/explainers/sun.json")

#let A = D.age_now
#let L(t) = 100 / (1 + 0.4 * (1 - (A + t) / A))
// inverse: year at which the Sun reached p percent
#let tof(p) = -A * (100 / p - 1) / 0.4

#let T0 = -4700000000
#let Wl = 86mm   // narrower than W to leave room for the right-hand W/m² scale
#let xp(t) = Wl * (t - T0) / (0 - T0)
#let H = 54mm
#let ymin = 62.0
#let ymax = 102.0
#let yp(v) = H * (1 - (v - ymin) / (ymax - ymin))

#header(D.title)

#let ox = 10mm
#box(width: Wl + 17mm, height: H + 13mm, {
  place(dx: ox, box(width: Wl, height: H, {
    // faint-young-Sun zone
    let z = D.zone
    place(dx: xp(z.from), rect(width: xp(z.to) - xp(z.from), height: H, fill: luma(232), stroke: none))
    place(dx: xp(z.from) + 1.5mm, dy: 2mm, box(width: xp(z.to) - xp(z.from) - 3mm,
      text(size: 6pt)[#z.label#cites(z.sources)]))
    hgrid(yp, (70, 80, 90, 100), Wl)
    // luminosity curve
    let pts = range(0, 92).map(i => { let t = -A + i * 50000000; (xp(calc.min(t, 0)), yp(L(calc.min(t, 0)))) })
    place(pline(pts, stroke: 1.1pt))
    place(dx: xp(-A) - 0.9mm, dy: yp(L(-A)) - 0.9mm, circle(radius: 0.9mm, fill: black))
    note(xp(-A), yp(L(-A)), [71% · 4.57 Ga], dx: 1.5mm, dy: 0.9mm)
    // milestones
    for p in D.milestones {
      let t = tof(p)
      place(dx: xp(t) - 0.8mm, dy: yp(p) - 0.8mm, circle(radius: 0.8mm, fill: white, stroke: 0.6pt))
      let lab = str(calc.round(-t / 1e9, digits: 1)) + " Ga"
      note(xp(t), yp(p), [#p% · #lab], dx: 1.2mm, dy: 0.8mm)
    }
    // evidence of liquid water: small up-triangles under the curve
    for w in D.water {
      let x = xp(w.t)
      place(dx: x - 1mm, dy: H - 8mm, polygon(fill: none, stroke: 0.5pt, (0mm, 1.6mm), (2mm, 1.6mm), (1mm, 0mm)))
    }
    note(xp(D.water.at(0).t), H - 8mm, [#D.water.at(0).label#cites(D.water.at(0).sources)], dx: -1mm, dy: 1.8mm, size: 5.5pt)
    note(xp(D.water.at(1).t), H - 8mm, [#D.water.at(1).label#cites(D.water.at(1).sources)], dx: 1.6mm, dy: -0.3mm, size: 5.5pt)
    // ice ages: black bars along the bottom
    for g in D.ice {
      let w = calc.max(xp(g.to) - xp(g.from), 0.8mm)
      place(dx: xp(g.from), dy: H - 3.2mm, rect(width: w, height: 3.2mm, fill: black, stroke: none))
    }
    note(xp(D.ice.at(0).from), H - 3.2mm, [#D.ice.at(0).label], dx: -9.5mm, dy: -0.4mm, size: 5.5pt)
    note(xp(D.ice.at(1).to), H - 3.2mm, [#D.ice.at(1).label ice], dx: 1mm, dy: -0.4mm, size: 5.5pt)
    note(xp(D.ice.at(2).to), H - 3.2mm, [Snowball#cites(D.ice.at(2).sources)], dx: 1.2mm, dy: -0.4mm, size: 5.5pt)
    place(rect(width: Wl, height: H, stroke: 0.6pt))
  }))
  ylabel-col(yp, ((70, "70%"), (80, "80"), (90, "90"), (100, "100")), ox)
  // right axis: sunlight at Earth, W/m2
  for wm in (1000, 1100, 1200, 1300) {
    let p = 100 * wm / D.solar_constant
    place(dx: ox + Wl + 1.2mm, dy: yp(p) - 1.4mm, text(size: 6pt, fill: grey)[#wm])
  }
  place(dx: ox + Wl + 1.2mm, dy: yp(100) - 1.4mm, text(size: 6pt, fill: grey)[1361]); place(dx: ox + Wl + 1.2mm, dy: yp(100) - 4.6mm, text(size: 6pt, fill: grey)[W/m²])
  xlabels(t => ox + xp(t), ((-4500000000, "−4.5 Ga"), (-3500000000, "−3.5"), (-2500000000, "−2.5"), (-1500000000, "−1.5"), (-500000000, "−0.5"), (0, "now")), H + 1.5mm)
  place(dx: ox, dy: H + 6mm, box(width: Wl, text(size: 6pt, fill: grey)[Brightness of the Sun as a share of today's, from the standard model of how stars age#cites(("gough1981", "feulner2012")); the footer prints the same numbers. Right: sunlight arriving at Earth, in watts per square metre. Black bars: ice ages#cites(("feulner2012", "hoffman2017")).]))
})

#v(2mm)
#sections(D)
#v(1mm)
#biblio()
