# Modèle d’évaluation de maturité PCAF® – instructions

**Version :** 1.0  
**Date :** 9 février 2026

---

## FICHIERS MODÈLES

Deux fichiers sont fournis :

1. **`pcaf_assessment_template.csv`** - CSV pré-formaté (18 lignes prêtes à remplir)
2. **`PCAF_Assessment_Template_Instructions.md`** - le présent fichier d’instructions

---

## COMMENT UTILISER LE MODÈLE

### Étape 1 : sélectionner le format

**Option A : utiliser directement le fichier CSV**

- Ouvrir `pcaf_assessment_template.csv` dans Excel ou Google Sheets
- Remplacer les valeurs génériques par les données réelles
- Enregistrer et importer dans Looker Studio

**Option B : création complète**

- Utiliser la liste de critères ci-dessous
- Créer une feuille de calcul propriétaire
- Rependre la structure des colonnes

---

## DÉFINITIONS DES COLONNES

| Colonne| Type| Description| Exemple|
|----------|----------|----------|----------|
| **company**| Texte| Nom de l’institution financière| "Aviva PLC"|
| **assessment_date**| Date| Date d’évaluation (JJ-MM-AAAA)| "31-12-2024"|
| **institution_type**| Catégorie| Assurance / banque / gestionnaire d’actifs| "Assurance"|
| **pcaf_part**| Catégorie| Partie A / Partie B / Partie C| "Partie A"|
| **criterion**| Texte| Nom du critère (voir listes ci-dessous)| "Couverture des classes d’actifs"|
| **score**| Nombre| Score de 0 à 5| 3|
| **max_score**| Nombre| Valeur toujours égale à 5| 5|
| **percentage**| Nombre| (score/max_score) × 100| 60,0|
| **evidence**| Texte| Élément de justification| "5 classes d’actifs sur 10 font l’objet d’un reporting"|
| **priority**| Catégorie| Critique / Élevée / Moyenne / Faible / N/A| "Élevée"|
| **gap_description**| Texte| Description des éléments manquants| "Manquant(s) : prêts pour véhicules à moteur, produits titrisés"|
| **assessor_notes**| Texte| Remarques facultatives pour référence ultérieure| "Vérifier le traitement de la dette souveraine"|

---

## GUIDE DE SCORING

### Niveaux de maturité (0-5)

| Score| Classification| Description| Caractéristiques typiques|
|----------|----------|----------|----------|
| **0**| Aucune action engagée| Aucun reporting ou suivi| • Aucune méthode<br>• Aucune donnée<br>• Absent de la feuille de route|
| **1**| Phase initiale| Ad hoc, très limitée| • Phase exploratoire <br>• Couverture <20 % <br>• Phase pilote uniquement|
| **2**| Maturité en développement| Couverture partielle, basique| • Méthodologie basique <br>• Couverture de 20 %-40 % <br>• Granularité limitée|
| **3**| Méthode définie| Bonne couverture, reporting standard| • Alignement PCAF®<br>• Couverture de 40 %-70 % <br>• Reporting standard|
| **4**| Maturité avancée| Aboutie et solide| • Couverture de 70 %-90 % <br>• Qualité élevée des données<br>• Spécifique au secteur|
| **5**| Mature| Couverture intégrale, pratique d’excellence| • Couverture >90 % <br>• Exemplaire pour le secteur <br>• Innovation continue|

---

## PARTIE A : ÉMISSIONS FINANCÉES (8 critères)

### 1\. Couverture des classes d’actifs

**Mesures :** couverture des 10 classes d’actifs selon PCAF®

**Scoring :**

- **0 :** Aucune classe d’actifs ne fait l’objet de reporting
- **1 :** 1-2 classes (10 %-20 %)
- **2 :** 3-4 classes (30 %-40 %)
- **3 :** 5-6 classes (50 %-60 %)
- **4 :** 7-9 classes (70 %-90 %)
- **5 :** Totalité des 10 classes (100 %)

**10 classes d’actifs selon PCAF® :**

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

**Exemples de preuves/justifications :**

