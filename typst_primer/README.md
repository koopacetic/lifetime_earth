# Typst primer (for the Lifetime of the Earth project)

Typst is a markup-based typesetting system: a successor in spirit to LaTeX, with a real
scripting language built in, incremental compilation, and readable error messages.
One `.typ` file plus fonts/images/data in, one PDF (or PNG/SVG/HTML) out.

Read in order:

| File | What it covers |
|---|---|
| [01-nouns.md](01-nouns.md) | The things: modes, content, values, functions, elements, rules, context, units |
| [02-verbs.md](02-verbs.md) | The actions: `#let` `#set` `#show` `#import` `#place` `context`… and the CLI verbs |
| [03-functionality.md](03-functionality.md) | What it can do: layout, data loading, bibliography, introspection, math, packages |
| [04-workflow.md](04-workflow.md) | How you work with it, generically and in this repo (`build.py` → `book.typ`) |
| [05-book-typ-tour.md](05-book-typ-tour.md) | Annotated walk through `typeset/book.typ` |
| [06-links.md](06-links.md) | Further reading, grouped |
| [examples/](examples/) | Small runnable `.typ` files, one idea each |

Run the examples (uses the project's venv, which has the `typst` Python package):

```bash
# from the repo root
.venv/bin/python typst_primer/examples/compile.py
# -> typst_primer/examples/out/*.png
```

Or install the CLI (`cargo install typst-cli`, `brew install typst`, or a release binary from
GitHub) and run `typst watch examples/01-markup.typ`.
