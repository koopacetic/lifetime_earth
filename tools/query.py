#!/usr/bin/env python3
"""Look up existing data compactly, so you never need to read the JSON files.

    tools/query.py --page 901                 # entries printed on content page 901
    tools/query.py --from -70000000 --to -60000000
    tools/query.py --grep oxygen              # title/text/id substring (case-insensitive)
    tools/query.py --page-of -66043000        # which content page holds a year
    tools/query.py --id chicxulub-impact --full
    tools/query.py --sources                  # list bib keys with usage counts
    tools/query.py --tags                     # master tag list with usage counts
    tools/query.py --tag impact               # events with a tag (combine with other filters)

One line per event:  page | t ± err | id | title | sources | tags | file
"""
import argparse
import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(__file__))
import common as C  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--page", type=str, help="content page(s), e.g. 901 or 900-905")
    ap.add_argument("--from", dest="t0", type=int)
    ap.add_argument("--to", dest="t1", type=int)
    ap.add_argument("--grep")
    ap.add_argument("--id")
    ap.add_argument("--page-of", type=int)
    ap.add_argument("--sources", action="store_true")
    ap.add_argument("--tags", action="store_true", help="list master tags with usage counts")
    ap.add_argument("--tag", help="only events carrying this tag")
    ap.add_argument("--full", action="store_true", help="print full JSON of matches")
    a = ap.parse_args()
    cfg = C.config()

    if a.page_of is not None:
        n = C.page_of(a.page_of, cfg)
        top, bot = C.page_bounds(n, cfg)
        print(f"page {n}: {C.fmt_year(top)} to {C.fmt_year(bot)} "
              f"(at {C.frac_in_page(a.page_of, n, cfg):.0%} down the page)")
        return

    evs = C.load_events()
    if a.sources:
        used = Counter(s for e in evs for s in e["sources"] + e.get("art", {}).get("sources", []))
        for k in sorted(C.bib_keys()):
            print(f"{used.get(k, 0):4d}  {k}")
        return

    if a.tags:
        used = Counter(t for e in evs for t in e.get("tags", []))
        for k, d in C.load_tags().items():
            print(f"{used.get(k, 0):4d}  {k:<14} {d}")
        unknown = set(used) - set(C.load_tags())
        if unknown:
            print("not in tags.json:", ", ".join(sorted(unknown)))
        return

    if a.tag:
        evs = [e for e in evs if a.tag in e.get("tags", [])]
    if a.page:
        pages = set(C.parse_ranges(a.page, C.n_pages(cfg)))
        evs = [e for e in evs if C.page_of(e["t"], cfg) in pages
               or any(C.page_of(t, cfg) in pages for t in e.get("span", []))]
    if a.t0 is not None:
        evs = [e for e in evs if e["t"] >= a.t0]
    if a.t1 is not None:
        evs = [e for e in evs if e["t"] <= a.t1]
    if a.grep:
        g = a.grep.lower()
        evs = [e for e in evs if g in (e["id"] + " " + e["title"] + " " + e["text"]).lower()]
    if a.id:
        evs = [e for e in evs if e["id"] == a.id]

    for e in evs:
        if a.full:
            print(json.dumps(e, ensure_ascii=False, indent=2))
        else:
            print(f"p{C.page_of(e['t'], cfg):<4}| {C.fmt_when(e):<30}| {e['id']} | {e['title']} | "
                  f"{','.join(e['sources'])} | {','.join(e.get('tags', []))} | {e['_file']}")
    print(f"({len(evs)} events)", file=sys.stderr)


if __name__ == "__main__":
    main()
