"""Build sources/ cache: one markdown file per bib key with metadata, links and abstract.

    .venv/bin/python tools/source_cache.py .                  # only fetches keys without a file yet
    .venv/bin/python tools/source_cache.py . --refetch K1 K2  # re-fetch these keys (keeps their notes)
    .venv/bin/python tools/source_cache.py . --refetch-missing # re-fetch every key whose abstract is missing

Order: OpenAlex -> Crossref -> Europe PMC -> Semantic Scholar -> publisher landing page (meta tags /
abstract block, via doi.org). Anything below "## Notes" or "## Verification" in a file is kept on refetch.
"""
import re,json,urllib.request,urllib.parse,html,time,os,sys
ROOT=sys.argv[1]; ARGS=sys.argv[2:]; OUT=os.path.join(ROOT,"sources","abstracts"); os.makedirs(OUT,exist_ok=True)
bib=open(os.path.join(ROOT,"data","sources.bib"),encoding="utf-8").read()
H={"User-Agent":"bibcache/0.1"}
def get(u,t=30):
    return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=t))
BH={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36","Accept":"text/html"}
def landing(doi):
    """Abstract from the publisher's landing page: citation/dc/og meta tags or an abstract block."""
    t=urllib.request.urlopen(urllib.request.Request("https://doi.org/"+doi,headers=BH),timeout=30).read().decode("utf8","ignore")
    best=""
    for pat in [r'<meta[^>]+name="(?:citation_abstract|dc\.description|DC\.Description|description)"[^>]+content="([^"]{200,})"',
                r'<meta[^>]+property="og:description"[^>]+content="([^"]{200,})"',
                r'<div[^>]+id="Abs1-content"[^>]*>(.*?)</div>',
                r'<section[^>]+class="[^"]*abstract[^"]*"[^>]*>(.*?)</section>',
                r'<div[^>]+class="[^"]*abstract[^"]*"[^>]*>(.*?)</div>']:
        for m in re.finditer(pat,t,re.S|re.I):
            a=clean(m.group(1))
            if len(a)>len(best): best=a
    return best
def clean(a): return re.sub(r"\s+"," ",re.sub(r"<[^>]+>","",html.unescape(a or ""))).strip()
rows=[]
for m in re.finditer(r"@(\w+)\{([^,]+),(.*?)\n\}",bib,re.S):
    typ,key,body=m.groups(); body+="\n"
    if key.startswith("phylopic-"): continue
    f=lambda k:(re.search(k+r"\s*=\s*\{(.*?)\},?\n",body,re.S) or [None,""])[1]
    doi=f("doi"); title=clean(f("title")); year=f("year")
    path=os.path.join(OUT,key+".md")
    keep=""; redo=False
    if os.path.exists(path):
        old=open(path,encoding="utf-8").read()
        redo=key in ARGS or ("--refetch-missing" in ARGS and "Abstract from: (none found)" in old)
        if redo:
            m2=re.search(r"\n## (Notes|Verification).*",old,re.S); keep=m2.group(0) if m2 else ""
    if os.path.exists(path) and not redo:
        rows.append(open(path).read().split("\n")[1]); continue
    abs_,src,oa,oaurl="","","",""
    if doi:
        q=urllib.parse.quote(doi,safe="/()")
        try:
            w=get("https://api.openalex.org/works/doi:"+q)
            ii=w.get("abstract_inverted_index") or {}
            abs_=" ".join(t for _,t in sorted((p,t) for t,ps in ii.items() for p in ps)); src="OpenAlex" if abs_ else ""
            oa=(w.get("open_access") or {}).get("oa_status","")
            loc=w.get("best_oa_location") or {}
            oaurl=loc.get("pdf_url") or loc.get("landing_page_url") or ""
        except Exception: pass
        if len(abs_)<200 or "Search for other works" in abs_:
            try:
                a=clean(get("https://api.crossref.org/works/"+q)["message"].get("abstract",""))
                if len(a)>len(abs_): abs_,src=a,"Crossref"
            except Exception: pass
        if len(abs_)<200:
            try:
                res=get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query="+urllib.parse.quote(f'DOI:"{doi}"'))["resultList"]["result"]
                if res and len(res[0].get("abstractText",""))>len(abs_): abs_,src=clean(res[0]["abstractText"]),"Europe PMC"
            except Exception: pass
        if len(abs_)<200:
            try:
                r=get("https://api.semanticscholar.org/graph/v1/paper/DOI:"+q+"?fields=abstract,tldr"); time.sleep(1.1)
                a=r.get("abstract") or ""
                if not a and r.get("tldr"): a="(TLDR) "+r["tldr"]["text"]
                if len(a)>len(abs_): abs_,src=clean(a),"Semantic Scholar"
            except Exception: pass
        bad=lambda a: len(a)<300 or "Search for other works" in a or a.startswith("(TLDR)") or "this issue" in a
        if bad(abs_) or key in ARGS:
            try:
                a=landing(doi)
                if len(a)>200 and (key in ARGS or bad(abs_) and len(a)>len(abs_)*0.8 or not abs_): abs_,src=a,"publisher page"
            except Exception: pass
    link=f"https://doi.org/{doi}" if doi else ""
    head=f"{key} | {year} | {title}"
    md=f"# {key}\n{head}\n\n- DOI: {doi or '(none)'}\n- Link: {link or '(none)'}\n- Open access: {oa or 'unknown'}{(' — '+oaurl) if oaurl else ''}\n- Abstract from: {src or '(none found)'}\n\n## Abstract\n{abs_ or '(none found; read the paper)'}\n"+keep
    open(path,"w",encoding="utf-8").write(md); rows.append(head); print("fetched",key,"->",src or "nothing")
    time.sleep(0.25)
print(len(rows),"written")

# Rebuild the index table in sources/README.md (everything above the table is kept).
import glob
readme=os.path.join(ROOT,"sources","README.md")
headtxt=open(readme,encoding="utf-8").read().split("| Key |")[0] if os.path.exists(readme) else "# Sources cache\n\n"
lines=[]
for fn in sorted(glob.glob(os.path.join(OUT,"*.md"))):
    t=open(fn,encoding="utf-8").read(); h=t.split("\n")[1].split(" | ",2)
    doi=re.search(r"- DOI: (.*)",t).group(1); oa=re.search(r"- Open access: (\S+)",t).group(1)
    has="no" if "none found" in re.search(r"- Abstract from: (.*)",t).group(1) else "yes"
    lines.append(f"| [{h[0]}](abstracts/{h[0]}.md) | {h[1]} | {h[2][:90]} | {oa} | {has} | "+(f"[doi](https://doi.org/{doi})" if doi!="(none)" else "—")+" |")
open(readme,"w",encoding="utf-8").write(headtxt+"| Key | Year | Title | Open access | Abstract | Link |\n|---|---|---|---|---|---|\n"+"\n".join(lines)+"\n")
