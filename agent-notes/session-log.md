# Session log

Newest first. Each entry: what was done, what was learned, and what's next. Keep entries short; details belong in
decisions.md and the other docs.

## 2026-11-25 (later): Sun explainer drafted; families question
- New: data/explainers/sun.json + typeset/explainers/sun.typ → build/explainer-sun.pdf (one page). Curve computed in Typst from the
  same Gough formula as tools/models.py; milestones 75/80/90% from its inverse. Uses its own chart width (Wl = 86 mm) to fit the
  right-hand W/m² scale inside the text block.
- Feulner 2012 read via arXiv HTML (1204.4449v1; Wiley PDF 403). Verified: H→He / mean molecular weight / core contracts and heats
  (sec 2.1); eq. 1 with t from ZAMS at 4.57 Ga; 1361 W/m² (citing Kopp & Lean 2011); frozen first 2 Gyr (abstract, 2.4); liquid
  water from 3.8 Ga, no Archean glaciation (2.2); Pongola ~2.9 Ga (global?) and Huronian 2.4–2.2 (5.1); Rye 1995 paleosol CO₂ cap
  and "CO₂ alone … unable" (5.3); greenhouse most likely (5.5). Sagan & Mullen 1972 not first (Donn 1965); not in sources.bib.
- Families: no open family-level data (palaeoverse/sepkoski has genera only; Sepkoski 1992 family compendium is print-only).
  Suggested switching the footer metric to genera; recorded in project-plan.md and footer-candidates.md.

## 2026-11-25: explainer appendix drafts (diversity, climate, day length, largest life)
**Done**
- Four one-page drafts in typeset/explainers/ on a shared lib.typ; data in data/explainers/. All compile to one page (build/explainer-*.pdf).
- New bib keys: sepkoski2002, jones2022, alroy2008, judd2024 (shared with session 4c), lisiecki2005, payne2009. wells1963 tried and dropped (no abstract to check).
- Data: Sepkoski genera from palaeoverse/sepkoski `sepkoski.rda` (read with the `rdata` pip package in a scratch venv; installing into .venv was blocked);
  PhanDA GMST+CO₂ CSV from github.com/EJJudd/PhanDA; LR04 from NOAA. Regenerate with agent-notes/explainer_data.py.
- Day-length page reads session 4c's data/series/day_length.json and moon_distance.json (do not duplicate them).
- Payne 2009 Dryad file needs a login (API 401; PMC/PNAS SI behind bot checks), so the largest-life curve is a placeholder from the paper's text.
- Typst 0.15: the drawing `path()` is gone; use `curve` / `polygon` (lib.typ `pline`, `pfill`). `typst.compile(format="png")` returns bytes for a one-page doc.
**Next:** the "Explainer appendix" checklist in docs/project-plan.md.

## 2026-11-25 (later): footer formatters
**Done**
- `display` block in series files, applied by `format_metric` in tools/build.py; modes offset (Temp), ratio (CO₂), share (Moon).
  "Today" = `common.series_now`: value at t = 0 for models, else the latest point if within the Holocene (PhanDA ends at −5,850).
  check.py validates the mode and that a present-day value exists. Decision #48.
- Number–unit space is now U+202F (no break); a plain thin space let "°C" wrap alone onto line 2.
- Full-book build at 150 ppi: line 1 fits on pp. 822–914 with 3-digit citation markers. Pixel-counting footer lines does not
  work (ruler ticks, labels share the band); crop and look instead.
- Note: tools need `.venv/bin/python` (system python3 lacks jsonschema; build.py then reports "check.py failed").

## 2026-11-25: footer series data (sky + air slots)
**Done**
- day_length.json replaced: 8 cyclostratigraphic points from farhat2022 Table D.1 (0–2.46 Ga, one tidal model, so consistent).
  Rhythmite values (Table D.2) left out: Elatina 22.27 h at 620 Ma crosses Luoyixi 21.82 h at 500 Ma.
- moon_distance.json (new, sky): same points, km. days_per_year.json is now model `year_from_day_length` (8,765.81 h ÷ day).
- co2.json and temperature.json (new, air): PhanDA stage medians (judd2024), 84 stages 0–482 Ma, `lo`/`hi` = 5th/95th pct,
  PETM row dropped. CSV: github.com/EJJudd/PhanDA 5_Outputs/PhanDA_GMSTandCO2_percentiles.csv.
- New bib key farhat2022 (judd2024 was added the same hour by the parallel explainer session, lifetime-earth-50).
- Dead ends: Farhat model curve has no public data file (arXiv 2207.00438 tables only); Krause 2018 O₂ model "on request";
  Scotese 2021 GAT tables are images; Payne 2009 SI not on Europe PMC; NCEI paleo search API did not answer.
  Foster 2017 Supp. Data 2 (LOESS CO₂, 0–420 Ma) downloads fine from static-content.springer.com: cross-check option.
