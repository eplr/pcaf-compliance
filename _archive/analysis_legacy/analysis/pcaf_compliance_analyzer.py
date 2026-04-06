#!/usr/bin/env python3
"""
PCAF Compliance Analyzer
Analyzes financial institution sustainability reports for PCAF compliance
"""

import json
import os
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
import csv

# Configuration
REPORTS_DIR = Path("/Users/fidestra/Library/CloudStorage/OneDrive-fidestra/03_ACCOUNTS/Axylia/pcaf-compliance/resources/reports/text extraction")
OUTPUT_DIR = Path("/Users/fidestra/Library/CloudStorage/OneDrive-fidestra/03_ACCOUNTS/Axylia/pcaf-compliance/analysis/results")

# Institution classification
INSTITUTION_TYPES = {
    "ADMIRAL": "insurer",
    "AGEAS": "insurer",
    "ALLIANZ": "insurer",
    "AMUNDI": "asset_manager",
    "ASRNEDERLAND": "insurer",
    "AVIVA": "insurer",
    "AXA": "insurer",
    "COMMERZBANK": "bank",
    "CREDITAGRICOLE": "bank",
    "DEUTSCHEBOERSE": "exchange",
    "EURAZEO": "asset_manager",
    "GBL": "investment_holding",
    "KBC": "bancassurance",
    "LEGALGENERAL": "insurer",
    "NNGROUP": "insurer",
    "NORDEA": "bank",
    "PHOENIXGROUP": "insurer",
    "SANTANDER": "bank",
    "SCHRODERS": "asset_manager",
    "SOCGEN": "bank",
    "SWISSRE": "reinsurer",
    "UNICREDIT": "bank",
    "ZURICH": "insurer"
}

# PCAF Parts required by institution type
PCAF_REQUIREMENTS = {
    "insurer": ["part_a", "part_c"],
    "reinsurer": ["part_a", "part_c"],
    "bank": ["part_a", "part_b"],
    "asset_manager": ["part_a"],
    "bancassurance": ["part_a", "part_b", "part_c"],
    "exchange": ["part_a"],
    "investment_holding": ["part_a"]
}

@dataclass
class EmissionsData:
    """Store extracted emissions data"""
    # Operational emissions (tCO2e)
    scope_1: Optional[float] = None
    scope_2_market: Optional[float] = None
    scope_2_location: Optional[float] = None
    scope_3_operational: Optional[float] = None
    
    # Financed emissions (MtCO2e or tCO2e)
    financed_emissions_total: Optional[float] = None
    financed_emissions_unit: str = "unknown"
    
    # Insurance-associated emissions
    insurance_emissions_total: Optional[float] = None
    
    # Facilitated emissions
    facilitated_emissions_total: Optional[float] = None
    
    # Data quality
    pcaf_data_quality_score: Optional[float] = None
    
    # Coverage
    financed_coverage_pct: Optional[float] = None

@dataclass
class PCAFCompliance:
    """PCAF compliance assessment"""
    # Part A: Financed Emissions by asset class
    listed_equity_bonds: str = "missing"  # reported/partial/missing
    business_loans: str = "missing"
    project_finance: str = "missing"
    commercial_real_estate: str = "missing"
    mortgages: str = "missing"
    motor_vehicle_loans: str = "missing"
    use_of_proceeds: str = "missing"
    securitized_products: str = "missing"
    sovereign_debt: str = "missing"
    sub_sovereign_debt: str = "missing"
    
    # Part B: Facilitated Emissions
    facilitated_emissions: str = "missing"
    
    # Part C: Insurance-Associated Emissions
    commercial_lines: str = "missing"
    project_insurance: str = "missing"
    personal_motor: str = "missing"
    treaty_reinsurance: str = "missing"
    
    # Overall assessment
    part_a_status: str = "missing"
    part_b_status: str = "missing"
    part_c_status: str = "missing"

