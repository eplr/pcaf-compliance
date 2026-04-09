#!/usr/bin/env python3
"""
Generate pcaf_assessment_detailed.csv for 25 financial institutions.
PCAF Methodology V3 – 5 criteria (Part A) + 3 criteria (Part B) + 3 criteria (Part C).

Part A max = 23  (5+5+5+5+3)
Part B max = 13  (5+5+3)
Part C max = 13  (5+5+3)

V3 changes (April 2026, post-Lucie feedback):
  - Asset Class Coverage: "partial" = S1&S2 only (no S3 credit); "reported" = S1&S2+S3.
    Sovereign debt split into production (0.5) + LULUCF (0.5) + S3 (1.0).
    Sovereign debt sourced from extended_asset_class_coverage.json (like all other classes).
  - Portfolio Coverage: systematic audit against source reports (extracted_text/*.json).
    9/13 initial extractions were incorrect (wrong context). 3 additional coverages
    found in report tables (Allianz 63%, NN Group 80%, Swiss Re 67%).
    When coverage not explicitly disclosed → score 0 (non déclaré), no estimation.
  - All evidence fields enriched with: scoring justification, source reference
    [section/page], verbatim quotes, and explanation of rejected percentages.
  - Manual V2 overrides for Nordea, Commerzbank, Ageas from pcaf_v2_scores.json.

All evidence/gap text is in English.
Direct quotes from sustainability reports are kept in their original language.
"""

import csv
import json
import os
import re

BASE = "/Users/fidestra/Library/CloudStorage/OneDrive-fidestra/03_ACCOUNTS/Axylia/pcaf-compliance"

# ── Load data sources ───────────────────────────────────────────────

composite = {}
with open(os.path.join(BASE, "data/pcaf_composite_scores.csv")) as f:
    for row in csv.DictReader(f):
        inst = row["institution"]; part = row["part"]; cat = row["category"]
        composite.setdefault(inst, {}).setdefault(part, {})[cat] = {
            "composite": int(row["composite"]), "mention": int(row["mention"]),
        }

with open(os.path.join(BASE, "data/corrected_compliance_data.json")) as f:
    compliance = json.load(f)

with open(os.path.join(BASE, "data/extended_asset_class_coverage.json")) as f:
    ext_coverage_all = json.load(f)

with open(os.path.join(BASE, "data/pcaf_v2_scores.json")) as f:
    v2_manual = json.load(f)

# ── Institution list ────────────────────────────────────────────────

INSTITUTIONS = {
    "Admiral Group":   {"key":"ADMIRAL",        "composite_key":"Admiral Group",   "type":"Insurance",          "pcaf_type":"insurer"},
    "Ageas":           {"key":"AGEAS",           "composite_key":"Ageas",           "type":"Insurance",          "pcaf_type":"insurer"},
    "Allianz":         {"key":"ALLIANZ",         "composite_key":"Allianz",         "type":"Insurance",          "pcaf_type":"insurer"},
    "Amundi":          {"key":"AMUNDI",          "composite_key":"Amundi",          "type":"Asset Manager",      "pcaf_type":"asset_manager"},
    "ASR Nederland":   {"key":"ASRNEDERLAND",    "composite_key":"ASR Nederland",   "type":"Insurance",          "pcaf_type":"insurer"},
    "Aviva":           {"key":"AVIVA",           "composite_key":"Aviva",           "type":"Insurance",          "pcaf_type":"insurer"},
    "AXA":             {"key":"AXA",             "composite_key":"AXA",             "type":"Insurance",          "pcaf_type":"insurer"},
    "Commerzbank":     {"key":"COMMERZBANK",     "composite_key":"Commerzbank",     "type":"Bank",               "pcaf_type":"bank"},
    "Crédit Agricole": {"key":"CREDITAGRICOLE",  "composite_key":"Crédit Agricole", "type":"Bank",               "pcaf_type":"bank"},
    "Deutsche Börse":  {"key":"DEUTSCHEBOERSE",  "composite_key":"Deutsche Börse",  "type":"Exchange",           "pcaf_type":"other"},
    "Eurazeo":         {"key":"EURAZEO",         "composite_key":"Eurazeo",         "type":"Asset Manager",      "pcaf_type":"asset_manager"},
    "GBL":             {"key":"GBL",             "composite_key":"GBL",             "type":"Investment Holding", "pcaf_type":"other"},
    "KBC":             {"key":"KBC",             "composite_key":"KBC",             "type":"Bancassurance",      "pcaf_type":"bancassurance"},
    "Legal & General": {"key":"LEGALGENERAL",    "composite_key":"Legal & General", "type":"Insurance",          "pcaf_type":"insurer"},
    "NN Group":        {"key":"NNGROUP",         "composite_key":"NN Group",        "type":"Insurance",          "pcaf_type":"insurer"},
    "Nordea":          {"key":"NORDEA",          "composite_key":"Nordea",          "type":"Bank",               "pcaf_type":"bank"},
    "Phoenix Group":   {"key":"PHOENIXGROUP",    "composite_key":"Phoenix Group",   "type":"Insurance",          "pcaf_type":"insurer"},
    "Santander":       {"key":"SANTANDER",       "composite_key":"Santander",       "type":"Bank",               "pcaf_type":"bank"},
    "Schroders":       {"key":"SCHRODERS",       "composite_key":"Schroders",       "type":"Asset Manager",      "pcaf_type":"asset_manager"},
    "Société Générale":{"key":"SOCGEN",          "composite_key":"Société Générale","type":"Bank",               "pcaf_type":"bank"},
    "Swiss Re":        {"key":"SWISSRE",         "composite_key":"Swiss Re",        "type":"Reinsurance",        "pcaf_type":"reinsurer"},
    "UniCredit":       {"key":"UNICREDIT",       "composite_key":"UniCredit",       "type":"Bank",               "pcaf_type":"bank"},
    "Zurich":          {"key":"ZURICH",          "composite_key":"Zurich",          "type":"Insurance",          "pcaf_type":"insurer"},
    "ING":             {"key":"ING",             "composite_key":"ING",             "type":"Bank",               "pcaf_type":"bank"},
    "Julius Baer":     {"key":"JULIUSBAER",      "composite_key":"Julius Baer",     "type":"Bank",               "pcaf_type":"bank"},
}