- "5 classes d’actifs sur 10 font l’objet d’un reporting (50 %)"
- "Couverture complète, hors prêts pour véhicules à moteur et dette souveraine"
- "Suivi réalisé uniquement pour les actions cotées et les hypothèques"

---

### 2\. Data Quality Score (score de qualité des données)

**Mesures :** intégration du scoring de qualité PCAF® à 5 niveaux

**Scoring :**

- **0 :** Absence de scoring de qualité
- **1 :** Score de 4-5 (données indirectes/estimées)
- **2 :** Score 3-4 (données primaires/estimées)
- **3 :** Score 2-3 (données auditées/primaires)
- **4 :** Score 1-2 (données vérifiées/auditées)
- **5 :** Score <2 avec amélioration continue

**Niveaux de qualité PCAF® :**

- **1 :** données vérifiées – données d’émissions déclarées
- **2 :** données auditées – données déclarées, mais avec publication limitée
- **3 :** données primaires – données issues des activités physiques
- **4 :** données estimées – activités physiques estimées
- **5 :** données indirectes – données d’activité économique

**Exemples de preuves/justifications :**

- "Moyenne pondérée de 2,5 – bonne qualité"
- "Absence de méthodologie de scoring de la qualité"
- "Score de 1,8 sur l’ensemble du portefeuille"

---

### 3\. Méthode d’attribution

**Mesures :** méthode de calcul des émissions financées

**Scoring :**

- **0 :** Aucune méthode d’attribution
- **1 :** Estimation basique sans méthode claire
- **2 :** Méthode documentée, couverture limitée des classes d’actifs
- **3 :** Méthode alignée sur la norme PCAF®, plusieurs classes d’actifs couvertes
- **4 :** Méthode PCAF® complète avec mises à jour annuelles
- **5 :** PCAF® + améliorations spécifiques aux secteurs

**Exemples de preuves/justifications :**

- "Alignement PCAF® par l’utilisation de la part des investissements"
- "Aucune méthodologie documentée"
- "Méthodologie personnalisée avec ajustements sectoriels"

---

### 4\. Couverture des scopes

**Mesures :** inclusion des scopes d’émissions des entités investies

**Scoring :**

- **0 :** Aucune déclaration relative aux scopes
- **1 :** Scope 1 uniquement
- **2 :** Scopes 1 + 2 (fondés sur la localisation)
- **3 :** Scopes 1 + 2 (fondés sur le marché)
- **4 :** Scopes 1 + 2 + émissions importantes du scope 3
- **5 :** Scopes 1 + 2 + 3 avec émissions évitées

**Exemples de preuves/justifications :**

- "Scopes 1 + 2, uniquement fondés sur le marché"
- "Couverture de l’intégralité des scopes 1+2+3"
- "Scope 2 fondé sur la localisation uniquement"

---

### 5\. Couverture du portefeuille

**Mesures :** % des AsG/prêts intégrant des données d’émissions

**Scoring :**

- **0 :** Aucun reporting de la couverture
- **1 :** <40 % du portefeuille
- **2 :** 40 %-60 %
- **3 :** 60 %-80 %
- **4 :** 80 %-95 %
- **5 :** \>95 %

**Exemples de preuves/justifications :**

- "85 % du portefeuille couvert"
- "Couverture non publiée"
- "Couverture totale, hormis investissements privés"

---

### 6\. Inclusion de la dette souveraine

**Mesures :** traitement des participations souveraines

**Scoring :**

- **0 :** Non suivi
- **1 :** Suivi, mais non publié
- **2 :** Publié uniquement de manière séparée
- **3 :** Publiée de manière séparée avec une méthode
- **4 :** Intégré pleinement dans une publication séparée
- **5 :** Pleinement intégré avec l’engagement politique

**Exemples de preuves/justifications :**

- "Suivi séparément, exclu du total"
- "Pleinement intégré dans les émissions financées"
- "Non suivi"

---

### 7\. Couverture temporelle

**Mesures :** données historiques et reporting de tendances

**Scoring :**