@dataclass
class InstitutionAnalysis:
    """Complete analysis for one institution"""
    name: str
    institution_type: str
    required_pcaf_parts: list = field(default_factory=list)
    emissions: EmissionsData = field(default_factory=EmissionsData)
    compliance: PCAFCompliance = field(default_factory=PCAFCompliance)
    gaps: list = field(default_factory=list)
    recommendations: list = field(default_factory=list)
    raw_text_excerpts: dict = field(default_factory=dict)


def extract_number(text: str, patterns: list[str]) -> Optional[float]:
    """Extract a number following any of the given patterns"""
    for pattern in patterns:
        # Search for pattern followed by number
        match = re.search(rf'{pattern}[:\s]*([0-9,.\s]+)', text, re.IGNORECASE)
        if match:
            num_str = match.group(1).replace(',', '').replace(' ', '').strip()
            try:
                return float(num_str)
            except ValueError:
                continue
    return None


def analyze_operational_emissions(text: str, analysis: InstitutionAnalysis):
    """Extract operational emissions (Scope 1, 2, 3)"""
    
    # Look for Scope 1 emissions
    scope1_patterns = [
        r'Scope 1[:\s]+([0-9,.\s]+)\s*(?:tCO2e|tonnes|t\s*CO2)',
        r'Scope 1 emissions[:\s]+([0-9,.\s]+)',
        r'Scope 1 \(tCO2e\)[:\s]+([0-9,.\s]+)'
    ]
    for pattern in scope1_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                analysis.emissions.scope_1 = float(match.group(1).replace(',', '').replace(' ', ''))
                break
            except ValueError:
                continue
    
    # Look for Scope 2 market-based
    scope2_market_patterns = [
        r'Scope 2.*?market.based[:\s]*([0-9,.\s]+)',
        r'market.based.*?Scope 2[:\s]*([0-9,.\s]+)',
        r'Scope 2 \(market\)[:\s]*([0-9,.\s]+)'
    ]
    for pattern in scope2_market_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                analysis.emissions.scope_2_market = float(match.group(1).replace(',', '').replace(' ', ''))
                break
            except ValueError:
                continue
    
    # Look for Scope 2 location-based
    scope2_loc_patterns = [
        r'Scope 2.*?location.based[:\s]*([0-9,.\s]+)',
        r'location.based.*?Scope 2[:\s]*([0-9,.\s]+)'
    ]
    for pattern in scope2_loc_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                analysis.emissions.scope_2_location = float(match.group(1).replace(',', '').replace(' ', ''))
                break
            except ValueError:
                continue


def analyze_financed_emissions(text: str, analysis: InstitutionAnalysis):
    """Extract financed emissions data and assess Part A compliance"""
    
    # Look for total financed emissions
    financed_patterns = [
        r'financed emissions[:\s]*([0-9,.\s]+)\s*(million|Mt|MtCO2e|tCO2e)',
        r'Category 15.*?([0-9,.\s]+)\s*(million|Mt|MtCO2e)',
        r'investment emissions[:\s]*([0-9,.\s]+)\s*(million|Mt|MtCO2e|tCO2e)',
        r'portfolio emissions[:\s]*([0-9,.\s]+)\s*(million|Mt|MtCO2e)'
    ]
    for pattern in financed_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                analysis.emissions.financed_emissions_total = float(match.group(1).replace(',', '').replace(' ', ''))
                analysis.emissions.financed_emissions_unit = match.group(2).lower()
                break
            except (ValueError, IndexError):
                continue
    
    # Check for asset class breakdowns
    asset_class_keywords = {
        'listed_equity_bonds': ['listed equity', 'corporate bond', 'public equity', 'equity and bonds'],
        'business_loans': ['business loan', 'corporate loan', 'SME loan', 'commercial loan'],
        'project_finance': ['project finance'],
        'commercial_real_estate': ['commercial real estate', 'CRE', 'real estate debt'],
        'mortgages': ['mortgage', 'residential mortgage', 'home loan'],
        'motor_vehicle_loans': ['motor vehicle loan', 'auto loan', 'vehicle finance'],
        'sovereign_debt': ['sovereign', 'government bond'],
        'sub_sovereign_debt': ['sub-sovereign', 'municipal']
    }
    
    text_lower = text.lower()
    for asset_class, keywords in asset_class_keywords.items():
        for keyword in keywords:
            if keyword in text_lower:
                # Check if there's quantitative data nearby
                if re.search(rf'{keyword}.*?([0-9,]+)\s*(tCO2|MtCO2|million)', text, re.IGNORECASE):
                    setattr(analysis.compliance, asset_class, "reported")
                else:
                    current = getattr(analysis.compliance, asset_class)
                    if current == "missing":
                        setattr(analysis.compliance, asset_class, "partial")
                break
    
    # Determine overall Part A status
    part_a_fields = ['listed_equity_bonds', 'business_loans', 'project_finance', 
                     'commercial_real_estate', 'mortgages', 'motor_vehicle_loans',
                     'sovereign_debt', 'sub_sovereign_debt']
    
    reported_count = sum(1 for f in part_a_fields if getattr(analysis.compliance, f) == "reported")
    partial_count = sum(1 for f in part_a_fields if getattr(analysis.compliance, f) == "partial")
    
    if reported_count >= 5:
        analysis.compliance.part_a_status = "reported"
    elif reported_count >= 2 or partial_count >= 3:
        analysis.compliance.part_a_status = "partial"
    elif analysis.emissions.financed_emissions_total:
        analysis.compliance.part_a_status = "partial"
    else:
        analysis.compliance.part_a_status = "missing"


