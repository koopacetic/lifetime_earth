// Loading data, page() per item with header/footer, context for page numbers,
// metadata + query for introspection.
#let pages = json("sample.json")
#set page(width: 100mm, height: 60mm, margin: 10mm)

#for p in pages {
  page(
    header: align(right, text(size: 7pt)[#p.label]),
    footer: context align(center, text(size: 7pt)[physical page #here().page()]),
  )[
    #metadata(p.label)<page-marker>
    #p.body
  ]
}

#page[
  = Index (built with query)
  #context for m in query(<page-marker>) [
    - #m.value #h(1fr) p. #m.location().page()\
  ]
]
