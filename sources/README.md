# Sources cache

One file per cited paper (`abstracts/<bibkey>.md`): title, DOI link, open-access status (with the open copy's URL
when OpenAlex knows one) and the abstract. Read these **before** fetching anything online; it saves tokens and
requests. Built by `tools/source_cache.py` (OpenAlex → Crossref → Europe PMC → Semantic Scholar); rerun it after adding
sources. It only fetches keys that don't have a file yet.

Full PDFs are **not** stored. About 120 of the papers are paywalled; most open copies sit behind publisher bot
checks; and the open ones would total roughly 200 MB. Reading a PDF also costs far more tokens than an abstract.
When a claim needs the full text, open the "Open access" URL in the file.

"Abstract: no" means none was found: read the paper itself to verify those claims.

`--refetch KEY ...` re-fetches keys and also tries the publisher's landing page; `--refetch-missing` retries every
key without an abstract. Evidence found beyond the abstract (full text, search summaries) is kept in each file under
`## Verification (<date>)`, with where it came from. See `.claude/skills/verify-sources`.

| Key | Year | Title | Open access | Abstract | Link |
|---|---|---|---|---|---|
| [agangi2020](abstracts/agangi2020.md) | 2020 | The {Mesoarchaean} {Dominion} {Group} and the onset of intracontinental volcanism on the { | closed | yes | [doi](https://doi.org/10.1016/j.gr.2020.03.005) |
| [allwood2006](abstracts/allwood2006.md) | 2006 | Stromatolite reef from the Early Archaean era of Australia | closed | yes | [doi](https://doi.org/10.1038/nature04764) |
| [allwood2018](abstracts/allwood2018.md) | 2018 | Reassessing evidence of life in 3,700-million-year-old rocks of Greenland | closed | yes | [doi](https://doi.org/10.1038/s41586-018-0610-4) |
| [amato2008](abstracts/amato2008.md) | 2008 | Evolution of the {Mazatzal} province and the timing of the {Mazatzal} orogeny: Insights fr | closed | yes | [doi](https://doi.org/10.1130/B26200.1) |
| [anbar2007](abstracts/anbar2007.md) | 2007 | A Whiff of Oxygen Before the Great Oxidation Event? | closed | yes | [doi](https://doi.org/10.1126/science.1140325) |
| [andres2021](abstracts/andres2021.md) | 2021 | Morphology and taxonomy of Quetzalcoatlus Lawson 1975 (Pterodactyloidea: Azhdarchoidea) | hybrid | yes | [doi](https://doi.org/10.1080/02724634.2021.1907587) |
| [antonio2021](abstracts/antonio2021.md) | 2021 | West {Africa} in {Rodinia}: High quality paleomagnetic pole from the ~860 {Ma} {Manso} dyk | green | yes | [doi](https://doi.org/10.1016/j.gr.2021.02.010) |
| [armstrong2005](abstracts/armstrong2005.md) | 2005 | Geochronology of the {Nchanga} Granite, and constraints on the maximum age of the {Katanga | closed | no | [doi](https://doi.org/10.1016/j.jafrearsci.2005.08.012) |
| [arndt2008](abstracts/arndt2008.md) | 2008 | Komatiite | closed | yes | [doi](https://doi.org/10.1017/CBO9780511535550) |
| [ascarrunz2016](abstracts/ascarrunz2016.md) | 2016 | Triadobatrachus massinoti, the earliest known lissamphibian (Vertebrata: Tetrapoda) re-exa | diamond | yes | [doi](https://doi.org/10.1163/18759866-08502004) |
| [assisfernandes2019](abstracts/assisfernandes2019.md) | 2019 | 40Ar-39Ar step heating ages of North American tektites and of impact melt rock samples fro | green | yes | [doi](https://doi.org/10.1016/j.gca.2019.03.004) |
| [ayuso2016](abstracts/ayuso2016.md) | 2016 | Geochemistry, {Nd-Pb} Isotopes, and {Pb-Pb} Ages of the {Mesoproterozoic} {Pea Ridge} Iron | closed | yes | [doi](https://doi.org/10.2113/econgeo.111.8.1935) |
| [baldwin2004](abstracts/baldwin2004.md) | 2004 | Eclogites of the {Snowbird} tectonic zone: petrological and {U-Pb} geochronological eviden | closed | yes | [doi](https://doi.org/10.1007/s00410-004-0572-4) |
| [barboni2017](abstracts/barboni2017.md) | 2017 | Early Formation of the Moon 4.51 Billion Years Ago | gold | yes | [doi](https://doi.org/10.1126/sciadv.1602365) |
| [barden2016](abstracts/barden2016.md) | 2016 | Adaptive Radiation in Socially Advanced Stem-Group Ants from the Cretaceous | bronze | yes | [doi](https://doi.org/10.1016/j.cub.2015.12.060) |
| [barnosky2004](abstracts/barnosky2004.md) | 2004 | Assessing the Causes of Late Pleistocene Extinctions on the Continents | closed | yes | [doi](https://doi.org/10.1126/science.1101476) |
| [bekker2004](abstracts/bekker2004.md) | 2004 | Dating the Rise of Atmospheric Oxygen | closed | yes | [doi](https://doi.org/10.1038/nature02260) |
| [bekker2010](abstracts/bekker2010.md) | 2010 | Iron Formation: The Sedimentary Product of a Complex Interplay among Mantle, Tectonic, Oce | closed | yes | [doi](https://doi.org/10.2113/gsecongeo.105.3.467) |
| [bell2015](abstracts/bell2015.md) | 2015 | Potentially biogenic carbon preserved in a 4.1 billion-year-old zircon | green | yes | [doi](https://doi.org/10.1073/pnas.1517557112) |
| [bengtson2009](abstracts/bengtson2009.md) | 2009 | The controversial ``Cambrian'' fossils of the Vindhyan are real but more than a billion ye | green | yes | [doi](https://doi.org/10.1073/pnas.0812460106) |
| [bengtson2017](abstracts/bengtson2017.md) | 2017 | Three-dimensional preservation of cellular and subcellular structures suggests 1.6 billion | gold | yes | [doi](https://doi.org/10.1371/journal.pbio.2000735) |
| [bengtson2017fungi](abstracts/bengtson2017fungi.md) | 2017 | Fungus-like mycelial fossils in 2.4-billion-year-old vesicular basalt | green | yes | [doi](https://doi.org/10.1038/s41559-017-0141) |
| [berna2012](abstracts/berna2012.md) | 2012 | Microstratigraphic evidence of in situ fire in the Acheulean strata of Wonderwerk Cave, No | bronze | yes | [doi](https://doi.org/10.1073/pnas.1117620109) |
| [berner2006](abstracts/berner2006.md) | 2006 | GEOCARBSULF: A combined model for Phanerozoic atmospheric O2 and CO2 | closed | no | [doi](https://doi.org/10.1016/j.gca.2005.11.032) |
| [betts2018](abstracts/betts2018.md) | 2018 | Integrated genomic and fossil evidence illuminates life’s early evolution and eukaryote or | green | yes | [doi](https://doi.org/10.1038/s41559-018-0644-x) |
| [bianucci2023](abstracts/bianucci2023.md) | 2023 | A heavyweight early whale pushes the boundaries of vertebrate morphology | green | yes | [doi](https://doi.org/10.1038/s41586-023-06381-1) |
| [bickford2015](abstracts/bickford2015.md) | 2015 | {Mesoproterozoic}-trans-{Laurentian} magmatism: A synthesis of continent-wide age distribu | closed | yes | [doi](https://doi.org/10.1016/j.precamres.2014.11.024) |
| [biggin2015](abstracts/biggin2015.md) | 2015 | Palaeomagnetic field intensity variations suggest Mesoproterozoic inner-core nucleation | closed | yes | [doi](https://doi.org/10.1038/nature15523) |
| [blackburn2013](abstracts/blackburn2013.md) | 2013 | Zircon U-Pb Geochronology Links the End-Triassic Extinction with the Central Atlantic Magm | green | yes | [doi](https://doi.org/10.1126/science.1234204) |
| [bleeker2003](abstracts/bleeker2003.md) | 2003 | The late Archean record: a puzzle in ca. 35 pieces | closed | no | [doi](https://doi.org/10.1016/j.lithos.2003.07.003) |
| [bobrovskiy2018](abstracts/bobrovskiy2018.md) | 2018 | Ancient steroids establish the Ediacaran fossilDickinsoniaas one of the earliest animals | green | yes | [doi](https://doi.org/10.1126/science.aat7228) |
| [boessenecker2019](abstracts/boessenecker2019.md) | 2019 | The Early Pliocene extinction of the mega-toothed shark Otodus megalodon : a view from the | gold | yes | [doi](https://doi.org/10.7717/peerj.6088) |
| [bono2019](abstracts/bono2019.md) | 2019 | Young inner core inferred from Ediacaran ultra-low geomagnetic field intensity | closed | yes | [doi](https://doi.org/10.1038/s41561-018-0288-0) |
| [borg2011](abstracts/borg2011.md) | 2011 | Chronological evidence that the Moon is either young or did not have a global magma ocean | closed | yes | [doi](https://doi.org/10.1038/nature10328) |
| [borlina2020](abstracts/borlina2020.md) | 2020 | Reevaluating the evidence for a Hadean-Eoarchean dynamo | gold | yes | [doi](https://doi.org/10.1126/sciadv.aav9634) |
| [bottke2017](abstracts/bottke2017.md) | 2017 | The Late Heavy Bombardment | closed | yes | [doi](https://doi.org/10.1146/annurev-earth-063016-020131) |
| [bottomley1997](abstracts/bottomley1997.md) | 1997 | The age of the Popigai impact event and its relation to events at the Eocene/Oligocene bou | closed | yes | [doi](https://doi.org/10.1038/41073) |
| [bouvier2018](abstracts/bouvier2018.md) | 2018 | Evidence for extremely rapid magma ocean crystallization and crust formation on Mars | green | yes | [doi](https://doi.org/10.1038/s41586-018-0222-z) |
| [bowring1989](abstracts/bowring1989.md) | 1989 | 3.96 Ga gneisses from the Slave province, Northwest Territories, Canada | closed | yes | [doi](https://doi.org/10.1130/0091-7613(1989)017<0971:GGFTSP>2.3.CO;2) |
| [bowring1999](abstracts/bowring1999.md) | 1999 | Priscoan (4.00-4.03 Ga) orthogneisses from northwestern Canada | closed | yes | [doi](https://doi.org/10.1007/s004100050465) |
| [boyce2008](abstracts/boyce2008.md) | 2008 | How green was Cooksonia? The importance of size in understanding the early evolution of ph | closed | yes | [doi](https://doi.org/10.1666/0094-8373(2008)034[0179:hgwcti]2.0.co;2) |
| [boyd2024](abstracts/boyd2024.md) | 2024 | 3.7 billion year old detrital sediments in Greenland are consistent with active plate tect | gold | yes | [doi](https://doi.org/10.1038/s43247-024-01376-w) |
| [brasier1994](abstracts/brasier1994.md) | 1994 | Decision on the Precambrian-Cambrian boundary stratotype | hybrid | no | [doi](https://doi.org/10.18814/epiiugs/1994/v17i1.2/002) |
| [brocks2005](abstracts/brocks2005.md) | 2005 | Biomarker evidence for green and purple sulphur bacteria in a stratified Palaeoproterozoic | green | yes | [doi](https://doi.org/10.1038/nature04068) |
| [brocks2017](abstracts/brocks2017.md) | 2017 | The rise of algae in Cryogenian oceans and the emergence of animals | closed | yes | [doi](https://doi.org/10.1038/nature23457) |
| [brocks2023](abstracts/brocks2023.md) | 2023 | Lost world of complex life and the late rise of the eukaryotic crown | green | yes | [doi](https://doi.org/10.1038/s41586-023-06170-w) |
| [brookfield2020](abstracts/brookfield2020.md) | 2020 | Myriapod divergence times differ between molecular clock and fossil evidence: U/Pb zircon  | closed | yes | [doi](https://doi.org/10.1080/08912963.2020.1762593) |
| [brown2013](abstracts/brown2013.md) | 2013 | A 500-kiloton airburst over Chelyabinsk and an enhanced hazard from small impactors | green | yes | [doi](https://doi.org/10.1038/nature12741) |
| [brown2020](abstracts/brown2020.md) | 2020 | Dietary palaeoecology of an Early Cretaceous armoured dinosaur (Ornithischia; Nodosauridae | gold | yes | [doi](https://doi.org/10.1098/rsos.200305) |
| [brunet2002](abstracts/brunet2002.md) | 2002 | A new hominid from the Upper Miocene of Chad, Central Africa | closed | yes | [doi](https://doi.org/10.1038/nature00879) |
| [buchan2012](abstracts/buchan2012.md) | 2012 | Malley diabase dykes of the {Slave} craton, {Canadian} {Shield}: {U--Pb} age, paleomagneti | closed | yes | [doi](https://doi.org/10.1139/e11-061) |
| [bulakh2020](abstracts/bulakh2020.md) | 2020 | Rapakivi granite in the architecture of {St Petersburg}: a potential {Global Heritage Ston | closed | yes | [doi](https://doi.org/10.1144/SP486-2018-5) |
| [burgess2014](abstracts/burgess2014.md) | 2014 | High-Precision Timeline for Earth's Most Severe Extinction | bronze | yes | [doi](https://doi.org/10.1073/pnas.1317692111) |
| [burgess2015](abstracts/burgess2015.md) | 2015 | High-precision geochronology confirms voluminous magmatism before, during, and after Earth | gold | yes | [doi](https://doi.org/10.1126/sciadv.1500470) |
| [byerly2002](abstracts/byerly2002.md) | 2002 | An Archean Impact Layer from the Pilbara and Kaapvaal Cratons | closed | yes | [doi](https://doi.org/10.1126/science.1073934) |
| [cerling1997](abstracts/cerling1997.md) | 1997 | Global vegetation change through the Miocene/Pliocene boundary | closed | yes | [doi](https://doi.org/10.1038/38229) |
| [chan1994](abstracts/chan1994.md) | 1994 | Oldest direct evidence of lunar-solar tidal forcing encoded in sedimentary rhythmites, {Pr | closed | yes | [doi](https://doi.org/10.1130/0091-7613(1994)022<0791:ODEOLS>2.3.CO;2) |
| [channing2011](abstracts/channing2011.md) | 2011 | Equisetum thermale sp. nov. (Equisetales) from the Jurassic San Agustín hot spring deposit | bronze | yes | [doi](https://doi.org/10.3732/ajb.1000211) |
| [chen2025](abstracts/chen2025.md) | 2025 | Advent of three-dimensional sediment exploration reveals Ediacaran-Cambrian ecosystem tran | gold | yes | [doi](https://doi.org/10.1126/sciadv.adx9449) |
| [cheney1996](abstracts/cheney1996.md) | 1996 | Sequence stratigraphy and plate tectonic significance of the Transvaal succession of south | closed | no | [doi](https://doi.org/10.1016/0301-9268(95)00085-2) |
| [chyba1993](abstracts/chyba1993.md) | 1993 | The 1908 Tunguska explosion: atmospheric disruption of a stony asteroid | closed | yes | [doi](https://doi.org/10.1038/361040a0) |
| [clapham2012](abstracts/clapham2012.md) | 2012 | Environmental and biotic controls on the evolutionary history of insect body size | green | yes | [doi](https://doi.org/10.1073/pnas.1204026109) |
| [clark2006](abstracts/clark2006.md) | 2006 | The middle Pleistocene transition: characteristics, mechanisms, and implications for long- | closed | no | [doi](https://doi.org/10.1016/j.quascirev.2006.07.008) |
| [clark2009](abstracts/clark2009.md) | 2009 | The Last Glacial Maximum | closed | yes | [doi](https://doi.org/10.1126/science.1172873) |
| [clarke2005](abstracts/clarke2005.md) | 2005 | Definitive fossil evidence for the extant avian radiation in the Cretaceous | green | yes | [doi](https://doi.org/10.1038/nature03150) |
| [cleveland1998](abstracts/cleveland1998.md) | 1998 | Measurement of the solar electron neutrino flux with the {Homestake} chlorine detector | bronze | yes | [doi](https://doi.org/10.1086/305343) |
| [coates1990](abstracts/coates1990.md) | 1990 | Polydactyly in the earliest known tetrapod limbs | closed | yes | [doi](https://doi.org/10.1038/347066a0) |
| [cohen2013](abstracts/cohen2013.md) | 2013 | The {ICS} International Chronostratigraphic Chart | hybrid | yes | [doi](https://doi.org/10.18814/epiiugs/2013/v36i3/002) |
| [coleman2004](abstracts/coleman2004.md) | 2004 | Rethinking the emplacement and evolution of zoned plutons: Geochronologic evidence for inc | closed | yes | [doi](https://doi.org/10.1130/g20220.1) |
| [condie2009](abstracts/condie2009.md) | 2009 | Evidence and implications for a widespread magmatic shutdown for 250 {My} on {Earth} | closed | no | [doi](https://doi.org/10.1016/j.epsl.2009.03.033) |
| [connelly2012](abstracts/connelly2012.md) | 2012 | The Absolute Chronology and Thermal Processing of Solids in the Solar Protoplanetary Disk | closed | yes | [doi](https://doi.org/10.1126/science.1226919) |
| [cooper2021](abstracts/cooper2021.md) | 2021 | A global environmental crisis 42,000 years ago | green | yes | [doi](https://doi.org/10.1126/science.abb8677) |
| [coxall2005](abstracts/coxall2005.md) | 2005 | Rapid stepwise onset of Antarctic glaciation and deeper calcite compensation in the Pacifi | closed | yes | [doi](https://doi.org/10.1038/nature03135) |
| [crowe2013](abstracts/crowe2013.md) | 2013 | Atmospheric oxygenation three billion years ago | closed | yes | [doi](https://doi.org/10.1038/nature12426) |
| [czaja2016](abstracts/czaja2016.md) | 2016 | Sulfur-oxidizing bacteria prior to the {Great Oxidation Event} from the 2.52 {Ga} {Gamohaa | closed | yes | [doi](https://doi.org/10.1130/G38150.1) |
| [daeschler2006](abstracts/daeschler2006.md) | 2006 | A Devonian tetrapod-like fish and the evolution of the tetrapod body plan | closed | yes | [doi](https://doi.org/10.1038/nature04639) |
| [daley2014](abstracts/daley2014.md) | 2014 | Morphology ofAnomalocaris canadensisfrom the Burgess Shale | closed | yes | [doi](https://doi.org/10.1666/13-067) |
| [dauphas2011](abstracts/dauphas2011.md) | 2011 | Hf–W–Th evidence for rapid growth of Mars and its status as a planetary embryo | closed | yes | [doi](https://doi.org/10.1038/nature10077) |
| [david2010](abstracts/david2010.md) | 2010 | Rapid evolutionary innovation during an {Archaean} genetic expansion | green | yes | [doi](https://doi.org/10.1038/nature09649) |
| [davies2021](abstracts/davies2021.md) | 2021 | The largest arthropod in Earth history: insights from newly discovered Arthropleura remain | green | yes | [doi](https://doi.org/10.1144/jgs2021-115) |
| [davis1990](abstracts/davis1990.md) | 1990 | Report on the {Homestake} chlorine solar neutrino experiment | bronze | yes | [doi](https://doi.org/10.1017/S0252921100067920) |
| [dekock2009](abstracts/dekock2009.md) | 2009 | Validating the existence of Vaalbara in the Neoarchean | closed | no | [doi](https://doi.org/10.1016/j.precamres.2009.07.002) |
| [delsuc2016](abstracts/delsuc2016.md) | 2016 | The phylogenetic affinities of the extinct glyptodonts | bronze | yes | [doi](https://doi.org/10.1016/j.cub.2016.01.039) |
| [deng2021](abstracts/deng2021.md) | 2021 | An Oligocene giant rhino provides insights into Paraceratherium evolution | gold | yes | [doi](https://doi.org/10.1038/s42003-021-02170-6) |
| [dhuime2012](abstracts/dhuime2012.md) | 2012 | A {Change} in the {Geodynamics} of {Continental} {Growth} 3 {Billion} {Years} {Ago} | closed | yes | [doi](https://doi.org/10.1126/science.1216066) |
| [dodd2017](abstracts/dodd2017.md) | 2017 | Evidence for early life in Earth’s oldest hydrothermal vent precipitates | green | yes | [doi](https://doi.org/10.1038/nature21377) |
| [drabon2024](abstracts/drabon2024.md) | 2024 | Effect of a giant meteorite impact on Paleoarchean surface environments and life | hybrid | yes | [doi](https://doi.org/10.1073/pnas.2408721121) |
| [dudas1994](abstracts/dudas1994.md) | 1994 | Age of the Sudbury diabase dykes and their metamorphism in the Grenville Province, Ontario | gold | yes | [doi](https://doi.org/10.4095/195175) |
| [edwards1992](abstracts/edwards1992.md) | 1992 | A vascular conducting strand in the early land plant Cooksonia | closed | yes | [doi](https://doi.org/10.1038/357683a0) |
| [elalbani2010](abstracts/elalbani2010.md) | 2010 | Large colonial organisms with coordinated growth in oxygenated environments 2.1 Gyr ago | closed | yes | [doi](https://doi.org/10.1038/nature09166) |
| [eldrett2017](abstracts/eldrett2017.md) | 2017 | Water-mass evolution in the Cretaceous Western Interior Seaway of North America and equato | gold | yes | [doi](https://doi.org/10.5194/cp-13-855-2017) |
| [engel2004](abstracts/engel2004.md) | 2004 | New light shed on the oldest insect | closed | yes | [doi](https://doi.org/10.1038/nature02291) |
| [english2004](abstracts/english2004.md) | 2004 | The Laramide Orogeny: What Were the Driving Forces? | closed | yes | [doi](https://doi.org/10.2747/0020-6814.46.9.833) |
| [erickson2020](abstracts/erickson2020.md) | 2020 | Precise radiometric age establishes Yarrabubba, Western Australia, as Earth’s oldest recog | gold | yes | [doi](https://doi.org/10.1038/s41467-019-13985-7) |
| [erwin2011](abstracts/erwin2011.md) | 2011 | The Cambrian Conundrum: Early Divergence and Later Ecological Success in the Early History | closed | yes | [doi](https://doi.org/10.1126/science.1206375) |
| [evans2000](abstracts/evans2000.md) | 2000 | {SHRIMP} {U-Pb} geochronology of volcanic rocks, {Belt Supergroup}, western {Montana}: evi | closed | yes | [doi](https://doi.org/10.1139/e00-036) |
| [evans2021](abstracts/evans2021.md) | 2021 | Pannotia under prosecution | closed | yes | [doi](https://doi.org/10.1144/sp503-2020-182) |
| [evans2022](abstracts/evans2022.md) | 2022 | Environmental drivers of the first major animal extinction across the Ediacaran White Sea- | hybrid | yes | [doi](https://doi.org/10.1073/pnas.2207475119) |
| [ezcurra2020](abstracts/ezcurra2020.md) | 2020 | Enigmatic dinosaur precursors bridge the gap to the origin of Pterosauria | green | yes | [doi](https://doi.org/10.1038/s41586-020-3011-4) |
| [farquhar2000](abstracts/farquhar2000.md) | 2000 | Atmospheric Influence of Earth’s Earliest Sulfur Cycle | closed | yes | [doi](https://doi.org/10.1126/science.289.5480.756) |
| [feulner2012](abstracts/feulner2012.md) | 2012 | The faint young Sun problem | bronze | yes | [doi](https://doi.org/10.1029/2011rg000375) |
| [finnegan2011](abstracts/finnegan2011.md) | 2011 | The Magnitude and Duration of Late Ordovician–Early Silurian Glaciation | closed | yes | [doi](https://doi.org/10.1126/science.1200803) |
| [floudas2012](abstracts/floudas2012.md) | 2012 | The Paleozoic Origin of Enzymatic Lignin Decomposition Reconstructed from 31 Fungal Genome | green | yes | [doi](https://doi.org/10.1126/science.1221748) |
| [foth2014](abstracts/foth2014.md) | 2014 | New specimen of Archaeopteryx provides insights into the evolution of pennaceous feathers | closed | yes | [doi](https://doi.org/10.1038/nature13467) |
| [frankowiak2021](abstracts/frankowiak2021.md) | 2021 | Photosymbiosis in Late Triassic scleractinian corals from the Italian Dolomites | gold | yes | [doi](https://doi.org/10.7717/peerj.11062) |
| [french2015](abstracts/french2015.md) | 2015 | Reappraisal of hydrocarbon biomarkers in Archean rocks | bronze | yes | [doi](https://doi.org/10.1073/pnas.1419563112) |
| [froude1983](abstracts/froude1983.md) | 1983 | Ion microprobe identification of 4,100–4,200 Myr-old terrestrial zircons | closed | yes | [doi](https://doi.org/10.1038/304616a0) |
| [ganerod2010](abstracts/ganerod2010.md) | 2010 | The North Atlantic Igneous Province reconstructed and its relation to the Plume Generation | closed | yes | [doi](https://doi.org/10.1111/j.1365-246x.2010.04620.x) |
| [garciacastellanos2009](abstracts/garciacastellanos2009.md) | 2009 | Catastrophic flood of the Mediterranean after the Messinian salinity crisis | green | yes | [doi](https://doi.org/10.1038/nature08555) |
| [garde2012](abstracts/garde2012.md) | 2012 | Searching for giant, ancient impact structures on {Earth}: {The} {Mesoarchaean} {Maniitsoq | closed | no | [doi](https://doi.org/10.1016/j.epsl.2012.04.026) |
| [garzione2008](abstracts/garzione2008.md) | 2008 | Rise of the Andes | closed | yes | [doi](https://doi.org/10.1126/science.1148615) |
| [gasperini2007](abstracts/gasperini2007.md) | 2007 | A possible impact crater for the 1908 Tunguska Event | bronze | yes | [doi](https://doi.org/10.1111/j.1365-3121.2007.00742.x) |
| [gaucher2008](abstracts/gaucher2008.md) | 2008 | Palaeotemperature trend for Precambrian life inferred from resurrected proteins | closed | yes | [doi](https://doi.org/10.1038/nature06510) |
| [gbrdrilling2001](abstracts/gbrdrilling2001.md) | 2001 | New constraints on the origin of the Australian Great Barrier Reef: Results from an intern | closed | yes | [doi](https://doi.org/10.1130/0091-7613(2001)029<0483:ncotoo>2.0.co;2) |
| [gerard2009](abstracts/gerard2009.md) | 2009 | Modern subsurface bacteria in pristine 2.7 Ga-old fossil stromatolite drillcore samples fr | gold | yes | [doi](https://doi.org/10.1371/journal.pone.0005298) |
| [gerrienne2004](abstracts/gerrienne2004.md) | 2004 | Runcaria , a Middle Devonian Seed Plant Precursor | closed | yes | [doi](https://doi.org/10.1126/science.1102491) |
| [gerrienne2011](abstracts/gerrienne2011.md) | 2011 | A Simple Type of Wood in Two Early Devonian Plants | green | yes | [doi](https://doi.org/10.1126/science.1208882) |
| [gheerbrant2009](abstracts/gheerbrant2009.md) | 2009 | Paleocene emergence of elephant relatives and the rapid radiation of African ungulates | green | yes | [doi](https://doi.org/10.1073/pnas.0900251106) |
| [gibson2017](abstracts/gibson2017.md) | 2017 | Precise age of Bangiomorpha pubescens dates the origin of eukaryotic photosynthesis | green | yes | [doi](https://doi.org/10.1130/g39829.1) |
| [goldblatt2006](abstracts/goldblatt2006.md) | 2006 | Bistability of atmospheric oxygen and the Great Oxidation | closed | yes | [doi](https://doi.org/10.1038/nature05169) |
| [gomes2005](abstracts/gomes2005.md) | 2005 | Origin of the cataclysmic Late Heavy Bombardment period of the terrestrial planets | closed | yes | [doi](https://doi.org/10.1038/nature03676) |
| [gomez2015](abstracts/gomez2015.md) | 2015 | Montsechia , an ancient aquatic angiosperm | green | yes | [doi](https://doi.org/10.1073/pnas.1509241112) |
| [goodge2008](abstracts/goodge2008.md) | 2008 | A Positive Test of {East Antarctica}--{Laurentia} Juxtaposition Within the {Rodinia} Super | closed | yes | [doi](https://doi.org/10.1126/science.1159189) |
| [gough1981](abstracts/gough1981.md) | 1981 | Solar Interior Structure and Luminosity Variations | closed | yes | [doi](https://doi.org/10.1007/BF00151270) |
| [gower2002](abstracts/gower2002.md) | 2002 | A {U-Pb} geochronological review of the {Proterozoic} history of the eastern {Grenville Pr | closed | yes | [doi](https://doi.org/10.1139/e01-090) |
| [granot2016](abstracts/granot2016.md) | 2016 | Palaeozoic oceanic crust preserved beneath the eastern Mediterranean | closed | yes | [doi](https://doi.org/10.1038/ngeo2784) |
| [grotzinger2015](abstracts/grotzinger2015.md) | 2015 | Deposition, exhumation, and paleoclimate of an ancient lake deposit, Gale crater, Mars | closed | yes | [doi](https://doi.org/10.1126/science.aac7575) |
| [gu2012](abstracts/gu2012.md) | 2012 | Wing stridulation in a Jurassic katydid (Insecta, Orthoptera) produced low-pitched musical | green | yes | [doi](https://doi.org/10.1073/pnas.1118372109) |
| [gueneli2018](abstracts/gueneli2018.md) | 2018 | 1.1-billion-year-old porphyrins establish a marine ecosystem dominated by bacterial primar | green | yes | [doi](https://doi.org/10.1073/pnas.1803866115) |
| [guitreau2019](abstracts/guitreau2019.md) | 2019 | Hadean protocrust reworking at the origin of the {Archean} {Napier} {Complex} ({Antarctica | diamond | yes | [doi](https://doi.org/10.7185/geochemlet.1927) |
| [gumsley2017](abstracts/gumsley2017.md) | 2017 | Timing and tempo of the Great Oxidation Event | bronze | yes | [doi](https://doi.org/10.1073/pnas.1608824114) |
| [gumsley2020](abstracts/gumsley2020.md) | 2020 | Neoarchean large igneous provinces on the {Kaapvaal} {Craton} in southern {Africa} re-defi | hybrid | yes | [doi](https://doi.org/10.1130/b35237.1) |
| [haileselassie2001](abstracts/haileselassie2001.md) | 2001 | Late Miocene hominids from the Middle Awash, Ethiopia | closed | yes | [doi](https://doi.org/10.1038/35084063) |
| [hammel1995](abstracts/hammel1995.md) | 1995 | HST Imaging of Atmospheric Phenomena Created by the Impact of Comet Shoemaker-Levy 9 | closed | yes | [doi](https://doi.org/10.1126/science.7871425) |
| [han1992](abstracts/han1992.md) | 1992 | Megascopic Eukaryotic Algae from the 2.1-Billion-Year-Old Negaunee Iron-Formation, Michiga | closed | yes | [doi](https://doi.org/10.1126/science.1631544) |
| [handy2010](abstracts/handy2010.md) | 2010 | Reconciling plate-tectonic reconstructions of Alpine Tethys with the geological–geophysica | green | no | [doi](https://doi.org/10.1016/j.earscirev.2010.06.002) |
| [hanson2004](abstracts/hanson2004.md) | 2004 | Coeval Large-Scale Magmatism in the Kalahari and Laurentian Cratons During Rodinia Assembl | bronze | yes | [doi](https://doi.org/10.1126/science.1096329) |
| [haq2008](abstracts/haq2008.md) | 2008 | A Chronology of Paleozoic Sea-Level Changes | closed | yes | [doi](https://doi.org/10.1126/science.1161648) |
| [haq2014](abstracts/haq2014.md) | 2014 | Cretaceous eustasy revisited | closed | no | [doi](https://doi.org/10.1016/j.gloplacha.2013.12.007) |
| [haridy2025](abstracts/haridy2025.md) | 2025 | The origin of vertebrate teeth and evolution of sensory exoskeletons | hybrid | yes | [doi](https://doi.org/10.1038/s41586-025-08944-w) |
| [harmand2015](abstracts/harmand2015.md) | 2015 | 3.3-million-year-old stone tools from Lomekwi 3, West Turkana, Kenya | green | yes | [doi](https://doi.org/10.1038/nature14464) |
| [harms2004](abstracts/harms2004.md) | 2004 | Advances in the geology of the {Tobacco Root Mountains}, {Montana}, and their implications | bronze | yes | [doi](https://doi.org/10.1130/0-8137-2377-9.227) |
| [hatcher2010](abstracts/hatcher2010.md) | 2010 | The Appalachian orogen: A brief summary | closed | yes | [doi](https://doi.org/10.1130/2010.1206(01)) |
| [haug2005](abstracts/haug2005.md) | 2005 | North Pacific seasonality and the glaciation of North America 2.7 million years ago | green | yes | [doi](https://doi.org/10.1038/nature03332) |
| [hawkins1996](abstracts/hawkins1996.md) | 1996 | {U-Pb} geochronologic constraints on the {Paleoproterozoic} crustal evolution of the {Uppe | closed | yes | [doi](https://doi.org/10.1130/0016-7606(1996)108<1167:UPGCOT>2.3.CO;2) |
| [hays1976](abstracts/hays1976.md) | 1976 | Variations in the Earth’s Orbit: Pacemaker of the Ice Ages: For 500,000 years, major clima | closed | yes | [doi](https://doi.org/10.1126/science.194.4270.1121) |
| [head2009](abstracts/head2009.md) | 2009 | Giant boid snake from the Palaeocene neotropics reveals hotter past equatorial temperature | closed | yes | [doi](https://doi.org/10.1038/nature07671) |
| [heaman1992](abstracts/heaman1992.md) | 1992 | Nature and timing of Franklin igneous events, Canada: Implications for a Late Proterozoic  | closed | no | [doi](https://doi.org/10.1016/0012-821x(92)90078-a) |
| [heck2017](abstracts/heck2017.md) | 2017 | Rare meteorites common in the Ordovician period | closed | yes | [doi](https://doi.org/10.1038/s41550-016-0035) |
| [hodych1992](abstracts/hodych1992.md) | 1992 | Did the Manicouagan impact trigger end-of-Triassic mass extinction? | closed | yes | [doi](https://doi.org/10.1130/0091-7613(1992)020<0051:dtmite>2.3.co;2) |
| [hoffman1998](abstracts/hoffman1998.md) | 1998 | A Neoproterozoic Snowball Earth | closed | yes | [doi](https://doi.org/10.1126/science.281.5381.1342) |
| [hoffman2017](abstracts/hoffman2017.md) | 2017 | Snowball Earth climate dynamics and Cryogenian geology-geobiology | gold | yes | [doi](https://doi.org/10.1126/sciadv.1600983) |
| [hofmann2024](abstracts/hofmann2024.md) | 2024 | The {Belingwe} greenstone belt, {Zimbabwe} – some new age constraints and implications for | hybrid | yes | [doi](https://doi.org/10.1080/00206814.2024.2309477) |
| [hoke2008](abstracts/hoke2008.md) | 2008 | Paleosurfaces, paleoelevation, and the mechanisms for the late Miocene topographic develop | closed | no | [doi](https://doi.org/10.1016/j.epsl.2008.04.008) |
| [homann2018](abstracts/homann2018.md) | 2018 | Microbial life and biogeochemical cycling on land 3,220 million years ago | green | yes | [doi](https://doi.org/10.1038/s41561-018-0190-9) |
| [hopkins2008](abstracts/hopkins2008.md) | 2008 | Low heat flow inferred from >4 Gyr zircons suggests Hadean plate boundary interactions | closed | yes | [doi](https://doi.org/10.1038/nature07465) |
| [hren2009](abstracts/hren2009.md) | 2009 | Oxygen and hydrogen isotope evidence for a temperate climate 3.42 billion years ago | closed | yes | [doi](https://doi.org/10.1038/nature08518) |
| [hu2023](abstracts/hu2023.md) | 2023 | Genomic inference of a severe human bottleneck during the Early to Middle Pleistocene tran | green | yes | [doi](https://doi.org/10.1126/science.abq7487) |
| [huppert1984](abstracts/huppert1984.md) | 1984 | Emplacement and cooling of komatiite lavas | closed | yes | [doi](https://doi.org/10.1038/309019a0) |
| [huppert1985](abstracts/huppert1985.md) | 1985 | Komatiites I: Eruption and Flow | closed | yes | [doi](https://doi.org/10.1093/petrology/26.3.694) |
| [hutchinson2011](abstracts/hutchinson2011.md) | 2011 | A Computational Analysis of Limb and Body Dimensions in {Tyrannosaurus rex} with Implicati | gold | yes | [doi](https://doi.org/10.1371/journal.pone.0026037) |
| [iess2019](abstracts/iess2019.md) | 2019 | Measurement and implications of Saturn’s gravity field and ring mass | green | yes | [doi](https://doi.org/10.1126/science.aat2965) |
| [ivanov2017](abstracts/ivanov2017.md) | 2017 | Topography of the Deuteronilus contact on Mars: Evidence for an ancient water/mud ocean an | closed | no | [doi](https://doi.org/10.1016/j.pss.2017.05.012) |
| [jagodzinski2023](abstracts/jagodzinski2023.md) | 2023 | Precise zircon {U-Pb} dating of the {Mesoproterozoic} {Gawler} large igneous province, {So | gold | yes | [doi](https://doi.org/10.1016/j.ringeo.2022.100020) |
| [javaux2001](abstracts/javaux2001.md) | 2001 | Morphological and ecological complexity in early eukaryotic ecosystems | green | yes | [doi](https://doi.org/10.1038/35083562) |
| [javaux2010](abstracts/javaux2010.md) | 2010 | Organic-walled microfossils in 3.2-billion-year-old shallow-marine siliciclastic deposits | closed | yes | [doi](https://doi.org/10.1038/nature08793) |
| [javaux2025](abstracts/javaux2025.md) | 2025 | A diverse {Palaeoproterozoic} microbial ecosystem implies early eukaryogenesis | hybrid | yes | [doi](https://doi.org/10.1098/rstb.2024.0092) |
| [ji2006](abstracts/ji2006.md) | 2006 | A Swimming Mammaliaform from the Middle Jurassic and Ecomorphological Diversification of E | closed | yes | [doi](https://doi.org/10.1126/science.1123026) |
| [johnson1996](abstracts/johnson1996.md) | 1996 | Late Pleistocene Desiccation of Lake Victoria and Rapid Evolution of Cichlid Fishes | closed | yes | [doi](https://doi.org/10.1126/science.273.5278.1091) |
| [johnson2011](abstracts/johnson2011.md) | 2011 | Two collisions, two sutures: Punctuated pre-1950 {Ma} assembly of the {West Australian Cra | closed | no | [doi](https://doi.org/10.1016/j.precamres.2011.07.011) |
| [jourdan2014](abstracts/jourdan2014.md) | 2014 | High-precision dating of the Kalkarindji large igneous province, Australia, and synchrony  | green | yes | [doi](https://doi.org/10.1130/g35434.1) |
| [kamo1996](abstracts/kamo1996.md) | 1996 | A 2.023 Ga age for the Vredefort impact event and a first report of shock metamorphosed zi | closed | no | [doi](https://doi.org/10.1016/s0012-821x(96)00180-x) |
| [karhu1996](abstracts/karhu1996.md) | 1996 | Carbon isotopes and the rise of atmospheric oxygen | closed | yes | [doi](https://doi.org/10.1130/0091-7613(1996)024<0867:ciatro>2.3.co;2) |
| [karlstrom2014](abstracts/karlstrom2014.md) | 2014 | Formation of the Grand Canyon 5 to 6 million years ago through integration of older palaeo | closed | yes | [doi](https://doi.org/10.1038/ngeo2065) |
| [kasbohm2018](abstracts/kasbohm2018.md) | 2018 | Rapid eruption of the Columbia River flood basalt and correlation with the mid-Miocene cli | gold | yes | [doi](https://doi.org/10.1126/sciadv.aat8223) |
| [kempf2023](abstracts/kempf2023.md) | 2023 | Micrometeoroid infall onto Saturn’s rings constrains their age to no more than a few hundr | gold | yes | [doi](https://doi.org/10.1126/sciadv.adf8537) |
| [kenny2019](abstracts/kenny2019.md) | 2019 | On the track of a Scottish impact structure: a detrital zircon and apatite provenance stud | hybrid | yes | [doi](https://doi.org/10.1017/s0016756819000220) |
| [kiel2024](abstracts/kiel2024.md) | 2024 | Early Oligocene kelp holdfasts and stepwise evolution of the kelp ecosystem in the North P | hybrid | yes | [doi](https://doi.org/10.1073/pnas.2317054121) |
| [kivelson2000](abstracts/kivelson2000.md) | 2000 | Galileo Magnetometer Measurements: A Stronger Case for a Subsurface Ocean at Europa | closed | yes | [doi](https://doi.org/10.1126/science.289.5483.1340) |
| [kiyokawa2019](abstracts/kiyokawa2019.md) | 2019 | Timing and development of sedimentation of the {Cleaverville} {Formation} and a post‐accre | green | yes | [doi](https://doi.org/10.1111/iar.12324) |
| [kleine2002](abstracts/kleine2002.md) | 2002 | Rapid accretion and early core formation on asteroids and the terrestrial planets from Hf– | closed | yes | [doi](https://doi.org/10.1038/nature00982) |
| [knauth2003](abstracts/knauth2003.md) | 2003 | High Archean climatic temperature inferred from oxygen isotope geochemistry of cherts in t | closed | yes | [doi](https://doi.org/10.1130/0016-7606(2003)115<0566:hactif>2.0.co;2) |
| [krause2018](abstracts/krause2018.md) | 2018 | Stepwise oxygenation of the Paleozoic atmosphere | gold | yes | [doi](https://doi.org/10.1038/s41467-018-06383-y) |
| [krijgsman1999](abstracts/krijgsman1999.md) | 1999 | Chronology, causes and progression of the Messinian salinity crisis | green | yes | [doi](https://doi.org/10.1038/23231) |
| [kruijer2014](abstracts/kruijer2014.md) | 2014 | Protracted core formation and rapid accretion of protoplanets | closed | yes | [doi](https://doi.org/10.1126/science.1251766) |
| [kruijer2017](abstracts/kruijer2017.md) | 2017 | Age of Jupiter inferred from the distinct genetics and formation times of meteorites | green | yes | [doi](https://doi.org/10.1073/pnas.1704461114) |
| [kumar2012](abstracts/kumar2012.md) | 2012 | A {Paleoproterozoic} giant radiating dyke swarm in the {Dharwar} Craton, southern {India} | bronze | yes | [doi](https://doi.org/10.1029/2011GC003926) |
| [labarge2024](abstracts/labarge2024.md) | 2024 | The evolution and ecology of gigantism in terror birds (Aves, Phorusrhacidae) | green | yes | [doi](https://doi.org/10.1098/rspb.2024.0235) |
| [lantink2022](abstracts/lantink2022.md) | 2022 | Milankovitch cycles in banded iron formations constrain the Earth–Moon system 2.46 billion | hybrid | yes | [doi](https://doi.org/10.1073/pnas.2117146119) |
| [lapen2010](abstracts/lapen2010.md) | 2010 | A Younger Age for ALH84001 and Its Geochemical Link to Shergottite Sources in Mars | closed | yes | [doi](https://doi.org/10.1126/science.1185395) |
| [leakey1979](abstracts/leakey1979.md) | 1979 | Pliocene footprints in the Laetolil Beds at Laetoli, northern Tanzania | closed | yes | [doi](https://doi.org/10.1038/278317a0) |
| [lecheminant1989](abstracts/lecheminant1989.md) | 1989 | Mackenzie igneous events, Canada: Middle Proterozoic hotspot magmatism associated with oce | closed | no | [doi](https://doi.org/10.1016/0012-821x(89)90122-2) |
| [lepland2005](abstracts/lepland2005.md) | 2005 | Questioning the evidence for {Earth}'s earliest life---{Akilia} revisited | closed | yes | [doi](https://doi.org/10.1130/G20890.1) |
| [lepland2014](abstracts/lepland2014.md) | 2014 | Potential influence of sulphur bacteria on {Palaeoproterozoic} phosphogenesis | closed | yes | [doi](https://doi.org/10.1038/ngeo2005) |
| [lepot2019](abstracts/lepot2019.md) | 2019 | Extreme ¹³C-depletions and organic sulfur content argue for {S}-fueled anaerobic methane o | hybrid | yes | [doi](https://doi.org/10.1016/j.gca.2018.10.014) |
| [li1999](abstracts/li1999.md) | 1999 | The breakup of {Rodinia}: did it start with a mantle plume beneath {South China}? | closed | no | [doi](https://doi.org/10.1016/S0012-821X(99)00240-X) |
| [li2008](abstracts/li2008.md) | 2008 | Assembly, configuration, and break-up history of Rodinia: A synthesis | closed | no | [doi](https://doi.org/10.1016/j.precamres.2007.04.021) |
| [li2008b](abstracts/li2008b.md) | 2008 | An ancestral turtle from the Late Triassic of southwestern China | closed | yes | [doi](https://doi.org/10.1038/nature07533) |
| [li2021](abstracts/li2021.md) | 2021 | Two-billion-year-old volcanism on the Moon from Chang’e-5 basalts | hybrid | yes | [doi](https://doi.org/10.1038/s41586-021-04100-2) |
| [lillis2008](abstracts/lillis2008.md) | 2008 | Rapid decrease in Martian crustal magnetization in the Noachian era: Implications for the  | bronze | yes | [doi](https://doi.org/10.1029/2008GL034338) |
| [liu2014](abstracts/liu2014.md) | 2014 | Haootia quadriformis n. gen., n. sp., interpreted as a muscular cnidarian impression from  | hybrid | yes | [doi](https://doi.org/10.1098/rspb.2014.1202) |
| [liu2024](abstracts/liu2024.md) | 2024 | Chronological, Petrogenetic, and Tectonic Significance of {Paleoproterozoic} Continental C | gold | yes | [doi](https://doi.org/10.2113/2024/lithosphere_2023_234) |
| [loron2019](abstracts/loron2019.md) | 2019 | Early fungi from the Proterozoic era in Arctic Canada | green | yes | [doi](https://doi.org/10.1038/s41586-019-1217-0) |
| [love2009](abstracts/love2009.md) | 2009 | Fossil steroids record the appearance of Demospongiae during the Cryogenian period | green | yes | [doi](https://doi.org/10.1038/nature07673) |
| [lowe2015](abstracts/lowe2015.md) | 2015 | Geologic record of partial ocean evaporation triggered by giant asteroid impacts, 3.29–3.2 | closed | yes | [doi](https://doi.org/10.1130/g36665.1) |
| [luo2011](abstracts/luo2011.md) | 2011 | A Jurassic eutherian mammal and divergence of marsupials and placentals | closed | yes | [doi](https://doi.org/10.1038/nature10291) |
| [luo2016](abstracts/luo2016.md) | 2016 | Rapid oxygenation of Earth’s atmosphere 2.33 billion years ago | gold | yes | [doi](https://doi.org/10.1126/sciadv.1600134) |
| [lyons2014](abstracts/lyons2014.md) | 2014 | The rise of oxygen in Earth’s early ocean and atmosphere | closed | yes | [doi](https://doi.org/10.1038/nature13068) |
| [macdonald2010](abstracts/macdonald2010.md) | 2010 | Calibrating the Cryogenian | green | yes | [doi](https://doi.org/10.1126/science.1183325) |
| [machta1970](abstracts/machta1970.md) | 1970 | Atmospheric Oxygen in 1967 to 1970 | closed | yes | [doi](https://doi.org/10.1126/science.168.3939.1582) |
| [maconi2025](abstracts/maconi2025.md) | 2025 | The Solar System’s passage through the Radcliffe wave during the middle Miocene | gold | yes | [doi](https://doi.org/10.1051/0004-6361/202452061) |
| [malhotra1993](abstracts/malhotra1993.md) | 1993 | The origin of Pluto’s peculiar orbit | closed | yes | [doi](https://doi.org/10.1038/365819a0) |
| [manning2006](abstracts/manning2006.md) | 2006 | Geology, age and origin of supracrustal rocks at {Akilia}, {West Greenland} | bronze | yes | [doi](https://doi.org/10.2475/05.2006.02) |
| [marchi2012](abstracts/marchi2012.md) | 2012 | The Violent Collisional History of Asteroid 4 Vesta | closed | yes | [doi](https://doi.org/10.1126/science.1218757) |
| [marchi2013](abstracts/marchi2013.md) | 2013 | Global resurfacing of Mercury 4.0–4.1 billion years ago by heavy bombardment and volcanism | closed | yes | [doi](https://doi.org/10.1038/nature12280) |
| [martin2015](abstracts/martin2015.md) | 2015 | Multiple {Palaeoproterozoic} carbon burial episodes and excursions | green | yes | [doi](https://doi.org/10.1016/j.epsl.2015.05.023) |
| [martinez2011](abstracts/martinez2011.md) | 2011 | A Basal Dinosaur from the Dawn of the Dinosaur Era in Southwestern Pangaea | green | yes | [doi](https://doi.org/10.1126/science.1198467) |
| [matsumoto2025](abstracts/matsumoto2025.md) | 2025 | Multidisciplinary evidence for synchroneity between Ontong Java Nui volcanism and early Ap | gold | yes | [doi](https://doi.org/10.1126/sciadv.adt0204) |
| [maurice2020](abstracts/maurice2020.md) | 2020 | A long-lived magma ocean on a young Moon | gold | yes | [doi](https://doi.org/10.1126/sciadv.aba8949) |
| [mazrouei2019](abstracts/mazrouei2019.md) | 2019 | Earth and Moon impact flux increased at the end of the Paleozoic | closed | yes | [doi](https://doi.org/10.1126/science.aar4058) |
| [mccoy2016](abstracts/mccoy2016.md) | 2016 | The ‘Tully monster’ is a vertebrate | closed | yes | [doi](https://doi.org/10.1038/nature16992) |
| [mcinerney2011](abstracts/mcinerney2011.md) | 2011 | The Paleocene-Eocene Thermal Maximum: A Perturbation of Carbon Cycle, Climate, and Biosphe | closed | yes | [doi](https://doi.org/10.1146/annurev-earth-040610-133431) |
| [mckay1996](abstracts/mckay1996.md) | 1996 | Search for past life on {Mars}: possible relic biogenic activity in martian meteorite {ALH | green | yes | [doi](https://doi.org/10.1126/science.273.5277.924) |
| [mclelland2013](abstracts/mclelland2013.md) | 2013 | Tectonic Evolution of the Adirondack Mountains and Grenville Orogen Inliers within the USA | bronze | yes | [doi](https://doi.org/10.12789/geocanj.2013.40.022) |
| [meert2003](abstracts/meert2003.md) | 2003 | A synopsis of events related to the assembly of eastern Gondwana | closed | no | [doi](https://doi.org/10.1016/s0040-1951(02)00629-7) |
| [melezhik1999](abstracts/melezhik1999.md) | 1999 | {Karelian} shungite---an indication of 2.0-{Ga}-old metamorphosed oil-shale and generation | closed | no | [doi](https://doi.org/10.1016/S0012-8252(99)00027-6) |
| [melott2004](abstracts/melott2004.md) | 2004 | Did a gamma-ray burst initiate the late Ordovician mass extinction? | green | yes | [doi](https://doi.org/10.1017/s1473550404001910) |
| [merle2014](abstracts/merle2014.md) | 2014 | High resolution U‐Pb ages of Ca‐phosphates in Apollo 14 breccias: Implications for the age | closed | yes | [doi](https://doi.org/10.1111/maps.12395) |
| [meyers2018](abstracts/meyers2018.md) | 2018 | Proterozoic Milankovitch cycles and the history of the solar system | green | yes | [doi](https://doi.org/10.1073/pnas.1717689115) |
| [miao2019](abstracts/miao2019.md) | 2019 | New record of organic-walled, morphologically distinct microfossils from the late {Paleopr | closed | yes | [doi](https://doi.org/10.1016/j.precamres.2018.11.019) |
| [miao2024](abstracts/miao2024.md) | 2024 | 1.63-billion-year-old multicellular eukaryotes from the Chuanlinggou Formation in North Ch | gold | yes | [doi](https://doi.org/10.1126/sciadv.adk3208) |
| [mighani2020](abstracts/mighani2020.md) | 2020 | The end of the lunar dynamo | gold | yes | [doi](https://doi.org/10.1126/sciadv.aax0883) |
| [millar1999](abstracts/millar1999.md) | 1999 | {Neoproterozoic} extensional basic magmatism associated with the {West Highland} granite g | closed | yes | [doi](https://doi.org/10.1144/gsjgs.156.6.1153) |
| [miller2003](abstracts/miller2003.md) | 2003 | The oldest articulated chondrichthyan from the Early Devonian period | closed | yes | [doi](https://doi.org/10.1038/nature02001) |
| [minter2006](abstracts/minter2006.md) | 2006 | The sedimentary setting of {Witwatersrand} placer mineral deposits in an {Archean} atmosph | closed | yes | [doi](https://doi.org/10.1130/2006.1198(06)) |
| [mitchell2023](abstracts/mitchell2023.md) | 2023 | Mid-Proterozoic day length stalled by tidal resonance | hybrid | yes | [doi](https://doi.org/10.1038/s41561-023-01202-6) |
| [mittelholz2020](abstracts/mittelholz2020.md) | 2020 | Timing of the martian dynamo: New constraints for a core field 4.5 and 3.7 Ga ago | gold | yes | [doi](https://doi.org/10.1126/sciadv.aba0513) |
| [modesto2015](abstracts/modesto2015.md) | 2015 | The oldest parareptile and the early diversification of reptiles | green | yes | [doi](https://doi.org/10.1098/rspb.2014.1912) |
| [mohr2024](abstracts/mohr2024.md) | 2024 | High-precision U-Pb geochronology links magmatism in the Southwestern Laurentia large igne | hybrid | yes | [doi](https://doi.org/10.1130/g51786.1) |
| [mojzsis1996](abstracts/mojzsis1996.md) | 1996 | Evidence for life on {Earth} before 3,800 million years ago | closed | yes | [doi](https://doi.org/10.1038/384055a0) |
| [mojzsis2001](abstracts/mojzsis2001.md) | 2001 | Oxygen-isotope evidence from ancient zircons for liquid water at the Earth's surface 4,300 | closed | yes | [doi](https://doi.org/10.1038/35051557) |
| [mojzsis2019](abstracts/mojzsis2019.md) | 2019 | Onset of Giant Planet Migration before 4480 Million Years Ago | bronze | yes | [doi](https://doi.org/10.3847/1538-4357/ab2c03) |
| [montanez2013](abstracts/montanez2013.md) | 2013 | The Late Paleozoic Ice Age: An Evolving Paradigm | closed | yes | [doi](https://doi.org/10.1146/annurev.earth.031208.100118) |
| [moody2024](abstracts/moody2024.md) | 2024 | The nature of the last universal common ancestor and its impact on the early Earth system | hybrid | yes | [doi](https://doi.org/10.1038/s41559-024-02461-1) |
| [morelli2010](abstracts/morelli2010.md) | 2010 | Constraints on the genesis of gold mineralization at the {Homestake Gold Deposit}, {Black  | closed | yes | [doi](https://doi.org/10.1007/s00126-010-0284-9) |
| [morota2009](abstracts/morota2009.md) | 2009 | Formation age of the lunar crater Giordano Bruno | green | yes | [doi](https://doi.org/10.1111/j.1945-5100.2009.tb01211.x) |
| [motani2024](abstracts/motani2024.md) | 2024 | Downsizing a heavyweight: factors and methods that revise weight estimates of the giant fo | gold | yes | [doi](https://doi.org/10.7717/peerj.16978) |
| [moyen2024](abstracts/moyen2024.md) | 2024 | Felsic crust development in the {Kaapvaal} {Craton}, {South} {Africa}: {A} reference sampl | hybrid | yes | [doi](https://doi.org/10.1016/j.earscirev.2024.104680) |
| [mueller1992](abstracts/mueller1992.md) | 1992 | 3.96 Ga zircons from an Archean quartzite, Beartooth Mountains, Montana | closed | yes | [doi](https://doi.org/10.1130/0091-7613(1992)020<0327:GZFAAQ>2.3.CO;2) |
| [najman2010](abstracts/najman2010.md) | 2010 | Timing of India‐Asia collision: Geological, biostratigraphic, and palaeomagnetic constrain | green | yes | [doi](https://doi.org/10.1029/2010jb007673) |
| [nance2014](abstracts/nance2014.md) | 2014 | The supercontinent cycle: A retrospective essay | closed | no | [doi](https://doi.org/10.1016/j.gr.2012.12.026) |
| [nance2019](abstracts/nance2019.md) | 2019 | Supercontinents and the case for Pannotia | closed | yes | [doi](https://doi.org/10.1144/sp470.5) |
| [naturalearth](abstracts/naturalearth.md) | 2024 | Natural Earth: free vector and raster map data | unknown | no | — |
| [neil2025](abstracts/neil2025.md) | 2025 | 2.4--2.3 {Ga} granitoids of the {Arrowsmith} orogeny, southwestern {Rae} craton, {Canada}: | hybrid | yes | [doi](https://doi.org/10.1016/j.precamres.2025.107880) |
| [nelsen2016](abstracts/nelsen2016.md) | 2016 | Delayed fungal evolution did not cause the Paleozoic peak in coal production | green | yes | [doi](https://doi.org/10.1073/pnas.1517943113) |
| [nesvorny2018](abstracts/nesvorny2018.md) | 2018 | Evidence for very early migration of the Solar System planets from the Patroclus–Menoetius | green | yes | [doi](https://doi.org/10.1038/s41550-018-0564-3) |
| [nichols2024](abstracts/nichols2024.md) | 2024 | Possible Eoarchean Records of the Geomagnetic Field Preserved in the Isua Supracrustal Bel | hybrid | yes | [doi](https://doi.org/10.1029/2023jb027706) |
| [niedzwiedzki2010](abstracts/niedzwiedzki2010.md) | 2010 | Tetrapod trackways from the early Middle Devonian period of Poland | closed | yes | [doi](https://doi.org/10.1038/nature08623) |
| [nishiizumi1991](abstracts/nishiizumi1991.md) | 1991 | In situ10Be-26Al exposure ages at Meteor Crater, Arizona | bronze | no | [doi](https://doi.org/10.1016/0016-7037(91)90388-l) |
| [nowak2019](abstracts/nowak2019.md) | 2019 | No mass extinction for land plants at the Permian–Triassic transition | gold | yes | [doi](https://doi.org/10.1038/s41467-018-07945-w) |
| [nutman2013](abstracts/nutman2013.md) | 2013 | The Itsaq Gneiss Complex of Greenland: Episodic 3900 to 3660 Ma juvenile crust formation a | closed | yes | [doi](https://doi.org/10.2475/09.2013.03) |
| [nutman2016](abstracts/nutman2016.md) | 2016 | Rapid emergence of life shown by discovery of 3,700-million-year-old microbial structures | green | yes | [doi](https://doi.org/10.1038/nature19355) |
| [oberthur2013](abstracts/oberthur2013.md) | 2013 | Detrital platinum-group minerals in rivers draining the {Great Dyke}, {Zimbabwe} | closed | yes | [doi](https://doi.org/10.3749/canmin.51.2.197) |
| [och2012](abstracts/och2012.md) | 2012 | The Neoproterozoic oxygenation event: Environmental perturbations and biogeochemical cycli | closed | no | [doi](https://doi.org/10.1016/j.earscirev.2011.09.004) |
| [odea2016](abstracts/odea2016.md) | 2016 | Formation of the Isthmus of Panama | gold | yes | [doi](https://doi.org/10.1126/sciadv.1600883) |
| [ogg2020](abstracts/ogg2020.md) | 2020 | Geomagnetic Polarity Time Scale | closed | no | [doi](https://doi.org/10.1016/b978-0-12-824360-2.00005-x) |
| [oktaviana2024](abstracts/oktaviana2024.md) | 2024 | Narrative cave art in Indonesia by 51,200 years ago | hybrid | yes | [doi](https://doi.org/10.1038/s41586-024-07541-7) |
| [olierook2023](abstracts/olierook2023.md) | 2023 | Emplacement of the Argyle diamond deposit into an ancient rift zone triggered by supercont | gold | yes | [doi](https://doi.org/10.1038/s41467-023-40904-8) |
| [oneil2008](abstracts/oneil2008.md) | 2008 | Neodymium-142 Evidence for Hadean Mafic Crust | closed | yes | [doi](https://doi.org/10.1126/science.1161925) |
| [opdyke1995](abstracts/opdyke1995.md) | 1995 | Magnetostratigraphy of Permo-Carboniferous Time | closed | yes | [doi](https://doi.org/10.2110/pec.95.04.0041) |
| [page1998](abstracts/page1998.md) | 1998 | Geochronology of basin phases in the western {Mt} {Isa} {Inlier}, and correlation with the | closed | yes | [doi](https://doi.org/10.1080/08120099808728383) |
| [page2005](abstracts/page2005.md) | 2005 | Geochronology of the sequence hosting the {Broken Hill} {Pb-Zn-Ag} orebody, {Australia} | closed | yes | [doi](https://doi.org/10.2113/gsecongeo.100.4.633) |
| [palcu2021](abstracts/palcu2021.md) | 2021 | Late Miocene megalake regressions in Eurasia | gold | yes | [doi](https://doi.org/10.1038/s41598-021-91001-z) |
| [parnell2011](abstracts/parnell2011.md) | 2011 | The age of the Mesoproterozoic Stoer Group sedimentary and impact deposits, NW Scotland | closed | yes | [doi](https://doi.org/10.1144/0016-76492010-099) |
| [partin2023](abstracts/partin2023.md) | 2023 | {Paleoproterozoic} {A}-type postcollisional granitic magmatism associated with the {Arrows | closed | yes | [doi](https://doi.org/10.1086/727647) |
| [paterson2011](abstracts/paterson2011.md) | 2011 | Acute vision in the giant Cambrian predator Anomalocaris and the origin of compound eyes | closed | yes | [doi](https://doi.org/10.1038/nature10689) |
| [pates2022](abstracts/pates2022.md) | 2022 | New opabiniid diversifies the weirdest wonders of the euarthropod stem group | hybrid | yes | [doi](https://doi.org/10.1098/rspb.2021.2093) |
| [pavlov2005](abstracts/pavlov2005.md) | 2005 | A third superchron during the Early Paleozoic | hybrid | yes | [doi](https://doi.org/10.18814/epiiugs/2005/v28i2/001) |
| [pavlov2010](abstracts/pavlov2010.md) | 2010 | Variations in geomagnetic reversal frequency during the Earth's middle age | bronze | yes | [doi](https://doi.org/10.1029/2009gc002583) |
| [pawlowski2003](abstracts/pawlowski2003.md) | 2003 | The evolution of early Foraminifera | green | yes | [doi](https://doi.org/10.1073/pnas.2035132100) |
| [peltonen1996](abstracts/peltonen1996.md) | 1996 | Petrology and Geochemistry of Metabasalts from the 1.95 {Ga} {Jormua} Ophiolite, Northeast | closed | yes | [doi](https://doi.org/10.1093/petrology/37.6.1359) |
| [penalver2012](abstracts/penalver2012.md) | 2012 | Thrips pollination of Mesozoic gymnosperms | green | yes | [doi](https://doi.org/10.1073/pnas.1120499109) |
| [peng2008](abstracts/peng2008.md) | 2008 | A 1.78 {Ga} large igneous province in the {North China} craton: The {Xiong'er Volcanic Pro | closed | no | [doi](https://doi.org/10.1016/j.lithos.2007.07.006) |
| [penny2014](abstracts/penny2014.md) | 2014 | Ediacaran metazoan reefs from the Nama Group, Namibia | green | yes | [doi](https://doi.org/10.1126/science.1253393) |
| [percival2018](abstracts/percival2018.md) | 2018 | Precisely dating the Frasnian–Famennian boundary: implications for the cause of the Late D | gold | yes | [doi](https://doi.org/10.1038/s41598-018-27847-7) |
| [phillips1991](abstracts/phillips1991.md) | 1991 | Age and geomorphic history of Meteor Crater, Arizona, from cosmogenic 36Cl and 14C in rock | closed | no | [doi](https://doi.org/10.1016/0016-7037(91)90387-k) |
| [phillips2000](abstracts/phillips2000.md) | 2000 | {Witwatersrand} gold fields: geology, genesis, and exploration | closed | yes | [doi](https://doi.org/10.5382/rev.13.14) |
| [planavsky2014](abstracts/planavsky2014.md) | 2014 | Evidence for oxygenic photosynthesis half a billion years before the Great Oxidation Event | green | yes | [doi](https://doi.org/10.1038/ngeo2122) |
| [planavsky2014b](abstracts/planavsky2014b.md) | 2014 | Low Mid-Proterozoic atmospheric oxygen levels and the delayed rise of animals | green | yes | [doi](https://doi.org/10.1126/science.1258410) |
| [pol2021](abstracts/pol2021.md) | 2021 | Earliest evidence of herd-living and age segregation amongst dinosaurs | gold | yes | [doi](https://doi.org/10.1038/s41598-021-99176-1) |
| [popova2013](abstracts/popova2013.md) | 2013 | Chelyabinsk Airburst, Damage Assessment, Meteorite Recovery, and Characterization | green | yes | [doi](https://doi.org/10.1126/science.1242642) |
| [portegieszwart2021](abstracts/portegieszwart2021.md) | 2021 | Oort cloud Ecology: II. the chronology of the formation of the Oort cloud | bronze | yes | [doi](https://doi.org/10.1051/0004-6361/202040096) |
| [poulton2004](abstracts/poulton2004.md) | 2004 | The transition to a sulphidic ocean ∼ 1.84 billion years ago | green | yes | [doi](https://doi.org/10.1038/nature02912) |
| [poulton2021](abstracts/poulton2021.md) | 2021 | A 200-million-year delay in permanent atmospheric oxygenation | green | yes | [doi](https://doi.org/10.1038/s41586-021-03393-7) |
| [prasad2005](abstracts/prasad2005.md) | 2005 | Dinosaur Coprolites and the Early Evolution of Grasses and Grazers | closed | yes | [doi](https://doi.org/10.1126/science.1118806) |
| [price1994](abstracts/price1994.md) | 1994 | Mean age of rifting and volcanism on Venus deduced from impact crater densities | closed | yes | [doi](https://doi.org/10.1038/372756a0) |
| [pu2016](abstracts/pu2016.md) | 2016 | Dodging snowballs: Geochronology of the Gaskiers glaciation and the first appearance of th | closed | yes | [doi](https://doi.org/10.1130/g38284.1) |
| [rae2021](abstracts/rae2021.md) | 2021 | Atmospheric CO 2 over the Past 66 Million Years from Marine Archives | closed | yes | [doi](https://doi.org/10.1146/annurev-earth-082420-063026) |
| [ramo2014](abstracts/ramo2014.md) | 2014 | Age and isotopic fingerprints of some plutonic rocks in the {Wiborg} rapakivi granite bath | gold | yes | — |
| [rasmussen2002](abstracts/rasmussen2002.md) | 2002 | 1.6 {Ga} {U-Pb} zircon age for the {Chorhat} {Sandstone}, lower {Vindhyan}, {India}: possi | closed | yes | [doi](https://doi.org/10.1130/0091-7613(2002)030<0103:GUPZAF>2.0.CO;2) |
| [rasmussen2004](abstracts/rasmussen2004.md) | 2004 | Iridium anomalies and shocked quartz in a Late Archean spherule layer from the Pilbara cra | closed | yes | [doi](https://doi.org/10.1130/g20825.1) |
| [rasmussen2005](abstracts/rasmussen2005.md) | 2005 | U-Pb zircon age constraints on the Hamersley spherule beds: Evidence for a single 2.63 Ga  | closed | yes | [doi](https://doi.org/10.1130/g21616.1) |
| [rasmussen2008](abstracts/rasmussen2008.md) | 2008 | Reassessing the first appearance of eukaryotes and cyanobacteria | closed | yes | [doi](https://doi.org/10.1038/nature07381) |
| [rasmussen2024](abstracts/rasmussen2024.md) | 2024 | New {U-Pb} zircon tuff ages and revised stratigraphic correlations in the {Superior} crato | hybrid | yes | [doi](https://doi.org/10.1016/j.epsl.2024.118779) |
| [raup1982](abstracts/raup1982.md) | 1982 | Mass Extinctions in the Marine Fossil Record | closed | yes | [doi](https://doi.org/10.1126/science.215.4539.1501) |
| [reinhard2016](abstracts/reinhard2016.md) | 2016 | Evolution of the global phosphorus cycle | closed | yes | [doi](https://doi.org/10.1038/nature20772) |
| [reis2013](abstracts/reis2013.md) | 2013 | {Avanavero} mafic magmatism, a late {Paleoproterozoic} {LIP} in the {Guiana Shield}, {Amaz | closed | no | [doi](https://doi.org/10.1016/j.lithos.2012.10.014) |
| [reisz2005](abstracts/reisz2005.md) | 2005 | Embryos of an Early Jurassic Prosauropod Dinosaur and Their Evolutionary Significance | closed | yes | [doi](https://doi.org/10.1126/science.1114942) |
| [renne2013](abstracts/renne2013.md) | 2013 | Time Scales of Critical Events Around the {Cretaceous-Paleogene} Boundary | closed | yes | [doi](https://doi.org/10.1126/science.1230492) |
| [requia2003](abstracts/requia2003.md) | 2003 | {Re}--{Os} and {Pb}--{Pb} geochronology of the {Archean} {Salobo} iron oxide copper--gold  | green | yes | [doi](https://doi.org/10.1007/s00126-003-0364-1) |
| [richter2017](abstracts/richter2017.md) | 2017 | The age of the hominin fossils from Jebel Irhoud, Morocco, and the origins of the Middle S | closed | yes | [doi](https://doi.org/10.1038/nature22335) |
| [rivera2014](abstracts/rivera2014.md) | 2014 | Rapid magma evolution constrained by zircon petrochronology and 40Ar/39Ar sanidine ages fo | closed | yes | [doi](https://doi.org/10.1130/g35808.1) |
| [robert2006](abstracts/robert2006.md) | 2006 | A palaeotemperature curve for the Precambrian oceans based on silicon isotopes in cherts | closed | yes | [doi](https://doi.org/10.1038/nature05239) |
| [rogers2018](abstracts/rogers2018.md) | 2018 | Phosphorus and Potassium Metasomatic Enrichment in the Mantle Source of the c. 1450--1425  | closed | yes | [doi](https://doi.org/10.1093/petrology/egy104) |
| [rooney2013](abstracts/rooney2013.md) | 2013 | Re-Os geochronology and coupled Os-Sr isotope constraints on the Sturtian snowball Earth | green | yes | [doi](https://doi.org/10.1073/pnas.1317266110) |
| [rooney2015](abstracts/rooney2015.md) | 2015 | A Cryogenian chronology: Two long-lasting synchronous Neoproterozoic glaciations | closed | yes | [doi](https://doi.org/10.1130/g36511.1) |
| [rooney2020](abstracts/rooney2020.md) | 2020 | Calibrating the coevolution of Ediacaran life and environment | bronze | yes | [doi](https://doi.org/10.1073/pnas.2002918117) |
| [rudkin2008](abstracts/rudkin2008.md) | 2008 | The oldest horseshoe crab: a new xiphosurid from Late Ordovician Konservat-Lagerstätten de | bronze | yes | [doi](https://doi.org/10.1111/j.1475-4983.2007.00746.x) |
| [ruizlara2020](abstracts/ruizlara2020.md) | 2020 | The recurrent impact of the Sagittarius dwarf on the star formation history of the Milky W | green | yes | [doi](https://doi.org/10.1038/s41550-020-1097-0) |
| [rule2019](abstracts/rule2019.md) | 2019 | The pseudofossil {Horodyskia}: Flocs and flakes on microbial mats in a shallow {Mesoproter | closed | yes | [doi](https://doi.org/10.1016/j.precamres.2019.105439) |
| [sager2013](abstracts/sager2013.md) | 2013 | An immense shield volcano within the Shatsky Rise oceanic plateau, northwest Pacific Ocean | closed | yes | [doi](https://doi.org/10.1038/ngeo1934) |
| [sahney2010](abstracts/sahney2010.md) | 2010 | Rainforest collapse triggered Carboniferous tetrapod diversification in Euramerica | closed | yes | [doi](https://doi.org/10.1130/g31182.1) |
| [sallan2017](abstracts/sallan2017.md) | 2017 | The ‘Tully Monster’ is not a vertebrate: characters, convergence and taphonomy in Palaeozo | green | yes | [doi](https://doi.org/10.1111/pala.12282) |
| [scher2006](abstracts/scher2006.md) | 2006 | Timing and Climatic Consequences of the Opening of Drake Passage | closed | yes | [doi](https://doi.org/10.1126/science.1120044) |
| [schersten2013](abstracts/schersten2013.md) | 2013 | Complete hydrothermal re‐equilibration of zircon in the {Maniitsoq} structure, {West} {Gre | bronze | yes | [doi](https://doi.org/10.1111/maps.12169) |
| [schiller2011](abstracts/schiller2011.md) | 2011 | Rapid timescales for magma ocean crystallization on the howardite-eucrite-diogenite parent | bronze | yes | [doi](https://doi.org/10.1088/2041-8205/740/1/l22) |
| [schmidt2012](abstracts/schmidt2012.md) | 2012 | Arthropods in amber from the Triassic Period | green | yes | [doi](https://doi.org/10.1073/pnas.1208464109) |
| [schneider2002](abstracts/schneider2002.md) | 2002 | Age of volcanic rocks and syndepositional iron formations, Marquette Range Supergroup: imp | closed | yes | [doi](https://doi.org/10.1139/e02-016) |
| [schneider2004](abstracts/schneider2004.md) | 2004 | Ferns diversified in the shadow of angiosperms | green | yes | [doi](https://doi.org/10.1038/nature02361) |
| [schoene2009](abstracts/schoene2009.md) | 2009 | Sm–Nd isotopic mapping of lithospheric growth and stabilization in the eastern {Kaapvaal}  | bronze | yes | [doi](https://doi.org/10.1111/j.1365-3121.2009.00877.x) |
| [schoene2019](abstracts/schoene2019.md) | 2019 | U-Pb constraints on pulsed eruption of the Deccan Traps across the end-Cretaceous mass ext | bronze | yes | [doi](https://doi.org/10.1126/science.aau2422) |
| [schoene2021](abstracts/schoene2021.md) | 2021 | An evaluation of Deccan Traps eruption rates using geochronologic data | diamond | yes | [doi](https://doi.org/10.5194/gchron-3-181-2021) |
| [schopf2017](abstracts/schopf2017.md) | 2017 | SIMS analyses of the oldest known assemblage of microfossils document their taxon-correlat | green | yes | [doi](https://doi.org/10.1073/pnas.1718063115) |
| [schultz2008](abstracts/schultz2008.md) | 2008 | Major evolutionary transitions in ant agriculture | green | yes | [doi](https://doi.org/10.1073/pnas.0711024105) |
| [schuster2006](abstracts/schuster2006.md) | 2006 | The Age of the Sahara Desert | closed | yes | [doi](https://doi.org/10.1126/science.1120161) |
| [scoates2008](abstracts/scoates2008.md) | 2008 | PRECISE AGE OF THE PLATINIFEROUS MERENSKY REEF, BUSHVELD COMPLEX, SOUTH AFRICA, BY THE U-P | closed | yes | [doi](https://doi.org/10.2113/gsecongeo.103.3.465) |
| [scott1983](abstracts/scott1983.md) | 1983 | The earliest fossil conifer from the Westphalian B of Yorkshire | closed | yes | [doi](https://doi.org/10.1098/rspb.1983.0094) |
| [scott1992](abstracts/scott1992.md) | 1992 | {Purtuniq} ophiolite, {Cape Smith} belt, northern {Quebec}, {Canada}: A reconstructed sect | closed | yes | [doi](https://doi.org/10.1130/0091-7613(1992)020<0173:POCSBN>2.3.CO;2) |
| [scott2006](abstracts/scott2006.md) | 2006 | The diversification of Paleozoic fire systems and fluctuations in atmospheric oxygen conce | green | yes | [doi](https://doi.org/10.1073/pnas.0604090103) |
| [secord2012](abstracts/secord2012.md) | 2012 | Evolution of the Earliest Horses Driven by Climate Change in the Paleocene-Eocene Thermal  | closed | yes | [doi](https://doi.org/10.1126/science.1213859) |
| [seilacher1998](abstracts/seilacher1998.md) | 1998 | Triploblastic animals more than 1 billion years ago: trace fossil evidence from {India} | closed | yes | [doi](https://doi.org/10.1126/science.282.5386.80) |
| [servais2018](abstracts/servais2018.md) | 2018 | The Great Ordovician Biodiversification Event (GOBE): definition, concept and duration | bronze | yes | [doi](https://doi.org/10.1111/let.12259) |
| [shirey2011](abstracts/shirey2011.md) | 2011 | Start of the {Wilson} {Cycle} at 3 {Ga} {Shown} by {Diamonds} from {Subcontinental} {Mantl | closed | yes | [doi](https://doi.org/10.1126/science.1206275) |
| [shu1999](abstracts/shu1999.md) | 1999 | Lower Cambrian vertebrates from south China | closed | yes | [doi](https://doi.org/10.1038/46965) |
| [shumlyanskyy2017](abstracts/shumlyanskyy2017.md) | 2017 | The origin of the {Palaeoproterozoic} {AMCG} complexes in the {Ukrainian} shield: New {U-P | green | yes | [doi](https://doi.org/10.1016/j.precamres.2017.02.009) |
| [simonson2015](abstracts/simonson2015.md) | 2015 | First detection of extraterrestrial material in ca. 2.49 Ga impact spherule layer in Kurum | closed | yes | [doi](https://doi.org/10.1130/g36225.1) |
| [sims2006](abstracts/sims2006.md) | 2006 | Evolution of the diatoms: insights from fossil, biological and molecular data | green | yes | [doi](https://doi.org/10.2216/05-22.1) |
| [singer2019](abstracts/singer2019.md) | 2019 | Synchronizing volcanic, sedimentary, and ice core records of Earth’s last magnetic polarit | gold | yes | [doi](https://doi.org/10.1126/sciadv.aaw4621) |
| [siveter2014](abstracts/siveter2014.md) | 2014 | Exceptionally Preserved 450-Million-Year-Old Ordovician Ostracods with Brood Care | bronze | yes | [doi](https://doi.org/10.1016/j.cub.2014.02.040) |
| [slack2020](abstracts/slack2020.md) | 2020 | Origin of Tin Mineralization in the {Sullivan} {Pb-Zn-Ag} Deposit, {British Columbia}: Con | closed | yes | [doi](https://doi.org/10.5382/econgeo.4761) |
| [smith2015](abstracts/smith2015.md) | 2015 | Hallucigenia’s head and the pharyngeal armature of early ecdysozoans | green | yes | [doi](https://doi.org/10.1038/nature14573) |
| [smith2016](abstracts/smith2016.md) | 2016 | Large gem diamonds from metallic liquid in Earth’s deep mantle | green | yes | [doi](https://doi.org/10.1126/science.aal1303) |
| [smith2018](abstracts/smith2018.md) | 2018 | Humans thrived in South Africa through the Toba eruption about 74,000 years ago | green | yes | [doi](https://doi.org/10.1038/nature25967) |
| [smith2026](abstracts/smith2026.md) | 2026 | The iron and manganese formations of the {Paleoproterozoic} {Hotazel} Formation in the sou | gold | yes | [doi](https://doi.org/10.1016/j.oregeorev.2025.107060) |
| [smithies2005](abstracts/smithies2005.md) | 2005 | Modern-style subduction processes in the {Mesoarchaean}: {Geochemical} evidence from the 3 | closed | no | [doi](https://doi.org/10.1016/j.epsl.2004.12.026) |
| [smithies2011](abstracts/smithies2011.md) | 2011 | High-Temperature Granite Magmatism, Crust–Mantle Interaction and the Mesoproterozoic Intra | closed | yes | [doi](https://doi.org/10.1093/petrology/egr010) |
| [snyder2021](abstracts/snyder2021.md) | 2021 | Multidisciplinary modeling of mantle lithosphere structure within the {Superior} craton, { | hybrid | yes | [doi](https://doi.org/10.1029/2020gc009566) |
| [som2012](abstracts/som2012.md) | 2012 | Air density 2.7 billion years ago limited to less than twice modern levels by fossil raind | closed | yes | [doi](https://doi.org/10.1038/nature10890) |
| [som2016](abstracts/som2016.md) | 2016 | Earth’s air pressure 2.7 billion years ago constrained to less than half of modern levels | closed | yes | [doi](https://doi.org/10.1038/ngeo2713) |
| [sonett1998](abstracts/sonett1998.md) | 1998 | {Neoproterozoic} {Earth-Moon} dynamics: Rework of the 900 {Ma} {Big Cottonwood Canyon} tid | closed | yes | [doi](https://doi.org/10.1029/98GL00048) |
| [spencer2018](abstracts/spencer2018.md) | 2018 | A {Palaeoproterozoic} tectono-magmatic lull as a potential trigger for the supercontinent  | closed | yes | [doi](https://doi.org/10.1038/s41561-017-0051-y) |
| [srivastava2021](abstracts/srivastava2021.md) | 2021 | A ca. 2.25 {Ga} mafic dyke swarm discovered in the {Bastar} craton, {Central} {India}: Imp | closed | yes | [doi](https://doi.org/10.1016/j.precamres.2021.106232) |
| [stein2007](abstracts/stein2007.md) | 2007 | Giant cladoxylopsid trees resolve the enigma of the Earth’s earliest forest stumps at Gilb | closed | yes | [doi](https://doi.org/10.1038/nature05705) |
| [stein2020](abstracts/stein2020.md) | 2020 | Mid-Devonian Archaeopteris Roots Signal Revolutionary Change in Earliest Fossil Forests | bronze | yes | [doi](https://doi.org/10.1016/j.cub.2019.11.067) |
| [steinthorsdottir2021](abstracts/steinthorsdottir2021.md) | 2021 | The Miocene: The Future of the Past | hybrid | yes | [doi](https://doi.org/10.1029/2020pa004037) |
| [stepanova2015](abstracts/stepanova2015.md) | 2015 | The 2.31 {Ga} mafic dykes in the {Karelian} {Craton}, eastern {Fennoscandian} shield: {U-- | closed | no | [doi](https://doi.org/10.1016/j.precamres.2014.10.002) |
| [stevens2013](abstracts/stevens2013.md) | 2013 | Palaeontological evidence for an Oligocene divergence between Old World monkeys and apes | green | yes | [doi](https://doi.org/10.1038/nature12161) |
| [stoffler2001](abstracts/stoffler2001.md) | 2001 | Stratigraphy and Isotope Ages of Lunar Geologic Units: Chronological Standard for the Inne | closed | yes | [doi](https://doi.org/10.1023/a:1011937020193) |
| [storey2012](abstracts/storey2012.md) | 2012 | Astronomically calibrated 40 Ar/ 39 Ar age for the Toba supereruption and global synchroni | green | yes | [doi](https://doi.org/10.1073/pnas.1208178109) |
| [stouge2021](abstracts/stouge2021.md) | 2021 | Middle Ordovician (Darriwilian) conodonts from southern Tibet, the Indian passive margin:  | green | yes | [doi](https://doi.org/10.1017/s0016756820001077) |
| [strik2003](abstracts/strik2003.md) | 2003 | Palaeomagnetism of flood basalts in the {Pilbara} {Craton}, {Western} {Australia}: late {A | bronze | yes | [doi](https://doi.org/10.1029/2003jb002475) |
| [strom1994](abstracts/strom1994.md) | 1994 | The global resurfacing of Venus | green | yes | [doi](https://doi.org/10.1029/94je00388) |
| [stubbs2021](abstracts/stubbs2021.md) | 2021 | Ecological opportunity and the rise and fall of crocodylomorph evolutionary innovation | hybrid | yes | [doi](https://doi.org/10.1098/rspb.2021.0069) |
| [stueken2015](abstracts/stueken2015.md) | 2015 | Isotopic evidence for biological nitrogen fixation by molybdenum-nitrogenase from 3.2 Gyr | closed | yes | [doi](https://doi.org/10.1038/nature14180) |
| [su2025](abstracts/su2025.md) | 2025 | South Pole–Aitken massive impact 4.25 billion years ago revealed by Chang’e-6 samples | gold | yes | [doi](https://doi.org/10.1093/nsr/nwaf103) |
| [suavet2013](abstracts/suavet2013.md) | 2013 | Persistence and origin of the lunar core dynamo | bronze | yes | [doi](https://doi.org/10.1073/pnas.1300341110) |
| [sumner2004](abstracts/sumner2004.md) | 2004 | Implications for {Neoarchaean} ocean chemistry from primary carbonate mineralogy of the {C | green | yes | [doi](https://doi.org/10.1111/j.1365-3091.2004.00670.x) |
| [sun2002](abstracts/sun2002.md) | 2002 | Archaefructaceae, a New Basal Angiosperm Family | closed | yes | [doi](https://doi.org/10.1126/science.1069439) |
| [swansonhysell2019](abstracts/swansonhysell2019.md) | 2019 | Failed rifting and fast drifting: Midcontinent Rift development, Laurentia’s rapid motion  | green | yes | [doi](https://doi.org/10.1130/b31944.1) |
| [swapp2018](abstracts/swapp2018.md) | 2018 | 2.7 Ga high-pressure granulites of the {Teton} {Range}: record of {Neoarchean} continent c | gold | yes | [doi](https://doi.org/10.1130/ges01607.1) |
| [tang2016](abstracts/tang2016.md) | 2016 | Archean upper crust transition from mafic to felsic marks the onset of plate tectonics | closed | yes | [doi](https://doi.org/10.1126/science.aad5513) |
| [tang2020](abstracts/tang2020.md) | 2020 | A one-billion-year-old multicellular chlorophyte | green | yes | [doi](https://doi.org/10.1038/s41559-020-1122-9) |
| [tapanila2013](abstracts/tapanila2013.md) | 2013 | Jaws for a spiral-tooth whorl: CT images reveal novel adaptation and phylogeny in fossil H | green | yes | [doi](https://doi.org/10.1098/rsbl.2013.0057) |
| [tappe2021](abstracts/tappe2021.md) | 2021 | Sheared Peridotite and Megacryst Formation Beneath the Kaapvaal Craton: a Snapshot of Tect | bronze | yes | [doi](https://doi.org/10.1093/petrology/egab046) |
| [tarduno2010](abstracts/tarduno2010.md) | 2010 | Geodynamo, Solar Wind, and Magnetopause 3.4 to 3.45 Billion Years Ago | closed | yes | [doi](https://doi.org/10.1126/science.1183445) |
| [tarduno2015](abstracts/tarduno2015.md) | 2015 | A Hadean to Paleoarchean geodynamo recorded by single zircon crystals | closed | yes | [doi](https://doi.org/10.1126/science.aaa9114) |
| [tashiro2017](abstracts/tashiro2017.md) | 2017 | Early trace of life from 3.95 Ga sedimentary rocks in Labrador, Canada | closed | yes | [doi](https://doi.org/10.1038/nature24019) |
| [tejada2009](abstracts/tejada2009.md) | 2009 | Ontong Java Plateau eruption as a trigger for the early Aptian oceanic anoxic event | closed | yes | [doi](https://doi.org/10.1130/g25763a.1) |
| [thewissen2001](abstracts/thewissen2001.md) | 2001 | Skeletons of terrestrial cetaceans and the relationship of whales to artiodactyls | closed | yes | [doi](https://doi.org/10.1038/35095005) |
| [thomson2011](abstracts/thomson2011.md) | 2011 | Constraints on the origin and evolution of the layered mound in {Gale} {Crater}, {Mars} us | closed | no | [doi](https://doi.org/10.1016/j.icarus.2011.05.002) |
| [tice2004](abstracts/tice2004.md) | 2004 | Photosynthetic microbial mats in the 3,416-Myr-old ocean | closed | yes | [doi](https://doi.org/10.1038/nature02888) |
| [tice2006](abstracts/tice2006.md) | 2006 | Hydrogen-based carbon fixation in the earliest known photosynthetic organisms | closed | yes | [doi](https://doi.org/10.1130/G22012.1) |
| [tinkler1994](abstracts/tinkler1994.md) | 1994 | Postglacial Recession of Niagara Falls in Relation to the Great Lakes | closed | yes | [doi](https://doi.org/10.1006/qres.1994.1050) |
| [torsvik2009](abstracts/torsvik2009.md) | 2009 | A new scheme for the opening of the South Atlantic Ocean and the dissection of an Aptian s | bronze | yes | [doi](https://doi.org/10.1111/j.1365-246x.2009.04137.x) |
| [trendall1998](abstracts/trendall1998.md) | 1998 | Precise zircon {U}--{Pb} ages from the {Marra Mamba Iron Formation} and {Wittenoom Formati | closed | yes | [doi](https://doi.org/10.1080/08120099808728374) |
| [turgeon2008](abstracts/turgeon2008.md) | 2008 | Cretaceous oceanic anoxic event 2 triggered by a massive magmatic episode | closed | yes | [doi](https://doi.org/10.1038/nature07076) |
| [turner2021](abstracts/turner2021.md) | 2021 | Possible poriferan body fossils in early {Neoproterozoic} microbial reefs | hybrid | yes | [doi](https://doi.org/10.1038/s41586-021-03773-z) |
| [ueno2006](abstracts/ueno2006.md) | 2006 | Evidence from fluid inclusions for microbial methanogenesis in the early Archaean era | closed | yes | [doi](https://doi.org/10.1038/nature04584) |
| [vandenbergh2016](abstracts/vandenbergh2016.md) | 2016 | Homo floresiensis-like fossils from the early Middle Pleistocene of Flores | closed | yes | [doi](https://doi.org/10.1038/nature17999) |
| [vandenburg2026](abstracts/vandenburg2026.md) | 2026 | Modern arc-like water content in the source of 3.1-billion-year-old volcanic rocks | gold | yes | [doi](https://doi.org/10.1038/s41467-026-74653-1) |
| [vankranendonk2007](abstracts/vankranendonk2007.md) | 2007 | Review: secular tectonic evolution of {Archean} continental crust: interplay between horiz | bronze | yes | [doi](https://doi.org/10.1111/j.1365-3121.2006.00723.x) |
| [vartanyan1993](abstracts/vartanyan1993.md) | 1993 | Holocene dwarf mammoths from Wrangel Island in the Siberian Arctic | closed | yes | [doi](https://doi.org/10.1038/362337a0) |
| [voss2019](abstracts/voss2019.md) | 2019 | Stomach contents of the archaeocete Basilosaurus isis: Apex predator in oceans of the late | gold | yes | [doi](https://doi.org/10.1371/journal.pone.0209021) |
| [wallner2016](abstracts/wallner2016.md) | 2016 | Recent near-Earth supernovae probed by global deposition of interstellar radioactive 60Fe | green | yes | [doi](https://doi.org/10.1038/nature17196) |
| [walter1994](abstracts/walter1994.md) | 1994 | Age of Lucy and the First Family: Single-crystal 40Ar/39Ar dating of the Denen Dora and lo | closed | yes | [doi](https://doi.org/10.1130/0091-7613(1994)022<0006:aolatf>2.3.co;2) |
| [wan2012](abstracts/wan2012.md) | 2012 | Multiple 3.8--3.1 Ga tectono-magmatic events in a newly discovered area of ancient rocks ( | closed | no | [doi](https://doi.org/10.1016/j.jseaes.2012.03.007) |
| [wang2017](abstracts/wang2017.md) | 2017 | Lifetime of the solar nebula constrained by meteorite paleomagnetism | hybrid | yes | [doi](https://doi.org/10.1126/science.aaf5043) |
| [waterton2020](abstracts/waterton2020.md) | 2020 | Geodynamic {Implications} of {Synchronous} {Norite} and {TTG} {Formation} in the 3 Ga {Man | gold | yes | [doi](https://doi.org/10.3389/feart.2020.562062) |
| [wellman2003](abstracts/wellman2003.md) | 2003 | Fragments of the earliest land plants | green | yes | [doi](https://doi.org/10.1038/nature01884) |
| [westall2015](abstracts/westall2015.md) | 2015 | Archean (3.33 Ga) microbe-sediment systems were diverse and flourished in a hydrothermal c | green | yes | [doi](https://doi.org/10.1130/G36646.1) |
| [westerhold2020](abstracts/westerhold2020.md) | 2020 | An astronomically dated record of Earth’s climate and its predictability over the last 66  | green | yes | [doi](https://doi.org/10.1126/science.aba6853) |
| [whitehouse2019](abstracts/whitehouse2019.md) | 2019 | On the true antiquity of Eoarchean chemofossils: assessing the claim for Earth's oldest bi | green | yes | [doi](https://doi.org/10.1016/j.precamres.2019.01.001) |
| [wiemer2018](abstracts/wiemer2018.md) | 2018 | Earth's oldest stable crust in the Pilbara Craton formed by cyclic gravitational overturns | closed | yes | [doi](https://doi.org/10.1038/s41561-018-0105-9) |
| [wilde2001](abstracts/wilde2001.md) | 2001 | Evidence from Detrital Zircons for the Existence of Continental Crust and Oceans on the Ea | closed | yes | [doi](https://doi.org/10.1038/35051550) |
| [williams2000](abstracts/williams2000.md) | 2000 | Geological Constraints on the {Precambrian} History of {Earth's} Rotation and the {Moon's} | closed | yes | [doi](https://doi.org/10.1029/1999RG900016) |
| [wilsonmantilla2021](abstracts/wilsonmantilla2021.md) | 2021 | Earliest Palaeocene purgatoriids and the initial radiation of stem primates | gold | yes | [doi](https://doi.org/10.1098/rsos.210050) |
| [wingate1998](abstracts/wingate1998.md) | 1998 | Ion microprobe {U--Pb} ages for {Neoproterozoic} basaltic magmatism in south-central {Aust | closed | no | [doi](https://doi.org/10.1016/S0301-9268(97)00072-7) |
| [wingate2000](abstracts/wingate2000.md) | 2000 | Ion microprobe {U}--{Pb} zircon and baddeleyite ages for the {Great Dyke} and its satellit | closed | yes | [doi](https://doi.org/10.2113/103.1.74) |
| [xing2014](abstracts/xing2014.md) | 2014 | Diversity in early crustal evolution: 4100 Ma zircons in the Cathaysia Block of southern C | gold | yes | [doi](https://doi.org/10.1038/srep05143) |
| [yakymchuk2021](abstracts/yakymchuk2021.md) | 2021 | Stirred not shaken; critical evaluation of a proposed {Archean} meteorite impact in {West} | hybrid | yes | [doi](https://doi.org/10.1016/j.epsl.2020.116730) |
| [yan2025](abstracts/yan2025.md) | 2025 | An expansive global oxygenation of {Earth}'s surface environments 1.4 billion years ago | gold | yes | [doi](https://doi.org/10.1038/s41467-025-65551-z) |
| [yang2018](abstracts/yang2018.md) | 2018 | Geochronological constraint on the Cambrian Chengjiang biota, South China | green | yes | [doi](https://doi.org/10.1144/jgs2017-103) |
| [yin2002](abstracts/yin2002.md) | 2002 | A short timescale for terrestrial planet formation from Hf–W chronometry of meteorites | closed | yes | [doi](https://doi.org/10.1038/nature00995) |
| [young1998](abstracts/young1998.md) | 1998 | Earth's oldest reported glaciation: physical and chemical evidence from the {Archean} {Moz | closed | yes | [doi](https://doi.org/10.1086/516039) |
| [young2013](abstracts/young2013.md) | 2013 | Evolution of Earth’s climatic system: Evidence from ice ages, isotopes, and impacts | closed | no | [doi](https://doi.org/10.1130/gsatg183a.1) |
| [yue2020](abstracts/yue2020.md) | 2020 | Refined model age for Orientale Basin derived from zonal crater dating of its ejecta | closed | yes | [doi](https://doi.org/10.1016/j.icarus.2020.113804) |
| [zachos2001](abstracts/zachos2001.md) | 2001 | Trends, Rhythms, and Aberrations in Global Climate 65 Ma to Present | closed | yes | [doi](https://doi.org/10.1126/science.1059412) |
| [zahnle2003](abstracts/zahnle2003.md) | 2003 | Cratering rates in the outer Solar System | closed | no | [doi](https://doi.org/10.1016/s0019-1035(03)00048-4) |
| [zegers1998](abstracts/zegers1998.md) | 1998 | Vaalbara, Earth’s oldest assembled continent? A combined structural, geochronological, and | closed | yes | [doi](https://doi.org/10.1046/j.1365-3121.1998.00199.x) |
| [zeh2011](abstracts/zeh2011.md) | 2011 | Hafnium isotope record of the Ancient Gneiss Complex, Swaziland, southern Africa: evidence | closed | yes | [doi](https://doi.org/10.1144/0016-76492010-117) |
| [zerkle2012](abstracts/zerkle2012.md) | 2012 | A bistable organic-rich atmosphere on the Neoarchaean Earth | green | yes | [doi](https://doi.org/10.1038/ngeo1425) |
| [zhang2014](abstracts/zhang2014.md) | 2014 | Aridification of the Sahara desert caused by Tethys Sea shrinkage during the Late Miocene | closed | yes | [doi](https://doi.org/10.1038/nature13705) |
| [zhang2018](abstracts/zhang2018.md) | 2018 | Oxygenation of the {Mesoproterozoic} ocean and the evolution of complex eukaryotes | green | yes | [doi](https://doi.org/10.1038/s41561-018-0111-y) |
| [zhang2023](abstracts/zhang2023.md) | 2023 | Reworking of Eoarchean to Mesoarchean Continental Crust in the Anshan--Benxi Area, North C | gold | yes | [doi](https://doi.org/10.3390/min14010005) |
| [zhao2002](abstracts/zhao2002.md) | 2002 | Review of global 2.1–1.8 Ga orogens: implications for a pre-Rodinia supercontinent | closed | no | [doi](https://doi.org/10.1016/s0012-8252(02)00073-9) |
| [zhao2004](abstracts/zhao2004.md) | 2004 | A Paleo-Mesoproterozoic supercontinent: assembly, growth and breakup | closed | no | [doi](https://doi.org/10.1016/j.earscirev.2004.02.003) |
| [zhou2003](abstracts/zhou2003.md) | 2003 | The missing link in Ginkgo evolution | closed | yes | [doi](https://doi.org/10.1038/423821a) |
| [zhu2012](abstracts/zhu2012.md) | 2012 | Earliest known coelacanth skull extends the range of anatomically modern coelacanths to th | bronze | yes | [doi](https://doi.org/10.1038/ncomms1764) |
| [zhu2013](abstracts/zhu2013.md) | 2013 | A Silurian placoderm with osteichthyan-like marginal jaw bones | closed | yes | [doi](https://doi.org/10.1038/nature12617) |
| [zhu2016](abstracts/zhu2016.md) | 2016 | Decimetre-scale multicellular eukaryotes from the 1.56-billion-year-old {Gaoyuzhuang} {For | gold | yes | [doi](https://doi.org/10.1038/ncomms11500) |
| [zhu2022](abstracts/zhu2022.md) | 2022 | The oldest complete jawed vertebrates from the early Silurian of China | closed | yes | [doi](https://doi.org/10.1038/s41586-022-05136-8) |
| [zhuravlev2026](abstracts/zhuravlev2026.md) | 2026 | On the origin of metazoan reefs | hybrid | yes | [doi](https://doi.org/10.1098/rspb.2025.2760) |
| [zucker2022](abstracts/zucker2022.md) | 2022 | Star formation near the Sun is driven by expansion of the Local Bubble | green | yes | [doi](https://doi.org/10.1038/s41586-021-04286-5) |
