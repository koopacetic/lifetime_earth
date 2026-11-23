# 5. Tour of typeset/book.typ (195 lines)

Line numbers as of 2026-11-20.

**Lines 8–18: load data, derive lengths.**
```typst
#let D = json("/build/book.json")   // leading "/" = project root (build.py passes root=repo)
#let P = cfg.page
#let PW = P.width_mm * 1mm          // number × unit → length
```
Everything that crosses the Python→Typst boundary is plain numbers in mm and gets `* 1mm` here.

**Lines 20–26: global set rules.** `set document`, `set page`, `set text(font: cfg.type.font …)`,
`set par(leading:, spacing:)`. These are defaults for the whole book.

**Line 29: a context value.**
`#let physical-folio = context text(...)[#here().page()]`: the real page number, known only at layout time.

**Lines 63–65: small helpers.**
- `cites(keys)`: `keys.map(k => cite(label(k))).join()`. Bib keys arrive as strings; `label()` makes them citable.
- `rich(s)`: splits on `_` and wraps odd pieces in `emph`, a mini-markup for italics in JSON strings.
  (Strings from JSON are *not* parsed as Typst markup, which is why this helper exists.)

**Lines 68–130: page furniture.** `sides`, `page-header`, `metric-line`, `checkin-box`,
`page-footer`, `page-background`, `ruler`. Each is a function returning content; recto/verso
logic flips which side the foredge and ruler are on.

**Lines 134–151: `event-block(e)`.** One event: bold title, grey date in an inline `box`,
text plus citations, and optional art in a two-column `grid`. `e.at("kind", default: "event")`
is the safe dictionary lookup for optional fields.

**Lines 153–182: the page loop.**
```typst
#for p in D.pages {
  let recto = calc.odd(p.n)
  page(margin: ..., header: page-header(p, recto), footer: ..., background: ...)[
    #block(width: 100%, height: H, {
      ruler(recto)
      for e in p.events {
        place(top + left, line(start: (rx, ay), end: (edge, ty)))           // leader line
        place(top + left, dx: col-x, dy: ey, box(width: col-w, event-block(e)))
      }
    })
  ]
}
```
Each content page is a `page(...)` call with its own header/footer/background. Inside, a
fixed-height `block` is the coordinate system and every event is `place`d at Python-computed
`y_mm`. Nothing flows, so text that's taller than estimated will overlap, not push.
That's why the layout estimate in `tools/common.py` matters.

`metadata((name: u, n: p.n))<unit-start>` drops invisible labelled markers that can be
found later with `query(<unit-start>)` (e.g. for a table of contents or running header).

**Lines 187–195: bibliography.** A scoped `{ set text(...); ... }` block, `columns(n, bibliography(..., full: true))`.
`full: true` lists every entry even in partial builds.

To try a change: edit, `./run png 901`, look at `build/png/`.
