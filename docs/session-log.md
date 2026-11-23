# Session log

Newest first. Each entry: what was done, what was learned, and what's next. Keep entries short; details belong in
decisions.md and the other docs.

## 2026-11-22: "To add" pass through content-categories.md
Worked down the "To add" column one item at a time. Every research row is now ☑ except the leftovers below.
**Done**
- Jupiter entry: ~50 Earth masses by 3–4 Myr (kruijer2017). Impacts: Jeerinah 2.63 Ga (p389), Dales Gorge–Kuruman
  2.49 Ga (p417). Magnetic: Talakh-Khaya superchron (p705, date unverified).
- Tectonics: Kenorland vs supercratons (2.6 Ga), Superia break-up (2.45 Ga), Columbia break-up span (1.6–1.25 Ga),
  Gondwana assembly span (750–530 Ma), Pannotia (`debated`), Taconic/Appalachians, Everest summit limestone,
  South Atlantic (112 Ma), Laramide span (80–55 Ma), Alps (35 Ma, unverified).
- Eruptions: Bushveld, SW Laurentia plume + Midcontinent Rift, Siberian Traps, Ontong Java + OAE1a, Huckleberry Ridge.
- Atmosphere: ozone shield (~2.4 Ga, p435), mid-Proterozoic low O₂ span (1.8–0.8 Ga), Cenozoic CO₂ drawdown (rae2021).
- Oceans: first oceans (4.3 Ga, p55), Western Interior Seaway (94.5 Ma), Drake Passage (41 Ma).
- Climate: faint young Sun paradox (span from 3.8 Ga), Northern Hemisphere glaciation, Mid-Pleistocene Transition,
  deglaciation onset (last three on crowded p914).
- Early life: Moodies land mats (p271) and microfossils (p275), crown bacteria/archaea (<3.4 Ga), mitochondria
  (2.05–1.21 Ga, p588; betts2018).
- Firsts: _Anomalocaris_ eyes (515 Ma), _Cloudina_ reefs (548 Ma), oldest wood (~402 Ma), amniotes (314 Ma),
  _Castorocauda_ fur (Middle Jurassic).
- Behaviour: first 3D burrows (chen2025), _Mussaurus_ herd (pol2021), eusocial Cretaceous ants (barden2016).
- Plants: _Cooksonia_ (drawing attached, p831), _Swillingtonia_ (unverified), _Equisetum thermale_, polypod ferns.
- Animals: _Haootia_, _Triadobatrachus_, pterosaurs, _Vegavis_, oldest apes and Old World monkeys.
- Ancestors: _Doliodus_, _Eritherium_, PETM horses shrink, _Basilosaurus_ (PhyloPic drawing fetched).
- Ecosystems: archaeocyath reefs, Carnian coral symbiosis, first kelp.
- Extinctions: White Sea–Nama extinction (evans2022).
- Odd animals: _Quetzalcoatlus_, megalodon extinction, _Opabinia_ and terror birds (both dates unverified).
- Close calls: plants survive the end-Permian (nowak2019). Named ages: GOBE span (servais2018).
- Landmarks: Half Dome granite (coleman2004), Giant's Causeway/Antrim lavas (ganerod2010, unverified).
- Leftovers: _Acanthostega_/_Ichthyostega_ digits (coates1990), Wittenoom impact (p409), glyptodonts (delsuc2016),
  oldest dentine (haridy2025), crocodylomorphs (stubbs2021),
  Great Barrier Reef onset (gbrdrilling2001, p914), Niagara (tinkler1994, p914).
- Art: PhyloPic _Basilosaurus_ and _Acanthostega_ fetched and outlined but detached: long outlines hit a systemic
  wide-art layout bug (collision-pages.md, p831/840/907). 9 new art-candidate rows.
- Totals: 310 events (238 at start), 352 sources (280), 18 unverified (12); p901 now overflows.
- Sources added (cached in sources/; full-text notes for bleeker2003, meert2003, zhao2004, handy2010).
**Open:** Pangaea still on nance2014; unverified: talakh-khaya-superchron, alps-rise, swillingtonia-first-conifer,
opabinia, terror-birds-phorusrhacos, giants-causeway-antrim-lavas (verification-backlog.md); wide-art layout bug on p831/840/907 (collision-pages.md).
**Next:** fix the wide-art layout in typeset/book.typ, then reattach the two drawings; leftovers: oldest
living organisms (full text needed), Sue (no dated source yet), Campbellrand platform (no dated abstract found),
Pangaea source.
**Needs the user:** golden spikes (proposal), footer metrics, page-914 design for human history. (Animal groups: _Acanthostega_, synapsids left).

