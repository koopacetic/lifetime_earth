# Footer metric candidates

The footer prints a terse line of metrics on every page (decision #23). The metrics in use now are Sun, Day, Year and Moon (sky) and CO₂ and Temp (air)
(`data/series/`). This file lists candidates. Each needs cited values or a cited model, and prints only where one
exists (decision #20). Each metric may also get a **one-page explainer** in an appendix: one graph of the
whole history, what it shows, how it is known and how sure. Drafts in `typeset/explainers/` (data in `data/explainers/`):
oxygen, diversity (marine genera), climate (temperature + CO₂), day-length (with Moon distance), largest-life. Status in project-plan.md, "Explainer appendix".

Status: ☑ in use · ◐ sources in hand · ☐ idea only

| ☐ | Metric | Footer form | Sources in hand / leads | Notes |
|---|---|---|---|---|
| ☑ | Sun brightness | `Sun 94% of today` | gough1981 (model) | Whole book. Explainer drafted (typeset/explainers/sun.typ): milestones 75/80/90%, faint-young-Sun zone (feulner2012). |
| ☑ | Day length | `Day 21.9 h` | farhat2022 Table D.1 (cyclostratigraphy, recomputed with one tidal model): 0, 55, 270, 445, 493, 500 Ma, 1.4 Ga (meyers2018), 2.46 Ga (lantink2022) | Done 2026-11-25. Blank before 2.46 Ga. **Open:** mitchell2023's ~19 h plateau (2–1 Ga) is not shown by linear interpolation; add plateau points? Rhythmite values left out (they cross the curve). |
| ☑ | Days per year | `Year 393 days` | computed: 8,765.81 h ÷ day length (`year_from_day_length` in tools/models.py; orbit fixed as in farhat2022) | Done 2026-11-25: derived, so it always agrees with Day. |
| ☑ | Moon distance | `Moon 97%` | farhat2022 Table D.1, same points as Day; stored in km, today = 383,598 km (long-term mean, Laskar 2004) | Done 2026-11-25 (sky slot, every page from 2.46 Ga). Prints the share of today's distance only, so line 1 fits (decision #48). |
| ◐ | Oxygen | `O₂ ≤0.02%` or `O₂ ~21%` | crowe2013, gumsley2017, planavsky2014b, scott2006, berner2006, krause2018, machta1970 | Mostly limits, not values: needs a format for "below" and "range" (e.g. `O₂ <0.0002%`). Draft explainer done. |
| ☑ | CO₂ | `CO₂ 8.1×` | judd2024 (PhanDA stage medians, 5–95% in `lo`/`hi`), 0–482 Ma | Done 2026-11-25 (air slot). Multiple of the Holocene median, 276 ppm (≈ pre-industrial). Cross-check: Foster et al. 2017 LOESS fit (0–420 Ma, Nat. Commun. 8:14845, Supp. Data 2). |
| ☑ | Global temperature | `Temp +16 °C` | judd2024 (PhanDA GMST stage medians), 0–482 Ma | Done 2026-11-25 (air slot). Difference from the Holocene median, 14.0 °C. Scotese 2021 tables are images only. |
| ◐ | Sea level | `Sea +240 m` | haq2008 (Paleozoic), haq2014 (Cretaceous); leads: Miller et al. 2005 (last 100 Myr) | Phanerozoic only. |
| ☐ | Air pressure | `Air <0.5 bar` | som2016 (<0.5 bar at 2.7 Ga), som2012 (< 2× density) | Only limits at 2.7 Ga; probably explainer only. |
| ☐ | Marine families | `Families: sea 450 (40%)` | raup1982; leads: Sepkoski family compilation, Alroy et al. 2008 | Marine animals, Phanerozoic only. Explainer drafted (genera, from sepkoski2002 via jones2022). No open family data (Sepkoski 1992 compendium is print-only); consider printing genera instead: e.g. `Genera: sea 3,398 (64%)` on a Maastrichtian page (from data/explainers/diversity.json; 100% = 5,339 genera in the latest bin). |
| ☐ | Biomass | `Life ~550 Gt C` | leads: Bar-On, Phillips & Milo 2018 (present only) | No history curve exists; explainer or back-matter fact only. |
| ☐ | Continents | `Supercontinent: Pangaea` | zhao2002, li2008, nance2014 | Text, not a number; perhaps in the running head instead. |
| ☐ | Tetrapod (land animal) families | `land 50 (10%)` | sahney2010; leads: Benton 1995 (Science) | From ~370 Ma. Shares the Life slot with marine families. |
| ☐ | Land plants: share of spore / seed / flowering plants | `Plants: flowering 75%` | leads: Niklas, Tiffney & Knoll 1983 (Nature); Lidgard & Crane 1988 (Nature) | From ~430 Ma. One series combining vascular-plant groups and the flowering-plant takeover. |
| ☐ | Largest living thing | `Largest: seaweeds ~1 cm` | payne2009 (Table S1 on Dryad not yet downloaded) | Life slot before animals (3.5 Ga – ~540 Ma); after that, the check-in giants take over. Explainer drafted with a placeholder curve. |
| ☐ | Insect families | `Insects ~600 families` | leads: Labandeira & Sepkoski 1993 (Science) | From ~410 Ma. Not yet placed in a slot. |

### 100 Myr check-in candidates (only if the check-in box is brought back; see demo)
| ☐ | Metric | Footer form | Sources in hand / leads | Notes |
|---|---|---|---|---|
| ☐ | Largest sea animal | `Sea giant: blue whale 30 m` | per-period record holders | One cited record holder per 100 Myr. |
| ☐ | Largest land animal | `Land giant: elephant 6 t` | leads: Smith et al. 2010 (Science); Benson et al. 2014 (PLoS Biol) | From ~370 Ma. |
| ☐ | Largest flier | `Flier: 70 cm wings` | per-taxon records (griffinflies, pterosaurs, birds) | From ~320 Ma. |
| ☐ | Ice volume | `Ice 150%` (of today) | hoffman2017, montanez2013, westerhold2020 | Snowball episodes, Late Paleozoic ice age, Cenozoic ice. |
| ☐ | Land above sea level | `Land 3% of Earth` | leads: Bindeman et al. 2018 (Nature); Flament et al. 2008 | The area land animals could live on. Archean continents may have been mostly underwater. |

Moon distance and sea level could also move here from the every-page list.

Removed from candidacy (user, 2026-11-23): any series shorter than 10 pages (50 Myr), e.g. human population,
hominin brain size, C₄ grasslands, Antarctic ice alone; Earth–Sun orbit; mammal genera; geomagnetic reversals per page;
inner core radius; continental crust volume; paleolatitude of a place; radiogenic heat; mantle temperature; text-state labels (ice, sea chemistry, reef builders, fliers).

## Relative values
Print a familiar absolute value alone (Day 23.0 h, Year 381 d, O₂ 25% of air, Temp +3 °C vs today).
Otherwise print relative to today: Sun 97%; counts as `450 (40%)`; CO₂ as × pre-industrial (280 ppm); Moon as `km (98%)`.

## Footer design demos (B chosen, decision #45; implemented)
`docs/sketches/footer_demo.py` → `footer-demo.pdf`, `footer-demo-strips.png` (mock values, not cited).
A: three named slots (Sky · Air & climate · Life) every page. B: two plain lines every page plus a boxed check-in strip
on pages ending on a round 100 Myr (pp. 14, 34 … 914). Both use a fixed-height footer so the bottom time label stays under the ruler.

Skipped by the user: galactic year count.

## Explainer page pattern (draft)
1. Title and one graph of the whole 4.57 Gyr. A log axis where the range demands it, plus an inset for the last 540 Myr if the
   Phanerozoic is too compressed.
2. **What the graph shows**: the story in 3–4 sentences.
3. **How it is known**: the proxies or methods.
4. **How sure**: what is a value and what is only a limit, and where sources disagree.
5. Its own short bibliography, or citations into the main one.

Placement: appendix after the timeline (decision #22 keeps the timeline unbroken).
