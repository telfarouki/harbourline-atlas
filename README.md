# Harbourline Atlas

Interactive atlas of **ports, free & industrial zones, logistics corridors and border crossings** across Africa and the Middle East. Select a country, browse the four lists, open any infrastructure for its detail sheet (status, operator, concession, capacity, throughput, projects, sources, map link).

Built for business-development work at a global port operator. Wave 1 (Sept 2026): 10 countries, 305 infrastructures.

## Layout

```
<iso2>.json     one JSON file per country (ma.json, eg.json, …), see SCHEMA.md
template.html   the application (HTML/CSS/JS, no dependencies)
SCHEMA.md       data schema and research rules
build.py        merges the country JSON files into template.html → index.html
index.html      the built, self-contained application (this is what gets hosted)
```

## Build

```bash
ATLAS_CODE="choose-an-access-code" python3 build.py
```

The access code gates the page; only its SHA-256 hash is embedded. (It is a deterrent, not real security — the data is readable in the page source. Use hosting-level authentication such as Cloudflare Access for real control.)

## Hosting

Any static host works (GitHub Pages, Cloudflare Pages, Netlify): publish `index.html` at the root.

## Adding countries

1. Research the country following `SCHEMA.md`; save as `<iso2>.json` at the repository root.
2. Run `build.py`; commit the new JSON and the rebuilt `index.html`.
3. Remove the country from the "coming in later waves" list in `template.html` (`SOON` constant) if present.

## Data provenance

Every record carries at least one source URL. Figures are compressed from public press releases, port authorities, ministries, development banks and reputable trade press; unknown values are marked `n/a` rather than estimated. Last research pass: September 2026.
