# Footer metric candidates

The footer prints a terse line of metrics on every page (decision #23). The metrics in use now are Sun, Day and Year
(`data/series/`). This file lists candidates. Each needs cited values or a cited model, and prints only where one
exists (decision #20). Each metric may also get a **one-page explainer** in an appendix: one graph of the
whole history, what it shows, how it is known and how sure. A draft for oxygen is in `typeset/explainers/oxygen.typ`
with data in `data/explainers/oxygen.json`.

Status: ☑ in use · ◐ sources in hand · ☐ idea only

| ☐ | Metric | Footer form | Sources in hand / leads | Notes |
|---|---|---|---|---|
| ☑ | Sun brightness | `Sun 94% of today` | gough1981 (model) | Whole book. Explainer: luminosity milestones (e.g. when the Sun passed 80%, 90%). |
| ☑ | Day length | `Day 21.9 h` | williams2000; **add** lantink2022 (≈17 h at 2.46 Ga), meyers2018 (18.68 h at 1.4 Ga), mitchell2023 (≈19 h stalled 2–1 Ga) | Replace the linear demo with these points. The stall makes the curve flat for 1 Gyr. |
| ☑ | Days per year | `Year 400 days` | williams2000; derive from day length (year length in hours is constant) | Could be computed from day length instead of separate points; decide. |
| ◐ | Moon distance | `Moon 341,000 km` | lantink2022 (321,800 km at 2.46 Ga), meyers2018 (340,900 ± 2,600 km at 1.4 Ga), williams2000 (0.906 of today's distance at 2.45 Ga, 0.965 at 620 Ma); present ~384,300 km (lantink2022 text) | Only three points before the Phanerozoic; prints blank before 2.46 Ga unless a model is cited. |
| ◐ | Oxygen | `O₂ ≤0.02%` or `O₂ ~21%` | crowe2013, gumsley2017, planavsky2014b, scott2006, berner2006, krause2018, machta1970 | Mostly limits, not values: needs a format for "below" and "range" (e.g. `O₂ <0.0002%`). Draft explainer done. |
| ☐ | CO₂ | `CO₂ ~1,000 ppm` | leads: Foster et al. 2017 compilation; Cenozoic CO₂ proxy consortium | Phanerozoic only. |
| ☐ | Global temperature | `Temp ~+10 °C` | leads: westerhold2020 (Cenozoic, deep sea); Scotese et al. 2021 (Phanerozoic) | Relative to today. |
| ◐ | Sea level | `Sea +240 m` | haq2008 (Paleozoic), haq2014 (Cretaceous); leads: Miller et al. 2005 (last 100 Myr) | Phanerozoic only. |
| ☐ | Air pressure | `Air <0.5 bar` | som2016 (<0.5 bar at 2.7 Ga), som2012 (< 2× density) | Only limits at 2.7 Ga; probably explainer only. |
| ☐ | Species / families count | `Families ~900` | raup1982; leads: Sepkoski family compilation, Alroy et al. 2008 | Marine animals, Phanerozoic only. Strong explainer: the mass extinctions are the dips. |
| ☐ | Biomass | `Life ~550 Gt C` | leads: Bar-On, Phillips & Milo 2018 (present only) | No history curve exists; explainer or back-matter fact only. |
| ☐ | Continents | `Supercontinent: Pangaea` | zhao2002, li2008, nance2014 | Text, not a number; perhaps in the running head instead. |
| ☐ | Earth–Sun / orbit | (constant) | n/a | Orbit length in years is fixed; the day count changes (days per year). |

Skipped by the user: galactic year count.

## Explainer page pattern (draft)
1. Title and one graph of the whole 4.57 Gyr. A log axis where the range demands it, plus an inset for the last 540 Myr if the
   Phanerozoic is too compressed.
2. **What the graph shows**: the story in 3–4 sentences.
3. **How it is known**: the proxies or methods.
4. **How sure**: what is a value and what is only a limit, and where sources disagree.
5. Its own short bibliography, or citations into the main one.

Placement: appendix after the timeline (decision #22 keeps the timeline unbroken).