- **0 :** Aucune donnée historique
- **1 :** Année en cours uniquement
- **2 :** 2 ans
- **3 :** 3 ans
- **4 :** Plus de 3 ans avec analyse de tendances
- **5 :** Plus de 5 ans avec projections/objectifs

**Exemples de preuves/justifications :**

- "3 années de données (2022-2024)"
- "Année en cours uniquement"
- "5 années avec objectifs de réduction"

---

### 8\. Métriques d’intensité

**Mesures :** métriques d’émissions normalisées

**Scoring :**

- **0 :** Aucune métrique d’intensité
- **1 :** Intensité basique (par volume d’AsG)
- **2 :** Intensités multiples (par produit, volume d’AsG)
- **3 :** PCAF Economic Carbon Intensity (ECI, intensité carbone)
- **4 :** Métrique spécifique au secteur (WACI, EVIC, etc.)
- **5 :** Panel complet avec benchmarking

**Exemples de preuves/justifications :**

- "ECI et intensités spécifiques aux classes d’actifs"
- "Émissions par AsG uniquement"
- "Panel complet avec benchmarks sectoriels"

---

## PARTIE B : ÉMISSIONS FACILITÉES (2 critères)

**Remarquable :** principalement applicable aux banques d’investissement Indiquer « N/A » pour les assureurs et la plupart des gestionnaires d’actifs

### 1\. Activités sur les marchés des capitaux

**Mesures :** souscription et suivi d’émission

**Scoring :**

- **0 :** Aucun suivi (ou N/A)
- **1 :** Suivi du volume d’émission uniquement
- **2 :** Volume + estimations d’émission basiques
- **3 :** Méthodologie PCAF® pour les actions/la dette
- **4 :** Couverture complète avec scores de qualité
- **5 :** Couverture complète + engagement client

**Exemples de preuves/justifications :**

- "N/A – n’est pas une banque d’investissement"
- "Suit la souscription d’actions uniquement"
- "Intégration complète de la Partie B de PCAF"

---

### 2\. Attribution des émissions

**Mesures :** méthodes d’attribution des émissions facilitées

**Scoring :**

- **0 :** Aucune attribution (ou N/A)
- **1 :** Allocation simple
- **2 :** Allocation basée sur le temps
- **3 :** Méthode structurée PCAF®
- **4 :** Méthode améliorée avec analyse d’impact
- **5 :** Ensemble du cycle de vie avec émissions évitées

**Exemples de preuves/justifications :**

- "N/A – non applicable"
- "Attribution basée sur 1 année"
- "Méthodologie PCAF complète avec métriques d’incidence"

---

## PARTIE C : ÉMISSIONS LIÉES À L’ASSURANCE (8 critères)

**Remarquable :** applicable uniquement aux sociétés d’assurance Indiquer « N/A » pour les banques et les gestionnaires d’actifs

### 1\. Couverture des branches d’assurance

**Mesures :** Couverture des 4 catégories d’assurance définies par PCAF®

**Scoring :**

- **0 :** Aucun reporting sur les émissions liées à l’assurance (ou N/A)
- **1 :** 1 branche d’assurance
- **2 :** 2 branches d’assurance
- **3 :** 3 branches d’assurance
- **4 :** Ensemble des 4 branches avec des données basiques
- **5 :** Ensemble des 4 lignes avec des données complètes

**4 branches d’assurance PCAF® :**

1. Assurance de branches commerciales
2. Branches véhicule à moteur personnel
3. Assurance de projets
4. Traités de réassurance

**Exemples de preuves/justifications :**

- "N/A – n’est pas une assurance"
- "Suivi des branches commerciales uniquement"
- "Totalité des 4 branches avec données complètes"

---

### 2\. Branches commerciales

**Mesures :** émissions liées aux dommages aux biens et en responsabilité civile

**Scoring :**

- **0 :** Non suivi (ou N/A)
- **1 :** Établissement préliminaire du périmètre
- **2 :** Projet pilote pour le sous-ensemble
- **3 :** Méthodologie PCAF® pour les principaux secteurs
- **4 :** Couverture complète avec scores de qualité
- **5 :** Couverture complète + métriques pondérées des risques

