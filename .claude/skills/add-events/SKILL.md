---
name: add-events
description: Research and add cited events to the Lifetime of the Earth book data for a topic or time range. Use when asked to add, research or fill in events, facts or dates.
---

# Add events

Input: a topic ("Snowball Earth") or a range (years or content pages).

1. **See what exists.** Use `./run query --from T0 --to T1` or `--grep topic`. Don't open data files.
2. **Research.** Prefer primary literature or review papers with DOIs; the ICS chart for boundaries. For each fact
   note the date (midpoint), ± uncertainty, and the exact source. Never invent a citation; if unsure, leave it out.
3. **Add sources first.** Append BibTeX entries to `data/sources.bib` (key `firstauthorYEAR`, include `doi`).
   Check existing keys with `./run query --sources`.
4. **Pick tags.** Run `./run query --tags` (master list in `data/tags.json`, with usage counts). Give each event
   1–4 tags, **reusing existing tags** wherever one fits, even loosely. Only if no tag fits, add one to
   `data/tags.json` (kebab-case, one-line description) and tell the user in the report. Add `debated` when
   the date, cause or reality is disputed, and say so in the text with the competing range in `t_err`.
   Add `first` for earliest occurrences, `ancestor` for recognizable ancestors (good art candidates),
   `curiosity` for remarkable or amusing facts.
5. **Write events** as a JSON array (fields: `data/schema.json`, including `tags`). Integer years, negative. `t` = midpoint. Always set `importance` (1–5, scale in docs/significance-review.md).
   Titles ≤ 90 chars; text 1–3 sentences, ≤ 600 chars, plain and concrete. `"verified": false` unless you
   checked the date against the source text itself.
   Unverified events also get a row in `agent-notes/verification-backlog.md` (what to check, where).
6. **Art**: attach only images that can be fetched as is (PhyloPic: `./run art search`, `fetch`, `outline`; rules in
   `agent-notes/image-resources.md`). Don't make drawings, maps or diagrams here; add picture-worthy events to
   `docs/art-candidates.md` (what to show, likely resource, approach) for a separate art pass.
7. **Add**: `./run add data/events/<file>.json < /path/to/new.json` (rejects duplicates; use the existing file
   for that era, or events.json until sharding is decided).
8. **Look**: `./run png <page>` for affected pages and view the PNGs; fix overlaps or overlong text.
9. **Report** to the user: events added (id, page, tags), art candidates listed, any new tags, sources added, `./run fullness --text` before → after.
