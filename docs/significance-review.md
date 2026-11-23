# Significance review: low-value events

_Reviewed: 2026-11-23, all 388 events. Approved and applied the same day (decision #41); the table below is the
proposal as reviewed, the outcome follows it._

## Outcome (applied 2026-11-23)
- **34 events removed**, 388 → 354. 16 cut: `anshan-oldest-china`, `napier-gage-ridge-gneiss`, `nchanga-granite`,
  `korosten-pluton`, `cleaverville-iron-formation`, `salobo-copper-gold`, `pechenga-nickel`, `pea-ridge-iron`,
  `karelian-dykes-231`, `ippaguda-lip`, `sudbury-dykes`, `michael-shabogamo-gabbro`, `moine-metagabbros`,
  `big-sky-orogeny`, `labradorian-orogeny`, and `tumbiana-modern-bacteria` (moved to docs/introduction-notes.md).
- **18 merged** (fact and source folded into the target; each target's `notes` lists what it absorbed):
  Hadean zircons → `mount-narryer-zircons` (retitled "Continents already exist"); `acasta-gneiss-3962`,
  `acasta-reheated` → `acasta-gneiss`; `spa-second-impact-3870` → `late-heavy-bombardment`; `gordon-lake-ash` →
  `huronian-glaciation`; `marra-mamba-iron-formation` → `banded-iron-peak`; `prinsep-orogeny` (with its Pilbara
  map) → `pilbara-nucleus-rifts`; `dominion-group-volcanism` (with its Kaapvaal map) → `kaapvaal-craton-stable`;
  Broken Hill, McArthur River, Sullivan → `mount-isa-ore` (now a 1,690–1,640 Ma span on Australia's lead–zinc
  giants); `midcontinent-rift-plume` → `midcontinent-rift`; `xiongershan-arc` → `tectono-magmatic-lull`;
  `isukasian-orogeny` → `isua-terranes-collide`; `archean-impact-s2` → `impacts-boil-oceans`; `wittenoom-impact`
  → `jeerinah-impact`; `moodies-microfossils` → `moodies-land-mats`.
  (Changed from the proposal: Dominion and Prinsep merged instead of cut, to keep their maps; Pilbara and Kaapvaal
  stay two events, each retitled as an early stable continent.)
- **Retitled**: `ancient-gneiss-complex`, `klipriviersberg-flood-basalts` (Ventersdorp), `shawinigan-orogeny`
  (Grenville in three stages).
- **Importance set on all 354 events** (81 were unset): 25 at 5, 90 at 4, 167 at 3, 72 at 2, none at 1. Also
  raised for the threads the book should foreground: magnetic field (`geodynamo-3450`, `brunhes-matuyama-reversal`,
  superchrons), `vredefort-impact`, `rodinia-breakup`.
- **Reframes done** (same day, sources added and checked against abstracts): `alh84001-crystallizes` (1996
  'life on Mars' claim, mckay1996; tagged `debated`), `homestake-gold` (the mine's solar-neutrino detector from 1970,
  davis1990, cleveland1998), `wiborg-rapakivi` (St Petersburg's building stone, bulakh2020). All three now importance 3.
- Removed events' sources stay in `sources.bib` (unused).

## Why
Gap digs aim at "everything datable", so sparse Archean and Proterozoic stretches filled up with local records:
a zircon found here, a dyke swarm there, an ore body's age. Each is true and cited, but a reader learns little
from them compared with plate tectonics, reversals, oxidation or glaciations.

## Scale: the existing `importance` field (1–5, default 3)
The schema already has `importance` ("will drive emphasis and who yields in crowded pages"); 81 events have none.
Proposed meaning, used here and in the gap dossiers:
| importance | Meaning | Examples |
|---|---|---|
| 5 | **Era-defining**: a turning point every reader should meet | `great-oxidation`, `end-permian-extinction`, `moon-forms` |
| 4 | **Global story**: changes the whole Earth or a major lineage | `oldest-magnetic-reversal`, `columbia-nuna`, `vredefort-impact` |
| 3 | **Support**: regional, but illustrates a global story, names a place readers know, or is a strong curiosity | `kaapvaal-craton-stable`, `snowbird-eclogites`, `argyle-diamonds` |
| 2 | **Filler**: local record worth having only where the stretch is otherwise empty | `josefsdal-hydrothermal-mats`, `mazatzal-orogeny` |
| 1 | **Prune**: a specimen, deposit or regional rock unit whose point is "this rock here is this old"; cut or merge | `beartooth-zircons`, `sudbury-dykes`, `sullivan-ore` |

Rule of thumb: if the title only makes sense to a geologist who knows the place, it is a 1 or 2. Many can move up
by leading with what they show about the Earth ("Continents already exist" instead of "Mount Narryer zircons").

## Candidates
"Events ±5 pp" = other events within 5 pages: a low number means cutting re-opens a gap. Actions:
**Cut**; **Merge** (fold the fact and its source into the named event, delete this one); **Reframe** (keep,
rewrite title and text around the global point); **Keep only if the stretch stays empty** (importance 2).

| Id | Page | Events ±5 pp | Importance now → proposed | Action | Why |
|---|---|---|---|---|---|
| **A. Specimens: "oldest X found at Y"** | | | | | |
| `cathaysia-hadean-zircon` | 89 | 3 | – → 1 | Merge into `mount-narryer-zircons` | Third Hadean-zircon entry; point (crust existed) already made |
| `beartooth-zircons` | 123 | 2 | 1 → 1 | Merge into `mount-narryer-zircons` or cut | Same point, Montana |
| `acasta-gneiss-3962` | 122 | 2 | 2 → 1 | Cut | History-of-science duplicate of `acasta-gneiss` |
| `acasta-reheated` | 165 | 1 | 1 → 1 | Cut | A metamorphic date of a rock already in the book |
| `anshan-oldest-china` | 160 | 2 | 2 → 1 | Cut, or merge into a span "oldest rocks on each continent" | National record |
| `napier-gage-ridge-gneiss` | 143 | 2 | 2 → 1 | Cut or reframe (crust recycling) | Antarctic record; only the Hf-isotope point is general |
| `ancient-gneiss-complex` | 183 | 1 | 3 → 2 | Reframe as "crust remelts older crust" or cut | Eswatini record |
| `spa-second-impact-3870` | 141 | 2 | 2 → 1 | Merge into `late-heavy-bombardment` | Sample-level detail |
| `nchanga-granite` | 738 | 4 | – → 1 | Cut | Only a maximum age for a basin |
| `korosten-pluton` | 559 | 3 | 1 → 1 | Cut | Regional pluton |
| `wiborg-rapakivi` | 588 | 10 | 2 → 2 | Reframe (rapakivi as building stone, St Petersburg) or cut | Type-locality fact |
| `gordon-lake-ash` | 453 | 5 | 2 → 1 | Merge into `huronian-glaciation` | A dating bracket, not an event |
| `cleaverville-iron-formation` | 297 | 3 | 2 → 1 | Cut (BIF story told by `banded-iron-peak`) | One more BIF unit |
| `marra-mamba-iron-formation` | 395 | 4 | 3 → 1 | Merge into `banded-iron-peak` | One more BIF unit |
| `klipriviersberg-flood-basalts` | 357 | 0 | 3 → 2 | Reframe as the Ventersdorp LIP | Title is about bracketing the gold's age |
| `tumbiana-modern-bacteria` | 370 | 6 | 2 → 2 | Move to introduction (contamination caveat) | Method warning, not an event of 2.7 Ga |
| `alh84001-crystallizes` | 96 | 2 | – → 3 | Reframe: mention the 1996 'life on Mars' claim | Famous rock, but text gives only isotope ages |
| `mount-narryer-zircons` | 85 | 2 | – → 3 | Reframe title: "Continents already exist" | Keep the point, lose the find-story focus |
| **B. Ore deposits** | | | | | |
| `salobo-copper-gold` | 399 | 4 | 2 → 1 | Cut | Regional ore age |
| `pechenga-nickel` | 530 | 4 | 3 → 1 | Cut | Regional ore age |
| `broken-hill-ore` | 578 | 2 | 2 → 1 | Merge: one "age of giant lead–zinc ores" entry | Four lead–zinc giants within 165 Myr |
| `mount-isa-ore` | 584 | 9 | 2 → 1 | Merge (as above) |  |
| `mcarthur-river-zinc` | 587 | 10 | 2 → 1 | Merge (as above) |  |
| `sullivan-ore` | 620 | 4 | 2 → 1 | Merge (as above) |  |
| `pea-ridge-iron` | 620 | 4 | 2 → 1 | Cut |  |
| `homestake-gold` | 567 | 3 | 2 → 2 | Reframe (Homestake mine later hosted the solar-neutrino experiment) or cut | Curiosity needs a source |
| **C. Regional dykes, sills and LIPs** | | | | | |
| `karelian-dykes-231` | 453 | 5 | 2 → 1 | Cut |  |
| `ippaguda-lip` | 464 | 3 | 2 → 1 | Cut |  |
| `sudbury-dykes` | 668 | 2 | 2 → 1 | Cut |  |
| `michael-shabogamo-gabbro` | 627 | 6 | 2 → 1 | Cut |  |
| `moine-metagabbros` | 740 | 4 | – → 1 | Cut |  |
| `midcontinent-rift-plume` | 695 | 4 | – → 1 | Merge into `midcontinent-rift` | Two entries for one event |
| `granite-rhyolite-provinces` | 631 | 6 | 2 → 2 | Keep only if the stretch stays empty |  |
| `xiongershan-arc` | 455 | 4 | 2 → 1 | Merge into `tectono-magmatic-lull` | Counter-example to the lull |
| `dominion-group-volcanism` | 300 | 4 | – → 1 | Cut |  |
| **D. Regional orogenies and terranes** | | | | | |
| `prinsep-orogeny` | 303 | 1 | – → 1 | Cut |  |
| `isukasian-orogeny` | 189 | 0 | 2 → 1 | Cut or merge into `isua-terranes-collide` |  |
| `big-sky-orogeny` | 566 | 3 | 2 → 1 | Cut |  |
| `labradorian-orogeny` | 584 | 9 | 2 → 1 | Cut |  |
| `shawinigan-orogeny` | 681 | 3 | 3 → 2 | Reframe as "Grenville mountains build" (Rodinia) |  |
| `pilbara-nucleus-rifts` | 278 | 2 | 2 → 1 | Merge with `kaapvaal-craton-stable` into "first stable continents" |  |
| `glenburgh-orogeny` | 523 | 4 | 3 → 2 | Keep only if the stretch stays empty |  |
| `mazatzal-orogeny` | 585 | 9 | 2 → 2 | Keep only if the stretch stays empty (Arizona; US readers) |  |
| **E. Near-duplicates and repeated microfossils** | | | | | |
| `archean-impact-s2` | 263 | 0 | 3 → 1 | Merge with `impacts-boil-oceans` | Same Barberton impacts told twice |
| `wittenoom-impact` | 409 | 3 | – → 1 | Merge into a "three great impacts, 2.63–2.48 Ga" entry | With `jeerinah-impact`, `dales-gorge-kuruman-impact` |
| `moodies-microfossils` | 275 | 3 | – → 1 | Cut or merge with `moodies-land-mats` |  |
| `josefsdal-hydrothermal-mats` | 249 | 1 | 3 → 2 | Keep only if the stretch stays empty | Repeats the Buck Reef point |
| `gamohaan-sulfur-bacteria` | 411 | 4 | 3 → 2 | Keep only if the stretch stays empty |  |

## Looked at and kept
Ores and rocks with a recognisable name or a global link: `witwatersrand-gold` (over a third of the world's gold),
`hotazel-manganese` (tied to the Great Oxidation), `zaonega-shungite` (a 2-billion-year-old oil field),
`argyle-diamonds`, `premier-kimberlite` (Cullinan), `gawler-range-volcanics` (Olympic Dam),
`belt-basin` (Glacier National Park), `grand-canyon-basement-metamorphism`. Magmatism that pins a supercontinent
or is planet-scale: `mackenzie-lip`, `umkondo-lip`, `manso-dykes`, `gairdner-dyke-swarm`, `malley-dykes`,
`avanavero-lip`, `dharwar-giant-dyke-swarm`, `xionger-lip`, `great-dyke-zimbabwe`, `bushveld-complex`.
Tectonic firsts: `isua-terranes-collide`, `kaapvaal-craton-stable`, `snowbird-eclogites`, `purtuniq-ophiolite`,
`jormua-ophiolite`, `arrowsmith-orogeny` (mountain-building during the lull), `musgrave-orogeny`.

## Summary
- 48 events reviewed as weak (12% of the book): 35 proposed importance 1 (21 cuts, 14 merges), 11 importance 2
  (reframes and placeholders), 2 importance 3 after a reframe.
- Clusters: the Hadean–Eoarchean "oldest rock in country X" run (pp 85–183), the 1.69–1.47 Ga lead–zinc and
  iron ores (pp 578–620), Paleoproterozoic dyke swarms (pp 441–468), regional orogenies (pp 189–585).
- Most sit in stretches with 0–4 neighbours, so cutting them re-opens gaps. Honest empty pages are allowed
  (dig-gap rule); better fillers there are global threads that run through as spans (supercontinent cycle,
  BIF era, magmatic lull, boring billion).
- 81 events have no `importance` and the current values were set ad hoc (26 of the 48 above are already at 2,
  3 at 1). A full pass setting `importance` on every event would make the field usable for layout.
- Next step: approve or edit the proposed column, then apply cuts, merges and `importance` values in one pass.
