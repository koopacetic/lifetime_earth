---
name: dig-gap
description: Deep-dive one empty stretch of the Lifetime of the Earth book, find everything datable that happened in it, and keep a dossier of leads and dead ends. Use when asked to dig into, research or explore a specific gap, empty stretch or page range (fill-gaps is the broad survey; this is the deep one).
---

# Dig into a gap

Input: a page range (`326-374`), a year range, or "the next gap" (take the first ☐ row of the "Future threads"
table in `docs/content-categories.md`, else the longest stretch from `./run fullness --text --emptiest 10`).

Goal: everything honestly datable inside the stretch, with sources, plus a written record of what was searched so
the next session doesn't repeat it. An honestly empty page is fine; never stretch a date to land in the gap.

## 1. Frame the stretch
- `./run fullness --text --emptiest 20`: confirm the bounds (pages and years).
- `./run query --from T0 --to T1` with T0/T1 widened by ~50 Myr each side: what the neighbours already say,
  which spans (`span`) run through the gap, which threads it should continue.
- Note eon/era/period (`data/timescale.json` via `./run query --page N`) and which cratons have rock of this age.
- Check `docs/gaps/<first>-<last>.md` (or any dossier overlapping the range). If one exists, resume from it.

## 2. Mine what is already cited (free)
- Leads list in `docs/content-categories.md` ("Future threads" and "Leads from sources already cited").
- Grep the cached abstracts for ages in range, in every common style, e.g. for 2.95–2.70 Ga:
  `grep -l -E "2\.(7|8|9)[0-9]? ?(Ga|billion)|2,?[78][0-9]{2} ?Ma|29[0-4][0-9] ?Ma" sources/abstracts/*.md`
  Read only the matching files. A fact stated in a cached abstract needs no new source and can be `verified: true`.

## 3. Search systematically
Go through this checklist for the stretch; for each item, either find a dated fact or record "nothing found".
- **Rocks and records**: oldest/best-dated formations, type sections, palaeosols, tidalites, evaporites, BIFs.
- **Magmatism**: large igneous provinces, dyke swarms (great for precise U–Pb ages), komatiites, layered intrusions.
- **Tectonics**: orogenies, craton assembly or breakup, supercontinent stages, palaeomagnetic poles.
- **Impacts**: craters, spherule layers, shocked minerals.
- **Climate and chemistry**: glaciations, isotope excursions (C, S, Cr, Mo, MIF-S), oxygen whiffs, sea level.
- **Life**: microfossils, stromatolites, biomarkers, molecular-clock divergences (tag `debated` if contested).
- **Earth–Moon and sky**: day length, lunar distance, solar luminosity, galactic events.
- **Ore deposits and resources**: gold, uranium, iron, nickel deposits that formed in the window.
- **Detrital zircon / crustal growth peaks** and other global statistics (footer-series candidates too).
Prefer reviews and primary papers with DOIs (Crossref/OpenAlex lookups are fine); never cite from memory alone.
Run independent searches in parallel in one turn.

## 4. Write the dossier
Create or update `docs/gaps/<first>-<last>.md` (pages):

```
# Pages 326–374 (−2,945,000,000 to −2,700,000,000)
_Dug: YYYY-MM-DD. Status: N candidates, M added._
## Context
Neighbours, threads that pass through, cratons with rock of this age.
## Candidates
| t | ± | Page | Fact | Source (key or DOI) | Status |
(status: added / proposed / rejected: reason)
## Searched, nothing usable
Checklist items with no datable fact, and why (e.g. "no impacts known; spherule record starts 2.63 Ga").
## Art ideas
| Candidate | Resource tried | Result (file, or "none: reason") |
```

Compute pages with `./run query --page-of T`. Flag candidates that land outside the stretch but still belong to
the book (they go in too, just note it).

## 5. Look for art
Attach art only when an existing image can be fetched as is. **Don't create drawings during a dig** (maps, diagrams,
mini-graphs, redraws, traced outlines): list them in `docs/art-candidates.md` instead, to be made in a separate art pass.
- **Named organism** (genus or species, fossil or modern relative): read the PhyloPic hints in
  `docs/image-resources.md`, then `./run art search NAME`; if a usable image exists, `./run art fetch UUID SLUG` and
  `./run art outline art/phylopic/SLUG.svg`. Follow its working rules: CC0/PD, then CC BY, then CC BY-SA; no NC;
  check that the rendered preview isn't just a blob. If you use a modern relative, the caption must say "modern".
  The event's `art` gets `file` (relative to `art/`), a `caption` (name plus 1–2 sentences, `_italics_` for taxa)
  and `sources` for the caption's facts; `art fetch` writes the `art/credits.json` record.
- **Everything else** that would read better as a picture: add a row to `docs/art-candidates.md`
  (event id, page, what to show, possible source, approach). Use `docs/image-resources.md` to name the likely
  resource: Natural Earth locator map (`tools/basemap.py`) for where a site is today; Bioicons for cells;
  USGS FGDC patterns for rock columns; GPlates for past geography (≤1 Ga); NASA/USGS/NOAA for craters and
  eruptions; Smithsonian for minerals; a mini-graph from the cited data for trends; CC BY paper figures to redraw.
Record results as you go:
- Something new about a resource (useful, not found, a surprise) goes under that resource in `docs/image-resources.md`,
  and its ⏳ becomes 🔎 once you have searched it.
- Put the art ideas and their status in the dossier's "Art ideas" section.

## 6. Present, then add
Show the user the candidate table (fact, date ± error, page, source, suggested tags, proposed art), ordered by
confidence. On approval, follow the `add-events` skill (sources first, `./run add`, `./run check`, `./run png`
for touched pages). Check every page with art in the PNG; the drawing must not crowd the text.
Events whose claim or date couldn't be checked against the source (no abstract, paywalled) can still go in with
`"verified": false`, but each one also gets a row in `docs/verification-backlog.md`.

## 7. Close out
- Update the dossier statuses, and the stretch's row in `docs/content-categories.md` (☐ → ◐ or ☑, leads).
- New unverified claims go to `docs/verification-backlog.md`.
- Report: events added (id, page), art added (file, credit), art candidates listed, sources added, `./run fullness --text` before → after for this stretch,
  and what remains empty and why.
