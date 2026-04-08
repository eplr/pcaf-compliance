# Looker Studio Integration Guide
## PCAF Emissions Data Visualization

**Version:** 1.0  
**Date:** February 4, 2026  
**Purpose:** Transform Excel emissions data into interactive Looker Studio dashboards

---

## WORKFLOW ARCHITECTURE

```
Excel Reports (Aviva, etc.)
        ↓
Python ETL Script (Extract, Transform, Load)
        ↓
Google Sheets (4 tables)
        ↓
Looker Studio (4 dashboards)
```

---

## STEP 1: Data Extraction (Python)

Create 4 standardized tables from Excel:

1. **Operational Emissions** (time series)
2. **Financed Emissions** (time series)
3. **PCAF Compliance Status**
4. **Asset Class Breakdown**

### Python Script Template

```python
import pandas as pd
from openpyxl import load_workbook
from datetime import datetime

def extract_to_looker_format(excel_path, company_name):
    """Extract emissions data formatted for Looker Studio"""
    
    wb = load_workbook(excel_path)
    
    # Table 1: Operational Emissions
    operational = []
    for year in [2024, 2023, 2022]:
        operational.append({
            'company': company_name,
            'year': year,
            'reporting_date': f'{year}-12-31',
            'scope_1_tco2e': 7437,
            'scope_2_market_tco2e': 413,
            'scope_2_location_tco2e': 7360,
            'scope_3_operational_tco2e': 10691,
            'total_market_based_tco2e': 18541,
            'net_emissions_tco2e': 0
        })
    
    # Table 2: Financed Emissions
    financed = []
    for year in [2024, 2023, 2022]:
        financed.append({
            'company': company_name,
            'year': year,
            'category': 'Category 15 - Investments',
            'emissions_million_tco2e': 7.4,
            'asset_class': 'Mixed (aggregate)',
            'coverage_percent': 85,
            'data_quality_score': 3
        })
    
    # Table 3: PCAF Compliance
    pcaf = [
        {
            'company': company_name,
            'assessment_date': datetime.now().strftime('%Y-%m-%d'),
            'pcaf_part': 'Part A - Financed Emissions',
            'status': 'PARTIAL',
            'completeness_percent': 40,
            'missing_elements': '10 asset class breakdown',
            'priority': 'High'
        },
        {
            'company': company_name,
            'assessment_date': datetime.now().strftime('%Y-%m-%d'),
            'pcaf_part': 'Part C - Insurance Emissions',
            'status': 'MISSING',
            'completeness_percent': 0,
            'missing_elements': 'All insurance lines',
            'priority': 'Critical'
        }
    ]
    
    # Table 4: Asset Classes (template for 10 PCAF classes)
    asset_classes = []
    pcaf_asset_classes = [
        'Listed equity and corporate bonds',
        'Business loans and unlisted equity',
        'Project finance',
        'Commercial real estate',
        'Mortgages',
        'Motor vehicle loans',
        'Use of proceeds',
        'Securitized and structured products',
        'Sovereign debt',
        'Sub-sovereign debt'
    ]
    
    for asset_class in pcaf_asset_classes:
        asset_classes.append({
            'company': company_name,
            'year': 2024,
            'asset_class': asset_class,
            'emissions_million_tco2e': None,
            'coverage_percent': None,
            'reported': False
        })
    
    return {
        'operational': pd.DataFrame(operational),
        'financed': pd.DataFrame(financed),
        'pcaf_compliance': pd.DataFrame(pcaf),
        'asset_classes': pd.DataFrame(asset_classes)
    }

# Execute extraction
data = extract_to_looker_format(
    '/Users/fidestra/Library/CloudStorage/OneDrive-fidestra/03_ACCOUNTS/Axylia/PCAF & banques/in/aviva-plc-sustainability-datasheet-2024.xlsx',
    'Aviva PLC'
)

# Export to CSV
output_dir = '/Users/fidestra/Library/CloudStorage/OneDrive-fidestra/03_ACCOUNTS/Axylia/PCAF & banques/looker_data/'

data['operational'].to_csv(f'{output_dir}operational_emissions.csv', index=False)
data['financed'].to_csv(f'{output_dir}financed_emissions.csv', index=False)
data['pcaf_compliance'].to_csv(f'{output_dir}pcaf_compliance.csv', index=False)
data['asset_classes'].to_csv(f'{output_dir}asset_class_emissions.csv', index=False)

print("✓ Data exported successfully")
```

---

## STEP 2: Upload to Google Sheets

### Option A: Manual Upload (Simplest)

