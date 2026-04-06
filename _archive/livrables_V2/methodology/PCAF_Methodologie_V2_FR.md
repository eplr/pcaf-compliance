# Évaluation de la conformité PCAF® – Méthodologie V2

> Version 2.0 · Mars 2026 · Sur la base de *Nouvelle_Methodologie_PCAF_V2.docx*

---

## Vue d'ensemble

Cette méthodologie évalue le niveau de maturité du reporting PCAF® des institutions financières selon **3 parties** et **11 critères**. Chaque partie donne lieu à un pourcentage de conformité indépendant ; un score global pondéré est ensuite calculé selon le type d'institution.

| Partie | Périmètre | Critères | Score maximum |
|--------|-----------|----------|---------------|
| **A** | Émissions financées | 5 | 23 pts (5+5+5+5+**3**) |
| **B** | Émissions facilitées *(banques/bancassurance uniquement)* | 3 | 13 pts (5+5+**3**) |
| **C** | Émissions liées à l'assurance *(assureurs/réassureurs/bancassurance uniquement)* | 3 | 13 pts (5+5+**3**) |

**% de conformité par partie** = score total / score maximum × 100.  
La couverture temporelle a toujours un **maximum de 3** (et non de 5).

---

## Partie A – Émissions financées (maximum 23)

### 1. Couverture des classes d'actifs `0–5`
Tableau de coefficients pondérés. Chaque classe d'actifs rapporte des points pour la couverture S1&S2 et, lorsque cela est obligatoire, pour la couverture S3. Une justification des exclusions accorde **50 %** des points applicables.

| Classe d'actifs | Coeff. S1&S2 | Coeff. S3 | Maximum |
|---|---|---|---|
| Actions cotées et obligations de sociétés | 3 | 3 | **6** |
| Prêts aux entreprises et capitaux propres non cotés | 3 | 3 | **6** |
| Financement de projets | 1 | 1 *(si pertinent)* | **2** |
| Immobilier commercial | 1 | — | **1** |
| Hypothèques | 0,5 | — | **0,5** |
| Prêts pour véhicules à moteur | 0,5 | — *(facultatif)* | **0,5** |
| Dette souveraine | 0,5 + 0,5 LULUCF | 1 | **2** |
| **Total** | | | **18** |

Score brut ÷ 18 → taux de couverture → niveau (voir *Échelle des niveaux de couverture* ci-dessous).

### 2. Score de qualité des données `0–5`
Basé sur le Data Quality Score (DQS) PCAF® moyen de l'institution (1 = données vérifiées, 5 = données estimées).

| Niveau | DQS moyen |
|---|---|
| 0 | Non divulgué |
| 1 | 4,5 – 5 |
| 2 | 3,5 – 4,5 |
| 3 | 2,5 – 3,5 |
| 4 | 1,5 – 2,5 |
| 5 | < 1,5 avec amélioration continue |

### 3. Méthode d'attribution `0–5`
0 = aucune méthode · 1 = estimation de base sans méthode claire · 2 = méthodes documentées, couverture partielle des classes d'actifs · 3 = méthodes alignées sur PCAF® par classe d'actifs · 4 = méthodes PCAF® complètes (signataire) · 5 = PCAF® + améliorations sectorielles spécifiques

### 4. Couverture du portefeuille `0–5`
0 = non déclaré · 1 = < 40 % · 2 = 40–60 % · 3 = 60–80 % · 4 = 80–95 % · 5 = > 95 %

### 5. Couverture temporelle `0–3`
0 = aucun historique · 1 = année en cours uniquement · 2 = ≥ 3 années d'historique + tendances · 3 = ≥ 3 années + tendances + projections/objectifs

---

## Partie B – Émissions facilitées (maximum 13)

Applicable aux **banques et aux bancassurances** uniquement. Cinq classes d'actifs du marché primaire (dette publique, actions publiques, private equity, dette privée, prêts syndiqués), chacune valant 2 pts (1 S1&S2 + 1 S3) → score brut maximum = 10.

| Critère | Maximum |
|---|---|
| Couverture des classes d'actifs *(taux de couverture / 10 → niveau)* | 5 |
| Méthode d'attribution *(même échelle 0–5 que la Partie A)* | 5 |
| Couverture temporelle | 3 |

---

