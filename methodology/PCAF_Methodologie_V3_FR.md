# Évaluation de la conformité PCAF® – Méthodologie V3

> Version 3.0 · Avril 2026 · Sur la base de *Nouvelle_Methodologie_PCAF_V2.docx* + feedback Lucie (02/04/2026)

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

> **Scoring `partial` vs `reported` (V3)** : une classe d'actifs au statut `partial` ne reçoit que les points S1&S2 (pas de crédit S3). Seul le statut `reported` accorde les points S1&S2 **et** S3. Pour la dette souveraine, `partial` = production S1&S2 uniquement (0,5 pt), sans LULUCF ni S3.

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

> **Règle de cohérence (V3)** : lorsque le taux de couverture du portefeuille n'est pas explicitement divulgué dans le rapport de durabilité, le score est systématiquement **0** (« non déclaré »), quel que soit le niveau de reporting global de l'institution. L'outil ne doit **jamais** estimer un score > 0 à partir d'indices indirects (ex. % d'objectifs de décarbonation, % de Covered Bonds, etc.).
>
> **Règle de vérification contextuelle des pourcentages (V3)** : tout pourcentage extrait d'un rapport de durabilité doit être vérifié contre la phrase complète et son contexte. Un pourcentage peut se rapporter à un objet différent de la couverture PCAF® :
> - **Classification SFDR** (ex. KBC : « 92% of assets » = fonds Article 8/9, pas couverture PCAF®)
> - **Staging IFRS 9** (ex. ING : « 92.0% » = qualité Stage 1, pas couverture émissions)
> - **Cibles SBTi** (ex. Julius Baer : « 49% » = investissements dans des entreprises avec cibles SBTi)
> - **Objectifs net zero** (ex. Legal & General : « 100% of AUM » = objectif 2050, couverture réelle = 41%)
> - **Primes Part C** (ex. Swiss Re : « 90% » = couverture assurance branches commerciales, investissements = 34%)
> - **Cibles d'engagement** (ex. Zurich : « 65% » = engagement auprès d'entreprises sans SBT, pas couverture portefeuille)
> - **Classification de risque** (ex. UniCredit : « 90% » = clients risque Medium/Low)
> - **Contrats non pertinents** (ex. ASR Nederland : « 99% » = contrats verts de leasing, couverture PCAF réelle = 77%)
>
> L'audit V3 a révélé que **9 des 13 pourcentages** initialement extraits étaient issus d'un contexte erroné.

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
| `analysis/results/corrected_compliance_data.json` | Statut de conformité par institution (statut Parties A/B/C, DQS, etc.) |
| `analysis/results/pcaf_composite_scores.csv` | Scores composites par classe d'actifs (0–5) |
| `analysis/results/extended_asset_class_coverage.json` | Statut de couverture par classe d'actifs et par institution (`reported` / `partial` / `missing`). **Source pour la dette souveraine et toutes les classes d'actifs (V3).** |
| `analysis/results/pcaf_v2_scores.json` | **Scores V2 vérifiés par le client** pour Nordea, Commerzbank, Ageas (référence prioritaire) |
| `resources/reports/extracted_text/*.json` | Texte extrait des rapports de durabilité source – utilisé pour l'audit V3 des extractions |

### Scripts – à exécuter dans l'ordre

