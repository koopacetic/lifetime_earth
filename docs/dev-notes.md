# Developer notes & gotchas

Things learned while building the engine that aren't obvious from the code.

## Environment
- Typst is the `typst` **pip package** (typst-py 0.15) inside `.venv`. There's no system `typst` CLI, no TeX, and no `make`
  (hence `./run`). Python 3.15. Network access works (PhyloPic, doi.org).
- `typst.compile(src, root=..., format="png", ppi=N)` returns a **list of PNG bytes**, one per page. With `output=` it writes a PDF.
  `root` must be the project root, because the template reads `/build/book.json`, `/data/sources.bib` and `/art/...`.
- `typst.query(...)` exists and is the planned route for measuring rendered heights (emit `metadata`, query it back).

## Typst pitfalls hit so far
- A function whose code block ends with a bare value (e.g. returning a length after drawing) gets that value
  *joined* with content: "cannot join content with length". Keep drawing functions and value functions separate
  (`ruler()` vs `ruler-x()`).
- `cite()` requires a `bibliography()` somewhere in the document, so the bibliography is **always** typeset, even in
  partial builds. `--content-only` cuts the PDF afterwards with pypdf.
- Nature citation style = superscript numbers, numbered by first citation, no DOIs. Adjacent cites merge (²˒³).

## Page sides
- Left and right come from the **content page number** (odd = recto = foredge on the right), *not* the physical page,
  so partial builds mirror like the real book. The front matter ends with `pagebreak(to: "odd")` so content page 1
  is physically odd too.
- Content margins are set per page as explicit left/right values; the front and back matter use Typst's inside/outside.

## Layout engine (tools/common.py)
- Heights are **estimated** from character counts (avg char width 0.48 em). Good to about ±10% so far; captions sit beside the
  drawing, so art adds only `art_height_mm`.
- Unit boundaries are entries with `fixed: True`, centred on their tick; events flow around them (pushed down, then pulled up).
- Leader lines end level with the anchor when the text block spans it, otherwise at the block's nearest end.

## Art
- PhyloPic API requires the current `build` number; `tools/art.py` fetches it from the API root each time.
- Outlined silhouettes (`fill=none`, uniform stroke) keep tiny interior speckles from the potrace tracing. Acceptable;
  clean up per image if needed (delete small paths).
- Downloaded SVGs are checked for `<script` and `href=` before saving.
- `outline` pads the viewBox by the stroke width (stroke/10 viewBox units, since potrace scales paths by 0.1), so
  silhouettes that touch the canvas edge aren't clipped (Titanoboa was). Hand-drawn SVGs (e.g. mini-graphs) can live
  directly in `art/line/`; cite their data in `art.sources` and add a credits.json record with `"credits": ["claude-drawings"]`.
- Image credits (decision #40): Typst allows only one `bibliography()`, so the lettered Image credits list is built in
  Python (`common.image_credits`), passed in book.json (`image_credits`, `art.letters`) and typeset by hand in book.typ.
  Letters cover the whole book, not just the built pages, so they're stable in partial builds. Event art is matched to its
  record by file basename (`line/x.svg` -> slug `x`).
- Spans: `common.page_entries` prints start + end entries (decision #33); the end entry's text is generated.

## Safety habits
- Claude Code blocks `rm` on unguarded shell variables (`rm -f $DIR/*`). Use `"${DIR:?}"/*`, or do file work in Python.
