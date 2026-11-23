# Lifetime of the Earth: agent notes

Book: 914 content pages, 5 Myr each, from −4,570,000,000 (page 1) to 0 (page 914), plus front and back matter.
Pipeline: `data/*.json` → `tools/build.py` (validate, lay out) → `build/book.json` → `typeset/book.typ` (Typst) → PDF.
Overview, features and status: README.md. Settled decisions: docs/decisions.md (don't relitigate; append new ones).
Also in docs/: session-log.md (read the latest entry first), project-plan.md, verification-backlog.md (unchecked citations),
reference-numbers.md (key pages and physical sizes), art-candidates.md (events needing hand drawing or image research), dev-notes.md (Typst/tooling gotchas; read before editing code).

## Commands (use these; don't read data files wholesale)
- `./run check`: validate everything. Run after any data edit.
- `./run query --page 901` | `--from T --to T` | `--grep word` | `--page-of T` | `--id X --full` | `--sources` | `--tags` | `--tag impact`
- `./run add data/events/<file>.json < new.json`: add, sort, format, dedupe, validate
- `./run png 901`, then view build/png/*.png to check a page visually
- `./run demo` | `./run pages 1-15` | `./run book`
- `./run art search NAME` / `fetch UUID SLUG` / `outline art/phylopic/SLUG.svg`: fetch adds the image credit to art/credits.json
- `./run fullness --text`: emptiest stretches (cheap to read)

## Data rules
- Format reference = `data/schema.json`. Years are integers relative to present (negative). No units, no strings.
- `t` is the midpoint of the estimate; put uncertainty in `t_err`. Long phenomena: `span` + optional `mention`.
- Every event needs ≥1 `sources` key that exists in `data/sources.bib` (add the BibTeX entry first).
  Footer series points and art captions need sources too. Never invent citations; include a DOI when one exists.
- Every image needs a record in `art/credits.json` (lettered Image credits, decision #40), never a sources.bib key.
  Drawings made in-house (by script or by hand) get `"credits": ["claude-drawings"]` (plus e.g. `naturalearth`).
- New entries get `"verified": false` unless the date and claim were checked against the source.
- `_underscores_` give italics (taxon names) in titles, text and art captions. Art captions: name plus 1–2 sentences, facts cited in art.sources.
- `tags`: reuse tags from `data/tags.json` (`./run query --tags`); add a new one there only if none fits. `debated` marks disputed events.
- `id` is kebab-case, unique, permanent. Don't hand-format event files; `./run fmt` owns formatting.
- Bulk of the book = timeline pages only (no inserted pages; full-page images go in appendices).
- Don't add fields outside the schema; propose schema changes in docs/decisions.md.

## Code map
- tools/common.py: page math, loading, layout estimate (shared by every tool)
- tools/build.py, check.py, query.py, add.py, fullness.py, basemap.py (Natural Earth line maps); see tools/README.md
- typeset/book.typ: all visual design. Python passes positions in mm; Typst draws. Odd content page = recto:
  ruler, labels and foredge band on the RIGHT; even = LEFT. config.json holds page geometry, foredge, footer mode.
- data/: events/, series/ (footer metrics), explainers/ (draft metric explainer data), tags.json (master tag list), timescale.json, foredge.json, sources.bib, schema.json
- sources/: cached abstract + links per bib key (`sources/abstracts/<key>.md`); read before fetching online; `tools/source_cache.py .` adds new keys
- typeset/explainers/: draft one-page explainers for footer metrics (docs/footer-candidates.md)
- Skills: `.claude/skills/add-events`, `.claude/skills/fill-gaps` (survey), `.claude/skills/dig-gap` (deep-dive one stretch; dossiers in docs/gaps/)
