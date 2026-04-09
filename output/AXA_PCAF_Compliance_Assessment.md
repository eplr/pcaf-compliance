# AXA — PCAF® Compliance Assessment

> **Report analysed**: AXA Universal Registration Document 2024 (PDF, 5 717 lines of extracted text)
> **Institution type**: Insurer (Part A + Part C applicable — Part B N/A)
> **Assessment date**: 9 April 2026
> **Methodology**: PCAF Compliance Methodology V3.1 (April 2026)
> **Reading method**: Full report reading. Key sections read in full: investment GHG methodology (L1861–1875, L2542–2560), financed emissions tables (L1866–1875), IAE targets and table (L2025–2033, L2584–2587), signatory confirmation (L1809, L2586).

---

## Part A — Financed Emissions: 10/23

### 1. Asset Class Coverage — 1/5

Raw score: 4.5/18 = 25.0% → Level 1 (0% < rate ≤ 40%)

AXA calculates GHG emissions for: **listed corporate debt & equities** (EVIC-based S1&S2), **sovereign debt** (PPP-GDP, S1 production), **real estate equity** (GAV-based), and **private assets** (infrastructure, CLOs, private debt — carbon intensity only, 2024 expansion). Mortgages and private equity are explicitly excluded from financed emissions (L1875).

| Asset class | Status | Points | Justification |
|---|---|---|---|
| Listed equity & corporate bonds | partial | 3.0/6.0 (S1&S2 only) | L1867–1868: listed corporate debt €165bn (87% coverage), 4,139 ktCO₂e; listed equities €28bn (93% coverage), 292 ktCO₂e. L2542: *"Scope 3 emissions are not taken into account by the calculation of carbon intensity."* S3 not reported. Status `partial` → 3/6 pts. |
| Business loans & unlisted equity | missing | 0.0/6.0 | L1875: *"AXA seeks to address operational limitations that prevent it from disclosing sufficiently comprehensive [...] emissions financed from [...] private equity instruments and mortgage loans."* Private equity explicitly excluded. Private debt partially covered in “private assets” (L1863) but no PCAF attribution methodology referenced. |
| Project finance | missing | 0.0/2.0 | Not identified as a separate PCAF category. Infrastructure included in “private assets” for carbon intensity only (L1861, L1869); no PCAF project finance methodology referenced. |
| Commercial real estate | reported | 1.0/1.0 (S1&S2) | L1867–1868: real estate equity covered (carbon intensity by GAV — L1863 footnote 3). L1872–1873: RE equity financed emissions 228 ktCO₂e (2024). L2548–2552: methodology covers landlord and tenant S1, S2 emissions via ownership share. Coverage 86.9% of in-scope RE assets (L1863 fn.3). Max = 1 pt. |
| Mortgages | missing | 0.0/0.5 | L1875: *"AXA seeks to address operational limitations that prevent it from disclosing sufficiently comprehensive and reliable information on emissions financed from [...] mortgage loans in General Account assets. These asset classes are not currently included in financed emissions."* |
| Motor vehicle loans | missing | 0.0/0.5 | Not identified as a financed emissions asset class. |
| Sovereign debt | partial | 0.5/2.0 (S1 production only) | L1863–1869: sovereign debt €127bn, 100% coverage, 19,001 ktCO₂e. L2553: *"the carbon intensity of AXA Group's proprietary sovereign assets is the production emissions (tCO2e) per Purchase Power Parity (PPP) - adjusted GDP."* L2553 fn.2: based on PCAF standard using *"Scope 1 GHG emissions i.e. domestic production emissions as defined by UNFCCC."* **LULUCF**: not separately reported (no incl./excl. LULUCF table found). **S3**: not included. → 0.5/2.0 pts (S1 production only). |

**Raw score**: 3.0 + 0.0 + 0.0 + 1.0 + 0.0 + 0.0 + 0.5 = **4.5/18 = 25.0%** → Level **1/5**

---

### 2. Data Quality Score — 0/5

No aggregate PCAF DQS is disclosed for Part A (financed investments). The DQS values found in the report (3.00, 4.50, 3.70 — L2032–2033) are for Part C (IAE). The auto-generated assessment incorrectly extracted these as Part A DQS.

For the investment methodology, AXA uses EVIC-based data from third-party providers (ISS, Trucost — L2562), which typically corresponds to DQS 2–3, but no explicit weighted average DQS is disclosed for the financed emissions portfolio. Per V3 rule → **Score 0/5**.

