# PCAF Maturity Assessment Template - Instructions

**Version:** 1.0  
**Date:** February 9, 2026

---

## TEMPLATE FILES

Two files provided for your convenience:

1. **`pcaf_assessment_template.csv`** - Pre-formatted CSV (18 rows, ready to fill)
2. **`PCAF_Assessment_Template_Instructions.md`** - This instruction file

---

## HOW TO USE THE TEMPLATE

### Step 1: Choose Your Format

**Option A: Use CSV directly**
- Open `pcaf_assessment_template.csv` in Excel or Google Sheets
- Replace placeholder values with actual data
- Save and import to Looker Studio

**Option B: Create from scratch**
- Use the criteria lists below
- Build your own spreadsheet
- Follow the same column structure

---

## COLUMN DEFINITIONS

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| **company** | Text | Name of financial institution | "Aviva PLC" |
| **assessment_date** | Date | Date of assessment (YYYY-MM-DD) | "2024-12-31" |
| **institution_type** | Category | Insurance / Bank / Asset Manager | "Insurance" |
| **pcaf_part** | Category | Part A / Part B / Part C | "Part A" |
| **criterion** | Text | Name of criterion (see lists below) | "Asset Class Coverage" |
| **score** | Number | Score 0-5 | 3 |
| **max_score** | Number | Always 5 | 5 |
| **percentage** | Number | (score/max_score) × 100 | 60.0 |
| **evidence** | Text | Brief supporting evidence | "5 of 10 asset classes reported" |
| **priority** | Category | Critical / High / Medium / Low / N/A | "High" |
| **gap_description** | Text | Description of what's missing | "Missing: Motor loans, Securitized products" |
| **assessor_notes** | Text | Optional notes for future reference | "Need to verify sovereign debt treatment" |

---

## SCORING GUIDE

### Maturity Levels (0-5)

| Score | Label | Description | Typical Characteristics |
|-------|-------|-------------|------------------------|
| **0** | Not Started | No reporting or tracking | • No methodology<br>• No data<br>• Not on roadmap |
| **1** | Initial | Ad-hoc, very limited | • Exploratory phase<br>• <20% coverage<br>• Pilot only |
| **2** | Developing | Partial coverage, basic | • Basic methodology<br>• 20-40% coverage<br>• Limited granularity |
| **3** | Defined | Good coverage, standard | • PCAF-aligned<br>• 40-70% coverage<br>• Standard reporting |
| **4** | Advanced | Comprehensive, robust | • 70-90% coverage<br>• High data quality<br>• Sector-specific |
| **5** | Leading | Full coverage, best practice | • >90% coverage<br>• Industry leading<br>• Continuous innovation |

---

## PART A: FINANCED EMISSIONS (8 Criteria)

### 1. Asset Class Coverage
**Measures:** Coverage of 10 PCAF asset classes

**Scoring:**
- **0:** No asset classes reported
- **1:** 1-2 classes (10-20%)
- **2:** 3-4 classes (30-40%)
- **3:** 5-6 classes (50-60%)
- **4:** 7-9 classes (70-90%)
- **5:** All 10 classes (100%)

**10 PCAF Asset Classes:**
1. Listed equity and corporate bonds
2. Business loans and unlisted equity
3. Project finance
4. Commercial real estate
5. Mortgages
6. Motor vehicle loans
7. Use of proceeds
8. Securitized and structured products
9. Sovereign debt
10. Sub-sovereign debt

**Evidence Examples:**
- "Reports 5 of 10 asset classes (50%)"
- "Full coverage except motor loans and sovereign debt"
- "Only listed equity and mortgages tracked"

---

### 2. Data Quality Score
**Measures:** PCAF 5-tier quality scoring implementation

**Scoring:**
- **0:** No quality scoring
- **1:** Score 4-5 (proxy/estimated data)
- **2:** Score 3-4 (primary/estimated)
- **3:** Score 2-3 (audited/primary)
- **4:** Score 1-2 (verified/audited)
- **5:** Score <2 with continuous improvement

