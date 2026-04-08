# MÉTHODOLOGIE : analyse des émissions des institutions financières et évaluation de la conformité PCAF®

**Version :** 1.0  
**Date :** 4 février 2026  
**basée sur :** Étude de cas Aviva PLC

---

## 1\. OBJECTIF

Évaluer la déclaration des émissions de gaz à effet de serre (GES) d’une institution financière par rapport à la norme PCAF® (Partnership for Carbon Accounting Financials) afin d’identifier les écarts en matière de conformité et de fournir des recommandations concrètes.

---

## 2\. SOURCES DE DONNÉES

### 2.1 Source principale : rapport/fiche technique de durabilité de l’entreprise

- **Format :** fichier de données Excel, PDF ou structuré
- **Contenu :** informations annuelles relatives aux émissions, indicateurs de durabilité

### 2.2 Norme de référence : directives méthodologiques PCAF®

- **Format :** JSON/document de référence structuré
- **Contenu :** définitions du cadre PCAF®, classes d’actifs, catégories d’émissions

---

## 3\. MÉTHODE D’EXTRACTION DES DONNÉES

### 3.1 Extraction des émissions opérationnelles

**Étape 1 :** identifier les documents/sections pertinents (par exemple, « Action climatique »)  
**Étape 2 :** extraire les données d’émissions de scopes 1, 2 et 3  
**Étape 3 :** faire la distinction entre les méthodologies basées sur le marché et celles basées sur la localisation 
**Étape 4 :** collecter des données pluriannuelles pour l’analyse des tendances  
 **Étape 5 :** définition des documents et méthodologies de calcul

### 3.2 Extraction des émissions financées/facilitées/liées à l’assurance

**Étape 1 :** identifier les émissions de l’investissement/du portefeuille (scope 3, catégorie 15)  
**Étape 2 :** extraire les émissions financées par classe d’actifs (si les données sont disponibles)  
**Étape 3 :** identifier les émissions liées à l’assurance (pour les assureurs)  
**Étape 4 :** recueillir les émissions facilitées (pour les banques/souscripteurs)  
**Étape 5 :** noter les scores de qualité des données et les pourcentages de couverture

---

## 4\. STRUCTURE-CADRE PCAF®

### 4.1 Partie A : émissions financées

**10 classes d’actifs exigées :**

1. Actions cotées et obligations de sociétés
2. Prêts aux entreprises et capitaux propres non cotés
3. Financement de projets
4. Immobilier commercial
5. Hypothèques
6. Prêts pour véhicules à moteur
7. Utilisation des produits
8. Produits titrisés et structurés
9. Dette souveraine
10. Dette sub-souveraine

### 4.2 Partie B : émissions facilitées

- Activités d’émission sur les marchés des capitaux
- **Champ d’application :** banques d’investissement, souscripteurs

### 4.3 Partie C : émissions liées à l’assurance

- Assurance de branches commerciales
- Assurance de projets
- Branches véhicule à moteur personnel
- Traités de réassurance
- **Champ d’application :** assureurs et réassureurs

---

## 5\. CADRE D’ANALYSE DES ÉCARTS

### 5.1 Évaluation de la couverture

- ✓ **REPORTING EFFECTUÉ :** données présentes et alignées sur les exigences PCAF®
- ⚠ **REPORTING PARTIEL :** données présentes, mais manque de granularité/ventilation nécessaire
- ✗ **MANQUANT :** données non publiées ou non alignées sur le cadre PCAF®

### 5.2 Analyse de granularité

- Comparer le niveau d’agrégation rapporté vs les exigences PCAF®
- Identifier les ventilations des classes d’actifs manquantes
- Noter les exclusions (par exemple, omission de la dette souveraine)

### 5.3 Analyse de l’importance

- Calculer le ratio : émissions financées/assurées vs émissions opérationnelles
- Déterminer quelles parties PCAF sont les plus importantes pour l’institution
- Hiérarchiser les écarts en fonction de l’importance

### 5.4 Cartographie des types d’institutions

| Type d’institution| Parties PCAF essentielles|
|----------|----------|
| Compagnies d’assurance| Parties A + C|
| Banques| Parties A + B|
| Gestionnaires d’actifs| Partie A|
| Institutions mixtes| Toutes les parties potentiellement applicables|

---

## 6\. ÉTAPES DE L’ANALYSE COMPARATIVE

### Étape 1 : structurer l’extraction

- Analyser le rapport de l’entreprise pour toutes les catégories d’émissions
- Organiser les données en émissions opérationnelles vs financées/facilitées/liés à l’assurance

### Étape 2 : cartographie PCAF®

