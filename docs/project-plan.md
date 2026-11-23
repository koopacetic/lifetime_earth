# Project plan: upcoming sessions

Each session ends with: `./run check` clean, decisions appended to docs/decisions.md, README.md statuses updated,
a short entry at the top of docs/session-log.md, and verification-backlog.md updated for any unverified facts.

## Phase 1: Foundations
| # | Session | Output |
|---|---|---|
| 1 | ✅ **Design & scaffold** (2026-11-19) | Folder structure, schema, tools, Typst demo, docs |
| 2 | ✅ **Physical decisions** (2026-11-20) | Sheet/paper/printer/trim answered; foredge prototype; ruler on foredge; footer and art demos |
| 2b | **Imposition & first print test** | `tools/impose.py` (booklet sheets per signature, padding, creep, marks); print, fold, sew and trim one test signature; measure the printer's non-printable margin, registration, trim and gutter |
| 3 | **Typography & page design** | Font, sizes, ruler, header/footer, event block styles, mirrored margins, registration; print test spreads |
| 4 | **Foredge test** | Decide the band set (eons vs life milestones); bleed and trim test on a dummy stack of signatures |

## Phase 2: Engine
| # | Session | Output |
|---|---|---|
| 5 | **Engine hardening & verification** | Layout calibrated with Typst measurements (`metadata` + `typst.query`); overflow strategy; spans; full timescale (periods/epochs); pytest for page math; fullness from measured heights |
| 6 | **Event taxonomy & schema finalization** | User's event-type list → schema (`cat`/types), styling hooks, fullness per type |
| 7 | **Footer metrics research** | Cited series: day length, O₂, CO₂, temperature, land %, sea level, luminosity, Moon distance, land animal diversity; footer design or 100 Myr check-ins |
| 8 | **Front & back matter** | Intro text, contents, colophon or credits generator, appendices, index decision |

## Phase 3: Content (deep research sessions; use the `add-events` / `fill-gaps` skills)
Started early (2026-11-20). Worklist by theme: docs/content-categories.md. Sessions may go theme by theme instead of eon by eon.
| # | Session | Pages |
|---|---|---|
| 9 | Solar System formation & Hadean | 1–107 |
| 10 | Archean (2 sessions) | 108–414 |
| 11 | Proterozoic (2–3 sessions) | 415–807 |
| 12 | Paleozoic | 807–864 |
| 13 | Mesozoic | 864–901 |
| 14 | Cenozoic (not the final page) | 901–913 |
| 15 | **Final page & human history**: zoom insets / compaction design plus content | 914 |
| 16+ | Gap filling by fullness report; verification passes (`verified: true`) | all |
| 16a | **Duplicate review** (to circle back): find events that tell the same story twice (same rock, impact, sample or claim under different ids, e.g. `archean-impact-s2` vs `impacts-boil-oceans`), and series of near-identical records (one more zircon, BIF or dyke swarm). `./run add` only catches near-duplicates at insert time (close `t` and shared title words), so also check across wider time gaps and by shared sources. Merge or cut; see docs/significance-review.md | all |

## Phase 4: Art & extras
| # | Session | Output |
|---|---|---|
| 17 | Illustration pipeline: ✅ basic fetch/outline/credits; choose taxa per era, check style consistency; work through docs/art-candidates.md (hand drawing, photo research) | `art/`, `art/credits.json` |
| 17a | **Hand-made images** (to circle back): draw SVGs for events no image library covers (stromatolite vs folded rock at Isua, O₂ mini-graph, banded iron, zircon with a hair for scale, Snowball rock column, prokaryote vs eukaryote cell; list in docs/image-resources.md). First build an **image-fullness** check (like `./run fullness`, but counting pages that have art): report the longest stretches with only text or blank pages, to pick where drawings help most | `art/line/`, image-fullness report |
| 18 | Paleogeography thumbnails (GPlates) — tabled idea | maps every N pages |
| 19 | Mini-strip "you are here" — tabled idea | per-page strip |
| 20 | Short-range time-ruler brackets — tabled idea | ruler annotations |

