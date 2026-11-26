# Collision pages: todo

Pages where entries overflow or crowd each other. For now research keeps adding, and these get whittled down later
(user, 2026-11-21). Check with `./run fullness --text` (overflowing pages) and `./run png N`.

Ways to resolve a crowded page, roughly in order of preference:
1. Lower `importance` and drop the least important entries from print (keep them in the data).
2. Shorten texts or move art to a neighbouring entry.
3. Merge related entries (e.g. several hominin firsts into one entry).
4. Design change: zoom insets for the last pages (session 15 idea), ~~or a back-matter "last 5 million years" section~~ (ruled out, decision #47).

| ☐ | Page | Years | Status (2026-11-21) | Notes |
|---|---|---|---|---|
| ☐ | **914** | −5,000,000 to 0 | Overflows: 22 entries, about 3.4 pages of content | First priority. The whole of human evolution, Ice Ages, cave art, Wrangel mammoths, Toba, Laschamps, LGM, recent impacts. Needs the zoom/inset design or a back-matter section. |
| ☐ | 913 | −10,000,000 to −5,000,000 | Overflows: 11 entries, about 1.4 pages | Sahara, C4 grasslands, Messinian/Zanclean, _Sahelanthropus_, _Ardipithecus_, Andes, Grand Canyon, Giordano Bruno. |
| ☐ | 901 | −70,000,000 to −65,000,000 | Overflows (2026-11-22) | Chicxulub, Deccan, _Purgatorius_, grass in dung; added 2026-11-22: _Vegavis_, _Quetzalcoatlus_ (both could move: their t is a Maastrichtian midpoint, so a t of −69 to −72 Ma within t_err would put them on p900). |
| ☐ | 1 | −4,570,000,000 to −4,565,000,000 | 68% full | First solids, protoplanets, Jupiter, Mars. |
| ☐ | 831 | −420,000,000 to −415,000,000 | Art layout bug (pre-existing, seen 2026-11-22) | _Entelognathus_ drawing is so wide that its caption is squeezed into a one-word column over the ruler. Cap drawing width or put the caption below. _Cooksonia_ (added 2026-11-22) shares the page. |
| ☐ | 907 | −40,000,000 to −35,000,000 | Same wide-art bug (2026-11-22) | _Perucetus_ caption squeezed over the ruler. A _Basilosaurus_ drawing (art/line/basilosaurus.svg, credit in art/credits.json) was tried here and detached: same squeeze, and the long thin outline is cropped on the left. Reattach once wide drawings are capped. |
| ☐ | 840 | −375,000,000 to −370,000,000 | Same wide-art bug (2026-11-22) | _Tiktaalik_ caption squeezed to one word per line. An _Acanthostega_ drawing (art/line/acanthostega.svg) was tried and detached: same squeeze, and it ran past the page bottom. **Systemic:** long, low animal outlines (fish, whales, tetrapods) are scaled to full width, cropped at the left, and starve the caption column; seen on p831, 840, 907. Likely fix in typeset/book.typ: cap drawing width (e.g. ≤ 60% of the text block) and set a minimum caption width. |

Add pages here when `fullness` reports them.
