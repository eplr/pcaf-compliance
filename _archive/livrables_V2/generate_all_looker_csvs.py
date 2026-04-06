#!/usr/bin/env python3
"""
Regenerate all 6 Looker Studio CSV files for 23 financial institutions.
Sources: pcaf_assessment_detailed.csv, corrected_compliance_data.json,
         pcaf_composite_scores.csv, deep_analysis_results.json
"""

import csv
import json
import os
import math

BASE = "/Users/fidestra/Library/CloudStorage/OneDrive-fidestra/03_ACCOUNTS/Axylia/pcaf-compliance"
OUT = os.path.join(BASE, "looker_data")

# ── Load sources ────────────────────────────────────────────────────

# 1. Assessment detailed (just generated)
assessment = []
with open(os.path.join(OUT, "pcaf_assessment_detailed.csv"), "r", encoding="utf-8") as f:
    assessment = list(csv.DictReader(f))

# 2. Compliance data
with open(os.path.join(BASE, "analysis/results/corrected_compliance_data.json"), "r") as f:
    compliance = json.load(f)

# 3. Composite scores
composite = {}
with open(os.path.join(BASE, "analysis/results/pcaf_composite_scores.csv"), "r") as f:
    for row in csv.DictReader(f):
        inst = row["institution"]
        composite.setdefault(inst, {}).setdefault(row["part"], {})[row["category"]] = {
            "composite": int(row["composite"]),
            "mention": int(row["mention"]),
            "quantitative": int(row["quantitative"]),
            "coverage": int(row["coverage"]),
            "data_quality": int(row["data_quality"]),
        }

# 4. Deep analysis
with open(os.path.join(BASE, "analysis/results/deep_analysis_results.json"), "r") as f:
    deep_raw = json.load(f)
deep = {d["institution"]: d for d in deep_raw}

# ── Institution master list ─────────────────────────────────────────
INSTITUTIONS = [
    {"name": "Admiral Group",     "key": "ADMIRAL",        "comp": "Admiral Group",     "type": "Insurance",          "pcaf_type": "insurer"},
    {"name": "Ageas",             "key": "AGEAS",          "comp": "Ageas",             "type": "Insurance",          "pcaf_type": "insurer"},
    {"name": "Allianz",           "key": "ALLIANZ",        "comp": "Allianz",           "type": "Insurance",          "pcaf_type": "insurer"},
    {"name": "Amundi",            "key": "AMUNDI",         "comp": "Amundi",            "type": "Asset Manager",      "pcaf_type": "asset_manager"},
    {"name": "ASR Nederland",     "key": "ASRNEDERLAND",   "comp": "ASR Nederland",     "type": "Insurance",          "pcaf_type": "insurer"},
    {"name": "Aviva",             "key": "AVIVA",          "comp": "Aviva",             "type": "Insurance",          "pcaf_type": "insurer"},
    {"name": "AXA",               "key": "AXA",            "comp": "AXA",               "type": "Insurance",          "pcaf_type": "insurer"},
    {"name": "Commerzbank",       "key": "COMMERZBANK",    "comp": "Commerzbank",       "type": "Bank",               "pcaf_type": "bank"},
    {"name": "Crédit Agricole",   "key": "CREDITAGRICOLE", "comp": "Crédit Agricole",   "type": "Bank",               "pcaf_type": "bank"},
    {"name": "Deutsche Börse",    "key": "DEUTSCHEBOERSE", "comp": "Deutsche Börse",    "type": "Exchange",           "pcaf_type": "other"},
    {"name": "Eurazeo",           "key": "EURAZEO",        "comp": "Eurazeo",           "type": "Asset Manager",      "pcaf_type": "asset_manager"},
    {"name": "GBL",               "key": "GBL",            "comp": "GBL",               "type": "Investment Holding",  "pcaf_type": "other"},
    {"name": "KBC",               "key": "KBC",            "comp": "KBC",               "type": "Bancassurance",      "pcaf_type": "bancassurance"},
    {"name": "Legal & General",   "key": "LEGALGENERAL",   "comp": "Legal & General",   "type": "Insurance",          "pcaf_type": "insurer"},
    {"name": "NN Group",          "key": "NNGROUP",        "comp": "NN Group",          "type": "Insurance",          "pcaf_type": "insurer"},
    {"name": "Nordea",            "key": "NORDEA",         "comp": "Nordea",            "type": "Bank",               "pcaf_type": "bank"},
    {"name": "Phoenix Group",     "key": "PHOENIXGROUP",   "comp": "Phoenix Group",     "type": "Insurance",          "pcaf_type": "insurer"},
    {"name": "Santander",         "key": "SANTANDER",      "comp": "Santander",         "type": "Bank",               "pcaf_type": "bank"},
    {"name": "Schroders",         "key": "SCHRODERS",      "comp": "Schroders",         "type": "Asset Manager",      "pcaf_type": "asset_manager"},
    {"name": "Société Générale",  "key": "SOCGEN",         "comp": "Société Générale",  "type": "Bank",               "pcaf_type": "bank"},
    {"name": "Swiss Re",          "key": "SWISSRE",        "comp": "Swiss Re",          "type": "Reinsurance",        "pcaf_type": "reinsurer"},
    {"name": "UniCredit",         "key": "UNICREDIT",      "comp": "UniCredit",         "type": "Bank",               "pcaf_type": "bank"},
    {"name": "Zurich",          "key": "ZURICH",        "comp": "Zurich",           "type": "Insurance",          "pcaf_type": "insurer"},
    {"name": "ING",              "key": "ING",           "comp": "ING",              "type": "Bank",               "pcaf_type": "bank"},
    {"name": "Julius Baer",      "key": "JULIUSBAER",    "comp": "Julius Baer",      "type": "Bank",               "pcaf_type": "bank"},
]

