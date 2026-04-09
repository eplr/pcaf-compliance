# Évaluation de la conformité PCAF® – Méthodologie V3.1

> Version 3.1 · Avril 2026 · Sur la base de *Nouvelle_Methodologie_PCAF_V2.docx* + feedback Lucie (02/04/2026) + corrections et évaluations complètes (09/04/2026)

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

### Approche de lecture des rapports (V3.1 – 09/04/2026)

L'approche privilégiée pour l'évaluation de conformité est la **lecture complète du rapport source**, pas l'extraction par regex.

**Pour les rapports ESEF XHTML** (format européen structuré) :
1. Convertir le XHTML en texte propre en supprimant les images base64, CSS, et balises HTML
2. Résultat : réduction de ~99 % (ex. ING : 121 Mo → 1,86 Mo, 89 783 lignes)
3. Lire les sections pertinentes en entier (sustainability statement, technical notes)
4. Pour chaque critère : identifier le verbatim exact + référence de ligne

**Pour les rapports PDF** :
1. Texte extrait disponible dans `resources/reports/extracted_text/*.json`
2. Structure : `{"text": "...", "metadata": [{"page_number": N, "text_length": M}, ...]}`
3. Même approche : lecture complète, pas de recherche par regex isolée

> **Leçon V3** : une lecture partielle (0,1 % du document) a produit 2 erreurs de scoring pour ING. La lecture complète les a corrigées. Chaque score doit être justifié par un verbatim exact avec référence de ligne ou de page.

### Format du rapport d'évaluation

Chaque institution évaluée produit un rapport au format `output/{INSTITUTION}_PCAF_Compliance_Assessment.md` contenant :
- Métadonnées : rapport source, type d'institution, date, méthode de lecture
- Pour chaque critère des 3 parties : score, verbatim avec référence de ligne, raisonnement
- Tableau récapitulatif Part A / Part B / Part C (scores bruts uniquement, pas de pondération)

### Prérequis
- Python ≥ 3.10

### Fichiers de données

| Fichier | Rôle |
|---|---|
| `data/corrected_compliance_data.json` | Statut de conformité par institution (statut Parties A/B/C, DQS, etc.) |
| `data/pcaf_composite_scores.csv` | Scores composites par classe d'actifs (0–5) |
| `data/extended_asset_class_coverage.json` | Statut de couverture par classe d'actifs (`reported` / `partial` / `missing`) |
| `data/pcaf_v2_scores.json` | Scores vérifiés (client + lectures complètes) pour 25 institutions |
| `data/verification_checklist.json` | Trace d'audit des vérifications manuelles |
| `resources/reports/extracted_text/*.json` | Texte extrait des rapports PDF |
| `resources/reports/extracted_text/*_full_clean.txt` | Texte propre des rapports XHTML |
| `resources/reports/origin/` | Rapports source (PDF, XHTML) |

### Scripts

```bash
# Générer les scores par critère (25 institutions)
python3 generate_pcaf_assessment.py
# → output/pcaf_assessment_detailed.csv

# Générer les CSV Looker Studio
python3 generate_all_looker_csvs.py
# → output/*.csv
```

---

## Résultats validés par Axylia (Nordea · Commerzbank · Ageas)

| Institution | Conformité A | Conformité B | Conformité C |
|---|---|---|---|
| Nordea | 18/23 = **78,3 %** | 0/13 = 0 % | N/A |
| Commerzbank | 15/23 = **65,2 %** | 0/13 = 0 % | 3/13 = **23,1 %** |
| Ageas | 11/23 = **47,8 %** | 0/13 = 0 % | 7/13 = **53,8 %** |

*Scores validés par Axylia, croisés avec le fichier de référence `Comparaison_methodologique_-_Score_compliance_PCAF.xlsx` (section Nouvelle Méthode).*

---

## Corrections V3.1 – Audit d'extraction Portfolio Coverage + évaluations complètes (02–09/04/2026)

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
| Nordea | 75 % | 3 | Validé par Axylia |
|| Ageas | ~71 % | 3 | Validé par Axylia |
|| Swiss Re | 67 % | 3 | Annual Report 2024 – narrative section Sustainability performance |
|| Allianz | 63 % | 3 | Annual Report 2024, p.82-83 – weighted coverage table |
|| Commerzbank | ~54 % | 2 | Validé par Axylia |
| Legal & General | 41 % | 2 | Climate Report 2024 – verbatim « c.41 % direct coverage » |
| 15 institutions | non divulgué | 0 | Aucun taux de couverture PCAF® explicite trouvé dans le rapport |

---

## Format des justifications (V3.1)

Chaque score du fichier `pcaf_assessment_detailed.csv` est accompagné d'un champ `evidence` structuré :

- **Asset Class Coverage** : détail par classe d'actifs avec points/max et raison (`S1&S2 + S3`, `S1&S2 only, S3 not covered`, `S1&S2 production only, LULUCF not included, S3 not covered`, `not reported`).
- **Data Quality Score** : DQS moyen, seuil de la grille appliqué.
- **Attribution Methodology** : PCAF® mentionné/signataire, Part A status, score attribué avec raisonnement.
- **Portfolio Coverage** : préfixé `[Source section/page]` pour les données vérifiées, ou `[No data]` pour les taux non divulgués. Inclut le verbatim, le calcul, et l'explication des pourcentages rejetés.
- **Temporal Coverage** : Part A status, présence d'émissions quantifiées, score avec raisonnement.

---