**PCAF Quality Tiers:**
- **1:** Verified - Reported emissions data
- **2:** Audited - Reported with limited disclosure
- **3:** Primary - Physical activity data
- **4:** Estimated - Estimated physical activity
- **5:** Proxy - Economic activity data

**Evidence Examples:**
- "Weighted average 2.5 - good quality"
- "No quality scoring methodology"
- "Score 1.8 across portfolio"

---

### 3. Attribution Methodology
**Measures:** Method for calculating financed emissions

**Scoring:**
- **0:** No attribution methodology
- **1:** Basic estimation without clear methodology
- **2:** Documented methodology, limited asset classes
- **3:** PCAF-aligned methodology, multiple asset classes
- **4:** Full PCAF methodology with annual updates
- **5:** PCAF + enhanced sector-specific refinements

**Evidence Examples:**
- "PCAF-aligned using share of investment"
- "No documented methodology"
- "Custom methodology with sector adjustments"

---

### 4. Scope Coverage
**Measures:** Investee emission scopes included

**Scoring:**
- **0:** No scope reporting
- **1:** Scope 1 only
- **2:** Scope 1 + 2 (location-based)
- **3:** Scope 1 + 2 (market-based)
- **4:** Scope 1 + 2 + material Scope 3
- **5:** Scope 1 + 2 + 3 with avoided emissions

**Evidence Examples:**
- "Scope 1 + 2 market-based only"
- "Full scope 1+2+3 coverage"
- "Location-based Scope 2 only"

---

### 5. Portfolio Coverage
**Measures:** % of AUM/loans with emissions data

**Scoring:**
- **0:** No coverage reporting
- **1:** <40% of portfolio
- **2:** 40-60%
- **3:** 60-80%
- **4:** 80-95%
- **5:** >95%

**Evidence Examples:**
- "85% of portfolio covered"
- "Coverage not disclosed"
- "Full coverage except private investments"

---

### 6. Sovereign Debt Inclusion
**Measures:** Treatment of sovereign holdings

**Scoring:**
- **0:** Not tracked
- **1:** Tracked but not disclosed
- **2:** Disclosed separately only
- **3:** Disclosed separately with methodology
- **4:** Included in total with separate disclosure
- **5:** Fully integrated with policy engagement

**Evidence Examples:**
- "Tracked separately, excluded from total"
- "Fully integrated in financed emissions"
- "Not tracked"

---

### 7. Temporal Coverage
**Measures:** Historical data and trend reporting

**Scoring:**
- **0:** No historical data
- **1:** Current year only
- **2:** 2 years
- **3:** 3 years
- **4:** 3+ years with trend analysis
- **5:** 5+ years with projections/targets

**Evidence Examples:**
- "3 years of data (2022-2024)"
- "Current year only"
- "5 years with reduction targets"

---

### 8. Intensity Metrics
**Measures:** Normalized emissions metrics

**Scoring:**
- **0:** No intensity metrics
- **1:** Basic intensity (per AUM)
- **2:** Multiple intensities (per revenue, AUM)
- **3:** PCAF Economic Carbon Intensity (ECI)
- **4:** Sector-specific (WACI, EVIC, etc.)
- **5:** Comprehensive suite with benchmarking

**Evidence Examples:**
- "ECI and asset-class specific intensities"
- "Only emissions per AUM"
- "Full suite with sector benchmarks"

---

## PART B: FACILITATED EMISSIONS (2 Criteria)

**Note:** Primarily applicable to investment banks. Mark as "N/A" for insurers and most asset managers.

### 1. Capital Markets Activity
**Measures:** Underwriting and issuance tracking

**Scoring:**
- **0:** No tracking (or N/A)
- **1:** Track issuance volume only
- **2:** Volume + basic emission estimates
- **3:** PCAF methodology for equity/debt
- **4:** Comprehensive with quality scores
- **5:** Full coverage + client engagement

