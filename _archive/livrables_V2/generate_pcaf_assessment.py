#!/usr/bin/env python3
"""
Generate pcaf_assessment_detailed.csv for 23 financial institutions.
PCAF Methodology V2 – 5 criteria (Part A) + 3 criteria (Part B) + 3 criteria (Part C).

Part A max = 23  (5+5+5+5+3)
Part B max = 13  (5+5+3)
Part C max = 13  (5+5+3)

Manual V2 scores for Nordea, Commerzbank, Ageas loaded from
analysis/results/pcaf_v2_scores.json (client-verified).
All other institutions are scored algorithmically from existing data.
"""

import csv
import json
import os

BASE = "/Users/fidestra/Library/CloudStorage/OneDrive-fidestra/03_ACCOUNTS/Axylia/pcaf-compliance"

# ── Load data sources ───────────────────────────────────────────────

composite = {}
with open(os.path.join(BASE, "analysis/results/pcaf_composite_scores.csv"), "r") as f:
    for row in csv.DictReader(f):
        inst = row["institution"]
        part = row["part"]
        cat  = row["category"]
        composite.setdefault(inst, {}).setdefault(part, {})[cat] = {
            "mention":      int(row["mention"]),
            "quantitative": int(row["quantitative"]),
            "coverage":     int(row["coverage"]),
            "data_quality": int(row["data_quality"]),
            "composite":    int(row["composite"]),
        }

with open(os.path.join(BASE, "analysis/results/corrected_compliance_data.json"), "r") as f:
    compliance = json.load(f)

with open(os.path.join(BASE, "analysis/results/extended_asset_class_coverage.json"), "r") as f:
    ext_coverage_all = json.load(f)

with open(os.path.join(BASE, "analysis/results/pcaf_v2_scores.json"), "r") as f:
    v2_manual = json.load(f)

# ── Institution list ────────────────────────────────────────────────

INSTITUTIONS = {
    "Admiral Group":   {"key": "ADMIRAL",        "composite_key": "Admiral Group",   "type": "Insurance",         "pcaf_type": "insurer"},
    "Ageas":           {"key": "AGEAS",           "composite_key": "Ageas",           "type": "Insurance",         "pcaf_type": "insurer"},
    "Allianz":         {"key": "ALLIANZ",         "composite_key": "Allianz",         "type": "Insurance",         "pcaf_type": "insurer"},
    "Amundi":          {"key": "AMUNDI",          "composite_key": "Amundi",          "type": "Asset Manager",     "pcaf_type": "asset_manager"},
    "ASR Nederland":   {"key": "ASRNEDERLAND",    "composite_key": "ASR Nederland",   "type": "Insurance",         "pcaf_type": "insurer"},
    "Aviva":           {"key": "AVIVA",           "composite_key": "Aviva",           "type": "Insurance",         "pcaf_type": "insurer"},
    "AXA":             {"key": "AXA",             "composite_key": "AXA",             "type": "Insurance",         "pcaf_type": "insurer"},
    "Commerzbank":     {"key": "COMMERZBANK",     "composite_key": "Commerzbank",     "type": "Bank",              "pcaf_type": "bank"},
    "Crédit Agricole": {"key": "CREDITAGRICOLE",  "composite_key": "Crédit Agricole", "type": "Bank",              "pcaf_type": "bank"},
    "Deutsche Börse":  {"key": "DEUTSCHEBOERSE",  "composite_key": "Deutsche Börse",  "type": "Exchange",          "pcaf_type": "other"},
    "Eurazeo":         {"key": "EURAZEO",         "composite_key": "Eurazeo",         "type": "Asset Manager",     "pcaf_type": "asset_manager"},
    "GBL":             {"key": "GBL",             "composite_key": "GBL",             "type": "Investment Holding","pcaf_type": "other"},
    "KBC":             {"key": "KBC",             "composite_key": "KBC",             "type": "Bancassurance",     "pcaf_type": "bancassurance"},
    "Legal & General": {"key": "LEGALGENERAL",    "composite_key": "Legal & General", "type": "Insurance",         "pcaf_type": "insurer"},
    "NN Group":        {"key": "NNGROUP",         "composite_key": "NN Group",        "type": "Insurance",         "pcaf_type": "insurer"},
    "Nordea":          {"key": "NORDEA",          "composite_key": "Nordea",          "type": "Bank",              "pcaf_type": "bank"},
    "Phoenix Group":   {"key": "PHOENIXGROUP",    "composite_key": "Phoenix Group",   "type": "Insurance",         "pcaf_type": "insurer"},
    "Santander":       {"key": "SANTANDER",       "composite_key": "Santander",       "type": "Bank",              "pcaf_type": "bank"},
    "Schroders":       {"key": "SCHRODERS",       "composite_key": "Schroders",       "type": "Asset Manager",     "pcaf_type": "asset_manager"},
    "Société Générale":{"key": "SOCGEN",          "composite_key": "Société Générale","type": "Bank",              "pcaf_type": "bank"},
    "Swiss Re":        {"key": "SWISSRE",         "composite_key": "Swiss Re",        "type": "Reinsurance",       "pcaf_type": "reinsurer"},
    "UniCredit":       {"key": "UNICREDIT",       "composite_key": "UniCredit",       "type": "Bank",              "pcaf_type": "bank"},
    "Zurich":          {"key": "ZURICH",          "composite_key": "Zurich",          "type": "Insurance",         "pcaf_type": "insurer"},
    "ING":             {"key": "ING",             "composite_key": "ING",             "type": "Bank",              "pcaf_type": "bank"},
    "Julius Baer":     {"key": "JULIUSBAER",      "composite_key": "Julius Baer",     "type": "Bank",              "pcaf_type": "bank"},
}

