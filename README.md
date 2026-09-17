# Harbourline Atlas

Interactive atlas of **ports, free & industrial zones, logistics corridors and border crossings** across Africa and the Middle East. Select a country, browse the four lists, open any infrastructure for its detail sheet (status, operator, concession, capacity, throughput, projects, sources, map link).

Built for business-development work at a global port operator. Wave 1 (Sept 2026): 10 countries, 305 infrastructures.

## Layout

```
index.html      the application: access-request form, 6-digit e-mail code sign-in, atlas (data loaded from Supabase)
admin.html      administration: approve/reject requests, revoke users, import country JSON files, visit log
config.js       Supabase project URL + publishable key (public by design)
<iso2>.json     one JSON file per country (ma.json, eg.json, …), see SCHEMA.md — imported into Supabase via admin.html
supabase/schema.sql   database tables, functions and row-level-security policies
template.html + build.py   legacy single-file build (access-code gate, data inlined) — kept for reference
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
