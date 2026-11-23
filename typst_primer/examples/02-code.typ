// Code mode: let, functions, arrays, dictionaries, loops. `#` enters code from markup.
#set page(width: 120mm, height: auto, margin: 8mm)
#let name = "Earth"
#let age-myr = 4570
#let eras = (
  (name: "Hadean", start: -4567),
  (name: "Archean", start: -4031),
  (name: "Proterozoic", start: -2500),
  (name: "Phanerozoic", start: -539),
)
#let label-era(e) = [*#e.name* from #calc.abs(e.start) Ma]

The #name is #age-myr Myr old. That is #(age-myr / 5) five-Myr pages... roughly.

// A for loop *produces* content; results are joined.
#for e in eras [- #label-era(e)\ ]

// Code blocks return their last value(s), joined:
#{
  let n = eras.len()
  [There are #n eons. ]
  if n > 3 { [More than three.] } else { [Three or fewer.] }
}

// Inspect a value's type and representation while debugging:
#type(eras.at(0)) / #repr(eras.at(0))
