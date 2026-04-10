# PCAF® Compliance Assessment — Project Summary V3.1

> **Date**: 9 April 2026  
> **Methodology**: PCAF Compliance Methodology V3.1  
> **Repository tag**: `v3.1` (commit `b93f334`)  
> **Scope**: 25 European financial institutions

---

## 1. Project overview

This project delivers a systematic PCAF® compliance assessment for 25 major European financial institutions, evaluating their GHG reporting maturity against the PCAF Global GHG Accounting and Reporting Standard across three parts:

| Part | Scope | Maximum |
|---|---|---|
| **A** — Financed Emissions | All institutions | 23 pts |
| **B** — Facilitated Emissions | Banks and bancassurances only | 13 pts |
| **C** — Insurance-Associated Emissions | Insurers, reinsurers, bancassurances | 13 pts |

Each part is scored independently. No global weighted score is published — compliance percentages per part stand alone.

---

## 2. Methodology

**Version**: V3.1 (April 2026)  
**Reference document**: `methodology/PCAF_Methodologie_V3.1_FR.md`

### Key V3.1 principles

- **Full report reading**: Every score is justified by a verbatim quote with line reference from the source report. No regex extraction.
- **Contextual percentage verification**: All percentages are verified against the full sentence and context before use — 9 of 13 initial extractions were found to be incorrect in V3 audit.
- **No estimation of portfolio coverage**: Score 0 when coverage rate is not explicitly disclosed (never estimated from indirect signals).
- **Evidence tagging**:
  - `[VERIFIED]` — full report reading completed
  - `[CHECKED BY AXYLIA]` — score validated by Axylia against reference file
  - `[FOUND]` — evidence identified in source report
  - `[NOT FOUND]` — criterion not reported in source document

---

## 3. Results — 25 institutions

| Institution | Type | Part A | % A | Part B | % B | Part C | % C | Status |
|---|---|---|---|---|---|---|---|---|
| Admiral Group | Insurance | 6/23 | 26.1% | N/A | — | 5/13 | 38.5% | `[VERIFIED]` |
| Ageas | Insurance | 11/23 | 47.8% | 0/13 | 0.0% | 7/13 | 53.8% | `[CHECKED BY AXYLIA]` |
| Allianz | Insurance | 12/23 | 52.2% | N/A | — | 10/13 | 76.9% | `[VERIFIED]` |
| Amundi | Asset Manager | 5/23 | 21.7% | N/A | — | N/A | — | `[VERIFIED]` |
| ASR Nederland | Insurance | 14/23 | 60.9% | N/A | — | 7/13 | 53.8% | `[VERIFIED]` |
| Aviva | Insurance | 14/23 | 60.9% | N/A | — | 0/13 | 0.0% | `[VERIFIED]` |
| AXA | Insurance | 10/23 | 43.5% | N/A | — | 7/13 | 53.8% | `[VERIFIED]` |
| Commerzbank | Bank | 15/23 | 65.2% | 0/13 | 0.0% | 3/13 | 23.1% | `[CHECKED BY AXYLIA]` |
| Crédit Agricole | Bank | 11/23 | 47.8% | 0/13 | 0.0% | N/A | — | `[VERIFIED]` |
| Deutsche Börse | Exchange | 3/23 | 13.0% | N/A | — | N/A | — | `[VERIFIED]` |
| Eurazeo | Asset Manager | 7/23 | 30.4% | N/A | — | N/A | — | `[VERIFIED]` |
| GBL | Investment Holding | 8/23 | 34.8% | N/A | — | N/A | — | `[VERIFIED]` |
| ING | Bank | 16/23 | 69.6% | 5/13 | 38.5% | N/A | — | `[VERIFIED]` |
| Julius Baer | Bank | 13/23 | 56.5% | 0/13 | 0.0% | N/A | — | `[VERIFIED]` |
| KBC | Bancassurance | 13/23 | 56.5% | 0/13 | 0.0% | 7/13 | 53.8% | `[VERIFIED]` |
| Legal & General | Insurance | 19/23 | 82.6% | N/A | — | 0/13 | 0.0% | `[VERIFIED]` |
| NN Group | Insurance | 17/23 | 73.9% | N/A | — | 10/13 | 76.9% | `[VERIFIED]` |
| Nordea | Bank | 18/23 | 78.3% | 0/13 | 0.0% | N/A | — | `[CHECKED BY AXYLIA]` |
| Phoenix Group | Insurance | 16/23 | 69.6% | N/A | — | 0/13 | 0.0% | `[VERIFIED]` |
| Santander | Bank | 15/23 | 65.2% | 0/13 | 0.0% | N/A | — | `[VERIFIED]` |
| Schroders | Asset Manager | 7/23 | 30.4% | N/A | — | N/A | — | `[VERIFIED]` |
| Société Générale | Bank | 10/23 | 43.5% | 0/13 | 0.0% | N/A | — | `[VERIFIED]` |
| Swiss Re | Reinsurance | 10/23 | 43.5% | N/A | — | 7/13 | 53.8% | `[VERIFIED]` |
| UniCredit | Bank | 10/23 | 43.5% | 0/13 | 0.0% | N/A | — | `[VERIFIED]` |
| Zurich | Insurance | 11/23 | 47.8% | N/A | — | 5/13 | 38.5% | `[VERIFIED]` |

