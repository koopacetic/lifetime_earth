# Project plan

Each session ends with: `./run check` clean, decisions appended to docs/decisions.md, README.md statuses updated,
a short entry at the top of agent-notes/session-log.md, agent-notes/verification-backlog.md updated for any unverified
facts, and **this file updated** (phase status, todo register).

This file is the single index of open work. Detailed lists live in the files linked from each item; when an item is
done, tick it here and in its source file.

Status: ✅ done · ◐ in progress · ☐ not started · 💬 tabled (idea, waiting for a decision)

## Snapshot (2026-11-25)
| Measure | Now | Notes |
|---|---|---|
| Events | 354 (388 printed entries incl. span ends) | After the significance pruning of 2026-11-23 (388 → 354) |
| Sources | 432 in sources.bib | All cached in sources/abstracts/ |
| Verified | 331 of 354 (93%) | 23 unverified; list in agent-notes/verification-backlog.md |
| Pages with ≥1 entry | 236 of 914 (26%) | Mean fullness 7.1% |
| By eon (non-empty / pages) | Hadean 21/107 · Archean 50/306 · Proterozoic 94/392 · Phanerozoic 70/108 | Mean fullness 3.9% · 3.7% · 5.0% · 27.1% |
| Overflowing pages | 901, 913, 914 | docs/collision-pages.md |
| Events with art | 42 | 3 drawings ready but unattached; 53 art-candidate rows open |
| Footer series | 6: Sun, Day, Year, Moon (`sky`); CO₂, Temp (`air`) | `life` and `checkin` slots have no data yet |
| Importance | 5: 25 · 4: 90 · 3: 169 · 2: 70 · 1: 0 | Decision #41 |

## Phase status

