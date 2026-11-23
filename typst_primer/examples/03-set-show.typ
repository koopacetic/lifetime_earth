// set = change defaults; show = change what an element becomes.
#set page(width: 120mm, height: auto, margin: 8mm)
#set text(size: 10pt)
#set par(justify: true)

#show heading: it => block(fill: luma(230), inset: 4pt, width: 100%, smallcaps(it.body))
#show "Earth": strong     // show rule on matching text
#show emph: set text(fill: blue)

= Before

The Earth formed about 4.57 billion years ago, _give or take_.

// Rules are scoped: this block gets bigger text, then it ends.
#[
  #set text(size: 14pt)
  Larger inside the scope.
]

Back to normal size.