---

### 3. Attribution Methodology — 3/5

| Source | Verbatim |
|---|---|
| L1809 | *"AXA refers to [...] the Partnership for Carbon Accounting Financials ('PCAF') for the calculation of its underwriting and investment carbon footprint."* |
| L1863 fn.5 | *"It is based on the current version of the PCAF's Global GHG Accounting and Reporting Standard and using the Scope 1 GHG emissions i.e. domestic production emissions as defined by UNFCCC."* (sovereign debt) |
| L1861 | *"AXA is aiming to be in a position to measure the carbon intensity of its entire General Account by 2030, assuming the PCAF and NZAOA standards are available."* |
| L2542–2548 | Detailed methodology: EVIC for listed corporates, GAV for real estate, PPP-GDP for sovereign — all PCAF-aligned attribution approaches. |

PCAF methodology applied per asset class (EVIC, GAV, PPP-GDP). PCAF standard referenced for sovereign. No explicit PCAF signatory statement found; language is *"refers to"* rather than *"complies with"* or *"is a signatory of."* Primary metric is **carbon intensity** (not PCAF absolute financed emissions). S3 and LULUCF not covered. → **Score 3/5**.

---

### 4. Portfolio Coverage — 3/5

Coverage: **72%** of General Account assets covered by a GHG measurement methodology (L1863).

| Source | Verbatim / Data |
|---|---|
| L1861–1863 | *"As of December 31, 2024, 72% of the General Account's asset classes were covered by a GHG emissions measurement methodology."* AXA's General Account: €465bn (2024) — covered: **72%** |
| L1863 | *"The majority of unaccounted assets are sub-sovereign debt, mortgages, cash, and private equity."* |
| L1863 fn.3 | *"the carbon intensity coverage rate stands at 86.9% of the in-scope assets"* ← **Real estate equity only** (not overall portfolio) |

**Contextual check (V3 rule)**: The 86.9% cited in the V3 audit is specifically the coverage rate for **real estate equity in-scope assets** (L1863 footnote 3), not the overall portfolio. The correct PCAF portfolio coverage is **72%** (L1863, “GenAccount” row: 72% GHG measurement coverage). The 24% at L2026 was the IAE in-scope commercial premium share — a completely different metric. → 72% → range 60–80% → **Score 3/5**.

---

### 5. Temporal Coverage — 3/3

| Source | Data |
|---|---|
| L1866–1869 | Carbon intensity: 2024 = 32 tCO₂/€m; 2023 = 33; 2019 = 65 |
| L1872–1875 | Financed emissions: listed corporates 2024 = 4,660 ktCO₂e; 2023 = 4,620; 2019 = 11,712. Sovereign: 2024 = 19,001; 2023 = 20,832 (restated). |
| L1838 | NZAOA member since 2019; 2025 intermediate target and 2030 target (-50% carbon intensity) |

Three data points: 2019 (baseline) + 2023 + 2024, plus 2030 target. → **Score 3/3**.

---

## Part B — Facilitated Emissions: N/A

AXA is an insurer. Part B applies to banks and bancassurances only. Not applicable.

---

## Part C — Insurance-Associated Emissions: 7/13

### 1. Asset Class Coverage — 3/5

Raw score: 5.0/8 = 62.5% → Level 3 (50% ≤ rate < 70%)

| Branch | Status | Points | Justification |
|---|---|---|---|
| Commercial lines | reported (S1&S2) | 2.0/3.0 | L2032–2033: Absolute IAE largest clients 2024 = 277,225 tCO₂e, DQS 3.00 (−25% vs 2021 baseline 369,613 tCO₂e, DQS 5.00). IAE intensity all other commercial clients 2024 = 321 tCO₂e/€m GWP, DQS 4.50 (−7% vs 2021). Scope S1&S2 only (L2026: *"Scopes 1 & 2 of commercial insureds"*). S3 monitored but not yet included. → 2/3 pts. |
| Reinsurance – commercial | missing | 0.0/1.0 | Facultative reinsurance explicitly excluded from IAE targets (L1806 fn.h: *"excluding facultative reinsurance"*). No separate reinsurance IAE calculated. |
| Personal motor (retail motor) | reported | 3.0/3.0 | L2032–2033: IAE intensity motor 2024 = 124 kgCO₂e/vehicle, DQS 3.70 (−11% vs 2019 baseline 139, DQS 3.40). L2586: PCAF attribution factor 6.99% applied. Scope: 4 markets (France, Germany, Switzerland, UK) — 83% of total retail motor GWP in-scope entities (L2028). → 3/3 pts. |
| Reinsurance – personal motor | missing | 0.0/1.0 | Not reported. |