# ── V3 Coefficient tables ───────────────────────────────────────────

PART_A_COEFF = {
    "Listed equity and corporate bonds":  {"s1s2":3.0,"s3":3.0,"ext_key":"listed_equity_corporate_bonds"},
    "Business loans and unlisted equity": {"s1s2":3.0,"s3":3.0,"ext_key":"business_loans_unlisted_equity"},
    "Project finance":                    {"s1s2":1.0,"s3":1.0,"ext_key":"project_finance"},
    "Commercial real estate":             {"s1s2":1.0,"s3":0.0,"ext_key":"commercial_real_estate"},
    "Mortgages":                          {"s1s2":0.5,"s3":0.0,"ext_key":"residential_mortgages"},
    "Motor vehicle loans":                {"s1s2":0.5,"s3":0.0,"ext_key":"motor_vehicle_loans"},
}
PART_A_SOVEREIGN = {"prod":0.5, "lulucf":0.5, "s3":1.0}  # max = 2.0
PART_A_MAX = 18.0

PART_C_COEFF = {
    "Commercial lines":       {"s1s2":2.0,  "s3":1.0},
    "Reinsurance commercial": {"s1s2":0.75, "s3":0.25},
    "Personal motor":         {"s1s2":3.0,  "s3":0.0},
    "Reinsurance motor":      {"s1s2":1.0,  "s3":0.0},
}
PART_C_MAX = 8.0

# ── Portfolio Coverage DB (V3 – audited against source reports) ─────────
# Format: { KEY: (pct_or_None, citation, score_override_or_None) }
#   pct: disclosed portfolio coverage %, or None if not found.
#   citation: evidence string with [Source ref], verbatim, calculation details.
#             Prefixed [No data] when coverage not found, explaining rejected %.
#   score_override: force score (used when pct=None → 0). None = auto from pct.
# Explanatory text is in English. Direct report quotes are in their original language.

