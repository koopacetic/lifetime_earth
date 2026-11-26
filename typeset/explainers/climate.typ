// DRAFT one-page explainer: global temperature and CO2 over 485 Myr (PhanDA) with an LR04 glacial-cycle inset.
// Reads data/explainers/climate.json.
// Compile: .venv/bin/python -c "import typst; typst.compile('typeset/explainers/climate.typ', output='build/explainer-climate.pdf', root='.')"
#import "lib.typ": *
#show: setup
#let D = json("/data/explainers/climate.json")

#let T0 = -490000000
#let xp(t) = W * (t - T0) / (0 - T0)
// temperature panel
#let H1 = 44mm
#let tmin = 5.0
#let tmax = 45.0
#let yT(v) = H1 * (1 - (v - tmin) / (tmax - tmin))
// CO2 panel (log)
#let H2 = 22mm
#let cmin = calc.log(100, base: 10)
#let cmax = calc.log(6000, base: 10)
#let yC(v) = H2 * (1 - (calc.log(v, base: 10) - cmin) / (cmax - cmin))

#let stepband(yf, key) = {
  // 5th-95th percentile band and median step line from stage data
  let lo = ()
  let hi = ()
  let med = ()
  for s in D.stages {
    if s.stage == "PETM" { continue }
    let v = s.at(key)
    lo.push((xp(s.from), yf(v.at(0)))); lo.push((xp(s.to), yf(v.at(0))))
    hi.push((xp(s.from), yf(v.at(2)))); hi.push((xp(s.to), yf(v.at(2))))
    med.push((xp(s.from), yf(v.at(1)))); med.push((xp(s.to), yf(v.at(1))))
  }
  place(pfill((..hi, ..lo.rev())))
  place(pline(med, stroke: 0.8pt + black))
}

#header(D.title)

#let ox = 10mm
#box(width: W + 12mm, height: H1 + H2 + 34mm, {
  // ---- temperature ----
  place(dx: ox, box(width: W, height: H1, {
    hgrid(yT, (10, 20, 30, 40), W)
    stepband(yT, "T")
    let st(name) = D.stages.find(s => s.stage == name)
    let mid(s) = (s.from + s.to) / 2
    // PETM spike as a tick (stage is only 0.3 Myr long)
    let p = st("PETM")
    place(line(start: (xp(mid(p)), yT(p.T.at(1))), end: (xp(mid(p)), yT(24)), stroke: 0.8pt))
    let lab(name, body, dx: 1mm, dy: -3.2mm) = { let s = st(name); note(xp(mid(s)), yT(s.T.at(1)), body, dx: dx, dy: dy) }
    lab("Hirnantian", [Hirnantian ice, 21 °C], dx: -4mm, dy: 7mm)
    lab("Serpukhovian", [Carboniferous ice], dx: -8mm, dy: 1.5mm)
    lab("Turonian", [Turonian 36 °C], dx: -10mm, dy: -3.6mm)
    lab("PETM", [PETM], dx: 0.8mm, dy: -1.5mm)
    lab("Upper Pleistocene", [last glacial 11 °C], dx: -21mm, dy: 1.2mm)
    // today line
    place(line(start: (0mm, yT(14)), end: (W, yT(14)), stroke: (paint: grey, thickness: 0.4pt, dash: "dotted")))
    note(W, yT(14), text(fill: grey)[pre-industrial ≈14 °C], dx: -40mm, dy: 0.4mm, size: 5.5pt)
    place(rect(width: W, height: H1, stroke: 0.6pt))
  }))
  ylabel-col(yT, ((10, "10 °C"), (20, "20"), (30, "30"), (40, "40")), ox)
  // ---- CO2 ----
  place(dx: ox, dy: H1 + 2mm, box(width: W, height: H2, {
    hgrid(yC, (280, 1000, 3000), W)
    stepband(yC, "CO2")
    note(W, yC(280), text(fill: grey)[280 ppm, pre-industrial], dx: -45mm, dy: 0.6mm, size: 5.5pt)
    place(rect(width: W, height: H2, stroke: 0.6pt))
  }))
  place(dy: H1 + 2mm, ylabel-col(yC, ((280, "280"), (1000, "1000"), (3000, "3000 ppm")), ox + 1mm))
  place(dx: ox + 1.5mm, dy: H1 + 2.5mm, text(size: 6pt, weight: "bold")[CO₂])
  xlabels(t => ox + xp(t), ((-400000000, "−400 Ma"), (-300000000, "−300"), (-200000000, "−200"), (-100000000, "−100"), (0, "now")), H1 + H2 + 3mm)
  place(dx: ox, dy: H1 + H2 + 8mm, text(size: 6pt, fill: grey)[Global mean surface temperature and CO₂ per geological stage, median and 90% range#cites(("judd2024",)).])

  // ---- inset: LR04 last 1 Myr (sawtooth) ----
  let iw = W
  let ih = 12mm
  let ix = ox
  let iy = H1 + H2 + 14mm
  let dmin = 3.0
  let dmax = 5.2
  let xi(t) = iw * (t + 1000000) / 1000000
  let yi(v) = ih * (v - dmin) / (dmax - dmin)   // inverted: more ice (high δ18O) plots lower
  place(dx: ix, dy: iy, box(width: iw, height: ih, fill: white, {
    place(pline(D.lr04.map(p => (xi(p.at(0)), yi(p.at(1)))), stroke: 0.45pt))
    place(rect(width: iw, height: ih, stroke: 0.4pt))
  }))
  place(dx: ix, dy: iy - 3mm, text(size: 6pt, weight: "bold")[Zoom: the last million years])
  place(dx: 0mm, dy: iy + 1mm, box(width: ox - 1.5mm, align(right, text(size: 5.5pt)[warm])))
  place(dx: 0mm, dy: iy + ih - 3mm, box(width: ox - 1.5mm, align(right, text(size: 5.5pt)[ice])))
  xlabels(t => ix + xi(t), ((-1000000, "−1 Ma"), (-800000, "−800 ka"), (-600000, "−600"), (-400000, "−400"), (-200000, "−200"), (0, "now")), iy + ih + 1mm)
  place(dx: ix, dy: iy + ih + 5mm, box(width: iw, text(size: 6pt, fill: grey)[Deep-sea oxygen isotopes (LR04 stack): down = more ice on land and colder deep water#cites(("lisiecki2005",)).]))
})

#v(1mm)
#sections(D)
#v(1mm)
#biblio()
