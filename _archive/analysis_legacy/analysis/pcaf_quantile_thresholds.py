#!/usr/bin/env python3
"""
PCAF Quantile-Based Thresholds
Calculates composite scores per asset class / insurance line / facilitated emissions,
then derives empirical REPORTED/PARTIAL/MISSING thresholds from the panel distribution.

Output:
  - pcaf_composite_scores.csv        : score détaillé par institution × classe d'actifs
  - pcaf_quantile_thresholds.csv     : seuils Q1/médiane/Q3 par classe d'actifs + Part B/C
  - pcaf_quantile_classification.csv : classification finale (REPORTED/PARTIAL/MISSING)
  - pcaf_quantile_summary.csv        : résumé par institution (remplacement de pcaf_compliance.csv)
"""

import json
import re
import csv
import os
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional, Dict, List
import statistics

# ──────────────────────────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────────────────────────
REPORTS_DIR = Path("/Users/fidestra/Library/CloudStorage/OneDrive-fidestra/03_ACCOUNTS/Axylia/pcaf-compliance/resources/reports/extracted_text")
OUTPUT_DIR = Path("/Users/fidestra/Library/CloudStorage/OneDrive-fidestra/03_ACCOUNTS/Axylia/pcaf-compliance/analysis/results")

INSTITUTIONS = {
    "ADMIRAL": {"type": "insurer", "country": "UK", "name": "Admiral Group"},
    "AGEAS": {"type": "insurer", "country": "Belgium", "name": "Ageas"},
    "ALLIANZ": {"type": "insurer", "country": "Germany", "name": "Allianz"},
    "AMUNDI": {"type": "asset_manager", "country": "France", "name": "Amundi"},
    "ASRNEDERLAND": {"type": "insurer", "country": "Netherlands", "name": "ASR Nederland"},
    "AVIVA": {"type": "insurer", "country": "UK", "name": "Aviva"},
    "AXA": {"type": "insurer", "country": "France", "name": "AXA"},
    "COMMERZBANK": {"type": "bank", "country": "Germany", "name": "Commerzbank"},
    "CREDITAGRICOLE": {"type": "bank", "country": "France", "name": "Crédit Agricole"},
    "DEUTSCHEBOERSE": {"type": "other", "country": "Germany", "name": "Deutsche Börse"},
    "EURAZEO": {"type": "asset_manager", "country": "France", "name": "Eurazeo"},
    "GBL": {"type": "other", "country": "Belgium", "name": "GBL"},
    "KBC": {"type": "bancassurance", "country": "Belgium", "name": "KBC"},
    "LEGALGENERAL": {"type": "insurer", "country": "UK", "name": "Legal & General"},
    "NNGROUP": {"type": "insurer", "country": "Netherlands", "name": "NN Group"},
    "NORDEA": {"type": "bank", "country": "Finland", "name": "Nordea"},
    "PHOENIXGROUP": {"type": "insurer", "country": "UK", "name": "Phoenix Group"},
    "SANTANDER": {"type": "bank", "country": "Spain", "name": "Santander"},
    "SCHRODERS": {"type": "asset_manager", "country": "UK", "name": "Schroders"},
    "SOCGEN": {"type": "bank", "country": "France", "name": "Société Générale"},
    "SWISSRE": {"type": "reinsurer", "country": "Switzerland", "name": "Swiss Re"},
    "UNICREDIT": {"type": "bank", "country": "Italy", "name": "UniCredit"},
    "ZURICH": {"type": "insurer", "country": "Switzerland", "name": "Zurich"},
}

PCAF_REQUIREMENTS = {
    "insurer":       {"part_a": True, "part_b": False, "part_c": True},
    "reinsurer":     {"part_a": True, "part_b": False, "part_c": True},
    "bank":          {"part_a": True, "part_b": True,  "part_c": False},
    "asset_manager": {"part_a": True, "part_b": False, "part_c": False},
    "bancassurance": {"part_a": True, "part_b": True,  "part_c": True},
    "other":         {"part_a": True, "part_b": False, "part_c": False},
}