# ── V2 Coefficient tables ───────────────────────────────────────────

# Part A – Financed Emissions (max raw score = 18)
PART_A_COEFF = {
    "Listed equity and corporate bonds":  {"s1s2": 3.0, "s3": 3.0, "ext_key": "listed_equity_corporate_bonds"},
    "Business loans and unlisted equity": {"s1s2": 3.0, "s3": 3.0, "ext_key": "business_loans_unlisted_equity"},
    "Project finance":                    {"s1s2": 1.0, "s3": 1.0, "ext_key": "project_finance"},
    "Commercial real estate":             {"s1s2": 1.0, "s3": 0.0, "ext_key": "commercial_real_estate"},
    "Mortgages":                          {"s1s2": 0.5, "s3": 0.0, "ext_key": "residential_mortgages"},
    "Motor vehicle loans":                {"s1s2": 0.5, "s3": 0.0, "ext_key": "motor_vehicle_loans"},
}
PART_A_SOVEREIGN = {"s1s2": 1.0, "s3": 1.0}  # handled via corrected_compliance.sovereign_debt
PART_A_MAX = 18.0

# Part C – Insurance-Associated Emissions (max raw score = 8)
PART_C_COEFF = {
    "Commercial lines":       {"s1s2": 2.0,  "s3": 1.0},
    "Reinsurance commercial": {"s1s2": 0.75, "s3": 0.25},
    "Personal motor":         {"s1s2": 3.0,  "s3": 0.0},
    "Reinsurance motor":      {"s1s2": 1.0,  "s3": 0.0},
}
PART_C_MAX = 8.0


# ── Helper functions ────────────────────────────────────────────────

def get_composite(comp_data, part, category):
    return comp_data.get(part, {}).get(category, {}).get("composite", 0)


def clamp(val, lo=0, hi=5):
    return max(lo, min(hi, val))


def coverage_to_level(ratio):
    """
    Map coverage ratio (0-1) to level (0-5).
    Calibrated against client-verified data:
      36.1% -> 1,  50% -> 3,  75% -> 4,  >=90% -> 5
    """
    if ratio <= 0:
        return 0
    elif ratio <= 0.40:
        return 1
    elif ratio < 0.50:
        return 2
    elif ratio < 0.70:
        return 3
    elif ratio < 0.90:
        return 4
    else:
        return 5


# ── Part A scoring ──────────────────────────────────────────────────

