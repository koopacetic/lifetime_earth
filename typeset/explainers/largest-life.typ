// DRAFT one-page explainer: maximum size of life over 3.5 Gyr. Reads data/explainers/largest-life.json.
// PLACEHOLDER curve until Payne et al. 2009 Table S1 values replace the text-derived steps (see the JSON _doc).
// Compile: .venv/bin/python -c "import typst; typst.compile('typeset/explainers/largest-life.typ', output='build/explainer-largest-life.pdf', root='.')"
#import "lib.typ": *
#show: setup
#let D = json("/data/explainers/largest-life.json")

#let T0 = -3700000000
#let xp(t) = W * (t - T0) / (0 - T0)
#let H = 66mm
#let ymax = 17.0
#let yp(v) = H * (1 - v / ymax)

#header(D.title)

#let ox = 10mm
#box(width: W + 12mm, height: H + 13mm, {
  place(dx: ox, box(width: W, height: H, {
    hgrid(yp, (0, 4, 8, 12, 16), W)
    for m in D.oxygen_marks {
      place(line(start: (xp(m.t), 0mm), end: (xp(m.t), H), stroke: (paint: grey, thickness: 0.4pt, dash: "dashed")))
      place(dx: xp(m.t) - 2.6mm, dy: H - 2mm, rotate(-90deg, origin: bottom + left, reflow: false,
        text(size: 5.5pt, fill: grey)[#m.label#cites(m.sources)]))
    }
    // staircase: hold each value until the next step's time; the 600->450 Ma rise is drawn as a ramp
    let s = D.steps
    let pts = ((xp(s.at(0).t), yp(s.at(0).v)), (xp(s.at(1).t), yp(s.at(0).v)), (xp(s.at(1).t), yp(s.at(1).v)),
               (xp(s.at(2).t), yp(s.at(2).v)), (xp(s.at(3).t), yp(s.at(3).v)), (xp(s.at(4).t), yp(s.at(4).v)))
    place(pline(pts, stroke: 1.1pt))
    for p in s { place(dx: xp(p.t) - 0.9mm, dy: yp(p.v) - 0.9mm, circle(radius: 0.9mm, fill: black)) }
    note(xp(s.at(0).t), yp(0), rich(s.at(0).label), dx: 1mm, dy: -3.4mm)
    note(xp(s.at(1).t), yp(6), [#emph[Grypania] \ (first eukaryotic \ macrofossils)], dx: 1.5mm, dy: 1.2mm, size: 5.5pt)
    note(xp(s.at(2).t), yp(7), rich(s.at(2).label), dx: -24mm, dy: -4.2mm)
    note(xp(s.at(3).t), yp(13), rich(s.at(3).label), dx: -25mm, dy: -1.6mm)
    note(xp(0), yp(16), rich(s.at(4).label), dx: -17mm, dy: -3.6mm)
    let e = D.extra.at(0)
    place(dx: xp(e.t) - 0.9mm, dy: yp(e.v) - 0.9mm, circle(radius: 0.9mm, fill: white, stroke: 0.6pt))
    note(xp(0), yp(e.v), e.label, dx: -16mm, dy: -1.4mm)
    place(rect(width: W, height: H, stroke: 0.6pt))
  }))
  ylabel-col(yp, ((0, "1"), (4, "10⁴"), (8, "10⁸"), (12, "10¹²"), (16, "10¹⁶")), ox)
  xlabels(t => ox + xp(t), ((-3500000000, "−3.5 Ga"), (-3000000000, "−3"), (-2000000000, "−2"), (-1000000000, "−1"), (0, "now")), H + 1.5mm)
  place(dx: ox, dy: H + 6mm, box(width: W, text(size: 6pt, fill: grey)[Volume of the largest known living thing, relative to the largest fossils 3.5 billion years ago (log scale)#cites(("payne2009",)). Draft: steps read from the paper's text.]))
})

#v(2mm)
#sections(D)
#v(1mm)
#biblio()