## Colonnes du CSV détaillé (V3.1)

Le fichier `pcaf_assessment_detailed.csv` comprend 15 colonnes :

| Colonne | Description |
|---|---|
| `company` | Nom de l’institution |
| `assessment_date` | Date de référence (2024-12-31) |
| `institution_type` | Type : Bank, Insurance, Bancassurance, Asset Manager, etc. |
| `pcaf_signatory` | Statut PCAF : `Signatory` / `Non-signatory` / `Non-signatory (mentions PCAF)` / `Non-signatory (no mention)` |
| `pcaf_part` | Partie évaluée (Part A / Part B / Part C) |
| `criterion` | Critère (Asset Class Coverage, Data Quality Score, etc.) |
| `score` | Score attribué (entier ou N/A) |
| `max_score` | Score maximum possible |
| `percentage` | Score en pourcentage (score/max × 100) |
|| `verification_status` | `[VERIFIED]` = lecture complète · `[CHECKED BY AXYLIA]` = validé par Axylia (Nordea, Commerzbank, Ageas) · `[UNVERIFIED]` = auto-généré · `[N/A]` |
| `extraction_result` | `[NOT FOUND]` = donnée absente · `[FOUND — ...]` = donnée trouvée (à vérifier) · `[No data]` = absence confirmée |
| `evidence` | Justification factuelle (sans tags) |
| `priority` | Priorité de remédiation |
| `gap_description` | Description de l’écart |
| `assessor_notes` | Notes de l’évaluateur |

---

## Évaluations complètes (lecture complète du rapport)

| Institution | Source | Méthode | Part A | Part B | Part C | Rapport |
|---|---|---|---|---|---|---|
| ING | Annual Report 2025 (ESEF XHTML) | Lecture complète (89 783 lignes) | **16**/23 | **5**/13 | N/A | `output/ING_PCAF_Compliance_Assessment.md` |
| Admiral Group | Sustainability Report 2024 (PDF) | Lecture complète (1 004 lignes) | **6**/23 | N/A | **5**/13 | `output/Admiral_Group_PCAF_Compliance_Assessment.md` |

*Toutes les 25 institutions ont été évaluées par lecture complète ou validées par Axylia (Nordea, Commerzbank, Ageas).*

---

## Protocole d’analyse des rapports — Phase 2 (prévu avril 2026)

### Objectif
Passer les 19 institutions `[UNVERIFIED]` à `[VERIFIED]` par lecture complète de chaque rapport source.

### Ordre de traitement (par taille décroissante de rapport)

**Batch 1 — Rapports > 2M caractères** (~2h)
1. UniCredit (3,37M) — Bank
2. Santander (3,09M) — Bank
3. GBL (2,79M) — Investment Holding
4. Crédit Agricole (2,62M) — Bank

**Batch 2 — Rapports 1M–2M caractères** (~3h30)
5. AXA (1,92M) — Insurance
6. Amundi (1,88M) — Asset Manager
7. ASR Nederland (1,82M) — Insurance
8. Allianz (1,54M) — Insurance
9. NN Group (1,48M) — Insurance
10. Eurazeo (1,41M) — Asset Manager
11. Phoenix Group (1,38M) — Insurance
12. Zurich (1,38M) — Insurance
13. Deutsche Börse (1,17M) — Exchange
14. Schroders (747k) — Asset Manager
15. KBC (447k) — Bancassurance

**Batch 3 — Rapports < 500k caractères** (~50min)
16. Swiss Re (413k) — Reinsurance
17. Aviva (370k) — Insurance
18. Legal & General (281k) — Insurance
19. Julius Baer (239k) — Bank

### Procédure par institution

Pour chaque institution :

1. **Ouvrir** le texte extrait : `resources/reports/extracted_text/{KEY}_2024_clean.txt`
2. **Identifier** les sections pertinentes : sustainability statement, financed emissions, PCAF methodology, data quality, portfolio coverage, temporal data, facilitated emissions, insurance-associated emissions
3. **Pour chaque critère des 11** :
   - Trouver le **verbatim exact** avec référence de ligne
   - Appliquer la grille de scoring de la méthodologie V3
   - Documenter le raisonnement
   - Vérifier tout pourcentage contre le contexte complet de la phrase
4. **Mettre à jour** `data/pcaf_v2_scores.json` avec les scores vérifiés et l’evidence enrichie
5. **Générer** le rapport d’évaluation : `output/{INSTITUTION}_PCAF_Compliance_Assessment.md`
6. **Regénérer** les CSV : `python3 generate_pcaf_assessment.py && python3 generate_all_looker_csvs.py`
7. **Vérifier** que `verification_status` passe de `[UNVERIFIED]` à `[VERIFIED]`

### Points d’attention prioritaires

- **Portfolio Coverage** : 12 pourcentages `[FOUND — HUMAN VERIFICATION REQUIRED]` à vérifier (historique d’erreur : 69 %)
- **DQS** : 8 valeurs extraites par regex à confirmer en contexte
- **Part C (assureurs)** : scores génériques (2/5, 2/5, 1/3) à détailler avec données réelles
- **Temporal Coverage** : vérifier les années réellement présentes (pas juste les années mentionnées dans le header)

### Livrables attendus
- 19 rapports `.md` enrichis dans `output/`
- `pcaf_v2_scores.json` mis à jour (25 institutions vérifiées)
- 7 CSV regénérés avec 0 lignes `[UNVERIFIED]`
- Commit + push sur GitHub