def compute_part_a_scores(name, info, comp_data, compl_data, ext_cov):
    rows = []
    part_a_status = compl_data.get("part_a_status", "missing")

    # 1. Asset Class Coverage
    raw = 0.0
    for ac_name, coeff in PART_A_COEFF.items():
        status = ext_cov.get(coeff["ext_key"], "missing")
        if status in ("reported", "partial"):
            raw += coeff["s1s2"] + coeff["s3"]
    sov_status = compl_data.get("sovereign_debt", "missing")
    if sov_status == "reported":
        raw += PART_A_SOVEREIGN["s1s2"] + PART_A_SOVEREIGN["s3"]
    elif sov_status == "partial":
        raw += PART_A_SOVEREIGN["s1s2"]

    ratio = raw / PART_A_MAX
    score = coverage_to_level(ratio)
    evidence = f"{raw:.1f}/{PART_A_MAX:.0f} coefficient coverage ({ratio:.1%})"
    priority = "Critical" if score <= 1 else ("High" if score <= 2 else ("Medium" if score <= 3 else "Low"))
    gap = "Extend coverage to remaining asset classes and S3 scopes" if score < 5 else "Full coverage"
    rows.append(("Asset Class Coverage", score, 5, evidence, priority, gap))

    # 2. Data Quality Score
    dqs = compl_data.get("dqs")
    if dqs is None:
        score, evidence, priority, gap = 0, "No PCAF data quality score reported", "High", "Implement and disclose PCAF DQS"
    elif isinstance(dqs, str):
        score, evidence, priority, gap = 1, f"DQS range {dqs} (wide dispersion)", "Medium", "Narrow DQS range"
    else:
        dqs_val = float(dqs)
        if dqs_val >= 4.5:   score = 1
        elif dqs_val >= 3.5: score = 2
        elif dqs_val >= 2.5: score = 3
        elif dqs_val >= 1.5: score = 4
        else:                score = 5
        evidence  = f"Average PCAF DQS {dqs_val:.2f}/5"
        priority  = "High" if score <= 1 else ("Medium" if score <= 3 else "Low")
        gap = f"Improve DQS toward <2.5" if score < 4 else "Good – target DQS <2 for Level 5"
    rows.append(("Data Quality Score", score, 5, evidence, priority, gap))

    # 3. Attribution Methodology
    pcaf_mentioned = compl_data.get("pcaf_mentioned", False)
    pcaf_signatory = compl_data.get("pcaf_signatory", False)
    if part_a_status == "missing":
        score, evidence = 0, "No attribution methodology disclosed"
    elif not pcaf_mentioned and part_a_status != "reported":
        score, evidence = 1, "Basic estimation without documented PCAF method"
    elif pcaf_mentioned and part_a_status == "partial" and not pcaf_signatory:
        score, evidence = 2, "Documented methodology, partial asset class coverage"
    elif pcaf_mentioned and not pcaf_signatory:
        score, evidence = 3, "PCAF-aligned methods per asset class"
    elif pcaf_signatory and part_a_status == "reported":
        score, evidence = 4, "Full PCAF methods (signatory), annual updates"
    else:
        score, evidence = 3 if part_a_status == "reported" else 2, "PCAF-referenced methodology"
    priority = "Critical" if score <= 1 else ("High" if score <= 2 else "Low")
    gap = "No PCAF methodology" if score == 0 else ("Incomplete" if score <= 2 else "Enhance with sector-specific improvements")
    rows.append(("Attribution Methodology", score, 5, evidence, priority, gap))

    # 4. Portfolio Coverage
    financed = compl_data.get("financed_emissions")
    n_covered = sum(
        1 for coeff in PART_A_COEFF.values()
        if ext_cov.get(coeff["ext_key"], "missing") in ("reported", "partial")
    ) + (1 if sov_status in ("reported", "partial") else 0)

    if part_a_status == "missing":
        score, evidence = 0, "No portfolio coverage reporting"
    elif part_a_status == "partial" and financed is None:
        score, evidence = 1, "Coverage not disclosed – estimated <40%"
    elif part_a_status == "partial":
        score, evidence = 2, "Estimated 40-60% portfolio coverage"
    elif part_a_status == "reported" and n_covered >= 6:
        score, evidence = 3, "Estimated 60-80% portfolio coverage"
    elif part_a_status == "reported" and n_covered >= 7:
        score, evidence = 4, "Estimated 80-95% portfolio coverage"
    else:
        score, evidence = 2, "Partial portfolio coverage"
    priority = "Medium" if score <= 2 else "Low"
    gap = "Disclose exact portfolio coverage %" if score < 4 else "Good portfolio coverage"
    rows.append(("Portfolio Coverage", score, 5, evidence, priority, gap))

    # 5. Temporal Coverage (max 3)
    if part_a_status == "missing":
        score, evidence = 0, "No historical financed emissions data"
    elif part_a_status == "partial" and financed is None:
        score, evidence = 1, "Current year only"
    elif part_a_status == "partial":
        score, evidence = 2, "2-3 years + trends"
    elif part_a_status == "reported":
        score, evidence = 3, "3+ years with trends and projections"
    else:
        score, evidence = 1, "Limited historical data"
    priority = "Low"
    gap = "Extend to 3 years + projections for full score" if score < 3 else "Good temporal coverage"
    rows.append(("Temporal Coverage", score, 3, evidence, priority, gap))

    return rows