## 2026-11-21 (late night): gap dig, pages 326–374; dig-gap skill
**Done**
- New skill `.claude/skills/dig-gap` (deep-dive one stretch; dossier per stretch in `docs/gaps/`). Art policy in
  dig-gap and add-events: attach only fetchable images (PhyloPic); drawings, maps and diagrams go to art-candidates.md.
- Largest stretch 326–374 (2.945–2.70 Ga): 9 events added, all verified from abstracts (Pongola glaciation,
  Witwatersrand gold, Moon volcanism wanes, Klipriviersberg basalts, Zimbabwe flare, oldest magnetic reversal,
  Tumbiana bacteria and stromatolites, Kenoran orogeny on p377); 10 sources. Dossier: docs/gaps/326-374.md.
- 4 art-candidate rows (Kaapvaal map, reversal diagram, dropstone, Tumbiana stromatolite).
**Next**
- Pages 326–334 still empty; next largest stretches 666–704 and 276–314 (`/dig-gap`).

## 2026-11-21 (late night): verification pass 2
**Done**
- 120 of 131 unverified events checked and set `verified: true` (210 of 221 now); 16 corrections (dates moved to ICS
  stages, unsupported clauses removed, two sources added). Details and the 11 still-unverified events at the top of
  docs/verification-backlog.md.
- `tools/source_cache.py`: publisher landing-page fallback, `--refetch` and `--refetch-missing`; verification notes kept.
  34 cache files got `## Verification` notes; Rämö 2014 abstract from its open PDF. New source thomson2011.
- New skill `.claude/skills/verify-sources`.
**Next**
- Sources for the 11 remaining events (backlog table); cohen2013 boundaries vs ICS v2023/09; check pages of moved
  events (tetrapod trackways, Montsechia, Chorhat, Rodinia assembly) with `./run png`.

## 2026-11-21 (night, later): gap dig 276–314 (3.195–3.0 Ga)
**Done**
- Dossier docs/gaps/276-314.md. 8 events (p278–314): Pilbara rifting, Whundo arc, Kaapvaal craton, Cleaverville BIF,
  Archaean genetic expansion (unverified), Dominion Group, Prinsep Orogeny, Maniitsoq impact claim (refuted).
  `plate-tectonics-onset` gains diamonds (shirey2011) and crustal growth (dhuime2012). 14 sources.
- Maps (Natural Earth): pilbara-map, kaapvaal-dominion-map, maniitsoq-map.
**Next**
- Pages 271–275 (Moodies tides and microfossils, land mats 3.22 Ga); still empty p279–290 and p304–313.
- Read david2010 full text to verify the 3.33–2.85 Ga window.

## 2026-11-21 (night): Paleoarchean batch, image resources
**Done**
- 5 events in pages 231–249 (Buck Reef and Josefsdal mats, komatiites, ocean-temperature debate, Vaalbara); 13 sources.
  Hand-drawn `komatiite-spinifex.svg`.
- docs/image-resources.md: image sources with hints (PhyloPic, Natural Earth, Bioicons, IAN, FGDC, GPlates, BHL...).
- Art added to 8 events: stromatolite (Strelley Pool), _Juramaia_, _Purgatorius_, _Entelognathus_, _Archaefructus_,
  thrips, katydid (PhyloPic); Vaalbara locator map (`tools/basemap.py`, Natural Earth). Mediterranean map made, not attached.
**Next**
- project-plan row 17a: image-fullness check, then hand-made images. Confirm the no-NC licence rule (image-resources.md).

## 2026-11-21 (late): 1.64–1.50 Ga batch
**Done**
- 9 events, pages 587–603 (protosterols, McArthur River, _Qingshania_, Wiborg rapakivi, Tirohan red algae, Chorhat
  burrows, Gawler Range Volcanics, Gaoyuzhuang oxygenation and macrofossils); 11 sources. All `verified: false`; see backlog.
- project-plan.md: glossary appendix idea added (row 22a2).
**Next**
- Art candidates: Gaoyuzhuang blades, _Qingshania_ filament, Tirohan red algae (open-access CC BY figures to redraw).
- Not added yet: Mazatzal orogeny, Nuna breakup onset, Chuanlinggou acritarchs.