ASSET_CLASSES = [
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


def write_csv(path, fieldnames, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print(f"  ✓ {os.path.basename(path):40s} {len(rows):>4d} rows")


# ═══════════════════════════════════════════════════════════════════
# 1. asset_class_emissions.csv
# ═══════════════════════════════════════════════════════════════════
def gen_asset_class_emissions():
    rows = []
    for inst in INSTITUTIONS:
        comp_data = composite.get(inst["comp"], {}).get("Part A", {})
        compl = compliance.get(inst["key"], {})
        financed = compl.get("financed_emissions")

        for ac in ASSET_CLASSES:
            ac_data = comp_data.get(ac, {})
            comp_score = ac_data.get("composite", 0)
            reported = comp_score > 0

            # Coverage % based on composite score (0-7 range mapped to 0-100)
            if comp_score == 0:
                coverage = 0
            elif comp_score <= 1:
                coverage = 20
            elif comp_score <= 2:
                coverage = 40
            elif comp_score <= 3:
                coverage = 40
            elif comp_score <= 4:
                coverage = 70
            elif comp_score <= 5:
                coverage = 70
            else:
                coverage = 90

            # Emissions: only for institutions with known financed emissions
            emissions = ""
            if reported and financed is not None and isinstance(financed, (int, float)):
                # Distribute proportionally (rough estimate)
                n_reported = sum(1 for a in ASSET_CLASSES
                                 if comp_data.get(a, {}).get("composite", 0) > 0)
                if n_reported > 0:
                    # Weight by composite score
                    total_comp = sum(comp_data.get(a, {}).get("composite", 0) for a in ASSET_CLASSES)
                    if total_comp > 0:
                        share = comp_score / total_comp
                        # financed is in MtCO2e for most, tCO2e for some
                        unit = compl.get("financed_unit", "unknown")
                        if unit == "MtCO2e":
                            emissions = round(financed * share, 2)
                        elif unit == "tCO2e":
                            emissions = round(financed * share / 1_000_000, 4)

            rows.append({
                "company": inst["name"],
                "year": 2024,
                "asset_class": ac,
                "emissions_million_tco2e": emissions if emissions != "" else "",
                "coverage_percent": coverage,
                "reported": "TRUE" if reported else "FALSE",
            })

    write_csv(
        os.path.join(OUT, "asset_class_emissions.csv"),
        ["company", "year", "asset_class", "emissions_million_tco2e", "coverage_percent", "reported"],
        rows,
    )


# ═══════════════════════════════════════════════════════════════════
# 2. financed_emissions.csv
# ═══════════════════════════════════════════════════════════════════
def gen_financed_emissions():
    rows = []
    for inst in INSTITUTIONS:
        compl = compliance.get(inst["key"], {})
        financed = compl.get("financed_emissions")
        unit = compl.get("financed_unit", "unknown")
        dqs = compl.get("dqs")

        # Normalize to MtCO2e
        emissions_mt = ""
        asset_class_label = "Mixed (aggregate)"
        if financed is not None:
            if isinstance(financed, (int, float)):
                if unit == "MtCO2e":
                    emissions_mt = round(financed, 2)
                elif unit == "tCO2e":
                    emissions_mt = round(financed / 1_000_000, 4)
                else:
                    emissions_mt = financed
                asset_class_label = "Mixed (aggregate)"
            elif isinstance(financed, str):
                # e.g. "87-161" for Allianz
                emissions_mt = financed
                asset_class_label = "Range estimate"

        # Coverage from assessment
        inst_rows = [r for r in assessment if r["company"] == inst["name"]
                     and r["pcaf_part"] == "Part A" and r["criterion"] == "Portfolio Coverage"]
        coverage = ""
        if inst_rows:
            score = int(inst_rows[0]["score"])
            coverage_map = {0: "", 1: 30, 2: 50, 3: 70, 4: 87, 5: 97}
            coverage = coverage_map.get(score, "")

        # DQS
        dqs_val = ""
        if dqs is not None:
            dqs_val = dqs

        rows.append({
            "company": inst["name"],
            "year": 2024,
            "category": "Category 15 - Investments",
            "emissions_million_tco2e": emissions_mt,
            "asset_class": asset_class_label,
            "coverage_percent": coverage,
            "data_quality_score": dqs_val,
        })

    write_csv(
        os.path.join(OUT, "financed_emissions.csv"),
        ["company", "year", "category", "emissions_million_tco2e", "asset_class",
         "coverage_percent", "data_quality_score"],
        rows,
    )


# ═══════════════════════════════════════════════════════════════════
# 3. operational_emissions.csv
# ═══════════════════════════════════════════════════════════════════
def gen_operational_emissions():
    rows = []

    # Known operational data from various sources
    known_ops = {
        "ADMIRAL":        {"scope_1": 542},
        "AVIVA":          {"scope_1": 7437, "scope_2_market": 413, "scope_2_location": 7360,
                           "scope_3_op": 10691, "total_market": 18541, "net": 0},
        "SANTANDER":      {"scope_1": 35503},
        "EURAZEO":        {"scope_1": 45, "scope_2_market": 80},
        "ZURICH":         {"scope_1": 1034},
        "SCHRODERS":      {"scope_1": 483},
        "LEGALGENERAL":   {"scope_2_market": 2432, "scope_2_location": 23423},
        "NNGROUP":        {"scope_2_market": 6601},
    }

    for inst in INSTITUTIONS:
        ops = known_ops.get(inst["key"], {})
        for year in [2024, 2023, 2022]:
            row = {
                "company": inst["name"],
                "year": year,
                "reporting_date": f"{year}-12-31",
                "scope_1_tco2e": ops.get("scope_1", "") if year == 2024 else "",
                "scope_2_market_tco2e": ops.get("scope_2_market", "") if year == 2024 else "",
                "scope_2_location_tco2e": ops.get("scope_2_location", "") if year == 2024 else "",
                "scope_3_operational_tco2e": ops.get("scope_3_op", "") if year == 2024 else "",
                "total_market_based_tco2e": ops.get("total_market", "") if year == 2024 else "",
                "net_emissions_tco2e": ops.get("net", "") if year == 2024 else "",
            }
            rows.append(row)

    write_csv(
        os.path.join(OUT, "operational_emissions.csv"),
        ["company", "year", "reporting_date", "scope_1_tco2e", "scope_2_market_tco2e",
         "scope_2_location_tco2e", "scope_3_operational_tco2e", "total_market_based_tco2e",
         "net_emissions_tco2e"],
        rows,
    )


# ═══════════════════════════════════════════════════════════════════
# 4. pcaf_assessment_parts.csv
# ═══════════════════════════════════════════════════════════════════
def gen_assessment_parts():
    rows = []
    for inst in INSTITUTIONS:
        name = inst["name"]
        pcaf_type = inst["pcaf_type"]

        # V2 max scores
        PART_A_MAX = 23  # 5+5+5+5+3
        PART_B_MAX = 13  # 5+5+3
        PART_C_MAX = 13  # 5+5+3

        def part_total_v2(part):
            pr = [r for r in assessment if r["company"] == name and r["pcaf_part"] == part]
            if all(str(r["score"]) == "N/A" for r in pr):
                return None
            return sum(int(r["score"]) for r in pr if str(r["score"]).lstrip("-").isdigit())

        # Part A (all institutions)
        part_a_total = part_total_v2("Part A") or 0
        part_a_pct = round((part_a_total / PART_A_MAX) * 100, 1)
        part_a_level = min(5, part_a_total // (PART_A_MAX // 5))
        rows.append({
            "company": name,
            "assessment_date": "2024-12-31",
            "pcaf_part": "Part A",
            "part_name": "Financed Emissions",
            "total_score": part_a_total,
            "max_score": PART_A_MAX,
            "percentage": part_a_pct,
            "maturity_level": part_a_level,
        })

        # Part B (banks + bancassurance)
        if pcaf_type in ("bank", "bancassurance"):
            part_b_total = part_total_v2("Part B") or 0
            part_b_pct = round((part_b_total / PART_B_MAX) * 100, 1)
            part_b_level = min(5, part_b_total // (PART_B_MAX // 5))
            rows.append({
                "company": name,
                "assessment_date": "2024-12-31",
                "pcaf_part": "Part B",
                "part_name": "Facilitated Emissions",
                "total_score": part_b_total,
                "max_score": PART_B_MAX,
                "percentage": part_b_pct,
                "maturity_level": part_b_level,
            })

        # Part C (insurers + reinsurers + bancassurance)
        if pcaf_type in ("insurer", "reinsurer", "bancassurance"):
            part_c_total_val = part_total_v2("Part C")
            if part_c_total_val is not None:
                part_c_total = part_c_total_val
                part_c_pct = round((part_c_total / PART_C_MAX) * 100, 1)
                part_c_level = min(5, part_c_total // (PART_C_MAX // 5))
                rows.append({
                    "company": name,
                    "assessment_date": "2024-12-31",
                    "pcaf_part": "Part C",
                    "part_name": "Insurance-Associated Emissions",
                    "total_score": part_c_total,
                    "max_score": PART_C_MAX,
                    "percentage": part_c_pct,
                    "maturity_level": part_c_level,
                })

    write_csv(
        os.path.join(OUT, "pcaf_assessment_parts.csv"),
        ["company", "assessment_date", "pcaf_part", "part_name", "total_score",
         "max_score", "percentage", "maturity_level"],
        rows,
    )
    return rows  # needed for overall


# ═══════════════════════════════════════════════════════════════════
# 5. pcaf_assessment_overall.csv
# ═══════════════════════════════════════════════════════════════════
def gen_assessment_overall(part_rows):
    rows = []
    for inst in INSTITUTIONS:
        name = inst["name"]
        pcaf_type = inst["pcaf_type"]

        inst_parts = [r for r in part_rows if r["company"] == name]
        part_a_pct = next((float(r["percentage"]) for r in inst_parts if r["pcaf_part"] == "Part A"), 0)
        part_b_pct = next((float(r["percentage"]) for r in inst_parts if r["pcaf_part"] == "Part B"), 0)
        part_c_pct = next((float(r["percentage"]) for r in inst_parts if r["pcaf_part"] == "Part C"), 0)

        # Weighted score per institution type
        if pcaf_type in ("insurer", "reinsurer"):
            weighted = part_a_pct * 0.5 + part_c_pct * 0.5
        elif pcaf_type == "bank":
            weighted = part_a_pct * 0.7 + part_b_pct * 0.3
        elif pcaf_type == "bancassurance":
            # KBC: weighted across all 3 parts
            weighted = part_a_pct * 0.40 + part_b_pct * 0.20 + part_c_pct * 0.40
        else:
            # Asset managers, exchanges, investment holdings
            weighted = part_a_pct

        weighted = round(weighted, 1)
        maturity = int(weighted // 20)

        maturity_labels = {
            0: "Not Started",
            1: "Initial",
            2: "Developing",
            3: "Defined",
            4: "Advanced",
            5: "Leading",
        }

        rows.append({
            "company": name,
            "assessment_date": "2024-12-31",
            "institution_type": inst["type"],
            "weighted_score": weighted,
            "maturity_level": maturity,
            "maturity_label": maturity_labels.get(maturity, "Unknown"),
            "part_a_score": part_a_pct,
            "part_b_score": part_b_pct if pcaf_type in ("bank", "bancassurance") else "N/A",
            "part_c_score": part_c_pct if pcaf_type in ("insurer", "reinsurer", "bancassurance") else "N/A",
        })

    write_csv(
        os.path.join(OUT, "pcaf_assessment_overall.csv"),
        ["company", "assessment_date", "institution_type", "weighted_score",
         "maturity_level", "maturity_label", "part_a_score", "part_b_score", "part_c_score"],
        rows,
    )


# ═══════════════════════════════════════════════════════════════════
# 6. pcaf_compliance.csv
# ═══════════════════════════════════════════════════════════════════
def gen_pcaf_compliance(part_rows):
    rows = []
    for inst in INSTITUTIONS:
        name = inst["name"]
        pcaf_type = inst["pcaf_type"]
        compl = compliance.get(inst["key"], {})
        inst_parts = [r for r in part_rows if r["company"] == name]

        # Part A (all institutions)
        pa = next((r for r in inst_parts if r["pcaf_part"] == "Part A"), None)
        if pa:
            pct = float(pa["percentage"])
            if pct >= 80:
                status = "REPORTED"
            elif pct >= 40:
                status = "PARTIAL"
            else:
                status = "MISSING"

            # Missing elements (guard against N/A scores from V2 overrides)
            inst_assessment = [r for r in assessment if r["company"] == name and r["pcaf_part"] == "Part A"]
            gaps = [r["criterion"] for r in inst_assessment
                    if str(r["score"]).lstrip("-").isdigit() and int(r["score"]) <= 1 and r["priority"] != "N/A"]
            missing = ", ".join(gaps) if gaps else "Minor gaps"

            # Priority
            if status == "MISSING":
                priority = "Critical"
            elif status == "PARTIAL":
                priority = "High"
            else:
                priority = "Low"

            rows.append({
                "company": name,
                "assessment_date": "2024-12-31",
                "pcaf_part": "Part A - Financed Emissions",
                "status": status,
                "completeness_percent": round(pct),
                "missing_elements": missing,
                "priority": priority,
            })

        # Part B (banks + bancassurance)
        if pcaf_type in ("bank", "bancassurance"):
            pb = next((r for r in inst_parts if r["pcaf_part"] == "Part B"), None)
            if pb:
                pct = float(pb["percentage"])
                if pct >= 80:
                    status = "REPORTED"
                elif pct >= 30:
                    status = "PARTIAL"
                else:
                    status = "MISSING"

                inst_b = [r for r in assessment if r["company"] == name and r["pcaf_part"] == "Part B"]
                gaps = [r["criterion"] for r in inst_b
                        if str(r["score"]).lstrip("-").isdigit() and int(r["score"]) <= 1 and r["priority"] != "N/A"]
                missing = ", ".join(gaps) if gaps else "Minor gaps"

                priority = "Critical" if status == "MISSING" else ("High" if status == "PARTIAL" else "Low")
                rows.append({
                    "company": name,
                    "assessment_date": "2024-12-31",
                    "pcaf_part": "Part B - Facilitated Emissions",
                    "status": status,
                    "completeness_percent": round(pct),
                    "missing_elements": missing,
                    "priority": priority,
                })

        # Part C (insurers + reinsurers + bancassurance)
        if pcaf_type in ("insurer", "reinsurer", "bancassurance"):
            pc = next((r for r in inst_parts if r["pcaf_part"] == "Part C"), None)
            if pc:
                pct = float(pc["percentage"])
                if pct >= 80:
                    status = "REPORTED"
                elif pct >= 20:
                    status = "PARTIAL"
                else:
                    status = "MISSING"

                inst_c = [r for r in assessment if r["company"] == name and r["pcaf_part"] == "Part C"]
                gaps = [r["criterion"] for r in inst_c
                        if int(r["score"]) <= 1 and r["priority"] not in ("N/A", "Low")]
                missing = ", ".join(gaps) if gaps else "Minor gaps"

                priority = "Critical" if status == "MISSING" else ("High" if status == "PARTIAL" else "Low")
                rows.append({
                    "company": name,
                    "assessment_date": "2024-12-31",
                    "pcaf_part": "Part C - Insurance-Associated Emissions",
                    "status": status,
                    "completeness_percent": round(pct),
                    "missing_elements": missing,
                    "priority": priority,
                })

    write_csv(
        os.path.join(OUT, "pcaf_compliance.csv"),
        ["company", "assessment_date", "pcaf_part", "status",
         "completeness_percent", "missing_elements", "priority"],
        rows,
    )


# ═══════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════
def main():
    print(f"Generating 6 CSVs for {len(INSTITUTIONS)} institutions...\n")

    gen_asset_class_emissions()
    gen_financed_emissions()
    gen_operational_emissions()
    part_rows = gen_assessment_parts()
    gen_assessment_overall(part_rows)
    gen_pcaf_compliance(part_rows)

    print(f"\n✓ All 6 CSV files generated in {OUT}")


if __name__ == "__main__":
    main()
