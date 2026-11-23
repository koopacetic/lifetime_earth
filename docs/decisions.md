# Decisions

Settled choices. Append new ones (date, decision, short reason). Change one only by explicit user decision.

| # | Date | Decision | Why |
|---|---|---|---|
| 1 | 2026-11-19 | **Typst** (not LaTeX) as the typesetter, driven by Python | Reads JSON natively, real scripting, measures text, compiles 900+ pages in about 1 s. Installed as the `typst` pip package in `.venv` (no system install). |
| 2 | 2026-11-19 | Timeline runs from **−4,570,000,000 to 0**, **5,000,000 years per page**, giving **914 content pages**. Page boundaries are multiples of 5 Myr. | Starts just before the Solar System's first solids (−4,567.3 Myr); clean page math. |
| 3 | 2026-11-19 | Page 1 is the oldest. **Time runs down each page** and forward through the book. Top label = page start, bottom label = page end. | Reading order matches time. |
| 4 | 2026-11-19 | Years are **integers relative to present** (negative = past) everywhere in data. No unit strings. | No conversions; one representation. |
| 5 | 2026-11-19 | Uncertain dates: `t` = **midpoint** of the estimate, `t_err` = ±, printed with the date. Intra-page precision only needs to be roughly top/middle/bottom. | User preference. |
| 6 | 2026-11-19 | Long phenomena: `span` [start, end], entry at the midpoint by default; `mention` adds start/end pages for very large spans. | Avoids drawing multi-page bars for now. |
| 7 | 2026-11-19 | **Every** printed fact, date, metric and image is cited by BibTeX key in `data/sources.bib`; the bibliography prints the full list. | Scholarly book. |
| 8 | 2026-11-19 | Python owns data, validation and layout positions; `build/book.json` is the only interface to Typst; Typst owns all visual design. | Keeps each side simple and testable. |
| 9 | 2026-11-19 | No `cat`/category field yet. Event types are tabled until the first research session (the user has a list). | Avoid premature taxonomy. |
| 10 | 2026-11-19 | Self-printed, booklet imposition (4 pages per sheet), signatures of 4–6 sheets, hand-bound. | User is binding it. |
| 11 | 2026-11-19 | `./run` script instead of a Makefile | `make` isn't installed on this machine. |
| 12 | 2026-11-19 | Demo data (6 events, day-length series) is real and cited but **unverified**; a research session must verify or replace it. | Placeholder for building the engine. |
| 13 | 2026-11-20 | **Ruler, time labels and foredge band are always on the foredge side.** Content page 1 is a right-hand page (recto); odd content pages have the foredge on the right, even pages on the left. Mirroring is keyed to the content page number, so partial builds match the real book. | User: "always toward the foredge". |
| 14 | 2026-11-20 | Sheet: US Letter folded to 4 pages → 5.5×8.5 in untrimmed pages. Laser duplex, 24 lb bright paper, one volume (~2.5–3 in). Black and grey only. | User's equipment. |
| 15 | 2026-11-20 | Foredge trimmed with a plough after binding: bands printed into the bleed (12 mm from the untrimmed edge, 6 mm assumed trim), thumb-index vertical slots, data in `data/foredge.json`. | User confirmed trimming. |
| 16 | 2026-11-20 | Running head = one line of named units at the page's start (eon · era · period · epoch). Mid-page unit starts are heavy ruler ticks with a fixed italic label. | Keeps headers to one line. |
| 17 | 2026-11-20 | Citations: superscript numbers (Nature style); dense two-column 6.5 pt bibliography. | User: superscripts; dense but complete. |
| 18 | 2026-11-20 | Labels are always fully written with commas (−4,570,000,000); no "Ma"/"mya". Page boundaries stay round; page 1 (−4,570,000,000 to −4,565,000,000) contains the Solar System's first solids. | User preference; round labels. |
| 19 | 2026-11-20 | Art: PhyloPic silhouettes, made into uniform-stroke line drawings by `tools/art.py outline` (`art/line/`); each image has a bib entry and a credits record. | Consistent style, licensed, cited. |
| 20 | 2026-11-20 | Footer series can be cited point data (interpolated, never extrapolated) or a cited named model in `tools/models.py` (e.g. Gough 1981 solar luminosity). | Lets every page get a value where a published model exists. |
| 21 | 2026-11-20 | **Signatures: 4 sheets = 16 pages.** Total page count is padded to a multiple of 16 at imposition. | User. |
| 22 | 2026-11-20 | **The bulk of the book is timeline pages only**: no title pages, chapter openers or full-page images between timeline pages. Full-page images, if any, go in appendices. | Keeps 1 page = 5 Myr exact and the left/right mirroring intact. |
| 23 | 2026-11-20 | **Footer metrics on every page** (terse line); the 100 Myr check-in box is not used. Repeating values are fine. | User. |
| 24 | 2026-11-20 | **Ordinary page numbers in the footer**, quieter than the time labels and metrics (6.5 pt light grey, spine side). | User; needed for contents and binding checks. |
| 25 | 2026-11-20 | Unit boundaries inside a page: heavy ruler tick, **bold** title ("Cenozoic Era … begin") and an italic description (`description` in timescale.json). | User review of demo. |
| 26 | 2026-11-20 | Drawings carry a full caption (name plus 1–2 cited sentences) set beside the image; `_underscores_` give italics in titles, text and captions. | User review of demo. |
| 27 | 2026-11-20 | Front-of-book diagram tabled to the end of the project; may become text in the introduction instead. | User. |
| 28 | 2026-11-20 | **DOIs stay in `sources.bib` but are not printed** (Nature style omits them). Revisit only by explicit decision. | Dense bibliography; DOIs still used for verification. |
| 29 | 2026-11-20 | Events get optional **`tags`** (several per event), validated against the master list `data/tags.json` ({tag: description}). Reuse existing tags; add new ones only when none fits. No single `cat` field for now (supersedes #9 for tagging). | Many events span themes (Chicxulub = impact + extinction); a closed list prevents synonyms. |
| 30 | 2026-11-20 | **Debated events are included**: tagged `debated`, the text says what is disputed, `t_err` covers the competing range. | User. |
| 31 | 2026-11-20 | Layout: unit-boundary labels keep their ruler tick but the **label may move up** when the entries below it don't fit; any remaining overlap counts as overflow. Fullness now lays out boundary labels too (same input as the build). | Page 914 showed overlapping blocks that fullness reported as fine. |
| 32 | 2026-11-20 | Layout: after pull-up, a final push-down lets unit labels slide **down** below crowded entries (their tick stays at the true time). A page overflows only when content runs off the bottom. | Fixes overlaps when several entries share an anchor just above a boundary. |
| 33 | 2026-11-21 | **Long phenomena print at their start and end**, not at the midpoint (supersedes #6's default). The start entry carries the full text, the range ("−717,000,000 to −659,000,000") and any art. The end entry is a short reminder ("Began at …; lasted about 58 million years."). A span whose start and end fall on the same page prints once, at the midpoint, with the range. An explicit `mention` list still overrides. | User. |
| 34 | 2026-11-21 | **"Now" is immaterial**: year 0 is simply the end of page 914. Present-day events (Tunguska, Shoemaker–Levy 9, Chelyabinsk) keep small negative `t` values that differ only minutely on the last page; no calendar-year convention is needed. | User. |
| 35 | 2026-11-21 | **Competing dates**: when a source gives a range, `t` is its midpoint and `t_err` the half-width. When sources give *different* estimates, each case is put to the user: average them into one entry, or keep separate entries tagged `debated`. | User; extends #5 and #30. |
| 36 | 2026-11-21 | New tags `galaxy` (the Sun's path through the Milky Way, supernovae, gamma-ray bursts), `behaviour` (behaviour firsts) and `record` (record holders). The iron-60 supernova and Sagittarius events moved from `solar` to `galaxy`. | Groups grew large enough (per content-categories.md). |
| 37 | 2026-11-21 | _Grypania_ placed at 1,874 ± 9 Myr (Schneider et al. 2002 dated a volcanic layer correlated with the Negaunee Iron Formation), with its original 2.1 Gyr date in the text, tagged `debated`. | User: find a citation, else mark debated. |
| 38 | 2026-11-21 | **Dropped:** "surprising coexistence" comparisons (e.g. _T. rex_ closer to us than to _Stegosaurus_) and named-by-a-joke taxa. | User. |
| 39 | 2026-11-21 | The introduction must say that debated facts are included and marked as debated (collected in docs/introduction-notes.md). | User. |
| 40 | 2026-11-21 | **Images get their own lettered bibliography.** Image credits live in `art/credits.json` (one record per image; shared entries such as `claude-drawings` for line drawings, diagrams and maps made for the book, and `naturalearth`). `build.py` letters them a, b, … aa in order of first use in the book; captions end with the numbered fact cites, then italic superscript letters; an **Image credits** list follows the bibliography. Image keys are no longer in `sources.bib` and no longer in `art.sources` (which now holds only sources for caption facts). Supersedes the bib-entry part of #19. | User. |
