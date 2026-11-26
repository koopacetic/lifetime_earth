# Verification backlog

## Status after verification pass 2 (2026-11-21, late)
**120 of 131 unverified events were set `verified: true`** (now 210 of 221 verified). Every event row in the tables
below is resolved unless it is listed under "Still unverified". Evidence came from the cached abstracts, abstracts
recovered from publisher pages (`tools/source_cache.py --refetch`), open full texts (PMC, the Rämö 2014 PDF) and
web-search summaries of abstracts and papers. Evidence beyond the abstract is recorded under
`## Verification` in the source's `sources/abstracts/<key>.md`. Skill for future passes: `.claude/skills/verify-sources`.

**Corrections made:**
| Event | Was | Now | Source |
|---|---|---|---|
| `tetrapod-trackways` | 395 ± 3 Ma | 391.6 ± 1.7 Ma, early Eifelian (ICS 2023: Eifelian 393.3–387.7) | niedzwiedzki2010 |
| `montsechia` | 130 Ma | Barremian, 123.6 ± 2.2 Ma (ICS 2023: 125.77–121.4) | gomez2015 |
| `chorhat-burrows` | 1600 ± 10 Ma; "widely doubted" | 1614 ± 22 Ma (between tuffs 1628 ± 8 and 1599 ± 8); "biological origin has been questioned" | rasmussen2002 |
| `rodinia-assembles` | span 1.1–0.9 Ga | 1.3–0.9 Ga | li2008 |
| `mackenzie-lip` | no t_err | ± 2 Myr (1267 ± 2 Ma) | lecheminant1989 |
| `tamu-massif` | 145 Ma | 144.6 ± 0.8 Ma | sager2013 |
| `qingshania-multicellular` | "up to 20 or more cells" | "cells up to 190 µm wide, some holding possible spores" (no cell count in the paper) | miao2024 |
| `mcarthur-river-zinc` | brine/euxinic wording, "Here's Your Chance", "stagnant" basin | removed (not in source); added the 1655–1640 Ma regional synchrony | page1998 (merged into `mount-isa-ore` 2026-11-23) |
| `wiborg-rapakivi` | "Finnish for crumbly stone" | removed (not in source); "type locality" added | ramo2014 |
| `gale-crater-lakes` | "an impact 3.8–3.6 Ga makes Gale crater" | the mound's layered sediment builds 3.8–3.6 Ga | thomson2011 (new) |
| `chicxulub-impact` | "about 10 km across" | "a large asteroid" (size not in renne2013) | renne2013 |
| `franklin-lip-sturtian` | "the eruptions may have helped trigger it" | removed (not in sources) | macdonald2010 |
| `moyero-superchron` | "Its upper limit is debated" | removed (not in source) | pavlov2005 |
| `lomekwi-stone-tools` | "older than the earliest known _Homo_ fossils" | removed (not in source) | harmand2015 |
| `inner-core-nucleation-early` | Ediacaran alternative uncited | bono2019 added | bono2019 |
| `vesta-rheasilvia-impact` | marchi2012 only (abstract was a journal summary) | heck2017 added (500 km basin ~1 Ga) | heck2017 |

**Still unverified (13 events):**
| Event | What is missing |
|---|---|
| `nuvvuagittuq-crust` | Source for the ~3.8 Ga counter-view (e.g. Cates & Mojzsis 2007); date itself matches oneil2008 |
| `barberton-komatiites` | arndt2008 not read: 1,600 °C, "400 °C hotter", span 3.5–3.3 Ga |
| `sudbury-impact` | Primary source (Krogh, Davis & Corfu 1984, OGS Special Volume 1; no DOI); erickson2020 is secondary |
| `neoproterozoic-oxygenation` | och2012 dates (800–540 Ma not found; Wikipedia says ~850–540) |
| `dickinsonia-animal` | 558 Ma appears only in press releases; need a radiometric age for the Lyamtsa (White Sea) beds |
| `pangaea-assembled` | nance2014 is an essay; need a source dating final assembly (~320 Ma uncertain; terminal Alleghanian collision ~290 Ma) |
| `late-paleozoic-ice-age` | span 360–260 Ma not supported; montanez2013 cites ~70 Myr; others ~330–255 Ma |
| `archaeopteryx` | foth2014 has no age; Solnhofen (early Tithonian) age needs a source |
| `borealopelta-last-meal` | 112 Ma vs the 2017 paper's "Aptian" (ICS: Aptian ends 113.2 Ma) |
| `europa-young-surface` | 30–70 Myr comes from Zahnle's 2004 workshop abstract, not zahnle2003 |
| `shoemaker-levy-9` | 16–22 July 1994 not in hammel1995 abstract |
| `mars-deuteronilus-ocean` | ivanov2017 abstract not retrievable (Elsevier 403, ADS empty); check the ~3.6 Ga model age and that it dates the Vastitas Borealis surface, not the water (added 2026-11-22, dig 176–202) |
| `premier-kimberlite` | Neither abstract says the Cullinan diamond came from the Premier mine or that it is the largest gem diamond found; t_err 30 Myr is a placeholder for tappe2021's 'c. 1150 Ma' (a precise age: Wu et al. 2013, Chem. Geol., doi 10.1016/j.chemgeo.2012.06.002, no abstract) (added 2026-11-22, dig 666–694) |

