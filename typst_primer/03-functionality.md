# 3. Functionality: what Typst can do

**Page setup.** `page(width:, height:, margin:, header:, footer:, background:, foreground:)`.
Margins can be `(inside:, outside:)` for books, or per side. Calling `page(...)[body]` as a
function starts a fresh page with those settings, which is how book.typ gives each
content page its own header/footer/background.
→ https://typst.app/docs/reference/layout/page/

**Layout primitives.**
- `block`, `box`: containers with `width`, `height`, `inset`, `stroke`, `fill`, `radius`
- `grid`, `table`: columns `(auto, 1fr, 30mm)`, gutters, per-cell alignment
- `stack`, `columns`, `align`, `pad`, `move`, `rotate`, `scale`
- `place`: absolute positioning inside the parent; `float: true` for figure-like placement
- `measure(content)`: size of content before placing it (inside `context`)
→ https://typst.app/docs/reference/layout/

**Drawing.** `line`, `rect`, `circle`, `ellipse`, `polygon`, `curve`/`path`, gradients, tiling patterns.
For serious diagrams use the `cetz` package.
→ https://typst.app/docs/reference/visualize/

**Text.** `text(font:, size:, weight:, style:, fill:, lang:, tracking:)`, `par(leading:, spacing:, justify:)`,
OpenType features, hyphenation by `lang`, smart quotes, `smallcaps`, `super`/`sub`.
→ https://typst.app/docs/reference/text/

**Data in.** `json`, `csv`, `yaml`, `toml`, `xml`, `cbor`, `read` (raw text/bytes). Paths are
relative to the file or absolute from the project root. This is the bridge this repo
relies on: Python computes, Typst draws.
→ https://typst.app/docs/reference/data-loading/

**Bibliography.** `bibliography("refs.bib", style: "apa")` + `cite(<key>)` or `@key`.
Reads BibTeX or Hayagriva YAML; styles are CSL (built-in names or a `.csl` file).
If anything is cited, a bibliography must exist somewhere in the document.
→ https://typst.app/docs/reference/model/bibliography/

**Introspection.** `counter`, `state`, `here()`, `locate`, `query`, `metadata`. Lets you build
running headers ("current unit"), tables of contents, cross-references. Reading these
values needs `context`. Typst iterates layout (up to 5 passes) until values stabilize.
→ https://typst.app/docs/reference/introspection/

**Math.** `$ ... $` with LaTeX-like but cleaner syntax (`$sum_(i=1)^n x_i$`).
→ https://typst.app/docs/reference/math/

**Images.** PNG, JPEG, GIF, SVG, PDF (as an image, in recent versions), `width`/`height`/`fit`.
→ https://typst.app/docs/reference/visualize/image/

**Output.** PDF (incl. PDF/A, tagged PDF for accessibility), PNG, SVG, and experimental HTML.

**Packages.** Typst Universe: `#import "@preview/name:version"`. Downloaded and cached on
first use. Popular: `cetz` (drawing), `fletcher` (diagrams), `tablex`, `codly` (code),
`touying`/`polylux` (slides).
→ https://typst.app/universe/

**What it is not.** No arbitrary shell/network access from a document (deterministic, sandboxed),
no mutable globals (use `state`), and no "measure the whole page then rewrite earlier pages"
except through introspection. That's why this repo estimates layout in Python
(`tools/common.py`) and passes exact mm positions in.