**Evidence Examples:**
- "N/A - not an investment bank"
- "Tracks equity underwriting only"
- "Full PCAF Part B implementation"

---

### 2. Emission Attribution
**Measures:** Method for attributing facilitated emissions

**Scoring:**
- **0:** No attribution (or N/A)
- **1:** Simple allocation
- **2:** Time-based allocation
- **3:** PCAF facilitation methodology
- **4:** Enhanced with impact assessment
- **5:** Full lifecycle with avoided emissions

**Evidence Examples:**
- "N/A - not applicable"
- "1-year time-based attribution"
- "Full PCAF methodology with impact metrics"

---

## PART C: INSURANCE-ASSOCIATED EMISSIONS (8 Criteria)

**Note:** Only applicable to insurance companies. Mark as "N/A" for banks and asset managers.

### 1. Insurance Lines Coverage
**Measures:** Coverage of 4 PCAF insurance categories

**Scoring:**
- **0:** No insurance emission reporting (or N/A)
- **1:** 1 insurance line
- **2:** 2 insurance lines
- **3:** 3 insurance lines
- **4:** All 4 lines with basic data
- **5:** All 4 lines comprehensive

**4 PCAF Insurance Lines:**
1. Commercial lines insurance
2. Personal motor lines
3. Project insurance
4. Treaty reinsurance

**Evidence Examples:**
- "N/A - not an insurer"
- "Commercial lines only tracked"
- "All 4 lines with comprehensive data"

---

### 2. Commercial Lines
**Measures:** Commercial property & liability emissions

**Scoring:**
- **0:** Not tracked (or N/A)
- **1:** Preliminary scoping
- **2:** Pilot for subset
- **3:** PCAF methodology for major sectors
- **4:** Comprehensive with quality scores
- **5:** Full coverage + risk-weighted metrics

**Evidence Examples:**
- "Not tracked"
- "Pilot for energy sector only"
- "Full portfolio coverage with risk metrics"

---

### 3. Motor Insurance
**Measures:** Personal & commercial motor emissions

**Scoring:**
- **0:** Not tracked (or N/A)
- **1:** Preliminary scoping
- **2:** Basic fleet data
- **3:** PCAF methodology for motor
- **4:** Detailed by vehicle type
- **5:** Full coverage + transition risk

**Evidence Examples:**
- "Not tracked"
- "Basic fleet emissions estimated"
- "Detailed by vehicle type with EV transition tracking"

---

### 4. Project Insurance
**Measures:** Large infrastructure/project emissions

**Scoring:**
- **0:** Not tracked (or N/A)
- **1:** Preliminary scoping
- **2:** High-emission projects only
- **3:** PCAF for projects >threshold
- **4:** All material projects
- **5:** Full coverage + impact assessment

**Evidence Examples:**
- "Not tracked"
- "Energy projects only"
- "All infrastructure with impact assessment"

---

### 5. Treaty Reinsurance
**Measures:** Reinsurance portfolio emissions

**Scoring:**
- **0:** Not tracked (or N/A)
- **1:** Preliminary scoping
- **2:** Major treaties only
- **3:** PCAF for material treaties
- **4:** Comprehensive treaty coverage
- **5:** Full coverage + cedent engagement

**Evidence Examples:**
- "Not tracked"
- "Top 10 treaties only"
- "Full portfolio with cedent engagement"

---

### 6. Attribution Methodology (Insurance)
**Measures:** Insurance-specific attribution method

**Scoring:**
- **0:** No methodology (or N/A)
- **1:** Basic premium-based
- **2:** Insurance-to-value (ITV)
- **3:** PCAF insurance attribution
- **4:** PCAF + risk-adjusted
- **5:** Enhanced with loss prevention

**Evidence Examples:**
- "No methodology"
- "Premium-based allocation"
- "PCAF ITV method with risk adjustment"

---

### 7. Underwriting Integration
**Measures:** Emissions data in underwriting decisions

**Scoring:**
- **0:** No integration (or N/A)
- **1:** High-level awareness
- **2:** Considered for certain sectors
- **3:** Integrated in risk assessment
- **4:** Emissions-based pricing/terms
- **5:** Full integration + transition support