# ──────────────────────────────────────────────────────────────────
# Part A : 10 classes d'actifs PCAF
# Keywords par classe, avec variantes
# ──────────────────────────────────────────────────────────────────
ASSET_CLASS_KEYWORDS = {
    "Listed equity and corporate bonds": [
        "listed equity", "corporate bond", "equity and bonds", "public equity",
        "listed shares", "equity portfolio", "bond portfolio"
    ],
    "Business loans and unlisted equity": [
        "business loan", "corporate loan", "sme loan", "commercial lending",
        "corporate lending", "business lending", "commercial loans", "unlisted equity"
    ],
    "Project finance": [
        "project finance", "infrastructure finance", "project-finance"
    ],
    "Commercial real estate": [
        "commercial real estate", "real estate debt", "commercial property",
        "office building", "retail property"
    ],
    "Mortgages": [
        "mortgage", "residential mortgage", "home loan", "housing loan",
        "residential real estate", "housing finance"
    ],
    "Motor vehicle loans": [
        "motor vehicle", "auto loan", "car loan", "vehicle finance",
        "auto finance", "car finance"
    ],
    "Use of proceeds": [
        "use of proceeds", "green bond", "sustainability bond",
        "social bond", "sustainable bond", "sustainability-linked"
    ],
    "Securitized and structured products": [
        "securiti", "abs ", "mbs ", "structured product", "asset-backed",
        "mortgage-backed", "clo ", "collateralized", "structured finance"
    ],
    "Sovereign debt": [
        "sovereign debt", "government bond", "sovereigns", "sovereign bond",
        "government securities"
    ],
    "Sub-sovereign debt": [
        "sub-sovereign", "municipal", "local government", "regional government",
        "municipal bond"
    ],
}

# Part C : lignes d'assurance PCAF
INSURANCE_LINE_KEYWORDS = {
    "Commercial lines": [
        "commercial line", "commercial insurance", "p&c ",
        "property and casualty", "commercial propert"
    ],
    "Personal motor": [
        "motor insurance", "auto insurance", "vehicle insurance",
        "car insurance", "personal motor"
    ],
    "Project insurance": [
        "project insurance", "infrastructure insurance"
    ],
    "Treaty reinsurance": [
        "reinsurance", "treaty reinsurance", "ceded", "cedant"
    ],
}

# Part B : facilitated emissions
FACILITATED_KEYWORDS = [
    "facilitated emission", "capital market", "underwriting emission",
    "debt issuance", "equity issuance", "capital markets facilitat"
]


# ──────────────────────────────────────────────────────────────────
# Scoring functions (0–3 per dimension, max composite = 12)
# ──────────────────────────────────────────────────────────────────

def score_mention(text_lower: str, keywords: List[str]) -> int:
    """
    0 = aucune mention
    1 = mention qualitative (keyword trouvé)
    2 = mention dans un contexte émissions (keyword + emission/carbon/tco2 dans ±500 chars)
    3 = mention PCAF explicite (keyword + 'pcaf' dans ±500 chars)
    """
    best = 0
    for kw in keywords:
        idx = text_lower.find(kw)
        if idx == -1:
            continue
        best = max(best, 1)
        # Contexte émissions
        window = text_lower[max(0, idx - 200):idx + len(kw) + 500]
        emission_terms = ["emission", "tco2", "carbon", "ghg", "co2e", "carbon footprint"]
        if any(t in window for t in emission_terms):
            best = max(best, 2)
        # Contexte PCAF
        if "pcaf" in window:
            best = max(best, 3)
    return best


def score_quantitative(text: str, text_lower: str, keywords: List[str]) -> int:
    """
    0 = pas de donnée chiffrée
    1 = un total agrégé trouvé (chiffre + unité dans ±300 chars)
    2 = données par scope (scope 1/2 mentionnés à proximité)
    3 = données par scope + intensité (intensity/per €/per million)
    """
    best = 0
    for kw in keywords:
        idx = text_lower.find(kw)
        if idx == -1:
            continue
        window = text[max(0, idx - 100):idx + len(kw) + 400]
        window_lower = window.lower()

        # Chiffre + unité
        if re.search(r'\d[\d,\.]*\s*(tco2|mtco2|million|kt|mt\b|tonnes)', window_lower):
            best = max(best, 1)
            # Par scope
            if re.search(r'scope\s*[12]', window_lower):
                best = max(best, 2)
            # Intensité
            if re.search(r'(intensit|per\s*(€|eur|million|m€|meur)|waci|eci|evic)', window_lower):
                best = max(best, 3)
    return best


