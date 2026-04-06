#!/usr/bin/env python3
"""
PCAF Quantile Charts — Graphiques à barres
Génère des visualisations des scores composites et seuils par quantiles.
"""

import csv
import locale
from pathlib import Path
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

RESULTS_DIR = Path("/Users/fidestra/Library/CloudStorage/OneDrive-fidestra/03_ACCOUNTS/Axylia/pcaf-compliance/analysis/results")
OUTPUT_DIR = RESULTS_DIR / "charts"

# ── Formatage FR : virgule décimale, espace insécable milliers ──
def fr_formatter(x, pos=None):
    """Formatte un nombre avec virgule décimale et espace insécable milliers."""
    if x == int(x):
        s = f"{int(x):,}".replace(",", "\u202f")
    else:
        s = f"{x:,.1f}".replace(",", "\u202f").replace(".", ",")
    return s

# ── Couleurs cohérentes avec le fichier Excel ──
COLOR_REPORTED = "#66BB6A"   # vert
COLOR_PARTIAL  = "#FFEE58"   # jaune
COLOR_MISSING  = "#EF5350"   # rouge
COLOR_Q3       = "#1565C0"   # bleu foncé (seuil REPORTED)
COLOR_MEDIAN   = "#FF8F00"   # orange (médiane)
COLOR_Q1       = "#8D6E63"   # brun (Q1)
COLOR_BG       = "#FAFAFA"

PART_A_CATS = [
    "Listed equity and corporate bonds",
    "Business loans and unlisted equity",
    "Project finance",
    "Commercial real estate",
    "Mortgages",
    "Motor vehicle loans",
    "Use of proceeds",
    "Securitized and structured products",
    "Sovereign debt",
    "Sub-sovereign debt",
]
SHORT_LABELS = {
    "Listed equity and corporate bonds": "Listed eq.\n& bonds",
    "Business loans and unlisted equity": "Business\nloans",
    "Project finance": "Project\nfinance",
    "Commercial real estate": "Commercial\nreal estate",
    "Mortgages": "Mortgages",
    "Motor vehicle loans": "Motor\nvehicle loans",
    "Use of proceeds": "Use of\nproceeds",
    "Securitized and structured products": "Securitized\nproducts",
    "Sovereign debt": "Sovereign\ndebt",
    "Sub-sovereign debt": "Sub-sovereign\ndebt",
    "Facilitated emissions": "Facilitated\nemissions",
    "Commercial lines": "Commercial\nlines",
    "Personal motor": "Personal\nmotor",
    "Project insurance": "Project\ninsurance",
    "Treaty reinsurance": "Treaty\nreinsurance",
}


