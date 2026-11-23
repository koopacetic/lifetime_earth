# Project plan: upcoming sessions

Each session ends with: `./run check` clean, decisions appended to docs/decisions.md, PROJECT.md statuses updated,
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
