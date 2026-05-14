"""
Parse mini-PC products from raw/ into structured data:
  - data/minipcs.json          - hierarchical: products with specs and variants
  - data/minipc_configs.csv    - flat one-row-per-configuration
"""

from __future__ import annotations

import csv
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)


# Site categorization, taken from the navigation drawer.
SITE_CATEGORIES = {
    "Daily Tasks": [
        "helix-by-skullsaints-intel-core-series-12gb-lpddr5-4800mhz-dual-nvme-pcie-ssd-usb-3-2-usb-c-10gbps-4k-2-5gbps-lan-wi-fi-6-bt-5-2-4k-triple-display-mini-pc",
        "mist-by-skullsaints-ryzen-3-4300u-ddr4-dual-channel-pcie-nvme-ssd-usb-3-2-gen2-usb-c-dp-pd-2-5gbps-lan-wi-fi-6-bt-5-3-4k-dual-display-mini-pc",
        "corex-by-skullsaints-powered-by-ryzen-5-4500u-wi-fi-6e-bt-5-3-triple-display-and-expandable-ram-storage-ai-mini-pc",
        "agni-by-skullsaints-mini-pc-intel-twin-lake-n150-vibrant-lcd-screen-m-2-ssd-mini-tower-with-rgb-lights-wifi-6-4k-uhd-dual-lan-for-home-and-office",
        "ash-by-skullsaints-mini-pc-intel-twin-lake-n150-16gb-lpddr5-triple-display-support-m-2-nvme-wifi-5-bluetooth-5-2",
        "rudra-by-skullsaints-mini-pc-with-n150-twin-lake-upto-3-6ghz-16gb-ddr5-ram-512gb-m-2-ssd-triple-4k-display-dual-lan-wifi-6-bluetooth-5-2-win-11-pro",
        "pulse-by-skullsaints-mini-pc-intel-celeron-5205u-dual-m-2-ssd-slots-2-5gb-lan-hdmi-dual-4k-display-wifi-5-bt-5-0",
    ],
    "Heavy Work": [
        "corex-powered-by-ryzen-7-4800h-wi-fi-6-bt-5-2-triple-display-and-expandable-ram-storage",
        "corex-powered-by-ryzen-9-5900hx-wi-fi-6-bt-5-2-triple-display-and-expandable-ram-storage-ai-mini-pc",
        "skullsaints-dragon-ryzen-5-5600u-colorful-mini-pc",
        "jupiter-by-skullsaints-intel-core-ultra-5-135h-14-cores-18-threads-arc-graphics-ddr5-pcie-4-0-wi-fi-6-bluetooth-5-2-ai-optimized-mini-pc",
    ],
    "Extreme Power": [
        "corex-pro-max-by-skullsaints-amd-ryzen-7-7840hs-radeon-780m-graphics-32gb-lpddr5-6400mhz-ram-upto-8tb-storage-usb4-8k-support-2-5g-lan-wi-fi-6-bt5-2-and-quad-display-support",
        "fury-by-skullsaints-compact-mini-pc-with-amd-ryzen-7840hs-radeon-780m-graphics-usb4-8k-support-dual-2-5g-lan-and-wi-fi-6-bt5-2-triple-display",
        "fury-x-by-skullsaints-amd-ryzen-7840hs-radeon-780m-graphics-usb4-8k-support-dual-2-5g-lan-and-wi-fi-6e-bt5-3-triple-display-with-oculink-port",
        "corex-pro-by-skullsaints-powered-by-ryzen-7-6800h-24gb-lpddr5-6400mhz-usb-4-0-2-5gbps-lan-wi-fi-6e-bt-5-3-triple-display-ai-mini-pc",
        "jupiter-by-skullsaints-intel-core-ultra-7-155h-16-cores-22-threads-arc-graphics-ddr5-pcie-4-0-wi-fi-6-bluetooth-5-2-ai-optimized-high-performance-mini-pc",
    ],
    "NAS Mini PC": [
        "nebula-by-skullsaints-mini-pc-nas-hybrid-with-intel-n150-12gb-lpddr5-quad-m-2-slots-up-to-16tb-dual-2-5g-lan-wifi-6-usb3-2-hdmi-4k-type-c-pd",
    ],
    "Industrial Fanless": [
        "skullsaints-onyx-intel-j6412",
    ],
    "Legacy / Older Listings": [
        "rudra-by-skullsaints-intel-12th-gen-alder-lake-processor-hdmi-4k-60hz-3-screen-display-dual-ethernet-cube-mini-pocket-pc",
        "titan-by-skullsaints-amd-ryzen-9-6900hx-8c-16t-upto-4-9ghz-ddr5-4800mhz-dual-m-2-ssd-wifi-6-bt-5-2-rgb-gaming-mini-pc",
    ],
}

