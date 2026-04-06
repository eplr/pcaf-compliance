# Note méthodologique – analyse PCAF® – répartition de couverture par quantiles

**Date :** 2 mars 2026
**Fichier associé :** `pcaf_quantile_analysis_FR.xlsx`

---

## 1. Rappel du contexte

L’analyse évalue la conformité de 23 institutions financières européennes au standard PCAF® (*Partnership for Carbon Accounting Financials*), structuré en trois volets :

- **Partie A** – émissions financées (10 classes d’actifs)
- **Partie B** – émissions facilitées (activités de marché de capitaux)
- **Partie C** – émissions liées à l’assurance (4 branches d’assurance)

---

## 2. Méthode de scoring

Chaque catégorie (classe d’actifs, branche d’assurance ou émission facilitée) est évaluée pour chaque institution sur un **score composite de 0 à 12**, somme de 4 dimensions notées de 0 à 3 :

### Grille de notation

**Mention (0–3)**
- 0 = Absente
- 1 = Qualitative (mot-clé trouvé)
- 2 = Dans un contexte émissions (mot-clé + emission/carbon/tCO2 à proximité)
- 3 = Contexte PCAF explicite (mot-clé + « pcaf » à proximité)

**Donnée quantitative (0–3)**
- 0 = Absente
- 1 = Total agrégé (chiffre + unité tCO2/MtCO2/million)
- 2 = Par scope (scope 1/2 mentionnés à proximité)
- 3 = Par scope + intensité (WACI, ECI, EVIC, per €M…)

**Couverture (0–3)**
- 0 = Non indiquée
- 1 = Mentionnée (mot « coverage » ou « couverture »)
- 2 = Supérieure à 50 %
- 3 = Supérieure à 80 %

**Qualité des données (0–3)**
- 0 = Non indiquée
- 1 = Mentionnée (« data quality » ou « quality score »)
- 2 = Score chiffré présent (entre 1 et 5)
- 3 = Score PCAF ≤ 2,5 (bonne qualité)

---

## 3. Classification : seuils empiriques par catégorie

La classification REPORTING RÉALISÉ / PARTIEL / MANQUANT repose sur la **distribution des scores du panel** (23 institutions). Le seuil pour qu’un reporting soit considéré comme « réalisé » (REPORTING RÉALISÉ) est fixé au **Q3 (75e percentile)** de chaque catégorie. Ce seuil varie donc d’une catégorie à l’autre.

### Règle de classification

- **MANQUANT** : score = 0 (aucune occurrence/mention dans le rapport)
- **PARTIEL** : 0 < score ≤ Q3 (mention et/ou données partielles, en-dessous du 75e percentile du panel)
- **REPORTING RÉALISÉ** : score > Q3 (reporting supérieur à 75 % des pairs)

*Cas particulier :* lorsque le Q3 = 0 (quasiment aucune institution ne couvre la catégorie), un seuil absolu de 4/12 s’applique.

### Partie A – émissions financées (10 classes d’actifs)

| Classe d’actifs | Médiane | Seuil REPORTING RÉALISÉ (Q3) |
|---|---|---|
| Actions cotées et obligations | 2 | > 3 |
| Prêts aux entreprises et actions non cotées | 0 | > 1 |
| Financement de projets | 0 | > 1 |
| Immobilier commercial | 1 | > 2 |
| Hypothèques | 1 | > 2 |
| Prêts pour véhicules à moteur | 0 | > 2 |
| Utilisation des produits | 2 | > 2 |
| Produits titrisés et structurés | 1 | > 2 |
| Dette souveraine | 2 | > 3 |
| Dette sub-souveraine | 1 | > 2 |

### Partie B – émissions facilitées

| Catégorie | Médiane | Seuil REPORTING RÉALISÉ (Q3) |
|---|---|---|
| Émissions facilitées | 1 | > 2 |

### Partie C – émissions liées aux activités d’assurance (4 branches)

| Branche d’assurance | Médiane | Seuil REPORTING RÉALISÉ (Q3) |
|---|---|---|
| Branches commerciales | 1 | > 2 |
| Véhicule à moteur personnel | 0 | > 3 |
| Assurance de projets | 0 | ≥ 4 (seuil absolu) |
| Traités de réassurance | 1 | > 1 |

---

## 4. Résultats clés du panel

### Distribution globale des classifications

- **Partie A** (230 observations) : 16 % REPORTING RÉALISÉ, 53 % PARTIEL, 31 % MANQUANT
- **Partie B** (23 observations) : 9 % REPORTING RÉALISÉ, 74 % PARTIEL, 17 % MANQUANT
- **Partie C** (92 observations) : 11 % REPORTING RÉALISÉ, 30 % PARTIEL, 59 % MANQUANT

### Lecture des seuils

Les seuils sont **relatifs au panel** :

- Les classes bien couvertes par l’ensemble des institutions (Actions cotées, Dette souveraine, Véhicule à moteur personnel) ont un Q3 plus élevé (3), ce qui exige un reporting plus complet pour être classé REPORTING RÉALISÉ.
- Les classes peu couvertes (Prêts aux entreprises, Financement de projets, Traités de réassurance) ont un Q3 bas (1) — il suffit de peu pour se distinguer.
- La branche « Assurance de projets » n’est couverte par aucune institution du panel (Q3 = 0) ; le seuil absolu de 4/12 s’applique.

---

## 5. Contenu du fichier Excel

| Onglet | Contenu |
|---|---|
| **Matrice de classification** | Matrice ✓/◐/✗ par institution × catégorie, regroupée par niveau de couverture (élevée ≥ 80 %, moyenne 60–80 %, faible < 60 %) |
| **Scores composites** | Scores composites (0–12) avec dégradé coloré par intensité |
| **Seuils en quantiles** | Statistiques descriptives (min, Q1, médiane, Q3, max) et seuils par catégorie |
| **Synthèse par institution** | Synthèse par institution et par Partie PCAF® (statut, comptages REPORTING RÉALISÉ/PARTIEL/MANQUANT, éléments manquants) |

### Légende des symboles (Matrice de classification)

- ✓ (vert) = REPORTING RÉALISÉ — reporting au-dessus du Q3 du panel
- ◐ (jaune) = PARTIEL — reporting détecté mais en-dessous du Q3
- ✗ (rouge) = MANQUANT — aucun reporting détecté
- — (gris) = N/A — catégorie non applicable au type d’institution

---

## 6. Points de vigilance

- Les seuils sont **relatifs au panel étudié** : un reporting classé REPORTING RÉALISÉ signifie « au-dessus du 75e percentile de ce panel de 23 institutions », pas nécessairement « conforme à 100 % au standard PCAF® ».
- La branche **Assurance de projets** n’est couverte par aucune institution du panel (Q3 = 0), ce qui limite la significativité du seuil pour cette catégorie.
- La taille du panel (n = 23) implique que les quantiles sont sensibles à l’ajout ou au retrait d’institutions.
