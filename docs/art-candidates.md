# Art candidates: hand drawing or deeper image research

Events that would be clearer shown as well as explained, but with no usable image source yet (nothing on PhyloPic,
no licensed drawing found). Add rows as they turn up; remove a row once art is in the event's `art` field.

Options per row: **redraw** (line art traced or drawn from a figure in an open-access paper; cite the paper),
**draw** (original sketch from a description), **photo research** (look for licensed photos, museum or survey images).

| Event id | Page | What to show | Possible source | Approach |
|---|---|---|---|---|
| `gaoyuzhuang-macrofossils` | 603 | Long ribbon-like blades, up to 30 cm, on a bedding surface | zhu2016 figures (Nature Communications, CC BY) | redraw |
| `qingshania-multicellular` | 588 | Unbranched filament of cylindrical cells, spore-like bodies | miao2024 figures (Science Advances, CC BY) | redraw |
| `tirohan-red-algae` | 595 | Filament with central disc in each cell; lobed thallus | bengtson2017 tomography figures (PLoS Biology, CC BY) | redraw |
| `wiborg-rapakivi` | 587–590 | Rapakivi texture: round feldspar crystals with pale rims | Geological survey or Wikimedia Commons photos | photo research, then draw |
| `chorhat-burrows` | 595 | The disputed grooves on a sandstone bedding plane | seilacher1998 figure (Science, not open access) | photo research; draw only if licensing allows |
| `witwatersrand-gold`, `klipriviersberg-flood-basalts`, `pongola-glaciation` | 339, 357, 335 | Locator map of the Kaapvaal craton today: Witwatersrand basin (Johannesburg), Pongola, Ventersdorp lavas | Natural Earth via `tools/basemap.py` (like `vaalbara-map.svg`); credits `naturalearth` + `claude-drawings` | draw (script) |
| `oldest-magnetic-reversal` | 366 | Compass needle pointing north, then south; or a short black/white polarity bar | Diagram from strik2003's description; no image needed | draw |
| `pongola-glaciation` | 335 | Striated, faceted stone dropped into laminated mud (dropstone) | young1998 figures (Journal of Geology, not open access); Wikimedia Commons dropstone photos | photo research, then draw |
| `tumbiana-lake-stromatolites` | 371 | Domed lake stromatolite in cross-section (cut drill core) | gerard2009 figures (PLoS ONE, CC BY); PhyloPic "stromatolite" search fails (not a taxon) | redraw |
| `gondwana-assembles` | 787 | Gondwana outline with the East African and Kuunga orogens | meert2003 figures; Natural Earth basemap | map (`tools/basemap.py`) |
| `western-interior-seaway-connects` | 896 | North America split by the seaway, Tethyan water from the south meeting boreal water from the north | eldrett2017 (Climate of the Past, CC BY) figure 1 | map |
| `drake-passage-opens` | 908 | South America and Antarctica parting; the new circum-Antarctic seaway | scher2006; Natural Earth | map |
| `everest-summit-limestone` | 822 | Everest profile with the Ordovician limestone band at the summit | stouge2021 figures | diagram |
| `anomalocaris-eyes` | 812 | One compound eye, 16,000 lenses (inset next to the existing _Anomalocaris_ outline) | paterson2011 figure | redraw |
| `cloudina-reefs` | 805 | Nested cone-in-cone tubes cemented together | penny2014 figure | redraw |
| `mussaurus-herd` | 876 | _Mussaurus_ adult with hatchlings | PhyloPic search (`./run art search Mussaurus`) | fetch if available |
| `haootia-cnidarian` | 803 | Four-cornered fibrous impression | liu2014 (Proc R Soc B, CC BY) figure | redraw |
| `basilosaurus` | 907 | Drawing ready (art/line/basilosaurus.svg); reattach after the wide-art fix | PhyloPic (Tripoli, CC BY) | fetched |
| `acanthostega-eight-fingers` | 840 | Drawing ready (art/line/acanthostega.svg); reattach after the wide-art fix | PhyloPic (Hartman, CC0) | fetched |
| `stac-fada-impact` | 679 | Locator map of NW Scotland: Stac Fada outcrops and the Lairg Gravity Low ~50 km east | Natural Earth via `tools/basemap.py`; positions from kenny2019/simms2015 | draw (script) |
| `midcontinent-rift` | 693 | Arc of the Midcontinent Rift around Lake Superior, Kansas to Michigan | Natural Earth via `tools/basemap.py`; swansonhysell2019 figure 1 | draw (script) |
| `premier-kimberlite` | 685 | Rough Cullinan diamond (3,106 ct) beside a hand for scale | Wikimedia Commons public-domain photos of the rough stone / replicas | photo research, then draw |
| `isua-terranes-collide` | 181 | Locator map of SW Greenland: Isua belt and Itsaq Gneiss Complex near Nuuk | Natural Earth via `tools/basemap.py`; positions from nutman2013 | draw (script) |
| `pilbara-crustal-overturn` | 195 | Cross-section of granite domes rising between sinking greenstone keels | wiemer2018 figures (Nature Geoscience, closed; check licence) or draw from the abstract | draw |
| `akilia-earliest-life-claim` | 150 | Banded quartz–pyroxene rock of Akilia island, or a locator map of SW Greenland (Akilia near Nuuk) | Wikimedia Commons / GEUS photos; Natural Earth via `tools/basemap.py` | photo research, or draw (script) |
| `alh84001-crystallizes` | 96 | The ALH84001 meteorite (fist-sized, fusion-crusted) | NASA/JSC public-domain photos | photo research, then draw |
| `mount-narryer-zircons` | 85 | Locator map of the Yilgarn Craton: Mt Narryer and Jack Hills, Western Australia | Natural Earth via `tools/basemap.py` | draw (script) |
| `isua-forearc-sediments` | 174 | Cartoon of a fore-arc basin: arc, trench, boninite floor, turbidites and graphite-rich muds | boyd2024 Fig. (Communications Earth & Environment, CC BY) | redraw |
| `zaonega-shungite` | 520 | A lump of shungite (black, glassy, almost pure carbon) from Karelia | Smithsonian / Wikimedia Commons mineral photos (check licence) | photo research, then draw |
| `glenburgh-orogeny` | 523 | Locator map of Western Australia: Pilbara and Yilgarn cratons with the Glenburgh Terrane between | Natural Earth via `tools/basemap.py` (craton outlines from johnson2011 figure) | draw (script) |
| `jormua-ophiolite` | 525 | Cross-section of an ophiolite (pillow lavas, sheeted dykes, gabbro, mantle peridotite); could also serve `purtuniq-ophiolite` (p515) | USGS FGDC patterns; textbook ophiolite column | draw |
| `horodyskia` | 625 | Curving "string of beads" (1–5 mm beads, up to 15 cm long) on a bedding plane | rule2019 / retallack2013 figures (not open access); NPS Glacier National Park photos (public domain) | photo research, then draw |
| `belt-basin` | 621 | Belt Supergroup stromatolites or the layered strata at Logan Pass, Glacier National Park | NPS / USGS photos (public domain) | photo research, then draw |
| `mount-isa-ore` (Sullivan), `belt-basin` | 620–625 | Locator map of North America: Sullivan (BC), Belt basin (Montana), St. Francois Mountains (Missouri), Michael–Shabogamo belt (Labrador) | Natural Earth via `tools/basemap.py` | draw (script) |
| `antarctic-laurentian-granite` | 627 | East Antarctica fitted against western North America, with the ~1.44 Ga granite belt crossing both | goodge2008 figure (Science, not open access) | redraw schematically |
| `mount-isa-ore` | 578, 584, 587 | Locator map of eastern Australia: Broken Hill (NSW), Mount Isa (Qld), McArthur River (NT), the 1.69–1.64 Ga lead–zinc belt | Natural Earth via `tools/basemap.py` | draw (script) |
| `grand-canyon-basement-metamorphism`, `mazatzal-orogeny` | 573–585 | Map of Laurentia's growing southern and eastern margin: Yavapai, Mazatzal and Labradorian belts, Grand Canyon marked | Natural Earth via `tools/basemap.py`; belt outlines from amato2008 / gower2002 figures (not open access) | draw (script), belts schematic |
| `changcheng-microfossils` | 583 | Spiny _Germinosphaera_ or net-walled _Dictyosphaera_ vesicle (tens of µm) | miao2019 figures (Precambrian Research, not open access); PhyloPic has no acritarchs | photo research; draw only if licensing allows |
| `acasta-gneiss`, `mount-narryer-zircons` (Beartooth), `saglek-graphite-life` | 122–125 | Locator map of North America's ~3.95 Ga sites: Acasta (NW Territories), Beartooth Mountains (Montana), Saglek Block (northern Labrador) | Natural Earth via `tools/basemap.py`; Acasta outcrop photos (GSC / Wikimedia) as an alternative | draw (script) or photo research |
| `dharwar-giant-dyke-swarm` | 441 | Southern India outline with the dykes fanning out (N48°E in the north to N90°E in the south) towards a focal point ~300 km west of the craton | Natural Earth via `tools/basemap.py`; trends from the kumar2012 abstract (G-cubed, not open access) | draw (script), dykes schematic |
| `ongeluk-fungus-like-fossils` | 435 | Branching, tangled filaments growing from a film on the wall of a gas bubble | bengtson2017fungi figures (Nature Ecology & Evolution, not open access) | photo research; draw only if licensing allows |
| `malley-dykes` | 468 | Locator: Slave craton (NW Territories) with NE-trending Malley dykes toward the Kilohigok basin | Natural Earth via `tools/basemap.py`; buchan2012 abstract | draw (script) |
| `oxygen-oscillations` | 461 | Mini-graph: O₂ swinging around 10⁻⁵ PAL from 2.32 to 2.22 Ga, then staying high | poulton2021 Fig. 4 (author copy on White Rose eprints 171586; licence to check) | redraw (mini-graph) |
| `little-dal-sponge-reefs` | 737 | Thin-section view of the vermiform mesh of branching tubes inside calcimicrobial reef, beside a modern horny sponge's spongin skeleton | turner2021 figures (Nature, not open access); a modern keratose sponge (e.g. _Spongia_) on PhyloPic, captioned "modern" | photo research / redraw if licensing allows; don't imply the fossil is certainly a sponge |
| `gairdner-dyke-swarm` | 749 | Locator: South Australia with the NW-trending Gairdner dykes, and South China (Guibei) on an inset, both ~827 Ma | Natural Earth via `tools/basemap.py`; wingate1998, li1999 | draw (script); could become a GPlates Rodinia view (~825 Ma) showing the two side by side |
| `big-cottonwood-tidal-day` | 735 | Mini-graph: day length vs time from the book's day-length events (16.9 h at 2.46 Ga, ~19 h stall, 18.7 h at 1.4 Ga, 18.9 h at 0.9 Ga, 24 h today) | lantink2022, mitchell2023, meyers2018, sonett1998 | draw (mini-graph); shared candidate with the day-length footer series |
| `great-dyke-zimbabwe` | 400 | Locator: Zimbabwe with the NNE-trending Great Dyke (~550 km) and its satellite dykes | Natural Earth via `tools/basemap.py`; wingate2000, oberthur2013 | draw (script) |
| `gamohaan-sulfur-bacteria` | 411 | Single large coccoid microfossil beside a modern _Thiomargarita_ cell, with a 100 µm scale bar | czaja2016 Fig. (Geology, licence to check); PhyloPic has no _Thiomargarita_ (404); Bioicons for a generic cell | redraw / draw (caption "modern" for the comparison) |
| `campbellrand-platform` | 403 | Sketch of an aragonite crystal fan growing on the seafloor (cm scale) | sumner2004 figures (licence to check) | redraw |
| `xionger-lip` | 559 | Locator: North China craton with the Xiong'er volcanic field along its southern margin and the dyke swarm in the interior (~1.78 Ga) | Natural Earth via `tools/basemap.py`; peng2008 (outline from a CC BY figure, if any) | draw (script) |
| `avanavero-lip` | 556 | Locator: Guiana Shield (Venezuela, Guyana, Suriname, N Brazil) with Avanavero sill/dyke sites and the Roraima Supergroup outcrop | Natural Earth via `tools/basemap.py`; reis2013 | draw (script); could pair with `xionger-lip` as "1.79–1.78 Ga LIPs of Columbia" |
| `mcdermott-eukaryotes` | 564 | Sketch of a budding cell, a small multicellular cluster and an opened cyst wall, with a 10 µm scale bar | javaux2025 figures (Phil. Trans. B, open access; licence to check); PhyloPic has no acritarchs (404, dig 570–585) | redraw |
| `homestake-gold` | 567 | Locator: Black Hills, South Dakota, with the Homestake mine (Lead, SD) | Natural Earth via `tools/basemap.py`; morelli2010 | draw (script) |