# ── Part B scoring ──────────────────────────────────────────────────

def compute_part_b_scores(name, info, comp_data, compl_data):
    rows = []
    pcaf_type   = info["pcaf_type"]
    applicable  = pcaf_type in ("bank", "bancassurance")
    part_b_status = compl_data.get("part_b_status", "N/A")
    fac_composite = get_composite(comp_data, "Part B", "Facilitated emissions")

    # 1. Asset Class Coverage
    if not applicable:
        score, evidence, priority, gap = 0, "N/A – not a bank/bancassurance", "N/A", "Not applicable"
    elif part_b_status in ("N/A", "missing"):
        score, evidence, priority, gap = 0, "No facilitated emissions reported", "High", "Implement PCAF Part B"
    else:
        raw_b  = min(fac_composite * 2.0, 10.0)
        ratio_b = raw_b / 10.0
        score   = coverage_to_level(ratio_b)
        evidence = f"Facilitated emissions composite {fac_composite}/5 -> ~{ratio_b:.0%} Part B class coverage"
        priority = "High" if score <= 1 else ("Medium" if score <= 2 else "Low")
        gap = "Extend Part B to all 5 asset class categories" if score < 5 else "Full Part B coverage"
    rows.append(("Asset Class Coverage", score, 5, evidence, priority, gap))

    # 2. Attribution Methodology
    if not applicable:
        score, evidence, priority, gap = 0, "N/A – not applicable", "N/A", "Not applicable"
    elif part_b_status in ("N/A", "missing"):
        score, evidence, priority, gap = 0, "No facilitated emission attribution", "High", "Develop Part B attribution"
    elif fac_composite <= 1:
        score, evidence, priority, gap = 1, "Basic allocation", "Medium", "Adopt time-based PCAF attribution"
    elif fac_composite <= 2:
        score, evidence, priority, gap = 2, "Time-based allocation documented", "Medium", "Full PCAF Part B alignment"
    elif fac_composite <= 3:
        score, evidence, priority, gap = 3, "PCAF facilitation attribution applied", "Low", "Enhance with impact assessment"
    else:
        score, evidence, priority, gap = clamp(fac_composite), "Comprehensive facilitation attribution", "Low", "Continue improving"
    rows.append(("Attribution Methodology", score, 5, evidence, priority, gap))

    # 3. Temporal Coverage (max 3)
    if not applicable:
        score, evidence, priority, gap = 0, "N/A – not applicable", "N/A", "Not applicable"
    elif part_b_status in ("N/A", "missing"):
        score, evidence, priority, gap = 0, "No historical facilitated emissions data", "High", "Build Part B data series"
    elif part_b_status == "partial":
        score, evidence, priority, gap = 1, "Current year only", "Low", "Extend to multi-year trend reporting"
    else:
        score, evidence, priority, gap = 2, "Multi-year data with trend analysis", "Low", "Add projections for full score"
    rows.append(("Temporal Coverage", score, 3, evidence, priority, gap))

    return rows


# ── Part C scoring ──────────────────────────────────────────────────