**Evidence Examples:**
- "Not integrated"
- "Considered for energy sector only"
- "Emissions-based pricing with transition support"

---

### 8. Data Quality (Insurance)
**Measures:** Quality of insurance emissions data

**Scoring:**
- **0:** No data (or N/A)
- **1:** <20% coverage
- **2:** 20-40%, low quality
- **3:** 40-60%, PCAF 3-4
- **4:** 60-80%, PCAF 2-3
- **5:** >80%, PCAF <2.5

**Evidence Examples:**
- "No data"
- "30% coverage, quality score 3.5"
- "90% coverage, quality score 2.0"

---

## EXAMPLE: COMPLETED ROW

```csv
Aviva PLC,2024-12-31,Insurance,Part A,Asset Class Coverage,3,5,60.0,"5 of 10 PCAF asset classes reported (50%)",High,"Missing: Motor vehicle loans, Use of proceeds, Securitized products, Sovereign debt, Sub-sovereign debt","Need to prioritize motor loans given auto insurance business"
```

---

## CALCULATING OVERALL SCORES

### Part Scores
```
Part A Total = Sum of 8 criteria scores (max 40)
Part B Total = Sum of 2 criteria scores (max 10)
Part C Total = Sum of 8 criteria scores (max 40)

Part Percentage = (Part Total / Part Max) × 100
```

### Weighted Overall Score

**For Insurers:**
```
Weighted Score = (Part A % × 50%) + (Part C % × 50%)
```

**For Banks:**
```
Weighted Score = (Part A % × 70%) + (Part B % × 30%)
```

**For Asset Managers:**
```
Weighted Score = Part A %
```

### Maturity Level
```
Level = Weighted Score ÷ 20 (rounded down)

0-19%   = Level 0-1 (Not Started / Initial)
20-39%  = Level 1-2 (Initial / Developing)
40-59%  = Level 2-3 (Developing / Defined)
60-79%  = Level 3-4 (Defined / Advanced)
80-100% = Level 4-5 (Advanced / Leading)
```

---

## TIPS FOR ASSESSORS

### Before Starting
1. **Gather evidence:** Collect sustainability reports, TCFD disclosures, website data
2. **Read Part A/B/C definitions:** Understand what each part covers
3. **Identify institution type:** Determines which parts apply
4. **Set assessment date:** Use latest reporting period end date

### During Assessment
1. **Be evidence-based:** Document specific facts supporting each score
2. **Be consistent:** Use the same standards across all criteria
3. **Mark N/A appropriately:** Part B for insurers, Part C for banks
4. **Note uncertainties:** Use assessor_notes for unclear items
5. **Set priorities:** Critical for material gaps, Low for minor improvements

### After Completion
1. **Calculate totals:** Verify math on part scores
2. **Check materiality:** Do priorities align with institution type?
3. **Review consistency:** Do similar criteria have similar scores?
4. **Document gaps:** Clear action items in gap_description
5. **Export data:** Save for Looker Studio or further analysis

---

## QUALITY CHECKS

- [ ] All 18 rows completed (or appropriate N/A marks)
- [ ] Scores are 0-5 only
- [ ] Percentages calculated correctly
- [ ] Evidence documented for each score
- [ ] Priorities assigned based on materiality
- [ ] Gap descriptions specific and actionable
- [ ] Institution type correctly identified
- [ ] Part B/C marked N/A if not applicable

---

## NEXT STEPS

1. **Complete template** using this guide
2. **Calculate scores** (part totals and weighted overall)
3. **Export to Looker Studio** (see PCAF_Maturity_Assessment_Guide.md)
4. **Build dashboard** for visualization
5. **Develop action plan** based on critical gaps

---

**Questions?** Refer to the comprehensive guide:
`PCAF_Maturity_Assessment_Guide.md`

**Template Version:** 1.0  
**Last Updated:** February 9, 2026