def analyze_facilitated_emissions(text: str, analysis: InstitutionAnalysis):
    """Extract facilitated emissions data (Part B)"""
    
    facilitated_patterns = [
        r'facilitated emissions[:\s]*([0-9,.\s]+)',
        r'capital market.*?emissions[:\s]*([0-9,.\s]+)',
        r'underwriting.*?emissions[:\s]*([0-9,.\s]+)'
    ]
    
    for pattern in facilitated_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                analysis.emissions.facilitated_emissions_total = float(match.group(1).replace(',', '').replace(' ', ''))
                analysis.compliance.facilitated_emissions = "reported"
                analysis.compliance.part_b_status = "reported"
                return
            except ValueError:
                continue
    
    # Check for mentions without quantitative data
    if re.search(r'facilitated emissions', text, re.IGNORECASE):
        analysis.compliance.facilitated_emissions = "partial"
        analysis.compliance.part_b_status = "partial"


def analyze_insurance_emissions(text: str, analysis: InstitutionAnalysis):
    """Extract insurance-associated emissions data (Part C)"""
    
    insurance_patterns = [
        r'insurance.associated emissions[:\s]*([0-9,.\s]+)',
        r'underwriting emissions[:\s]*([0-9,.\s]+)',
        r'insurance portfolio emissions[:\s]*([0-9,.\s]+)'
    ]
    
    for pattern in insurance_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                analysis.emissions.insurance_emissions_total = float(match.group(1).replace(',', '').replace(' ', ''))
                analysis.compliance.part_c_status = "reported"
                return
            except ValueError:
                continue
    
    # Check for specific insurance line mentions
    insurance_lines = {
        'commercial_lines': ['commercial line', 'commercial insurance', 'P&C'],
        'personal_motor': ['motor insurance', 'auto insurance', 'vehicle insurance'],
        'treaty_reinsurance': ['reinsurance', 'treaty']
    }
    
    text_lower = text.lower()
    found_any = False
    for line_type, keywords in insurance_lines.items():
        for keyword in keywords:
            if keyword in text_lower and 'emission' in text_lower:
                setattr(analysis.compliance, line_type, "partial")
                found_any = True
                break
    
    if found_any:
        analysis.compliance.part_c_status = "partial"


def analyze_pcaf_mentions(text: str, analysis: InstitutionAnalysis):
    """Check for PCAF methodology mentions and data quality scores"""
    
    text_lower = text.lower()
    
    # Check for PCAF membership/methodology
    if 'pcaf' in text_lower:
        analysis.raw_text_excerpts['pcaf_mentioned'] = True
        
        # Look for data quality score
        dq_match = re.search(r'data quality.*?score.*?([1-5](?:\.[0-9]+)?)', text, re.IGNORECASE)
        if dq_match:
            try:
                analysis.emissions.pcaf_data_quality_score = float(dq_match.group(1))
            except ValueError:
                pass
    else:
        analysis.raw_text_excerpts['pcaf_mentioned'] = False


