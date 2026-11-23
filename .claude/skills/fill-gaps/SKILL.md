---
name: fill-gaps
description: Find the emptiest stretches of the Lifetime of the Earth book and propose or research events to fill them. Use when asked how full the book is, or to fill empty pages.
---

# Fill gaps

1. `./run fullness --text --emptiest 20` and read the summary. Don't open the PNG unless the user wants it.
2. Pick stretches (the user's choice, else the longest gaps in eras with known literature).
3. For each stretch, list candidate topics that genuinely fall in that time: dated rock formations, impacts,
   isotope excursions, orogenies, glaciations, first appearances, supercontinent events, zircon or detrital records.
   Never fake precision to fill a page; an honestly empty page is fine.
4. Present candidates with likely sources; on approval, follow the `add-events` skill.
   To research one stretch in depth, use the `dig-gap` skill instead.
5. Re-run `./run fullness` and report the change.