### Notable highlights

- **Highest Part A**: Legal & General 82.6% · Nordea 78.3% · NN Group 73.9%
- **Highest Part C (IAE)**: Allianz 76.9% · NN Group 76.9%
- **Only Part B reporter**: ING (5/13 = 38.5% — syndicated loans via PCAF Part B)
- **Part C = 0**: Aviva, Legal & General, Phoenix Group — life/retirement insurers with no P&C underwriting; IAE not yet applicable or not yet reported
- **PCAF IAE standard co-developer**: Swiss Re (chaired PCAF IAE working group)

---

## 4. Source reports

| Institution | Report | Lines |
|---|---|---|
| Admiral Group | Sustainability Report 2024 | 1,005 |
| Allianz | Annual Report 2024 | ~26,000 |
| Amundi | Annual Report 2024 | ~18,800 |
| ASR Nederland | Annual Report 2024 | ~8,600 |
| Aviva | Climate-related Financial Disclosure 2024 + Datasheet | 4,013 |
| AXA | Annual Report 2024 | ~19,200 |
| Crédit Agricole | Rapport Annuel 2024 (XHTML) | ~42,000 |
| Deutsche Börse | Annual Report 2024 | 10,420 |
| Eurazeo | Document d'enregistrement universel 2024 | 22,154 |
| GBL | Annual Report 2024 | ~27,900 |
| ING | Annual Report 2025 (ESEF XHTML) | 89,783 |
| Julius Baer | Sustainability Report 2025 (FY2025 data) | 4,924 |
| KBC | Sustainability Report 2024 | 6,013 |
| Legal & General | Climate and Nature Report 2024 | 3,236 |
| NN Group | Annual Report 2024 | 23,633 |
| Phoenix Group | Annual Report and Accounts 2024 | 26,036 |
| Santander | Annual Report 2024 | ~30,900 |
| Schroders | Annual Report and Accounts 2024 | 10,342 |
| Société Générale | Annual Report 2024 | ~20,135 |
| Swiss Re | Sustainability Report 2024 | 5,217 |
| UniCredit | Annual Reports and Accounts 2024 | ~4,320 |
| Zurich | Annual Report 2024 | 26,238 |

*Nordea, Commerzbank, Ageas: scores validated by Axylia against reference file `Comparaison_methodologique_-_Score_compliance_PCAF.xlsx`.*

---

## 5. Key V3.1 corrections vs auto-generated V2 scores

### Portfolio Coverage — 9 false positives corrected

| Institution | V2 (wrong) | V3.1 (correct) | Error |
|---|---|---|---|
| ASR Nederland | 99% → score 5 | 77% → score 3 | 99% = green lease hectares |
| ING | 92% → score 4 | not disclosed → score 0 | 92% = IFRS 9 Stage 1 |
| Julius Baer | 49% → score 2 | not disclosed → score 0 | 49% = SBTi portfolio coverage target |
| KBC | 92% → score 4 | not disclosed → score 0 | 92% = SFDR Article 8/9 classification |
| Legal & General | 100% → score 5 | 41% → score 2 | 100% = 2050 net zero target |
| Schroders | 97% → score 5 | not disclosed → score 0 | 97% = operational Scope 3 share |
| Swiss Re | 90% → score 4 | 67% → score 3 | 90% = IAE commercial lines premiums (Part C) |
| UniCredit | 90% → score 4 | not disclosed → score 0 | 90% = credit risk classification |
| Zurich | 65% → score 3 | not disclosed → score 0 | 65% = SBT engagement target |