def generate_gaps_and_recommendations(analysis: InstitutionAnalysis):
    """Generate gap analysis and recommendations"""
    
    inst_type = analysis.institution_type
    required_parts = analysis.required_pcaf_parts
    
    # Part A gaps (all institutions)
    if 'part_a' in required_parts:
        if analysis.compliance.part_a_status == "missing":
            analysis.gaps.append("CRITICAL: No financed emissions reported (PCAF Part A)")
            analysis.recommendations.append("Priority 1: Implement PCAF Part A methodology for investment portfolio")
        elif analysis.compliance.part_a_status == "partial":
            # Check specific missing asset classes
            missing_classes = []
            for field in ['listed_equity_bonds', 'business_loans', 'project_finance', 
                         'commercial_real_estate', 'mortgages', 'sovereign_debt']:
                if getattr(analysis.compliance, field) == "missing":
                    missing_classes.append(field.replace('_', ' '))
            if missing_classes:
                analysis.gaps.append(f"MODERATE: Missing asset class breakdown for: {', '.join(missing_classes[:3])}")
                analysis.recommendations.append("Priority 2: Break down financed emissions by PCAF asset classes")
    
    # Part B gaps (banks)
    if 'part_b' in required_parts:
        if analysis.compliance.part_b_status == "missing":
            analysis.gaps.append("MODERATE: No facilitated emissions reported (PCAF Part B)")
            analysis.recommendations.append("Priority 2: Report capital market facilitated emissions")
        elif analysis.compliance.part_b_status == "partial":
            analysis.gaps.append("MINOR: Facilitated emissions mentioned but incomplete")
    
    # Part C gaps (insurers)
    if 'part_c' in required_parts:
        if analysis.compliance.part_c_status == "missing":
            analysis.gaps.append("CRITICAL: No insurance-associated emissions reported (PCAF Part C)")
            analysis.recommendations.append("Priority 1: Implement PCAF Part C methodology for insurance portfolios")
        elif analysis.compliance.part_c_status == "partial":
            analysis.gaps.append("MODERATE: Insurance emissions partially reported - missing line breakdowns")
            analysis.recommendations.append("Priority 2: Report emissions by insurance line (commercial, motor, reinsurance)")


def analyze_institution(filepath: Path) -> InstitutionAnalysis:
    """Analyze a single institution's report"""
    
    # Extract institution name from filename
    name = filepath.stem.replace('_2024', '')
    
    # Load JSON
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    text = data.get('text', '')
    
    # Initialize analysis
    inst_type = INSTITUTION_TYPES.get(name, 'unknown')
    analysis = InstitutionAnalysis(
        name=name,
        institution_type=inst_type,
        required_pcaf_parts=PCAF_REQUIREMENTS.get(inst_type, ['part_a'])
    )
    
    # Run all analysis functions
    analyze_operational_emissions(text, analysis)
    analyze_financed_emissions(text, analysis)
    analyze_facilitated_emissions(text, analysis)
    analyze_insurance_emissions(text, analysis)
    analyze_pcaf_mentions(text, analysis)
    generate_gaps_and_recommendations(analysis)
    
    return analysis


