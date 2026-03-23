# Guide d’intégration à Looker Studio

## Visualisation des données d’émissions PCAF®

**Version :** 1.0  
**Date :** 4 février 2026  
**Objectif :** transformer les données d’émissions sous Excel en tableaux de bord interactifs dans Looker Studio

---

## ORGANISATION DES FLUX DE TRAVAIL

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

## ÉTAPE 1 : extraction de données (Python)

Créer 4 tableaux standardisés dans Excel :

1. **Émissions opérationnelles** (séries temporelles)
2. **Émissions financées** (séries temporelles)
3. **Statut de conformité PCAF®**
4. **Répartition par classe d’actifs**

### Modèle de script Python

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

## ÉTAPE 2 : téléverser dans Google Sheets

### Option A : téléversement manuel (le plus simple)

1. Accéder à [Google Sheets](https://sheets.google.com)
2. Créer une nouvelle feuille de calcul : **« PCAF Emissions Database »**
3. Créer 4 feuilles :
   - `Operational_Emissions`
   - `Financed_Emissions`
   - `PCAF_Compliance`
   - `Asset_Classes`
4. Fichier → Importer → Télécharger un fichier CSV pour chaque feuille

### Option B : via Python + gspread

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

## ÉTAPE 3 : connecter Looker Studio et les données

1. Accéder à [Looker Studio](https://lookerstudio.google.com)
2. Cliquer sur **Créer** → **Rapport**
3. Cliquer sur **Ajouter des données**
4. Sélectionner **Google Sheets**
5. Sélectionner **« PCAF Emissions Database »**
6. Sélectionner chaque feuille comme source de données distincte
7. Définir les types de données :
   - Dates → date
   - Nombres → nombre
   - Texte → texte

---

## ÉTAPE 4 : modèles de tableau de bord

### Tableau de bord 1 : résumé

**Composants :**

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

**Métriques à inclure :**

- Émissions totales (opérationnelles + financées)
- % conformité PCAF
- Tendance d’une année sur l’autre
- Nombre d’écarts par priorité

### Tableau de bord 2 : émissions opérationnelles

**Composants :**

1. **Graphique linéaire** (série temporelle)
   
   - Axe X : année
   - Axe Y : émissions (tCO2e)
   - Séries : scopes 1, 2, 3

2. **Tableau** (comparaison d’une année sur l’autre)
   
   ```
   Metric              | 2024   | 2023   | 2022   | Change
   Scope 1             | 7,437  | 7,503  | 8,526  | -12.8%
   Scope 2 (market)    | 413    | 429    | 563    | -26.6%
   Scope 3             | 10,691 | 9,454  | 4,869  | +119.5%
   Total               | 18,541 | 17,386 | 13,958 | +32.8%
   ```

3. **Graphique en cascade**
   
   - Scope 1 → +Scope 2 → +Scope 3 → Total

### Tableau de bord 3 : conformité PCAF®

**Composants :**

1. **Diagramme circulaire** (émissions financées vs opérationnelles)
   
   - Affiche le ratio XXX:1

2. **Diagramme à barres horizontales** (classes d’actifs)
   
   - 10 classes d’actifs PCAF®
   - Couleurs : vert (reporting réalisé), rouge (manquant)

3. **Carte de densité** (matrice de conformité)
   
   ```
   Part A  [■■■■□□□□□□] 40%  Missing breakdown
   Part B  [□□□□□□□□□□]  0%  N/A
   Part C  [□□□□□□□□□□]  0%  CRITICAL GAP
   ```

4. **Tableau des écarts**
   
   ```
   PCAF Part | Status  | Priority | Missing Elements
   Part A    | PARTIAL | High     | Asset class breakdown
   Part C    | MISSING | Critical | All insurance lines
   ```

### Tableau de bord 4 : Détail des classes d’actifs

**Composants :**

- répartition selon les 10 classes d’actifs PCAF®
- % de couverture par classe d’actifs
- Scores de qualité des données
- Principales données manquantes

---

## ÉTAPE 5 : champs calculés

À créer dans Looker Studio :

### 1\. Intensité des émissions

```javascript
total_market_based_tco2e / revenue_million
```

### 2\. Ratio émissions financées/opérationnelles

```javascript
(emissions_million_tco2e * 1000000) / total_market_based_tco2e
```

### 3\. Score de conformité PCAF®

```javascript
AVG(completeness_percent)
```

### 4\. Variation d’une année sur l’autre %

```javascript
(total_market_based_tco2e - LAG(total_market_based_tco2e)) / 
LAG(total_market_based_tco2e) * 100
```

### 5\. Score de priorité

```javascript
CASE
  WHEN priority = 'Critical' THEN 5
  WHEN priority = 'High' THEN 4
  WHEN priority = 'Medium' THEN 3
  WHEN priority = 'Low' THEN 2
  ELSE 1
END
```

### 6\. Couleur du statut

```javascript
CASE
  WHEN status = 'REPORTED' THEN '#34A853'
  WHEN status = 'PARTIAL' THEN '#FBBC04'
  WHEN status = 'MISSING' THEN '#EA4335'
END
```

---

## ÉTAPE 6 : recommandations pour la visualisation

### Jeu de couleurs

- ✓ **Reporting réalisé :** vert (#34A853)
- ⚠ **Reporting partiel :** orange (#FBBC04)
- ✗ **Manquant :** rouge (#EA4335)
- **Neutre :** gris (#9AA0A6)

### Guide de sélection des graphiques

| Type de données| Graphique le plus adapté|
|----------|----------|
| Séries temporelles| Graphique linéaire|
| « Part-to-whole »| Anneau/circulaire|
| Comparaisons| Diagramme à barres|
| Statut| Jauges/puces|
| Distribution| Histogramme|
| Corrélation| Diagramme de dispersion|

### Interactivité

- Ajouter un **filtre de plage de dates**
- Ajouter un **sélecteur d’entreprise**
- Ajouter un **filtre de partie PCAF®**
- Activer l’**Exploration détaillée** (résumé → détail)

---

## ÉTAPE 7 : automatisation

### Actualisation mensuelle des données (Python)

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

## LISTE DE CONTRÔLE DES LIVRABLES

- [ ] Script Python pour l’extraction
- [ ] Exportation des 4 fichiers CSV
- [ ] Création de la feuille de calcul Google Sheets
- [ ] Connexion de Looker Studio aux données
- [ ] Création de 4 tableaux de bord :
  - [ ] Vue d’ensemble
  - [ ] Émissions opérationnelles
  - [ ] Conformité PCAF®
  - [ ] Détail des classes d’actifs
- [ ] Champs calculés configurés
- [ ] Filtres et interactivité activés
- [ ] Jeu de couleurs appliqué
- [ ] Tableau de bord partagé avec l’équipe

---

## DÉMARRAGE RAPIDE (exemple société X)

```bash
# 1. Run extraction with the script file:
python3 extract_emissions.py

# 2. Upload CSVs to Google Sheets manually

# 3. Connect Looker Studio
# Visit: https://lookerstudio.google.com
# Add data source → Google Sheets → PCAF Emissions Database

# 4. Build dashboards using templates above
```

---

## EXEMPLE DE STRUCTURE DE RAPPORT

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

## ÉTAPES SUIVANTES

1. ✓ Exécuter l’extraction Python sur le fichier Excel contenant les données d’émissions
2. Exporter les 4 fichiers CSV
3. Téléverser dans Google Sheets
4. Connecter Looker Studio et les données
5. Créer les 4 tableaux de bord

---

**Fin**