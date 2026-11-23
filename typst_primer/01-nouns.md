# 1. Nouns: the things Typst is made of

## Three syntactic modes
A `.typ` file starts in **markup mode**. You switch modes with a character:

| Mode | Enter with | Example | Use |
|---|---|---|---|
| Markup | default; `[ ... ]` from code | `*bold* _emph_ = Heading` | prose |
| Code | `#` from markup; `{ ... }` block | `#let x = 3` / `#x` | logic, calls |
| Math | `$ ... $` | `$E = m c^2$` | equations |

`#` is the bridge: in markup, `#expr` evaluates one expression and inserts the result.
Inside a code block `{ }` you don't need `#`.
→ https://typst.app/docs/reference/syntax/

## Content
The central type. Everything that ends up on the page is **content**: text, headings,
boxes, images. A `[...]` block is a content literal. Content values can be stored in
variables, passed to functions, joined (`a + b`, `.join()`), and returned.
`[Hello #name]` is content; `"Hello"` is a **string**. Strings become content when inserted.
→ https://typst.app/docs/reference/foundations/content/

## Values and types
`int`, `float`, `str`, `bool`, `none`, `auto`, `array` `(1, 2, 3)`, `dictionary` `(a: 1, b: 2)`,
`length` (`3mm`, `12pt`, `1em`), `ratio` (`50%`), `relative` (`50% + 2mm`), `fraction` (`1fr`),
`angle`, `color` (`rgb("#336")`, `luma(90)`), `alignment` (`top + left`), `function`, `content`.
Arrays/dictionaries are immutable values (copied on modification), so there's no aliasing.
→ https://typst.app/docs/reference/foundations/

## Units (lengths)
`pt`, `mm`, `cm`, `in`, `em` (relative to current font size). Multiply a number by a unit
to make a length: `P.width_mm * 1mm`. This is how this project turns JSON numbers into
positions. You cannot add a bare number to a length.
→ https://typst.app/docs/reference/layout/length/

## Functions
Called with `name(positional, named: value)`. A trailing `[content]` block is sugar for
the last positional argument: `text(fill: red)[hi]` == `text(fill: red, [hi])`.
Define your own with `#let f(x, y: 2) = ...`. Closures: `x => x * 2`.
→ https://typst.app/docs/reference/foundations/function/

## Elements
Built-in functions that produce styled, introspectable content: `heading`, `par`,
`text`, `page`, `block`, `box`, `figure`, `image`, `cite`, `bibliography`, `table`, `grid`…
They have **fields** (`heading.level`), can be targeted by **set** and **show** rules,
and can be found later by `query`.
→ https://typst.app/docs/reference/model/  ·  https://typst.app/docs/reference/layout/

## Block vs inline
`block` (and headings, paragraphs) break lines / stack vertically.
`box` is inline: it sits in a line of text (used in book.typ for the grey date).
`place` takes content *out of flow* and positions it absolutely (relative to its container).

## Rules
- **set rule**: default arguments for an element from here to the end of the scope.
- **show rule**: transform how an element (or matched text / label) is displayed.
Covered in 02-verbs.md. → https://typst.app/docs/reference/styling/

## Labels and references
`<name>` attaches a label to the preceding element; `@name` refers to it (or cites a bib key).
`label("x")` builds one from a string, as book.typ does for citation keys.
→ https://typst.app/docs/reference/model/ref/

## Context
Some facts are only known during layout: the current page number, the current font size,
what headings came before. Reading them requires a `context` expression, which Typst
re-evaluates until layout converges. `context here().page()` is the physical page number.
→ https://typst.app/docs/reference/context/

## Scopes and modules
Every `{}` / `[]` block is a scope: `let` and `set` inside it end at the closing brace.
A file is a **module**; `#import "x.typ": f` brings in names. **Packages** are versioned
modules from Typst Universe: `#import "@preview/cetz:0.3.4"`.

## Project root
The folder that absolute paths like `"/build/book.json"` resolve against, set with
`--root` (CLI) or `root=` (Python). Files outside the root are inaccessible on purpose.
This repo uses the repo root.