def load_csv(filename):
    with open(RESULTS_DIR / filename, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def chart1_scores_by_category(scores, thresholds):
    """
    Graphique 1 : Score composite moyen par catégorie (Part A)
    avec barres empilées par dimension + lignes de seuils Q3/médiane.
    """
    # Agréger par catégorie
    cat_dims = defaultdict(lambda: {"mention": [], "quantitative": [], "coverage": [], "data_quality": []})
    for row in scores:
        if row["part"] != "Part A":
            continue
        cat = row["category"]
        for dim in ["mention", "quantitative", "coverage", "data_quality"]:
            cat_dims[cat][dim].append(int(row[dim]))

    cats = PART_A_CATS
    labels = [SHORT_LABELS.get(c, c) for c in cats]

    mention_avg    = [np.mean(cat_dims[c]["mention"]) for c in cats]
    quant_avg      = [np.mean(cat_dims[c]["quantitative"]) for c in cats]
    coverage_avg   = [np.mean(cat_dims[c]["coverage"]) for c in cats]
    dq_avg         = [np.mean(cat_dims[c]["data_quality"]) for c in cats]

    # Seuils
    thresh_map = {}
    for row in thresholds:
        if row["part"] == "Part A":
            thresh_map[row["category"]] = {"median": float(row["median"]), "q3": float(row["q3"])}

    medians = [thresh_map.get(c, {}).get("median", 0) for c in cats]
    q3s     = [thresh_map.get(c, {}).get("q3", 0) for c in cats]

    x = np.arange(len(cats))
    width = 0.55

    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor(COLOR_BG)
    ax.set_facecolor(COLOR_BG)

    # Barres empilées
    b1 = ax.bar(x, mention_avg, width, label="Mention (0–3)", color="#90CAF9")
    b2 = ax.bar(x, quant_avg, width, bottom=mention_avg, label="Quantitative (0–3)", color="#CE93D8")
    b3 = ax.bar(x, coverage_avg, width,
                bottom=[m + q for m, q in zip(mention_avg, quant_avg)],
                label="Coverage (0–3)", color="#FFB74D")
    b4 = ax.bar(x, dq_avg, width,
                bottom=[m + q + c for m, q, c in zip(mention_avg, quant_avg, coverage_avg)],
                label="Data Quality (0–3)", color="#A5D6A7")

    # Lignes de seuils
    for i, (med, q3) in enumerate(zip(medians, q3s)):
        if i == 0:
            ax.plot([i - 0.35, i + 0.35], [med, med], color=COLOR_MEDIAN, linewidth=2.5,
                    label="Median (panel)" if i == 0 else None)
            ax.plot([i - 0.35, i + 0.35], [q3, q3], color=COLOR_Q3, linewidth=2.5, linestyle="--",
                    label="Q3 → seuil REPORTED" if i == 0 else None)
        else:
            ax.plot([i - 0.35, i + 0.35], [med, med], color=COLOR_MEDIAN, linewidth=2.5)
            ax.plot([i - 0.35, i + 0.35], [q3, q3], color=COLOR_Q3, linewidth=2.5, linestyle="--")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8.5, ha="center")
    ax.set_ylabel("Score composite moyen (0–12)", fontsize=11)
    ax.set_title("Part A — Score composite par classe d'actifs\n(moyennes des 23 institutions + seuils quantiles)",
                 fontsize=13, fontweight="bold", pad=12)
    ax.set_ylim(0, 12)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(fr_formatter))
    ax.legend(loc="upper right", fontsize=9, framealpha=0.9)
    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()
    path = OUTPUT_DIR / "chart1_part_a_scores_by_category.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  ✓ {path.name}")


def chart2_institution_coverage(classification):
    """
    Graphique 2 : Barres empilées REPORTED/PARTIAL/MISSING par institution
    (toutes Parts applicables confondues).
    """
    from collections import OrderedDict

    PCAF_REQS = {
        "insurer":       {"part_a": True, "part_b": False, "part_c": True},
        "reinsurer":     {"part_a": True, "part_b": False, "part_c": True},
        "bank":          {"part_a": True, "part_b": True,  "part_c": False},
        "asset_manager": {"part_a": True, "part_b": False, "part_c": False},
        "bancassurance": {"part_a": True, "part_b": True,  "part_c": True},
        "other":         {"part_a": True, "part_b": False, "part_c": False},
    }

    # Compter par institution (catégories applicables uniquement)
    inst_data = defaultdict(lambda: {"REPORTED": 0, "PARTIAL": 0, "MISSING": 0, "total": 0})
    for row in classification:
        inst = row["institution"]
        itype = row["institution_type"]
        part = row["part"]
        reqs = PCAF_REQS.get(itype, {"part_a": True})
        part_key = f"part_{part.split(' ')[1].lower()}"
        if not reqs.get(part_key, False):
            continue
        inst_data[inst][row["status"]] += 1
        inst_data[inst]["total"] += 1

    # Trier par % REPORTED décroissant
    def sort_key(item):
        d = item[1]
        return -(d["REPORTED"] / d["total"]) if d["total"] else 0

    sorted_insts = sorted(inst_data.items(), key=sort_key)
    names = [i[0] for i in sorted_insts]
    rep = [i[1]["REPORTED"] for i in sorted_insts]
    par = [i[1]["PARTIAL"] for i in sorted_insts]
    mis = [i[1]["MISSING"] for i in sorted_insts]

    y = np.arange(len(names))
    height = 0.6

    fig, ax = plt.subplots(figsize=(12, 9))
    fig.patch.set_facecolor(COLOR_BG)
    ax.set_facecolor(COLOR_BG)

    ax.barh(y, rep, height, label="REPORTED", color=COLOR_REPORTED)
    ax.barh(y, par, height, left=rep, label="PARTIAL", color=COLOR_PARTIAL)
    ax.barh(y, mis, height, left=[r + p for r, p in zip(rep, par)], label="MISSING", color=COLOR_MISSING)

    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=9)
    ax.set_xlabel("Nombre de catégories (applicables)", fontsize=11)
    ax.set_title("Classification par institution\n(catégories PCAF applicables uniquement)",
                 fontsize=13, fontweight="bold", pad=12)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(fr_formatter))
    ax.legend(loc="lower right", fontsize=10, framealpha=0.9)
    ax.invert_yaxis()
    ax.grid(axis="x", alpha=0.3)

    fig.tight_layout()
    path = OUTPUT_DIR / "chart2_institution_coverage.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  ✓ {path.name}")


