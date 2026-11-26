// DRAFT one-page explainer: marine animal genera through the Phanerozoic. Reads data/explainers/diversity.json.
// Compile: .venv/bin/python -c "import typst; typst.compile('typeset/explainers/diversity.typ', output='build/explainer-diversity.pdf', root='.')"
#import "lib.typ": *
#show: setup
#let D = json("/data/explainers/diversity.json")

#let H = 70mm
#let T0 = -545000000
#let ymax = 6000
#let xp(t) = W * (t - T0) / (0 - T0)
#let yp(v) = H * (1 - v / ymax)

#header(D.title)

#box(width: W + 12mm, height: H + 12mm, {
  let ox = 10mm
  place(dx: ox, box(width: W, height: H, {
    hgrid(yp, (1000, 2000, 3000, 4000, 5000), W)
    // period boundaries (GTS2020 rounded) as faint ticks with letters at top
    for (t, p) in ((-538800000, "Cm"), (-485400000, "O"), (-443800000, "S"), (-419200000, "D"), (-358900000, "C"),
                   (-298900000, "P"), (-251900000, "Tr"), (-201400000, "J"), (-145000000, "K"), (-66000000, "Pg"), (-23030000, "N")) {
      place(line(start: (xp(t), 0mm), end: (xp(t), 1.5mm), stroke: 0.3pt + grey))
      place(dx: xp(t) + 0.4mm, dy: 0.3mm, text(size: 5pt, fill: grey)[#p])
    }
    // diversity as a step line (skip the Ediacaran bin before T0)
    let pts = ()
    for s in D.steps {
      if s.at(1) <= T0 { continue }
      let a = calc.max(s.at(0), T0)
      pts.push((xp(a), yp(s.at(2))))
      pts.push((xp(s.at(1)), yp(s.at(2))))
    }
    place(pline(pts, stroke: 0.9pt + black))
    // fill under the curve, light
    place(pfill((..pts, (xp(0), H), (xp(T0), H)), fill: luma(232)))
    place(pline(pts, stroke: 0.9pt + black))
    // the Big Five
    for m in D.marks {
      let x = xp(m.t)
      place(line(start: (x, 9mm), end: (x, H), stroke: (paint: grey, thickness: 0.4pt, dash: "dashed")))
      place(dx: x - 1.2mm, dy: 4mm, polygon(fill: black, (0mm, 0mm), (2.4mm, 0mm), (1.2mm, 1.8mm)))
    }
    note(xp(-443800000), 9mm, [End-Ordovician \ #D.marks.at(0).lost_pct%], dx: -16mm, dy: 0mm)
    note(xp(-358900000), 9mm, [Late Devonian \ #D.marks.at(1).lost_pct%], dx: 1mm, dy: 0mm)
    note(xp(-251902000), 20mm, [End-Permian \ #D.marks.at(2).lost_pct%], dx: -14mm, dy: 0mm)
    note(xp(-201400000), 9mm, [End-Triassic \ #D.marks.at(3).lost_pct%], dx: 1mm, dy: 0mm)
    note(xp(-66000000), 20mm, [End-Cretaceous \ #D.marks.at(4).lost_pct%], dx: -17mm, dy: 0mm)
    place(rect(width: W, height: H, stroke: 0.6pt))
  }))
  ylabel-col(v => yp(v), ((0, "0"), (1000, "1,000"), (2000, "2,000"), (3000, "3,000"), (4000, "4,000"), (5000, "5,000"), (6000, "6,000")), ox)
  xlabels(t => ox + xp(t), ((-500000000, "−500 Ma"), (-400000000, "−400"), (-300000000, "−300"), (-200000000, "−200"), (-100000000, "−100"), (0, "now")), H + 1.5mm)
  place(dx: ox, dy: H + 6mm, box(width: W, text(size: 6pt, fill: grey)[Genera of sea animals known from each interval#cites(D.sources). Dashed lines: the five mass extinctions, with the share of genera last seen in the stage before each.]))
})

#v(2mm)
#sections(D)
#v(1mm)
#biblio()