```bash
# 1. Générer les scores par critère pour les 25 institutions
python3 generate_pcaf_assessment.py
# → looker_data/pcaf_assessment_detailed.csv

# 2. Régénérer les 6 fichiers CSV Looker Studio
python3 generate_all_looker_csvs.py
# → looker_data/{asset_class_emissions, financed_emissions,
#              operational_emissions, pcaf_assessment_parts,
#              pcaf_assessment_overall, pcaf_compliance}.csv

# 3. Synchroniser vers livrables/V3
cp looker_data/*.csv livrables/V3/looker_data/
cp looker_data/*.csv livrables/V3/data/
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

---

## Corrections V3 – Audit d'extraction Portfolio Coverage (02–06/04/2026)

Suite au feedback de Lucie, un audit systématique de **tous** les pourcentages de couverture portefeuille a été réalisé contre les rapports source (dossier `resources/reports/extracted_text/`). Résultat : **9 des 13 extractions initiales étaient erronées**, et 3 couvertures supplémentaires ont été trouvées dans les tableaux des rapports.

### Corrections d'extraction (9 erreurs)

| Institution | V2 | V3 | Erreur |
|---|---|---|---|
| ASR Nederland | 99 % → score 5 | **77 %** → score 3 | 99 % = contrats verts hectares |
| ING | 92 % → score 4 | **non divulgué** → score 0 | 92 % = IFRS 9 Stage 1 |
| Julius Baer | 49 % → score 2 | **non divulgué** → score 0 | 49 % = cibles SBTi |
| KBC | 92 % → score 4 | **non divulgué** → score 0 | 92 % = classification SFDR |
| Legal & General | 100 % → score 5 | **41 %** → score 2 | 100 % = objectif net zero 2050 |
| Schroders | 97 % → score 5 | **non divulgué** → score 0 | 97 % = Scope 3 opérationnel |
| Swiss Re | 90 % → score 4 | **67 %** → score 3 | 90 % = primes Part C assurance (34 % était 2023 ; 67 % est la donnée 2024 du narrative) |
| UniCredit | 90 % → score 4 | **non divulgué** → score 0 | 90 % = classification risque clients |
| Zurich | 65 % → score 3 | **non divulgué** → score 0 | 65 % = cible engagement SBT |

### Couvertures trouvées dans les tableaux des rapports (3 ajouts)

| Institution | V2 | V3 | Source |
|---|---|---|---|
| Allianz | non divulgué → score 0 | **63 %** → score 3 | Table p.82-83, section E1 : coverage pondérée (Corporates 79,5 %, Public debt 99,5 %, Real estate 20,3 %, No methodology 0 %) |
| NN Group | non divulgué → score 0 | **80 %** → score 4 | Table « Financed emissions » : 80 % des actifs propriétaires inclus dans le calcul GHG |
| Swiss Re | 34 % → score 1 | **67 %** → score 3 | Narrative : « 67 % of its overall investment portfolio is covered in terms of absolute GHG emissions » |

### Récapitulatif final des 25 institutions – Portfolio Coverage

| Institution | Taux | Score | Source |
|---|---|---|---|
| Aviva | 95 % | 4 | Climate Report 2024 – verbatim « coverage has increased to 95 % » |
| AXA | 86,9 % | 4 | URD 2024 – verbatim « coverage rate stands at 86.9 % » |
| NN Group | 80 % | 4 | Annual Report 2024 – table financed emissions (propriétaire) |
| ASR Nederland | 77 % | 3 | Annual Report 2024, section E1-6 – table S1&S2 coverage |
| Nordea | 75 % | 3 | Client-vérifié |
| Ageas | ~71 % | 3 | Client-vérifié |
| Swiss Re | 67 % | 3 | Annual Report 2024 – narrative section Sustainability performance |
| Allianz | 63 % | 3 | Annual Report 2024, p.82-83 – weighted coverage table |
| Commerzbank | ~54 % | 2 | Client-vérifié |
| Legal & General | 41 % | 2 | Climate Report 2024 – verbatim « c.41 % direct coverage » |
| 15 institutions | non divulgué | 0 | Aucun taux de couverture PCAF® explicite trouvé dans le rapport |

---

## Format des justifications (V3)

Chaque score du fichier `pcaf_assessment_detailed.csv` est accompagné d'un champ `evidence` structuré :

- **Asset Class Coverage** : détail par classe d'actifs avec points/max et raison (`S1&S2 + S3`, `S1&S2 only, S3 not covered`, `S1&S2 production only, LULUCF not included, S3 not covered`, `not reported`).
- **Data Quality Score** : DQS moyen, seuil de la grille appliqué.
- **Attribution Methodology** : PCAF® mentionné/signataire, Part A status, score attribué avec raisonnement.
- **Portfolio Coverage** : préfixé `[Source section/page]` pour les données vérifiées, ou `[No data]` pour les taux non divulgués. Inclut le verbatim, le calcul, et l'explication des pourcentages rejetés.
- **Temporal Coverage** : Part A status, présence d'émissions quantifiées, score avec raisonnement.

---

## Résultats finaux V3 – 25 institutions (06/04/2026)

| Institution | Type | Part A | Part B | Part C | Pondéré |
|---|---|---|---|---|---|
| Swiss Re | Réassurance | 73,9 % | — | 69,2 % | **71,6 %** |
| AXA | Assurance | 78,3 % | — | 61,5 % | **69,9 %** |
| Allianz | Assurance | 78,3 % | — | 53,8 % | **66,0 %** |
| ASR Nederland | Assurance | 60,9 % | — | 61,5 % | **61,2 %** |
| Santander | Banque | 69,6 % | 30,8 % | — | **58,0 %** |
| ING | Banque | 69,6 % | 23,1 % | — | **55,6 %** |
| Nordea | Banque | 78,3 % | 0 % | — | **54,8 %** |
| KBC | Bancassurance | 47,8 % | 69,2 % | 53,8 % | **54,5 %** |
| Ageas | Assurance | 47,8 % | — | 53,8 % | **50,8 %** |
| Aviva | Assurance | 82,6 % | — | 15,4 % | **49,0 %** |
| UniCredit | Banque | 52,2 % | 30,8 % | — | **45,8 %** |
| Commerzbank | Banque | 65,2 % | 0 % | — | **45,6 %** |
| NN Group | Assurance | 65,2 % | — | 23,1 % | **44,2 %** |
| Schroders | Gest. d'actifs | 43,5 % | — | — | **43,5 %** |
| Zurich | Assurance | 30,4 % | — | 53,8 % | **42,1 %** |
| Legal & General | Assurance | 56,5 % | — | 23,1 % | **39,8 %** |
| Julius Baer | Banque | 52,2 % | 0 % | — | **36,5 %** |
| Admiral Group | Assurance | 17,4 % | — | 53,8 % | **35,6 %** |
| Phoenix Group | Assurance | 52,2 % | — | 15,4 % | **33,8 %** |
| Eurazeo | Gest. d'actifs | 30,4 % | — | — | **30,4 %** |
| Société Générale | Banque | 26,1 % | 30,8 % | — | **27,5 %** |
| Deutsche Börse | Bourse | 26,1 % | — | — | **26,1 %** |
| GBL | Holding | 26,1 % | — | — | **26,1 %** |
| Crédit Agricole | Banque | 17,4 % | 23,1 % | — | **19,1 %** |
| Amundi | Gest. d'actifs | 8,7 % | — | — | **8,7 %** |

### Vérification de cohérence

- **275 lignes** générées pour 25 institutions (5 critères Part A + 3 Part B + 3 Part C)
- **Scores pondérés** : 25/25 vérifiés (detailed → parts → overall)
- **Evidence** : 25/25 Portfolio Coverage avec référence `[Source]`, 22/22 critères auto avec justification du score
- **Compliance** : 1 REPORTED, 30 PARTIAL, 15 MISSING (46 entrées)