PORTFOLIO_COV_DB = {
    # ── Confirmed: no coverage data found ───────────────────────────
    "ADMIRAL": (None,
        "[No data] Admiral does not publish financed emissions (Scope 3, Cat. 15 PCAF®). "
        "No portfolio coverage rate found in the 2024 sustainability report.",
        0),
    "AMUNDI": (None,
        "[No data] Amundi does not publish financed emissions under PCAF® (Scope 3, Cat. 15). "
        "Emissions reported via other frameworks (SFDR, Art. 29 LEC) without PCAF® coverage rate.",
        0),
    "CREDITAGRICOLE": (None,
        "[No data] No portfolio coverage data for PCAF® financed emissions (Scope 3, Cat. 15) "
        "found in Crédit Agricole's 2024 sustainability report.",
        0),
    "DEUTSCHEBOERSE": (None,
        "[No data] Deutsche Börse does not calculate PCAF® financed emissions. Percentages "
        "(100%, 38%) relate to EU Green Taxonomy eligible activities, not PCAF® coverage.",
        0),
    "EURAZEO": (None,
        "[No data] No PCAF® financed emissions portfolio coverage rate found in Eurazeo's "
        "2024 sustainability report.",
        0),
    "GBL": (None,
        "[No data] GBL does not publish a PCAF® portfolio coverage rate. Financed emissions "
        "data is partial, no explicit coverage rate.",
        0),
    "ING": (None,
        "[No data] The 92.0% figure (p.~280, Annual Report 2025) refers to IFRS 9 Stage 1 "
        "portfolio quality (credit risk staging), NOT financed emissions coverage. "
        "No explicit PCAF® portfolio coverage rate found.",
        0),
    "JULIUSBAER": (None,
        "[No data] The 49% figure (Sustainability Highlights, Annual Report 2025) refers to "
        "assets allocated to companies with SBTi targets, NOT PCAF® portfolio coverage. "
        "Individual PCAF book tables show ~100% within-scope coverage per sector, but overall "
        "AuM coverage rate not disclosed.",
        0),
    "KBC": (None,
        "[No data] The 92% figure (Sustainability Report 2024) refers to Pensioenfonds KBC "
        "assets classified as Article 8/9 SFDR funds, NOT PCAF® financed emissions coverage. "
        "Sector-by-sector data available but no overall portfolio coverage rate.",
        0),
    "PHOENIXGROUP": (None,
        "[No data] The 100% figure relates to the 2030 decarbonisation target scope "
        "('portfolio coverage towards 100% of the scope of our 2030 decarbonisation target'), "
        "NOT the current PCAF® financed emissions coverage rate.",
        0),
    "SANTANDER": (None,
        "[No data] The 99% figure (2024 Report) refers to Scope 3 Cat. 15 materiality weighting "
        "(financed emissions = 99% of total Scope 3), NOT portfolio coverage. "
        "No overall PCAF® portfolio coverage rate found.",
        0),
    "SCHRODERS": (None,
        "[No data] The 97% figure (2024 Annual Report, section Sustainability) refers to "
        "operational Scope 3 emissions from business travel and supply chain, "
        "NOT PCAF® financed emissions portfolio coverage.",
        0),
    "SOCGEN": (None,
        "[No data] No PCAF® portfolio coverage rate (Scope 3, Cat. 15) found in "
        "Société Générale's 2024 sustainability report.",
        0),
    "UNICREDIT": (None,
        "[No data] The 90% figure (p.~673, 2024 Annual Report) refers to client risk "
        "classification ('90% Medium/Low' from C&E Questionnaire). The '45-50%' is ESG "
        "questionnaire mapping, NOT PCAF® financed emissions coverage. 2024 is the first "
        "reporting year for financed emissions; no overall coverage rate disclosed.",
        0),
    "ZURICH": (None,
        "[No data] The 65% figure (p.~117, Sustainability Report 2024) is an engagement "
        "target ('Engage with companies that produce 65% of financed emissions that have "
        "not set SBTs'). The 60% was the 2023 achievement. Neither represents portfolio "
        "coverage. No PCAF® portfolio coverage rate disclosed.",
        0),
    # ── Verified coverage from report tables ────────────────────────
    "ALLIANZ": (63,
        "[Weighted from table p.82-83, section E1 Climate Change, Annual Report 2024] "
        "63% = weighted coverage across asset classes: Corporates €369.6bn (79.5%), "
        "Public debt €165.2bn (99.5%), Real estate €125.4bn (20.3%), No methodology €106.8bn "
        "(0%). Calculation: (369.6×79.5%+165.2×99.5%+125.4×20.3%+106.8×0%)/767.0 = 63%. "
        "Note: the 50% figure in the report refers to a GHG reduction target, not coverage.",
        None),
    "ASRNEDERLAND": (77,
        "[Table 'Scope 3 Cat. 15 Investments – Financed emissions breakdown (S1&S2)', "
        "section E1-6, Annual Report 2024] 77% = Own investments total AuM data coverage. "
        "Per asset class: Govt bonds 98%, Corp bonds 94%, Equity 93%, Mortgages 100%, "
        "Other 0%. Insurance contract investments 79%, Third parties 100%.",
        None),
    "AVIVA": (95,
        "[Climate Report 2024, section 'Financed emissions – Coverage'] "
        "95% = emissions data coverage of assets included in financed emissions calculation "
        "(2023: 87%). Verbatim: 'Overall emissions data coverage has increased to 95%'. "
        "Note: AUM coverage is only 57%, the 95% is emissions data coverage within "
        "calculated asset classes.",
        None),
    "AXA": (87,
        "[Universal Registration Document 2024, section Sustainability] "
        "86.9% = carbon intensity coverage rate of in-scope assets. "
        "Verbatim: 'the carbon intensity coverage rate stands at 86.9% of the in-scope assets'. "
        "Private assets coverage: 93.6% (€42bn, 9% of General Account). "
        "Third-party AUM: 90% coverage.",
        None),
    "COMMERZBANK": (54,
        "[Client-verified data] ~54% estimated coverage of the loan portfolio in the "
        "financed emissions calculation. The report does not disclose this figure explicitly.",
        None),
    "LEGALGENERAL": (41,
        "[Climate and Nature Report 2024, section 'Scope 3 investment portfolio carbon "
        "footprint'] 41% = direct ISS data coverage of 2024 portfolio. "
        "Verbatim: 'c.41% direct coverage of 2024 portfolio' (£24.7bn corporate + "
        "£12.5bn sovereign). Note: the 100% figure is a 2050 net zero target, not current coverage. "
        "Proxies/estimates applied beyond 41% but not quantified.",
        None),
    "NNGROUP": (80,
        "[Annual Report 2024, section 'Financed emissions'] 80% = share of total proprietary "
        "assets included in the GHG emissions calculation. From table: included €126,017m "
        "out of €156,987m proprietary assets (20% not part of GHG calculation, 80% included). "
        "Extrapolation covers ~13% of additional assets with PCAF DQS 5. "
        "Note: including policyholder assets, overall = 60%.",
        None),
    "NORDEA": (75,
        "[Client-verified data, 2024 Report] ~75% estimated overall portfolio coverage "
        "(loans + investments). Note: ~95% lending portfolio coverage is mentioned separately, "
        "but the consolidated overall coverage is lower.",
        None),
    "SWISSRE": (67,
        "[Annual Report 2024, section 'Sustainability performance'] 67% = overall investment "
        "portfolio coverage for absolute financed GHG emissions. Verbatim: '67% of its overall "
        "investment portfolio and most of its operational spend is covered in terms of absolute "
        "GHG emissions'. Note: the 90% figure refers to Part C commercial lines insurance "
        "premiums, NOT investment coverage. The 34% (2023) was the previous year figure.",
        None),
}