def generate_compliance_matrix(analyses: list[InstitutionAnalysis]) -> str:
    """Generate a compliance matrix summary"""
    
    output = []
    output.append("=" * 100)
    output.append("PCAF COMPLIANCE ANALYSIS - SUMMARY MATRIX")
    output.append("=" * 100)
    output.append("")
    
    # Status symbols
    status_symbols = {"reported": "✓", "partial": "⚠", "missing": "✗"}
    
    # Group by institution type
    by_type = {}
    for a in analyses:
        by_type.setdefault(a.institution_type, []).append(a)
    
    for inst_type, institutions in sorted(by_type.items()):
        output.append(f"\n{'='*50}")
        output.append(f"INSTITUTION TYPE: {inst_type.upper()}")
        output.append(f"Required PCAF Parts: {', '.join(PCAF_REQUIREMENTS.get(inst_type, ['part_a']))}")
        output.append(f"{'='*50}")
        
        for a in sorted(institutions, key=lambda x: x.name):
            output.append(f"\n--- {a.name} ---")
            output.append(f"Part A (Financed):    {status_symbols.get(a.compliance.part_a_status, '?')} {a.compliance.part_a_status.upper()}")
            
            if 'part_b' in a.required_pcaf_parts:
                output.append(f"Part B (Facilitated): {status_symbols.get(a.compliance.part_b_status, '?')} {a.compliance.part_b_status.upper()}")
            
            if 'part_c' in a.required_pcaf_parts:
                output.append(f"Part C (Insurance):   {status_symbols.get(a.compliance.part_c_status, '?')} {a.compliance.part_c_status.upper()}")
            
            # Show key emissions data
            if a.emissions.financed_emissions_total:
                output.append(f"Financed Emissions:   {a.emissions.financed_emissions_total:,.1f} {a.emissions.financed_emissions_unit}")
            
            # Show gaps
            if a.gaps:
                output.append("Gaps identified:")
                for gap in a.gaps[:3]:
                    output.append(f"  • {gap}")
    
    return "\n".join(output)


def generate_detailed_report(analyses: list[InstitutionAnalysis]) -> str:
    """Generate detailed analysis report"""
    
    output = []
    output.append("=" * 100)
    output.append("PCAF COMPLIANCE ANALYSIS - DETAILED REPORT")
    output.append("Generated: 2026-02-10")
    output.append("=" * 100)
    
    for a in sorted(analyses, key=lambda x: (x.institution_type, x.name)):
        output.append(f"\n{'#'*80}")
        output.append(f"# {a.name}")
        output.append(f"{'#'*80}")
        output.append(f"Institution Type: {a.institution_type}")
        output.append(f"Required PCAF Parts: {', '.join(a.required_pcaf_parts)}")
        output.append(f"PCAF Mentioned in Report: {a.raw_text_excerpts.get('pcaf_mentioned', 'Unknown')}")
        
        output.append("\n## Operational Emissions")
        output.append(f"  Scope 1:              {a.emissions.scope_1:,.0f} tCO2e" if a.emissions.scope_1 else "  Scope 1:              Not found")
        output.append(f"  Scope 2 (market):     {a.emissions.scope_2_market:,.0f} tCO2e" if a.emissions.scope_2_market else "  Scope 2 (market):     Not found")
        output.append(f"  Scope 2 (location):   {a.emissions.scope_2_location:,.0f} tCO2e" if a.emissions.scope_2_location else "  Scope 2 (location):   Not found")
        
        output.append("\n## PCAF Part A: Financed Emissions")
        output.append(f"  Status: {a.compliance.part_a_status.upper()}")
        if a.emissions.financed_emissions_total:
            output.append(f"  Total: {a.emissions.financed_emissions_total:,.1f} {a.emissions.financed_emissions_unit}")
        output.append("  Asset Class Breakdown:")
        output.append(f"    Listed equity/bonds:    {a.compliance.listed_equity_bonds}")
        output.append(f"    Business loans:         {a.compliance.business_loans}")
        output.append(f"    Project finance:        {a.compliance.project_finance}")
        output.append(f"    Commercial real estate: {a.compliance.commercial_real_estate}")
        output.append(f"    Mortgages:              {a.compliance.mortgages}")
        output.append(f"    Motor vehicle loans:    {a.compliance.motor_vehicle_loans}")
        output.append(f"    Sovereign debt:         {a.compliance.sovereign_debt}")
        output.append(f"    Sub-sovereign debt:     {a.compliance.sub_sovereign_debt}")
        
        if 'part_b' in a.required_pcaf_parts:
            output.append("\n## PCAF Part B: Facilitated Emissions")
            output.append(f"  Status: {a.compliance.part_b_status.upper()}")
            if a.emissions.facilitated_emissions_total:
                output.append(f"  Total: {a.emissions.facilitated_emissions_total:,.1f}")
        
        if 'part_c' in a.required_pcaf_parts:
            output.append("\n## PCAF Part C: Insurance-Associated Emissions")
            output.append(f"  Status: {a.compliance.part_c_status.upper()}")
            if a.emissions.insurance_emissions_total:
                output.append(f"  Total: {a.emissions.insurance_emissions_total:,.1f}")
            output.append("  By Insurance Line:")
            output.append(f"    Commercial lines:    {a.compliance.commercial_lines}")
            output.append(f"    Personal motor:      {a.compliance.personal_motor}")
            output.append(f"    Treaty reinsurance:  {a.compliance.treaty_reinsurance}")
        
        output.append("\n## Gap Analysis")
        if a.gaps:
            for gap in a.gaps:
                output.append(f"  • {gap}")
        else:
            output.append("  No critical gaps identified")
        
        output.append("\n## Recommendations")
        if a.recommendations:
            for rec in a.recommendations:
                output.append(f"  • {rec}")
        else:
            output.append("  Continue current reporting practices")
    
    return "\n".join(output)


