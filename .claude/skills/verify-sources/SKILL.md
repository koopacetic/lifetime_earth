---
name: verify-sources
description: Check unverified events (and other cited claims) in the Lifetime of the Earth data against their sources, correct what the source contradicts, record the evidence in sources/, and set "verified": true. Use when asked to verify, fact-check or work through the verification backlog.
---

# Verify sources

Goal: every event's date, uncertainty and text claims match what its cited sources say. `verified: true` means
the date **and** each factual claim were checked against the source (abstract, full text, or a reliable quote of
it), not against memory.

## 1. Build the worklist
- `./run check` prints the number of unverified events. List them with their source keys:
  `python3 -c "import json,glob;[print(e['id'],e['sources']) for f in glob.glob('data/events/*.json') for e in json.load(open(f)) if not e.get('verified')]"`
- Read the top of `agent-notes/verification-backlog.md` ("Still unverified" table) for known gaps and the claims to check.

## 2. Fill the cache first (cheap)
- `.venv/bin/python tools/source_cache.py .` fetches any source key without a `sources/abstracts/<key>.md` yet.
- `--refetch-missing` retries keys with no abstract; `--refetch KEY ...` forces a re-fetch, adding the publisher's
  landing page (works for Nature, Springer, Wiley and some others; Science, Elsevier and GSA usually block it).
  Notes under `## Notes` / `## Verification` in a cache file are kept.
- Spot bad abstracts: journal "this issue" summaries (Science), GSA page boilerplate (the real abstract follows
  "Search Abstract"), abstracts cut at the start, `(TLDR)` lines. Refetch those, or treat as missing.

## 3. Check each event (batches of ~15)
Print each unverified event next to its cached abstracts (a short script; truncate abstracts to ~1,400 characters
so output stays readable). For each event decide one of:
- **Matches:** date, ± and every claim are in the source → verify.
- **Wrong or unsupported detail:** correct `t`/`t_err`/`span` or the text to what the source says, or remove the
  unsupported clause. Prefer cutting a sentence to keeping an unsourced one. Then verify.
- **Needs more:** the abstract is silent → go to step 4.

Rules of thumb:
- A session-chosen ± or span is fine if it is derived from the source's stated range; say so in the backlog.
- Convert stage names with the current ICS chart (`data/timescale.json`), e.g. "early Eifelian", "Barremian".
- A counter-claim ("others argue...", "debated") needs its own cited source, often a second key on the event.
- Never add a citation from memory. A new bib entry needs metadata checked on Crossref (`api.crossref.org/works/DOI`).

## 4. Beyond the abstract
In this order, stopping when the claim is settled:
1. Open-access full text through PMC: look up the PMCID on Europe PMC by DOI, then
   `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=<number>` and grep the text for the claim.
2. The open-access URL in the cache file (PDF: download to the scratchpad, `pdftotext`, grep).
3. WebSearch for the abstract or the specific number (send several searches in one turn). Search summaries of
   the paper's own text count; press releases and Wikipedia do not verify a claim on their own.
Full PDFs are not stored in `sources/` (see `sources/README.md`). An abstract recovered from a PDF or page goes in
the cache file's `## Abstract`; anything else goes under `## Verification (<date>)` as one line per claim with
where it came from (URL or PMCID).

## 5. Apply and record
- Edit the event file with a script (load JSON, change fields, dump), then `./run fmt` and `./run check`.
  Keep a backup copy in the scratchpad first.
- Add new bib entries to `data/sources.bib`, then run `tools/source_cache.py .` again.
- Update `agent-notes/verification-backlog.md`: the top section's corrections table (event, was, now, source) and the
  "Still unverified" table with what each remaining event lacks.
- Add a session-log entry. If a correction moves an event far (another page), mention it so the layout gets checked
  (`./run png <page>`).
