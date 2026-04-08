# Institutions financières et PCAF® — Étude de conformité

## Synthèse des travaux

---

### 1. Avant-propos

La présente étude porte sur **23 institutions financières** européennes, signataires ou non de l'initiative Partnership for Carbon Accounting Financials® (PCAF). L'échantillon comprend des banques, assureurs, réassureurs, gestionnaires d'actifs et holdings d'investissement.

Sur son site Web, PCAF indique mettre à disposition les publications de ses membres signataires à des fins de transparence. L'initiative précise toutefois que l'intégration de ces publications ne constitue pas une certification ou validation quant au degré d'alignement effectif d'un rapport versus le standard PCAF.

Cette précision est d'autant plus fondamentale au regard des difficultés méthodologiques persistantes, notamment concernant les émissions de scope 3 et les activités d'assurance, où « la qualité des données et la disponibilité de la méthodologie constituent des difficultés pour la prise de décision et le reporting. »

---

### 2. Méthodologie

La méthode appliquée à la présente étude compte **quatre phases** :

**Phase 1 — Extraction du référentiel PCAF**

Extraction des catégories d'émissions du standard PCAF, structuré en trois parties :

- **Partie A** : Émissions financées (financed emissions)
- **Partie B** : Émissions facilitées (facilitated emissions)
- **Partie C** : Émissions liées aux activités d'assurance (insurance-associated emissions)

Les données structurées sont disponibles au format JSON (pcaf_emissions_categories.json).

**Phase 2 — Extraction des données d'émissions**

Extraction des données à partir des rapports annuels et documents d'enregistrement universel (DEU) des 23 institutions financières concernées.

**Phase 3 — Analyse comparative**

Mise en perspective des données extraites versus le référentiel PCAF. Cette phase constitue le cœur de l'analyse, permettant de dériver les indicateurs de conformité, les scores de maturité et les écarts identifiés.

**Phase 4 — Analyse sémantique et terminologique**

Extraction terminologique du standard PCAF et analyse sémantique des parties extra-financières des DEU versus le corpus PCAF. L'objectif est de croiser ces résultats avec ceux des phases précédentes.

---

### 3. Résultats

#### 3.1 Vue d'ensemble

| Indicateur | Résultat |
|------------|----------|
| Institutions analysées | 23 |
| Mention de PCAF | 21/23 (91 %) |
| Signataires PCAF confirmés | 14/23 (61 %) |
| Partie A (émissions financées) complète | 9/23 (39 %) |
| DQS documenté | 12/23 (52 %) |
| Score moyen d'adhérence aux recommandations | 57,2 % |

#### 3.2 Conformité par partie du standard

**Partie A — Émissions financées**

- **Statut « reported »** : 9 institutions (39 %) — Allianz, ASR Nederland, Aviva, AXA, Nordea, Phoenix Group, Santander, Swiss Re, UniCredit
- **Statut « partial »** : 12 institutions (52 %) — reporting incomplet ou sans méthodologie PCAF explicite
- **Statut « missing »** : 2 institutions (9 %) — Amundi, Deutsche Börse

**Partie B — Émissions facilitées**

Applicable principalement aux banques d'investissement. Parmi les 6 banques de l'échantillon, 5 rapportent partiellement les émissions facilitées (Commerzbank, Crédit Agricole, Nordea, Santander, Société Générale). Aucune institution ne déclare une couverture complète.

**Partie C — Émissions d'assurance**

Parmi les 12 assureurs/réassureurs de l'échantillon :

- **Statut « partial »** : 12/12 (100 %)
- Aucun assureur ne rapporte intégralement les émissions de la Partie C

#### 3.3 Qualité des données (Data Quality Score)

Le DQS mesure la fiabilité des données sources sur une échelle de 1 (optimal) à 5 (estimations sectorielles). Sur les 23 institutions :

| DQS | Institutions |
|-----|--------------|
| 1 (optimal) | Aviva, Commerzbank, NN Group, Santander |
| 2 | Allianz, AXA, Legal & General |
| 3 | Swiss Re |
| 4 | Nordea |
| 5 | ASR Nederland, UniCredit |
| Non documenté | 12 institutions (52 %) |

**Constat clé** : La moitié des institutions ne publie pas de DQS explicite, limitant la comparabilité des données.

#### 3.4 Couverture par classe d'actifs

L'analyse de la couverture des **10 classes d'actifs** du standard PCAF (Partie A) révèle des écarts significatifs :

**Partie A — Émissions financées (10 classes)**

| Classe d'actifs | Couverture complète | Partielle | Absente |
|-----------------|---------------------|-----------|---------|
| Actions cotées et obligations | 39 % | 43 % | 13 % |
| Prêts aux entreprises / actions non cotées | 74 % | 22 % | 4 % |
| Financement de projets | 26 % | 35 % | 39 % |
| Immobilier commercial | 61 % | 26 % | 13 % |
| Crédits hypothécaires résidentiels | 83 % | 13 % | 4 % |
| Prêts pour véhicules à moteur | 48 % | 17 % | 35 % |
| Utilisation des produits | 39 % | 22 % | 39 % |
| Produits titrisés et structurés | 35 % | 9 % | 57 % |
| Dette souveraine | 74 % | 17 % | 9 % |
| Dette sub-souveraine | 17 % | 17 % | 65 % |

