"""
Fetch all products from electroniksindia.com (Shopify store) and save raw data.

For each product we save:
  - raw/products/{handle}.json   - full product JSON (variants, options, prices)
  - raw/pages/{handle}.html      - full product page HTML (for spec tables, descriptions)

We also save the master listing in raw/products_listing.json.
"""

from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin

import requests

BASE = "https://www.electroniksindia.com"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

OUT = Path(__file__).resolve().parent.parent / "raw"
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "products").mkdir(exist_ok=True)
(OUT / "pages").mkdir(exist_ok=True)


def fetch(url: str, *, as_json: bool = False, retries: int = 4) -> bytes | dict:
    last_err = None
    for attempt in range(retries):
        try:
            r = requests.get(url, headers=HEADERS, timeout=30)
            r.raise_for_status()
            return r.json() if as_json else r.content
        except Exception as e:  # noqa: BLE001
            last_err = e
            wait = 2 ** attempt
            print(f"  retry {attempt + 1}/{retries} after {wait}s: {e}", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"failed to fetch {url}: {last_err}")


def main() -> None:
    # 1) Pull master listing across all pages
    all_products: list[dict] = []
    for page in range(1, 20):
        url = f"{BASE}/products.json?limit=250&page={page}"
        print(f"GET {url}")
        data = fetch(url, as_json=True)
        prods = data.get("products", [])
        if not prods:
            break
        all_products.extend(prods)

    print(f"Total products in listing: {len(all_products)}")
    (OUT / "products_listing.json").write_text(json.dumps(all_products, indent=2))

    # 2) For each product, fetch the per-product JSON + HTML page
    for i, p in enumerate(all_products, 1):
        handle = p["handle"]
        product_json_path = OUT / "products" / f"{handle}.json"
        page_html_path = OUT / "pages" / f"{handle}.html"

        if not product_json_path.exists():
            url = f"{BASE}/products/{handle}.json"
            print(f"[{i}/{len(all_products)}] product json {handle}")
            try:
                data = fetch(url, as_json=True)
                product_json_path.write_text(json.dumps(data, indent=2))
            except Exception as e:  # noqa: BLE001
                print(f"  ! failed product JSON: {e}", file=sys.stderr)

        if not page_html_path.exists():
            url = f"{BASE}/products/{handle}"
            print(f"[{i}/{len(all_products)}] page html {handle}")
            try:
                html = fetch(url)
                page_html_path.write_bytes(html)
            except Exception as e:  # noqa: BLE001
                print(f"  ! failed page HTML: {e}", file=sys.stderr)

        time.sleep(0.25)


if __name__ == "__main__":
    main()