**Exemples de preuves/justifications :**

- "Non suivi"
- "Projet pilote pour le secteur de l’énergie uniquement"
- "Couverture complète du portefeuille avec métriques de risque"

---

### 3\. Assurance véhicules à moteur

**Mesures :** émissions des véhicules à moteur personnels et professionnels

**Scoring :**

- **0 :** Non suivi (ou N/A)
- **1 :** Établissement préliminaire du périmètre
- **2 :** Données de flotte basique
- **3 :** Méthodologie PCAF® pour les véhicules à moteur
- **4 :** Émissions détaillées par type de véhicule
- **5 :** Couverture complète + risque de transition

**Exemples de preuves/justifications :**

- "Non suivi"
- "Estimation des émissions de flotte basique"
- "Données détaillées par type de véhicule avec suivi de transition vers les véhicules électriques"

---

### 4\. Assurance de projets

**Mesures :** émissions de grandes infrastructures/projets d’envergure

**Scoring :**

- **0 :** Non suivi (ou N/A)
- **1 :** Établissement préliminaire du périmètre
- **2 :** Projets fortement émissifs uniquement
- **3 :** PCAF pour les projets > seuil
- **4 :** Tous les projets importants
- **5 :** Couverture complète + analyse d’impact

**Exemples de preuves/justifications :**

- "Non suivi"
- "Projets d’énergie uniquement"
- "Ensemble des infrastructures avec analyse d’impact"

---

### 5\. Traités de réassurance

**Mesures :** émissions du portefeuille de réassurance

**Scoring :**

- **0 :** Non suivi (ou N/A)
- **1 :** Établissement préliminaire du périmètre
- **2 :** Traités principaux uniquement
- **3 :** PCAF® pour les traités importants
- **4 :** Couverture de l’ensemble des traités
- **5 :** Couverture complète + engagement de la cédante

**Exemples de preuves/justifications :**

- "Non suivi"
- "10 principaux traités uniquement"
- "Portefeuille complet avec engagement de la cédante"

---

### 6\. Méthodologie d’attribution (assurance)

**Mesures :** méthode d’attribution spécifique à l’assurance

**Scoring :**

- **0 :** Aucune méthodologie (ou N/A)
- **1 :** Basique, fondé sur les primes
- **2 :** Valeur d’exposition de l’assurance (ITV)
- **3 :** Attribution d’assurance selon PCAF®
- **4 :** Méthode PCAF® + ajustement en fonction du risque
- **5 :** Données améliorées avec prévention des pertes

**Exemples de preuves/justifications :**

- "Aucune méthode"
- "Allocation basée sur les primes"
- "Méthode ITV selon PCAF avec ajustement du risque"

---

### 7\. Intégration de la souscription

**Mesures :** données d’émissions dans les décisions de souscription

**Scoring :**

- **0 :** Aucune intégration (ou N/A)
- **1 :** Sensibilité élevée
- **2 :** Prise en compte dans certains secteurs
- **3 :** Intégration à l’évaluation des risques
- **4 :** Tarification/conditions en fonction des émissions
- **5 :** Intégration complète + soutien à la transition

**Exemples de preuves/justifications :**

- "Non intégré"
- "Pris en compte uniquement pour le secteur de l’énergie"
- "Tarification sur la base des émissions avec accompagnement de la transition"

---

### 8\. Qualité des données (assurance)

**Mesures :** qualité des données d’émissions liées aux assurances

**Scoring :**

- **0 :** Absence de données (ou N/A)
- **1 :** Couverture <20 %
- **2 :** 20 %-40 %, qualité faible
- **3 :** 40 %-60 %, PCAF 3-4
- **4 :** 60 %-80 %, PCAF 2-3
- **5 :** \>80 %, PCAF <2,5

**Exemples de preuves/justifications :**

- "Absence de données"
- "Couverture de 30 %, score de qualité de 3,5"
- "Couverture de 90 %, score de qualité de 2,0"

---

## EXEMPLE : LIGNE REMPLIE

