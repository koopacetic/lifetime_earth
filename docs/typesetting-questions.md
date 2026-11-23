# Typesetting & imposition: questions and answers

Answers from the 2026-11-20 session are recorded inline (**A:**). Settled items are mirrored in docs/decisions.md.
Open items are marked **OPEN**.

## A. Critical

1. **Sheet size.** **A:** US Letter (8.5×11 in), folded once into 4 pages, giving a 5.5×8.5 in untrimmed page.
   Inner (binding) margin allowance: 20 mm for now; tune after printed tests.
2. **Printer.** **A:** Laser, duplex. **OPEN:** measure the non-printable margin and front/back registration during printed tests.
3. **Trimming.** **A:** Yes; the foredge is trimmed with a plough after binding. `config.json` assumes 6 mm trim;
   foredge bands are printed 12 mm wide from the untrimmed edge, so about 6 mm stays visible on the page and the cut goes through the band.
   Short trim ticks at the head and tail of each page show where the plough is expected to cut.
4. **Signature size.** **A:** 4 sheets per signature = 16 pages. Page count padded to a multiple of 16. Revisit at printed tests.
5. **Paper.** **A:** 24 lb bright white bond, about 0.11 mm per leaf, so 1000 pages (500 leaves) is about 55 mm before covers and sewing swell.
6. **Volumes.** **A:** One volume, about 2.5–3 in thick.
7. **Ruler position.** **A:** On the outer (foredge) side of every page, mirrored left and right. ✅ Implemented.
8. **Font.** **A:** No strong opinion; comfortable reading beats exact placement. Libertinus Serif 9 pt for now.
9. **Page budget.** **A:** 1000 is a soft target. This is book 1 of a trilogy, each about 1000 pages.
10. **Nothing inserted mid-timeline.** *Expanded:* the book's core rule is "each sheet of paper = a fixed slice
    of time". Examples of what would break it:
    - a part-opener page such as *"Part II: The Archean"* placed between page 107 (ending −4,035,000,000) and page 108;
    - a full-page illustration of a Cambrian sea between two Cambrian pages;
    - a two-page explainer on how zircons are dated, placed where zircons first appear.

    The problems: (a) the inserted page covers no time, so the 5 Myr rhythm and the "thickness of the book = time" idea
    become false (the foredge bands would be slightly off); (b) a single inserted page swaps left and right for
    every later page, so the ruler would end up on the spine side (inserting pages in pairs avoids this);
    (c) the time labels would jump across a non-time page.
    **A:** Every page in the bulk of the book is a timeline page: no title pages, chapters or full-page images.
    Full-page images, if needed, go in appendices.
11. **Color.** **A:** Black and grey only.

## B. Optional

1. **Running head.** *Answer to the question:* one line at the top of each page listing the named units in force
   at that page's start, largest to smallest: eon · era · period · epoch. ✅ Implemented. Examples:
   - page 901 (−70,000,000): `Phanerozoic · Mesozoic · Cretaceous`; Mesozoic epochs aren't in the data yet
   - page 902 (−65,000,000): `Phanerozoic · Cenozoic · Paleogene · Paleocene`
   - page 451 (−2,320,000,000): `Proterozoic · Paleoproterozoic · Rhyacian` (no epochs exist in the Precambrian)
   - page 34 (−4,405,000,000): `Hadean` (no subdivisions)

   When a unit *begins mid-page*, a heavy tick crosses the ruler with a small italic label, e.g.
   *Cenozoic / Paleogene / Paleocene begins −66,000,000*. The header stays one line.
2. **Citations.** **A:** Superscripts. ✅ Implemented with the Nature citation style (numbered in order of first citation).
3. **Number style.** **A:** Fully written out with commas (`−4,570,000,000`), never "Ma"/"mya". ✅ Already the case.
4. **Page 1 and the Sun's formation.** **A:** It already is that page. Page 1 spans −4,570,000,000 to −4,565,000,000,
   and the first solids (−4,567,300,000) sit 54% of the way down it, followed by the "Hadean begins" tick at −4,567,000,000.
   Starting page 1 *exactly* at −4,567,300,000 would make every label a non-round number (−4,562,300,000 …) and
   leave a partial final page, so I recommend keeping the round boundaries.
5. **Visual hierarchy.** **A:** Not needed while pages hold 0–1 entries. Tabled.
6. **Footer frequency.** **A:** Demo built: `build/footer-demo-every.pdf` (terse line on all 10 pages) vs
   `build/footer-demo-checkin.pdf` (boxed check-in only on the page beginning at −200,000,000, i.e. every 20 pages).
   **A:** Every page; small changes from page to page are fine. (The check-in mode remains in code, unused.)
7. **Physical page numbers.** *Explained:* apart from the time labels, should pages carry ordinary sequential numbers
   (1 … ~1000)? They are useful for (a) the contents, index and cross-references ("see p. 812"), and (b) binding:
   checking imposition and signature order. Without them, the contents would point to time labels instead
   ("Cambrian … −540,000,000"), which suits this book but is slower to look up. Current state: a tiny grey folio
   on the spine side of the footer. **A:** Keep ordinary page numbers in the footer, lower emphasis than the date and
   metrics (6.5 pt light grey). ✅
8. **Dense pages, callouts, hierarchy.** **A:** Tabled until pages crowd, or the final-page zoom session.
9. **Front-of-book diagram.** **A:** Tabled to the end of the project (sketches in docs/front-diagram-ideas.md); possibly
   described in the introduction text instead. Endpapers handled separately. **TODO (late project):** spine and cover
   design, discussed and drafted for print tests.
10. **Bibliography.** **A:** Professional and complete, but dense. ✅ Two columns, 6.5 pt, Nature style: about 64 entries per page,
    so 1000 sources ≈ 16 pages. **A:** DOIs are kept in sources.bib (for verification) but not printed; Nature style
    omits them. Web sources such as PhyloPic still print their URL.

## C. Enhancements: text position in the physical book

1. **Back-to-back registration:** ruler, labels and frame mirrored to the same physical position on both sides of a leaf
   (now true by construction, because the ruler is mirrored); verify show-through on 24 lb paper in printed tests.
2. **Gutter loss:** a 2.5–3 in sewn book loses several mm at the spine; inside margin is 20 mm, tune after tests.
3. **Creep:** with small signatures, inner sheets stick out <0.5 mm at the foredge; the plough trim removes it. Optional per-sheet shift in `impose.py`.
4. **Spreads as 10 Myr views:** continuation marks at the bottom of left pages and the top of right pages?
5. **Foredge bands:** ✅ prototype; thumb-index slots, demo set = the 4 eons (`data/foredge.json`). A life-based set
   (single-celled / multicellular / animals / life on land) needs research and citations. Band visible width after trim ≈ 6 mm.
6. **Head-edge bands:** the head (top edge) could carry a second band set if the head is trimmed too.
7. **Flip-book consistency:** fixed positions for ruler, labels and footer; ✅ so far.
8. **Imposition marks:** fold, sewing-station and collation-ladder marks on the spine fold of each signature.
9. **Crop marks:** ✅ head and tail trim ticks at the foredge cut line.
