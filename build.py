#!/usr/bin/env python3
"""Build index.html from template.html + <iso2>.json country files (flat layout).

Usage:  ATLAS_CODE="your-access-code" python3 build.py
The access code is never stored in the repo — only its SHA-256 hash is embedded in index.html.
"""
import glob, hashlib, json, os, sys

code = os.environ.get("ATLAS_CODE")
if not code:
    sys.exit("Set ATLAS_CODE=<access code> before building.")

atlas = {}
for path in sorted(glob.glob("*.json")):
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    atlas[d["country"]["code"]] = d

payload = json.dumps(atlas, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
template = open("template.html", encoding="utf-8").read()
html = template.replace("__DATA__", payload).replace("__CODEHASH__", hashlib.sha256(code.encode()).hexdigest())

# Standalone page (the Claude artifact wraps this skeleton itself; GitHub Pages needs it explicitly)
doc = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
       '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
       '<style>:root{color-scheme:light dark}body{margin:0}[hidden]{display:none!important}</style>'
       '</head><body>' + html + '</body></html>')
open("index.html", "w", encoding="utf-8").write(doc)
n = sum(len(d[k]) for d in atlas.values() for k in ("ports", "zones", "corridors", "border_crossings"))
print(f"index.html built: {len(atlas)} countries, {n} infrastructures, {os.path.getsize('index.html')//1024} KB")
