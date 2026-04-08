#!/usr/bin/env python3
"""
PCAF Deep Analyzer - Comprehensive data extraction from sustainability reports
Strictly follows methodology requirements
"""

import json
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional, Dict, List
import csv

REPORTS_DIR = Path("/Users/fidestra/Library/CloudStorage/OneDrive-fidestra/03_ACCOUNTS/Axylia/pcaf-compliance/resources/reports/text extraction")
OUTPUT_DIR = Path("/Users/fidestra/Library/CloudStorage/OneDrive-fidestra/03_ACCOUNTS/Axylia/pcaf-compliance/looker_data")

# Institution classification per methodology
INSTITUTIONS = {
    "ADMIRAL": {"type": "insurer", "country": "UK", "full_name": "Admiral Group"},
    "AGEAS": {"type": "insurer", "country": "Belgium", "full_name": "Ageas"},
    "ALLIANZ": {"type": "insurer", "country": "Germany", "full_name": "Allianz"},
    "AMUNDI": {"type": "asset_manager", "country": "France", "full_name": "Amundi"},
    "ASRNEDERLAND": {"type": "insurer", "country": "Netherlands", "full_name": "ASR Nederland"},
    "AVIVA": {"type": "insurer", "country": "UK", "full_name": "Aviva"},
    "AXA": {"type": "insurer", "country": "France", "full_name": "AXA"},
    "COMMERZBANK": {"type": "bank", "country": "Germany", "full_name": "Commerzbank"},
    "CREDITAGRICOLE": {"type": "bank", "country": "France", "full_name": "Crédit Agricole"},
    "DEUTSCHEBOERSE": {"type": "other", "country": "Germany", "full_name": "Deutsche Börse"},
    "EURAZEO": {"type": "asset_manager", "country": "France", "full_name": "Eurazeo"},
    "GBL": {"type": "other", "country": "Belgium", "full_name": "GBL"},
    "KBC": {"type": "bancassurance", "country": "Belgium", "full_name": "KBC"},
    "LEGALGENERAL": {"type": "insurer", "country": "UK", "full_name": "Legal & General"},
    "NNGROUP": {"type": "insurer", "country": "Netherlands", "full_name": "NN Group"},
    "NORDEA": {"type": "bank", "country": "Finland", "full_name": "Nordea"},
    "PHOENIXGROUP": {"type": "insurer", "country": "UK", "full_name": "Phoenix Group"},
    "SANTANDER": {"type": "bank", "country": "Spain", "full_name": "Santander"},
    "SCHRODERS": {"type": "asset_manager", "country": "UK", "full_name": "Schroders"},
    "SOCGEN": {"type": "bank", "country": "France", "full_name": "Société Générale"},
    "SWISSRE": {"type": "reinsurer", "country": "Switzerland", "full_name": "Swiss Re"},
    "UNICREDIT": {"type": "bank", "country": "Italy", "full_name": "UniCredit"},
    "ZURICH": {"type": "insurer", "country": "Switzerland", "full_name": "Zurich"}
}

# PCAF requirements by type
PCAF_REQUIREMENTS = {
    "insurer": {"part_a": True, "part_b": False, "part_c": True},
    "reinsurer": {"part_a": True, "part_b": False, "part_c": True},
    "bank": {"part_a": True, "part_b": True, "part_c": False},
    "asset_manager": {"part_a": True, "part_b": False, "part_c": False},
    "bancassurance": {"part_a": True, "part_b": True, "part_c": True},
    "other": {"part_a": True, "part_b": False, "part_c": False}
}

@dataclass
class EmissionsData:
    # Operational
    scope_1: Optional[float] = None
    scope_2_market: Optional[float] = None
    scope_2_location: Optional[float] = None
    scope_3_operational: Optional[float] = None
    total_operational: Optional[float] = None
    
    # Financed (Part A)
    financed_total: Optional[float] = None
    financed_unit: str = ""
    financed_coverage_pct: Optional[float] = None
    pcaf_data_quality: Optional[float] = None
    
    # By asset class
    ac_listed_equity_bonds: Optional[float] = None
    ac_business_loans: Optional[float] = None
    ac_project_finance: Optional[float] = None
    ac_commercial_re: Optional[float] = None
    ac_mortgages: Optional[float] = None
    ac_motor_loans: Optional[float] = None
    ac_sovereign: Optional[float] = None
    ac_use_of_proceeds: Optional[float] = None
    ac_securitized: Optional[float] = None
    ac_sub_sovereign: Optional[float] = None
    
    # Facilitated (Part B)
    facilitated_total: Optional[float] = None
    facilitated_unit: str = ""
    
    # Insurance (Part C)
    insurance_total: Optional[float] = None
    insurance_unit: str = ""
    insurance_commercial: Optional[float] = None
    insurance_motor: Optional[float] = None
    insurance_project: Optional[float] = None
    insurance_reinsurance: Optional[float] = None

