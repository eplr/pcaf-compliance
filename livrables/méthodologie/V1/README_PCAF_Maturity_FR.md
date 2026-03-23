# Évaluation de la maturité PCAF – guide de démarrage rapide

**Date :** 6 février 2026  
**Entreprise :** Société X  
**Score global :** 32,5 % (Niveau 1 – Phase initiale)

---

## FICHIERS CRÉÉS

### 1\. Documentation

- **`PCAF_Maturity_Assessment_Guide.md`** - Guide utilisateur complet (18 critères, méthodologie de notation)
- **`export_pcaf_maturity.py`** - Script Python pour générer des fichiers CSV
- **`README_PCAF_Maturity.md`** - Le présent guide

### 2\. Fichiers de données (pour Looker Studio)

Emplacement : `looker_data/`

- **`pcaf_assessment_detailed.csv`** - 16 lignes, scores critère par critère
- **`pcaf_assessment_parts.csv`** - 2 lignes, résumés des parties A et C
- **`pcaf_assessment_overall.csv`** - 1 ligne, score global pondéré

---

## RÉSUMÉ DES RÉSULTATS DE LA SOCIÉTÉ X (ASSURANCE)

### Partie A : émissions financées

**Score :** 26/40 (65 %) – **Niveau 3 (défini)**

| Critère| Score| Statut|
|----------|----------|----------|
| Couverture des classes d’actifs| 3/5| ⚠ Seulement 50 % des classes d’actifs PCAF®|
| Data Quality Score (score de qualité des données)| 3/5| ✓ Bon (2,5/5 en moyenne)|
| Méthode d’attribution| 4/5| ✓ Alignement PCAF®|
| Couverture des scopes| 3/5| ⚠ Scope 3 manquant|
| Couverture du portefeuille| 3/5| ✓ Couverture ~85 %|
| Dette souveraine| 3/5| ⚠ N’apparaît pas dans le total|
| Couverture temporelle| 3/5| ✓ Données sur 3 ans|
| Métriques d’intensité| 4/5| ✓ Solides|

### Partie C : émissions liées à l’assurance

**Score :** 0/40 (0 %) - **Niveau 0 (Aucune action engagée)** – **ÉCART MAJEUR**

La note de 0 est attribuée aux 8 critères – aucune émission liée à l’assurance n’est publiée.

---

## ÉTAPES SUIVANTES

### Pour la visualisation dans Looker Studio

1. **Téléverser dans Google Sheets**
   
   ```
   - Go to sheets.google.com
   - Create new spreadsheet: "PCAF Maturity - X"
   - Import 3 CSV files from looker_data/ folder
   ```

2. **Se connecter à Looker Studio**
   
   ```
   - Go to lookerstudio.google.com
   - Create → Report
   - Add Data → Google Sheets
   - Select your spreadsheet
   ```

3. **Créer les tableaux de bord**
   
   **Page 1 : Synthèse**
   
   - Fiche d’évaluation : Globale 32,5 %
   - Tableaux des niveaux : Partie A (65 %), Partie C (0 %)
   - Carte radar : Visualisation à l’aide de 18 critères
   
   **Page 2 : Détail de la partie A**
   
   - Diagramme à barres : scores des 8 critères
   - Tableau : preuves et écarts
   
   **Page 3 : Analyse des écarts vs la Partie C**
   
   - Carte de densité : 8 critères manquants
   - Matrice des priorités (4 – critique, 3 – élevée)

### Pour la société X – Actions immédiates

**6 prochains mois (priorité critique) :**

1. Mettre en œuvre le projet pilote PCAF® Partie C pour les branches commerciales + assurance véhicules à moteur
2. Ajouter 2 classes d’actifs d’émissions financées supplémentaires (prêts automobiles, produits titrisés)
3. Inclure la dette souveraine dans le total des émissions financées

**12 prochains mois (priorité élevée) :**

1. Obtenir une couverture de 50 % de la partie C (2 des 4 branches d’assurance)
2. Étendre la partie A à 7-8 classes d’actifs
3. Ajouter le scope 3 pour les principales entités investies

**Objectif :** Score global de 60 % (niveau 3) dans les 2 ans

---

## RESSOURCES CLÉS

### Ressources PCAF®

- Norme PCAF® : https://carbonaccountingfinancials.com/
- Guide Partie C PCAF® (assurance) : https://carbonaccountingfinancials.com/files/standard-launch-2025/PCAF-PartC-2025-V2-15012026.pdf

### Interne

- Rapport de durabilité ou fiche technique : `in/aviva-plc-sustainability-datasheet-2024.xlsx`
- Méthode d’analyse : `PCAF_Analysis_Methodology.md`
- Intégration à Looker Studio : `Looker_Studio_Integration_Guide.md`

---

## RÉFÉRENCE DES CRITÈRES D’ÉVALUATION

### 6 niveaux de maturité

| Niveau| Classification| Description|
|----------|----------|----------|
| 0| Aucune action engagée| Aucun reporting|
| 1| Phase initiale| Ad hoc, couverture <20 %|
| 2| Maturité en développement| Couverture 20 %- 40 %, méthodologie basique|
| 3| Méthode définie| Couverture 40 %-70 %, alignement PCAF®|
| 4| Maturité avancée| Couverture 70 %-90 %, solide|
| 5| Mature| Couverture >90 %, pratiques d’excellence|

### 18 critères d’évaluation

**Partie A (8 critères) :** couverture des classes d’actifs, qualité des données, attribution, couverture des scopes, couverture du portefeuille, dette souveraine, couverture temporelle, mesures d’intensité

**Partie B (2 critères) :** activités sur les marchés de capitaux, attribution des émissions (N/A pour les assureurs)

**Partie C (8 critères) :** couverture des branhces d’assurance, branches commerciales, assurance véhicules à moteur, assurance de projet, traités de réassurance, méthodologie d’attribution, intégration de la souscription, qualité des données

---

## FORMULE DE NOTATION

**Pour les assureurs (comme la société X) :**

```
Weighted Score = (Part A Score × 50%) + (Part C Score × 50%)
                = (26/40 × 50%) + (0/40 × 50%)
                = 32.5% + 0%
                = 32.5%
```

**Niveau de maturité :** Score / 20 = 32,5 / 20 = Niveau 1 (phase initiale)

---

## METTRE À JOUR LES INSTRUCTIONS

Pour mettre à jour l’évaluation (par exemple, pour le prochain exercice) :

1. **Modifier les données dans le script Python :**
   
   ```bash
   nano export_pcaf_maturity.py
   # Update assessment_data dictionary with new scores
   ```

2. **Générer à nouveau les fichiers CSV :**
   
   ```bash
   python3 export_pcaf_maturity.py
   ```

3. **Actualiser Looker Studio :**
   
   - Google Sheets sera automatiquement mis à jour
   - Les nouvelles données seront actualisées dans Looker Studio

---

## En cas de questions

Voir le guide complet : **`PCAF_Maturity_Assessment_Guide.md`** (Détail des 18 critères)

---

**Version du document :** 1.0  
**Dernière mise à jour :** 6 février 2026  
**Prochaine révision :** annuelle (ou après les principales mises à jour du rapport de durabilité)