### Coverage found in report tables (3 additions)

| Institution | V2 | V3.1 | Source |
|---|---|---|---|
| Allianz | not disclosed → score 0 | 63% → score 3 | Annual Report, section E1 weighted table |
| NN Group | not disclosed → score 0 | 80% → score 4 | Financed emissions table, Annual Report |
| Swiss Re | 34% → score 1 | 67% → score 3 | Narrative section, Sustainability Report |

### Part C Attribution upgrades

| Institution | V2 | V3.1 | Reason |
|---|---|---|---|
| Swiss Re | 3/5 | 4/5 | Co-developed + chaired PCAF IAE standard (L1484, L305-308) |
| KBC | 2/5 | 3/5 | PCAF Standard Part C explicitly applied (L5726, L3840) |
| Zurich | 2/5 | 3/5 | PCAF IAE method explicitly cited (L6308, L6315); WACI = supplementary |

---

## 6. Output files

### Assessment reports (`output/`)

25 markdown files in `output/assessment_reports/` — one per institution:
`*_PCAF_Compliance_Assessment.md` — each contains metadata header, per-criterion verbatim evidence with line references, and summary table.

### Data files (`output/`)

| File | Rows | Description |
|---|---|---|
| `pcaf_assessment_detailed.csv` | 275 | Full detail — 11 criteria × 25 institutions |
| `pcaf_assessment_parts.csv` | 46 | Part-level compliance scores |
| `pcaf_compliance.csv` | 46 | Compliance % per part per institution |
| `pcaf_assessment_overall.csv` | 25 | Overall by institution |
| `financed_emissions.csv` | 25 | Part A scores and totals |
| `asset_class_emissions.csv` | 250 | Per asset class scores |
| `operational_emissions.csv` | 75 | Temporal and DQS details |

### Reference data (`data/`)

| File | Description |
|---|---|
| `pcaf_v2_scores.json` | Authoritative scores for all 25 institutions |
| `extended_asset_class_coverage.json` | Asset class status per institution |
| `corrected_compliance_data.json` | Compliance status and DQS per institution |

### Methodology (`methodology/`)

| File | Description |
|---|---|
| `PCAF_Methodologie_V3.1_FR.md` | **Current** — V3.1, April 2026 |
| `PCAF_Methodologie_V3_FR.md` | Previous version — V3.0, April 2026 |

---

## 7. Generation scripts

```bash
# Regenerate pcaf_assessment_detailed.csv (275 rows)
python3 generate_pcaf_assessment.py

# Regenerate all 6 Looker Studio CSVs
python3 generate_all_looker_csvs.py
```

Both scripts read from `data/pcaf_v2_scores.json` as the single source of truth.

---

## 8. Git history (V3.1 deliverable)

| Commit | Description |
|---|---|
| `b93f334` | **V3.1**: [CHECKED BY AXYLIA], [FOUND], assessor_notes, methodology rename |
| `1a102bd` | ING + Admiral Group verification_status cleanup |
| `f998f21` | Zurich + Eurazeo + Deutsche Börse [VERIFIED] |
| `62f4b63` | Phoenix Group [VERIFIED] |
| `64d31f9` | Schroders [VERIFIED] |
| `6d5fe4c` | KBC [VERIFIED] — Part C Attribution upgrade 3/5 |
| `e46bb19` | Julius Baer [VERIFIED] |
| `f742fcb` | Legal & General [VERIFIED] |
| `e218d57` | Aviva [VERIFIED] |
| `3a766ab` | Swiss Re [VERIFIED] — Part C Attribution 4/5 |
| `9b3d230` | Allianz · ASR · AXA · Amundi · CA · GBL · NN · Santander · SocGen · UniCredit |

**Tag**: `v3.1` → commit `b93f334`

---

*Generated by Oz · Axylia pcaf-compliance project · 9 April 2026*