def score_coverage(text_lower: str, keywords: List[str]) -> int:
    """
    0 = couverture non mentionnée
    1 = couverture mentionnée (coverage/couverture)
    2 = couverture > 50 %
    3 = couverture > 80 %
    """
    best = 0
    for kw in keywords:
        idx = text_lower.find(kw)
        if idx == -1:
            continue
        window = text_lower[max(0, idx - 200):idx + len(kw) + 500]
        if "coverage" in window or "couverture" in window:
            best = max(best, 1)
            # Chercher un pourcentage
            pct_matches = re.findall(r'(\d{1,3}(?:[,\.]\d+)?)\s*%', window)
            for p in pct_matches:
                try:
                    val = float(p.replace(",", "."))
                    if val > 80:
                        best = max(best, 3)
                    elif val > 50:
                        best = max(best, 2)
                    else:
                        best = max(best, 1)
                except ValueError:
                    pass
    return best


def score_data_quality(text_lower: str, keywords: List[str]) -> int:
    """
    0 = qualité non mentionnée
    1 = PCAF data quality mentionné
    2 = score chiffré présent
    3 = score ≤ 2.5 (bonne qualité)
    """
    best = 0
    for kw in keywords:
        idx = text_lower.find(kw)
        if idx == -1:
            continue
        window = text_lower[max(0, idx - 200):idx + len(kw) + 500]
        if "data quality" in window or "quality score" in window:
            best = max(best, 1)
            # Score chiffré
            dq_matches = re.findall(r'(?:score|quality)[:\s]*(\d(?:\.\d+)?)', window)
            for dq in dq_matches:
                try:
                    val = float(dq)
                    if 1.0 <= val <= 5.0:
                        best = max(best, 2)
                        if val <= 2.5:
                            best = 3
                except ValueError:
                    pass
    return best


def compute_composite_score(text: str, text_lower: str, keywords: List[str]) -> Dict[str, int]:
    """Calcule le score composite (0-12) et les 4 sous-scores."""
    mention = score_mention(text_lower, keywords)
    quant = score_quantitative(text, text_lower, keywords)
    cov = score_coverage(text_lower, keywords)
    dq = score_data_quality(text_lower, keywords)
    return {
        "mention": mention,
        "quantitative": quant,
        "coverage": cov,
        "data_quality": dq,
        "composite": mention + quant + cov + dq,
    }


# ──────────────────────────────────────────────────────────────────
# Quantile calculation + threshold derivation
# ──────────────────────────────────────────────────────────────────

def compute_quantiles(values: List[float]) -> Dict[str, float]:
    """Calcule Q1, médiane, Q3 pour une liste de valeurs."""
    if not values:
        return {"q1": 0, "median": 0, "q3": 0, "min": 0, "max": 0, "mean": 0}
    s = sorted(values)
    n = len(s)
    q1_idx = n // 4
    q3_idx = (3 * n) // 4
    return {
        "min": s[0],
        "q1": s[q1_idx],
        "median": statistics.median(s),
        "q3": s[q3_idx],
        "max": s[-1],
        "mean": round(statistics.mean(s), 2),
    }


def classify(score: float, q_median: float, q3: float) -> str:
    """
    Classification basée sur les quantiles du panel :
      - MISSING  : score = 0
      - PARTIAL  : 0 < score ≤ médiane
      - REPORTED : score > Q3

    Cas intermédiaire (médiane < score ≤ Q3) :
      - PARTIAL+ (traité comme PARTIAL dans le CSV simplifié)

    Note : si Q3 = 0 (majorité du panel à 0), on abaisse le seuil :
      - score > 0 → PARTIAL
      - score ≥ 4  → REPORTED (seuil absolu minimal)
    """
    if score == 0:
        return "MISSING"

    # Cas dégénéré : le panel est quasi-entièrement à 0
    if q3 == 0:
        if score >= 4:
            return "REPORTED"
        return "PARTIAL"

    if score > q3:
        return "REPORTED"
    if score > q_median:
        return "PARTIAL"  # PARTIAL+ dans la version détaillée
    return "PARTIAL"


