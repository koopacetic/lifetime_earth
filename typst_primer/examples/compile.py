"""Compile every examples/*.typ to examples/out/<name>-<page>.png (and .pdf)."""
import pathlib, sys, typst

here = pathlib.Path(__file__).resolve().parent
out = here / "out"
out.mkdir(exist_ok=True)
targets = sys.argv[1:] or sorted(p.name for p in here.glob("*.typ"))
for name in targets:
    src = here / name
    stem = src.stem
    try:
        typst.compile(str(src), output=str(out / f"{stem}.pdf"), root=str(here))
        pngs = typst.compile(str(src), format="png", ppi=144, root=str(here))
        pngs = pngs if isinstance(pngs, list) else [pngs]
        for i, b in enumerate(pngs, 1):
            (out / f"{stem}-{i}.png").write_bytes(b)
        print(f"ok   {name}: {len(pngs)} page(s)")
    except Exception as e:
        print(f"FAIL {name}: {e}")