@dataclass 
class ComplianceStatus:
    # Part A
    part_a_reported: bool = False
    part_a_partial: bool = False
    part_a_asset_classes: Dict[str, str] = field(default_factory=dict)
    
    # Part B
    part_b_reported: bool = False
    part_b_partial: bool = False
    
    # Part C
    part_c_reported: bool = False
    part_c_partial: bool = False
    part_c_lines: Dict[str, str] = field(default_factory=dict)
    
    # Metadata
    pcaf_member: bool = False
    tcfd_aligned: bool = False
    sbti_committed: bool = False

@dataclass
class InstitutionResult:
    code: str
    name: str
    inst_type: str
    country: str
    emissions: EmissionsData = field(default_factory=EmissionsData)
    compliance: ComplianceStatus = field(default_factory=ComplianceStatus)
    gaps: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)


def extract_numbers(text: str, context_pattern: str, window: int = 200) -> List[float]:
    """Extract numbers near a context pattern"""
    numbers = []
    for match in re.finditer(context_pattern, text, re.IGNORECASE):
        start = max(0, match.start() - 50)
        end = min(len(text), match.end() + window)
        snippet = text[start:end]
        # Find numbers with various formats
        num_matches = re.findall(r'[\d,]+\.?\d*', snippet)
        for n in num_matches:
            try:
                val = float(n.replace(',', ''))
                if val > 0 and val < 1e12:  # Reasonable range
                    numbers.append(val)
            except:
                pass
    return numbers


