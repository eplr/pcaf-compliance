# PCAF Maturity Assessment - Quick Start

**Date:** February 6, 2026  
**Company:** Aviva PLC  
**Overall Score:** 32.5% (Level 1 - Initial)

---

## FILES CREATED

### 1. Documentation
- **`PCAF_Maturity_Assessment_Guide.md`** - Complete user guide (18 criteria, scoring methodology)
- **`export_pcaf_maturity.py`** - Python script to generate CSV files
- **`README_PCAF_Maturity.md`** - This quick start guide

### 2. Data Files (for Looker Studio)
Location: `looker_data/`

- **`pcaf_assessment_detailed.csv`** - 16 rows, criterion-by-criterion scores
- **`pcaf_assessment_parts.csv`** - 2 rows, Part A & C summaries  
- **`pcaf_assessment_overall.csv`** - 1 row, overall weighted score

---

## AVIVA PLC RESULTS SUMMARY

### Part A: Financed Emissions
**Score:** 26/40 (65%) - **Level 3 (Defined)**

| Criterion | Score | Status |
|-----------|-------|--------|
| Asset Class Coverage | 3/5 | ⚠ Only 50% of PCAF classes |
| Data Quality Score | 3/5 | ✓ Good (2.5/5 avg) |
| Attribution Methodology | 4/5 | ✓ PCAF-aligned |
| Scope Coverage | 3/5 | ⚠ Scope 3 missing |
| Portfolio Coverage | 3/5 | ✓ ~85% coverage |
| Sovereign Debt | 3/5 | ⚠ Not in total |
| Temporal Coverage | 3/5 | ✓ 3 years data |
| Intensity Metrics | 4/5 | ✓ Strong |

### Part C: Insurance Emissions
**Score:** 0/40 (0%) - **Level 0 (Not Started)** - **CRITICAL GAP**

All 8 criteria score 0 - no insurance-associated emissions reported.

---

## NEXT STEPS

### For Looker Studio Visualization

1. **Upload to Google Sheets**
   ```
   - Go to sheets.google.com
   - Create new spreadsheet: "PCAF Maturity - Aviva"
   - Import 3 CSV files from looker_data/ folder
   ```

2. **Connect to Looker Studio**
   ```
   - Go to lookerstudio.google.com
   - Create → Report
   - Add Data → Google Sheets
   - Select your spreadsheet
   ```

3. **Build Dashboards**
   
   **Page 1: Executive Summary**
   - Scorecard: Overall 32.5%
   - Gauge charts: Part A (65%), Part C (0%)
   - Radar chart: 18 criteria visualization
   
   **Page 2: Part A Detail**
   - Bar chart: 8 criteria scores
   - Table: Evidence and gaps
   
   **Page 3: Part C Gap Analysis**
   - Heatmap: 8 missing criteria
   - Priority matrix (4 Critical, 3 High)

### For Aviva - Immediate Actions

**Next 6 months (Critical):**
1. Implement PCAF Part C pilot for commercial lines + motor insurance
2. Add 2 more financed emission asset classes (motor vehicle loans, securitized products)
3. Include sovereign debt in financed emissions total

**Next 12 months (High):**
1. Achieve 50% Part C coverage (2 of 4 insurance lines)
2. Expand Part A to 7-8 asset classes
3. Add Scope 3 for major investees

**Target:** 60% overall score (Level 3) within 2 years

---

## KEY CONTACTS & RESOURCES

### PCAF Resources
- PCAF Standard: https://carbonaccountingfinancials.com/
- PCAF Part C Guide (Insurance): [Download from PCAF website]

### Internal
- Sustainability datasheet: `in/aviva-plc-sustainability-datasheet-2024.xlsx`
- Analysis methodology: `PCAF_Analysis_Methodology.md`
- Looker integration: `Looker_Studio_Integration_Guide.md`

---

## ASSESSMENT CRITERIA REFERENCE

### 6 Maturity Levels

| Level | Label | Description |
|-------|-------|-------------|
| 0 | Not Started | No reporting |
| 1 | Initial | Ad-hoc, <20% coverage |
| 2 | Developing | 20-40% coverage, basic methodology |
| 3 | Defined | 40-70% coverage, PCAF-aligned |
| 4 | Advanced | 70-90% coverage, robust |
| 5 | Leading | >90% coverage, best practices |

### 18 Assessment Criteria

**Part A (8 criteria):** Asset class coverage, data quality, attribution, scope coverage, portfolio coverage, sovereign debt, temporal coverage, intensity metrics

**Part B (2 criteria):** Capital markets activity, emission attribution (N/A for insurers)

**Part C (8 criteria):** Insurance lines coverage, commercial lines, motor insurance, project insurance, treaty reinsurance, attribution methodology, underwriting integration, data quality

---

## SCORING FORMULA

**For Insurers (like Aviva):**
```
Weighted Score = (Part A Score × 50%) + (Part C Score × 50%)
                = (26/40 × 50%) + (0/40 × 50%)
                = 32.5% + 0%
                = 32.5%
```

**Maturity Level:** Score ÷ 20 = 32.5 ÷ 20 = Level 1 (Initial)

---

## UPDATE INSTRUCTIONS

To update the assessment (e.g., for next year):

1. **Edit data in Python script:**
   ```bash
   nano export_pcaf_maturity.py
   # Update assessment_data dictionary with new scores
   ```

2. **Re-generate CSV files:**
   ```bash
   python3 export_pcaf_maturity.py
   ```

3. **Refresh Looker Studio:**
   - Google Sheets will auto-update
   - Looker Studio will reflect new data

---

## QUESTIONS?

See the comprehensive guide: **`PCAF_Maturity_Assessment_Guide.md`** (700 lines, all 18 criteria detailed)

---

**Document Version:** 1.0  
**Last Updated:** February 6, 2026  
**Next Review:** Annual (or after major sustainability report updates)