**Partie B — Émissions facilitées (2 classes)**

| Classe d'actifs | Couverture complète | Partielle | N/A |
|-----------------|---------------------|-----------|---------|
| Marchés de capitaux | 35 % | 4 % | 61 % |
| Services de conseil | 35 % | — | 65 % |

**Partie C — Émissions d'assurance (1 classe)**

| Classe d'actifs | Couverture complète | Partielle | N/A |
|-----------------|---------------------|-----------|---------|
| Souscription d'assurance | 48 % | 17 % | 35 % |

**Points d'attention** : Les produits titrisés/structurés (57 % absents) et la dette sub-souveraine (65 % absents) présentent les lacunes les plus importantes. Le financement de projets et les prêts véhicules restent également sous-couverts (39 % et 35 % absents respectivement).

---

### 4. Matrice de maturité

L'évaluation multicritère positionne les institutions selon leur niveau de maturité PCAF :

**Leaders (>80 %)** — 5 institutions

- Nordea (92,3 %), ASR Nederland (87,5 %), Santander (84,6 %), AXA (84,4 %), NN Group (84,4 %)

**Avancés (60-80 %)** — 8 institutions

- Allianz, Swiss Re, Zurich, Commerzbank, UniCredit, Aviva, Legal & General, Phoenix Group

**En développement (40-60 %)** — 4 institutions

- KBC, Schroders, Admiral, Deutsche Börse

**Émergents (<40 %)** — 6 institutions

- Société Générale, GBL, Amundi, Ageas, Crédit Agricole, Eurazeo

---

### 5. Analyse des écarts

#### 5.1 Écarts critiques identifiés

1. **Absence de méthodologie PCAF** (2 institutions)
   - Amundi : gestionnaire d'actifs sans mention PCAF ni émissions financées déclarées
   - Deutsche Börse : opérateur de marché sans adoption du standard

2. **DQS non documenté** (12 institutions)
   - Lacune majeure affectant la comparabilité inter-institutions

3. **Partie C inexistante** (tous les assureurs)
   - Aucun reporting complet des émissions liées à la souscription d'assurance

4. **Émissions facilitées parcellaires** (toutes les banques concernées)
   - Les activités de marchés de capitaux et de conseil restent peu couvertes

#### 5.2 Écarts terminologiques et sémantiques

L'analyse textuelle révèle que si 91 % des institutions mentionnent PCAF, l'intégration terminologique varie considérablement :

- **Intégration forte** (>40 mentions) : Nordea, NN Group, Commerzbank, Santander
- **Intégration faible** (<5 mentions) : Amundi, Deutsche Börse, Admiral, Eurazeo, GBL

Cette corrélation entre densité terminologique et maturité de conformité suggère que l'adoption formelle du lexique PCAF précède généralement une implémentation méthodologique approfondie.

---

### 6. Recommandations

#### 6.1 Priorité 1 — Actions immédiates

Pour **Amundi** et **Deutsche Börse** :

- Adhérer à l'initiative PCAF
- Implémenter la méthodologie Partie A pour les émissions financées
- Établir un calendrier de mise en conformité sur 12-18 mois

#### 6.2 Priorité 2 — Renforcement du reporting

Pour les institutions en statut « partial » :

- **Consolider les émissions financées totales** : Commerzbank, Crédit Agricole, Legal & General, NN Group, Société Générale, Zurich
- **Documenter explicitement le DQS** : 12 institutions concernées
- **Étendre la couverture** aux classes d'actifs manquantes (financement de projets, prêts véhicules)

#### 6.3 Priorité 3 — Amélioration continue

Pour les leaders et avancés :

- Améliorer la qualité des données (cible DQS 2-3)
- Développer le reporting Partie C pour les assureurs
- Réduire les incertitudes sur les estimations Scope 3

---

### 7. Conclusion

Cette étude révèle une **adoption généralisée mais inégale** du standard PCAF parmi les institutions financières européennes. Si 91 % mentionnent l'initiative et 61 % sont signataires, seules 39 % présentent un reporting Partie A complet avec méthodologie documentée.

Les principaux axes de progression concernent :

- La **documentation systématique du DQS** (absente pour 52 % de l'échantillon)
- L'**extension aux Parties B et C** du standard, actuellement sous-couvertes
- L'**homogénéisation des pratiques** pour permettre une véritable comparabilité sectorielle

Le tableau de bord HTML accompagnant cette synthèse permet une exploration interactive des résultats détaillés par institution, classe d'actifs et critère d'évaluation.

---

*Étude réalisée pour Axylia — Février 2025*

*Données sources : Documents d'enregistrement universel 2024 des institutions analysées*
