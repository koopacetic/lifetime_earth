# tools/

Command-line tools that do all the work on data and builds. They exist so that people and Claude sessions
can change the book **without reading or hand-editing large JSON files**: query instead of reading, add instead
of editing, check instead of eyeballing. Run with `.venv/bin/python tools/<name>.py --help` or through `./run`.

## Current

| Tool | Purpose |
|---|---|
| `common.py` | Shared library: paths, loading, **page math** (`page_of`, `page_bounds`), number formatting, series interpolation, entry expansion (spans → start/mid/end), **layout estimate** (`layout_page`). |
| `check.py` | Validates everything: JSON schema, unique ids, years in range, `t` inside `span`, every source key in `sources.bib` (events, art, timescale, series), every tag in `data/tags.json`, art files exist. Counts unverified entries. Exit 1 on error. Runs automatically before every build and after every add. |
| `query.py` | Compact one-line-per-event lookups by page, year range, text, id; `--page-of YEAR`; `--sources` usage counts; `--tags` master tag list with counts; `--tag X` filter. |
| `add.py` | Adds events from stdin or a file into an event file; rejects duplicate ids and near-duplicates (close in time and similar title); sorts by `t`; writes canonical formatting; runs check. `--fmt` reformats all files. |
| `build.py` | Lays out the selected pages and writes `build/book.json`, then compiles with Typst. Modes: full book, `--demo` (config `demo_pages`), `--pages 1-15,900-914`, `--at YEAR`, `--content-only` (exactly those pages, e.g. a single-page PDF), `--png` (per-page images for visual checks), `--no-front`. Adds unit-boundary entries (fixed position), foredge slot, and footer metrics per page. |
| `models.py` | Named, cited analytic models for footer series (e.g. `gough1981` solar luminosity). |
| `art.py` | PhyloPic pipeline: `search NAME`, `fetch UUID SLUG` (SVG → `art/phylopic/`, plus `art/credits.json` and a bib entry), `outline FILE` (uniform-stroke line drawing → `art/line/`). |
| `fullness.py` | Lays out **all** pages without typesetting; writes `build/fullness.md` (summary by eon, longest empty stretches), `build/fullness.png` (page grid), and appends to `build/fullness_history.csv`. `--text` prints the summary only. |
| `basemap.py` | Draws a present-day locator map as line art from Natural Earth GeoJSON (downloaded to a scratch folder): `--bbox W S E N`, `--mark lon,lat,label`, `--label lon,lat,text`. Output goes in `art/line/`; credit `claude-drawings` + `naturalearth` in art/credits.json. See docs/image-resources.md. |

## Planned

| Tool | Purpose |
|---|---|
| `impose.py` | Reorder the finished PDF into booklet sheets: 2 pages per side, 4 per sheet, grouped in signatures of N sheets; blank padding; optional creep shift, crop, fold and collation marks. Output: a print-ready PDF per volume. (pypdf) |
| `measure.py` | Calibrate layout: Typst emits measured event-block heights as `metadata`, read back via `typst.query`; replaces the character-count estimate and makes fullness exact. |
| `bib.py` | Add a source by DOI (fetch BibTeX from doi.org), normalize keys, report unused or uncited entries. |
| `series.py` | Plot each footer metric series across the whole book for sanity checks; flag gaps where a footer value is missing. |
| `stats.py` | Fullness history chart; counts by tag and by eon; verification progress. |
| tests | pytest for page math, span expansion, layout invariants (no overlap, nothing off-page). |
