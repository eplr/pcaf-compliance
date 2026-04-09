# PCAF® Compliance Assessment – V3

Évaluation de la conformité PCAF® de 25 institutions financières européennes (banques, assureurs, réassureurs, gestionnaires d'actifs).

**Version** : V3 – Avril 2026
**Méthodologie** : [`methodology/PCAF_Methodologie_V3_FR.md`](methodology/PCAF_Methodologie_V3_FR.md)

---

## Structure du projet

```
pcaf-compliance/
├── generate_pcaf_assessment.py   ← Script principal : scores par critère (275 lignes)
├── generate_all_looker_csvs.py   ← Génère les 7 CSV pour Looker Studio
│
├── data/                         ← Données source (JSON/CSV)
├── output/                       ← CSV générés (7 fichiers)
├── methodology/                  ← Méthodologie V3 (document unique)
├── resources/                    ← Rapports source (PDF + texte extrait)
├── feedback/                     ← Feedbacks client (V2, V3)
└── _archive/                     ← Versions précédentes (V1, V2, dashboards, etc.)
```

## Exécution

```bash
# 1. Générer les scores détaillés pour 25 institutions
python3 generate_pcaf_assessment.py
# → output/pcaf_assessment_detailed.csv

# 2. Générer les 7 CSV Looker Studio
python3 generate_all_looker_csvs.py
# → output/*.csv
```

**Prérequis** : Python ≥ 3.10 (aucune dépendance externe pour les scripts principaux).

## Données source (`data/`)

| Fichier | Rôle |
|---|---|
| `corrected_compliance_data.json` | Statut de conformité par institution (Parts A/B/C, DQS, etc.) |
| `extended_asset_class_coverage.json` | Couverture par classe d'actifs (`reported` / `partial` / `missing`) |
| `pcaf_composite_scores.csv` | Scores composites par classe d'actifs (0–5) |
| `pcaf_v2_scores.json` | Scores vérifiés (client + lectures complètes) pour 25 institutions |
| `deep_analysis_results.json` | Résultats de l'analyse approfondie |

## Sorties (`output/`)

| Fichier | Contenu |
|---|---|
| `pcaf_assessment_detailed.csv` | 275 lignes : score + evidence par critère et institution |
| `pcaf_assessment_parts.csv` | Totaux Part A/B/C par institution |
| `pcaf_assessment_overall.csv` | Score pondéré global par institution |
| `pcaf_compliance.csv` | Statut de conformité (REPORTED/PARTIAL/MISSING) |
| `asset_class_emissions.csv` | Émissions par classe d'actifs |
| `financed_emissions.csv` | Émissions financées agrégées |
| `operational_emissions.csv` | Émissions opérationnelles |

### Colonnes clés de `pcaf_assessment_detailed.csv`

| Colonne | Description |
|---|---|
| `pcaf_signatory` | Statut PCAF : `Signatory`, `Non-signatory`, `Non-signatory (mentions PCAF)`, `Non-signatory (no mention)` |
| `verification_status` | `[VERIFIED]` = lecture complète du rapport · `[CLIENT-VERIFIED]` = validé par le client · `[UNVERIFIED]` = auto-généré · `[N/A]` = non applicable |
| `extraction_result` | Résultat de l'extraction automatique : `[NOT FOUND]` = donnée absente · `[FOUND — ...]` = donnée trouvée (à vérifier) · `[INCOMPLETE — ...]` = vérification partielle · `[No data]` = absence confirmée |
| `evidence` | Justification factuelle du score (sans tags) |

## Historique des versions

- **V1** (Mars 2026) : première version, méthodologie initiale
- **V2** (Mars 2026) : nouvelle méthodologie à 11 critères, scores client-vérifiés
- **V3** (Avril 2026) : audit systématique des extractions, corrections Portfolio Coverage (9/13 erreurs corrigées), justifications enrichies avec source/page/verbatim, scoring `partial` vs `reported` corrigé
- **V3.1** (Avril 2026) : ajout des colonnes `pcaf_signatory`, `verification_status`, `extraction_result` ; correction Crédit Agricole Portfolio Coverage (faux positif 89,2%)
