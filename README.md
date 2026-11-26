# The Lifetime of the Earth

A self-printed, hand-bound book of roughly 1000 pages that presents the whole history of the Earth, from the
formation of the Solar System (about 4.57 billion years ago) to now, at a fixed scale of
**5,000,000 years per page**. Each content page is labelled with the year at its top and bottom
(e.g. `−3,445,000,000` / `−3,440,000,000`). Events, facts and phenomena are placed at their position in time,
and every fact, date and image is cited in a full bibliography.

The book is generated from data (`data/`) by a Python + Typst pipeline, so it can be rebuilt after every change.

- **Content pages:** 914 (−4,570,000,000 → 0). Front matter and bibliography bring the total to about 1000.
- **Reading direction:** page 1 is the oldest; time runs down each page and forward through the book.
- **Physical:** US Letter sheets folded to 4 pages (5.5×8.5 in), laser duplex, 24 lb paper, black and grey only;
  sewn signatures, one volume of about 2.5–3 in; foredge trimmed with a plough. Book 1 of a planned trilogy (~1000 pages each).

See also: [docs/project-plan.md](docs/project-plan.md) · [docs/decisions.md](docs/decisions.md) ·
[agent-notes/dev-notes.md](agent-notes/dev-notes.md) · [tools/README.md](tools/README.md) · [CLAUDE.md](CLAUDE.md)

## Feature list

Status: ✅ working (basic) · 🔧 planned · 💬 tabled for discussion · ❓ uncertain feasibility

### Pages & timeline
- ✅ Fixed 5 Myr per page; page boundaries at multiples of 5 Myr; top and bottom time labels as full numbers
- ✅ Time ruler with 100 kyr / 500 kyr / 1 Myr ticks, **always on the foredge side** (mirrored left and right)
- ✅ One-line running head: eon · era · period · epoch (🔧 add Paleozoic/Mesozoic epochs and stages to the timescale)
- ✅ Unit boundaries inside a page: heavy ruler tick, bold title and italic description
- ✅ Events placed at their approximate vertical position (top / middle / bottom accuracy is enough)
- ✅ Uncertain dates: placed at the midpoint of the estimate, with ± printed
- ✅ Very long phenomena: optional `span` with entries at the start, middle and/or end pages
- 🔧 Calibrate the layout height estimate against Typst's measured sizes; overflow handling for dense pages
- 🔧 Final page and human history: compaction or leader lines for the crowded last few hundred thousand years
- 💬 Short-range "time ruler bracket" for events lasting a fraction of a page
- 💬 Nested zoom insets for the final page (5 Myr → 500 kyr → … → 50 yr)

### Footer metrics (terse generated metadata)
- ✅ Machinery: `data/series/*.json`, cited point data (never extrapolated) or cited models (`tools/models.py`)
- ✅ Demo series: Sun brightness (Gough 1981 model, every page), length of day, days per year (Williams 2000, last 620 Myr)
- ✅ Footer layout B (decision #45): line 1 = `sky` · `air` series, line 2 = `life`, on every page; a boxed
  **100 Myr check-in** strip on pages ending on a round 100 Myr (pp. 14, 34 … 914). Fixed height, so the bottom time label never moves
- ✅ Rules (decision #43): a series must span ≥10 pages (50 Myr); values relative to today unless familiar (24 h, 365 d)
- 🔧 Series for the `air`, `life` and `checkin` slots (none yet); replace the linear day-length demo with cited points;
  candidates in [docs/footer-candidates.md](docs/footer-candidates.md) (Moon distance, O₂, sea level, CO₂, temperature, families, …)
- 🔧 One-page explainers per metric in the back matter (oxygen draft in `typeset/explainers/oxygen.typ`)
- ✅ Ordinary page numbers in the footer, quieter than the time labels and metrics

### Physical book
- ✅ Foredge tabs: grey thumb-index blocks printed into the bleed and trimmed through by the plough; head and tail trim ticks.
  **11 era-level tabs** (Hadean eon + 10 eras), each labelled vertically in white bold (decision #44). 🔧 print test of the 6 pt
  reverse type and the thin Mesozoic/Cenozoic bands. 💬 a life-based set (*before life / single-celled / multicellular / animals / life on land*), with citations.
- 🔧 Imposition: reorder pages into 4-up booklet sheets per signature (`tools/impose.py`, pypdf), with blank
  padding and optional creep compensation
- 🔧 Physical page numbers (folio): currently tiny on the outer edge, for binding/debug

### Front & back matter (the bulk of the book is timeline pages only, with no inserts)
- ✅ Title page
- ✅ Summary table of contents (eons / eras → physical page), generated from data
- 🔧 Introduction / how to read this book (points to cover: [docs/introduction-notes.md](docs/introduction-notes.md))
- 💬 Whole-history overview diagram: **tabled to the end of the project**; sketches in [docs/front-diagram-ideas.md](docs/front-diagram-ideas.md); may become introduction text
- 🔧 Cover and spine (pasted on separately): discuss and draft printable versions near the end of the project
- ✅ "Names of geological time": one-page back-matter explainer with the foredge tab key (decision #44; 🔧 sources for the Greek glosses)
- ✅ Bibliography: superscript citations (Nature style), dense 2-column 6.5 pt (about 16 pages per 1000 sources)
- ✅ Image credits: lettered list after the bibliography, generated from `art/credits.json` (decision #40)
- 🔧 Colophon
- 🔧 Glossary appendix (project-plan row 22a2)
- 🔧 Optional subject index
- 🔧 Appendices for any full-page images

### Art
- ✅ Line drawings on 42 events (e.g. Tyrannosaurus on the Chicxulub page; `./run png 901`), each with a full cited caption beside it
- ✅ In-house drawings: Natural Earth locator maps (`tools/basemap.py`), mini-graphs, cross-sections
- 🔧 Wide drawings squeeze their caption (p831, 840, 907); fix in `typeset/book.typ`, then reattach _Basilosaurus_ and _Acanthostega_
- 🔧 Open image needs: [docs/art-candidates.md](docs/art-candidates.md)
- ✅ `tools/art.py`: PhyloPic search, fetch (with credits and bib entry), outline → uniform-stroke line art
- 💬 **PhyloPic** as the main source: free silhouettes of organisms, mostly CC0 / CC BY, with an API
  (https://www.phylopic.org/; e.g. search "Dimetrodon" or "Anomalocaris" there). License and attribution go in `art/credits.json`.
- 💬 Paleogeography thumbnails (continent positions per page or every N pages), e.g. via GPlates plate
  models (open source; reconstructions reliable to about 1 Ga). Check licensing before using any published maps.
- 💬 Per-page mini-strip: a "you are here" bar showing this page's position in the whole 4.57 Gyr

### Data & workflow
- ✅ JSON event data with schema, integer years, required citations, `verified` flag
- ✅ Tools: check, query, add (sorts, formats, rejects duplicates), build (full / demo / page range / PNG), fullness
- ✅ Fullness report: markdown summary plus a page-grid image plus a history CSV
- ✅ Event tags from a master list (`data/tags.json`, decision #29), `debated` events (#30), `importance` 1–5 (#41)
- ✅ Skills for research: add-events, fill-gaps, dig-gap (dossiers in `agent-notes/gaps/`), verify-sources
- ✅ Source cache: abstract and links per bib key in `sources/abstracts/`
- 🔧 Shard event files (by eon or topic) once they grow; tools already read every `data/events/*.json`