def compute_part_c_scores(name, info, comp_data, compl_data):
    rows = []
    pcaf_type  = info["pcaf_type"]
    applicable = pcaf_type in ("insurer", "reinsurer", "bancassurance")
    part_c_status = compl_data.get("part_c_status", "N/A")

    cl_comp = get_composite(comp_data, "Part C", "Commercial lines")
    pm_comp = get_composite(comp_data, "Part C", "Personal motor")
    tr_comp = get_composite(comp_data, "Part C", "Treaty reinsurance")

    # 1. Asset Class Coverage
    if not applicable:
        score, evidence, priority, gap = 0, "N/A – not an insurer/reinsurer", "N/A", "Not applicable"
    elif part_c_status in ("N/A", "missing"):
        score, evidence, priority, gap = 0, "No insurance-associated emissions reported", "Critical", "Implement PCAF Part C"
    else:
        raw_c = 0.0
        if cl_comp > 0:
            raw_c += PART_C_COEFF["Commercial lines"]["s1s2"]
            if cl_comp >= 3:
                raw_c += PART_C_COEFF["Commercial lines"]["s3"]
        if tr_comp > 0:
            raw_c += PART_C_COEFF["Reinsurance commercial"]["s1s2"]
            if tr_comp >= 3:
                raw_c += PART_C_COEFF["Reinsurance commercial"]["s3"]
        if pm_comp > 0:
            raw_c += PART_C_COEFF["Personal motor"]["s1s2"]
        if pm_comp >= 4:
            raw_c += PART_C_COEFF["Reinsurance motor"]["s1s2"]
        ratio_c = raw_c / PART_C_MAX
        score   = coverage_to_level(ratio_c)
        evidence = (f"{raw_c:.2f}/{PART_C_MAX:.0f} branch coefficient ({ratio_c:.0%}) – "
                    f"Comm.Lines {cl_comp}/5, Motor {pm_comp}/5, Re {tr_comp}/5")
        priority = "Critical" if score == 0 else ("High" if score <= 1 else ("Medium" if score <= 2 else "Low"))
        gap = "Extend to all 4 insurance branches" if score < 5 else "Full coverage"
    rows.append(("Asset Class Coverage", score, 5, evidence, priority, gap))

    # 2. Attribution Methodology
    if not applicable:
        score, evidence, priority, gap = 0, "N/A – not applicable", "N/A", "Not applicable"
    elif part_c_status in ("N/A", "missing"):
        score, evidence, priority, gap = 0, "No insurance attribution methodology", "Critical", "Develop PCAF ITV attribution"
    else:
        avg_c = (cl_comp + pm_comp + tr_comp) / 3.0
        if avg_c < 1.0:
            score, evidence, priority, gap = 0, "No insurance attribution", "Critical", "Develop ITV methodology"
        elif avg_c < 1.5:
            score, evidence, priority, gap = 1, "Basic premium-based allocation", "High", "Adopt ITV method"
        elif avg_c < 2.5:
            score, evidence, priority, gap = 2, "ITV allocation applied", "Medium", "Full PCAF Part C alignment"
        elif avg_c < 3.5:
            score, evidence, priority, gap = 3, "PCAF insurance attribution applied", "Low", "Add risk-adjusted refinements"
        else:
            score, evidence, priority, gap = 4, "PCAF + risk-adjusted attribution", "Low", "Continue enhancement"
    rows.append(("Attribution Methodology", score, 5, evidence, priority, gap))

    # 3. Temporal Coverage (max 3)
    if not applicable:
        score, evidence, priority, gap = 0, "N/A – not applicable", "N/A", "Not applicable"
    elif part_c_status in ("N/A", "missing"):
        score, evidence, priority, gap = 0, "No historical insurance emissions data", "High", "Build Part C data series"
    elif part_c_status == "partial":
        score, evidence, priority, gap = 1, "Current year only", "Low", "Extend to multi-year trend reporting"
    else:
        score, evidence, priority, gap = 2, "Multi-year data with trend analysis", "Low", "Add projections for full score"
    rows.append(("Temporal Coverage", score, 3, evidence, priority, gap))

    return rows


# ── Main generation ─────────────────────────────────────────────────