def analyze_report(filepath: Path) -> InstitutionResult:
    """Analyze a single institution report"""
    
    code = filepath.stem.replace('_2024', '')
    info = INSTITUTIONS.get(code, {"type": "other", "country": "Unknown", "full_name": code})
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    text = data.get('text', '')
    text_lower = text.lower()
    
    result = InstitutionResult(
        code=code,
        name=info['full_name'],
        inst_type=info['type'],
        country=info['country']
    )
    
    # Check PCAF membership
    result.compliance.pcaf_member = 'pcaf' in text_lower
    result.compliance.tcfd_aligned = 'tcfd' in text_lower or 'task force on climate' in text_lower
    result.compliance.sbti_committed = 'sbti' in text_lower or 'science based target' in text_lower or 'science-based target' in text_lower
    
    # ============ OPERATIONAL EMISSIONS ============
    # Scope 1
    scope1_patterns = [
        r'scope\s*1[:\s]+(\d[\d,\.]*)\s*(tco2|tonnes|t\s*co2)',
        r'scope\s*1\s*emissions[:\s]+(\d[\d,\.]*)',
        r'scope\s*1\s*\(tco2e?\)[:\s]+(\d[\d,\.]*)'
    ]
    for pattern in scope1_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                result.emissions.scope_1 = float(match.group(1).replace(',', ''))
                break
            except:
                pass
    
    # Scope 2 market-based
    scope2_market_patterns = [
        r'scope\s*2.*?market[- ]based[:\s]+(\d[\d,\.]*)',
        r'market[- ]based.*?scope\s*2[:\s]+(\d[\d,\.]*)',
    ]
    for pattern in scope2_market_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                result.emissions.scope_2_market = float(match.group(1).replace(',', ''))
                break
            except:
                pass
    
    # Scope 2 location-based  
    scope2_loc_patterns = [
        r'scope\s*2.*?location[- ]based[:\s]+(\d[\d,\.]*)',
        r'location[- ]based.*?scope\s*2[:\s]+(\d[\d,\.]*)',
    ]
    for pattern in scope2_loc_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                result.emissions.scope_2_location = float(match.group(1).replace(',', ''))
                break
            except:
                pass
    
    # ============ FINANCED EMISSIONS (Part A) ============
    financed_patterns = [
        r'financed\s+emissions[:\s]+(\d[\d,\.]*)\s*(million|mt|mtco2|tco2)',
        r'category\s*15.*?(\d[\d,\.]*)\s*(million|mt|mtco2)',
        r'investment.*?emissions[:\s]+(\d[\d,\.]*)\s*(million|mt)',
        r'portfolio\s+emissions[:\s]+(\d[\d,\.]*)\s*(million|mt)',
        r'scope\s*3.*?category\s*15.*?(\d[\d,\.]*)',
    ]
    
    for pattern in financed_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                result.emissions.financed_total = float(match.group(1).replace(',', ''))
                result.emissions.financed_unit = match.group(2).lower() if len(match.groups()) > 1 else 'unknown'
                result.compliance.part_a_partial = True
                break
            except:
                pass
    
    # Check for PCAF asset class mentions - all 10 PCAF asset classes
    asset_class_keywords = {
        'listed_equity_bonds': ['listed equity', 'corporate bond', 'equity and bonds', 'public equity', 'listed shares', 'equity portfolio', 'bond portfolio'],
        'business_loans': ['business loan', 'corporate loan', 'sme loan', 'commercial lending', 'corporate lending', 'business lending', 'commercial loans'],
        'project_finance': ['project finance', 'infrastructure finance', 'project-finance'],
        'commercial_re': ['commercial real estate', 'real estate debt', 'cre ', 'commercial property', 'office building', 'retail property'],
        'mortgages': ['mortgage', 'residential mortgage', 'home loan', 'housing loan', 'residential real estate', 'housing finance'],
        'motor_loans': ['motor vehicle', 'auto loan', 'car loan', 'vehicle finance', 'auto finance', 'car finance'],
        'sovereign': ['sovereign debt', 'government bond', 'sovereigns', 'sovereign bond', 'government securities', 'treasury'],
        'sub_sovereign': ['sub-sovereign', 'municipal', 'local government', 'regional government', 'municipal bond'],
        'use_of_proceeds': ['use of proceeds', 'green bond', 'sustainability bond', 'social bond', 'sustainable bond', 'green finance', 'sustainability-linked'],
        'securitized': ['securiti', 'abs ', 'mbs ', 'structured product', 'asset-backed', 'mortgage-backed', 'clo ', 'collateralized', 'structured finance']
    }
    
    reported_asset_classes = 0
    for ac_key, keywords in asset_class_keywords.items():
        for kw in keywords:
            # Check if mentioned with emissions context
            if kw in text_lower:
                # Look for emissions data nearby
                context = re.search(rf'{kw}.{{0,300}}(emissions|tco2|mtco2|carbon)', text, re.IGNORECASE)
                if context:
                    result.compliance.part_a_asset_classes[ac_key] = 'partial'
                    reported_asset_classes += 1
                    break
    
    # Check for quantitative asset class data
    for ac_key in asset_class_keywords.keys():
        kws = asset_class_keywords[ac_key]
        for kw in kws:
            match = re.search(rf'{kw}[:\s].*?(\d[\d,\.]+)\s*(tco2|mtco2|million)', text, re.IGNORECASE)
            if match:
                result.compliance.part_a_asset_classes[ac_key] = 'reported'
                break
    
    # Determine Part A status
    reported_count = sum(1 for v in result.compliance.part_a_asset_classes.values() if v == 'reported')
    partial_count = sum(1 for v in result.compliance.part_a_asset_classes.values() if v == 'partial')
    
    if reported_count >= 5:
        result.compliance.part_a_reported = True
    elif reported_count >= 2 or partial_count >= 3 or result.emissions.financed_total:
        result.compliance.part_a_partial = True
    
    # ============ FACILITATED EMISSIONS (Part B) ============
    facilitated_patterns = [
        r'facilitated\s+emissions[:\s]+(\d[\d,\.]*)',
        r'capital\s+market.*?emissions[:\s]+(\d[\d,\.]*)',
        r'underwriting.*?scope\s*3[:\s]+(\d[\d,\.]*)',
    ]
    
    for pattern in facilitated_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                result.emissions.facilitated_total = float(match.group(1).replace(',', ''))
                result.compliance.part_b_reported = True
                break
            except:
                pass
    
    # Check for facilitated emissions mention without numbers
    if not result.compliance.part_b_reported:
        if re.search(r'facilitated\s+emissions', text, re.IGNORECASE):
            result.compliance.part_b_partial = True
    
    # ============ INSURANCE EMISSIONS (Part C) ============
    insurance_patterns = [
        r'insurance[- ]associated\s+emissions[:\s]+(\d[\d,\.]*)',
        r'underwriting\s+emissions[:\s]+(\d[\d,\.]*)',
        r'part\s*c.*?emissions[:\s]+(\d[\d,\.]*)',
    ]
    
    for pattern in insurance_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                result.emissions.insurance_total = float(match.group(1).replace(',', ''))
                result.compliance.part_c_reported = True
                break
            except:
                pass
    
    # Check for insurance line mentions
    insurance_lines = {
        'commercial': ['commercial line', 'commercial insurance', 'p&c ', 'property and casualty'],
        'motor': ['motor insurance', 'auto insurance', 'vehicle insurance', 'car insurance'],
        'project': ['project insurance'],
        'reinsurance': ['reinsurance', 'treaty']
    }
    
    for line_key, keywords in insurance_lines.items():
        for kw in keywords:
            if kw in text_lower and 'emission' in text_lower:
                result.compliance.part_c_lines[line_key] = 'partial'
                result.compliance.part_c_partial = True
                break
    
    # ============ GAP ANALYSIS ============
    reqs = PCAF_REQUIREMENTS.get(result.inst_type, PCAF_REQUIREMENTS['other'])
    
    # Part A gaps
    if reqs['part_a']:
        if not result.compliance.part_a_reported and not result.compliance.part_a_partial:
            result.gaps.append("CRITICAL: No financed emissions reported (Part A)")
            result.recommendations.append("Priority 1: Implement PCAF Part A methodology")
        elif result.compliance.part_a_partial and not result.compliance.part_a_reported:
            missing_classes = [k for k, v in result.compliance.part_a_asset_classes.items() if v != 'reported']
            if missing_classes:
                result.gaps.append(f"MODERATE: Missing asset class detail for Part A")
                result.recommendations.append("Priority 2: Break down financed emissions by 10 PCAF asset classes")
    
    # Part B gaps (banks only)
    if reqs['part_b']:
        if not result.compliance.part_b_reported and not result.compliance.part_b_partial:
            result.gaps.append("MODERATE: No facilitated emissions reported (Part B)")
            result.recommendations.append("Priority 2: Report capital market facilitated emissions")
        elif result.compliance.part_b_partial:
            result.gaps.append("MINOR: Facilitated emissions mentioned but incomplete")
    
    # Part C gaps (insurers only)
    if reqs['part_c']:
        if not result.compliance.part_c_reported and not result.compliance.part_c_partial:
            result.gaps.append("CRITICAL: No insurance-associated emissions reported (Part C)")
            result.recommendations.append("Priority 1: Implement PCAF Part C methodology")
        elif result.compliance.part_c_partial and not result.compliance.part_c_reported:
            result.gaps.append("MODERATE: Insurance emissions partially reported")
            result.recommendations.append("Priority 2: Report emissions by insurance line")
    
    return result