**Raw score**: 2.0 + 0.0 + 3.0 + 0.0 = **5.0/8 = 62.5%** → Level **3/5**

---

### 2. Attribution Methodology — 3/5

| Source | Verbatim |
|---|---|
| L2026 | *"Methodology for associating insured emissions to insurers developed by the PCAF, namely the PCAF Standard Part C (2) published in 2023."* |
| L2586 | *"Insurance-Associated Emissions (IAE) is the standard measurement provided by the Partnership for Carbon Accounting Financials (PCAF). [...] For the Retail Motor IAE calculation, the attribution factor of 6.99% provided by PCAF was used."* |
| L2033 | *"due to a methodological change from PCAF regarding the attribution factor for the calculation (e.g. 6.99% versus the previous 18%)"* ← active PCAF methodology update applied |
| L1809 | *"AXA refers to [...] the Partnership for Carbon Accounting Financials ('PCAF') for the calculation of its underwriting [...] carbon footprint."* |

PCAF Standard Part C (2023) explicitly referenced and applied. PCAF attribution factors used (6.99% for motor). DQS disclosed per IAE category (commercial largest: 3.00; intensity: 4.50; motor: 3.70). S3 excluded per PCAF boundary for motor. No explicit signatory statement — language is *"refers to"* / *"is the standard measurement provided by."* → **Score 3/5**.

---

### 3. Temporal Coverage — 1/3

| Source | Data |
|---|---|
| L2032–2033 | Commercial lines: 2021 baseline (369,613 tCO₂e, DQS 5.00) + 2024 current (277,225 tCO₂e, DQS 3.00); target −30% by 2030 |
| L2032–2033 | Motor vehicles: 2019 baseline (139 kgCO₂e/vehicle, DQS 3.40) + 2024 current (124, DQS 3.70); target −20% by 2030 |

The IAE table shows only **two data points per metric** (baseline year + 2024). No 2023 intermediate year is disclosed in the report. L2025 states targets were first announced in June 2023, and 2024 is the second year of tracking. However, no 2023 IAE value appears in the table or the KPI summary.

Two data points (baseline + 2024) + 2030 targets. The ≥ 3 years threshold for Score 2 is not met. → **Score 1/3**.

---

## Summary

| Part | Score | Max | Compliance % |
|---|---|---|---|
| **Part A** — Financed Emissions | **10** | 23 | **43.5%** |
| **Part B** — Facilitated Emissions | N/A | N/A | N/A |
| **Part C** — Insurance-Associated Emissions | **7** | 13 | **53.8%** |


---

## Methodology notes

- **PCAF signatory**: Not explicitly confirmed. L1809: AXA *"refers to"* PCAF; L2586: IAE *"is the standard measurement provided by"* PCAF. No formal signatory statement found.
- **Key corrections vs auto-generated file**: (1) Commercial real estate changed from `missing` to `reported` (RE equity IS covered); (2) Motor vehicle loans changed from `reported` to `missing` (motor in auto-gen referred to IAE, not financed loans); (3) Mortgages changed from `partial` to `missing` (explicitly excluded at L1875); (4) DQS changed from 2/5 to **0/5** (the 4.0 extracted was IAE Part C DQS, not Part A); (5) Portfolio coverage changed from 1/5 to **3/5** (the 24% was the IAE commercial premium share; the 86.9% is real estate equity coverage only; the correct overall figure is 72% at L1863).
- **72% vs 86.9% (V3 audit)**: The V3 audit pre-determined 86.9% → score 4 for AXA. Full reading confirms this is real estate equity coverage only (L1863 fn.3). The correct overall portfolio coverage is 72% (L1863: *"72% of the General Account's asset classes were covered"*). Score 3 applied.
- **Part A gap**: AXA's financed emissions scope is narrow (listed corporates + sovereign + RE equity). Mortgages, private equity, business loans are excluded. DQS not disclosed for the investment portfolio (−5 pts).
- **Part C IAE temporal gap**: Only 2 years of data shown (baseline + 2024). A 2023 intermediate IAE data point is not published in the URD 2024.
- **Verification_status**: `[VERIFIED]` — full report reading (5 717 lines).
