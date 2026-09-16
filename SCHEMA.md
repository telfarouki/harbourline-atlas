# Infrastructure atlas — data schema (v1)

Write ONE file per country: `<ISO2 lowercase>.json` (e.g. `ma.json`). Valid JSON, UTF-8, no comments, no trailing commas. English.

```json
{
  "country": {
    "code": "MA",
    "name": "Morocco",
    "region": "North Africa | West Africa | Central Africa | East Africa | Southern Africa | Gulf | Levant",
    "capital": "Rabat",
    "coastline": "Atlantic and Mediterranean",
    "summary": "3–4 sentences: role in regional trade, main gateways, key operators, headline projects.",
    "key_operators": ["DP World", "APM Terminals", "Marsa Maroc"],
    "sources": ["https://..."]
  },
  "ports": [
    {
      "id": "ma-tanger-med",
      "name": "Tanger Med",
      "type": "container | multipurpose | bulk | oil & gas | ro-ro | fishing | river",
      "location": {"city": "Tangier", "lat": 35.888, "lng": -5.499},
      "operator": "Tanger Med Port Authority; terminals: APM Terminals, Eurogate, Marsa Maroc",
      "concession": "Concession details: who, term, since when (or 'n/a')",
      "capacity": "e.g. 9m TEU/year; 2 container terminals; draft 18 m",
      "throughput": "latest known volume with year, e.g. 10.2m TEU (2024)",
      "status": "operational | under construction | planned | suspended",
      "opened": "2007",
      "projects": "Expansion / upgrades under way or announced, with dates and values",
      "notes": "Anything else decision-relevant (hinterland links, congestion, ownership changes)",
      "sources": ["https://..."]
    }
  ],
  "zones": [
    {
      "id": "ma-tanger-free-zone",
      "name": "Tanger Free Zone",
      "type": "free zone | special economic zone | industrial zone | logistics zone | port-linked zone",
      "location": {"city": "Tangier", "lat": 35.72, "lng": -5.90},
      "authority": "Regulator / developer / operator",
      "area": "e.g. 400 ha",
      "sectors": ["automotive", "aerospace", "logistics"],
      "incentives": "Key fiscal/customs incentives in one or two lines",
      "tenants": "Notable tenants or number of companies",
      "status": "operational | under construction | planned",
      "opened": "1999",
      "projects": "Extensions / new phases",
      "notes": "",
      "sources": ["https://..."]
    }
  ],
  "corridors": [
    {
      "id": "ma-tanger-med-casablanca-rail",
      "name": "Tanger Med – Casablanca – Marrakech rail freight corridor",
      "modes": ["rail", "road", "pipeline", "inland waterway", "multimodal"],
      "route": "Origin → key nodes → destination",
      "countries": ["MA"],
      "length": "e.g. 350 km",
      "operator": "ONCF / concessionaire",
      "status": "operational | under construction | planned",
      "capacity_or_traffic": "Trains/day, tonnes/year, TEU/year if known",
      "projects": "Upgrades, financing (AfDB, World Bank, China Exim…), dates",
      "notes": "",
      "sources": ["https://..."]
    }
  ],
  "border_crossings": [
    {
      "id": "ma-bab-sebta",
      "name": "Bab Sebta",
      "with_country": "ES",
      "with_country_name": "Spain (Ceuta)",
      "type": "road | rail | road+rail | OSBP (one-stop border post) | ferry",
      "location": {"city": "Fnideq", "lat": 35.85, "lng": -5.34},
      "traffic": "Trucks/day, tonnes/year or qualitative ('main trade gateway to X')",
      "status": "operational | under construction | planned | closed",
      "hours": "24/7 or schedule if known",
      "projects": "OSBP upgrades, scanners, new terminals, financing",
      "notes": "Delays, informal trade, security context",
      "sources": ["https://..."]
    }
  ]
}
```

Rules
- Aim for the **main infrastructures**: 5–10 ports, 5–10 zones, 3–8 corridors, 4–8 border crossings per country (fewer only if the country genuinely has fewer).
- `id` = ISO2 lowercase + slug, unique within the file.
- `lat`/`lng` decimal degrees, WGS84, best available precision (city-level is acceptable if exact is unknown).
- Every record needs at least one real `sources` URL that you actually found. Prefer official sources (port authority, ministry, operator press room, World Bank/AfDB project pages) then reputable trade press. Never invent facts, URLs or figures; write "n/a" when unknown.
- Dates and figures must carry their year. Flag DP World assets or competitor concessions in `notes`.
- Status must be one of the listed values.
