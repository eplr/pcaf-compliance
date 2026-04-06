# Explication du champ `coverage_percent` dans `asset_class_emissions.csv`

## Définition

Le champ `coverage_percent` représente un **pourcentage estimé de couverture du portefeuille** pour chaque classe d’actifs — c’est-à-dire la proportion des encours de l’institution dans cette classe d’actifs pour laquelle des données d’émissions sont disponibles.

## Méthode de calcul

Ce pourcentage est dérivé du **score composite** issu du fichier `pcaf_composite_scores.csv` pour chaque paire institution/classe d’actifs. Le score composite (échelle de 0 à 7, combinant les sous-scores : mention dans le rapport, donnée quantitative, couverture et qualité des données) est converti en plage de couverture selon la logique suivante :

| Score composite | Couverture estimée | Interprétation |
|---|---|---|
| 0 | 0 % | Aucun reporting sur cette classe d’actifs |
| 1 | 20 % | Mention minimale, pas de données quantitatives |
| 2 | 40 % | Mention partielle + données limitées |
| 3 | 40 % | Mention + données quantitatives partielles |
| 4 | 70 % | Bonne mention + données quantitatives ou couverture avérée |
| 5 | 70 % | Mention solide + données sur plusieurs dimensions |
| 6+ | 90 % | Couverture forte sur plusieurs dimensions |

## Limites

Il s’agit d’une **estimation par proxy**, et non d’un chiffre directement reporté par les institutions. En effet, elles sont très peu nombreuses à publier un pourcentage exact de couverture de portefeuille par classe d’actifs. Les valeurs sont donc **inférées à partir du degré de publication** observé dans les rapports de durabilité, en utilisant la méthodologie de scoring composite du projet.

---

**Version :** 1.0
**Date :** 16 mars 2026