**Next:** formatters (Temp vs today, CO₂ ×280, Moon rounded + %), mitchell2023 plateau decision, O₂ limit format,
life slot (alroy2008 genera, payne2009 largest; the explainer session's data/explainers/diversity.json may be reusable).

## 2026-11-23 (latest): era-level foredge tabs + names explainer
**Done**
- data/foredge.json: 11 bands (Hadean + 10 eras), each with a `label` (two lines: eon, era). book.typ draws it in white,
  vertically, inside the visible 6 mm of the band, shrunk to fit (`foredge.label_size_pt`, config). Decision #44.
- Back matter: one-page “Names of geological time” explainer before the bibliography (data/explainers/timescale-names.json;
  build.py fills start years from timescale.json; check.py validates units and sources). Gated by `--no-back`.
- check.py: foredge labels, unique slots, contiguous bands.
- New sources: vankranendonk2012 (GTS2012 Precambrian chapter; read via a public proof copy), cloud1972, plumb1991, morrell2001.
- Uncited glosses (visible life, old/middle/new life, prefixes) listed in verification-backlog.md.

**Next:** source for the Greek glosses; print test of white 6 pt reverse type on the grey band (laser toner may fill in).

## 2026-11-23: repo cleanup
**Done**
- Removed: typst_primer/, data/sources-retired.bib and its 14 abstracts, docs/typesetting-questions.md (open items moved to
  project-plan.md), `./run single`, `./run footers`, and the check-in footer mode (build.py `--footer`, book.typ, config). Decision #42.
- Renamed data/events/demo.json → events.json. CLAUDE.md and project-plan.md now point to README.md (PROJECT.md never existed).
- Parked and kept: front-diagram sketches, oxygen explainer draft, mediterranean map, detached basilosaurus/acanthostega drawings.

## 2026-11-23: significance review, pruning, importance pass
**Done**
- docs/significance-review.md: 48 weak events reviewed (local specimens, ores, regional dykes and orogenies,
  duplicates). User approved; applied: 34 removed (16 cut, 18 merged into the event telling the global story),
  388 → 354 events. Maps from `prinsep-orogeny` and `dominion-group-volcanism` moved to `pilbara-nucleus-rifts`
  and `kaapvaal-craton-stable`. 25 pages became empty again (pp 89, 122, 123, 141, 143, 160, 165, 189, 263, 300, 303, 370, 399, 409, 453, 455, 464, 530, 566, 578, 584, 620, 668, 738, 740).
- `importance` set on every event (scale 1–5 in the review doc); decision #41.
- 14 sources used only by cut events moved to `data/sources-retired.bib` (the bibliography prints all of
  sources.bib). `brasier1994` and `rooney2015` were already unused; left in place.
- dig-gap dossiers get an "Imp." column; fill-gaps and add-events ask for `importance`. Gap dossiers, art-candidates,
  verification-backlog annotated for removed ids. `tumbiana-modern-bacteria` moved to introduction-notes.
- project-plan.md: session 16a, duplicate review.

- Reframes with new sources: ALH84001 life claim (mckay1996), Homestake neutrino detector (davis1990,
  cleveland1998), Wiborg rapakivi in St Petersburg (bulakh2020); verified from abstracts.

**Open:** `importance` is not yet used by the layout beyond "who yields".

## 2026-11-23 (later): four parallel gap digs on the longest stretches (736–749, 556–568, 396–408, 142–154)
**Done**
- Same setup (one dig-gap subagent per stretch, pre-approved adds, no commits). 19 events, 24 sources.
- 736–749 (895–825 Ma), 6 verified: Big Cottonwood 18.9 h day (p735), Little Dal sponge reefs (debated, p737), Nchanga granite (p738),
  Moine metagabbros (p740), Manso dykes (p743), Gairdner dykes + South China plume (debated, p749). Longest empty run now p744–748.
  Caveat: wingate1998, li1999, armstrong2005 marked verified from abstract copies found via web search, not the publisher page.
- 556–568 (1.795–1.73 Ga), 6 verified: Avanavero LIP (p556), Xiong'er LIP, Korosten pluton, Big Sky orogeny span (p559→573),
  McDermott eukaryotes (debated, p564), Homestake gold (p567).
- 396–408 (2.595–2.53 Ga), 5 events: Marra Mamba BIF (p395), Salobo Cu–Au (p399), Great Dyke (p400, unverified size/PGE claim),
  Campbellrand platform span (p403→411), Gamohaan sulfur bacteria (p411).
- 142–154 (3.865–3.80 Ga), 2 verified: Napier Gage Ridge gneiss (p143), Akilia earliest-life claim (debated, p150). Rest honestly empty.
- 11 art-candidate rows; no art fetched (PhyloPic has no _Thiomargarita_ or acritarchs). Totals: 388 events, 438 sources,
  25 unverified, 0 errors; pages with entries 245 → 260.
- OpenAlex daily quota was hit during this run.
**Next**
- Longest empty stretches now: 279–290 (12), 772–782, 604–614, 474–484, 346–356 (11 each).
- Proposed leads: Bi'r Umq ophiolite, Jiangnan arcs, Kivalliq/Nueltin 1.75 Ga, Capricorn orogeny, Slave granite bloom,
  Bee Gorge tuff, Serenitatis 3.89 Ga (p136, debated); details in each dossier.

## 2026-11-23: four more parallel gap digs (113–130, 452–468, 570–585, 436–450)
**Done**
- Same setup as the previous entry (flock, pre-approved adds), plus per-agent scratchpad folders and PNG copies. 20 events, 22 sources.
- 113–130 (4.01–3.92 Ga), 3 verified: Acasta 3.962 Ga gneiss (p122), Beartooth zircons (p123), Saglek graphite life (debated, p125).
  Longest empty run now p113–121.
- 452–468 (2.315–2.23 Ga), 6 events: Gordon Lake ash and Karelian dykes (unverified, p453), Xiong'ershan arc (debated span),
  oxygen oscillations 2.32–2.22 Ga (debated span, poulton2021), Ippaguda LIP (p464), Malley dykes (p468). Longest empty run now p456–460.
- 570–585 (1.725–1.645 Ga), 6 verified: Labradorian orogeny (span), Grand Canyon basement metamorphism (p574), Broken Hill ore (p578),
  Changcheng microfossils (p583), Mount Isa ore (p584), Mazatzal orogeny (p585). Longest empty run now p579–582.
- 436–450 (2.395–2.32 Ga), 5 verified: Arrowsmith orogeny (p439), Dharwar giant dyke swarm (p441), tectono-magmatic lull span
  (debated; spencer2018 added as third source), Hotazel manganese and Ongeluk fungus-like fossils (debated, both p435). Longest empty run now p442–448.
- 9 art-candidate rows; no art fetched. Totals: 369 events, 414 sources, 24 unverified, 0 errors; pages with entries 228 → 245.
**Next**
- Longest empty stretches now: 736–749 (14), 556–568, 396–408, 142–154 (13 each), 279–290 (12).
- Proposed leads: Iizuka 2007 eastern Acasta 3.94 Ga, Timeball Hill tuff 2310 Ma, Scourie dykes ~2375 Ma, Meteorite Bore glaciation,
  North China anorthosite–rapakivi suite, Yanliao rift ~1680 Ma; Elsevier abstracts unreachable for several.

## 2026-11-22 (latest): four parallel gap digs (616–634, 516–534, 156–174, 76–94)
**Done**
- Four subagents ran dig-gap at once on the four 19-page stretches, adding their strongest candidates without
  waiting for approval. Shared-file writes went through `flock` (lock file in the session scratchpad). 23 events added, 23 sources.
- 616–634 (1.495–1.40 Ga), 8 events, all verified: Sullivan ore, Pea Ridge iron (p620), Belt basin span, _Horodyskia_
  (debated, p625), Michael–Shabogamo gabbro span, Tieling oxygenation (debated, p626), Antarctic–Laurentian granite (p627),
  granite–rhyolite provinces span (prints p615/647). Longest empty run now p616–619.
- 516–534 (1.995–1.90 Ga), 7 events: Purtuniq ophiolite (p515), Zaonega shungite (unverified) and first phosphorites (p520),
  Glenburgh orogeny (unverified, p523), Jormua ophiolite (p525), Pechenga nickel (p530), Snowbird eclogites (p534). Longest empty run now 4 pages.
- 156–174 (3.795–3.70 Ga), 3 events: Anshan oldest China rocks (unverified, p160), Acasta reheated (p165),
  Isua fore-arc sediments (p174). Longest empty run now p166–173.
- 76–94 (4.195–4.10 Ga), 5 events, all verified: Mount Narryer zircons (p85), Cathaysia Hadean zircon (p89), Mars magnetization
  stops (debated, p90), zircon inclusions/subduction (debated, p94), ALH84001 crystallizes (p96). Longest empty run now p76–84.
- 12 art-candidate rows; no art fetched (PhyloPic has no _Horodyskia_). Dossiers in agent-notes/gaps/ for each stretch.
- Totals: 349 events, 392 sources, 23 unverified, 0 errors; pages with entries 207 → 228.
**Learned**
- Parallel agents share build/png (renders clear each other's PNGs: copy right after rendering) and the scratchpad (use per-agent subdirs).
**Next**
- Longest empty stretches now: 113–130 (18), 452–468 (17), 570–585 (16), 436–450 (15), 736–749 (14).
- Proposed leads in the new dossiers: Velkerri Fm (p631), Hongshuizhuang Fm (p623), Onega plateau lavas, Khondalite Belt,
  Manfred Complex anorthosite (p169), Apollo 17 basalts, Serenitatis basin (p73).

## 2026-11-22 (later): gap dig, pages 666–694
**Done**
- Largest stretch 666–694 (1.245–1.10 Ga, 29 pages): 10 events added, 9 verified from abstracts; 11 sources (all cached).
  In the stretch: Sudbury dykes (p668), Musgrave and Shawinigan orogenies (spans), Stac Fada impact (p679), Premier
  kimberlite (p685, unverified: Cullinan-diamond clause), Umkondo LIP (p693), Midcontinent Rift span (p693–698).
  Just outside: fossil chlorophyll (p695), eukaryote chloroplasts ~1.25 Ga (p665, debated), Argyle diamonds (p658).
  Dossier agent-notes/gaps/666-694.md; 3 art-candidate rows (Stac Fada map, Midcontinent Rift map, Cullinan diamond).
- dig-gap skill: candidates are now numbered in the dossier and the presented table.
**Next**
- Longest empty stretches now 19 pages each: 616–634, 516–534, 156–174, 76–94.

## 2026-11-22 (later): gap dig, pages 176–202
**Done**
- Second-largest stretch 176–202 (3.695–3.56 Ga, 27 pages): 6 events added; dossier agent-notes/gaps/176-202.md.
  `isua-terranes-collide` (p181, debated), `ancient-gneiss-complex` (p183), `isukasian-orogeny` (span, p183/195),
  `pilbara-crustal-overturn` (span, p195/232, debated), `mars-deuteronilus-ocean` (p195, unverified),
  `isua-magnetic-field` (p175). suavet2013 added as a source on `lunar-dynamo-strong`.
- 6 sources: suavet2013, wiemer2018, nutman2013, ivanov2017, zeh2011, nichols2024 (all but ivanov2017 verified from abstracts).
- 2 art-candidate rows (SW Greenland locator map, Pilbara dome-and-keel section). Longest empty run inside is now 184–194.
- Tooling: OpenAlex search from a script got 429; Crossref search + `tools/source_cache.py` worked. Elsevier/core.ac.uk/oro block fetches.
**Next:** snape2019 full text (Apollo 11 basalts ~3.58 Ga, would fill p196–202); verify ivanov2017; next stretches 666–694 (another session is on it), 616–634.

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
- New skill `.claude/skills/dig-gap` (deep-dive one stretch; dossier per stretch in `agent-notes/gaps/`). Art policy in
  dig-gap and add-events: attach only fetchable images (PhyloPic); drawings, maps and diagrams go to art-candidates.md.
- Largest stretch 326–374 (2.945–2.70 Ga): 9 events added, all verified from abstracts (Pongola glaciation,
  Witwatersrand gold, Moon volcanism wanes, Klipriviersberg basalts, Zimbabwe flare, oldest magnetic reversal,
  Tumbiana bacteria and stromatolites, Kenoran orogeny on p377); 10 sources. Dossier: agent-notes/gaps/326-374.md.
- 4 art-candidate rows (Kaapvaal map, reversal diagram, dropstone, Tumbiana stromatolite).
**Next**
- Pages 326–334 still empty; next largest stretches 666–704 and 276–314 (`/dig-gap`).

## 2026-11-21 (late night): verification pass 2
**Done**
- 120 of 131 unverified events checked and set `verified: true` (210 of 221 now); 16 corrections (dates moved to ICS
  stages, unsupported clauses removed, two sources added). Details and the 11 still-unverified events at the top of
  agent-notes/verification-backlog.md.
- `tools/source_cache.py`: publisher landing-page fallback, `--refetch` and `--refetch-missing`; verification notes kept.
  34 cache files got `## Verification` notes; Rämö 2014 abstract from its open PDF. New source thomson2011.
- New skill `.claude/skills/verify-sources`.
**Next**
- Sources for the 11 remaining events (backlog table); cohen2013 boundaries vs ICS v2023/09; check pages of moved
  events (tetrapod trackways, Montsechia, Chorhat, Rodinia assembly) with `./run png`.

## 2026-11-21 (night, later): gap dig 276–314 (3.195–3.0 Ga)
**Done**
- Dossier agent-notes/gaps/276-314.md. 8 events (p278–314): Pilbara rifting, Whundo arc, Kaapvaal craton, Cleaverville BIF,
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
- agent-notes/image-resources.md: image sources with hints (PhyloPic, Natural Earth, Bioicons, IAN, FGDC, GPlates, BHL...).
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
- Demo data: 6 events, 3 footer series, 1 drawing, all cited **from memory** → agent-notes/verification-backlog.md.
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