# Friendly model name overrides keyed by handle.
MODEL_NAMES = {
    "helix-by-skullsaints-intel-core-series-12gb-lpddr5-4800mhz-dual-nvme-pcie-ssd-usb-3-2-usb-c-10gbps-4k-2-5gbps-lan-wi-fi-6-bt-5-2-4k-triple-display-mini-pc": "Helix (Intel i3-1215U, 12th Gen)",
    "mist-by-skullsaints-ryzen-3-4300u-ddr4-dual-channel-pcie-nvme-ssd-usb-3-2-gen2-usb-c-dp-pd-2-5gbps-lan-wi-fi-6-bt-5-3-4k-dual-display-mini-pc": "Mist (AMD Ryzen 3 4300U)",
    "corex-by-skullsaints-powered-by-ryzen-5-4500u-wi-fi-6e-bt-5-3-triple-display-and-expandable-ram-storage-ai-mini-pc": "CoreX (AMD Ryzen 5 4500U)",
    "agni-by-skullsaints-mini-pc-intel-twin-lake-n150-vibrant-lcd-screen-m-2-ssd-mini-tower-with-rgb-lights-wifi-6-4k-uhd-dual-lan-for-home-and-office": "Agni (Intel N150 Twin Lake)",
    "ash-by-skullsaints-mini-pc-intel-twin-lake-n150-16gb-lpddr5-triple-display-support-m-2-nvme-wifi-5-bluetooth-5-2": "Ash (Intel N150 Twin Lake)",
    "rudra-by-skullsaints-mini-pc-with-n150-twin-lake-upto-3-6ghz-16gb-ddr5-ram-512gb-m-2-ssd-triple-4k-display-dual-lan-wifi-6-bluetooth-5-2-win-11-pro": "Rudra (Intel N150 Twin Lake)",
    "pulse-by-skullsaints-mini-pc-intel-celeron-5205u-dual-m-2-ssd-slots-2-5gb-lan-hdmi-dual-4k-display-wifi-5-bt-5-0": "Pulse (Intel Celeron 5205U)",
    "corex-powered-by-ryzen-7-4800h-wi-fi-6-bt-5-2-triple-display-and-expandable-ram-storage": "CoreX (AMD Ryzen 7 4800H)",
    "corex-powered-by-ryzen-9-5900hx-wi-fi-6-bt-5-2-triple-display-and-expandable-ram-storage-ai-mini-pc": "CoreX (AMD Ryzen 9 5900HX)",
    "skullsaints-dragon-ryzen-5-5600u-colorful-mini-pc": "Dragon (AMD Ryzen 5 5600U)",
    "jupiter-by-skullsaints-intel-core-ultra-5-135h-14-cores-18-threads-arc-graphics-ddr5-pcie-4-0-wi-fi-6-bluetooth-5-2-ai-optimized-mini-pc": "Jupiter (Intel Core Ultra 5 135H, 14th Gen)",
    "corex-pro-max-by-skullsaints-amd-ryzen-7-7840hs-radeon-780m-graphics-32gb-lpddr5-6400mhz-ram-upto-8tb-storage-usb4-8k-support-2-5g-lan-wi-fi-6-bt5-2-and-quad-display-support": "CoreX Pro Max (AMD Ryzen 7 7840HS)",
    "fury-by-skullsaints-compact-mini-pc-with-amd-ryzen-7840hs-radeon-780m-graphics-usb4-8k-support-dual-2-5g-lan-and-wi-fi-6-bt5-2-triple-display": "Fury (AMD Ryzen 7 7840HS)",
    "fury-x-by-skullsaints-amd-ryzen-7840hs-radeon-780m-graphics-usb4-8k-support-dual-2-5g-lan-and-wi-fi-6e-bt5-3-triple-display-with-oculink-port": "Fury-X (AMD Ryzen 7 7840HS, OCuLink)",
    "corex-pro-by-skullsaints-powered-by-ryzen-7-6800h-24gb-lpddr5-6400mhz-usb-4-0-2-5gbps-lan-wi-fi-6e-bt-5-3-triple-display-ai-mini-pc": "CoreX Pro (AMD Ryzen 7 6800H)",
    "jupiter-by-skullsaints-intel-core-ultra-7-155h-16-cores-22-threads-arc-graphics-ddr5-pcie-4-0-wi-fi-6-bluetooth-5-2-ai-optimized-high-performance-mini-pc": "Jupiter (Intel Core Ultra 7 155H, 14th Gen)",
    "nebula-by-skullsaints-mini-pc-nas-hybrid-with-intel-n150-12gb-lpddr5-quad-m-2-slots-up-to-16tb-dual-2-5g-lan-wifi-6-usb3-2-hdmi-4k-type-c-pd": "Nebula NAS (Intel N150 Twin Lake)",
    "skullsaints-onyx-intel-j6412": "Onyx Industrial (Intel Celeron J6412)",
    "rudra-by-skullsaints-intel-12th-gen-alder-lake-processor-hdmi-4k-60hz-3-screen-display-dual-ethernet-cube-mini-pocket-pc": "Rudra (Intel Alder Lake N100 / N5105) [legacy]",
    "titan-by-skullsaints-amd-ryzen-9-6900hx-8c-16t-upto-4-9ghz-ddr5-4800mhz-dual-m-2-ssd-wifi-6-bt-5-2-rgb-gaming-mini-pc": "Titan (AMD Ryzen 9 6900HX) [legacy]",
}


