# Matrice d’évaluation de maturité PCAF®

## Guide d’utilisation et d’intégration

**Version :** 1.0  
**Date :** 6 février 2026  
**Objectif :** évaluer le degré de conformité des institutions financières par rapport aux Parties A, B et C de la norme PCAF®

---

## SOMMAIRE

1. [Présentation](#1-présentation)
2. [Définition des niveaux de maturité](#2-niveaux-de-maturité)
3. [Critères d'évaluation](#3-critères-dévaluation)
4. [Méthodologie de scoring](#4-méthodologie-de-scoring)
5. [Comment utiliser cette matrice](#5-comment-utiliser-cette-matrice)
6. [Intégration à Looker Studio](#6-intégration-à-looker-studio)
7. [Guide d'interprétation des résultats](#7-guide-dinterprétation)

---

## 1\. Présentation

### Objectif

La matrice d’évaluation de maturité PCAF® jauge les progrès des institutions financières en matière d’intégration de la norme Partnership for Carbon Accounting Financials (PCAF®) et de ses trois parties :

- **Partie A :** émissions financées (10 classes d’actifs)
- **Partie B :** émissions facilitées (activités des marchés des capitaux)
- **Partie C :** émissions liées à l’assurance (4 branches d’assurance)

### Public cible

- Consultants en durabilité
- Équipes ESG d’institutions financières
- Investisseurs et parties prenantes
- Régulateurs et créateurs de normes

### Périmètre d’évaluation

- **18 critères distincts** dans l’ensemble des 3 parties de la norme PCAF®
- **Échelle de maturité à 6 niveaux** (0-5)
- **Pondération spécifique à l’institution financière** basée sur le modèle économique

---

## 2\. NIVEAUX DE MATURITÉ

| Niveau| Classification| Description| Caractéristiques|
|----------|----------|----------|----------|
| **0**| Aucune action engagée| Pas de reporting ni d’activité| • Aucun suivi des émissions<br>• Absence de méthodologie<br>• Absent de la feuille de route|
| **1**| Phase initiale| Ad hoc, périmètre limité| • Phase exploratoire<br>• Programme pilotes<br>• Couverture <20 %|
| **2**| Maturité en développement| Couverture partielle, méthodologie basique| • Méthodologie basique <br>• Couverture de 20 %-40 % <br>• Granularité limitée|
| **3**| Méthode définie| Bonne couverture, méthodologie standard| • Méthodes alignées sur PCAF®<br>• Couverture de 40 %-70 %<br>• Reporting standard|
| **4**| Maturité avancée| Couverture complète et solide| • Couverture de 70 %-90 % <br>• Données de grande qualité<br>• Méthodes spécifiques aux secteurs|
| **5**| Mature| Couverture totale, pratiques d’excellence| • Couverture >90 % <br>• Leader du secteur<br>• Innovation continue|

---

## 3\. CRITÈRES D’ÉVALUATION

### PARTIE A : ÉMISSIONS FINANCÉES (8 critères)

#### 1\. Couverture des classes d’actifs

**Ce que ce critère mesure :** couverture des 10 classes d’actifs définies par PCAF®

| Niveau| Couverture|
|----------|----------|
| 0| Aucune classe d’actifs ne fait l’objet de reporting|
| 1| 1-2 classes (10 %-20 %)|
| 2| 3-4 classes (30 %-40 %)|
| 3| 5-6 classes (50 %-60 %)|
| 4| 7-9 classes (70 %-90 %)|
| 5| Totalité des 10 classes (100 %)|

**Classes d’actifs selon PCAF® :**

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

#### 2\. Data Quality Score (score de qualité des données)

**Ce que ce critère mesure :** intégration du scoring de qualité PCAF® à 5 niveaux

| Niveau| Plage de scoring de qualité|
|----------|----------|
| 0| Absence de scoring de qualité|
| 1| Score de 4-5 (données indirectes/estimées)|
| 2| Score 3-4 (données primaires/estimées)|
| 3| Score 2-3 (données auditées/primaires)|
| 4| Score 1-2 (données vérifiées/auditées)|
| 5| Score <2 avec amélioration continue|

**Référence de score de qualité PCAF®**

- **Score 1 :** données vérifiées – données d’émissions déclarées
- **Score 2 :** données auditées – données déclarées, mais avec publication limitée
- **Score 3 :** données primaires – données issues des activités physiques
- **Score 4 :** données estimées – activités physiques estimées
- **Score 5 :** données indirectes – données d’activité économique

#### 3\. Méthode d’attribution

**Ce que ce critère mesure :** méthode de calcul des émissions financées

| Niveau| Méthode|
|----------|----------|
| 0| Aucune méthode d’attribution|
| 1| Estimation basique sans méthode claire|
| 2| Méthode documentée, couverture limitée des classes d’actifs|
| 3| Méthode alignée sur la norme PCAF®, plusieurs classes d’actifs couvertes|
| 4| Méthode PCAF® complète avec mises à jour annuelles|
| 5| PCAF® + améliorations spécifiques aux secteurs|

#### 4\. Couverture des scopes

**Ce que ce critère mesure :** inclusion des scopes d’émissions des entités investies

| Niveau| Scopes couverts|
|----------|----------|
| 0| Aucune déclaration relative aux scopes|
| 1| Scope 1 uniquement|
| 2| Scopes 1 + 2 (fondés sur la localisation)|
| 3| Scopes 1 + 2 (fondés sur le marché)|
| 4| Scopes 1 + 2 + émissions importantes du scope 3|
| 5| Scopes 1 + 2 + 3 avec émissions évitées|

#### 5\. Couverture du portefeuille

**Ce que ce critère mesure :** % des AsG/prêts intégrant des données d’émissions

| Niveau| % de couverture|
|----------|----------|
| 0| Aucun reporting de la couverture|
| 1| <40 % du portefeuille|
| 2| 40 %-60 %|
| 3| 60 %-80 %|
| 4| 80 %-95 %|
| 5| \>95 %|

#### 6\. Inclusion de la dette souveraine

**Ce que ce critère mesure :** traitement des participations souveraines

| Niveau| Traitement|
|----------|----------|
| 0| Non suivi|
| 1| Suivi, mais non publié|
| 2| Publié uniquement de manière séparée|
| 3| Publiée de manière séparée avec une méthode|
| 4| Intégré pleinement dans une publication séparée|
| 5| Pleinement intégré avec l’engagement politique|

#### 7\. Couverture temporelle

**Ce que ce critère mesure :** données historiques et reporting de tendances

| Niveau| Nombre d’années de données|
|----------|----------|
| 0| Aucune donnée historique|
| 1| Année en cours uniquement|
| 2| 2 ans|
| 3| 3 ans|
| 4| Plus de 3 ans avec analyse de tendances|
| 5| Plus de 5 ans avec projections/objectifs|

#### 8\. Métriques d’intensité

**Ce que ce critère mesure :** métriques d’émissions normalisées

| Niveau| Métriques|
|----------|----------|
| 0| Aucune métrique d’intensité|
| 1| Intensité basique (par volume d’AsG)|
| 2| Intensités multiples (par produit, volume d’AsG)|
| 3| PCAF Economic Carbon Intensity (ECI, intensité carbone)|
| 4| Métrique spécifique au secteur (WACI, EVIC, etc.)|
| 5| Panel complet avec benchmarking|

---

### PARTIE B : ÉMISSIONS FACILITÉES (2 critères)

#### 1\. Couverture des activités sur les marchés des capitaux

**Ce que ce critère mesure :** souscription et suivi d’émission

| Niveau| Couverture|
|----------|----------|
| 0| Aucun suivi|
| 1| Suivi du volume d’émission uniquement|
| 2| Volume + estimations d’émission basiques|
| 3| Méthodologie PCAF® pour les actions/la dette|
| 4| Couverture complète avec scores de qualité|
| 5| Couverture complète + engagement client|

**Remarque :** critère principalement applicable aux banques d’investissements

#### 2\. Attribution des émissions

**Ce que ce critère mesure :** méthodes d’attribution des émissions facilitées

| Niveau| Méthode|
|----------|----------|
| 0| Aucune attribution|
| 1| Allocation simple|
| 2| Allocation basée sur le temps|
| 3| Méthode structurée PCAF®|
| 4| Méthode améliorée avec analyse d’impact|
| 5| Ensemble du cycle de vie avec émissions évitées|

---

### PARTIE C : ÉMISSIONS LIÉES À L’ASSURANCE (8 critères)

#### 1\. Couverture des branches d’assurance

**Ce que ce critère mesure :** Couverture des 4 catégories d’assurance définies par PCAF®

| Niveau| Branches couvertes|
|----------|----------|
| 0| Aucun reporting sur les émissions liées à l’assurance|
| 1| 1 branche d’assurance|
| 2| 2 branches d’assurance|
| 3| 3 branches d’assurance|
| 4| Ensemble des 4 branches avec des données basiques|
| 5| Ensemble des 4 lignes avec des données complètes|

**Branches d’assurance PCAF® :**

1. Assurance de branches commerciales
2. Branches véhicule à moteur personnel
3. Assurance de projets
4. Traités de réassurance

#### 2\. Couverture des branches commerciales

**Ce que ce critère mesure :** émissions liées aux dommages aux biens et en responsabilité civile

| Niveau| Statut|
|----------|----------|
| 0| Non suivi|
| 1| Établissement préliminaire du périmètre|
| 2| Projet pilote pour le sous-ensemble|
| 3| Méthodologie PCAF® pour les principaux secteurs|
| 4| Couverture complète avec scores de qualité|
| 5| Couverture complète + métriques pondérées des risques|

#### 3\. Couverture de l’assurance pour véhicule à moteur

**Ce que ce critère mesure :** émissions des véhicules à moteur personnels et professionnels

| Niveau| Statut|
|----------|----------|
| 0| Non suivi|
| 1| Établissement préliminaire du périmètre|
| 2| Collecte basique des données de la flotte|
| 3| Méthodologie PCAF® pour le portefeuille d’assurance véhicules à moteur|
| 4| Émissions détaillées par type de véhicule|
| 5| Couverture complète + risque de transition|

#### 4\. Couverture d’assurance de projets

**Ce que ce critère mesure :** émissions de grandes infrastructures/projets d’envergure

| Niveau| Statut|
|----------|----------|
| 0| Non suivi|
| 1| Établissement préliminaire du périmètre|
| 2| Projets fortement émissifs uniquement|
| 3| PCAF pour les projets > seuil|
| 4| Tous les projets importants|
| 5| Couverture complète + analyse d’impact|

#### 5\. Couverture des traités de réassurance

**Ce que ce critère mesure :** émissions du portefeuille de réassurance

| Niveau| Statut|
|----------|----------|
| 0| Non suivi|
| 1| Établissement préliminaire du périmètre|
| 2| Traités principaux uniquement|
| 3| PCAF® pour les traités importants|
| 4| Couverture de l’ensemble des traités|
| 5| Couverture complète + engagement de la cédante|

#### 6\. Méthode d’attribution

**Ce que ce critère mesure :** méthode d’attribution spécifique à l’assurance

| Niveau| Méthode|
|----------|----------|
| 0| Aucune méthode|
| 1| Allocation basique fondée sur les primes|
| 2| Méthode ITV|
| 3| Attribution d’assurance selon PCAF®|
| 4| Méthode PCAF® + ajustement en fonction du risque|
| 5| Méthode améliorée avec incidence sur la prévention des pertes|

#### 7\. Intégration de la souscription

**Ce que ce critère mesure :** données d’émissions dans les décisions de souscription

| Niveau| Intégration|
|----------|----------|
| 0| Aucune intégration|
| 1| Sensibilité élevée|
| 2| Prise en compte dans certains secteurs|
| 3| Intégration à l’évaluation des risques|
| 4| Tarification/conditions en fonction des émissions|
| 5| Intégration complète + soutien à la transition|

#### 8\. Qualité et couverture des données

**Ce que ce critère mesure :** qualité des données d’émissions liées aux assurances

| Niveau| Qualité|
|----------|----------|
| 0| Aucune donnée|
| 1| Couverture <20 %|
| 2| Couverture 20 %-40 %, faible qualité|
| 3| Couverture 40 %-60 %, PCAF® 3-4|
| 4| Couverture 60 %-80 %, PCAF® 2-3|
| 5| Couverture >80 %, PCAF® <2,5|

---

## 4\. MÉTHODOLOGIE DE SCORING

### Score pour chaque critère

- Chaque critère est noté de 0 à 5
- Évaluation fondée sur des preuves requise
- Justificatif du document pour chaque score

### Scores des parties

```
Part Score = Sum of all criterion scores in that part
Part Percentage = (Part Score / Maximum Possible) × 100
```

**Exemple :**

- La Partie A compte 8 critères × 5 points = score maximum de 40
- L’institution financière affiche 26/40 = 65 %

### Score de maturité général

**Pour les assureurs :**

```
Weighted Score = (Part A × 50%) + (Part C × 50%)
```

**Pour les banques :**

```
Weighted Score = (Part A × 70%) + (Part B × 30%)
```

**Pour les gestionnaires d’actifs :**

```
Weighted Score = Part A × 100%
```

### Classification des niveaux de maturité

| Score global| Niveau de maturité|
|----------|----------|
| 0 %-19 %| Niveaux 0-1 : aucune action engagée / phase initiale|
| 20 %-39 %| Niveaux 1-2 : phase initiale / en développement|
| 40 %-59 %| Niveaux 2-3 : en développement / défini|
| 60 %-79 %| Niveaux 3-4 : défini / avancé|
| 80 %-100 %| Niveaux 4-5 : avancé / mature|

---

## 5\. COMMENT UTILISER CETTE MATRICE

### Étape 1 : collecter les données servant de preuve

Réunir les rapports de durabilité, publications TCFD et données d’émissions des institutions financières couvrant :

- la répartition des classes d’actifs
- les méthodologies de calcul des émissions
- les scores de qualité des données
- les métriques de couverture
- les tendances historiques

### Étape 2 : noter chaque critère

Pour chacun des 18 critères :

1. Lire la définition du critère
2. Analyser les descriptions des niveaux 0 à 5
3. Faire correspondre les pratiques de chaque institution financière avec le niveau le plus proche
4. Documenter la preuve étayant le score
5. Enregistrer la note

### Étape 3 : calculer le score des différentes parties

- Additionner l’ensemble des scores des différents critères au sein de chaque partie
- Calculer le pourcentage : (score / max) × 100
- Attributer le niveau de maturité pour la partie concernée

### Étape 4 : calculer le score global

- Appliquer la pondération adéquate selon le type d’institution financière
- Calculer le pourcentage pondéré
- Attribuer le niveau général de maturité

### Étape 5 : identifier les écarts et les priorités

- Identifier les critères notés 0-2 (écarts majeurs)
- Hiérarchiser par importance relative par type d’institution
- Élaborer une feuille de route d’amélioration

---

## 6\. INTÉGRATION À LOOKER STUDIO

### Structure des données

Créer un fichier CSV avec cette structure :

**Onglet 1 : scores d’évaluation**

```csv
company,assessment_date,pcaf_part,criterion,score,max_score,evidence,priority
Aviva PLC,2024-12-31,Part A,Asset Class Coverage,3,5,"5 of 10 classes",High
Aviva PLC,2024-12-31,Part A,Data Quality Score,3,5,"Avg 2.5/5",Medium
...
```

**Onglet 2 : résumés des parties**

```csv
company,assessment_date,pcaf_part,total_score,max_score,percentage,maturity_level
Aviva PLC,2024-12-31,Part A,26,40,65.0,3
Aviva PLC,2024-12-31,Part B,0,10,0.0,0
Aviva PLC,2024-12-31,Part C,0,40,0.0,0
```

**Onglet 3 : résumé global**

```csv
company,assessment_date,institution_type,weighted_score,maturity_level,maturity_label
Aviva PLC,2024-12-31,Insurance,32.5,1,Initial
```

### Design du tablau de bord Looker Studio

#### Page 1 : Synthèse

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

#### Page 2 : Détail de la partie A

- Diagramme à barres horizontal : scores des 8 critères
- Tableau : Critère | Score | Preuve | Écart
- Séries chronologiques : progression historique (si plusieurs évaluations sont disponibles)

#### Page 3 : Détail de la partie C (pour les assureurs)

- Carte de densité de la couverture des branches d’assurance
- Matrice de hiérarchisation des écarts
- Feuille de route et calendrier d’exécution

#### Page 4 : Benchmarking (multi-institutions)

- Diagramme à barres comparatif par institution
- Moyennes sectorielles
- Identification des pratiques d’excellence

### Script Python pour l’exportation

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

## 7\. GUIDE D’INTERPRÉTATION

### Comment lire les résultats

**Score élevé (4-5) :** pratique exemplaire

- Poursuivre l’approche actuelle
- Partager les pratiques d’excellence
- Se concentrer sur l’innovation

**Score moyen (3) :** adéquat/défini

- Exigences PCAF® basiques remplies
- Opportunités d’amélioration
- Se concentrer sur l’extension de la couverture

**Score faible (1-2) :** en développement/phase initiale

- Écarts significatifs
- Nécessité d’amélioration méthodologique
- Priorité de développement

**Score nul (0) :** Aucune action engagée

- Écart majeur
- Action immédiate requise
- Priorité absolue

### Matrice de priorité

| Score| Importance| Priorité|
|----------|----------|----------|
| 0-1| Élevée| **CRITIQUE** – action immédiate|
| 0-1| Moyenne| **ÉLEVÉE** – action au cours des 6 prochains mois|
| 2| Élevée| **ÉLEVÉE** – action au cours des 6 prochains mois|
| 2| Moyenne| **MOYENNE** – action au cours des 12 prochains mois|
| 3+| Faible| **FAIBLE** – amélioration continue|

### Progression typique de la maturité

**Année 1 (phase initiale → en développement) :**

- Élaborer une méthodologie de base
- Couvrir 2-3 classes d’actifs / branches d’assurance
- Couvrir 20 %-40 % du portefeuille
- Objectif : score global de 20 %-40 %

**Année 2 (en développement → défini) :**

- Étendre à 5-6 classe d’actifs / 2-3 branches d’assurance
- Améliorer la qualité des données pour atteindre une moyenne de 3,0
- Atteindre une couverture de 50 %-60 %
- Objectif : score global de 40 %-60 %

**Années 3+ (défini → avancé) :**

- Couverture quasi complète des classes d’actifs
- Qualité des données <2,5
- Couverture de 70 %-80 %
- Objectif : score global de 60 %-80 %

---

## ANNEXE : MODÈLE D’ÉVALUATION À REMPLIR

Utilisez ce modèle pour évaluer n’importe quelle institution financière.

\[Voir fichier CSV séparé : `pcaf_assessment_template.csv`]

---

**FIN DU GUIDE**