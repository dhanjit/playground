# ElectroniksIndia / SkullSaints Mini PCs — A Catalog & Mac/Intel Comparison

**Source store:** [electroniksindia.com](https://www.electroniksindia.com) (Shopify)
**Brand on the SKUs:** SkullSaints (their in‑house mini‑PC line, sold via ElectroniksIndia)
**Data captured:** 14 May 2026 (167 storefront products → 20 mini‑PC SKUs with 158 configurations)

> All prices are MRP / sale price in INR, **inclusive of 18% GST**, as listed on the storefront on 14 May 2026.
> The store applies a flat 10% discount when the URL is reached via their banner / link (so live‑cart prices are typically a bit lower than the page price). The numbers in this report are the page prices — the discount is on top of them.

This report has three parts:

1. **What is sold on electroniksindia.com** — full catalog of mini PCs with every configuration and price.
2. **Comparison vs. Apple Mac mini & Mac Studio** (India MRP).
3. **Comparison vs. Intel/AMD competitors sold in India** (ASUS NUC, Beelink, Geekom, Minisforum).

Raw scraper output (full product JSON, HTML pages, parsed CSV/JSON) lives in `electronics-scraper/`:

- `raw/products/*.json` — raw Shopify product JSON (all 167 storefront products, not just mini PCs)
- `raw/pages/*.html` — full product page HTML
- `data/minipcs.json` — parsed mini PCs with specs + variants
- `data/minipc_configs.csv` — flat one‑row‑per‑configuration table (all 158 SKUs)
- `data/minipc_summary.csv` — one row per model
- `data/apple_india_macs.json` — Apple India Mac mini + Mac Studio standard SKUs
- `data/competitor_minipcs.json` — competitor mini PCs sold in India

---

## 1. ElectroniksIndia / SkullSaints mini-PC catalog

The store's own navigation organises mini PCs into 6 groups. Below is each group with the SKUs in it and a one-line summary; full per-configuration prices follow further down.

### 1.1 Daily Tasks (entry / office / casual)

| Model                   | CPU                                | iGPU                | RAM (max)            | SSD (max)              | Notable I/O                              | Price range (INR)         |
|-------------------------|------------------------------------|---------------------|----------------------|------------------------|------------------------------------------|---------------------------|
| **Pulse**               | Intel Celeron 5205U (2C/2T, 1.9 GHz) | Intel UHD          | DDR4 SODIMM, 32 GB   | 2× M.2 NVMe, 3 TB      | 2.5G LAN (Intel i226), Dual 4K HDMI       | **₹12,999 – ₹17,999** (2 cfg) |
| **Mist**                | AMD Ryzen 3 4300U (4C/4T, 3.7 GHz) | Vega 5             | Dual DDR4 SODIMM, 32 GB | 2× M.2, up to 4 TB  | 2.5G LAN, USB-C DP/PD, Wi-Fi 6 BT5.3      | **₹18,999 – ₹35,999** (7 cfg) |
| **Agni**                | Intel N150 Twin Lake (4C/4T, 3.6 GHz) | Intel UHD       | DDR4 (single), 32 GB | M.2 NVMe + M.2 SATA, 8 TB | 2× 1G LAN, dual 4K HDMI, 1.9″ LCD       | **₹18,999 – ₹42,999** (9 cfg) |
| **Helix**               | Intel i3-1215U (6C/8T, 4.4 GHz)    | Intel UHD          | 12 GB LPDDR5 4800 (soldered) | Dual NVMe, 4 TB | 2.5G LAN, USB-C 10G/4K, **triple 4K**, 5× USB-A | **₹29,999 – ₹44,999** (5 cfg) |
| **Rudra (N150)**        | Intel N150 Twin Lake (4C/4T, 3.6 GHz) | Intel UHD       | 16 GB LPDDR5 4800 (soldered) | M.2 2242, 2 TB  | 2× 1G LAN, **triple 4K via 3× HDMI**     | **₹33,999 – ₹42,999** (3 cfg) |
| **Ash**                 | Intel N150 Twin Lake (4C/4T, 3.6 GHz) | Intel UHD       | 16 GB LPDDR5 4800 (soldered) | M.2 2242, 2 TB  | 2× 1G LAN, USB-C powered, **87×87×36 mm, 168 g** | **₹34,999 – ₹42,999** (3 cfg) |
| **CoreX (Ryzen 5 4500U)** | AMD Ryzen 5 4500U (6C/6T, 4.0 GHz) | Vega 6          | Dual DDR4 SODIMM, 64 GB | 2× M.2, 4 TB      | 1G LAN, USB-C, triple 4K, **metal**       | **₹20,999 – ₹51,499** (26 cfg) |

**PassMark single‑number sanity check** (taken from the SkullSaints spec cards):
- Pulse 5205U → 1,433
- Agni / Ash / Rudra / Nebula (N150) → 5,800
- Helix i3-1215U → ~10,400
- CoreX 4500U → 10,709

### 1.2 Heavy Work (multi-tasking, mid-tier creators, light gaming)

| Model                          | CPU                                 | iGPU                | RAM (max)            | SSD (max)             | Notable I/O                       | Price range (INR)            |
|--------------------------------|-------------------------------------|---------------------|----------------------|-----------------------|-----------------------------------|------------------------------|
| **CoreX (Ryzen 7 4800H)**      | AMD Ryzen 7 4800H (8C/16T, 4.2 GHz) | Vega 7             | Dual DDR4 SODIMM, 64 GB | 2× M.2, 4 TB       | Wi-Fi 6E BT5.3, USB-C, triple 4K  | **₹27,999 – ₹58,499** (26 cfg) |
| **Dragon (Ryzen 5 5600U)**     | AMD Ryzen 5 5600U (6C/12T, 4.2 GHz) | Vega 7 (Cezanne)   | Dual DDR4 SODIMM 3200, 64 GB | NVMe + NGFF, 2 TB | RGB, triple 4K HDMI/DP/USB-C, TPM 2.0 | **₹27,999 – ₹44,999** (7 cfg)  |
| **CoreX (Ryzen 9 5900HX)**     | AMD Ryzen 9 5900HX (8C/16T, 4.6 GHz) | Vega 8            | Dual DDR4 SODIMM, 64 GB | 2× M.2, 4 TB       | Wi-Fi 6E BT5.3, USB-C, triple 4K  | **₹33,999 – ₹63,499** (26 cfg) |
| **Jupiter (Core Ultra 5 135H)** | Intel Core Ultra 5 135H (14C/18T, 4.6 GHz) | Arc + AI Boost NPU | Dual DDR5 SODIMM, 64 GB | 1× M.2 2280 PCIe 4.0, 4 TB | 1G LAN, dual display (HDMI + VGA), 8 USB | **₹47,999 – ₹104,999** (3 cfg) |

**PassMark:** Ryzen 7 4800H → 18,118 • Ryzen 9 5900HX → 22,226 • Core Ultra 5 135H → 22,126.

### 1.3 Extreme Power (creators, gaming + eGPU, AI)

| Model                                | CPU                                  | iGPU              | RAM (max)              | SSD (max)              | Notable I/O                                 | Price range (INR)         |
|--------------------------------------|--------------------------------------|-------------------|------------------------|------------------------|---------------------------------------------|---------------------------|
| **CoreX Pro (Ryzen 7 6800H)**        | AMD Ryzen 7 6800H (8C/16T, 4.7 GHz)  | Radeon 680M       | 24 GB LPDDR5 6400 (soldered) | 2× M.2, 4 TB     | 2.5G LAN, USB-C, **USB4 (eGPU/DP)**        | **₹41,999 – ₹61,999** (20 cfg) |
| **Fury-X (Ryzen 7 7840HS)**          | AMD Ryzen 7 7840HS (8C/16T, 5.1 GHz) | Radeon 780M (12C @ 2.7 GHz) | Dual DDR5-5600, 64 GB | 2× M.2 2280 PCIe 4.0, 8 TB | **OCuLink + USB4** (lossless eGPU), 2× 2.5G Intel i226, Wi-Fi 6E, 8K HDMI 2.1, 8K DP 2.1 | **₹46,999 – ₹94,999** (5 cfg)  |
| **Fury (Ryzen 7 7840HS)**            | AMD Ryzen 7 7840HS (8C/16T, 5.1 GHz) | Radeon 780M       | Dual DDR5-5600 SODIMM, 256 GB advertised (limited by SoC support) | 2× M.2 NVMe, 4 TB each | **USB4** (eGPU/DP), 2× 2.5G Intel i226     | **₹49,999 – ₹99,500** (7 cfg)  |
| **Jupiter (Core Ultra 7 155H)**      | Intel Core Ultra 7 155H (16C/22T, 4.8 GHz) | Arc + AI Boost NPU | Dual DDR5 SODIMM, 64 GB | 1× M.2 2280 PCIe 4.0, 4 TB | 1G LAN, dual display (HDMI + VGA), 8 USB | **₹53,999 – ₹107,999** (7 cfg) |
| **CoreX Pro Max (Ryzen 7 7840HS)**   | AMD Ryzen 7 7840HS (8C/16T, 5.1 GHz, 35–54 W) | Radeon 780M (2.7 GHz) | 32 GB LPDDR5 6400 (soldered) | 2× M.2 NVMe, 8 TB | **USB4 full-function**, 2.5G Realtek, **Quad display: 2× HDMI 2.0 + 2× USB-C**, **MRP ₹1,29,000** | **₹84,999 – ₹99,500** (5 cfg) |

**PassMark:** Ryzen 7 6800H → 22,962 • Ryzen 7 7840HS → 28,618 (CoreX Pro Max claims ~29,800) • Core Ultra 7 155H → 24,754.

### 1.4 NAS Mini PC

| Model      | CPU                  | RAM            | Storage                                   | Price       |
|------------|----------------------|----------------|-------------------------------------------|-------------|
| **Nebula** | Intel N150 (4C/4T)  | 12 GB LPDDR5 (soldered) | **1× M.2 NVMe/SATA + 3× M.2 NVMe (PCIe 3.0)**, up to 16 TB | **₹27,999** (1 cfg) |

Dual 2.5G Intel i226 LAN, USB-C PD, triple 4K display. Designed for soft-NAS / home server.

### 1.5 Industrial Fanless

| Model      | CPU                                      | RAM                  | Storage                                | Networking            | Price range (INR)            |
|------------|------------------------------------------|----------------------|----------------------------------------|-----------------------|------------------------------|
| **Onyx**   | Intel Celeron J6412 (4C/4T, 2.6 GHz)     | 2× DDR4 SODIMM 2666, 8 GB included (up to 32 GB) | 1× M.2 NVMe (256 GB inc., up to 2 TB) + 1× 2.5″ SATA | **4× 2.5G Intel i226**, Wi-Fi 6, BT 5.2 | **₹19,999 – ₹39,999** (7 cfg) |

Full-metal industrial enclosure, fanless (uses high-speed cooling fan add-on for warm climates), targeted at pfSense/OPNsense, edge compute and firewall use.

### 1.6 Legacy / older still-listed SKUs

| Model      | CPU                                      | Price (INR)             | Note                         |
|------------|------------------------------------------|-------------------------|------------------------------|
| **Rudra (Alder Lake N100/N5105)** | Intel N100 (4C/4T, 3.4 GHz) or N5105   | ₹22,999 (only "Sold Out" variants present) | Older Rudra cube design pre N150 refresh; 101 reviews. |
| **Titan (Ryzen 9 6900HX)**        | AMD Ryzen 9 6900HX (8C/16T, 4.9 GHz)   | ₹44,999 – ₹59,999 (Sold Out) | DDR5 4800 dual M.2, RGB; older "Titan" Gaming SKU (MRP ₹1,29,000). |

These are still on the catalog page but show as Sold Out at the moment of capture.

### 1.7 Accessories on the same site (not mini PCs)

- **ADT F43SG** — PCIe 5.0 x16 → M.2 NVMe / OCuLink eGPU adapter for laptops, NUC, ITX. Pairs with Fury‑X.
- **SkullSaints Mini PC Adapter** — 19V / 6.32A spare power brick.
- **High‑Speed Cooling Fan** for Onyx and other minis.

---

## 2. ElectroniksIndia mini PCs vs Apple Mac mini / Mac Studio (India)

### 2.1 Apple India lineup at a glance (May 2026)

| Apple SKU                                  | Chip            | CPU/GPU cores | RAM   | SSD     | India MRP (incl. GST) |
|--------------------------------------------|-----------------|---------------|-------|---------|-----------------------|
| Mac mini M4 (legacy entry, withdrawn from apple.com/in early 2026, still seen at resellers like ImagineOnline, India iStore) | Apple M4         | 10C / 10C     | 16 GB | 256 GB  | **₹59,900**           |
| Mac mini M4 (current entry on apple.com/in) | Apple M4         | 10C / 10C     | 16 GB | 512 GB  | **₹79,900**           |
| Mac mini M4 (24/512)                       | Apple M4         | 10C / 10C     | 24 GB | 512 GB  | **₹99,900**           |
| Mac mini M4 Pro (base)                     | Apple M4 Pro     | 12C / 16C     | 24 GB | 512 GB  | **₹1,49,900**         |
| Mac mini M4 Pro (higher tier)              | Apple M4 Pro     | 14C / 20C     | 48 GB | 512 GB  | **₹1,69,900**         |
| Mac Studio (M4 Max base)                   | Apple M4 Max     | 14C / 32C     | 36 GB | 512 GB  | **₹2,14,900**         |
| Mac Studio (M4 Max higher)                 | Apple M4 Max     | 16C / 40C     | 48 GB | 512 GB  | **₹2,84,900**         |
| Mac Studio (M3 Ultra base)                 | Apple M3 Ultra   | 28C / 60C     | 96 GB | 1 TB    | **₹4,29,900**         |
| Mac Studio (M3 Ultra higher)               | Apple M3 Ultra   | 32C / 80C     | 96 GB | 1 TB    | **₹5,79,900**         |

Apple India CTO maxes: Mac mini M4 Pro → 64 GB / 8 TB. Mac Studio M4 Max → 128 GB / 8 TB. Mac Studio M3 Ultra → 512 GB unified / 16 TB.

10G Ethernet add-on on Mac mini = +₹10,000.
AppleCare+ Mac mini = +₹9,900; AppleCare+ Mac Studio ≈ +₹14,900.

Sources: [apple.com/in/shop/buy-mac/mac-mini](https://www.apple.com/in/shop/buy-mac/mac-mini), [apple.com/in/shop/buy-mac/mac-studio](https://www.apple.com/in/shop/buy-mac/mac-studio), [pcquest article on the 256 GB withdrawal](https://www.pcquest.com/computers-laptops/the-mac-mini-m4s-best-india-deal-just-got-ghosted-by-apple-11797672), [fonearena launch coverage](https://www.fonearena.com/blog/439135/apple-mac-mini-2024-price-india-features.html), [indiatv article on Mac Studio launch](https://www.indiatvnews.com/technology/gadgets/apple-introduces-another-new-product-launches-refreshed-mac-studio-starting-at-rs-2-14-900-2025-03-06-979381).

### 2.2 Tier-by-tier comparison (single-thread / multi-thread benchmark anchors)

The Apple chips are far ahead on per-watt/perf per the public benchmarks; the SkullSaints minis are far ahead on raw rupees-per-core and on legacy I/O. Approximate Geekbench 6 / PassMark comparisons:

| Tier | Closest SkullSaints (price) | Closest Apple Mac (price) | Multi-thread anchor |
|------|------------------------------|----------------------------|----------------------|
| **Entry "office" (~₹15–35 K)**  | Pulse 5205U ₹12,999 (1,433 PassMark)<br>Agni N150 ₹18,999 (5,800)<br>CoreX R5 4500U ₹20,999 (10,709) | (no Apple SKU under ₹50 K)         | N150 ≈ 5,800 PM; M4 base ≈ 23,000 PM. Apple wins ~4× single‑thread, ~4× multi‑thread but at ~4× the price. |
| **Mid (~₹40–80 K)**             | CoreX Pro 6800H ₹41,999 (22,962)<br>CoreX 9 5900HX ₹33,999 (22,226)<br>Jupiter U5 135H ₹47,999 (22,126)<br>Fury-X 7840HS ₹46,999 (28,618) | Mac mini M4 16/512 **₹79,900** (PM ≈ 23 K equiv.; GB6 single ≈ 3,800 / multi ≈ 15 K) | A loaded SkullSaints in this tier costs **half** of a base Mac mini M4 and matches multi-thread, but the M4 wins single-thread, energy efficiency and OS ecosystem. |
| **High (~₹85 K – ₹1.1 L)**      | CoreX Pro Max 7840HS ₹84,999 – ₹99,500 (32 GB / up to 1 TB / Quad display)<br>Fury 7840HS ₹49,999 – ₹99,500<br>Jupiter U7 155H ₹53,999 – ₹1,07,999 | Mac mini M4 24/512 **₹99,900** | Apples-vs-X86: Apple gives you tighter unified memory, faster ST; SkullSaints gives you 2× the RAM and 8 TB ceiling for similar money. |
| **"Pro mini" (~₹1.5–2.0 L)**    | Nothing in the SkullSaints range matches a Mac mini M4 Pro on raw CPU; **Fury-X with eGPU dock** can exceed it on GPU. | Mac mini M4 Pro 24/512 **₹1,49,900**; 14C/20C 48/512 **₹1,69,900** | M4 Pro is ~1.5–2× the multi-thread of a 7840HS at ~2× the price. |
| **Workstation (~₹2 L+)**        | (none on this site — Fury-X with a 4070 eGPU is the ceiling here) | Mac Studio M4 Max ₹2,14,900 – ₹2,84,900<br>Mac Studio M3 Ultra ₹4,29,900 – ₹5,79,900 | Different category. Mac Studio is the only option in this segment from either vendor. |

### 2.3 Specific head‑to‑heads

#### A) ~₹80,000 spent on a 16 GB / 512 GB machine

| Specification        | **CoreX Pro 6800H 16 GB / 512 GB** (`₹49,999`) + Win 11 Pro | **Fury 7840HS 16 GB / 512 GB** (`₹68,999`) + Win 11 Pro | **Mac mini M4 16 GB / 512 GB** (`₹79,900`) |
|----------------------|-----------|-----------|-----------|
| CPU cores / threads  | 8 / 16 (Zen 3+) | 8 / 16 (Zen 4) | 10 (4P+6E) |
| Boost clock          | 4.7 GHz | 5.1 GHz | 4.4 GHz |
| iGPU                 | Radeon 680M (12 CU @ 2.2 GHz) | Radeon 780M (12 CU @ 2.7 GHz) | M4 GPU (10C, ~4.6 TFLOPs) |
| RAM type/speed       | LPDDR5 6400 (soldered) | DDR5-5600 SODIMM, expandable to 64 GB | LPDDR5X-7500 unified, soldered |
| Max RAM / SSD        | 24 GB / 4 TB | 64 GB / 8 TB | 32 GB / 2 TB (Apple CTO) |
| Networking           | 1 × 2.5G + Wi-Fi 6E | **2 × 2.5G** Intel i226 + Wi-Fi 6E | 1 × 1G (10G +₹10K) + Wi-Fi 6E |
| Display              | Triple 4K (HDMI×2 + USB-C) | Triple 4K (HDMI + DP + USB4) | 3 displays @ 6K/4K via TB4 + HDMI 2.1 |
| eGPU                 | USB4 | **USB4** | TB4 (limited driver support) |
| Volume               | ~0.51 L (114×106×42.5) | ~0.85 L (136×123×51) | 0.78 L (127×127×50) |
| Warranty             | 15 months (12 + 3 mo) | 15 months | 1 year (AppleCare+ ₹9,900 extra) |
| OS                   | Windows 11 Pro / Linux | Windows 11 Pro / Linux | macOS |
| **Verdict**          | Cheapest, very capable | Best PC value, future-proof RAM | Best ST perf & macOS, but RAM cap & 1 G LAN |

#### B) ~₹1,00,000 spent on 24–32 GB / 512 GB–1 TB

| Spec | **CoreX Pro Max 32 GB / 512 GB** (`₹92,999`) | **Jupiter Ultra 7 155H 32 GB / 512 GB** (`₹99,999`) | **Mac mini M4 24 GB / 512 GB** (`₹99,900`) |
|------|-----------|-----------|-----------|
| CPU  | Ryzen 7 7840HS, 8C/16T, 5.1 GHz | Core Ultra 7 155H, 16C/22T, 4.8 GHz | M4, 10C (4P+6E), 4.4 GHz |
| iGPU | Radeon 780M (12 CU @ 2.7 GHz) | Intel Arc Graphics + AI Boost NPU | M4 GPU 10C |
| AI / NPU | None on chip; can run llama.cpp on CPU+iGPU | Intel AI Boost NPU (~11 TOPS) | Apple Neural Engine 16C (~38 TOPS) |
| RAM cap | 32 GB soldered | 64 GB SODIMM | 32 GB unified (CTO) |
| Storage | 2 × M.2 NVMe up to 8 TB | 1 × M.2 PCIe 4.0 up to 4 TB | up to 2 TB (Apple SSD) |
| Display | **Quad** 4K (2 HDMI + 2 USB-C) | Dual (HDMI + VGA — weak point) | 3 displays via TB |
| Networking | 2.5G LAN, Wi-Fi 6 | 1G LAN (weak), Wi-Fi 6 | 1G LAN, Wi-Fi 6E |
| Power draw | 35–54 W typical | 28–65 W | ~5–35 W |
| **Verdict** | Best for storage & display fan-out | Most cores & NPU for ₹1L | Best perf/W and best ST CPU |

#### C) Workstation tier — Fury-X eGPU vs Mac mini M4 Pro

| Spec | **Fury-X 32/1TB + 4070 eGPU stack** (~₹94,999 + ₹85K eGPU + ₹65K GPU ≈ **₹2.4 L**) | **Mac mini M4 Pro (14C/20C, 48 GB, 512 GB)** `₹1,69,900` | **Mac Studio M4 Max base** `₹2,14,900` |
|------|-----------|-----------|-----------|
| CPU  | Ryzen 7 7840HS, 8C/16T | M4 Pro 14C (10P+4E) | M4 Max 14C (10P+4E, faster boost) |
| GPU  | Discrete RTX 4070 (eGPU) | M4 Pro 20C GPU (~7 TFLOPs) | M4 Max 32C GPU (~14 TFLOPs) |
| RAM  | 32 GB DDR5 SODIMM | 48 GB unified | 36 GB unified (max 128) |
| Storage | up to 8 TB | up to 8 TB | up to 8 TB |
| Networking | 2× 2.5G Intel i226 | 1G (10G +₹10K) | **10G standard** |
| Use cases | Gaming, CUDA / NVIDIA AI workloads | macOS pro, video editing, code | macOS heavy, ML, video |
| **Verdict** | Only viable path to NVIDIA on a mini-PC budget; awkward stack | Tightest small workstation if you're macOS | Best raw "small workstation" |

### 2.4 What you simply cannot get from SkullSaints

- **CUDA‑class GPU built in** — Apple Silicon GPUs (≈14 TFLOPs FP32 on M4 Max, plus 38–66 TOPS Neural Engine), or NVIDIA via PCIe. Mini PCs route around this with USB4/OCuLink eGPU docks, but those add ₹15K–₹25K for the dock + GPU price.
- **macOS** and the Apple ecosystem (Logic, Final Cut, Xcode, Continuity).
- **Unified memory bandwidth** (~120 GB/s on M4 base, 273 GB/s on M4 Pro, 546 GB/s on M4 Max, 1090 GB/s on M3 Ultra). The DDR5 SODIMM minis get ~80 GB/s.
- **10 GbE standard** (Mac Studio).

### 2.5 What SkullSaints gives you that Apple does not

- **Bare-bones SKUs** (₹46,999 Fury-X without RAM/SSD, ₹84,999 CoreX Pro Max similar) — use your own kit.
- **Quad-LAN industrial soft-router** (Onyx, ₹19,999 starting): 4× 2.5G Intel i226. There is no Apple equivalent at any price.
- **Multi-bay NAS form-factor** (Nebula, ₹27,999): 4× M.2 NVMe slots and dual 2.5G LAN, total 16 TB raw NVMe in a box smaller than a Mac mini.
- **OCuLink eGPU port** (Fury-X, ₹46,999+) — no overhead, lossless link for an external GPU.
- **2.5G or dual 2.5G LAN** as standard on most Heavy/Extreme SKUs.
- **Triple/Quad display from one box** (CoreX Pro Max 4 outputs).
- **Linux first‑class support** and Windows 11 Pro included on most non‑barebone SKUs.
- **15‑month warranty + free pickup‑and‑replace** (3 months longer than Amazon's 12‑mo).

---

## 3. ElectroniksIndia vs Intel/AMD competitors in India

> Full machine‑readable competitor table: `data/competitor_minipcs.json`.
> Prices below are India INR list prices captured 14 May 2026. Most domestic prices come from authorised distributors (NationalPC for ASUS NUC, Nakhwa International for Beelink) and IndiaMART listings, since Amazon.in heavily throttles scraping.

### 3.1 Competitor matrix — what's actually stocked in India

#### ASUS NUC (most consistent local distribution; sold by NationalPC and PrimeABGB)

| Model                       | CPU                          | RAM   | SSD     | INR price | Source                    |
|-----------------------------|------------------------------|-------|---------|-----------|---------------------------|
| ASUS NUC 14 Essential       | Intel N150                   | 16 GB | 512 GB  | **₹14,200** | primeabgb.com             |
| Intel NUC 11 Pro            | Core i3-1115G4               | 16 GB | 128 GB  | ₹43,430   | nationalpc.in             |
| Intel NUC 13 Pro            | Core i3-1315U                | 8 GB  | 480 GB  | ₹44,999   | primeabgb.com             |
| ASUS NUC 15 Pro C5-210H (barebone) | Core Ultra Series 2   | 0     | 0       | ₹46,999   | primeabgb.com             |
| ASUS NUC 14 Pro NUC14RVHU5 (kit)   | Core Ultra 5 125H     | 8 GB  | 128 GB  | ₹61,940   | nationalpc.in             |
| ASUS NUC 15 Pro C7-240H (barebone) | Core Ultra Series 2   | 0     | 0       | ₹61,799   | primeabgb.com             |
| ASUS NUC 14 Pro+ NUC14RVSU7 (barebone) | Core Ultra 7 155H | 0     | 0       | ₹60,599   | primeabgb.com             |
| ASUS NUC 13 Pro NUC13ANHH7  | Core i7-13620H               | 8 GB  | 128 GB  | ₹69,630   | nationalpc.in             |
| ASUS NUC 14 Pro NUC14RVHU5  | Core Ultra 5 125H            | 16 GB | 128 GB  | ₹75,940   | nationalpc.in             |
| ASUS NUC 14 Pro+ NUC14RVSU5 | Core Ultra 5 125H            | 16 GB | 256 GB  | ₹80,990   | nationalpc.in             |
| ASUS NUC 14 Pro+ NUC14RVSU9 (barebone) | Core Ultra 9 185H | 0     | 0       | ₹84,429   | primeabgb.com             |
| ASUS NUC 14 Pro NUC14RVHU7  | Core Ultra 7 155H            | 8 GB  | 128 GB  | ₹85,580   | nationalpc.in             |
| ASUS NUC 14 Pro NUC14RVHU7  | Core Ultra 7 155H            | 16 GB | 128 GB  | ₹91,530   | nationalpc.in             |
| ASUS NUC 14 Pro+ NUC14RVSU7 | Core Ultra 7 155H            | 16 GB | 256 GB  | ₹98,990   | nationalpc.in             |
| ASUS NUC 14 Pro NUC14RVHU7  | Core Ultra 7 155H            | 32 GB | 1 TB    | **₹1,27,970** | nationalpc.in (incl GST)  |
| ASUS NUC 14 Pro+ NUC14RVSU9 | Core Ultra 9 185H            | 16 GB | 256 GB  | ₹1,31,990 | nationalpc.in             |
| ASUS NUC 14 Pro+ NUC14RVSU9 | Core Ultra 9 185H            | 48 GB | 2 TB    | ₹1,81,780 | nationalpc.in             |
| Intel NUC 12 Extreme NUC12DCMi9 | Core i9-12900            | 32 GB | 1 TB    | ₹2,22,222 | primeabgb.com             |
| ASUS ROG NUC 2025           | Core Ultra 9 275HX + RTX 5070 | 64 GB | 2 TB   | **₹4,39,980** | nationalpc.in             |

#### Beelink (Nakhwa International / IndiaMART are most reliable)

| Model               | CPU                              | RAM   | SSD       | INR price |
|---------------------|----------------------------------|-------|-----------|-----------|
| Mini S12 (entry)    | Intel N95                        | 8 GB  | 256 GB    | ₹13,999 – ₹17,690 |
| Mini S12 Pro        | Intel N100                       | 16 GB | 500 GB    | **₹24,960** (Nakhwa)   |
| EQ12 Pro            | Intel Core i3-N305               | 16 GB | 500 GB    | ₹39,640   |
| SER6 Max            | AMD Ryzen 7 7735HS               | 32 GB | 1 TB      | ₹59,400   |
| SER8                | AMD Ryzen 7 8745HS / 8845HS      | 32 GB | 1 TB      | **₹78,430** |
| GTR7                | AMD Ryzen 7 7840HS               | 32 GB | 1 TB      | ₹79,640   |
| SEi14               | Intel Core Ultra 5 125H          | 32 GB | 1 TB      | ₹83,950   |
| GTi14 Ultra         | Intel Core Ultra 7 155H          | 32 GB | 1 TB      | **₹1,09,730** |
| SER9 / SER9 Pro     | Ryzen AI 9 HX 370                | 32 GB | 1 TB      | (no domestic price; ~₹1,30,000–₹1,55,000 imported via Ubuy) |
| GTi15               | Core Ultra 9 285H                | 64 GB | 1 TB      | (imports only, US $1,499)   |

#### Geekom (almost entirely Amazon India / Ubuy)

| Model           | CPU                       | RAM   | SSD     | INR price                          |
|-----------------|---------------------------|-------|---------|------------------------------------|
| Air12           | Intel N100/N150           | 16 GB | 512 GB  | ~₹22–25 K (Amazon listing, throttled) |
| AS6             | AMD Ryzen 7 7735H         | 32 GB | 1 TB    | (Amazon listing, price unscraped)  |
| Mini IT12       | Intel i7-12xxx / R7 7735H | 32 GB | 1 TB    | (Amazon listing, price unscraped)  |
| A8              | AMD Ryzen 9 8945HS        | 32 GB | 2 TB    | ~₹65–80 K expected (US $722 comp)  |
| A8 Max          | AMD Ryzen 9 8945HS        | 32 GB | 2 TB    | ~₹90–110 K expected (US $1,019 comp) |
| **AX8 Pro**     | AMD Ryzen 9 8945HS        | 32 GB | 2 TB    | **₹80,000** (firm; Devi Enterprises Ahmedabad / Amazon B0D25Q94Q7) |
| IT13 (i9-13900H), IT15 (Ultra 9 285H) | (varies)    | (varies) | (varies) | Imports only via Ubuy             |

#### Minisforum (mostly Amazon India / IndiaMART; UM/MS-A series imports only)

| Model            | CPU                              | RAM   | SSD     | INR price                          |
|------------------|----------------------------------|-------|---------|------------------------------------|
| EM680 (Mercury)  | AMD Ryzen 7 6800U                | 32 GB | 512 GB  | ~₹65–75 K (Amazon listing, throttled) |
| UM890 Pro        | AMD Ryzen 9 8945HS               | 32–64 GB | 1 TB | Amazon listing (US $463 sale comp) |
| **AI X1 Pro**    | Ryzen AI 9 HX 370                | 64 GB | 1 TB    | **₹1,49,000** (Pune IndiaMART seller) |
| MS-A1 (barebone) | AM5 socket                       | 0     | 0       | Amazon listing                     |
| MS-A2            | Ryzen 9 9955HX                   | 64 GB | 1 TB    | Imports only (US $839–$1,103)      |
| TH50 (legacy)    | Core i5-11320H (barebone)        | 0     | 0       | ₹80,407                            |

### 3.2 Direct head‑to‑heads against SkullSaints SKUs

#### Office tier — N100/N150/N95 mini PCs (₹14 K – ₹25 K)

| | **SkullSaints Pulse 5205U** | **SkullSaints Agni N150** | **ASUS NUC 14 Essential N150** | **Beelink Mini S12 Pro N100** |
|---|---|---|---|---|
| Min price (INR) | ₹12,999 (barebone) | ₹18,999 (barebone) | **₹14,200** (16/512) | ₹24,960 (16/500) |
| CPU | Celeron 5205U 2C/2T | N150 4C/4T | N150 4C/4T | N100 4C/4T |
| PassMark | 1,433 | 5,800 | 5,800 | ≈5,500 |
| Memory | DDR4 SODIMM (replace) | DDR4 SODIMM (replace) | LPDDR5 (soldered, 16 GB) | DDR4 SODIMM (replace) |
| Networking | 2.5G LAN, Wi-Fi 5 | 2× 1G LAN, Wi-Fi 6 | 1G LAN, Wi-Fi 6E | 2× 2.5G LAN, Wi-Fi 6 |
| OS | No OS by default | Win 11 Pro on most variants | No OS | Win 11 Pro |
| Verdict | Cheapest possible | LCD + dual LAN gimmick | **Best value office mini** when stock available | Most polished but nearly 2× the NUC |

> The ASUS NUC 14 Essential at ₹14,200 with 16 GB / 512 GB / Win 11 (Pro tier with academic licensing) is the elephant in the room: **none** of the SkullSaints office SKUs match it on price for that exact spec — Pulse beats it on price only as a 0/0 barebone.

#### "Heavy work" — Ryzen 7000 / Core Ultra mid‑range (₹50 K – ₹85 K)

| | **CoreX Pro 6800H 24/512** | **Beelink SER8 R7 8745HS 32/1TB** | **Beelink GTR7 R7 7840HS 32/1TB** | **Beelink SEi14 Ultra 5 125H 32/1TB** |
|---|---|---|---|---|
| Price (INR) | **₹49,999** | ₹78,430 | ₹79,640 | ₹83,950 |
| CPU | R7 6800H, 8C/16T | R7 8745HS, 8C/16T | R7 7840HS, 8C/16T | Core Ultra 5 125H, 14C/18T |
| RAM (max) | 24 GB LPDDR5 6400 (soldered) | 32 GB DDR5 SODIMM (~96 GB cap) | 32 GB DDR5 SODIMM (~96 GB cap) | 32 GB DDR5 SODIMM |
| SSD (default) | 512 GB | 1 TB | 1 TB | 1 TB |
| Display | Triple 4K HDMI×2 + USB4 | Triple 4K HDMI/DP/USB4 | Triple 4K HDMI/DP/USB4 | Triple 4K |
| Networking | 2.5G | 2.5G | 2.5G | 2.5G |
| Warranty | 15 mo + free pickup | 1 yr (12 mo Amazon) | 1 yr | 1 yr |
| Verdict | **Cheapest** for a USB4 8‑core; older 6800H | Best value for a current Zen 4 8C w/ DDR5 | Last-gen 7840HS but 1 TB, Wi-Fi 7 | Pricier; AI NPU + more cores |

#### "Extreme power" — flagship 7840HS/Ultra 7 (₹85 K – ₹1.30 L)

| | **CoreX Pro Max 32/1TB** | **Fury 7840HS 32/1TB (price-equivalent)** | **ASUS NUC 14 Pro 32/1TB Ultra 7** | **Beelink GTi14 Ultra 7 155H 32/1TB** | **Mac mini M4 16/512** |
|---|---|---|---|---|---|
| Price (INR) | **₹99,500** | ₹84,499 (configured) | **₹1,27,970** | ₹1,09,730 | ₹79,900 |
| CPU | R7 7840HS 8C/16T 5.1 GHz | R7 7840HS 8C/16T | Core Ultra 7 155H 16C/22T | Core Ultra 7 155H 16C/22T | M4 10C |
| iGPU / NPU | Radeon 780M (12CU @ 2.7 GHz) | Radeon 780M | Arc + AI Boost NPU (~11 TOPS) | Arc + AI Boost NPU | Apple GPU 10C + Neural Engine 16C (~38 TOPS) |
| RAM | 32 GB LPDDR5 6400 | 32 GB DDR5 SODIMM (expandable to 64) | 32 GB DDR5 SODIMM | 32 GB DDR5 SODIMM | 16 GB LPDDR5X unified |
| SSD | up to 1 TB (slot for second) | up to 1 TB (slot for second) | 1 TB | 1 TB | 512 GB |
| Networking | 2.5G | **2× 2.5G** Intel i226 | 2.5G + Wi-Fi 6E + 2× TB4 | 2.5G + Wi-Fi 6 | 1G (10G +₹10K) + Wi-Fi 6E |
| Display | **Quad 4K (2 HDMI + 2 USB-C)** | Triple 4K + USB4 | 4 displays via TB4/HDMI | Triple 4K | 3 displays via TB |
| Warranty | 15 mo, free pickup | 15 mo, free pickup | 3 years (ASUS NUC) | 1 year | 1 year |
| **Verdict** | Best display fan-out + 8 TB ceiling, but RAM ceiling 32 GB | Cheapest path to 7840HS + dual 2.5G, expandable RAM | Most polished + 3-yr warranty, but 30% pricier than CoreX Pro Max | Premium Intel pick, fastest NPU on Win | Best ST CPU + NPU, but 1G LAN and 16 GB cap |

#### "Pro / workstation" tier (₹1.5 L+)

| | **Mac mini M4 Pro 12C/24/512** | **Mac mini M4 Pro 14C/48/512** | **ASUS NUC 14 Pro+ Ultra 9 48/2TB** | **Minisforum AI X1 Pro HX 370 64/1TB** | **Mac Studio M4 Max 14C/36/512** |
|---|---|---|---|---|---|
| Price (INR) | **₹1,49,900** | ₹1,69,900 | ₹1,81,780 | ₹1,49,000 | ₹2,14,900 |
| CPU | M4 Pro 12C | M4 Pro 14C | Core Ultra 9 185H 16C/22T | Ryzen AI 9 HX 370 12C/24T | M4 Max 14C |
| GPU | M4 Pro 16C (~7 TFLOPs) | M4 Pro 20C | Arc | Radeon 880M | M4 Max 32C (~14 TFLOPs) |
| AI / NPU | Apple Neural Engine 16C (38 TOPS) | Same | Intel AI Boost (~11 TOPS) | XDNA 2 NPU (~50 TOPS, AMD spec) | Apple Neural Engine 16C |
| RAM | 24 GB unified | 48 GB unified | 48 GB DDR5 | 64 GB | 36 GB unified |
| SSD | 512 GB | 512 GB | 2 TB | 1 TB | 512 GB |
| Networking | 1G (10G +₹10K) | same | 2× 2.5G + 2× TB4 | 2.5G + USB4 | **10G standard** + TB5 |
| Verdict | Best macOS small workstation | Same, more cores + RAM | Best Win pro workstation in a NUC | **Highest TOPS for Win on a budget**, AMD AI on a mini | Best raw compute in this band |

#### Workstation / "max it out" (₹4 L+)

| | **ASUS ROG NUC 2025 (RTX 5070)** | **Mac Studio M3 Ultra 28C/96/1TB** | **Mac Studio M3 Ultra 32C/96/1TB** |
|---|---|---|---|
| Price (INR) | ₹4,39,980 | ₹4,29,900 | ₹5,79,900 |
| CPU | Core Ultra 9 275HX 24C/24T | M3 Ultra 28C | M3 Ultra 32C |
| GPU | **NVIDIA RTX 5070 (Blackwell)** | M3 Ultra 60C (~21 TFLOPs) | M3 Ultra 80C (~28 TFLOPs) |
| RAM | 64 GB DDR5 (replaceable) | 96 GB unified (max 512 GB CTO) | same |
| SSD | 2 TB | 1 TB (max 16 TB CTO) | 1 TB |
| Networking | 2.5G + Wi-Fi 7 | 10G + TB5 | 10G + TB5 |
| Verdict | Best for **CUDA / NVIDIA‑only** workloads (LLMs in CUDA, gaming) | Best for **macOS workloads** that benefit from huge unified memory (LLMs in MLX, Final Cut, Logic) | Same with more GPU cores |

### 3.3 Cost‑per‑PassMark CPU score (Heavy / Extreme tier only)

A rough "rupees‑per‑1000 PassMark" for the *fully configured* (16 GB+ RAM, 512 GB+ SSD, OS) cheapest variant:

| Model | Variant priced | PassMark CPU | ₹ / 1k PM |
|-------|----------------|--------------|-----------|
| SkullSaints CoreX 5900HX 16/512 | ₹40,499 | 22,226 | **1,822** |
| SkullSaints CoreX Pro 6800H 16/512 | ₹49,999 | 22,962 | **2,177** |
| SkullSaints Fury-X 7840HS 16/512 | ₹65,999 | 28,618 | **2,306** |
| SkullSaints Fury 7840HS 16/512 | ₹68,999 | 28,618 | 2,411 |
| Beelink SER8 R7 8745HS 32/1TB | ₹78,430 | ~31,000 | **2,530** |
| SkullSaints CoreX Pro Max 32/512 | ₹92,999 | 29,800 | 3,121 |
| SkullSaints Jupiter U7 155H 32/512 | ₹99,999 | 24,754 | 4,040 |
| ASUS NUC 14 Pro U7 32/1TB | ₹1,27,970 | 24,754 | 5,170 |
| Beelink GTi14 Ultra 7 32/1TB | ₹1,09,730 | 24,754 | 4,433 |
| Mac mini M4 16/512 | ₹79,900 | (M4 ≈ 22,000–23,000 PM equiv.) | 3,541 |
| Mac mini M4 Pro 24/512 | ₹1,49,900 | (M4 Pro ≈ 35,000–37,000 PM equiv.) | 4,164 |

**Reading:** SkullSaints (especially the CoreX 5900HX and CoreX Pro 6800H) win the rupees‑per‑PassMark contest by ~30‑60% versus the established competitors at every tier below the Mac mini M4 Pro — but they trade off on warranty, network‑port quality, single‑thread performance, and macOS / NVIDIA compatibility.

### 3.4 What each vendor uniquely owns in India

- **Cheapest entry mini PC with OS** → ASUS NUC 14 Essential N150 16/512 at ₹14,200 (no SkullSaints SKU undercuts that with the same spec).
- **Cheapest 8‑core / 16‑thread Zen mini PC** → SkullSaints **CoreX Pro 6800H** at ₹41,999.
- **Cheapest USB4 + dual 2.5G LAN mini PC** → SkullSaints **Fury** 7840HS at ₹49,999 barebone / ₹68,999 16/512.
- **Cheapest mini PC with OCuLink eGPU port** → SkullSaints **Fury‑X** 7840HS at ₹46,999 barebone.
- **Cheapest quad-2.5G LAN box** → SkullSaints **Onyx J6412** at ₹19,999 (no comparable competitor SKU at any price).
- **Cheapest soft‑NAS mini with 4× M.2 NVMe** → SkullSaints **Nebula** N150 at ₹27,999.
- **Cheapest mini PC with NPU (any vendor)** → Jupiter Ultra 5 135H at ₹47,999, or Mac mini M4 16/512 at ₹79,900 (Apple has the highest TOPS NPU).
- **Cheapest mini PC with discrete NVIDIA GPU** → ASUS ROG NUC 2025 (RTX 5070) at ₹4,39,980 — no Apple or SkullSaints alternative.
- **Best-in-class small workstation** → Mac Studio M3 Ultra (₹4,29,900–₹5,79,900) — no competitor SKU matches the unified memory bandwidth or 16 TB SSD ceiling.
- **Cheapest macOS** → Mac mini M4 16/512 at ₹79,900 (only macOS option below the Mac Studio).

### 3.5 Caveats & data quality

- **Amazon India scraping is unreliable**. Several Geekom, Beelink and Minisforum SKUs are stocked but Amazon's anti‑bot defences blocked us from capturing today's INR price; we noted ASIN + expected price band where possible.
- **Imports vs domestic stock matter a lot.** Beelink SER9 / GTi15, all Geekom IT13/IT15, and Minisforum MS-A2 / UM870 are sold in India almost only via Ubuy.co.in cross-border — expect 25–40% over US MSRP plus customs delays.
- Authorized distributor pricing (NationalPC for ASUS NUC, Nakhwa International for Beelink) is what we treat as the "real" India price.
- **SkullSaints' "MRP"** numbers (₹99,999 / ₹1,29,000 you'll see crossed out) are aspirational — the cart prices are what most buyers actually pay, and they're already discounted further by 10% via the storefront banner promo.

---

## 4. How to read the configuration tables (`data/minipc_configs.csv`)

Each row is one configuration on the storefront:

| Column | Meaning |
|--------|---------|
| `site_category`            | The SkullSaints‑defined category (Daily Tasks / Heavy Work / Extreme Power / NAS / Industrial / Legacy). |
| `model`                    | Friendly model name (e.g. `Fury-X (AMD Ryzen 7 7840HS, OCuLink)`). |
| `cpu`                      | CPU as listed in the spec card on the product page. |
| `ram_spec` / `storage_spec`| The default RAM / storage profile from the spec card. |
| `configuration`            | The exact variant title, e.g. `Black / 16GB DDR5-6400 / 512GB M.2 NVMe + Win 11 Pro`. |
| `price_inr`                | The variant's current page price in INR. |
| `compare_at_price_inr`     | The crossed-out MRP if shown. |
| `discount_pct`             | (compare - price) / compare × 100, rounded to integer. |
| `url`                      | The product page on electroniksindia.com. |
| `handle`                   | The Shopify handle (URL slug). |

A few highlights:

- The **Pulse 5205U** at **₹12,999** is the cheapest mini PC on the site (barebone). Even fully kitted (16 GB / 512 GB) it tops out at ₹17,999 — interesting only as a thin client / DOS/Linux router.
- **Mist Ryzen 3 4300U** at **₹18,999 barebone / ₹35,999 16 GB+512 GB+Win** is the price/performance sweet spot for office work.
- **CoreX Ryzen 5 4500U** has 26 variants spanning **₹20,999 → ₹51,499** purely from RAM (0/8/16/32) × SSD (0/128/256/512/1TB) × colour (Black/Silver). Same chassis is reused for the 4800H and 5900HX SKUs.
- **CoreX Pro 6800H** (24 GB LPDDR5 6400 soldered, USB4) goes from **₹41,999** to **₹61,999** — the value pick of the Extreme tier.
- **CoreX Pro Max 7840HS** is the flagship: only RAM is fixed at 32 GB; storage scales 0 → 1 TB at **₹84,999 → ₹99,500**, with MRP **₹1,29,000**.
- **Fury-X 7840HS** is the only mini in this catalog with a real **OCuLink** port — a meaningful differentiator vs every Apple machine.

---

## 5. Reproducing this data

```bash
# 1. Fetch all 167 storefront products + product pages
python3 electronics-scraper/scripts/01_fetch_all.py

# 2. Parse the 20 mini PC SKUs into JSON + CSV
python3 electronics-scraper/scripts/02_parse_minipc.py
```

Outputs land in `electronics-scraper/data/`. Re-running `01_fetch_all.py` is idempotent — it skips files already on disk.

