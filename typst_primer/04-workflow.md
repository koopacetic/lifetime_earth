# 4. Workflow

## Generic Typst workflow
1. **Write** `main.typ`: `set` rules at the top (page, text, par), then content.
2. **Preview live**: `typst watch main.typ`, with a PDF viewer that reloads on change,
   or the Tinymist extension in VS Code (live side-by-side preview, completion, hover docs, jump-to-source).
3. **Factor out** styling into a template: `#let template(doc) = { set ...; doc }` then `#show: template`.
4. **Split** long docs with `#include "ch1.typ"` or `#import` for shared helpers.
5. **Feed data** via `json()` / `csv()` or `--input`.
6. **Compile** for release: `typst compile main.typ out.pdf`.
7. **Debug**: errors point to file:line with a span; `#repr(x)` or `#panic(x)` to inspect values;
   `#type(x)` to check types. Typst errors are usually type mismatches (number vs length, string vs content).

→ https://typst.app/docs/tutorial/  ·  https://myriad-dreamin.github.io/tinymist/

## This repo's workflow

```
data/*.json ──► tools/build.py ──► build/book.json ──► typeset/book.typ ──► build/*.pdf / build/png/*.png
 (events,        (validate, pick      (pages, each with      (reads JSON, draws        (typst.compile via
  config,         pages, estimate     events + y_mm,          everything at the         Python bindings)
  sources.bib)    heights, lay out)   anchor_mm, h_mm…)       given mm positions)
```

Division of labour:
- **Python decides** *what* goes on each page and *where* (all positions in mm).
- **Typst decides** *how it looks*: fonts, strokes, colours, header/footer, citation formatting.
- Changing a visual detail → edit `typeset/book.typ` only.
- Changing what's on a page or its placement → `tools/common.py` / `tools/build.py`.

Day-to-day commands (from the repo root):

| Goal | Command |
|---|---|
| Look at one page | `./run png 901`, then open `build/png/*.png` |
| A few pages as PDF | `./run pages 1-15` → `build/partial.pdf` |
| Design demo | `./run demo` → `build/demo.pdf` |
| Whole book | `./run book` → `build/book.pdf` |

Don't compile `book.typ` directly: it reads `build/book.json`, which may be stale
(or a partial selection) unless `build.py` just wrote it. If you *do* want a live
`typst watch` loop while tweaking design, run `./run pages 901-904` once to produce
`build/book.json`, then (with the CLI installed):

```bash
typst watch --root . typeset/book.typ /tmp/look.pdf
```

and edit `book.typ`. Re-run `./run pages …` whenever data or layout changes.

Fonts: the font name comes from `config.type.font` in the data. If it isn't installed,
Typst silently falls back (with a warning). Check with `typst fonts` or `python -c "import typst; ..."`.