## Partie C – Émissions liées à l'assurance (maximum 13)

Applicable aux **assureurs, réassureurs et bancassurances**.

| Branche | Coeff. S1&S2 | Coeff. S3 | Maximum |
|---|---|---|---|
| Assurance de branches commerciales | 2 | 1 | **3** |
| Réassurance – branches commerciales | 0,75 | 0,25 | **1** |
| Branches véhicule à moteur personnel | 3 | — | **3** |
| Réassurance – branches véhicule personnel | 1 | — | **1** |
| **Total** | | | **8** |

Score brut ÷ 8 → taux de couverture → niveau.

| Critère | Maximum |
|---|---|
| Couverture des classes d'actifs | 5 |
| Méthode d'attribution | 5 |
| Couverture temporelle | 3 |

---

## Échelle des niveaux de couverture (toutes parties)

Utilisée pour convertir un taux de couverture brut en niveau 0–5 pour le critère *Couverture des classes d'actifs*.

| Niveau | Taux de couverture |
|---|---|
| 0 | 0 % |
| 1 | 0 % < taux ≤ 40 % |
| 2 | 40 % < taux < 50 % |
| 3 | 50 % ≤ taux < 70 % |
| 4 | 70 % ≤ taux < 90 % |
| 5 | ≥ 90 % |

---

## Score global pondéré

| Type d'institution | Partie A | Partie B | Partie C |
|---|---|---|---|
| Banque | 70 % | 30 % | — |
| Assureur / Réassureur | 50 % | — | 50 % |
| Bancassurance | 40 % | 20 % | 40 % |
| Gestionnaire d'actifs / Autre | 100 % | — | — |

> Pour les banques dont les activités d'assurance sont intégrées aux émissions financées (ex. Commerzbank), la Partie C peut être évaluée même si elle n'est pas formellement requise ; la pondération est alors ajustée au cas par cas.

---

## Chaîne d'outils

### Prérequis
- Python ≥ 3.10
- `openpyxl`, `python-docx` (facultatif, pour la lecture des fichiers de retour client)

```bash
pip install openpyxl python-docx
```

### Fichiers de données principaux

| Fichier | Rôle |
|---|---|
| `analysis/results/corrected_compliance_data.json` | Statut de conformité par institution (statut Parties A/B/C, DQS, dette souveraine, etc.) |
| `analysis/results/pcaf_composite_scores.csv` | Scores composites par classe d'actifs (0–5) |
| `analysis/results/extended_asset_class_coverage.json` | Statut de couverture par classe d'actifs et par institution (`reported` / `partial` / `missing`) |
| `analysis/results/pcaf_v2_scores.json` | **Scores V2 vérifiés par le client** pour Nordea, Commerzbank, Ageas (référence prioritaire) |

### Scripts – à exécuter dans l'ordre

```bash
# 1. Générer les scores par critère pour les 23 institutions
python3 generate_pcaf_assessment.py
# → looker_data/pcaf_assessment_detailed.csv

# 2. Régénérer les 6 fichiers CSV Looker Studio
python3 generate_all_looker_csvs.py
# → looker_data/{asset_class_emissions, financed_emissions,
#              operational_emissions, pcaf_assessment_parts,
#              pcaf_assessment_overall, pcaf_compliance}.csv
```

### Ajout ou mise à jour de scores vérifiés
Pour ajouter une nouvelle institution avec des scores vérifiés par le client, ajouter une entrée dans `analysis/results/pcaf_v2_scores.json` en suivant la structure existante pour Nordea / Commerzbank / Ageas. Le script utilisera automatiquement ces scores à la place du calcul automatique.

---

## Résultats vérifiés (Nordea · Commerzbank · Ageas)

| Institution | Conformité A | Conformité B | Conformité C |
|---|---|---|---|
| Nordea | 18/23 = **78,3 %** | 0/13 = 0 % | N/A |
| Commerzbank | 15/23 = **65,2 %** | 0/13 = 0 % | 3/13 = **23,1 %** |
| Ageas | 11/23 = **47,8 %** | 0/13 = 0 % | 7/13 = **53,8 %** |

*Scores vérifiés par rapport au fichier de référence client `Comparaison_methodologique_-_Score_compliance_PCAF.xlsx` (section Nouvelle Méthode).*
