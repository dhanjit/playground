# electronics-scraper

Scraper + parser for [electroniksindia.com](https://www.electroniksindia.com),
focused on the SkullSaints mini-PC line, plus a competitor-pricing index for
Apple Mac mini / Mac Studio and Windows mini PCs sold in India.

## Layout

```
electronics-scraper/
├── README.md                    you are here
├── REPORT.md                    full catalog + Mac/Intel comparison (start here)
├── scripts/
│   ├── 01_fetch_all.py          fetch all 167 storefront products + product pages
│   └── 02_parse_minipc.py       parse the 20 mini-PC SKUs into JSON + CSV
├── raw/
│   ├── products/*.json          per-product Shopify JSON (variants, prices)
│   ├── pages/*.html.gz          per-product full page HTML (gzipped)
│   ├── products_listing.json    master listing across all products.json pages
│   ├── products_page1.json      raw paginated dump
│   └── competitors/             ad-hoc fetched HTML from Apple India and others
└── data/
    ├── minipcs.json             20 mini PCs, parsed specs + variants
    ├── minipc_configs.csv       175 rows, one per (model, configuration)
    ├── minipc_summary.csv       21 rows, one per mini-PC model
    ├── apple_india_macs.json    Apple India Mac mini + Mac Studio standard SKUs
    └── competitor_minipcs.json  ASUS NUC / Beelink / Geekom / Minisforum in India
```

## Reproducing the data

```bash
# 1. Fetch every storefront product + page
python3 scripts/01_fetch_all.py

# 2. Parse the 20 mini-PC SKUs into JSON + CSV
python3 scripts/02_parse_minipc.py
```

`01_fetch_all.py` is idempotent — it only downloads files that aren't already on
disk. The page HTMLs are stored gzipped (`.html.gz`); `02_parse_minipc.py` reads
either `.html` or `.html.gz` transparently.

## Data quality notes

- **Storefront prices** are read directly from the Shopify product JSON
  (`/products/{handle}.json` → `product.variants[].price`) and have been
  cross-checked against the live page (`WebFetch`) for several SKUs — they
  match exactly.
- **Specs** come from inline HTML "spec card" divs (`<div ...><strong>Label</strong>
  <br>Value</div>`) on the rendered product page. Two older legacy SKUs (Titan
  6900HX, Rudra Alder Lake) use a different layout and have empty spec maps;
  for those, see the title + variant option names + the `body_html` in
  `raw/products/`.
- **Competitor pricing** is a snapshot — Amazon India is volatile and the
  cross-border imports are especially so. See `data/competitor_minipcs.json`
  for the cited sources per row.
