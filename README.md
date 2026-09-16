# Harbourline Atlas

Interactive atlas of **ports, free & industrial zones, logistics corridors and border crossings** across Africa and the Middle East. Select a country, browse the four lists, open any infrastructure for its detail sheet (status, operator, concession, capacity, throughput, projects, sources, map link).

Built for business-development work at a global port operator. Wave 1 (Sept 2026): 10 countries, 305 infrastructures.

## Layout

```
data/       one JSON file per country (ISO2 lowercase), see docs/SCHEMA.md
src/        template.html — the application (HTML/CSS/JS, no dependencies)
docs/       SCHEMA.md — data schema and research rules
build.py    merges data/*.json into src/template.html → index.html
index.html  the built, self-contained application
```

## Build

```bash
ATLAS_CODE="choose-an-access-code" python3 build.py
```

The access code gates the page; only its SHA-256 hash is embedded. (It is a deterrent, not real security — the data is readable in the page source. Use hosting-level authentication such as Cloudflare Access for real control.)

## Hosting

Any static host works (GitHub Pages, Cloudflare Pages, Netlify): publish `index.html` at the root.

## Adding countries

1. Research the country following `docs/SCHEMA.md`; save as `data/<iso2>.json`.
2. Run `build.py`; commit `data/`, and `index.html`.
3. Remove the country from the "coming in later waves" list in `src/template.html` (`SOON` constant) if present.

## Data provenance

Every record carries at least one source URL. Figures are compressed from public press releases, port authorities, ministries, development banks and reputable trade press; unknown values are marked `n/a` rather than estimated. Last research pass: September 2026.
