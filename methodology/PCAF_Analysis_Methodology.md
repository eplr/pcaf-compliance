# METHODOLOGY: Financial Institution Emissions Analysis & PCAF Compliance Assessment

**Version:** 1.0  
**Date:** February 4, 2026  
**Based on:** Aviva PLC case study

---

## 1. OBJECTIVE

Assess a financial institution's greenhouse gas (GHG) emissions reporting against the PCAF (Partnership for Carbon Accounting Financials) standard to identify compliance gaps and provide actionable recommendations.

---

## 2. DATA SOURCES

### 2.1 Primary Source: Company Sustainability Report/Datasheet
- **Format:** Excel, PDF, or structured data file
- **Content:** Annual emissions disclosures, sustainability metrics

### 2.2 Reference Standard: PCAF Methodological Guidance
- **Format:** JSON/structured reference document
- **Content:** PCAF framework definitions, asset classes, emission categories

---

## 3. DATA EXTRACTION METHODOLOGY

### 3.1 Operational Emissions Extraction

**Step 1:** Identify relevant worksheets/sections (e.g., "Climate Action")  
**Step 2:** Extract Scope 1, 2, and 3 emissions data  
**Step 3:** Distinguish between market-based and location-based methodologies  
**Step 4:** Capture multi-year data for trend analysis  
**Step 5:** Document definitions and calculation methodologies

### 3.2 Financed/Facilitated/Insurance Emissions Extraction

**Step 1:** Identify investment/portfolio emissions (Scope 3 Category 15)  
**Step 2:** Extract financed emissions by asset class (if available)  
**Step 3:** Identify insurance-associated emissions (for insurers)  
**Step 4:** Capture facilitated emissions (for banks/underwriters)  
**Step 5:** Note data quality scores and coverage percentages

---

## 4. PCAF FRAMEWORK STRUCTURE

### 4.1 Part A: Financed Emissions

**10 asset classes required:**
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

### 4.2 Part B: Facilitated Emissions

- Capital market issuance activities
- **Applicable to:** Investment banks, underwriters

### 4.3 Part C: Insurance-Associated Emissions

- Commercial lines insurance
- Project insurance
- Personal motor lines
- Treaty reinsurance
- **Applicable to:** Insurers and reinsurers

---

## 5. GAP ANALYSIS FRAMEWORK

### 5.1 Coverage Assessment

- ✓ **REPORTED:** Data present and aligned with PCAF requirements
- ⚠ **PARTIAL:** Data present but lacks required granularity/breakdown
- ✗ **MISSING:** Data not disclosed or not aligned with PCAF framework

### 5.2 Granularity Analysis

- Compare reported aggregation level vs. PCAF requirements
- Identify missing asset class breakdowns
- Note exclusions (e.g., sovereign debt omitted)

### 5.3 Materiality Analysis

- Calculate ratio: Financed/Insurance emissions vs. Operational emissions
- Determine which PCAF parts are most material for the institution
- Prioritize gaps based on materiality

### 5.4 Institution Type Mapping

| Institution Type | Critical PCAF Parts |
|-----------------|---------------------|
| Insurance companies | Parts A + C |
| Banks | Parts A + B |
| Asset managers | Part A |
| Mixed institutions | All parts potentially applicable |

---

## 6. COMPARATIVE ANALYSIS STEPS

### Step 1: Structure Extraction
- Parse company report for all emission categories
- Organize data into operational vs. financed/facilitated/insurance

### Step 2: PCAF Mapping
- Map company's reported categories to PCAF framework
- Identify direct matches and discrepancies

### Step 3: Gap Identification
- For each PCAF part, assess: Reported? Complete? Granular?
- Document missing asset classes or emission categories

### Step 4: Quantitative Comparison
- Compare absolute emissions across years
- Calculate ratios (financed/operational, by asset class)
- Assess scale of unreported emissions

### Step 5: Qualitative Assessment
- Review methodology notes and definitions
- Assess data quality indicators
- Evaluate alignment with GHG Protocol and PCAF standards

---

## 7. OUTPUT DELIVERABLES

### 7.1 Emissions Data Summary
- Structured table: Scope 1, 2, 3 (operational)
- Structured table: Financed emissions by asset class
- Structured table: Insurance/facilitated emissions (if applicable)
- Multi-year trends and key metrics

### 7.2 PCAF Compliance Matrix
- **Part A (Financed)** → Coverage status by 10 asset classes
- **Part B (Facilitated)** → Coverage status + applicability assessment
- **Part C (Insurance)** → Coverage status by insurance lines

### 7.3 Gap Analysis Report
- Critical gaps (missing material emission categories)
- Moderate gaps (insufficient granularity)
- Minor gaps (methodological differences)

### 7.4 Recommendations
- **Priority 1:** Address critical gaps for institution type
- **Priority 2:** Enhance granularity for existing disclosures
- **Priority 3:** Adopt PCAF-aligned reporting structure
- **Priority 4:** Improve data quality and coverage

---

## 8. KEY METRICS & INDICATORS

### 8.1 Absolute Emissions
- Total operational (Scope 1 + 2 + 3)
- Total financed (across all asset classes)
- Total insurance-associated (for insurers)

### 8.2 Emission Intensity
- Per million revenue
- Per employee
- Per unit of assets under management

### 8.3 Coverage Ratios
- % of portfolio with emission data
- % of assets covered by PCAF methodology
- Data quality score distribution

