# PCAF Maturity Assessment Matrix
## User Guide & Implementation

**Version:** 1.0  
**Date:** February 6, 2026  
**Purpose:** Assess financial institutions' PCAF compliance maturity across Parts A, B, and C

---

## TABLE OF CONTENTS

1. [Overview](#overview)
2. [Maturity Levels Definition](#maturity-levels)
3. [Assessment Criteria](#assessment-criteria)
4. [Scoring Methodology](#scoring-methodology)
5. [How to Use This Matrix](#how-to-use)
6. [Looker Studio Integration](#looker-studio)
7. [Interpretation Guide](#interpretation)
8. [Case Study: Aviva PLC](#case-study)

---

## 1. OVERVIEW {#overview}

### Purpose
The PCAF Maturity Assessment Matrix evaluates financial institutions' progress in implementing the Partnership for Carbon Accounting Financials (PCAF) standard across three parts:

- **Part A:** Financed Emissions (10 asset classes)
- **Part B:** Facilitated Emissions (capital markets activities)
- **Part C:** Insurance-Associated Emissions (4 insurance lines)

### Target Users
- Sustainability consultants
- Financial institution ESG teams
- Investors and stakeholders
- Regulators and standard-setters

### Assessment Scope
- **18 distinct criteria** across 3 PCAF parts
- **6-level maturity scale** (0-5)
- **Institution-specific weighting** based on business model

---

## 2. MATURITY LEVELS {#maturity-levels}

| Level | Label | Description | Characteristics |
|-------|-------|-------------|----------------|
| **0** | Not Started | No reporting or activity | • No emissions tracking<br>• No methodology<br>• Not on roadmap |
| **1** | Initial | Ad-hoc, limited scope | • Exploratory phase<br>• Pilot programs<br>• <20% coverage |
| **2** | Developing | Partial coverage, basic methodology | • Basic methodology<br>• 20-40% coverage<br>• Limited granularity |
| **3** | Defined | Good coverage, standard methodology | • PCAF-aligned methods<br>• 40-70% coverage<br>• Standard reporting |
| **4** | Advanced | Comprehensive coverage, robust | • 70-90% coverage<br>• High data quality<br>• Sector-specific methods |
| **5** | Leading | Full coverage, best practices | • >90% coverage<br>• Industry leadership<br>• Continuous innovation |

---

## 3. ASSESSMENT CRITERIA {#assessment-criteria}

### PART A: FINANCED EMISSIONS (8 Criteria)

#### 1. Asset Class Coverage
**What it measures:** Coverage of 10 PCAF-defined asset classes

| Level | Coverage |
|-------|----------|
| 0 | No asset classes reported |
| 1 | 1-2 classes (10-20%) |
| 2 | 3-4 classes (30-40%) |
| 3 | 5-6 classes (50-60%) |
| 4 | 7-9 classes (70-90%) |
| 5 | All 10 classes (100%) |

**PCAF Asset Classes:**
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

#### 2. Data Quality Score
**What it measures:** PCAF 5-tier quality scoring implementation

| Level | Quality Score Range |
|-------|---------------------|
| 0 | No quality scoring |
| 1 | Score 4-5 (proxy/estimated data) |
| 2 | Score 3-4 (primary/estimated) |
| 3 | Score 2-3 (audited/primary) |
| 4 | Score 1-2 (verified/audited) |
| 5 | Score <2 with continuous improvement |

**PCAF Quality Score Reference:**
- **Score 1:** Verified - Reported emissions data
- **Score 2:** Audited - Reported with limited disclosure
- **Score 3:** Primary - Physical activity data
- **Score 4:** Estimated - Estimated physical activity
- **Score 5:** Proxy - Economic activity data

#### 3. Attribution Methodology
**What it measures:** Method for calculating financed emissions

| Level | Methodology |
|-------|-------------|
| 0 | No attribution methodology |
| 1 | Basic estimation without clear methodology |
| 2 | Documented methodology, limited asset classes |
| 3 | PCAF-aligned methodology, multiple asset classes |
| 4 | Full PCAF methodology with annual updates |
| 5 | PCAF + enhanced sector-specific refinements |

#### 4. Scope Coverage
**What it measures:** Investee emission scopes included

| Level | Scopes Covered |
|-------|----------------|
| 0 | No scope reporting |
| 1 | Scope 1 only |
| 2 | Scope 1 + 2 (location-based) |
| 3 | Scope 1 + 2 (market-based) |
| 4 | Scope 1 + 2 + material Scope 3 |
| 5 | Scope 1 + 2 + 3 with avoided emissions |

#### 5. Portfolio Coverage
**What it measures:** % of AUM/loans with emissions data

| Level | Coverage % |
|-------|------------|
| 0 | No coverage reporting |
| 1 | <40% of portfolio |
| 2 | 40-60% |
| 3 | 60-80% |
| 4 | 80-95% |
| 5 | >95% |

#### 6. Sovereign Debt Inclusion
**What it measures:** Treatment of sovereign holdings

| Level | Treatment |
|-------|-----------|
| 0 | Not tracked |
| 1 | Tracked but not disclosed |
| 2 | Disclosed separately only |
| 3 | Disclosed separately with methodology |
| 4 | Included in total with separate disclosure |
| 5 | Fully integrated with policy engagement |

#### 7. Temporal Coverage
**What it measures:** Historical data and trend reporting

| Level | Years of Data |
|-------|---------------|
| 0 | No historical data |
| 1 | Current year only |
| 2 | 2 years |
| 3 | 3 years |
| 4 | 3+ years with trend analysis |
| 5 | 5+ years with projections/targets |

#### 8. Intensity Metrics
**What it measures:** Normalized emissions metrics

| Level | Metrics |
|-------|---------|
| 0 | No intensity metrics |
| 1 | Basic intensity (per AUM) |
| 2 | Multiple intensities (per revenue, AUM) |
| 3 | PCAF Economic Carbon Intensity (ECI) |
| 4 | Sector-specific (WACI, EVIC, etc.) |
| 5 | Comprehensive suite with benchmarking |

---

### PART B: FACILITATED EMISSIONS (2 Criteria)

#### 1. Capital Markets Activity Coverage
**What it measures:** Underwriting and issuance tracking

| Level | Coverage |
|-------|----------|
| 0 | No tracking |
| 1 | Track issuance volume only |
| 2 | Volume + basic emission estimates |
| 3 | PCAF methodology for equity/debt |
| 4 | Comprehensive with quality scores |
| 5 | Full coverage + client engagement |

**Note:** Primarily applicable to investment banks

#### 2. Emission Attribution
**What it measures:** Method for attributing facilitated emissions

| Level | Method |
|-------|--------|
| 0 | No attribution |
| 1 | Simple allocation |
| 2 | Time-based allocation |
| 3 | PCAF facilitation methodology |
| 4 | Enhanced with impact assessment |
| 5 | Full lifecycle with avoided emissions |

---

### PART C: INSURANCE-ASSOCIATED EMISSIONS (8 Criteria)

#### 1. Insurance Lines Coverage
**What it measures:** Coverage of 4 PCAF insurance categories

| Level | Lines Covered |
|-------|---------------|
| 0 | No insurance emission reporting |
| 1 | 1 insurance line |
| 2 | 2 insurance lines |
| 3 | 3 insurance lines |
| 4 | All 4 lines with basic data |
| 5 | All 4 lines comprehensive |

**PCAF Insurance Lines:**
1. Commercial lines insurance
2. Personal motor lines
3. Project insurance
4. Treaty reinsurance

#### 2. Commercial Lines Coverage
**What it measures:** Commercial property & liability emissions

| Level | Status |
|-------|--------|
| 0 | Not tracked |
| 1 | Preliminary scoping |
| 2 | Pilot for subset |
| 3 | PCAF methodology for major sectors |
| 4 | Comprehensive with quality scores |
| 5 | Full coverage + risk-weighted metrics |

#### 3. Motor Insurance Coverage
**What it measures:** Personal & commercial motor emissions

| Level | Status |
|-------|--------|
| 0 | Not tracked |
| 1 | Preliminary scoping |
| 2 | Basic fleet data collection |
| 3 | PCAF methodology for motor portfolio |
| 4 | Detailed by vehicle type |
| 5 | Full coverage + transition risk |

#### 4. Project Insurance Coverage
**What it measures:** Large infrastructure/project emissions

| Level | Status |
|-------|--------|
| 0 | Not tracked |
| 1 | Preliminary scoping |
| 2 | High-emission projects only |
| 3 | PCAF for projects >threshold |
| 4 | All material projects |
| 5 | Full coverage + impact assessment |

#### 5. Treaty Reinsurance Coverage
**What it measures:** Reinsurance portfolio emissions

| Level | Status |
|-------|--------|
| 0 | Not tracked |
| 1 | Preliminary scoping |
| 2 | Major treaties only |
| 3 | PCAF for material treaties |
| 4 | Comprehensive treaty coverage |
| 5 | Full coverage + cedent engagement |

#### 6. Attribution Methodology
**What it measures:** Insurance-specific attribution method

| Level | Method |
|-------|--------|
| 0 | No methodology |
| 1 | Basic premium-based allocation |
| 2 | Insurance-to-value (ITV) method |
| 3 | PCAF insurance attribution |
| 4 | PCAF + risk-adjusted |
| 5 | Enhanced with loss prevention impact |

#### 7. Underwriting Integration
**What it measures:** Emissions data in underwriting decisions

| Level | Integration |
|-------|-------------|
| 0 | No integration |
| 1 | High-level awareness |
| 2 | Considered for certain sectors |
| 3 | Integrated in risk assessment |
| 4 | Emissions-based pricing/terms |
| 5 | Full integration + transition support |

#### 8. Data Quality & Coverage
**What it measures:** Quality of insurance emissions data

| Level | Quality |
|-------|---------|
| 0 | No data |
| 1 | <20% coverage |
| 2 | 20-40% coverage, low quality |
| 3 | 40-60% coverage, PCAF 3-4 |
| 4 | 60-80% coverage, PCAF 2-3 |
| 5 | >80% coverage, PCAF <2.5 |

---

## 4. SCORING METHODOLOGY {#scoring-methodology}

### Individual Criterion Score
- Each criterion scored 0-5
- Evidence-based assessment required
- Document rationale for each score

### Part Scores
```
Part Score = Sum of all criterion scores in that part
Part Percentage = (Part Score / Maximum Possible) × 100
```

**Example:**
- Part A has 8 criteria × 5 points = 40 max
- Institution scores 26/40 = 65%

### Overall Maturity Score

**For Insurers:**
```
Weighted Score = (Part A × 50%) + (Part C × 50%)
```

**For Banks:**
```
Weighted Score = (Part A × 70%) + (Part B × 30%)
```

**For Asset Managers:**
```
Weighted Score = Part A × 100%
```

### Maturity Level Classification

| Overall Score | Maturity Level |
|---------------|----------------|
| 0-19% | Level 0-1: Not Started / Initial |
| 20-39% | Level 1-2: Initial / Developing |
| 40-59% | Level 2-3: Developing / Defined |
| 60-79% | Level 3-4: Defined / Advanced |
| 80-100% | Level 4-5: Advanced / Leading |

---

## 5. HOW TO USE THIS MATRIX {#how-to-use}

### Step 1: Gather Evidence
Collect the institution's sustainability reports, TCFD disclosures, and emissions data covering:
- Asset class breakdowns
- Emission methodologies
- Data quality scores
- Coverage metrics
- Historical trends

### Step 2: Score Each Criterion
For each of the 18 criteria:
1. Read the criterion definition
2. Review the 0-5 level descriptions
3. Match institution's practices to closest level
4. Document evidence supporting the score
5. Record the score

### Step 3: Calculate Part Scores
- Sum all criterion scores within each part
- Calculate percentage: (score / max) × 100
- Assign maturity level for that part

### Step 4: Calculate Overall Score
- Apply appropriate weighting based on institution type
- Calculate weighted percentage
- Assign overall maturity level

### Step 5: Identify Gaps & Priorities
- Identify criteria scoring 0-2 (critical gaps)
- Prioritize by materiality to institution type
- Develop roadmap for improvement

---

## 6. LOOKER STUDIO INTEGRATION {#looker-studio}

### Data Structure

Create a CSV with this structure:

**Table 1: Assessment Scores**
```csv
company,assessment_date,pcaf_part,criterion,score,max_score,evidence,priority
Aviva PLC,2024-12-31,Part A,Asset Class Coverage,3,5,"5 of 10 classes",High
Aviva PLC,2024-12-31,Part A,Data Quality Score,3,5,"Avg 2.5/5",Medium
...
```

**Table 2: Part Summaries**
```csv
company,assessment_date,pcaf_part,total_score,max_score,percentage,maturity_level
Aviva PLC,2024-12-31,Part A,26,40,65.0,3
Aviva PLC,2024-12-31,Part B,0,10,0.0,0
Aviva PLC,2024-12-31,Part C,0,40,0.0,0
```

**Table 3: Overall Summary**
```csv
company,assessment_date,institution_type,weighted_score,maturity_level,maturity_label
Aviva PLC,2024-12-31,Insurance,32.5,1,Initial
```

### Looker Studio Dashboard Design

#### Page 1: Executive Summary
```
┌─────────────────────────────────────────────────────┐
│  PCAF MATURITY ASSESSMENT - [Company]               │
├─────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌───────────┐ │
│  │Overall Score │  │ Maturity     │  │ Rank      │ │
│  │   32.5%      │  │ Level 1      │  │ Initial   │ │
│  └──────────────┘  └──────────────┘  └───────────┘ │
│                                                      │
│  Progress by Part (Gauge Charts):                   │
│  Part A: [████████████░░░░░░░░] 65%                │
│  Part B: [N/A]                                      │
│  Part C: [░░░░░░░░░░░░░░░░░░░░] 0%                 │
│                                                      │
│  Radar Chart: Criterion Scores (0-5)                │
│  (Spider chart showing all 18 criteria)             │
└─────────────────────────────────────────────────────┘
```

#### Page 2: Part A Detail
- Horizontal bar chart: 8 criteria scores
- Table: Criterion | Score | Evidence | Gap
- Time series: Historical progression (if multiple assessments)

#### Page 3: Part C Detail (for insurers)
- Insurance lines coverage heatmap
- Gap prioritization matrix
- Roadmap timeline

#### Page 4: Benchmarking (multi-company)
- Comparative bar chart by institution
- Industry averages
- Best practices identification

### Python Export Script

```python
import pandas as pd
from datetime import datetime

# Assessment data structure
assessment_data = {
    'company': 'Aviva PLC',
    'assessment_date': '2024-12-31',
    'institution_type': 'Insurance',
    'part_a_scores': {
        'Asset Class Coverage': 3,
        'Data Quality Score': 3,
        'Attribution Methodology': 4,
        'Scope Coverage': 3,
        'Portfolio Coverage': 3,
        'Sovereign Debt Inclusion': 3,
        'Temporal Coverage': 3,
        'Intensity Metrics': 4
    },
    'part_b_scores': {
        'Capital Markets Activity': 0,
        'Emission Attribution': 0
    },
    'part_c_scores': {
        'Insurance Lines Coverage': 0,
        'Commercial Lines': 0,
        'Motor Insurance': 0,
        'Project Insurance': 0,
        'Treaty Reinsurance': 0,
        'Attribution Methodology': 0,
        'Underwriting Integration': 0,
        'Data Quality': 0
    }
}

# Export to CSV
def export_for_looker(assessment_data, output_path):
    """Export assessment data for Looker Studio"""
    
    # Table 1: Detailed scores
    detailed_scores = []
    
    for part, criteria in [('Part A', assessment_data['part_a_scores']),
                            ('Part B', assessment_data['part_b_scores']),
                            ('Part C', assessment_data['part_c_scores'])]:
        for criterion, score in criteria.items():
            detailed_scores.append({
                'company': assessment_data['company'],
                'assessment_date': assessment_data['assessment_date'],
                'pcaf_part': part,
                'criterion': criterion,
                'score': score,
                'max_score': 5,
                'percentage': (score / 5) * 100
            })
    
    df_detailed = pd.DataFrame(detailed_scores)
    df_detailed.to_csv(f'{output_path}/pcaf_assessment_detailed.csv', index=False)
    
    # Table 2: Part summaries
    part_a_total = sum(assessment_data['part_a_scores'].values())
    part_b_total = sum(assessment_data['part_b_scores'].values())
    part_c_total = sum(assessment_data['part_c_scores'].values())
    
    part_summaries = [
        {
            'company': assessment_data['company'],
            'assessment_date': assessment_data['assessment_date'],
            'pcaf_part': 'Part A',
            'total_score': part_a_total,
            'max_score': 40,
            'percentage': (part_a_total / 40) * 100,
            'maturity_level': part_a_total // 8
        },
        {
            'company': assessment_data['company'],
            'assessment_date': assessment_data['assessment_date'],
            'pcaf_part': 'Part C',
            'total_score': part_c_total,
            'max_score': 40,
            'percentage': (part_c_total / 40) * 100,
            'maturity_level': part_c_total // 8
        }
    ]
    
    df_parts = pd.DataFrame(part_summaries)
    df_parts.to_csv(f'{output_path}/pcaf_assessment_parts.csv', index=False)
    
    # Table 3: Overall
    weighted_score = (part_a_total * 0.5 + part_c_total * 0.5) / 40 * 100
    
    overall = [{
        'company': assessment_data['company'],
        'assessment_date': assessment_data['assessment_date'],
        'institution_type': assessment_data['institution_type'],
        'weighted_score': weighted_score,
        'maturity_level': int(weighted_score // 20),
        'part_a_score': (part_a_total / 40) * 100,
        'part_c_score': (part_c_total / 40) * 100
    }]
    
    df_overall = pd.DataFrame(overall)
    df_overall.to_csv(f'{output_path}/pcaf_assessment_overall.csv', index=False)
    
    print(f"✓ Exported 3 CSV files to {output_path}")
    return df_detailed, df_parts, df_overall

# Usage
export_for_looker(
    assessment_data, 
    '/Users/fidestra/Library/CloudStorage/OneDrive-fidestra/03_ACCOUNTS/Axylia/PCAF & banques/looker_data'
)
```

---

## 7. INTERPRETATION GUIDE {#interpretation}

### Reading the Results

**High Score (4-5):** Leading practice
- Continue current approach
- Share best practices
- Focus on innovation

**Medium Score (3):** Adequate/Defined
- Meets basic PCAF requirements
- Opportunities for enhancement
- Focus on coverage expansion

**Low Score (1-2):** Developing/Initial
- Significant gaps
- Requires methodological improvement
- Priority for development

**Zero Score (0):** Not Started
- Critical gap
- Immediate action needed
- Highest priority

### Priority Matrix

| Score | Materiality | Priority |
|-------|-------------|----------|
| 0-1 | High | **CRITICAL** - Immediate action |
| 0-1 | Medium | **HIGH** - Next 6 months |
| 2 | High | **HIGH** - Next 6 months |
| 2 | Medium | **MEDIUM** - Next 12 months |
| 3+ | Any | **LOW** - Continuous improvement |

### Typical Maturity Progression

**Year 1 (Initial → Developing):**
- Establish basic methodology
- Cover 2-3 asset classes / insurance lines
- Achieve 20-40% portfolio coverage
- Target: 20-40% overall score

**Year 2 (Developing → Defined):**
- Expand to 5-6 asset classes / 2-3 insurance lines
- Improve data quality to 3.0 average
- Achieve 50-60% coverage
- Target: 40-60% overall score

**Year 3+ (Defined → Advanced):**
- Near-complete asset class coverage
- Data quality <2.5
- 70-80% coverage
- Target: 60-80% overall score

---

## 8. CASE STUDY: AVIVA PLC {#case-study}

### Assessment Summary (2024)

**Overall Score:** 32.5% - **Level 1 (Initial)**

### Part A: Financed Emissions
**Score:** 26/40 (65%) - **Level 3 (Defined)**

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Asset Class Coverage | 3/5 | 5 of 10 classes (50%) |
| Data Quality | 3/5 | Weighted avg 2.5 |
| Attribution | 4/5 | PCAF-aligned |
| Scope Coverage | 3/5 | Scope 1+2 only |
| Portfolio Coverage | 3/5 | ~85% implied |
| Sovereign Debt | 3/5 | Tracked separately |
| Temporal Coverage | 3/5 | 3 years data |
| Intensity Metrics | 4/5 | ECI + asset-specific |

**Strengths:**
- Good methodology (PCAF-aligned)
- Strong data quality (2.5/5 avg)
- Comprehensive intensity metrics

**Gaps:**
- Only 50% asset class coverage
- Sovereign debt not in total
- Scope 3 not yet included

### Part C: Insurance Emissions
**Score:** 0/40 (0%) - **Level 0 (Not Started)**

All 8 criteria scored 0 - no insurance emissions reported.

**Impact:** **CRITICAL** - This is the most material gap for an insurer.

### Recommendations

**Immediate (6 months):**
1. Pilot PCAF Part C for commercial lines + motor insurance
2. Add 2 more financed emission asset classes
3. Include sovereign debt in total

**Short-term (12 months):**
1. Achieve 50% coverage on Part C (2 of 4 insurance lines)
2. Expand Part A to 7-8 asset classes
3. Improve data quality to <2.3 average

**Medium-term (2 years):**
1. Full Part C coverage (all 4 insurance lines)
2. Complete Part A (all 10 asset classes)
3. Integrate emissions in underwriting
4. Target: 60% overall score (Level 3)

---

## APPENDIX: BLANK ASSESSMENT TEMPLATE

Use this template to assess any financial institution:

[See separate CSV file: `pcaf_assessment_template.csv`]

---

**END OF GUIDE**