# ── Helpers ─────────────────────────────────────────────────────────

def get_composite(comp_data, part, category):
    return comp_data.get(part, {}).get(category, {}).get("composite", 0)

def clamp(val, lo=0, hi=5):
    return max(lo, min(hi, val))

def coverage_to_level(ratio):
    if ratio <= 0:      return 0
    elif ratio <= 0.40: return 1
    elif ratio < 0.50:  return 2
    elif ratio < 0.70:  return 3
    elif ratio < 0.90:  return 4
    else:               return 5

def portfolio_cov_score(pct):
    if pct is None: return None
    if pct > 95: return 5
    if pct > 80: return 4
    if pct > 60: return 3
    if pct > 40: return 2
    if pct > 0:  return 1
    return 0

NA = "N/A"

# ── Verification status helpers ─────────────────────────────────────

# Matches leading verification tags: [VERIFIED...], [AUTOMATED...], [UNVERIFIED...]
_LEADING_TAG_RE = re.compile(
    r'^\[(?:VERIFIED|Verified|AUTOMATED|UNVERIFIED)[^\]]*\]\s*',
    re.IGNORECASE,
)
# Matches inline status/scan tags: [NOT FOUND], [FOUND — ...], [INCOMPLETE — ...], [No data]
_INLINE_TAG_RE = re.compile(
    r'\[(?:NOT FOUND|FOUND[^\]]*|INCOMPLETE[^\]]*|No data)\]\s*'
)

def _detect_verification_status(evidence, score, assessor_notes=""):
    """Derive a verification_status label from evidence text / assessor_notes."""
    if score is None or str(score) == NA:
        return "[N/A]"
    ev_upper = evidence.upper()
    if ev_upper.startswith("[VERIFIED"):
        return "[VERIFIED]"
    if "[AUTOMATED" in ev_upper or "[UNVERIFIED" in ev_upper:
        return "[UNVERIFIED]"
    # Client-verified overrides (Nordea, Commerzbank, Ageas) have clean evidence
    if "client-verified" in assessor_notes.lower():
        return "[CLIENT-VERIFIED]"
    return "[UNVERIFIED]"

def _strip_verification_tag(evidence):
    """Remove all bracket labels from evidence, keeping only the factual content."""
    cleaned = _LEADING_TAG_RE.sub('', evidence)
    cleaned = _INLINE_TAG_RE.sub('', cleaned)
    return cleaned.strip()

# ── Part A ──────────────────────────────────────────────────────────