## Phase 5: Production
| # | Session | Output |
|---|---|---|
| 21 | Citation audit (every source opened and checked), final fullness pass | clean report |
| 22 | Full proof print of one volume's worth of signatures; fix | — |
| 22a | **Front-of-book diagram** (tabled): pick from docs/front-diagram-ideas.md or fold into the introduction | diagram or text |
| 22a2 | **Glossary appendix** (to circle back): dictionary of science terms used across all events (e.g. orogeny, rapakivi, euxinic, acritarch, stem/crown group). Could be generated from a `data/glossary.json` plus a check that flags undefined jargon in event text; needs a schema decision. **Rule:** a term used in only one event gets a short definition in-line (or right after the event text); a term used in a handful (≈5) or more events gets a fuller definition and explanation in the glossary. A usage count per term decides which | appendix pages |
| 22b | **Cover & spine**: discuss and draft printable designs for test prints | cover/spine PDFs |
| 23 | Final print, bind | the book |

## Open physical-book items (carried over from the retired typesetting Q&A, 2026-11-20)
Settled answers are in docs/decisions.md. Still open, for the print-test sessions (2b, 3, 4, 22):
- Printer: measure the non-printable margin and front/back registration.
- Show-through: check back-to-back registration of ruler and labels on 24 lb paper.
- Gutter loss and creep: tune the 20 mm inside margin; optional per-sheet creep shift in `impose.py`.
- Signature size (4 sheets = 16 pages) and the page-count padding: revisit after printing.
- Spreads as 10 Myr views: continuation marks at the bottom of left pages and the top of right pages?
- Head-edge bands: a second band set on the head, if the head is trimmed too.
- Imposition marks: fold, sewing-station and collation-ladder marks on the spine fold of each signature.
- Foredge tab labels (decision #44): print-test the white bold reverse type (6 pt, shrinking to ~5 pt for "Paleoproterozoic Era")
  on the luma-45 grey band; if toner fills in, raise `foredge.label_size_pt` or lighten `foredge.grey`.
- Foredge tabs: check that the 0.7 mm Cenozoic band and the 2.0 mm Mesozoic band read on the closed edge, and that labels clear
  the trim (plough cut may vary from the assumed 6 mm). If the head and tail are trimmed too, shorten the slots by the trim.
- Foredge tabs: consider alternating two greys so neighbouring thin bands (Mesozoic/Cenozoic) stand apart.

## Open engine items: page overflow (2026-11-23)
Planned as one full session on same-page overflows.
- [ ] Pages 913 and 914 overflow: the last events (Giordano Bruno crater on p913; Yellowstone Huckleberry Ridge on p914) are
      placed below the ruler's end and run into the footer. The same happens with the old footer, so the cause is in the layout, not the footer.
- [ ] Find every overfull page (the layout estimate in `tools/common.py` reports `used` > 1?) and choose a strategy:
      tighter spacing, shorter text, moving art, or letting low-`importance` events yield. Check against measured heights (session 5).
- [ ] The footer is now a fixed height (decision #45), so the body must never extend into the bottom margin.

## Open content items: back-matter explainer "Names of geological time" (2026-11-23)
- [ ] Find a citable source for the uncited glosses (Phanerozoic "visible life"; Paleozoic/Mesozoic/Cenozoic "old/middle/new life";
      prefixes Eo- dawn, Paleo- old, Meso- middle, Neo- new); add it to sources.bib and the rows' `sources`
      (list in verification-backlog.md). Otherwise drop the uncited glosses.
- [ ] Read Plumb 1991 (Episodes 14: 139–140) directly; at present it is verified only through vankranendonk2012's quote. Find its DOI if one exists.
- [ ] Read Cloud 1972 directly to confirm the Hadean definition (currently via vankranendonk2012).
- [ ] Decide whether the explainer also covers periods and epochs (they appear in the running heads), or stays at eons and eras.