### Phase 1: Foundations (≈ 50%)
| # | Session | Status | Done / remaining |
|---|---|---|---|
| 1 | Design & scaffold | ✅ 2026-11-19 | Folder structure, schema, tools, Typst demo, docs |
| 2 | Physical decisions | ✅ 2026-11-20 | Sheet, paper, printer, trim; foredge prototype; footer and art demos |
| 2b | Imposition & first print test | ☐ | `tools/impose.py` (booklet sheets per signature, padding, creep, marks) does not exist yet. Print, fold, sew and trim one test signature; measure the printer's non-printable margin, registration, trim and gutter |
| 3 | Typography & page design | ◐ ~40% | Page design v0 on screen (Libertinus Serif 9 pt, ruler, running head, event blocks, mirrored margins). Remaining: print test spreads, tune sizes and margins from them |
| 4 | Foredge test | ◐ ~50% | Band set decided: 11 era-level tabs with white labels (decision #44). Remaining: bleed and trim test on a dummy stack; see "Open physical-book items" |

### Phase 2: Engine (≈ 45%)
| # | Session | Status | Done / remaining |
|---|---|---|---|
| 5 | Engine hardening & verification | ◐ ~20% | Spans (#33), unit-label yielding (#31, #32) done. Remaining: calibrate layout against Typst measurements (`metadata` + `typst.query`; heights are still estimated from character counts in `tools/common.py`), overflow strategy (see "Open engine items"), pytest for page math, fullness from measured heights, Paleozoic/Mesozoic epochs in data/timescale.json (only 7 Cenozoic epochs so far) |
| 6 | Event taxonomy & schema | ✅ mostly | Tags with a master list (#29), `debated` (#30), `importance` 1–5 (#41). Remaining: fullness per tag; use `importance` in layout beyond "who yields" |
| 7 | Footer metrics research | ◐ ~30% | Rules (#43) and layout B (#45) implemented. 3 series in use. Remaining: series for the `air`, `life` and `checkin` slots; replace the linear day-length demo; see "Footer & explainers" |
| 8 | Front & back matter | ◐ ~45% | Done: title page, summary contents, bibliography, lettered Image credits (#40), "Names of geological time" explainer (#44). Remaining: introduction, colophon, index decision, appendices, metric explainers |

### Phase 3: Content (≈ 30% of pages have an entry)
Deep research sessions with the `add-events`, `fill-gaps`, `dig-gap` and `verify-sources` skills. Worklist by theme:
docs/content-categories.md (23 themes ☑ or ◐; open "To add" items listed below).
| # | Session | Pages | Status | Non-empty pages |
|---|---|---|---|---|
| 9 | Solar System formation & Hadean | 1–107 | ◐ | 21 of 107 |
| 10 | Archean | 108–414 | ◐ (10 gap digs done) | 50 of 306 |
| 11 | Proterozoic | 415–807 | ◐ (9 gap digs done) | 94 of 392 |
| 12 | Paleozoic | 807–864 | ◐ | 34 of 58 |
| 13 | Mesozoic | 864–901 | ◐ (p901 overflows) | 25 of 38 |
| 14 | Cenozoic (not the final page) | 901–913 | ◐ (p913 overflows) | 13 of 14 (incl. p914) |
| 15 | **Final page & human history**: zoom insets / compaction design plus content | 914 | ☐ blocked on design | Overflows (~3.4 pages of content) |
| 16+ | Gap filling by fullness report; verification passes | all | ◐ ongoing | 2 verification passes done (93% verified) |
| 16a | **Duplicate review**: events that tell the same story twice (same rock, impact, sample or claim under different ids, e.g. `archean-impact-s2` vs `impacts-boil-oceans`) and series of near-identical records (one more zircon, BIF or dyke swarm). `./run add` only catches near-duplicates at insert time, so also check across wider time gaps and by shared sources. Merge or cut; see docs/significance-review.md | all | ◐ first pass done in the significance review (34 removed) | — |

### Phase 4: Art & extras (≈ 25%)
| # | Session | Status | Output |
|---|---|---|---|
| 17 | Illustration pipeline: fetch/outline/credits ✅; choose taxa per era; check style consistency; work through docs/art-candidates.md | ◐ | `art/`, `art/credits.json`; 42 events with art |
| 17a | **Hand-made images**: draw SVGs for events no image library covers (stromatolite vs folded rock at Isua, O₂ mini-graph, banded iron, zircon with a hair for scale, Snowball rock column, prokaryote vs eukaryote cell; list in agent-notes/image-resources.md). First build an **image-fullness** check (like `./run fullness`, counting pages with art): report the longest stretches of text-only or blank pages | ◐ ~10% | Done so far: komatiite cross-section, bottleneck mini-graph, 5 Natural Earth maps. Image-fullness check not built |
| 18 | Paleogeography thumbnails (GPlates) | 💬 | maps every N pages |
| 19 | Mini-strip "you are here" | 💬 | per-page strip |
| 20 | Short-range time-ruler brackets | 💬 | ruler annotations |

### Phase 5: Production (≈ 0%)
| # | Session | Status | Output |
|---|---|---|---|
| 21 | Citation audit (every source opened and checked), final fullness pass | ☐ | clean report |
| 22 | Full proof print of one volume's worth of signatures; fix | ☐ | — |
| 22a | **Front-of-book diagram**: pick from docs/front-diagram-ideas.md or fold into the introduction | 💬 | diagram or text |
| 22a2 | **Glossary appendix**: dictionary of science terms used across events (orogeny, rapakivi, euxinic, acritarch, stem/crown group). Could come from a `data/glossary.json` plus a check that flags undefined jargon; needs a schema decision. **Rule:** a term used in one event gets a short in-line definition; a term used in ≈5 or more events gets a fuller glossary entry. A usage count per term decides | ☐ | appendix pages |
| 22b | **Cover & spine**: discuss and draft printable designs for test prints (spine could carry a scaled time ribbon, idea F in front-diagram-ideas.md) | ☐ | cover/spine PDFs |
| 23 | Final print, bind | ☐ | the book |

## Todo register

### Decisions needed from the user
- [ ] Page 914 design for human history: zoom insets (5 Myr → 500 kyr → … → 50 yr), or compaction (session 15; docs/collision-pages.md). No back-matter "last 5 million years" section (#47).
- [ ] Golden spikes: print the GSSP location on each boundary label? Needs ICS data in timescale.json and sources (content-categories.md; GSSP statements in verification-backlog.md "General-knowledge statements").
- [ ] "Meanwhile" cross-references between entries (raised 2026-11-21, not decided).
- [ ] Footer metrics to pursue next, and which go to explainers only (docs/footer-candidates.md).
- [ ] Days per year: now computed from day length (2026-11-25); confirm, then record as a decision (footer-candidates.md).
- [ ] Oxygen footer format for limits and ranges (`O₂ <0.0002%`) (footer-candidates.md).
- [ ] Names explainer: also cover periods and epochs, or stay at eons and eras (below).
- [ ] Index: subject index or not (README "Front & back matter").
- [ ] Image licence rule: confirm "no NC licences", then move it to decisions.md (agent-notes/image-resources.md).
- [ ] Foredge: research a life-based band set (before life / single-celled / multicellular / animals / life on land) as an alternative or second set (README "Physical book"; head-edge bands below).

### Open physical-book items (carried over from the retired typesetting Q&A, 2026-11-20)
Settled answers are in docs/decisions.md. Still open, for the print-test sessions (2b, 3, 4, 22):
- [ ] Printer: measure the non-printable margin and front/back registration.
- [ ] Show-through: check back-to-back registration of ruler and labels on 24 lb paper.
- [ ] Gutter loss and creep: tune the 20 mm inside margin; optional per-sheet creep shift in `impose.py`.
- [ ] Signature size (4 sheets = 16 pages) and the page-count padding: revisit after printing.
- [ ] Spreads as 10 Myr views: continuation marks at the bottom of left pages and the top of right pages?
- [ ] Head-edge bands: a second band set on the head, if the head is trimmed too.
- [ ] Imposition marks: fold, sewing-station and collation-ladder marks on the spine fold of each signature.
- [ ] Physical page numbers (folio): currently tiny on the outer edge for binding/debug; decide the final form.
- [ ] Foredge tab labels (decision #44): print-test the white bold reverse type (6 pt, shrinking to ~5 pt for "Paleoproterozoic Era")
      on the luma-45 grey band; if toner fills in, raise `foredge.label_size_pt` or lighten `foredge.grey`.
- [ ] Foredge tabs: check that the 0.7 mm Cenozoic band and the 2.0 mm Mesozoic band read on the closed edge, and that labels clear
      the trim (plough cut may vary from the assumed 6 mm). If the head and tail are trimmed too, shorten the slots by the trim.
- [ ] Foredge tabs: consider alternating two greys so neighbouring thin bands (Mesozoic/Cenozoic) stand apart.

### Open engine items: page overflow and layout (2026-11-23)
Planned as one full session on same-page overflows (session 5).
- [ ] Pages 913 and 914 overflow: the last events (Giordano Bruno crater on p913; Yellowstone Huckleberry Ridge on p914) are
      placed below the ruler's end and run into the footer. Cause is in the layout, not the footer.
- [ ] Page 901 overflows (Chicxulub, Deccan, _Purgatorius_, grass in dung, _Vegavis_, _Quetzalcoatlus_); the last two could move to p900 within their `t_err` (collision-pages.md).
- [ ] Find every overfull page (layout estimate reports `used` > 1) and choose a strategy: tighter spacing, shorter text, moving art,
      or letting low-`importance` events yield. Check against measured heights.
- [ ] The footer is a fixed height (decision #45), so the body must never extend into the bottom margin.
- [ ] **Wide-art bug** (p831, 840, 907): long, low outlines are scaled to full width, cropped at the left, and squeeze the caption into a
      one-word column. Fix in typeset/book.typ: cap drawing width (≤ ~60% of the text block) and set a minimum caption width (collision-pages.md).
- [ ] Then reattach the detached drawings `art/line/basilosaurus.svg` (p907) and `art/line/acanthostega.svg` (p840).
- [ ] Natural Earth maps print small labels at 520 px / font 21; tall maps shrink further (image-resources.md).
- [ ] Shard `data/events/events.json` by eon or topic once it grows (README "Data & workflow").

### Open content items: back-matter explainer "Names of geological time" (2026-11-23)
- [ ] Find a citable source for the uncited glosses (Phanerozoic "visible life"; Paleozoic/Mesozoic/Cenozoic "old/middle/new life";
      prefixes Eo- dawn, Paleo- old, Meso- middle, Neo- new); add it to sources.bib and the rows' `sources`
      (list in agent-notes/verification-backlog.md). Otherwise drop the uncited glosses.
- [ ] Read Plumb 1991 (Episodes 14: 139–140) directly; at present it is verified only through vankranendonk2012's quote. Find its DOI if one exists.
- [ ] Read Cloud 1972 directly to confirm the Hadean definition (currently via vankranendonk2012).
- [ ] Decide whether the explainer also covers periods and epochs, or stays at eons and eras (also under "Decisions needed").

### Content: research still to do
- [ ] **Empty stretches** (`./run fullness --text`, 2026-11-25), longest first: 156–173 (18), 298–313 (16), 136–149 (14), 258–270 (13),
      279–290, 113–124 (12 each), 772–782, 604–614, 474–484, 346–356, 204–214, 184–194, 44–54 (11 each), 789–798, 20–29 (10).
      Each dug stretch has a dossier with open leads in agent-notes/gaps/ (16 dossiers); summary table in content-categories.md "Future threads".
- [ ] **Open leads from dossiers** (selection; details in each dossier): Serenitatis 3.89 Ga (p136, debated), Iizuka 2007 eastern Acasta 3.94 Ga,
      Apollo 11 basalts (snape2019 full text, p196–202), Apollo 17 basalts, Manfred Complex 3.73 Ga, Bee Gorge tuff, Slave granite bloom,
      Timeball Hill tuff 2310 Ma, Scourie dykes, Meteorite Bore glaciation, Onega plateau lavas, Khondalite Belt, Kivalliq/Nueltin 1.75 Ga,
      Capricorn orogeny, North China AMCG suite, Yanliao rift, Velkerri Fm, Hongshuizhuang Fm, Bi'r Umq ophiolite, Jiangnan arcs, Heinrich 2015, Kambalda nickel.
- [ ] **Leads from sources already cited** (no new source needed): ~22 dated facts in content-categories.md "Leads from sources already cited"
      (chondrules, Mars primordial crust, third Moon-age estimate, giant-planet migration, Barberton impacts, end-Permian duration, CAMP pulses, …).
- [ ] Read the 13 Archean sources appended by another session (tice2004, tice2006, westall2015, arndt2008, huppert1984/1985, knauth2003,
      hren2009, robert2006, gaucher2008, cheney1996, zegers1998, dekock2009) (content-categories.md).
- [ ] Theme leftovers (content-categories.md "To add"): better Pangaea source than nance2014; oldest living organisms (arnaudhaond2012 full text);
      Sue the _T. rex_ (dated source); "Age of …" notes per period; human history on p914 (agriculture, writing, Ötzi; blocked by the p914 design);
      golden spikes; deep todo only if a stretch stays sparse: famous fossil sites (Burgess Shale, Chengjiang, Rhynie, Solnhofen, Messel).
- [ ] Session 16a duplicate review (second pass).

### Verification (agent-notes/verification-backlog.md)
- [ ] 23 unverified events: nuvvuagittuq-crust, mars-deuteronilus-ocean, barberton-komatiites, archaean-genetic-expansion, great-dyke-zimbabwe,
      zaonega-shungite, glenburgh-orogeny, sudbury-impact, premier-kimberlite, talakh-khaya-superchron, neoproterozoic-oxygenation,
      dickinsonia-animal, opabinia, pangaea-assembled, swillingtonia-first-conifer, late-paleozoic-ice-age, archaeopteryx,
      borealopelta-last-meal, giants-causeway-antrim-lavas, europa-young-surface, alps-rise, terror-birds-phorusrhacos, shoemaker-levy-9.
- [ ] Verified only from abstract copies found by web search (wingate1998, li1999, armstrong2005) or with "session's choice" `t_err`
      values (1.64–1.50 Ga batch, gap dig 326–374): recheck against full texts.
- [ ] cohen2013 boundaries vs ICS v2023/09; PhyloPic attribution wording.
- [ ] General-knowledge statements table (GSSP sites, Anthropocene rejection, Siccar Point, Gubbio, Hamelin Pool, year length constant): source each before use.
- [x] Footer data: replace the linear day-length demo (done 2026-11-25 with farhat2022 Table D.1; mitchell2023 plateau still open).
- [ ] Check pages of moved events (tetrapod trackways, _Montsechia_, Chorhat, Rodinia assembly) with `./run png`.

### Footer & explainers (docs/footer-candidates.md)
- [ ] Every-page candidates with sources in hand (◐): Moon distance, oxygen, sea level. Ideas only (☐): CO₂, temperature, air pressure,
      marine families, biomass, continents, tetrapod families, land-plant shares, largest living thing, insect families.
- [ ] Check-in strip (`checkin` slot, every 100 Myr): no series yet. Candidates: largest sea animal, largest land animal, largest flier, ice volume, land above sea level.
- [ ] Explainer pages per metric (pattern in footer-candidates.md): see "Explainer appendix" below.

### Explainer appendix (one page per metric; back matter, decision #22)
Drafts compile standalone to `build/explainer-<name>.pdf` and share `typeset/explainers/lib.typ` (page frame, header, text, references).
Data: `data/explainers/<name>.json`. diversity and climate are generated by `agent-notes/explainer_data.py` from downloaded datasets.
| Page | Typst / data | Graph | Sources | Draft state |
|---|---|---|---|---|
| Oxygen in the air | oxygen.typ / oxygen.json | log O₂ limits and ranges, 4 Ga–now | crowe2013, gumsley2017, planavsky2014b, scott2006 … | Draft (older layout, not yet on lib.typ) |
| Life in the sea | diversity.typ / diversity.json | marine genera per stage, Big Five marked | sepkoski2002 via jones2022, raup1982, alroy2008 | Draft, real data |
| Hothouse and icehouse | climate.typ / climate.json | temperature + CO₂ per stage (485 Ma–now), glacial sawtooth zoom | judd2024 (PhanDA), lisiecki2005 (LR04) | Draft, real data |
| The lengthening day | day-length.typ / day-length.json | day length + Moon distance, 2.46 Ga–now | reads data/series/day_length.json + moon_distance.json (farhat2022), lantink2022, meyers2018, williams2000, sonett1998, mitchell2023 | Draft, real data |
| The brightening Sun | sun.typ / sun.json | luminosity 71%→100% (Gough formula, same as the footer), faint-young-Sun zone, liquid-water evidence, ice ages, W/m² scale | gough1981, feulner2012, mojzsis2001, wilde2001, hoffman2017, rooney2013 | Draft, model curve |
| The largest living thing | largest-life.typ / largest-life.json | log max body volume, 3.5 Ga–now | payne2009 | **Placeholder curve** from the paper's text |
- [ ] Check and finalize the explainer drafts: read each page against its sources (every number in the text and labels), set wording,
      fix label placement at print size, confirm each fits one page with a printed proof.
- [ ] Largest living thing: replace the text-derived steps with Payne et al. 2009 Table S1 (Dryad doi:10.5061/dryad.223; needs a
      browser download, the API wants a login), then decide between the "relative to 3.5 Ga" axis and absolute volume (mm³ to m³).
- [ ] Life in the sea: decide genera (Sepkoski curve, drawn) vs families (footer candidate wording). No open family-level dataset:
      Sepkoski's 1992 family compendium (4,075 families) is print-only and Benton's Fossil Record 2 has no download, so a family curve
      would mean digitizing a published figure (e.g. raup1982). Simplest: switch the footer candidate to genera from diversity.json; optionally colour Sepkoski's three
      evolutionary faunas (column `fauna` in the dataset).
- [ ] Hothouse and icehouse: PhanDA starts at 485 Ma; decide whether to note Snowball Earth and older ice ages (hoffman2017) as text only.
- [ ] Lengthening day: mitchell2023 stall shown as a band only; decide whether the line should follow it.
- [ ] Move oxygen.typ onto lib.typ so all explainers share one frame; then wire the set into the back matter after the timeline
      (order, appendix title, numbering; one bibliography or the book's).
- [ ] Further explainer candidates (second tier): sea level (haq2008/haq2014 vs Miller 2005), land-plant groups (Niklas et al. 1983).

### Front & back matter
- [ ] Introduction / how to read this book: points collected in docs/introduction-notes.md (debated facts, dates and ±, spans, "now",
      citations, drawings, contamination of old life traces; possibly the whole-history overview).
- [ ] Colophon (image credits already print as a lettered list; decide what else the colophon carries).
- [ ] Appendices for full-page images and metric explainers (decision #22).
- [ ] Front-matter page for events before page 1 (presolar supernova, molecular cloud; content-categories.md "Dropped").
- [ ] Glossary appendix (22a2), front-of-book diagram (22a), cover & spine (22b).

### Art (docs/art-candidates.md, agent-notes/image-resources.md)
- [ ] 53 art-candidate rows: redraws from open-access figures, Natural Earth locator maps (`tools/basemap.py`), photo research, mini-graphs
      (oxygen oscillations, day length vs time).
- [ ] Attach ready images: `basilosaurus.svg`, `acanthostega.svg` (after the wide-art fix), `mediterranean-map.svg` (p913, after its overflow is fixed),
      _Homo sapiens_ silhouette for Jebel Irhoud (PhyloPic uuid bb3230d6-…).
- [ ] Image-fullness check (17a), then hand drawings for the longest text-only stretches.
- [ ] Unchecked image sources: IAN symbols, USGS FGDC patterns, GPlates, BHL, Wikimedia Commons, NASA/USGS/NOAA, Smithsonian.
- [ ] Map candidates: Isthmus of Panama, Paratethys, Grand Canyon, Chicxulub/Yucatán, world map of Archean rock sites.

### Documentation housekeeping
- [x] CLAUDE.md points to agent-notes/ for Claude-only notes (decision #46) (2026-11-25).
- [x] README.md feature list brought up to date: era foredge tabs (#44), footer B with check-in strip (#45), tags and importance
      (#29, #41), Names explainer, image credits, art status (2026-11-25).
- [ ] content-categories.md "Future threads" table predates the 2026-11-23 pruning (25 pages became empty again); refresh from `./run fullness --text`.
- [ ] collision-pages.md statuses dated 2026-11-21/22; refresh after the overflow session.

## Drafts and parked work
| Item | Where | State | To finish |
|---|---|---|---|
| Metric explainer pages (5) | typeset/explainers/*.typ, data/explainers/*.json | Drafts, compile standalone | See "Explainer appendix" under Footer & explainers |
| Footer design demos | docs/sketches/footer_demo.py → footer-demo.pdf, footer-demo-strips.png | Done; B chosen (#45) | Keep as reference (mock values, not cited) |
| Front-of-book diagram sketches | docs/sketches/front_diagrams.py → front-diagram-ideas.png (`./run sketches`) | Tabled (#27) | Pick D + C, another, or fold into the introduction |
| Mediterranean map | art/line/mediterranean-map.svg | Ready, unattached | Attach to Messinian/Zanclean once p913 fits |
| _Basilosaurus_, _Acanthostega_ drawings | art/line/ | Ready, unattached | Wide-art fix first |
| Introduction notes | docs/introduction-notes.md | Point list | Write the text (session 8) |
| Significance review | docs/significance-review.md | Applied 2026-11-23 | Reuse its scale for new events; second duplicate pass |
| Gap dossiers | agent-notes/gaps/ (16 files) | Living | Pick up open leads |

## Tabled ideas (💬)
- Paleogeography thumbnails via GPlates (row 18), per-page "you are here" mini-strip (row 19), short-range time-ruler brackets (row 20).
- Nested zoom insets for page 914 (session 15).
- Whole-history overview diagram (22a; docs/front-diagram-ideas.md); spine as a scaled time ribbon.
- Explainers for metrics too short for the footer (#43): human population, hominin brain size, C₄ grasslands, Antarctic ice.
- Back-matter items: Andromeda (future), biomass today.
- Trilogy: this is volume 1 of a planned trilogy; keep title, time range and scale in config.json.

## Where todos live
| File | Holds |
|---|---|
| docs/project-plan.md | This index: phases, every open item in one line |
| docs/decisions.md | Settled decisions (append only) |
| docs/collision-pages.md | Overflowing and crowded pages, wide-art bug |
| docs/content-categories.md | Theme worklist, empty-stretch leads, leads from cited sources |
| docs/art-candidates.md | Events needing drawings, maps or photo research |
| docs/footer-candidates.md | Footer metric candidates, explainer pattern |
| docs/introduction-notes.md | Points the introduction must cover |
| docs/front-diagram-ideas.md | Tabled front diagram and cover/spine ideas |
| docs/significance-review.md | Importance scale and pruning record |
| agent-notes/verification-backlog.md | Unverified events and claims |
| agent-notes/gaps/*.md | Per-stretch dossiers with open leads |
| agent-notes/image-resources.md | Image sources, unchecked libraries, map candidates |
| agent-notes/session-log.md | What each session did and planned next |
