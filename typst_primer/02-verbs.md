# 2. Verbs: what you do in Typst

## Language verbs (keywords and core functions)

| Verb | Shape | Meaning |
|---|---|---|
| `let` | `#let x = 1`, `#let f(a) = ...` | bind a variable or define a function |
| `set` | `#set text(size: 9pt)` | change element defaults for the rest of the scope |
| `set ... if` | `#set par(justify: true) if wide` | conditional set |
| `show` | `#show heading: it => ...` | restyle / replace an element everywhere it appears |
| `show: f` | `#show: template` | wrap *the whole rest of the document* in `f` (templates) |
| `show X: set ...` | `#show heading: set text(red)` | scoped set rule just for X's contents |
| `import` | `#import "lib.typ": f, g` | load names from a module or package |
| `include` | `#include "chapter.typ"` | insert another file's content here |
| `if / else` | `if recto { a } else { b }` | conditionals (an expression; returns a value) |
| `for` | `for p in pages [ ... ]` | loop; the bodies' results are **joined** |
| `while`, `break`, `continue`, `return` | | as expected |
| `context` | `context here().page()` | read layout-time state |
| `place` | `place(top + left, dx:, dy:, body)` | absolute positioning, out of flow |
| `v` / `h` | `v(1mm)`, `h(0.3em)` | vertical / horizontal space |
| `query` | `query(<unit-start>)` | find labelled elements / elements of a type anywhere |
| `json` / `csv` / `yaml` / `toml` / `read` | `json("/build/book.json")` | load data files |
| `.map / .filter / .join / .enumerate` | `keys.map(k => cite(label(k))).join()` | array methods |

Key insight on `for`: loop bodies return content, and the results are concatenated.
`#for p in D.pages { page(...) }` *produces* the pages; there's no print/append.

### set vs show, in one line
`set` = "change this element's parameters". `show` = "change what this element turns into".
→ https://typst.app/docs/reference/styling/  ·  https://typst.app/docs/tutorial/advanced-styling/

## CLI verbs (`typst <verb>`)

| Command | Does |
|---|---|
| `typst compile in.typ [out.pdf]` | one-shot build. `--format png --ppi 150`, `--root DIR`, `--input key=val`, `--pages 3-5` |
| `typst watch in.typ` | rebuild on save (incremental, fast). Pair with a PDF viewer that auto-reloads |
| `typst query in.typ "<label>"` | dump introspected elements/metadata as JSON (`--field value`) |
| `typst fonts` | list fonts Typst can see (`--font-path DIR` to add) |
| `typst init @preview/template` | start a project from a Universe template |
| `typst update` | self-update the CLI |

→ https://github.com/typst/typst#usage

## Python verbs (what this repo uses)
```python
import typst
typst.compile("typeset/book.typ", output="build/book.pdf", root=".")
pngs = typst.compile(src, root=".", format="png", ppi=150)   # list of bytes, one per page
typst.query(src, "<unit-start>", field="value", root=".")     # like `typst query`, returns JSON text
pdf, warnings = typst.compile_with_warnings(src, root=".")      # surfaces e.g. "unknown font family"
```
`sys_inputs={"k": "v"}` corresponds to `--input`, read in Typst via `sys.inputs.k`.
→ https://pypi.org/project/typst/  ·  https://github.com/messense/typst-py