def compute_part_a_scores(name, info, comp_data, compl_data, ext_cov, inst_key):
    rows = []
    part_a_status = compl_data.get("part_a_status", "missing")

    # 1. Asset Class Coverage – detailed per-asset-class breakdown
    raw = 0.0
    ac_details = []
    for ac_name, coeff in PART_A_COEFF.items():
        status = ext_cov.get(coeff["ext_key"], "missing")
        ac_max = coeff["s1s2"] + coeff["s3"]
        has_s3 = coeff["s3"] > 0
        ac_pts = 0.0
        if status == "reported":
            ac_pts = coeff["s1s2"] + coeff["s3"]
            reason = "S1&S2 + S3" if has_s3 else "S1&S2"
        elif status == "partial":
            ac_pts = coeff["s1s2"]  # S1&S2 only, no S3 credit
            reason = "S1&S2 only, S3 not covered" if has_s3 else "S1&S2 partial coverage"
        else:
            reason = "not reported"
        raw += ac_pts
        ac_details.append(f"{ac_name}: {ac_pts:.1f}/{ac_max:.1f} ({reason})")
    sov = ext_cov.get("sovereign_debt", "missing")  # use ext_cov like other asset classes
    sov_max = PART_A_SOVEREIGN["prod"] + PART_A_SOVEREIGN["lulucf"] + PART_A_SOVEREIGN["s3"]
    sov_pts = 0.0
    if sov == "reported":
        sov_pts = sov_max
        sov_reason = "S1&S2 production + LULUCF + S3"
    elif sov == "partial":
        sov_pts = PART_A_SOVEREIGN["prod"]  # production-based S1&S2 only
        sov_reason = "S1&S2 production only, LULUCF not included, S3 not covered"
    else:
        sov_reason = "not reported"
    raw += sov_pts
    ac_details.append(f"Sovereign debt: {sov_pts:.1f}/{sov_max:.1f} ({sov_reason})")
    ratio = raw / PART_A_MAX
    score = coverage_to_level(ratio)
    evidence = (f"{raw:.1f}/{PART_A_MAX:.0f} weighted coverage ({ratio:.0%}). "
                f"Detail: {'; '.join(ac_details)}")
    priority = "Critical" if score<=1 else ("High" if score<=2 else ("Medium" if score<=3 else "Low"))
    gap = "Extend coverage to missing asset classes and include S3 emissions" if score<5 else "Full coverage"
    rows.append(("Asset Class Coverage", score, 5, evidence, priority, gap))

    # 2. Data Quality Score
    dqs = compl_data.get("dqs")
    if dqs is None:
        s = 0
        ev = ("PCAF® data quality score not disclosed in the sustainability report. "
              "Score 0: no DQS data available to assess data quality.")
        pr, gp = "High", "Implement and disclose PCAF® DQS"
    elif isinstance(dqs, str):
        s = 1
        ev = (f"DQS reported as a wide range ({dqs}), indicating heterogeneous data quality "
              f"across asset classes. Score 1: range too broad to confirm DQS < 4.5.")
        pr, gp = "Medium", "Narrow DQS range"
    else:
        dqs_val = float(dqs)
        s = 1 if dqs_val>=4.5 else (2 if dqs_val>=3.5 else (3 if dqs_val>=2.5 else (4 if dqs_val>=1.5 else 5)))
        thresholds = {1:"≥4.5", 2:"3.5–4.5", 3:"2.5–3.5", 4:"1.5–2.5", 5:"<1.5"}
        ev = (f"Average PCAF® DQS: {dqs_val:.2f}/5. "
              f"Score {s}: DQS falls in the {thresholds[s]} range per the scoring grid.")
        pr = "High" if s<=1 else ("Medium" if s<=3 else "Low")
        gp = "Improve DQS toward <2.5" if s<4 else "Good level – target DQS <2 for level 5"
    rows.append(("Data Quality Score", s, 5, ev, pr, gp))

    # 3. Attribution Methodology
    pcaf_mentioned = compl_data.get("pcaf_mentioned", False)
    pcaf_signatory = compl_data.get("pcaf_signatory", False)
    if part_a_status == "missing":
        s = 0
        ev = ("No attribution methodology disclosed. The institution does not report "
              "financed emissions under any recognized standard. Score 0.")
    elif not pcaf_mentioned and part_a_status != "reported":
        s = 1
        ev = ("Basic estimation without documented PCAF® methodology. PCAF® is not mentioned "
              f"in the report (signatory: {pcaf_signatory}). Part A status: {part_a_status}. Score 1.")
    elif pcaf_mentioned and part_a_status == "partial" and not pcaf_signatory:
        s = 2
        ev = (f"PCAF® mentioned but not a signatory. Documented methods with partial asset class "
              f"coverage (Part A status: {part_a_status}). Score 2.")
    elif pcaf_mentioned and not pcaf_signatory:
        s = 3
        ev = (f"PCAF®-aligned methods per asset class. PCAF® mentioned, not a signatory. "
              f"Part A status: {part_a_status}. Score 3.")
    elif pcaf_signatory and part_a_status == "reported":
        s = 4
        ev = ("Full PCAF® methods – institution is a PCAF® signatory with comprehensive reporting "
              f"(Part A status: reported). Score 4.")
    else:
        s = 3 if part_a_status=="reported" else 2
        ev = (f"PCAF® methodology referenced. Signatory: {pcaf_signatory}, "
              f"Part A status: {part_a_status}. Score {s}.")
    pr = "Critical" if s<=1 else ("High" if s<=2 else "Low")
    gp = ("No PCAF® methodology" if s==0 else
          "Incomplete methodology" if s<=2 else
          "Enhance with sector-specific improvements")
    rows.append(("Attribution Methodology", s, 5, ev, pr, gp))

    # 4. Portfolio Coverage (sourced from PORTFOLIO_COV_DB)
    db = PORTFOLIO_COV_DB.get(inst_key)
    if db:
        pct, citation, score_override = db
        if score_override is not None:
            s = score_override
            ev = citation
            gp = ("Coverage data not disclosed – publish explicit PCAF® portfolio coverage rate" if s==0 else
                  "Disclose exact PCAF® portfolio coverage rate" if s<4 else "Good coverage")
        else:
            s = portfolio_cov_score(pct)
            ev = (f"{pct:.0f}% disclosed. {citation} "
                  f"Score {s} per grid (0=N/D, 1=<40%, 2=40-60%, 3=60-80%, 4=80-95%, 5=>95%).")
            gp = "Disclose exact PCAF® portfolio coverage rate" if s<4 else "Good coverage"
        pr = "Medium" if s<=2 else "Low"
    else:
        # Consistent rule: if coverage not explicitly disclosed → 0 (non déclaré)
        s = 0
        ev = ("No explicit PCAF® portfolio coverage rate found in the sustainability report. "
              f"Part A status: {part_a_status}. Score 0 (non déclaré).")
        pr = "Medium"
        gp = "Disclose exact PCAF® portfolio coverage rate"
    rows.append(("Portfolio Coverage", s, 5, ev, pr, gp))

    # 5. Temporal Coverage (max 3)
    financed = compl_data.get("financed_emissions")
    if part_a_status == "missing":
        s = 0
        ev = ("No historical financed emissions data found. Part A status: missing. "
              "Score 0: no time series available.")
    elif part_a_status == "partial" and financed is None:
        s = 1
        ev = ("Part A status: partial, no quantified financed emissions found. "
              "Score 1: current year only (no multi-year trend possible).")
    elif part_a_status == "partial":
        s = 2
        ev = (f"Part A status: partial, financed emissions quantified ({financed}). "
              "Score 2: 2–3 years of history with trend analysis identified.")
    elif part_a_status == "reported":
        s = 3
        ev = ("Part A status: reported with comprehensive data. "
              "Score 3: 3+ years of history with trends and projections/targets.")
    else:
        s = 1
        ev = (f"Part A status: {part_a_status}. Limited historical data. Score 1.")
    pr = "Low"
    gp = "Extend to 3 years + projections for maximum score" if s<3 else "Good temporal coverage"
    rows.append(("Temporal Coverage", s, 3, ev, pr, gp))

    return rows