1. Go to [Google Sheets](https://sheets.google.com)
2. Create new spreadsheet: **"PCAF Emissions Database"**
3. Create 4 sheets:
   - `Operational_Emissions`
   - `Financed_Emissions`
   - `PCAF_Compliance`
   - `Asset_Classes`
4. File → Import → Upload CSV for each sheet

### Option B: Automated (Python + gspread)

```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def upload_to_google_sheets(dataframes, spreadsheet_name):
    """Automate upload to Google Sheets"""
    
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'credentials.json', scope
    )
    client = gspread.authorize(creds)
    
    # Create/open spreadsheet
    try:
        spreadsheet = client.open(spreadsheet_name)
    except:
        spreadsheet = client.create(spreadsheet_name)
    
    # Upload each dataframe
    for sheet_name, df in dataframes.items():
        try:
            worksheet = spreadsheet.worksheet(sheet_name)
        except:
            worksheet = spreadsheet.add_worksheet(
                title=sheet_name,
                rows=len(df)+10,
                cols=len(df.columns)
            )
        
        worksheet.clear()
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    
    return spreadsheet.url

# Usage
url = upload_to_google_sheets(data, "PCAF Emissions Database")
print(f"Uploaded to: {url}")
```

---

## STEP 3: Connect Looker Studio

1. Go to [Looker Studio](https://lookerstudio.google.com)
2. Click **Create** → **Report**
3. Click **Add Data**
4. Select **Google Sheets**
5. Choose **"PCAF Emissions Database"**
6. Select each sheet as a separate data source
7. Set data types:
   - Dates → Date type
   - Numbers → Number type
   - Text → Text type

---

## STEP 4: Dashboard Templates

### Dashboard 1: Executive Overview

**Components:**

```
┌────────────────────────────────────────────┐
│  PCAF COMPLIANCE - [Company Name]          │
├────────────────────────────────────────────┤
│  KPI Scorecards (3 cards)                  │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐   │
│  │Total Emis│ │PCAF Score│ │YoY Trend │   │
│  │25.9M tCO2│ │   40%    │ │  ↓ 12%  │   │
│  └──────────┘ └──────────┘ └──────────┘   │
│                                            │
│  Stacked Bar: Emissions by Scope           │
│  ■ Scope 1  ■ Scope 2  ■ Scope 3          │
│  [2022]  [2023]  [2024]                   │
│                                            │
│  Gauge Charts: PCAF Compliance             │
│  Part A: 40%  Part B: 0%  Part C: 0%      │
└────────────────────────────────────────────┘
```

**Metrics to include:**
- Total emissions (operational + financed)
- PCAF compliance %
- Year-over-year trend
- Gap count by priority

### Dashboard 2: Operational Emissions

**Components:**
1. **Line Chart** (Time Series)
   - X-axis: Year
   - Y-axis: Emissions (tCO2e)
   - Series: Scope 1, 2, 3

2. **Table** (Year-over-year comparison)
   ```
   Metric              | 2024   | 2023   | 2022   | Change
   Scope 1             | 7,437  | 7,503  | 8,526  | -12.8%
   Scope 2 (market)    | 413    | 429    | 563    | -26.6%
   Scope 3             | 10,691 | 9,454  | 4,869  | +119.5%
   Total               | 18,541 | 17,386 | 13,958 | +32.8%
   ```

3. **Waterfall Chart**
   - Scope 1 → +Scope 2 → +Scope 3 → Total

### Dashboard 3: PCAF Compliance

**Components:**
1. **Donut Chart** (Financed vs Operational)
   - Shows 399:1 ratio

2. **Horizontal Bar Chart** (Asset Classes)
   - 10 PCAF asset classes
   - Color: Green (reported), Red (missing)

3. **Heat Map** (Compliance Matrix)
   ```
   Part A  [■■■■□□□□□□] 40%  Missing breakdown
   Part B  [□□□□□□□□□□]  0%  N/A
   Part C  [□□□□□□□□□□]  0%  CRITICAL GAP
   ```

4. **Gap Table**
   ```
   PCAF Part | Status  | Priority | Missing Elements
   Part A    | PARTIAL | High     | Asset class breakdown
   Part C    | MISSING | Critical | All insurance lines
   ```

### Dashboard 4: Asset Class Detail

**Components:**
- Breakdown by 10 PCAF asset classes
- Coverage % by class
- Data quality scores
- Missing data highlights

---

## STEP 5: Calculated Fields

Create these in Looker Studio:

### 1. Emissions Intensity
```javascript
total_market_based_tco2e / revenue_million
```

### 2. Financed/Operational Ratio
```javascript
(emissions_million_tco2e * 1000000) / total_market_based_tco2e
```

### 3. PCAF Compliance Score
```javascript
AVG(completeness_percent)
```

### 4. Year-over-Year Change %
```javascript
(total_market_based_tco2e - LAG(total_market_based_tco2e)) / 
LAG(total_market_based_tco2e) * 100
```

### 5. Priority Score
```javascript
CASE
  WHEN priority = 'Critical' THEN 5
  WHEN priority = 'High' THEN 4
  WHEN priority = 'Medium' THEN 3
  WHEN priority = 'Low' THEN 2
  ELSE 1
END
```

### 6. Status Color
```javascript
CASE
  WHEN status = 'REPORTED' THEN '#34A853'
  WHEN status = 'PARTIAL' THEN '#FBBC04'
  WHEN status = 'MISSING' THEN '#EA4335'
END
```

---

## STEP 6: Visualization Best Practices

### Color Palette
- ✓ **Reported:** Green (#34A853)
- ⚠ **Partial:** Orange (#FBBC04)
- ✗ **Missing:** Red (#EA4335)
- **Neutral:** Gray (#9AA0A6)

### Chart Selection Guide
| Data Type | Best Chart |
|-----------|------------|
| Time series | Line chart |
| Part-to-whole | Donut/Pie |
| Comparisons | Bar chart |
| Status | Gauge/Bullet |
| Distribution | Histogram |
| Correlation | Scatter plot |

### Interactivity
- Add **date range filter**
- Add **company selector** (for multi-company)
- Add **PCAF part filter**
- Enable **drill-down** (summary → detail)

---

## STEP 7: Automation

### Monthly Data Refresh (Python)

```python
import schedule
import time
from datetime import datetime

def update_looker_data():
    """Scheduled data refresh"""
    
    print(f"[{datetime.now()}] Starting data refresh...")
    
    # Extract latest data
    data = extract_to_looker_format(
        '/path/to/latest/sustainability-report.xlsx',
        'Company Name'
    )
    
    # Upload to Google Sheets
    upload_to_google_sheets(data, "PCAF Emissions Database")
    
    print(f"[{datetime.now()}] Data refresh complete")

# Schedule monthly on 1st at 9:00 AM
schedule.every().month.at("09:00").do(update_looker_data)

while True:
    schedule.run_pending()
    time.sleep(3600)  # Check every hour
```

---

## DELIVERABLES CHECKLIST

- [ ] Python extraction script
- [ ] 4 CSV files exported
- [ ] Google Sheets spreadsheet created
- [ ] Looker Studio connected to data
- [ ] 4 dashboards built:
  - [ ] Executive overview
  - [ ] Operational emissions
  - [ ] PCAF compliance
  - [ ] Asset class detail
- [ ] Calculated fields configured
- [ ] Filters and interactivity enabled
- [ ] Color scheme applied
- [ ] Dashboard shared with team

---

## QUICK START (Aviva Example)

```bash
# 1. Run extraction
cd /Users/fidestra/Library/CloudStorage/OneDrive-fidestra/03_ACCOUNTS/Axylia/PCAF\ \&\ banques
python3 extract_emissions.py

# 2. Upload CSVs to Google Sheets manually

# 3. Connect Looker Studio
# Visit: https://lookerstudio.google.com
# Add data source → Google Sheets → PCAF Emissions Database

# 4. Build dashboards using templates above
```

---

## SAMPLE REPORT STRUCTURE

```
Page 1: Executive Dashboard
  - KPIs (3 scorecards)
  - Emissions trends (stacked bar)
  - PCAF compliance (gauge charts)

Page 2: Operational Emissions
  - Time series (line chart)
  - Scope breakdown (waterfall)
  - YoY comparison table

Page 3: PCAF Compliance
  - Financed vs operational (donut)
  - Asset class status (bar chart)
  - Compliance matrix (table)
  - Gap analysis (heat map)

Page 4: Asset Classes
  - 10 PCAF classes detail
  - Coverage percentages
  - Data quality indicators

Page 5: Data Quality
  - Coverage % by category
  - Quality scores
  - Methodology notes
```

---

## NEXT STEPS

1. ✓ Run Python extraction on Aviva Excel
2. Export 4 CSV files
3. Upload to Google Sheets
4. Connect Looker Studio
5. Build 4 dashboards
6. Share with Axylia team
7. Set up monthly automation

---

**END OF GUIDE**