def get_part_a_status(r: InstitutionResult) -> str:
    if r.compliance.part_a_reported:
        return "REPORTED"
    elif r.compliance.part_a_partial:
        return "PARTIAL"
    return "MISSING"


def get_part_b_status(r: InstitutionResult) -> str:
    reqs = PCAF_REQUIREMENTS.get(r.inst_type, {})
    if not reqs.get('part_b', False):
        return "N/A"
    if r.compliance.part_b_reported:
        return "REPORTED"
    elif r.compliance.part_b_partial:
        return "PARTIAL"
    return "MISSING"


def get_part_c_status(r: InstitutionResult) -> str:
    reqs = PCAF_REQUIREMENTS.get(r.inst_type, {})
    if not reqs.get('part_c', False):
        return "N/A"
    if r.compliance.part_c_reported:
        return "REPORTED"
    elif r.compliance.part_c_partial:
        return "PARTIAL"
    return "MISSING"


def export_operational_emissions(results: List[InstitutionResult]):
    """Export operational_emissions.csv per Looker guide"""
    path = OUTPUT_DIR / "operational_emissions.csv"
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['company', 'year', 'reporting_date', 'scope_1_tco2e', 'scope_2_market_tco2e', 
                        'scope_2_location_tco2e', 'scope_3_operational_tco2e', 'total_market_based_tco2e', 'net_emissions_tco2e'])
        for r in sorted(results, key=lambda x: x.name):
            for year in [2024, 2023, 2022]:
                s1 = r.emissions.scope_1 if year == 2024 else ''
                s2m = r.emissions.scope_2_market if year == 2024 else ''
                s2l = r.emissions.scope_2_location if year == 2024 else ''
                s3 = r.emissions.scope_3_operational if year == 2024 else ''
                total = r.emissions.total_operational if year == 2024 else ''
                writer.writerow([r.name, year, f'{year}-12-31', s1 or '', s2m or '', s2l or '', s3 or '', total or '', ''])
    print(f"Saved: {path}")