# ── Part B ──────────────────────────────────────────────────────────

def compute_part_b_scores(name, info, comp_data, compl_data):
    rows = []
    applicable = info["pcaf_type"] in ("bank", "bancassurance")
    part_b_status = compl_data.get("part_b_status", "N/A")
    fac_comp = get_composite(comp_data, "Part B", "Facilitated emissions")

    # 1. Asset Class Coverage
    if not applicable:
        rows.append(("Asset Class Coverage", NA, NA,
                     "N/A – not applicable (not a bank/bancassurance institution)", NA, NA))
    elif part_b_status in ("N/A", "missing"):
        rows.append(("Asset Class Coverage", 0, 5,
                     "No facilitated emissions reported", "High", "Implement PCAF® Part B"))
    else:
        raw_b = min(fac_comp*2.0, 10.0); ratio_b = raw_b/10.0
        s = coverage_to_level(ratio_b)
        ev = f"Facilitated emissions composite {fac_comp}/5 → ~{ratio_b:.0%} Part B asset class coverage"
        pr = "High" if s<=1 else ("Medium" if s<=2 else "Low")
        gp = "Extend Part B to all 5 asset classes" if s<5 else "Full Part B coverage"
        rows.append(("Asset Class Coverage", s, 5, ev, pr, gp))

    # 2. Attribution Methodology
    if not applicable:
        rows.append(("Attribution Methodology", NA, NA, "N/A – not applicable", NA, NA))
    elif part_b_status in ("N/A", "missing"):
        rows.append(("Attribution Methodology", 0, 5,
                     "No facilitated emission attribution methodology", "High",
                     "Develop Part B attribution methodology"))
    elif fac_comp <= 1:
        rows.append(("Attribution Methodology", 1, 5, "Basic allocation", "Medium",
                     "Adopt PCAF® time-based attribution"))
    elif fac_comp <= 2:
        rows.append(("Attribution Methodology", 2, 5, "Time-based allocation documented", "Medium",
                     "Full PCAF® Part B alignment"))
    elif fac_comp <= 3:
        rows.append(("Attribution Methodology", 3, 5,
                     "PCAF® facilitation attribution methodology applied", "Low",
                     "Enhance with impact assessment"))
    else:
        rows.append(("Attribution Methodology", clamp(fac_comp), 5,
                     "Comprehensive attribution with quality scores", "Low", "Continue improving"))

    # 3. Temporal Coverage (max 3)
    if not applicable:
        rows.append(("Temporal Coverage", NA, NA, "N/A – not applicable", NA, NA))
    elif part_b_status in ("N/A", "missing"):
        rows.append(("Temporal Coverage", 0, 3,
                     "No historical facilitated emissions data", "High", "Build Part B time series"))
    elif part_b_status == "partial":
        rows.append(("Temporal Coverage", 1, 3,
                     "Current year only", "Low", "Extend to multi-year reporting"))
    else:
        rows.append(("Temporal Coverage", 2, 3,
                     "Multi-year data with trend analysis", "Low", "Add projections for maximum score"))
    return rows