- Cartographier les catégories publiées par l’entreprise par rapport au cadre PCAF®
- Identifier les correspondances et les divergences directes

### Étape 3 : identification des écarts

- Pour chaque partie PCAF®, évaluer : reporting réalisé ? Reporting complet ? Niveau de granularité ?
- Documenter les classes d’actifs ou les catégories d’émissions manquantes

### Étape 4 : comparaison quantitative

- Comparer les émissions absolues d’une année à l’autre
- Calculer les ratios (émissions financées/opérationnelles, par classe d’actifs)
- Évaluer l’ampleur des émissions non déclarées

### Étape 5 : évaluation qualitative

- Examiner les remarques méthodologiques et les définitions
- Évaluer les indicateurs de qualité des données
- Évaluer l’alignement sur GHG Protocol et la norme PCAF®

---

## 7\. LIVRABLES

### 7.1 Résumé des données sur les émissions

- Tableau structuré : scopes 1, 2, 3 (émissions opérationnelles)
- Tableau structuré : émissions financées par classe d’actifs
- Tableau structuré : émissions facilitées/liés à l’assurance (le cas échéant)
- Tendances pluriannuelles et indicateurs clés

### 7.2 Matrice de conformité PCAF®

- **Partie A (émissions financées)**	 Niveau de couverture, ventilation pour les 10 classes d’actifs
- **Partie B (émissions facilitées)** 	 Niveau de couverture + évaluation de l’applicabilité
- **Partie C (émissions liées à l’assurance)** 	 Niveau de la couverture par branches d’assurance

### 7.3 Rapport d’analyse des écarts

- Écarts majeurs (catégories d’émissions importantes manquantes)
- Écarts modérés (granularité insuffisante)
- Écarts mineurs (différences méthodologiques)

### 7.4 Recommandations

- **Priorité 1 :** combler les écarts majeurs pour le type d’institution
- **Priorité 2 :** améliorer la granularité des publications existantes
- **Priorité 3 :** adopter une structure de rapports alignée sur PCAF®
- **Priorité 4 :** améliorer la qualité et la couverture des données

---

## 8\. MÉTRIQUES ET INDICATEURS CLÉS

### 8.1 Émissions absolues

- Total des émissions opérationnelles (scopes 1 + 2 + 3)
- Total des émissions financées (toutes classes d’actifs confondues)
- Total des émissions liées à l’assurance (pour les assureurs)

### 8.2 Intensité des émissions

- Par million d’USD/EUR/GBP/CHF (ou autre devise) de revenus
- Par salarié
- Par unité d’actifs sous gestion

### 8.3 Ratios de couverture

- % du portefeuille avec données d’émissions
- % d’actifs couverts par la méthodologie PCAF®
- Répartition du score de qualité des données

### 8.4 Indicateurs d’échelle

- Ratio émissions financées/opérationnelles
- Ratio assurance/opérationnel
- Principales sources d’émissions par classe d’actifs

---

## 9\. ASSURANCE QUALITÉ

- [ ] Extraction des émissions de tous les scopes (1, 2, 3)
- [ ] Recueil de données pluriannuelles (minimum 3 ans)
- [ ] Unités vérifiées et cohérentes (tCO2e, millions de tCO2e)
- [ ] Collecte à la fois basée sur le marché et sur la localisation (si disponible)
- [ ] Définitions et remarques documentées
- [ ] Cadre PCAF correctement appliqué au type d’institution
- [ ] Écarts classés par ordre de priorité en fonction de l’importance
- [ ] Recommandations exploitables et spécifiques

---

## 10\. OPPORTUNITÉS D’AUTOMATISATION

- Analyse Excel/PDF pour les formats de rapport de durabilité standard
- Cartographie automatisée de PCAF en fonction du type d’institution
- Génération de la matrice d’analyse des écarts
- Graphiques de visualisation et de comparaison des tendances
- Exportation au format JSON/CSV standardisé pour une analyse plus approfondie

---

## 11\. LIMITES ET HYPOTHÈSES

- L’analyse dépend de la qualité et de l’exhaustivité des données sources
- L’interprétation du cadre PCAF® peut varier selon les institutions
- Certaines catégories d’émissions peuvent ne pas s’appliquer à toutes les institutions
- Les scores de qualité des données ne sont pas toujours publiés
- Des différences méthodologiques peuvent exister entre les entreprises
- Le traitement de la dette souveraine varie (inclusion/exclusion)

---

## ANNEXE A : Modèles de code Python

### Modèle 1 : extraction des émissions depuis un fichier Excel

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

### Modèle 2 : matrice d’analyse d’écarts

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

FIN