def export_financed_emissions(results: List[InstitutionResult]):
    """Export financed_emissions.csv per Looker guide"""
    path = OUTPUT_DIR / "financed_emissions.csv"
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['company', 'year', 'category', 'emissions_million_tco2e', 'asset_class', 'coverage_percent', 'data_quality_score'])
        for r in sorted(results, key=lambda x: x.name):
            em = r.emissions.financed_total or ''
            unit = r.emissions.financed_unit or 'Mixed (aggregate)'
            cov = r.emissions.financed_coverage_pct or ''
            dq = r.emissions.pcaf_data_quality or ''
            writer.writerow([r.name, 2024, 'Category 15 - Investments', em, unit, cov, dq])
    print(f"Saved: {path}")


def export_pcaf_compliance(results: List[InstitutionResult]):
    """Export pcaf_compliance.csv per Looker guide"""
    path = OUTPUT_DIR / "pcaf_compliance.csv"
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['company', 'assessment_date', 'pcaf_part', 'status', 'completeness_percent', 'missing_elements', 'priority'])
        
        for r in sorted(results, key=lambda x: x.name):
            reqs = PCAF_REQUIREMENTS.get(r.inst_type, {})
            
            # Part A
            if reqs.get('part_a', True):
                status = get_part_a_status(r)
                pct = 90 if status == 'REPORTED' else (50 if status == 'PARTIAL' else 0)
                missing = 'Minor gaps' if status == 'REPORTED' else ('Asset class breakdown' if status == 'PARTIAL' else 'All')
                priority = 'Low' if status == 'REPORTED' else ('High' if status == 'PARTIAL' else 'Critical')
                writer.writerow([r.name, '2026-02-10', 'Part A - Financed Emissions', status, pct, missing, priority])
            
            # Part B
            if reqs.get('part_b', False):
                status = get_part_b_status(r)
                if status != 'N/A':
                    pct = 90 if status == 'REPORTED' else (30 if status == 'PARTIAL' else 0)
                    missing = 'Minor gaps' if status == 'REPORTED' else ('Incomplete disclosure' if status == 'PARTIAL' else 'Capital market emissions')
                    priority = 'Low' if status == 'REPORTED' else ('Medium' if status == 'PARTIAL' else 'High')
                    writer.writerow([r.name, '2026-02-10', 'Part B - Facilitated Emissions', status, pct, missing, priority])
            
            # Part C
            if reqs.get('part_c', False):
                status = get_part_c_status(r)
                if status != 'N/A':
                    pct = 90 if status == 'REPORTED' else (25 if status == 'PARTIAL' else 0)
                    missing = 'Minor gaps' if status == 'REPORTED' else ('Insurance line breakdown' if status == 'PARTIAL' else 'All insurance lines')
                    priority = 'Low' if status == 'REPORTED' else ('High' if status == 'PARTIAL' else 'Critical')
                    writer.writerow([r.name, '2026-02-10', 'Part C - Insurance Emissions', status, pct, missing, priority])
    
    print(f"Saved: {path}")