# ──────────────────────────────────────────────────────────────────
# Main analysis
# ──────────────────────────────────────────────────────────────────

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Charger et scorer tous les rapports
    print("=" * 80)
    print("PCAF QUANTILE-BASED THRESHOLDS")
    print("=" * 80)

    all_scores = []  # Rows: (institution, category, part, sub-scores, composite)
    json_files = sorted(REPORTS_DIR.glob("*.json"))
    print(f"\nRapports trouvés : {len(json_files)}")

    for filepath in json_files:
        code = filepath.stem.replace("_2024", "")
        info = INSTITUTIONS.get(code, {"type": "other", "country": "?", "name": code})
        inst_name = info["name"]
        inst_type = info["type"]

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        text = data.get("text", "")
        text_lower = text.lower()

        print(f"  Scoring : {inst_name} ({inst_type})")

        # Part A : 10 classes d'actifs
        for ac_name, keywords in ASSET_CLASS_KEYWORDS.items():
            scores = compute_composite_score(text, text_lower, keywords)
            all_scores.append({
                "institution": inst_name,
                "institution_type": inst_type,
                "country": info["country"],
                "part": "Part A",
                "category": ac_name,
                **scores,
            })

        # Part B : facilitated emissions (score unique)
        reqs = PCAF_REQUIREMENTS.get(inst_type, {})
        scores_b = compute_composite_score(text, text_lower, FACILITATED_KEYWORDS)
        all_scores.append({
            "institution": inst_name,
            "institution_type": inst_type,
            "country": info["country"],
            "part": "Part B",
            "category": "Facilitated emissions",
            **scores_b,
        })

        # Part C : 4 lignes d'assurance
        for line_name, keywords in INSURANCE_LINE_KEYWORDS.items():
            scores_c = compute_composite_score(text, text_lower, keywords)
            all_scores.append({
                "institution": inst_name,
                "institution_type": inst_type,
                "country": info["country"],
                "part": "Part C",
                "category": line_name,
                **scores_c,
            })

    # ──────────────────────────────────────────────────────────
    # 2. Exporter les scores composites bruts
    # ──────────────────────────────────────────────────────────
    scores_path = OUTPUT_DIR / "pcaf_composite_scores.csv"
    with open(scores_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "institution", "institution_type", "country", "part", "category",
            "mention", "quantitative", "coverage", "data_quality", "composite"
        ])
        writer.writeheader()
        writer.writerows(all_scores)
    print(f"\n✓ Scores composites : {scores_path}")

    # ──────────────────────────────────────────────────────────
    # 3. Calculer les quantiles par catégorie
    # ──────────────────────────────────────────────────────────
    categories = set((r["part"], r["category"]) for r in all_scores)
    quantiles = {}

    for part, cat in sorted(categories):
        values = [r["composite"] for r in all_scores if r["part"] == part and r["category"] == cat]
        q = compute_quantiles(values)
        quantiles[(part, cat)] = q

    # Exporter les quantiles
    thresholds_path = OUTPUT_DIR / "pcaf_quantile_thresholds.csv"
    with open(thresholds_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "part", "category", "n", "min", "q1", "median", "q3", "max", "mean",
            "seuil_partial", "seuil_reported"
        ])
        for (part, cat), q in sorted(quantiles.items()):
            n = len([r for r in all_scores if r["part"] == part and r["category"] == cat])
            # Seuils dérivés
            seuil_partial = "> 0"
            if q["q3"] == 0:
                seuil_reported = ">= 4 (seuil absolu)"
            else:
                seuil_reported = f"> {q['q3']:.1f} (Q3)"
            writer.writerow([
                part, cat, n,
                q["min"], q["q1"], q["median"], q["q3"], q["max"], q["mean"],
                seuil_partial, seuil_reported
            ])
    print(f"✓ Quantiles et seuils : {thresholds_path}")

    # ──────────────────────────────────────────────────────────
    # 4. Classifier chaque institution × catégorie
    # ──────────────────────────────────────────────────────────
    classified = []
    for row in all_scores:
        key = (row["part"], row["category"])
        q = quantiles[key]
        status = classify(row["composite"], q["median"], q["q3"])
        classified.append({
            **row,
            "q1": q["q1"],
            "median": q["median"],
            "q3": q["q3"],
            "status": status,
        })

    classification_path = OUTPUT_DIR / "pcaf_quantile_classification.csv"
    with open(classification_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "institution", "institution_type", "country", "part", "category",
            "mention", "quantitative", "coverage", "data_quality", "composite",
            "q1", "median", "q3", "status"
        ])
        writer.writeheader()
        writer.writerows(classified)
    print(f"✓ Classification détaillée : {classification_path}")

    # ──────────────────────────────────────────────────────────
    # 5. Résumé par institution × Part (comparable à pcaf_compliance.csv)
    # ──────────────────────────────────────────────────────────
    summary = []
    institutions_list = sorted(set(r["institution"] for r in classified))

    for inst in institutions_list:
        inst_rows = [r for r in classified if r["institution"] == inst]
        inst_type = inst_rows[0]["institution_type"]
        reqs = PCAF_REQUIREMENTS.get(inst_type, {})

        for part_key, part_label, required in [
            ("Part A", "Part A - Financed Emissions", reqs.get("part_a", True)),
            ("Part B", "Part B - Facilitated Emissions", reqs.get("part_b", False)),
            ("Part C", "Part C - Insurance Emissions", reqs.get("part_c", False)),
        ]:
            if not required:
                continue

            part_rows = [r for r in inst_rows if r["part"] == part_key]
            if not part_rows:
                continue

            composites = [r["composite"] for r in part_rows]
            statuses = [r["status"] for r in part_rows]
            avg_composite = round(sum(composites) / len(composites), 2)
            max_composite = max(composites)

            reported_count = statuses.count("REPORTED")
            partial_count = statuses.count("PARTIAL")
            missing_count = statuses.count("MISSING")
            total = len(statuses)

            # Statut global de la Part : basé sur la proportion
            reported_pct = reported_count / total * 100
            non_missing_pct = (reported_count + partial_count) / total * 100

            if reported_pct > 50:
                part_status = "REPORTED"
            elif non_missing_pct > 50:
                part_status = "PARTIAL"
            elif non_missing_pct > 0:
                part_status = "PARTIAL"
            else:
                part_status = "MISSING"

            # Missing elements
            missing_cats = [r["category"] for r in part_rows if r["status"] == "MISSING"]
            missing_str = "; ".join(missing_cats[:4]) if missing_cats else "None"

            summary.append({
                "institution": inst,
                "institution_type": inst_type,
                "part": part_label,
                "status": part_status,
                "avg_composite_score": avg_composite,
                "max_composite_score": max_composite,
                "reported_count": reported_count,
                "partial_count": partial_count,
                "missing_count": missing_count,
                "total_categories": total,
                "completeness_pct": round(non_missing_pct, 1),
                "missing_elements": missing_str,
            })

    summary_path = OUTPUT_DIR / "pcaf_quantile_summary.csv"
    with open(summary_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "institution", "institution_type", "part", "status",
            "avg_composite_score", "max_composite_score",
            "reported_count", "partial_count", "missing_count", "total_categories",
            "completeness_pct", "missing_elements"
        ])
        writer.writeheader()
        writer.writerows(summary)
    print(f"✓ Résumé par institution : {summary_path}")

    # ──────────────────────────────────────────────────────────
    # 6. Afficher les seuils par catégorie
    # ──────────────────────────────────────────────────────────
    print("\n" + "=" * 80)
    print("SEUILS EMPIRIQUES PAR CATÉGORIE (basés sur les quantiles du panel)")
    print("=" * 80)

    for (part, cat), q in sorted(quantiles.items()):
        seuil_r = f"> {q['q3']:.0f} (Q3)" if q["q3"] > 0 else ">= 4 (absolu)"
        print(f"  {part} - {cat:<45} "
              f"Q1={q['q1']:<4} med={q['median']:<5} Q3={q['q3']:<4} "
              f"→ PARTIAL: >0   REPORTED: {seuil_r}")

    # ──────────────────────────────────────────────────────────
    # 7. Stats globales
    # ──────────────────────────────────────────────────────────
    print("\n" + "=" * 80)
    print("DISTRIBUTION DES CLASSIFICATIONS")
    print("=" * 80)

    for part_key in ["Part A", "Part B", "Part C"]:
        part_classified = [r for r in classified if r["part"] == part_key]
        if not part_classified:
            continue
        total = len(part_classified)
        rep = sum(1 for r in part_classified if r["status"] == "REPORTED")
        par = sum(1 for r in part_classified if r["status"] == "PARTIAL")
        mis = sum(1 for r in part_classified if r["status"] == "MISSING")
        print(f"\n  {part_key}:")
        print(f"    REPORTED : {rep:>3} ({rep/total*100:5.1f}%)")
        print(f"    PARTIAL  : {par:>3} ({par/total*100:5.1f}%)")
        print(f"    MISSING  : {mis:>3} ({mis/total*100:5.1f}%)")

    print("\n" + "=" * 80)
    print(f"Fichiers générés dans : {OUTPUT_DIR}")
    print("=" * 80)


if __name__ == "__main__":
    main()