```csv
Aviva PLC,2024-12-31,Insurance,Part A,Asset Class Coverage,3,5,60.0,"5 of 10 PCAF asset classes reported (50%)",High,"Missing: Motor vehicle loans, Use of proceeds, Securitized products, Sovereign debt, Sub-sovereign debt","Need to prioritize motor loans given auto insurance business"
```

---

## CALCUL DES SCORES GLOBAUX

### Scores des parties

```
Part A Total = Sum of 8 criteria scores (max 40)
Part B Total = Sum of 2 criteria scores (max 10)
Part C Total = Sum of 8 criteria scores (max 40)

Part Percentage = (Part Total / Part Max) × 100
```

### Score global pondéré

**Pour les assureurs :**

```
Weighted Score = (Part A % × 50%) + (Part C % × 50%)
```

**Pour les banques :**

```
Weighted Score = (Part A % × 70%) + (Part B % × 30%)
```

**Pour les gestionnaires d’actifs :**

```
Weighted Score = Part A %
```

### Niveau de maturité

```
Level = Weighted Score ÷ 20 (rounded down)

0-19%   = Level 0-1 (Not Started / Initial)
20-39%  = Level 1-2 (Initial / Developing)
40-59%  = Level 2-3 (Developing / Defined)
60-79%  = Level 3-4 (Defined / Advanced)
80-100% = Level 4-5 (Advanced / Leading)
```

---

## CONSEILS POUR LES ANALYSTES

### Avant de commencer

1. **Collecter les données servant de preuve :** recueillir les rapports de durabilité, les publications TCFD, les données provenant des sites Web
2. **Lire des définitions des Parties A/B/C :** comprendre ce que couvre chaque partie
3. **Identifier le type d’institution :** cela permet de déterminer quelles parties s’appliquent
4. **Définir une date d’évaluation :** utiliser la date de clôture de la dernière période de référence

### Pendant l’évaluation

1. **Se fonder sur des preuves :** documenter les faits spécifiques appuyant chaque score
2. **Faire preuve de cohérence :** utiliser les mêmes normes pour l’ensemble des critères
3. **Indiquer la mention « N/A » de manière adaptée :** Partie B pour les assureurs, Partie C pour les banques
4. **Indiquer les incertitudes :** Utiliser « assessor_notes » pour les éléments qui ne sont pas clairs
5. **Définir des priorités :** critique pour les écarts importants, faible pour les améliorations mineures

### Après l’évaluation

1. **Calculer les totaux :** vérifier les calculs concernant les scores des différentes parties
2. **Vérifier l’importance :** les priorités correspondent-elles au type d’institution ?
3. **Vérifier la cohérence :** les critères similaires affichent-ils des scores similaires ?
4. **Documenter les écarts :** indiquer des éléments d’action clairs dans « gap_description »
5. **Exporter les données :** enregistrer pour visualisation dans Looker Studio ou analyse ultérieure

---

## ASSURANCE QUALITÉ

- [ ] L’ensemble des 18 lignes sont remplies (ou indiquées comme « N/A » lorsque cela est approprié)
- [ ] Scores compris uniquement entre 0 et 5
- [ ] Les pourcentages ont été correctement calculés
- [ ] Une preuve est documentée pour chaque score
- [ ] Les priorités sont attribuées en fonction de l’importance
- [ ] Les descriptions des écarts doivent être spécifiques et pouvoir donner lieu à des actions immédiates
- [ ] Type d’institution correctement identifié
- [ ] Parties B/C indiquées comme « N/A » si elles ne sont pas applicables

---

## ÉTAPES SUIVANTES

1. **Compléter le modèle** à l’aide de ce guide
2. **Calculer les scores** (totaux des différentes parties et total général pondéré)
3. **Exporter vers Looker Studio** (voir PCAF_Maturity_Assessment_Guide_FR.md)
4. **Créer le tableau de bord** pour la visualisation
5. **Développer un plan d’action** basé sur les écarts majeurs

---

**En cas de questions** Se reporter au guide complet : `PCAF_Maturity_Assessment_Guide.md`

**Version du modèle :** 1.0  
**Dernière mise à jour :** 9 février 2026