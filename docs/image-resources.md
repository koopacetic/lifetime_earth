# Image resources

A list of **places to get images**, as opposed to `data/sources.bib`, which cites individual facts and individual
images. Use this when looking for art for an event: check the hints first, then search. Each image actually used still
needs a record in `art/credits.json`, which prints as a lettered entry in the book's **Image credits** list
(decision #40; not in sources.bib). `art.sources` cites only the facts in the caption.

Working rules (from the 2026-11-21 session; confirm or move to decisions.md):
- Prefer CC0 / public domain, then CC BY, then CC BY-SA. **Skip NC (non-commercial) licences**: the book may be
  given away or sold, and NC is ambiguous for that.
- SVG only, black line art in the end (`art/line/`). Downloaded SVGs must pass the `<script` / `href=` check; files
  that fail are **reference material to redraw from**, not art to use directly.
- Downloads go in a scratch folder, not the repo; only the final line drawing is kept in `art/`.
- A silhouette that is just a blob (many microbe images) adds nothing; check a rendered preview before using it.

Status key: ✅ in use · 🔎 searched, findings below · ⏳ not yet checked.

## PhyloPic ✅
- https://www.phylopic.org · API used by `tools/art.py search / fetch / outline` · credit record added automatically
- Licences per image: CC0, PDM, CC BY, CC BY-SA, some CC BY-NC (skip those).
- **Good for:** named animal and plant species and genera, especially fossil vertebrates (Nobu Tamura's
  reconstructions), dinosaurs, insects, early mammals, hominins.
- **Weak for:** microbes (mostly featureless blobs; *Arthrospira*, *Methanosarcina* and *Gloeobacter* were tried and
  rejected), Proterozoic eukaryotes, algae, fungi.
- **Not found (2026-11-21):** *Bangiomorpha*, *Grypania*, *Qingshania*, *Wattieza*, *Eospermatopteris*,
  *Rhyniognatha*, *Montsechia*, *Sahelanthropus*, *Ardipithecus*, Demospongiae, *Acromyrmex*. "Diplopoda" made the
  search error, so try "millipede" or a genus name. "stromatolite" also errors (not a taxon; 2026-11-21).
- **Surprises:** the "Cyanobacteriota" image (Sanaa Mughal, CC BY) is a stromatolite block cut open (used for
  Strelley Pool). Modern relatives work for groups that have no fossil drawing (*Tettigonia* for the Jurassic katydid,
  Thysanoptera for amber thrips); the caption must say "modern".
- Usable but not yet attached: *Homo sapiens sapiens* (Natalie Kestel, CC BY 4.0, uuid bb3230d6-…) for Jebel Irhoud.

## Natural Earth ✅
- https://www.naturalearthdata.com · GeoJSON mirror: github.com/nvkelso/natural-earth-vector/tree/master/geojson
- Public domain · credits id `naturalearth` (shared, plus `claude-drawings`) · drawn with `tools/basemap.py` (land outlines, dots, labels)
- **Good for:** present-day locator maps: where a rock unit, crater or fossil site is today; modern seas and
  straits. 1:110m for continents, 1:50m for regional maps (the Mediterranean).
- **Not for:** past geography. Use GPlates (below) for that.
- Made so far: `art/line/vaalbara-map.svg`, `pilbara-map.svg`, `kaapvaal-dominion-map.svg`, `maniitsoq-map.svg` (in use);
  at 520 px wide with font 21 the labels print small; tall maps (Greenland) shrink further, `art/line/mediterranean-map.svg` (ready for Messinian/Zanclean,
  not attached because p913 already overflows).
- Candidates: Isthmus of Panama, Paratethys/Black Sea, Grand Canyon locator, Chicxulub/Yucatán, a world map of
  Archean rock sites (Isua, Acasta, Jack Hills, Barberton, Pilbara, Nuvvuagittuq).

## Bioicons 🔎
- https://bioicons.com · repo github.com/duerrsimon/bioicons (`static/icons/<licence>/<category>/<author>/*.svg`;
  list the repo tree with the GitHub API to search filenames)