def generate_assessment():
    output_rows = []

    for name, info in INSTITUTIONS.items():
        key       = info["key"]
        comp_key  = info["composite_key"]
        inst_type = info["type"]

        comp_data  = composite.get(comp_key, {})
        compl_data = compliance.get(key, {})
        ext_cov    = ext_coverage_all.get(key, {})
        v2_over    = v2_manual.get(name)

        def row_from_override(part_label, criterion, data):
            score  = data.get("score")
            max_s  = data.get("max")
            evid   = data.get("evidence", "")
            if score is None:
                return {
                    "company": name, "assessment_date": "2024-12-31",
                    "institution_type": inst_type, "pcaf_part": part_label,
                    "criterion": criterion, "score": "N/A", "max_score": "N/A",
                    "percentage": 0.0, "evidence": evid,
                    "priority": "N/A", "gap_description": "N/A",
                    "assessor_notes": "V2 client-verified – N/A",
                }
            pct = round((score / max_s) * 100, 1) if max_s else 0.0
            return {
                "company": name, "assessment_date": "2024-12-31",
                "institution_type": inst_type, "pcaf_part": part_label,
                "criterion": criterion, "score": score, "max_score": max_s,
                "percentage": pct, "evidence": evid,
                "priority": "—", "gap_description": "—",
                "assessor_notes": "V2 client-verified score",
            }

        # Manual V2 override (Nordea, Commerzbank, Ageas)
        if v2_over:
            for part_label in ("Part A", "Part B", "Part C"):
                part_data = v2_over.get(part_label, {})
                for criterion, crit_data in part_data.items():
                    if criterion.startswith("_"):
                        continue
                    output_rows.append(row_from_override(part_label, criterion, crit_data))
            continue

        # Algorithmic scoring for the remaining 20 institutions
        def append_rows(part_label, scored_rows):
            for criterion, score, max_s, evidence, priority, gap in scored_rows:
                pct = round((score / max_s) * 100, 1) if isinstance(score, (int, float)) else 0.0
                output_rows.append({
                    "company": name, "assessment_date": "2024-12-31",
                    "institution_type": inst_type, "pcaf_part": part_label,
                    "criterion": criterion, "score": score, "max_score": max_s,
                    "percentage": pct, "evidence": evidence,
                    "priority": priority, "gap_description": gap,
                    "assessor_notes": compl_data.get("recommendation", ""),
                })

        append_rows("Part A", compute_part_a_scores(name, info, comp_data, compl_data, ext_cov))
        append_rows("Part B", compute_part_b_scores(name, info, comp_data, compl_data))
        append_rows("Part C", compute_part_c_scores(name, info, comp_data, compl_data))

    return output_rows


def main():
    rows = generate_assessment()

    output_path = os.path.join(BASE, "looker_data", "pcaf_assessment_detailed.csv")
    fieldnames = [
        "company", "assessment_date", "institution_type", "pcaf_part",
        "criterion", "score", "max_score", "percentage", "evidence",
        "priority", "gap_description", "assessor_notes",
    ]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    companies = sorted(set(r["company"] for r in rows))
    print(f"✓ Generated {len(rows)} rows for {len(companies)} institutions")
    print(f"✓ Output: {output_path}\n")

    PART_A_MAX_SCORE = 23
    PART_B_MAX_SCORE = 13
    PART_C_MAX_SCORE = 13

    print(f"{'Company':<22} {'Type':<14}  {'Compliance A':>22}  {'Compliance B':>22}  {'Compliance C':>22}")
    print("-" * 90)
    for company in companies:
        inst_rows = [r for r in rows if r["company"] == company]
        inst_type = inst_rows[0]["institution_type"]

        def part_total(part):
            pr = [r for r in inst_rows if r["pcaf_part"] == part]
            if all(str(r["score"]) == "N/A" for r in pr):
                return None
            return sum(int(r["score"]) for r in pr if str(r["score"]).lstrip("-").isdigit())

        a, b, c = part_total("Part A"), part_total("Part B"), part_total("Part C")
        a_s = f"{a}/{PART_A_MAX_SCORE} = {a/PART_A_MAX_SCORE:.1%}" if a is not None else "N/A"
        b_s = f"{b}/{PART_B_MAX_SCORE} = {b/PART_B_MAX_SCORE:.1%}" if b is not None else "N/A"
        c_s = f"{c}/{PART_C_MAX_SCORE} = {c/PART_C_MAX_SCORE:.1%}" if c is not None else "N/A"
        print(f"{company:<22} {inst_type:<14}  {a_s:>22}  {b_s:>22}  {c_s:>22}")


if __name__ == "__main__":
    main()
