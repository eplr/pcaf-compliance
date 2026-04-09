# PCAF Compliance Scoring – Methodology V2

> Version 2.0 · March 2026 · Based on *Nouvelle_Methodologie_PCAF_V2.docx*

---

## Overview

This methodology evaluates the PCAF® reporting compliance of financial institutions across **3 parts** and **11 criteria**. Each part yields an independent compliance percentage; a weighted overall score is then derived based on institution type.

| Part | Scope | Criteria | Max score |
|------|-------|----------|-----------|
| **A** | Financed Emissions | 5 | 23 pts (5+5+5+5+**3**) |
| **B** | Facilitated Emissions *(banks/bancassurance only)* | 3 | 13 pts (5+5+**3**) |
| **C** | Insurance-Associated Emissions *(insurers/reinsurers/bancassurance only)* | 3 | 13 pts (5+5+**3**) |

**Compliance % per part** = total score / max score × 100.  
Temporal Coverage always has a **max of 3** (not 5).

---

## Part A – Financed Emissions (max 23)

### 1. Asset Class Coverage `0–5`
Coefficient-weighted table. Each asset class earns points for S1&S2 coverage and, where mandatory, for S3 coverage. Justification for exclusions awards **50 %** of the applicable points.

| Asset class | S1&S2 coeff | S3 coeff | Max |
|---|---|---|---|
| Listed equity & corporate bonds | 3 | 3 | **6** |
| Business loans & unlisted equity | 3 | 3 | **6** |
| Project finance | 1 | 1 *(if relevant)* | **2** |
| Commercial real estate | 1 | — | **1** |
| Mortgages | 0.5 | — | **0.5** |
| Motor vehicle loans | 0.5 | — *(optional)* | **0.5** |
| Sovereign debt | 0.5 + 0.5 LULUCF | 1 | **2** |
| **Total** | | | **18** |

Raw score ÷ 18 → coverage ratio → level (see *Coverage level scale* below).

### 2. Data Quality Score `0–5`
Based on the institution's average PCAF DQS (1 = verified, 5 = estimated).

| Level | Average DQS |
|---|---|
| 0 | Not disclosed |
| 1 | 4.5 – 5 |
| 2 | 3.5 – 4.5 |
| 3 | 2.5 – 3.5 |
| 4 | 1.5 – 2.5 |
| 5 | < 1.5 with continuous improvement |

### 3. Attribution Methodology `0–5`
0 = no method · 1 = basic estimation · 2 = documented, partial coverage · 3 = PCAF-aligned per asset class · 4 = full PCAF (signatory) · 5 = PCAF + sector-specific enhancements

### 4. Portfolio Coverage `0–5`
0 = not reported · 1 = < 40 % · 2 = 40–60 % · 3 = 60–80 % · 4 = 80–95 % · 5 = > 95 %

### 5. Temporal Coverage `0–3`
0 = no history · 1 = current year only · 2 = ≥ 3 years + trends · 3 = ≥ 3 years + trends + projections/targets

---

## Part B – Facilitated Emissions (max 13)

Applicable to **banks and bancassurance** only. Five primary-market asset classes (public debt, public equity, private equity, private debt, syndicated loans), each worth 2 pts (1 S1&S2 + 1 S3) → max raw = 10.

| Criterion | Max |
|---|---|
| Asset Class Coverage *(coverage ratio / 10 → level)* | 5 |
| Attribution Methodology *(same 0–5 scale as Part A)* | 5 |
| Temporal Coverage | 3 |

---

## Part C – Insurance-Associated Emissions (max 13)

Applicable to **insurers, reinsurers and bancassurance**.

| Branch | S1&S2 coeff | S3 coeff | Max |
|---|---|---|---|
| Commercial Lines | 2 | 1 | **3** |
| Reinsurance – Commercial Lines | 0.75 | 0.25 | **1** |
| Personal Motor Lines | 3 | — | **3** |
| Reinsurance – Personal Motor | 1 | — | **1** |
| **Total** | | | **8** |

Raw score ÷ 8 → coverage ratio → level.

| Criterion | Max |
|---|---|
| Asset Class Coverage | 5 |
| Attribution Methodology | 5 |
| Temporal Coverage | 3 |

---

## Coverage Level Scale (all parts)

Used to convert a raw coverage ratio into a 0–5 level for the *Asset Class Coverage* criterion.

| Level | Coverage ratio |
|---|---|
| 0 | 0 % |
| 1 | 0 % < ratio ≤ 40 % |
| 2 | 40 % < ratio < 50 % |
| 3 | 50 % ≤ ratio < 70 % |
| 4 | 70 % ≤ ratio < 90 % |
| 5 | ≥ 90 % |

---

## Weighted Overall Score

| Institution type | Part A | Part B | Part C |
|---|---|---|---|
| Bank | 70 % | 30 % | — |
| Insurer / Reinsurer | 50 % | — | 50 % |
| Bancassurance | 40 % | 20 % | 40 % |
| Asset Manager / Other | 100 % | — | — |

> For banks with embedded insurance activity (e.g. Commerzbank), Part C can be scored even if Part C is not formally required; the weight allocation is then adjusted case by case.

---

## Toolchain

### Prerequisites
- Python ≥ 3.10
- `openpyxl`, `python-docx` (optional, for reading client feedback files)

```bash
pip install openpyxl python-docx
```

### Key data files

| File | Role |
|---|---|
| `analysis/results/corrected_compliance_data.json` | Institution-level compliance status (Part A/B/C status, DQS, sovereign debt, etc.) |
| `analysis/results/pcaf_composite_scores.csv` | Per-asset-class composite scores (0–5) |
| `analysis/results/extended_asset_class_coverage.json` | Asset class coverage status per institution (`reported` / `partial` / `missing`) |
| `analysis/results/pcaf_v2_scores.json` | **Client-verified V2 scores** for Nordea, Commerzbank, Ageas (authoritative override) |

### Scripts – run in order

```bash
# 1. Generate per-criterion scores for all 23 institutions
python3 generate_pcaf_assessment.py
# → looker_data/pcaf_assessment_detailed.csv

# 2. Regenerate the 6 Looker Studio CSV files
python3 generate_all_looker_csvs.py
# → looker_data/{asset_class_emissions, financed_emissions,
#              operational_emissions, pcaf_assessment_parts,
#              pcaf_assessment_overall, pcaf_compliance}.csv
```

### Adding or updating verified scores
To add a new institution with client-verified scores, add an entry to `analysis/results/pcaf_v2_scores.json` following the existing structure for Nordea / Commerzbank / Ageas. The script will automatically use those scores instead of the algorithmic fallback.

---

## Verified Results (Nordea · Commerzbank · Ageas)

| Institution | Compliance A | Compliance B | Compliance C |
|---|---|---|---|
| Nordea | 18/23 = **78.3 %** | 0/13 = 0 % | N/A |
| Commerzbank | 15/23 = **65.2 %** | 0/13 = 0 % | 3/13 = **23.1 %** |
| Ageas | 11/23 = **47.8 %** | 0/13 = 0 % | 7/13 = **53.8 %** |

*Scores verified against client reference file `Comparaison_methodologique_-_Score_compliance_PCAF.xlsx` (Nouvelle Méthode section).*