### 8.4 Scale Indicators
- Financed/Operational ratio
- Insurance/Operational ratio
- Largest emission sources by asset class

---

## 9. QUALITY ASSURANCE CHECKS

- [ ] All emission scopes extracted (1, 2, 3)
- [ ] Multi-year data captured (minimum 3 years)
- [ ] Units verified and consistent (tCO2e, million tCO2e)
- [ ] Both market-based and location-based captured (if available)
- [ ] Definitions and notes documented
- [ ] PCAF framework correctly applied to institution type
- [ ] Gaps prioritized by materiality
- [ ] Recommendations actionable and specific

---

## 10. AUTOMATION OPPORTUNITIES

- Excel/PDF parsing for standard sustainability report formats
- Automated PCAF mapping based on institution type
- Gap analysis matrix generation
- Trend visualization and comparison charts
- Export to standardized JSON/CSV for further analysis

---

## 11. LIMITATIONS & ASSUMPTIONS

- Analysis depends on quality and completeness of source data
- PCAF framework interpretation may vary by institution
- Some emission categories may not apply to all institutions
- Data quality scores not always disclosed
- Methodological differences may exist between companies
- Sovereign debt treatment varies (inclusion/exclusion)

---

## 12. CASE STUDY: AVIVA PLC

### Key Findings

**Operational Emissions (2024):**
- Scope 1: 7,437 tCO2e
- Scope 2 (market-based): 413 tCO2e
- Scope 3 (operational): 10,691 tCO2e
- Total: 18,541 tCO2e (net-zero after offsets)

**Financed Emissions (2024):**
- Category 15 - Investments: 7.4 million tCO2e
- Coverage: Scope 1 & 2 of investees (excludes sovereign)

**Scale:**
- Financed emissions are 399x larger than operational emissions

### PCAF Compliance Assessment

| PCAF Part | Status | Notes |
|-----------|--------|-------|
| Part A: Financed Emissions | ⚠ PARTIAL | Aggregate reporting, missing 10 asset class breakdown |
| Part B: Facilitated Emissions | ✗ MISSING | May not be applicable |
| Part C: Insurance Emissions | ✗ MISSING | **CRITICAL GAP** - Aviva is a major insurer |

### Critical Gaps Identified

1. **No insurance-associated emissions reported** (PCAF Part C)
   - Missing: Commercial lines, motor insurance, reinsurance
   - Most material gap for an insurance company

2. **Insufficient granularity in financed emissions**
   - Reports aggregate vs. 10 required asset classes
   - Sovereign debt excluded

3. **Scale disparity highlights importance**
   - Financed emissions dwarf operational emissions
   - PCAF compliance more impactful than operational emission reductions

### Recommendations

1. **Immediate:** Implement PCAF Part C methodology for insurance portfolios
2. **Short-term:** Break down financed emissions by PCAF asset classes
3. **Medium-term:** Include sovereign debt in financed emissions
4. **Long-term:** Align full reporting structure with PCAF's 3-part framework

---

## APPENDIX A: Python Code Templates

### Template 1: Extract Emissions from Excel

```python
from openpyxl import load_workbook

def extract_emissions(filepath, sheet_name='Climate Action'):
    """Extract scope 1, 2, 3 emissions from Excel file"""
    wb = load_workbook(filepath)
    ws = wb[sheet_name]
    
    emissions = {
        'market_based': {},
        'location_based': {}
    }
    
    in_market_section = False
    in_location_section = False
    
    for row in ws.iter_rows(values_only=True):
        if not row or not row[0]:
            continue
        
        row_name = str(row[0])
        
        if 'Emissions (market-based)' in row_name:
            in_market_section = True
            in_location_section = False
        elif 'Emissions (location-based)' in row_name:
            in_market_section = False
            in_location_section = True
        
        if in_market_section:
            if row_name.startswith('Scope 1 (tCO2e)'):
                emissions['market_based']['scope_1'] = {
                    '2024': row[3], '2023': row[4], '2022': row[5]
                }
            # Add scope 2, 3 similarly
    
    return emissions
```

### Template 2: Gap Analysis Matrix

```python
def pcaf_gap_analysis(company_data, institution_type):
    """Compare company emissions data against PCAF requirements"""
    
    pcaf_requirements = {
        'insurance': ['part_a', 'part_c'],
        'bank': ['part_a', 'part_b'],
        'asset_manager': ['part_a']
    }
    
    gaps = {
        'critical': [],
        'moderate': [],
        'minor': []
    }
    
    required_parts = pcaf_requirements.get(institution_type, [])
    
    # Check Part A: Financed Emissions
    if 'part_a' in required_parts:
        if not company_data.get('financed_emissions'):
            gaps['critical'].append('Part A: Financed emissions missing')
        elif len(company_data['financed_emissions']) < 10:
            gaps['moderate'].append('Part A: Missing asset class breakdown')
    
    # Check Part C: Insurance Emissions
    if 'part_c' in required_parts:
        if not company_data.get('insurance_emissions'):
            gaps['critical'].append('Part C: Insurance emissions missing')
    
    return gaps
```

---

## DOCUMENT CHANGELOG

### Version 1.0 (February 4, 2026)
- Initial methodology based on Aviva PLC analysis
- Established 12-section framework
- Defined PCAF 3-part structure
- Created gap analysis matrix
- Developed recommendations framework
- Added Python code templates
- Included Aviva case study

---

**END OF DOCUMENT**
