// Citations: cite by label (book.typ builds labels from strings), then a bibliography.
#set page(width: 120mm, height: auto, margin: 8mm)
#let cites(keys) = keys.map(k => cite(label(k))).join()

Zircons are old#cites(("wilde2001",)). Same thing with sugar: @wilde2001.

#bibliography("refs.bib", style: "apa")