## 2026-11-21 (later): worklist cleanup, source cache
**Done**
- content-categories.md rewritten: per theme, "in the book" vs "to add" vs "dropped"; future threads table.
- Ongeluk eruptions + Makganyene glaciation added (gumsley2017). Decisions #38 (comparisons and joke names dropped),
  #39 (introduction mentions debated facts; docs/introduction-notes.md).
- General-knowledge statements listed as unverified (verification-backlog.md).
- `sources/`: local cache of every cited paper's metadata, link and abstract (`sources/abstracts/<key>.md`).

## 2026-11-21: verification pass, further categories, decisions
**Done**
- Verification pass on the from-memory batches: 57 events now `verified: true`; about 25 corrections (wrong taxon
  name, wrong ages, unsupported claims). Details and the remaining gaps are in verification-backlog.md.
- 43 new events from the "further categories" list (galaxy, Earth–Moon, sea level, biggest things, biomarkers,
  isotope excursions, microfossils, behaviour, odd animals, oddities, specimens, bottleneck); 16 new drawings and
  one hand-drawn mini-graph. 201 events, 260 sources.
- Decisions #33–#37: spans print at start and end; "now" immaterial; competing-dates rule; tags `galaxy`,
  `behaviour`, `record`; _Grypania_ redated.
- New docs: footer-candidates.md, collision-pages.md. Draft oxygen explainer page
  (`typeset/explainers/oxygen.typ`, `data/explainers/oxygen.json`).
- Art outline padding fix (clipped strokes).

**Open for the user:** competing-dates case (Moon age), "meanwhile" cross-references, GSSP labels, joke-name taxa,
review vs primary citations (explained), explainer pattern.

**Next:** fill the open stretches (content-categories.md table), page 914 design, the remaining unverified items.

## 2026-11-20 (later): Phase 3 started, first content pass
**Done**
- Tags: `tags` field + master list `data/tags.json` (decision #29); debated events allowed (#30).
- Worklist `docs/content-categories.md`; 158 events across all themes, 180 sources (DOIs via Crossref), 12 PhyloPic drawings.
- Layout fixes: unit labels yield both up and down; fullness includes labels; real overlaps count as overflow (#31, #32).

**Open decisions:** present-year convention (t for 1908/1994/2013); page 914 zoom design (overflowing);
range vs separate entries for competing dates; review-paper citations; long spans' start/end mentions.

**Next:** verification pass (many dates from memory, see verification-backlog.md); fill pages 548–642 and Archean gaps.

## 2026-11-19/20: Sessions 1–2, design, scaffold & physical decisions
**Done**
- Chose Typst + Python over LaTeX; built the pipeline: data → layout → `build/book.json` → Typst → PDF/PNG.
- Tools: check, query, add (dedupe and format), build (full / demo / range / single page / PNG), fullness (md + grid PNG + CSV), art (PhyloPic), models.
- Page design v0: ruler on the foredge side (mirrored), full-number time labels, one-line unit header, bold unit-boundary
  ticks with descriptions, events with leader lines, captioned line drawing, footer metrics on every page,
  quiet page numbers, foredge thumb-index bands with trim ticks, dense superscript bibliography.
- Demo data: 6 events, 3 footer series, 1 drawing, all cited **from memory** → docs/verification-backlog.md.
- Docs: PROJECT.md (features), decisions.md (28 entries), typesetting-questions.md (answered), project-plan.md,
  front-diagram-ideas.md + sketches (tabled), reference-numbers.md, dev-notes.md.

**User preferences learned** (beyond decisions.md)
- Values comfortable reading over exact vertical placement; roughly top/middle/bottom is enough.
- Wants every fact, date, metric and image cited; no fabricated precision.
- Likes the per-page footer even when values barely change.
- Reviews demos visually and gives itemized feedback; prefers concrete demos over abstract discussion.
- Has a separate list of event types to bring to the first research session.
- The book is volume 1 of a planned trilogy of ~1000-page books, so keep the engine generic (title, time range and scale all in config).

**Next:** Session 2b, imposition (`tools/impose.py`, 16-page signatures) and the first print, fold, sew and trim test.
Bring measurements: the printer's non-printable margin, duplex front/back registration, gutter loss, trim amount, foredge band visibility.