def extract_specs_from_html(html: str) -> dict[str, str]:
    """Pull spec card divs (<div ...><strong>label</strong><br>value</div>)."""
    soup = BeautifulSoup(html, "lxml")
    specs: dict[str, str] = {}
    for div in soup.find_all("div"):
        strong = div.find("strong", recursive=False)
        if not strong:
            continue
        style = div.get("style", "")
        if "border-left" not in style:
            continue
        label = strong.get_text(" ", strip=True)
        full = div.get_text(" ", strip=True)
        value = full[len(label):].strip()
        if not label or not value:
            continue
        # Skip the marketing pitch cards that show up on every page
        if label in {
            "Lower Prices",
            "Extended 15-Month Warranty",
            "Free Pickup & Replacement",
            "Lower Prices ",
        }:
            continue
        specs.setdefault(label, value)
    return specs


def extract_review_count(html: str) -> int | None:
    m = re.search(r"(\d+)\s+reviews?", html)
    if m:
        return int(m.group(1))
    return None


@dataclass
class Variant:
    sku: str | None
    title: str  # human-readable variant title
    options: list[str]  # the option1 / option2 / option3 values
    price_inr: float
    compare_at_price_inr: float | None
    available: bool


@dataclass
class MiniPC:
    handle: str
    site_category: str
    model: str
    full_title: str
    vendor: str
    url: str
    options_meta: list[dict]  # the schema of the option dropdowns
    specs: dict[str, str]  # parsed spec card key/value
    variants: list[Variant] = field(default_factory=list)
    base_price_inr: float | None = None
    max_price_inr: float | None = None
    mrp_inr: float | None = None
    review_count: int | None = None


def load_product(handle: str) -> dict:
    return json.loads((RAW / "products" / f"{handle}.json").read_text())["product"]


def _read_page_html(handle: str) -> str:
    """Page HTML is stored either as .html or .html.gz."""
    plain = RAW / "pages" / f"{handle}.html"
    gz = RAW / "pages" / f"{handle}.html.gz"
    if plain.exists():
        return plain.read_text()
    if gz.exists():
        import gzip
        return gzip.decompress(gz.read_bytes()).decode("utf-8")
    raise FileNotFoundError(f"no page HTML for {handle}")