def export_to_csv(analyses: list[InstitutionAnalysis], filepath: Path):
    """Export results to CSV"""
    
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow([
            'Institution', 'Type', 'PCAF Mentioned',
            'Scope 1 (tCO2e)', 'Scope 2 Market (tCO2e)',
            'Financed Emissions', 'Financed Unit',
            'Part A Status', 'Part B Status', 'Part C Status',
            'Listed Equity/Bonds', 'Business Loans', 'Mortgages', 'Sovereign Debt',
            'Critical Gaps', 'Primary Recommendation'
        ])
        
        for a in sorted(analyses, key=lambda x: x.name):
            writer.writerow([
                a.name,
                a.institution_type,
                a.raw_text_excerpts.get('pcaf_mentioned', ''),
                a.emissions.scope_1 or '',
                a.emissions.scope_2_market or '',
                a.emissions.financed_emissions_total or '',
                a.emissions.financed_emissions_unit,
                a.compliance.part_a_status,
                a.compliance.part_b_status if 'part_b' in a.required_pcaf_parts else 'N/A',
                a.compliance.part_c_status if 'part_c' in a.required_pcaf_parts else 'N/A',
                a.compliance.listed_equity_bonds,
                a.compliance.business_loans,
                a.compliance.mortgages,
                a.compliance.sovereign_debt,
                '; '.join([g for g in a.gaps if 'CRITICAL' in g]) or 'None',
                a.recommendations[0] if a.recommendations else 'None'
            ])


def main():
    """Main analysis function"""
    
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Get all JSON files
    json_files = list(REPORTS_DIR.glob('*.json'))
    print(f"Found {len(json_files)} reports to analyze")
    
    # Analyze each institution
    analyses = []
    for filepath in json_files:
        print(f"Analyzing: {filepath.stem}")
        try:
            analysis = analyze_institution(filepath)
            analyses.append(analysis)
        except Exception as e:
            print(f"  ERROR: {e}")
    
    print(f"\nCompleted analysis of {len(analyses)} institutions")
    
    # Generate outputs
    matrix = generate_compliance_matrix(analyses)
    detailed = generate_detailed_report(analyses)
    
    # Save outputs
    matrix_path = OUTPUT_DIR / "pcaf_compliance_matrix.txt"
    detailed_path = OUTPUT_DIR / "pcaf_compliance_detailed.txt"
    csv_path = OUTPUT_DIR / "pcaf_compliance_data.csv"
    
    with open(matrix_path, 'w', encoding='utf-8') as f:
        f.write(matrix)
    print(f"Saved: {matrix_path}")
    
    with open(detailed_path, 'w', encoding='utf-8') as f:
        f.write(detailed)
    print(f"Saved: {detailed_path}")
    
    export_to_csv(analyses, csv_path)
    print(f"Saved: {csv_path}")
    
    # Print summary matrix to console
    print("\n" + matrix)
    
    return analyses


if __name__ == "__main__":
    main()