# ── Part C ──────────────────────────────────────────────────────────

def compute_part_c_scores(name, info, comp_data, compl_data):
    rows = []
    applicable = info["pcaf_type"] in ("insurer", "reinsurer", "bancassurance")
    part_c_status = compl_data.get("part_c_status", "N/A")
    cl_comp = get_composite(comp_data, "Part C", "Commercial lines")
    pm_comp = get_composite(comp_data, "Part C", "Personal motor")
    tr_comp = get_composite(comp_data, "Part C", "Treaty reinsurance")

    # 1. Asset Class Coverage
    if not applicable:
        rows.append(("Asset Class Coverage", NA, NA,
                     "N/A – not applicable (not an insurer/reinsurer)", NA, NA))
    elif part_c_status in ("N/A", "missing"):
        rows.append(("Asset Class Coverage", 0, 5,
                     "No insurance-associated emissions reported", "Critical",
                     "Implement PCAF® Part C"))
    else:
        raw_c = 0.0
        if cl_comp > 0:
            raw_c += PART_C_COEFF["Commercial lines"]["s1s2"]
            if cl_comp >= 3: raw_c += PART_C_COEFF["Commercial lines"]["s3"]
        if tr_comp > 0:
            raw_c += PART_C_COEFF["Reinsurance commercial"]["s1s2"]
            if tr_comp >= 3: raw_c += PART_C_COEFF["Reinsurance commercial"]["s3"]
        if pm_comp > 0: raw_c += PART_C_COEFF["Personal motor"]["s1s2"]
        if pm_comp >= 4: raw_c += PART_C_COEFF["Reinsurance motor"]["s1s2"]
        ratio_c = raw_c/PART_C_MAX; s = coverage_to_level(ratio_c)
        ev = (f"{raw_c:.2f}/{PART_C_MAX:.0f} branch coefficient coverage ({ratio_c:.0%}) – "
              f"Comm.Lines {cl_comp}/5, Motor {pm_comp}/5, Re {tr_comp}/5")
        pr = "Critical" if s==0 else ("High" if s<=1 else ("Medium" if s<=2 else "Low"))
        gp = "Extend to all 4 insurance branches" if s<5 else "Full coverage"
        rows.append(("Asset Class Coverage", s, 5, ev, pr, gp))

    # 2. Attribution Methodology
    if not applicable:
        rows.append(("Attribution Methodology", NA, NA, "N/A – not applicable", NA, NA))
    elif part_c_status in ("N/A", "missing"):
        rows.append(("Attribution Methodology", 0, 5,
                     "No insurance attribution methodology (ITV)", "Critical",
                     "Develop PCAF® ITV methodology"))
    else:
        avg_c = (cl_comp+pm_comp+tr_comp)/3.0
        if avg_c < 1.0:
            rows.append(("Attribution Methodology", 0, 5,
                         "No insurance attribution", "Critical", "Develop ITV methodology"))
        elif avg_c < 1.5:
            rows.append(("Attribution Methodology", 1, 5,
                         "Basic premium-based allocation", "High", "Adopt ITV method"))
        elif avg_c < 2.5:
            rows.append(("Attribution Methodology", 2, 5,
                         "ITV method applied", "Medium", "Full PCAF® Part C alignment"))
        elif avg_c < 3.5:
            rows.append(("Attribution Methodology", 3, 5,
                         "PCAF® insurance attribution applied", "Low", "Add risk-adjusted refinements"))
        else:
            rows.append(("Attribution Methodology", 4, 5,
                         "PCAF® + risk-adjusted attribution", "Low", "Continue enhancement"))

    # 3. Temporal Coverage (max 3)
    if not applicable:
        rows.append(("Temporal Coverage", NA, NA, "N/A – not applicable", NA, NA))
    elif part_c_status in ("N/A", "missing"):
        rows.append(("Temporal Coverage", 0, 3,
                     "No historical insurance-associated emissions data", "High",
                     "Build Part C time series"))
    elif part_c_status == "partial":
        rows.append(("Temporal Coverage", 1, 3,
                     "Current year only", "Low", "Extend to multi-year reporting"))
    else:
        rows.append(("Temporal Coverage", 2, 3,
                     "Multi-year data with trend analysis", "Low", "Add projections for maximum score"))
    return rows

