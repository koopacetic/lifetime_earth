// Lengths and absolute placement, the core of book.typ.
// Python passes numbers in mm; Typst multiplies by 1mm.
#let data = (height_mm: 60, events: (
  (y_mm: 5, anchor_mm: 8, title: "Moon-forming impact"),
  (y_mm: 25, anchor_mm: 40, title: "Oldest zircon"),
))
#set page(width: 120mm, height: 80mm, margin: 8mm)
#block(width: 100%, height: data.height_mm * 1mm, stroke: 0.3pt + luma(180), {
  let rx = 95mm   // ruler x position
  place(top + left, line(start: (rx, 0mm), end: (rx, data.height_mm * 1mm), stroke: 1pt))
  for e in data.events {
    let ay = e.anchor_mm * 1mm
    let ey = e.y_mm * 1mm
    place(top + left, line(start: (rx, ay), end: (60mm, ey + 2mm), stroke: 0.4pt))
    place(top + left, dx: 2mm, dy: ey, box(width: 56mm, text(weight: "bold", e.title)))
  }
})