- Mixed CC0 / CC BY 3.0 / CC BY 4.0 / CC BY-SA (licence is in the folder path)
- **Good for:** cells and microbes as diagrams: SwissBioPics (CC BY 4.0) has Archaea, Eukaryota, Animal, Plant,
  Fungal, *Chlamydomonas*, *Nostoc* (filamentous cyanobacterium) and bacteria in many shapes; Mariana Ruiz
  Villarreal's average prokaryote cell (CC0).
- **Catch:** SwissBioPics files are 0.5–1.4 MB colour drawings with internal `href` links; they fail the safety check
  and won't outline. Use them as references for hand-drawn line versions (credit them in `art/credits.json`).
- Candidates: LUCA (prokaryote cell), oldest eukaryote fossils (prokaryote vs eukaryote side by side),
  nitrogen fixation or oxygenic photosynthesis (*Nostoc* filament with heterocysts), Ourasphaira (fungal hyphae).

## IAN Symbol Library ⏳
- https://ian.umces.edu/media-library/symbols/ (University of Maryland Center for Environmental Science)
- CC BY-SA 4.0 · about 3,000 vector symbols for science diagrams
- **Probably good for:** ocean, sediment, volcanoes, ice, rocks, plankton, algae, generic organisms.
- Search runs in JavaScript, so it wasn't checked from a script; browse it by hand or find its download endpoint.

## USGS FGDC geologic map patterns ⏳
- FGDC Digital Cartographic Standard for Geologic Map Symbolization (USGS), lithology patterns section
- Public domain (US government)
- **Good for:** fill patterns in hand-drawn rock columns and cross-sections: chert, banded iron, evaporite (salt),
  tillite/diamictite, limestone, sandstone, volcanic rocks. Use for banded iron, the Snowball cap-carbonate column,
  Messinian salt, the Grand Canyon column.

## GPlates and EarthByte plate models ⏳
- https://www.gplates.org, https://www.earthbyte.org · software open source; models mostly CC BY (cite the model paper)
- **Good for:** maps of continents in the past: Pangaea, Rodinia, Columbia, India's track. Reliable to about 1 Ga.
- Ties to project-plan row 18 (paleogeography thumbnails).

## Biodiversity Heritage Library / Internet Archive ⏳
- https://www.biodiversitylibrary.org, https://archive.org
- Public domain (age) for works before about 1929
- **Good for:** 19th-century engravings to trace: stromatolites ("Cryptozoon"), crystals, fossil plants and
  invertebrates, rock sections (Lyell's *Principles*, Dana's *Manual of Geology*). Engraving style suits a hand-bound
  book.

## Wikimedia Commons ⏳
- https://commons.wikimedia.org · licence per file (check each one)
- **Good for:** SVG diagrams of plate motions, orbits, Solar System, stratigraphy, cell structure (Mariana Ruiz
  Villarreal's public-domain cell diagrams). Often better as a reference to redraw than to use directly.

## NASA / USGS / NOAA image libraries ⏳
- Public domain (US government)
- **Good for:** lunar and Martian basin and crater outlines (South Pole–Aitken, Imbrium, Orientale, Gale), eruption
  extents (Deccan, Columbia River), and planet images to trace.

## Smithsonian Open Access ⏳
- https://www.si.edu/openaccess · CC0
- **Good for:** photos and 3D scans of meteorites, minerals and fossils to trace (zircon, Allende chondrite).

## Hand-drawn (in-house) ✅
- `art/line/*.svg` written by hand or by script (mini-graphs, cross-sections, maps); cite the data in `art.sources`.
- Credits id `claude-drawings` (shared entry in `art/credits.json`): "Line drawings, diagrams and maps drawn for this book",
  Claude (Anthropic). Every in-house drawing's record lists it.
- Examples: `bottleneck-930ka.svg` (mini-graph), `komatiite-spinifex.svg` (cross-section), `*-map.svg` (basemap).
- Follow-up idea (project-plan row 17a): an image-fullness check to find long text-only stretches.