**Non-event items checked:** hutchinson2011 (adults 6,000–8,000 kg, "Sue" ~9,500 kg: caption OK); williams2000
(620 Ma: 21.9 ± 0.4 h, 400 ± 7 days: OK); gough1981 (luminosity rose from ~70%: consistent with the model formula).
**Not checked:** cohen2013 boundaries vs ICS v2023/09, PhyloPic attribution wording, the "General-knowledge statements" table.

## Original backlog (2026-11-19/20)

Every citation and number in the original tables was written **from memory** during the design sessions (2026-11-19/20), to build
the engine. None has been checked against the source text. A research session should open each source, confirm
or correct the claim and the bibliographic details, then set `"verified": true` (events) or tick it here.

| Key | Used for | Claim to check |
|---|---|---|
| connelly2012 | event `solar-system-first-solids` | CAI age −4,567,300,000 ± 160,000; Science 338:651–655; DOI |
| barboni2017 | event `moon-forms` | Moon formed by ~4.51 Ga (Apollo 14 zircons); ± used here is 10 Myr (my choice; check the paper's stated uncertainty) |
| wilde2001 | event `jack-hills-zircon` | 4.404 ± 0.008 Ga zircon; continental crust and water; Nature 409:175–178 |
| bekker2004 | event `great-oxidation` | Rise of O₂ by ~2.32 Ga; ± 10 Myr is my choice; Nature 427:117–120 |
| burgess2014 | event `end-permian-extinction` | Onset 251.941 ± 0.037 Ma; ~60 kyr duration; PNAS 111:3316–3321 |
| renne2013 | event `chicxulub-impact` | 66.043 ± 0.011 Ma; Science 339:684–687 |
| hutchinson2011 | art caption (T. rex) | Adult mass "roughly 6 to 9 tonnes"; also confirm a citation exists for "western North America, last few million years of the Cretaceous" |
| cohen2013 | timescale.json, foredge.json, boundary descriptions | All unit boundary ages vs **ICS chart v2023/09** (or a newer version); citation details |
| williams2000 | day_length, days_per_year series | 620 Ma: 21.9 ± 0.4 h, 400 ± 7 days/yr; present 24.0 h / 365.24 days cited to the same paper (find a better source for present values?) |
| gough1981 | sun_luminosity model | L/L⊙ = 1/(1 + 0.4(1 − t/t⊙)), t⊙ = 4.57 Gyr; Solar Physics 74:21–34; DOI |
| phylopic-tyrannosaurus | drawing | Fetched from the PhyloPic API (fact, not memory): CC BY 4.0, Fred Wierum. Confirm the attribution wording the license requires |

Also check:
- **Footer interpolation:** day length and days per year are interpolated *linearly* between 620 Ma and today. That's a
  placeholder; a proper tidal-history curve with more data points is needed (session 7, footer metrics research).
- **Hadean start:** −4,567,000,000 is an informal convention; decide whether to use it or the CAI age.

## Solar theme (2026-11-20)
Bibliographic details came from doi.org/Crossref (reliable). Dates were checked against abstracts or search
summaries, **not** the full papers. Uncertainties marked "my choice" were set by the session.

| Key | Used for | Claim to check |
|---|---|---|
| kruijer2014 | `iron-meteorite-parents-accrete` | Accretion 0.1–0.3 Myr after CAIs; core formation over ~1 Myr |
| kruijer2017 | `jupiter-core-forms` | Core within ~1 Myr; barrier / no super-Earths; ± 0.5 Myr my choice |
| dauphas2011 | `mars-half-grown` | Half size in 1.8 (+0.9/−1.0) Myr; "stranded embryo" |
| wang2017 | `solar-nebula-disperses` | Angrites 4,563.5 ± 0.1 Ma, field < 0.6 µT, disk gone within 3.8 Myr |
| bouvier2018 | `mars-crust-forms`, `oldest-mars-zircon` | < 20 Myr for accretion/core/magma ocean (t placed mid-window, my choice); oldest zircon 4,476.3 ± 0.9 Ma in NWA 7034 |
| nesvorny2018, mojzsis2019, gomes2005, malhotra1993 | `giant-planet-instability` | Within ~100 Myr of disk dispersal; before 4,480 Ma; Nice model ~700 Myr after; Pluto 3:2 by Neptune migration. t and ± are my choice spanning 4,565–4,475 Ma |
| ruizlara2020 | `sagittarius-passage-1900`, `-1000` | Star-formation bursts 5.7, 1.9, 1.0 Gyr; Sgr pericentres ~2.2 and ~1.1 Gyr per the paper |
| marchi2012 | `vesta-rheasilvia-impact` | ~1 Ga crater age (model dependent); ~500 km diameter |
| heck2017 | `l-chondrite-breakup` | 466 Ma; largest disruption in 3 Gyr; fossil meteorites in Ordovician limestone |
| strom1994, price1994 | `venus-resurfacing` | ~300 Ma (Strom); 300–500 Ma (Price & Suppe) |
| iess2019, kempf2023 | `saturn-rings-form` | 10–100 Myr (Iess); ≤ a few hundred Myr (Kempf) |
| wallner2016 | `supernova-iron-60-*` | Influxes 1.5–3.2 and 6.5–8.7 Ma; sources within ~100 pc |
| schiller2011 | `hed-parent-body-solidifies` | Magma ocean onset 0.6 (+0.5/−0.4) Myr; near-solid 2–3 Myr later; authors' "smaller than Vesta" argument. t, ± my choice |
| kleine2002, yin2002 | `earth-core-forms` | Terrestrial cores within ~30 Myr; smaller bodies earlier. ± 10 Myr my choice |
| portegieszwart2021 | `sun-leaves-birth-cluster` | Ejection 20–50 Myr; Oort cloud mostly later; captured fraction |
| marchi2013 | `mercury-resurfaced` | 4.0–4.1 Ga; volcanism ends within 300–400 Myr |
| mittelholz2020 | `mars-dynamo-still-active` | Dynamo at 4.5 and 3.7 Ga; Lucus Planum; unmagnetized basins |
| grotzinger2015 | `gale-crater-lakes` | Crater 3.8–3.6 Ga; ≥ 75 m fill; lakes intermittent over thousands–millions of years |
| zahnle2003, kivelson2000 | `europa-young-surface` | 30–70 Myr (Case A, seen only in secondary sources; check the paper); factor-of-3 uncertainty; ocean from magnetometer |
| hammel1995 | `shoemaker-levy-9` | 16–22 July 1994; HST imaging. t = −32 assumes present = 2026 (undecided convention) |

## Moon, impact, magnetic themes (2026-11-20)
Bibliographic details from doi.org/Crossref. Dates checked against abstracts or search summaries only.

| Key | Used for | Claim to check |
|---|---|---|
| maurice2020 | `moon-age-young-alternative` | Moon 4.40–4.45 Ga; long-lived magma ocean |
| borg2011 | `lunar-anorthosite-crust` | 60025 at 4,360 ± 3 Ma; Apollo 16 |
| su2025 | `south-pole-aitken-basin` | 4.25 Ga (second age 3.87 Ga in same paper); "largest and oldest well-preserved" |
| bottke2017 | `late-heavy-bombardment` | Elevated flux ~4.2–4.0 to 3.5 Ga; tail to 2.5–2.0 Ga. Span ends my choice within those ranges |
| mighani2020 | `lunar-dynamo-strong`, `lunar-dynamo-ends` | Tens of µT 4.25–3.56 Ga; ceased 1.92–0.80 Ga; core crystallization |
| stoffler2001 | `nectaris-basin`, `imbrium-basin`, `copernicus-crater`, `tycho-crater` | Nectaris 3.92 ± 0.03 (alt 3.85); Imbrium 3.85 (secondary); Copernicus 800 ± 15 Ma; Tycho 109 ± 4 Ma; sampled by Apollo |
| merle2014 | `imbrium-basin` | Phosphate age 3,934 Ma (attributed via search summary to "Nemchin 2014"; check it is this paper) |
| li2021 | `youngest-lunar-volcanism` | 2,030 ± 4 Ma; most basalt volcanism ended 2.9–2.8 Ga |
| mazrouei2019 | `impact-rate-increase` | Factor ~2.6 increase **~290 Ma (from memory)**; abstract snippet only says "within ~500 Myr" |
| drabon2024, lowe2015 | `archean-impact-s2` | 3.26 Ga; ≥16 Archean impacts >10 km; tsunami, upper-ocean boiling, iron upwelling, quick recovery; Barberton (merged into `impacts-boil-oceans` 2026-11-23) |
| erickson2020 | `yarrabubba-impact`, `sudbury-impact` | Yarrabubba 2229 ± 5 Ma, ~70 km; Sudbury 1850 ± 1 Ma (**secondary citation**; primary is Krogh et al. 1984, no DOI found) |
| kamo1996 | `vredefort-impact` | 2,023 ± 4 Ma |
| hodych1992 | `manicouagan-impact` | 214 ± 1 Ma; ~12 Myr before T/J boundary |
| bottomley1997 | `popigai-impact` | 35.7 ± 0.2 Ma (value seen only on Wikipedia); not K/T |
| phillips1991, nishiizumi1991 | `meteor-crater` | 49.7 ± 0.85 ka (³⁶Cl); ≥ 49.2 ± 1.7 ka (¹⁰Be–²⁶Al) |
| chyba1993 | `tunguska-airburst` | 30 June 1908; stony asteroid, tens of metres. t = −118 assumes present = 2026 |
| tarduno2015, borlina2020 | `earliest-geodynamo` | 4.2 Ga field; rebuttal: pre-3.5 Ga field unknown |
| tarduno2010 | `geodynamo-3450` | 3.45–3.4 Ga; Kaapvaal; magnetopause ~half present distance |
| biggin2015 | `inner-core-nucleation-early` | Mesoproterozoic ~1.5–1 Ga |
| bono2019 | `ediacaran-weak-field` | ~565 Ma; 10× weaker; Sept-Îles, Quebec |
| ogg2020 | `kiaman-superchron`, `cretaceous-normal-superchron` | **Kiaman 318–265 Ma from memory**; CNS 121–84 Ma (secondary citing Ogg 2020) |
| singer2019 | `brunhes-matuyama-reversal` | 773 ka; excursions 795 and 784 ka |
| cooper2021 | `laschamps-excursion` | ~41 ka; kauri radiocarbon; crisis claim debated |
| byerly2002 | `earliest-impact-spherule-bed` | **3.47 Ga from memory**; Pilbara + Kaapvaal correlation |
| yue2020 | `orientale-basin` | 3.80 Ga; earlier 3.68–3.8 Ga |
| pavlov2005 | `moyero-superchron` | 15–20 Myr, Floian–Darriwilian; **span hand-mapped to ages** |
| assisfernandes2019 | `chesapeake-bay-impact` | Tektites 34.86 ± 0.25 Ma (isochron mean) |
| morota2009 | `giordano-bruno-crater` | 1–10 Ma; 22 km; rules out 1178 AD |
| popova2013, brown2013 | `chelyabinsk-airburst` | 15 Feb 2013; ~20 m (Popova) / ~19 m (Brown); ~500 kt. t = −13 assumes present = 2026 |
| gasperini2007 | `tunguska-airburst` | Lake Cheko proposal; 5–10 km burst height; >2,000 km² forest |

## Earth-system and life themes (2026-11-20, bulk pass)
Bibliographic details from doi.org/Crossref; titles confirmed. **Most dates and numbers in this batch were written
from memory and checked only against paper titles**, so every entry needs a full check. Highest-risk claims:

| Key | Event | Claim to check |
|---|---|---|
| tang2016 | `plate-tectonics-onset` | ~3.0 Ga |
| zhao2002, li2008, nance2014 | supercontinent events | Columbia 2.1–1.8; Rodinia 1.1–0.9 in, 825–740 out; Pangaea complete ~320 Ma |
| najman2010, garzione2008, odea2016 | collisions/mountains | ~50 Ma; Andes 10–6 Ma; Panama 2.8 Ma |
| lecheminant1989, heaman1992, macdonald2010 | Mackenzie, Franklin | 1267 Ma; Franklin ~717 Ma = Sturtian onset |
| jourdan2014, turgeon2008, schoene2019, kasbohm2018, storey2012 | LIPs | 510.7 ± 0.6; OAE2 ~94 Ma; Deccan span 66.4–65.4 (my choice); CRB 16.7–15.9; Toba 73.88 ± 0.32 ka |
| crowe2013, planavsky2014, som2016, zerkle2012, anbar2007 | early oxygen/air | 3.0; 2.95; <0.5 bar at 2.7; haze 2.65–2.5; whiff 2.5 Ga |
| gumsley2017, och2012, berner2006 | GOE/Huronian, NOE, O₂ peak | Huronian span 2.45–2.22 (memory); NOE 800–540 (memory); O₂ peak ~300 Ma |
| bekker2010, poulton2004, krijgsman1999, garciacastellanos2009, granot2016 | oceans | BIF peak ~2.5; 1.84 Ga; 5.96–5.33 Ma; flood months–2 yr; 340 Ma crust |
| rooney2015, hoffman1998, pu2016, finnegan2011, montanez2013 | glaciations | Sturtian 717–660, Marinoan 650(memory)–635; Gaskiers 580, <340 kyr; first Ediacarans 571 (memory); Hirnantian 445; LPIA 360–260 (memory) |
| mcinerney2011, coxall2005, zachos2001, clark2009 | Cenozoic climate | PETM ~5 °C, ~200 kyr recovery (memory); 33.9 Ma; EECO 52–50; MMCO 17–14 (memory); LGM 26.5–19 ka, >100 m |
| ueno2006, stueken2015 | cycles | 3.46 Ga methanogens; 3.2 Ga N-fixation |
| moody2024, bell2015, dodd2017, nutman2016, allwood2018, schopf2017, allwood2006 | earliest life | 4.2 Ga LUCA; 4.1 Ga; 3.77–4.28; 3.7; 3.465; 3.43 |
| han1992, elalbani2010, javaux2001, gibson2017, tang2020, loron2019 | early eukaryotes | 2.1 (Grypania redated ~1.87, need source); 2.1; ~1.5; 1.047; ~1.0; 0.9–1.0 Ga |
| brocks2017, love2009, bobrovskiy2018, erwin2011 | early animals | 659–645 Ma; >635 Ma; ~558 Ma (memory); Cambrian span 539–515 (my choice) |
| shu1999, zhu2022, zhu2013, rudkin2008, zhu2012 | fishes/horseshoe crab | 518 (memory); 439; ~423 (memory); 445; 410 Ma |
| wellman2003, brookfield2020, engel2004, niedzwiedzki2010 | land invasion | ~470 (memory); 425; ~400; 395 Ma |
| stein2020, stein2007, gerrienne2004, daeschler2006, percival2018 | Devonian | 386; 385; 385; 375 (memory); 371.93 Ma |
| sahney2010, clapham2012 | Carboniferous | ~305 Ma; griffinfly wingspan ~70 cm (memory) |
| martinez2011, li2008b, luo2011, foth2014 | Mesozoic animals | 231.4; ~220; 160; ~150 Ma |
| gomez2015, sun2002, penalver2012, prasad2005 | Cretaceous plants | 130; ~125; ~110; ~67 Ma (memory) |
| wilsonmantilla2021, thewissen2001, cerling1997 | Cenozoic | 65.9; ~50; 8–6 Ma |
| brunet2002, haileselassie2001, richter2017, oktaviana2024, barnosky2004 | humans/megafauna | 6–7; 5.2–5.8 Ma; 315 ± 34 ka; ≥51.2 ka; 50–10 ka span (my choice) |
| daley2014 | Anomalocaris caption | grasping appendages; Burgess Shale |

## Verification pass (2026-11-21)
Checked the "from memory" claims of the earlier batches against abstracts. Abstracts came from Crossref, OpenAlex,
Europe PMC and Semantic Scholar; full text was read where available: Clark 2009, Hoke & Garzione 2008,
Rooney 2013 and Hoffman 2017. **57 events were set `verified: true`**: date and claim match the abstract or full text.
Mid-pass count: 101 unverified. After this session's new batch: 118 of 201.

**Corrections made:**
| Event | Was | Now | Source |
|---|---|---|---|
| `first-land-animal-millipede` | _Kampecaris_ "air-breathing" at 425 Ma | Kerrera myriapods 425 Ma; oldest millipede with spiracles (Cowie) 414 Ma | brookfield2020 |
| `oldest-complete-jawed-fish` | 439 Ma | 436 Ma (Telychian) | zhu2022 |
| `entelognathus` | 423 Ma | 419 Ma | zhu2013 |
| `oldest-coelacanth` | skull named _Eoactinistia_ | skull is _Euporosteus yunnanensis_ (_Eoactinistia_ is an Australian jaw) | zhu2012 |
| `oceanic-anoxic-event-2` | 94 Ma | 93.5 Ma | turgeon2008 |
| `sturtian-glaciation` | 717–660, "some 57 Myr" | 717–659 Ma, 57–59 Myr | hoffman2017, rooney2013 (new) |
| `marinoan-glaciation` | 650–635 (memory) | ca. 645–635 Ma (onset 649.9–639.0) | hoffman2017 |
| `sponge-biomarkers` | 660 Ma (my choice) | 652 ± 7 Ma, "no later than the interlude between the glaciations" | love2009, hoffman2017, brocks2017 |
| `first-ediacaran-macrofossils` | 571 Ma | 575 ± 4.5 Ma, "within 9.5 Myr after Gaskiers" | pu2016 |
| `grypania` | 2.1 Ga | 1,874 ± 9 Ma (correlated volcanic layer), original 2.1 Ga in text | han1992, schneider2002 (new) |
| `kiaman-superchron` | 318–265 (memory) | 315–260 Ma, ends debated | opdyke1995 (new) |
| `huronian-glaciation` | 2.45–2.22 (memory) | 2.45–2.21 Ga | young2013 (new) |
| `andes-rise` | Garzione only | 2.5 ± 1 km between 10 and 6 Ma; spurts of 1–4 Myr | hoke2008 (new), garzione2008 |
| `petm` | "~5 °C within a few thousand years" | 5–8 °C; carbon release < 20 kyr; event ~200 kyr | mcinerney2011 |
| `last-glacial-maximum` | ">100 m" | ~130 m (their ice model), 26.5–19 ka | clark2009 |
| `deccan-traps` | "tens of thousands of years before" | four pulses over 700–800 kyr, first before the extinction | schoene2019, schoene2021 (new) |
| `columbia-river-basalts` | 16.7–15.9, "800 kyr" | from 16.65 Ma, 750 kyr | kasbohm2018 |
| `mid-miocene-climatic-optimum` | 17–14, zachos2001 | ~2 Myr interval, 17–15 Ma | steinthorsdottir2021 (new), kasbohm2018 |
| `earliest-impact-spherule-bed` | "cratons close together" (unsupported) | single global fallout layer, 3,470 ± 2 Ma | byerly2002 |
| `toba-supereruption` | "largest of the last 2 Myr" | largest on land in the Quaternary; humans in South Africa thrived through it | storey2012, smith2018 (new) |
| `wattieza-trees` | "palm-like" | tree-fern-like, ≥ 8 m | stein2007 |
| `proterocladus-green-alga` | "lineage that gave rise to land plants" | chlorophytes are cousins of that lineage | tang2020 |
| `carboniferous-oxygen-peak` | stated as fact | model result, disputed by later models and proxies; tagged `debated` | berner2006, krause2018 (new) |
| several | t_err 0 | t_err from the stated range (LUCA ±120 Myr, Bangiomorpha ±15 Myr, fungi ±60 Myr, Nuvvuagittuq ±67 Myr, ...) | as cited |

**Confirmed as written:** mazrouei2019 (2.6× rise ~290 Ma; via the paper PDF and coverage, not the abstract);
bottomley1997 (Popigai 35.7 ± 0.2 Ma; abstract via search); krijgsman1999 (MSC onset 5.96 ± 0.02 Ma; abstract via search).

**Still unverified after this pass** (abstract silent or unavailable; check the full text):
- Supercontinents and LIPs: zhao2002, li2008, nance2014 (a history essay; a better Pangaea source is needed),
  lecheminant1989, heaman1992, och2012 (NOE span), tang2016.
- Dates chosen by the session: Deccan span ends, EECO 53–49 (westerhold2020 text not read), LPIA 360–260
  (montanez2013 abstract has no dates), Cambrian explosion span, megafauna span, Tiktaalik ±5 Myr (stage range),
  first-land-plants and tetrapod-trackways ±.
- Ages not in the abstract: Dickinsonia 558 Ma (press release only), Archaeopteryx, Eoraptor, Pakicetus,
  Montsechia, grass coprolites, C4 grasslands, Panama 2.8 Ma, India–Asia 51.7 ± 1.1 (from the abstract's
  marine-facies range; the collision definition varies).

## New batch (2026-11-21): categories from the "further" list
Bibliographic data from doi.org/Crossref. `verified: true` where the abstract (or the PMC full text) states the date and
the claim. Remaining checks:

| Key | Event | Claim to check |
|---|---|---|
| mitchell2023 | `stalled-day` | span 2.0–1.0 Ga is the session's reading of "about 1 billion years during the mid-Proterozoic" |
| haq2014 | `cretaceous-sea-level-peak` | 240–250 m earliest Turonian; 75–250 m envelope (catalogue record, not the paper) |
| haq2008 | `ordovician-sea-level-peak` | t = Katian midpoint (session's choice); "up to ~125 m" is from the abstract |
| sager2013 | `tamu-massif` | 145 Ma, 650 km across, "largest single volcano" (press release) |
| floudas2012, nelsen2016 | `lignin-and-coal` | t at the Carboniferous–Permian boundary (session's choice); Floudas's own date not read |
| pawlowski2003 | `first-foraminifera` | early Cambrian 530 ± 9 Myr (session's choice) |
| sims2006 | `diatom-floras` | 120 ± 15 Myr for the Early Cretaceous floras (session's choice) |
| harmand2015 | `lomekwi-stone-tools` | "older than the earliest known _Homo_ fossils" (not in the abstract) |
| reisz2005 | `massospondylus-embryos` | ~190 Ma (Elliot Formation, not in the abstract) |
| johnson1996 | `lake-victoria-cichlids` | t = −14,500 is the session's calendar conversion of 12,400 radiocarbon years |
| zhou2003 | `ginkgo-unchanged` | > 121 Myr, Yixian Formation (only the Semantic Scholar summary was read) |
| leakey1979 | `laetoli-footprints` | 3.66 ± 0.1 Ma (sources say 3.6–3.7) |
| walter1994 | `lucy` | 3.18 Ma (abstract via search) |
| brown2020 | `borealopelta-last-meal` | ~112 Ma (Clearwater Formation, not in the abstract) |
| tapanila2013 | `helicoprion` | 275 ± 15 Myr (session's choice: "Late Paleozoic") |
| deng2021 | `paraceratherium` | 26.5 Ma; "one of the largest land mammals" (abstract not read) |
| bianucci2023, motani2024 | `perucetus` | ~39 Ma; heaviest-ever claim and its rebuttal |
| davies2021 | `arthropleura` | t = Serpukhovian midpoint (session's choice) |
| hu2023 | `human-bottleneck-930ka` | mini-graph is schematic; only 1,280 and 930–813 ka are data |

## General-knowledge statements (not checked against any source)
Stated from general knowledge in conversation or in docs (2026-11-21). **None is in the event data yet.** Each needs a
source before use.

| Statement | Where it appears | Use if verified |
|---|---|---|
| Base of the Cambrian GSSP is at Fortune Head, Newfoundland | chat (golden spikes) | boundary label |
| Base of the Paleogene (K–Pg) GSSP is at El Kef, Tunisia | chat | boundary label |
| Ediacaran GSSP at Enorama Creek, South Australia, ratified 2004; first new period in over a century | chat | boundary label |
| ~~Boundaries older than the Ediacaran are defined by numeric ages (GSSAs), not spikes~~ (vankranendonk2012 Fig. 16.1 caption; plumb1991; 2026-11-23) | chat | introduction |
| The Anthropocene proposal (Crawford Lake) was rejected in 2024 | chat | page 914 / back matter |
| James Hutton recognized deep time at Siccar Point (1788) | chat (famous rocks) | history note |
| Gubbio (Bottaccione Gorge) K–Pg clay is where the iridium anomaly was found (Alvarez et al. 1980) | chat | Chicxulub entry |
| Hamelin Pool, Shark Bay, has living stromatolites | chat | page 914 / caption |
| Year length in hours stays constant while day length changes | footer-candidates.md | days-per-year footer |
| Lead ages in the open-stretch table: ~~Pongola glaciation ~2.9 Ga~~ (young1998 abstract, 2026-11-21); Moodies tidal deposits ~3.2 Ga; ~~spherule layers ~2.63/2.56/2.49 Ga~~ (rasmussen2005, 2026-11-22); Midcontinent Rift ~1.1 Ga; Bushveld ~2.05 Ga; ~1.56 Ga multicellular fossils in China; ~~Columbia breakup 1.5–1.3 Ga~~ (zhao2004: 1.6–1.2 Ga); ~~Kenorland 2.7–2.5 Ga~~ (bleeker2003: supercratons ~2.6 Ga); Northern Hemisphere glaciation ~2.7 Ma; deglaciation onset 19–20 ka (this one is in clark2009's abstract) | content-categories.md | new events |
| Footer leads: Foster et al. 2017 (CO₂), Scotese et al. 2021 (temperature), Miller et al. 2005 (sea level), Bar-On et al. 2018 (biomass ~550 Gt C), Alroy et al. 2008 (diversity) | footer-candidates.md | footer series |

## Names explainer (2026-11-23): uncited glosses
Printed on the back-matter page “Names of geological time” (data/explainers/timescale-names.json) with empty `sources`.
Standard Greek glosses, but no source checked yet. Find one (a time-scale handbook or dictionary with an etymology) and add it.

| Statement | Where |
|---|---|
| Phanerozoic = Greek “visible life” (coined by G. H. Chadwick, 1930, per secondary sources; not printed) | Phanerozoic row |
| Paleozoic / Mesozoic / Cenozoic = “old / middle / new life” (morrell2001 confirms only that Phillips named them in 1841) | era rows |
| Prefixes Eo- dawn, Paleo- old, Meso- middle, Neo- new; era glosses “Dawn of the Archean” etc. | Precambrian era rows, footnote |

## 1.64–1.50 Ga batch (2026-11-21)
DOIs and titles came from web search summaries (publisher, PMC, Crossref mirrors). Dates came from abstracts or search summaries, not the full papers.

| Key | Used for | Claim to check |
|---|---|---|
| brocks2023 | `protosterol-biota` | Protosterols in the 1.64 Ga Barney Creek Fm; full author list |
| page1998 | `protosterol-biota`, `mcarthur-river-zinc` | HYC Pyritic Shale tuffs 1638 ± 7, 1640 ± 3, 1639 ± 3 Ma; brine/euxinic wording (merged into `mount-isa-ore` 2026-11-23) |
| miao2024 | `qingshania-multicellular` | ~1635 Ma; "up to 20 or more cells" and spore-like bodies (from memory); ± 5 Myr is the session's choice |
| ramo2014 | `wiborg-rapakivi` | Span 1642–1627 Ma; exact title (paraphrased); DOI (probably 10.17741/bgsf/86.2.00x); "crumbly stone" etymology needs a source |
| bengtson2017, bengtson2009 | `tirohan-red-algae` | Age ~1.6 Ga (Pb–Pb 1650 ± 89 Ma); ± 90 Myr is the session's choice |
| seilacher1998, rasmussen2002 | `chorhat-burrows` | ~1.6 Ga age and ± 10 Myr; rasmussen2002 authors abbreviated to "and others"; "widely doubted" needs a source (e.g. a review) |
| jagodzinski2023 | `gawler-range-volcanics` | 1595–1586 Ma, ≤ 260 kyr rhyolites; Olympic Dam link not checked in this paper |
| zhang2018 | `gaoyuzhuang-oxygenation` | Onset ~1570 Ma; ± 10 Myr is the session's choice; authors abbreviated |
| zhu2016 | `gaoyuzhuang-macrofossils` | 30 × 8 cm, ~10 µm cells, 1560 ± 5 Ma; authors abbreviated |

## Gap dig, pages 326–374 (2026-11-21)
Nine events added from `agent-notes/gaps/326-374.md`; all `verified: true` because each abstract (OpenAlex) states the claim and
date. Items still worth a check against the full text:
- `witwatersrand-gold`: t = −2.88 Ga ± 90 Myr is the session's midpoint between sedimentation onset (2.97 Ga, minter2006)
  and the cross-cutting sills (2.79 Ga, gumsley2020); the gold reefs themselves sit mostly in the upper (Central Rand)
  part. The 48,000 t figure is phillips2000's total to about 2000.
- `oldest-magnetic-reversal`: t is the midpoint of the 2775–2715 Ma succession; the reversed interval's own age is in
  strik2003's text, not the abstract.
- `pongola-glaciation`, `zimbabwe-mantle-flare`, `tumbiana-*`: t_err values are rounding allowances for "~2.9 Ga",
  "~2.75 Ga", "2.72 Ga" and "2,724 Myr".
- Leads not used (no abstract to check): heinrich2015 (10.1038/ngeo2344, Witwatersrand gold from volcanic rain and
  microbial mats; green OA copy hdl.handle.net/20.500.11850/100230), Condie 1998 crustal-growth peak, Eigenbrode &
  Freeman 2006 methanotrophy, Kambalda nickel (hoatson2006).

## Gap dig, pages 276–314 (2026-11-21)
Eight events added from `agent-notes/gaps/276-314.md`; seven are `verified: true` (claim and date in the abstract).
- `archaean-genetic-expansion` (`verified: false`): the abstract confirms 3,983 families, 27%, electron transport and
  respiration, and later oxygen use. The 3.33–2.85 Ga window comes from the paper body, recalled, not read. Green OA
  copy at hdl.handle.net/1721.1/61263 (MIT DSpace refused automated download).
- `whundo-arc`: smithies2005 has no cached abstract (date in its title); claims rest on vankranendonk2007 and vandenburg2026.
- `maniitsoq-impact-claim`: garde2012 has no cached abstract; the proposal is described in yakymchuk2021's abstract.
- `prinsep-orogeny` (merged into `pilbara-nucleus-rifts` 2026-11-23): t = midpoint of kiyokawa2019's 3070–3050 Ma; vankranendonk2007 says 3.07 Ga.
- `dominion-group-volcanism` (merged into `kaapvaal-craton-stable` 2026-11-23) map caption: "about 450 km" is measured on the map (Klerksdorp to Barberton), not from a source.

## "To add" list pass (2026-11-21/22)
Events from the content-categories.md "To add" column, one at a time. Verified unless listed here.
- `talakh-khaya-superchron` (`verified: false`): pavlov2010's abstract dates the two sections only as ~1100–800 Ma;
  t = 1050 ± 50 Ma is a placeholder for the Talakh-Khaya interval. The Wiley PDF refused automated download; read
  the paper for the section's age.
- `alps-rise` (`verified: false`): the 35 Ma rollback/Western Alpine orogenesis phase comes from a web-search
  summary of handy2010's abstract; the edoc.unibas.ch record gives only the abstract's second half (Adria as rigid
  indenter, slabs under the Alps and Apennines). Full PDF: Durham mantleplumes mirror (download failed).
- `swillingtonia-first-conifer` (`verified: false`): scott1983 gives Westphalian B only; t = 313 ± 3 Ma (Duckmantian) needs a
  timescale source for the regional stage (e.g. the Carboniferous chapter of the Geologic Time Scale 2020).
- `opabinia` (`verified: false`): t = 505.5 ± 1 Ma assumes the Burgess Shale is Wuliuan; pates2022's abstract gives no
  date. "Five eyes and a clawed proboscis" is from general knowledge (Whittington 1975, doi 10.1098/rstb.1975.0001).
- `terror-birds-phorusrhacos` (`verified: false`): labarge2024 places _Phorusrhacos_ in the Santacrucian SALMA without a
  numeric age; t = 17.5 ± 1.5 Ma needs a SALMA age source.
- `giants-causeway-antrim-lavas` (`verified: false`): lava ages are in ganerod2010's summary (read from the PDF at
  geologist.nl); the Causeway Tholeiite's place between the Tardree rhyolite and the Upper Basalt is from a GSA Today
  (July 2026) summary, not a cited source. Find a citable stratigraphy (e.g. BGS / Lyle 2000) before verifying.

## Gap dig, pages 156–174 (2026-11-22)
Three events added from `agent-notes/gaps/156-174.md`; `acasta-reheated` (merged into `acasta-gneiss` 2026-11-23) (bowring1999 abstract) and `isua-forearc-sediments`
(boyd2024 OA full text, quotes in sources/abstracts/boyd2024.md) are verified.
- `anshan-oldest-china` (cut 2026-11-23, significance review) (`verified: false`): 3773 ± 6 Ma banded trondhjemitic gneiss (Shengousi) is from web-search
  excerpts of the wan2012 abstract (Elsevier elides it; UOW repository ro.uow.edu.au/scipapers/4559 returned 403).
  zhang2023 abstract confirms "oldest rocks in China (~3.8 Ga)". The inherited-zircon objection (Wu et al., SHRIMP,
  Baijiafen/Dongshan emplaced ~3.3 and 3.1 Ga) is from a search summary, not a cited source: add a citation or soften.

## Gap dig, pages 516–534 (2026-11-22)
Seven events added from `agent-notes/gaps/516-534.md`; `purtuniq-ophiolite` (scott1992), `jormua-ophiolite` (peltonen1996),
`snowbird-eclogites` (baldwin2004), `first-phosphorites` (lepland2014) are verified from abstracts; `pechenga-nickel` (cut 2026-11-23, significance review)
and the Zaonega dates from the martin2015 accepted manuscript (quotes in sources/abstracts/martin2015.md).
- `zaonega-shungite` (`verified: false`): the oil-to-shungite claim rests on the melezhik1999 title (abstract elided).
  Read its abstract. Note the Re–Os age of 2.05 Ga for the Shunga "fossil oil field" (Hannah et al. 2008), older than
  martin2015's U–Pb 1975–1968 Ma; if the conflict matters, tag `debated`.
- `glenburgh-orogeny` (`verified: false`): 1965–1950 Ma collision window is in the companion GSWA Record 2010/5 abstract
  and in web-search summaries of johnson2011; johnson2011's own abstract was not seen (Elsevier elides it).
- `karelian-dykes-231` (cut 2026-11-23, significance review) (`verified: false`, dig 452–468): the 2.31 Ga age and the break-up link come from the
  stepanova2015 title only (abstract elided by Elsevier, none in OpenAlex/Semantic Scholar). Check the U–Pb age and error.
- `great-dyke-zimbabwe` (`verified: false`, dig 396–408): the 2574 ± 2 Ma age is in the wingate2000 abstract; the
  ~550 km × 11 km size and "world's second-largest PGE resource after the Bushveld" come from web-search snippets of
  oberthur2013 (introduction; not in its abstract). Check both in the oberthur2013 full text.