def parse_minipc(handle: str, category: str) -> MiniPC:
    p = load_product(handle)
    html = _read_page_html(handle)

    specs = extract_specs_from_html(html)
    review_count = extract_review_count(html)

    variants: list[Variant] = []
    prices = []
    compares = []
    for v in p["variants"]:
        opts = [v.get("option1"), v.get("option2"), v.get("option3")]
        opts = [o for o in opts if o is not None]
        price = float(v["price"])
        compare = float(v["compare_at_price"]) if v.get("compare_at_price") else None
        prices.append(price)
        if compare:
            compares.append(compare)
        # Treat a zero-RAM/zero-storage variant as "barebone" but still record it.
        variants.append(
            Variant(
                sku=v.get("sku") or None,
                title=v["title"],
                options=opts,
                price_inr=price,
                compare_at_price_inr=compare,
                available=bool(v.get("requires_shipping", True)) and price > 0,
            )
        )

    return MiniPC(
        handle=handle,
        site_category=category,
        model=MODEL_NAMES.get(handle, p["title"][:80]),
        full_title=p["title"],
        vendor=p["vendor"],
        url=f"https://www.electroniksindia.com/products/{handle}",
        options_meta=p["options"],
        specs=specs,
        variants=variants,
        base_price_inr=min(prices) if prices else None,
        max_price_inr=max(prices) if prices else None,
        mrp_inr=max(compares) if compares else None,
        review_count=review_count,
    )


def main() -> None:
    minipcs: list[MiniPC] = []
    for category, handles in SITE_CATEGORIES.items():
        for h in handles:
            try:
                m = parse_minipc(h, category)
                minipcs.append(m)
            except FileNotFoundError as e:
                print(f"  ! missing data for {h}: {e}")

    # Write structured JSON
    out = []
    for m in minipcs:
        d = asdict(m)
        out.append(d)
    (DATA / "minipcs.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"wrote {DATA/'minipcs.json'}: {len(out)} mini PCs")

    # Write flat CSV: one row per (model, configuration)
    csv_path = DATA / "minipc_configs.csv"
    with csv_path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "site_category",
                "model",
                "cpu",
                "ram_spec",
                "storage_spec",
                "configuration",
                "price_inr",
                "compare_at_price_inr",
                "discount_pct",
                "url",
                "handle",
            ]
        )
        for m in minipcs:
            cpu = m.specs.get("Processor (CPU)") or m.specs.get("Processor") or ""
            ram_default = m.specs.get("Memory (RAM)") or ""
            storage_default = (
                m.specs.get("Storage (SSD)")
                or m.specs.get("Storage")
                or m.specs.get("NVMe Storage")
                or ""
            )
            for v in m.variants:
                discount = ""
                if v.compare_at_price_inr and v.compare_at_price_inr > v.price_inr:
                    discount = (
                        f"{(v.compare_at_price_inr - v.price_inr) / v.compare_at_price_inr * 100:.0f}%"
                    )
                w.writerow(
                    [
                        m.site_category,
                        m.model,
                        cpu,
                        ram_default,
                        storage_default,
                        v.title,
                        f"{v.price_inr:.0f}",
                        f"{v.compare_at_price_inr:.0f}" if v.compare_at_price_inr else "",
                        discount,
                        m.url,
                        m.handle,
                    ]
                )
    print(f"wrote {csv_path}")

    # Write a per-model summary
    summary_path = DATA / "minipc_summary.csv"
    with summary_path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "site_category",
                "model",
                "cpu",
                "default_ram",
                "default_storage",
                "min_price_inr",
                "max_price_inr",
                "mrp_inr",
                "n_variants",
                "review_count",
                "url",
            ]
        )
        for m in minipcs:
            w.writerow(
                [
                    m.site_category,
                    m.model,
                    m.specs.get("Processor (CPU)") or m.specs.get("Processor") or "",
                    m.specs.get("Memory (RAM)") or "",
                    m.specs.get("Storage (SSD)")
                    or m.specs.get("Storage")
                    or m.specs.get("NVMe Storage")
                    or "",
                    f"{m.base_price_inr:.0f}" if m.base_price_inr else "",
                    f"{m.max_price_inr:.0f}" if m.max_price_inr else "",
                    f"{m.mrp_inr:.0f}" if m.mrp_inr else "",
                    len(m.variants),
                    m.review_count if m.review_count is not None else "",
                    m.url,
                ]
            )
    print(f"wrote {summary_path}")


if __name__ == "__main__":
    main()