def export_asset_classes(results: List[InstitutionResult]):
    """Export asset_class_emissions.csv per Looker guide"""
    path = OUTPUT_DIR / "asset_class_emissions.csv"
    
    asset_classes = [
        ('Listed equity and corporate bonds', 'listed_equity_bonds'),
        ('Business loans and unlisted equity', 'business_loans'),
        ('Project finance', 'project_finance'),
        ('Commercial real estate', 'commercial_re'),
        ('Mortgages', 'mortgages'),
        ('Motor vehicle loans', 'motor_loans'),
        ('Use of proceeds', 'use_of_proceeds'),
        ('Securitized and structured products', 'securitized'),
        ('Sovereign debt', 'sovereign'),
        ('Sub-sovereign debt', 'sub_sovereign')
    ]
    
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['company', 'year', 'asset_class', 'emissions_million_tco2e', 'coverage_percent', 'reported'])
        
        for r in sorted(results, key=lambda x: x.name):
            for ac_name, ac_key in asset_classes:
                status = r.compliance.part_a_asset_classes.get(ac_key, 'missing')
                reported = status in ['reported', 'partial']
                coverage = 70 if status == 'reported' else (40 if status == 'partial' else 0)
                writer.writerow([r.name, 2024, ac_name, '', coverage, 'TRUE' if reported else 'FALSE'])
    
    print(f"Saved: {path}")


def print_summary(results: List[InstitutionResult]):
    """Print compliance summary"""
    print("\n" + "="*100)
    print("PCAF COMPLIANCE ANALYSIS - SUMMARY")
    print("="*100)
    
    # Group by type
    by_type = {}
    for r in results:
        by_type.setdefault(r.inst_type, []).append(r)
    
    for inst_type, institutions in sorted(by_type.items()):
        print(f"\n{'='*50}")
        print(f"INSTITUTION TYPE: {inst_type.upper()}")
        reqs = PCAF_REQUIREMENTS.get(inst_type, {})
        req_parts = [p for p, v in reqs.items() if v]
        print(f"Required PCAF Parts: {', '.join(req_parts)}")
        print(f"{'='*50}")
        
        for r in sorted(institutions, key=lambda x: x.name):
            print(f"\n--- {r.name} ({r.country}) ---")
            print(f"  PCAF Member: {'Yes' if r.compliance.pcaf_member else 'No'}")
            print(f"  Part A (Financed):    {get_part_a_status(r)}")
            
            if reqs.get('part_b'):
                print(f"  Part B (Facilitated): {get_part_b_status(r)}")
            
            if reqs.get('part_c'):
                print(f"  Part C (Insurance):   {get_part_c_status(r)}")
            
            if r.emissions.financed_total:
                print(f"  Financed Emissions:   {r.emissions.financed_total:,.1f} {r.emissions.financed_unit}")
            
            if r.gaps:
                print("  Gaps:")
                for gap in r.gaps[:3]:
                    print(f"    • {gap}")
    
    # Statistics
    print("\n" + "="*100)
    print("STATISTICS")
    print("="*100)
    
    total = len(results)
    pcaf_members = sum(1 for r in results if r.compliance.pcaf_member)
    part_a_reported = sum(1 for r in results if r.compliance.part_a_reported)
    part_a_partial = sum(1 for r in results if r.compliance.part_a_partial and not r.compliance.part_a_reported)
    part_a_missing = total - part_a_reported - part_a_partial
    
    print(f"\nTotal Institutions: {total}")
    print(f"PCAF Members: {pcaf_members} ({pcaf_members/total*100:.1f}%)")
    print(f"\nPart A Compliance:")
    print(f"  Reported: {part_a_reported}")
    print(f"  Partial:  {part_a_partial}")
    print(f"  Missing:  {part_a_missing}")
    
    # Count critical gaps
    critical = sum(1 for r in results if any('CRITICAL' in g for g in r.gaps))
    print(f"\nInstitutions with Critical Gaps: {critical}")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    json_files = list(REPORTS_DIR.glob('*.json'))
    print(f"Analyzing {len(json_files)} reports...")
    
    results = []
    for filepath in json_files:
        print(f"  Processing: {filepath.stem}")
        try:
            result = analyze_report(filepath)
            results.append(result)
        except Exception as e:
            print(f"    ERROR: {e}")
    
    print(f"\nCompleted analysis of {len(results)} institutions")
    
    # Export files
    export_operational_emissions(results)
    export_financed_emissions(results)
    export_pcaf_compliance(results)
    export_asset_classes(results)
    
    # Print summary
    print_summary(results)
    
    return results


if __name__ == "__main__":
    main()