# ── Generation ──────────────────────────────────────────────────────

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
            score = data.get("score"); max_s = data.get("max"); evid = data.get("evidence", "")
            notes = "V2 client-verified"
            vstatus = _detect_verification_status(evid, score, notes)
            clean_evid = _strip_verification_tag(evid)
            if score is None:
                return {"company":name,"assessment_date":"2024-12-31","institution_type":inst_type,
                        "pcaf_part":part_label,"criterion":criterion,"score":NA,"max_score":NA,
                        "percentage":"","verification_status":"[N/A]","evidence":clean_evid,
                        "priority":NA,"gap_description":NA,
                        "assessor_notes":"V2 client-verified – N/A"}
            pct = round((score/max_s)*100,1) if max_s else ""
            return {"company":name,"assessment_date":"2024-12-31","institution_type":inst_type,
                    "pcaf_part":part_label,"criterion":criterion,"score":score,"max_score":max_s,
                    "percentage":pct,"verification_status":vstatus,"evidence":clean_evid,
                    "priority":"—","gap_description":"—",
                    "assessor_notes":"V2 client-verified"}

        if v2_over:
            for part_label in ("Part A","Part B","Part C"):
                for criterion, crit_data in v2_over.get(part_label, {}).items():
                    if not criterion.startswith("_"):
                        output_rows.append(row_from_override(part_label, criterion, crit_data))
            continue

        def append_rows(part_label, scored_rows):
            for criterion, score, max_s, evidence, priority, gap in scored_rows:
                pct = "" if score==NA else (round((score/max_s)*100,1) if isinstance(max_s,(int,float)) and max_s>0 else "")
                vstatus = "[N/A]" if score == NA else "[UNVERIFIED]"
                clean_evid = _strip_verification_tag(evidence)
                output_rows.append({
                    "company":name,"assessment_date":"2024-12-31","institution_type":inst_type,
                    "pcaf_part":part_label,"criterion":criterion,"score":score,"max_score":max_s,
                    "percentage":pct,"verification_status":vstatus,"evidence":clean_evid,
                    "priority":priority,"gap_description":gap,
                    "assessor_notes":compl_data.get("recommendation",""),
                })

        append_rows("Part A", compute_part_a_scores(name, info, comp_data, compl_data, ext_cov, key))
        append_rows("Part B", compute_part_b_scores(name, info, comp_data, compl_data))
        append_rows("Part C", compute_part_c_scores(name, info, comp_data, compl_data))

    return output_rows


def main():
    rows = generate_assessment()
    output_path = os.path.join(BASE, "output", "pcaf_assessment_detailed.csv")
    fieldnames = ["company","assessment_date","institution_type","pcaf_part","criterion",
                  "score","max_score","percentage","verification_status","evidence","priority","gap_description","assessor_notes"]
    with open(output_path,"w",newline="",encoding="utf-8") as f:
        w = csv.DictWriter(f,fieldnames=fieldnames); w.writeheader(); w.writerows(rows)

    companies = sorted(set(r["company"] for r in rows))
    print(f"✓ {len(rows)} rows generated for {len(companies)} institutions → {output_path}\n")
    MAXS = {"Part A":23,"Part B":13,"Part C":13}
    print(f"{'Institution':<22} {'Type':<14}  {'Compliance A':>22}  {'Compliance B':>22}  {'Compliance C':>22}")
    print("─"*90)
    for company in companies:
        ir = [r for r in rows if r["company"]==company]
        def ptotal(part):
            pr=[r for r in ir if r["pcaf_part"]==part]
            if all(str(r["score"])==NA for r in pr): return None
            return sum(int(r["score"]) for r in pr if str(r["score"]).lstrip("-").isdigit())
        a,b,c = ptotal("Part A"),ptotal("Part B"),ptotal("Part C")
        a_s = f"{a}/{MAXS['Part A']} = {a/MAXS['Part A']:.1%}" if a is not None else NA
        b_s = f"{b}/{MAXS['Part B']} = {b/MAXS['Part B']:.1%}" if b is not None else NA
        c_s = f"{c}/{MAXS['Part C']} = {c/MAXS['Part C']:.1%}" if c is not None else NA
        print(f"{company:<22} {ir[0]['institution_type']:<14}  {a_s:>22}  {b_s:>22}  {c_s:>22}")

if __name__=="__main__":
    main()
