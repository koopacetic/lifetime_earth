#!/usr/bin/env python3
"""Add events from JSON (stdin or file) into an event file, then sort, format and validate.

    tools/add.py data/events/demo.json < new_events.json   # a JSON object or array of objects
    tools/add.py data/events/demo.json --from new.json
    tools/add.py --fmt                                      # just re-sort/format all event files

Refuses: duplicate ids (anywhere), and near-duplicates (close in time and sharing title words)
unless --force. Never hand-edit formatting; let this tool own it so diffs stay clean.
"""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
import common as C  # noqa: E402

KEY_ORDER = ["id", "t", "t_err", "span", "mention", "title", "text", "sources",
             "tags", "importance", "art", "verified", "notes"]


def canonical(ev: dict) -> dict:
    out = {k: ev[k] for k in KEY_ORDER if k in ev}
    out.update({k: v for k, v in ev.items() if k not in out and not k.startswith("_")})
    return out


def dumps(events: list[dict]) -> str:
    """indent=2, but arrays of scalars stay on one line (compact, grep-friendly)."""
    s = json.dumps(events, ensure_ascii=False, indent=2)
    return re.sub(r"\[\s*((?:[^\[\]{}\s][^\[\]{}]*?))\s*\]",
                  lambda m: "[" + re.sub(r",\s+", ", ", m.group(1)) + "]", s)


def write(path: Path, events: list[dict]):
    events = sorted((canonical(e) for e in events), key=lambda e: (e["t"], e["id"]))
    path.write_text(dumps(events) + "\n", encoding="utf-8")


def words(s: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if len(w) > 3}


def similar(a: dict, b: dict) -> bool:
    """Close in time (within either error bar or 0.5%) and sharing title words."""
    tol = max(a.get("t_err", 0), b.get("t_err", 0), abs(a["t"]) * 0.005, 1000)
    if abs(a["t"] - b.get("t", 0)) > tol:
        return False
    wa, wb = words(a["title"]), words(b.get("title", ""))
    return bool(wa and wb) and len(wa & wb) / min(len(wa), len(wb)) >= 0.5


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", nargs="?", help="event file to add into (created if missing)")
    ap.add_argument("--from", dest="src")
    ap.add_argument("--fmt", action="store_true")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()

    if a.fmt:
        for p in C.event_files():
            write(p, C.load_json(p))
        print("formatted", len(C.event_files()), "files")
    else:
        if not a.target:
            ap.error("target file required")
        raw = Path(a.src).read_text() if a.src else sys.stdin.read()
        new = json.loads(raw)
        new = new if isinstance(new, list) else [new]
        existing = C.load_events()
        ids = {e["id"] for e in existing}
        problems = []
        for ev in new:
            if ev.get("id") in ids:
                problems.append(f"duplicate id: {ev['id']}")
            for old in existing:
                if similar(old, ev):
                    problems.append(f"near-duplicate: {ev.get('id')} ~ {old['id']} ({old['_file']})")
            ids.add(ev.get("id"))
        if problems and not a.force:
            print("\n".join(problems), "\n(use --force to add anyway)", file=sys.stderr)
            return 1
        target = Path(a.target)
        current = C.load_json(target) if target.exists() else []
        write(target, current + new)
        print(f"added {len(new)} -> {target}")

    return subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "check.py")]).returncode


if __name__ == "__main__":
    sys.exit(main())