def chart3_all_parts_thresholds(thresholds, scores):
    """
    Graphique 3 : Toutes catégories (A + B + C) — scores moyens vs seuils
    """
    ALL_CATS = (
        PART_A_CATS
        + ["Facilitated emissions"]
        + ["Commercial lines", "Personal motor", "Project insurance", "Treaty reinsurance"]
    )

    cat_composites = defaultdict(list)
    for row in scores:
        cat_composites[(row["part"], row["category"])].append(int(row["composite"]))

    thresh_map = {}
    for row in thresholds:
        thresh_map[(row["part"], row["category"])] = {
            "q1": float(row["q1"]), "median": float(row["median"]), "q3": float(row["q3"])
        }

    # Préparer les données dans l'ordre ALL_CATS
    ordered_keys = []
    for cat in ALL_CATS:
        if cat in PART_A_CATS:
            ordered_keys.append(("Part A", cat))
        elif cat == "Facilitated emissions":
            ordered_keys.append(("Part B", cat))
        else:
            ordered_keys.append(("Part C", cat))

    labels = [SHORT_LABELS.get(k[1], k[1]) for k in ordered_keys]
    means = [np.mean(cat_composites.get(k, [0])) for k in ordered_keys]
    q3s = [thresh_map.get(k, {}).get("q3", 0) for k in ordered_keys]
    medians_v = [thresh_map.get(k, {}).get("median", 0) for k in ordered_keys]

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(16, 7))
    fig.patch.set_facecolor(COLOR_BG)
    ax.set_facecolor(COLOR_BG)

    # Zones de couleur pour les parts
    ax.axvspan(-0.5, 9.5, alpha=0.06, color="#1565C0", label="Part A")
    ax.axvspan(9.5, 10.5, alpha=0.06, color="#6A1B9A", label="Part B")
    ax.axvspan(10.5, 14.5, alpha=0.06, color="#E65100", label="Part C")

    ax.bar(x - width / 2, means, width, label="Score moyen (panel)", color="#64B5F6", edgecolor="#1565C0", linewidth=0.5)
    ax.bar(x + width / 2, q3s, width, label="Seuil Q3 (REPORTED)", color=COLOR_Q3, alpha=0.7, edgecolor="#0D47A1", linewidth=0.5)

    # Ligne médiane
    ax.plot(x, medians_v, "o-", color=COLOR_MEDIAN, linewidth=1.5, markersize=5, label="Médiane (panel)", zorder=5)

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8, ha="center")
    ax.set_ylabel("Score composite (0–12)", fontsize=11)
    ax.set_title("Score moyen vs seuil REPORTED par catégorie\n(Parts A, B et C — 23 institutions)",
                 fontsize=13, fontweight="bold", pad=12)
    ax.set_ylim(0, 8)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(fr_formatter))
    ax.legend(loc="upper right", fontsize=9, framealpha=0.9, ncol=2)
    ax.grid(axis="y", alpha=0.3)

    # Annotations Parts
    ax.text(4.5, 7.5, "Part A — Financed Emissions", ha="center", fontsize=10, fontstyle="italic", color="#1565C0")
    ax.text(10, 7.5, "B", ha="center", fontsize=10, fontstyle="italic", color="#6A1B9A")
    ax.text(12.5, 7.5, "Part C — Insurance", ha="center", fontsize=10, fontstyle="italic", color="#E65100")

    fig.tight_layout()
    path = OUTPUT_DIR / "chart3_all_parts_thresholds.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  ✓ {path.name}")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Chargement des données...")
    scores = load_csv("pcaf_composite_scores.csv")
    thresholds = load_csv("pcaf_quantile_thresholds.csv")
    classification = load_csv("pcaf_quantile_classification.csv")

    print("\nGénération des graphiques :")
    chart1_scores_by_category(scores, thresholds)
    chart2_institution_coverage(classification)
    chart3_all_parts_thresholds(thresholds, scores)

    print(f"\n✓ Graphiques générés dans : {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
