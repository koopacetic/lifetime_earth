#!/usr/bin/env python3
"""Validate all data. Exit 1 on errors. Run after every data change.

    tools/check.py            # errors + warnings summary
    tools/check.py --quiet    # errors only
"""
import argparse
import os
import re
import sys

import jsonschema

sys.path.insert(0, os.path.dirname(__file__))
import common as C  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    cfg = C.config()
    errors, warnings = [], []
    schema = C.load_json(C.DATA / "schema.json")
    keys = C.bib_keys()
    tags = C.load_tags()
    lo, hi = cfg["time"]["start_year"], cfg["time"]["end_year"]

    seen: dict[str, str] = {}
    for path in C.event_files():
        data = C.load_json(path)
        v = jsonschema.Draft202012Validator(schema)
        for err in v.iter_errors(data):
            loc = "/".join(str(x) for x in err.absolute_path)
            errors.append(f"{path.name}:{loc}: {err.message}")
        if not isinstance(data, list):
            continue
        prev_t = None
        for ev in data:
            if not isinstance(ev, dict) or "id" not in ev:
                continue
            i = ev["id"]
            if i in seen:
                errors.append(f"{path.name}: duplicate id '{i}' (also in {seen[i]})")
            seen[i] = path.name
            t = ev.get("t")
            if isinstance(t, int) and not (lo <= t <= hi):
                errors.append(f"{i}: t={t} outside book range")
            if prev_t is not None and isinstance(t, int) and t < prev_t:
                warnings.append(f"{path.name}: not sorted by t at '{i}' (run tools/add.py --fmt)")
            prev_t = t if isinstance(t, int) else prev_t
            srcs = list(ev.get("sources", [])) + list(ev.get("art", {}).get("sources", []))
            for s in srcs:
                if s not in keys:
                    errors.append(f"{i}: source key '{s}' not in sources.bib")
            for tg in ev.get("tags", []):
                if tg not in tags:
                    errors.append(f"{i}: tag '{tg}' not in data/tags.json (reuse an existing tag or add it there)")
            if "art" in ev and not (C.ROOT / "art" / ev["art"]["file"]).exists():
                errors.append(f"{i}: art file missing: art/{ev['art']['file']}")
            if "span" in ev and isinstance(t, int):
                s, e = sorted(ev["span"])
                if not (s <= t <= e):
                    errors.append(f"{i}: t must lie inside span")
            if "mention" in ev and "span" not in ev:
                errors.append(f"{i}: 'mention' requires 'span'")
            if not ev.get("verified"):
                warnings.append(f"{i}: unverified")

    ts = C.load_timescale()
    for s in ts.get("sources", []):
        if s not in keys:
            errors.append(f"timescale.json: source '{s}' not in sources.bib")
    for ser in C.load_series():
        srcs = list(ser.get("sources", [])) + [s for p in ser["points"] for s in p["sources"]]
        if not srcs:
            errors.append(f"series {ser['id']}: no sources")
        if ser.get("slot", "sky") not in C.FOOTER_SLOTS:
            errors.append(f"series {ser['id']}: slot must be one of {', '.join(C.FOOTER_SLOTS)}")
        if ser.get("model"):
            from models import MODELS
            if ser["model"] not in MODELS:
                errors.append(f"series {ser['id']}: unknown model '{ser['model']}'")
        for s in srcs:
            if s not in keys:
                errors.append(f"series {ser['id']}: source '{s}' not in sources.bib")
    for tg, d in tags.items():
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", tg) or not isinstance(d, str) or not d:
            errors.append(f"tags.json: '{tg}' needs a kebab-case name and a description")
    fe = C.load_foredge()
    for s in fe.get("sources", []):
        if s not in keys:
            errors.append(f"foredge.json: source '{s}' not in sources.bib")
    for b in fe["bands"]:
        if not 0 <= b["slot"] < fe["slots"]:
            errors.append(f"foredge band {b['name']}: slot out of range")
        lab = b.get("label", [])
        if not isinstance(lab, list) or not all(isinstance(x, str) and x for x in lab):
            errors.append(f"foredge band {b['name']}: label must be a list of non-empty strings")
    if len({b["slot"] for b in fe["bands"]}) != len(fe["bands"]):
        errors.append("foredge.json: two bands share a slot")
    for b0, b1 in zip(fe["bands"], fe["bands"][1:]):
        if b0["end"] != b1["start"]:
            errors.append(f"foredge.json: gap or overlap between {b0['name']} and {b1['name']}")
    # Back-matter explainer of unit names: every row names a timescale unit; every cited key exists.
    tsn_path = C.DATA / "explainers" / "timescale-names.json"
    if tsn_path.exists():
        tsn = C.load_timescale_names()
        ts = C.load_timescale()
        unit_names = {u["name"] for lvl in ("eons", "eras") for u in ts[lvl]}
        for part in tsn.get("paragraphs", []) + tsn.get("rows", []):
            if "unit" in part and part["unit"] not in unit_names:
                errors.append(f"timescale-names.json: unknown unit '{part['unit']}'")
            for s in part.get("sources", []):
                if s not in keys:
                    errors.append(f"timescale-names.json: source '{s}' not in sources.bib")
    # Image credits (decision #40): every art file needs a credits.json record whose credit ids resolve.
    credits = C.load_credits()
    for ev in C.load_events():
        if "art" not in ev:
            continue
        slug = C.art_slug(ev["art"]["file"])
        im = credits["by_slug"].get(slug)
        if im is None:
            errors.append(f"{ev['id']}: art '{ev['art']['file']}' has no record in art/credits.json")
            continue
        for cid in im.get("credits", [slug]):
            if cid not in credits["entries"]:
                errors.append(f"art credit {slug}: credit id '{cid}' not in art/credits.json")
        for s in ev["art"]["sources"]:
            if s.startswith("phylopic-"):
                errors.append(f"{ev['id']}: image credit '{s}' belongs in art/credits.json, not art.sources")

    for e in errors:
        print("ERROR", e)
    if not a.quiet:
        unver = sum(1 for w in warnings if w.endswith("unverified"))
        for w in warnings:
            if not w.endswith("unverified"):
                print("WARN ", w)
        print(f"{len(seen)} events, {len(keys)} sources, {unver} unverified, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
