#!/usr/bin/env python3
"""
PCAF Maturity Assessment - Looker Studio Export Script
Generates CSV files for PCAF maturity visualization in Google Looker Studio

Usage:
    python3 export_pcaf_maturity.py
"""

import pandas as pd
from datetime import datetime
import os

# Configuration
OUTPUT_DIR = '/Users/fidestra/Library/CloudStorage/OneDrive-fidestra/03_ACCOUNTS/Axylia/PCAF & banques/looker_data'

# Assessment data for Aviva PLC
assessment_data = {
    'company': 'Aviva PLC',
    'assessment_date': '2024-12-31',
    'institution_type': 'Insurance',
    
    # Part A: Financed Emissions (8 criteria, max 40 points)
    'part_a_scores': {
        'Asset Class Coverage': {
            'score': 3,
            'max': 5,
            'evidence': '5 of 10 PCAF asset classes reported (50%)',
            'priority': 'High',
            'gap_description': 'Missing: Motor vehicle loans, Use of proceeds, Securitized products, Sub-sovereign debt'
        },
        'Data Quality Score': {
            'score': 3,
            'max': 5,
            'evidence': 'Weighted average 2.5/5 (audited/primary data)',
            'priority': 'Medium',
            'gap_description': 'Good quality overall, opportunity to improve to <2.0'
        },
        'Attribution Methodology': {
            'score': 4,
            'max': 5,
            'evidence': 'PCAF-aligned attribution using share of investment',
            'priority': 'Low',
            'gap_description': 'Minor refinements possible with sector-specific enhancements'
        },
        'Scope Coverage': {
            'score': 3,
            'max': 5,
            'evidence': 'Scope 1 + 2 only, Scope 3 when methodology permits',
            'priority': 'Medium',
            'gap_description': 'Scope 3 investee emissions not yet included'
        },
        'Portfolio Coverage': {
            'score': 3,
            'max': 5,
            'evidence': '~85% coverage implied (not explicitly stated)',
            'priority': 'Medium',
            'gap_description': 'Coverage metric could be more explicit'
        },
        'Sovereign Debt Inclusion': {
            'score': 3,
            'max': 5,
            'evidence': 'Tracked separately with quality scores, excluded from total',
            'priority': 'High',
            'gap_description': 'Should be included in financed emissions total per PCAF'
        },
        'Temporal Coverage': {
            'score': 3,
            'max': 5,
            'evidence': '3 years of data reported (2022-2024)',
            'priority': 'Low',
            'gap_description': 'Good coverage, add projections/targets for Level 5'
        },
        'Intensity Metrics': {
            'score': 4,
            'max': 5,
            'evidence': 'ECI and asset-class specific intensities reported',
            'priority': 'Low',
            'gap_description': 'Strong performance, add benchmarking for Level 5'
        }
    },
    
    # Part B: Facilitated Emissions (2 criteria, max 10 points)
    'part_b_scores': {
        'Capital Markets Activity': {
            'score': 0,
            'max': 5,
            'evidence': 'Not applicable - Aviva is not an investment bank',
            'priority': 'N/A',
            'gap_description': 'N/A for insurance companies'
        },
        'Emission Attribution': {
            'score': 0,
            'max': 5,
            'evidence': 'Not applicable',
            'priority': 'N/A',
            'gap_description': 'N/A for insurance companies'
        }
    },
    
    # Part C: Insurance-Associated Emissions (8 criteria, max 40 points)
    'part_c_scores': {
        'Insurance Lines Coverage': {
            'score': 0,
            'max': 5,
            'evidence': 'No insurance-associated emissions reported',
            'priority': 'Critical',
            'gap_description': 'All 4 PCAF insurance lines missing'
        },
        'Commercial Lines': {
            'score': 0,
            'max': 5,
            'evidence': 'Commercial property & liability emissions not tracked',
            'priority': 'Critical',
            'gap_description': 'Most material line for insurers - immediate implementation needed'
        },
        'Motor Insurance': {
            'score': 0,
            'max': 5,
            'evidence': 'Personal & commercial motor emissions not tracked',
            'priority': 'Critical',
            'gap_description': 'Second priority - motor portfolio emissions missing'
        },
        'Project Insurance': {
            'score': 0,
            'max': 5,
            'evidence': 'Infrastructure/project emissions not tracked',
            'priority': 'High',
            'gap_description': 'Large project emissions not reported'
        },
        'Treaty Reinsurance': {
            'score': 0,
            'max': 5,
            'evidence': 'Reinsurance portfolio emissions not tracked',
            'priority': 'High',
            'gap_description': 'Reinsurance emissions gap'
        },
        'Attribution Methodology': {
            'score': 0,
            'max': 5,
            'evidence': 'No insurance-specific attribution methodology disclosed',
            'priority': 'Critical',
            'gap_description': 'Need PCAF insurance attribution (ITV method)'
        },
        'Underwriting Integration': {
            'score': 0,
            'max': 5,
            'evidence': 'Emissions data integration in underwriting not disclosed',
            'priority': 'High',
            'gap_description': 'No evidence of emissions in risk assessment'
        },
        'Data Quality': {
            'score': 0,
            'max': 5,
            'evidence': 'No insurance emissions data quality scores',
            'priority': 'Critical',
            'gap_description': 'No baseline data quality measurement'
        }
    }
}


def export_for_looker(data, output_dir):
    """Export PCAF maturity assessment data for Looker Studio"""
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    print("="*70)
    print("PCAF MATURITY ASSESSMENT - LOOKER STUDIO EXPORT")
    print("="*70)
    print(f"\nCompany: {data['company']}")
    print(f"Assessment Date: {data['assessment_date']}")
    print(f"Institution Type: {data['institution_type']}")
    print(f"Output Directory: {output_dir}\n")
    
    # TABLE 1: Detailed Criterion Scores
    detailed_scores = []
    
    for part, part_name in [('part_a_scores', 'Part A'), 
                             ('part_b_scores', 'Part B'), 
                             ('part_c_scores', 'Part C')]:
        for criterion_name, criterion_data in data[part].items():
            detailed_scores.append({
                'company': data['company'],
                'assessment_date': data['assessment_date'],
                'institution_type': data['institution_type'],
                'pcaf_part': part_name,
                'criterion': criterion_name,
                'score': criterion_data['score'],
                'max_score': criterion_data['max'],
                'percentage': (criterion_data['score'] / criterion_data['max']) * 100,
                'evidence': criterion_data['evidence'],
                'priority': criterion_data['priority'],
                'gap_description': criterion_data['gap_description']
            })
    
    df_detailed = pd.DataFrame(detailed_scores)
    detailed_path = f'{output_dir}/pcaf_assessment_detailed.csv'
    df_detailed.to_csv(detailed_path, index=False)
    print(f"✓ Exported: pcaf_assessment_detailed.csv ({len(df_detailed)} rows)")
    
    # TABLE 2: Part Summaries
    part_a_total = sum(c['score'] for c in data['part_a_scores'].values())
    part_a_max = sum(c['max'] for c in data['part_a_scores'].values())
    
    part_b_total = sum(c['score'] for c in data['part_b_scores'].values())
    part_b_max = sum(c['max'] for c in data['part_b_scores'].values())
    
    part_c_total = sum(c['score'] for c in data['part_c_scores'].values())
    part_c_max = sum(c['max'] for c in data['part_c_scores'].values())
    
    part_summaries = [
        {
            'company': data['company'],
            'assessment_date': data['assessment_date'],
            'institution_type': data['institution_type'],
            'pcaf_part': 'Part A',
            'part_name': 'Financed Emissions',
            'total_score': part_a_total,
            'max_score': part_a_max,
            'percentage': (part_a_total / part_a_max) * 100,
            'maturity_level': part_a_total // 8,
            'maturity_label': get_maturity_label(part_a_total, part_a_max)
        },
        {
            'company': data['company'],
            'assessment_date': data['assessment_date'],
            'institution_type': data['institution_type'],
            'pcaf_part': 'Part B',
            'part_name': 'Facilitated Emissions',
            'total_score': part_b_total,
            'max_score': part_b_max,
            'percentage': 0.0 if part_b_max == 0 else (part_b_total / part_b_max) * 100,
            'maturity_level': 0,
            'maturity_label': 'N/A'
        },
        {
            'company': data['company'],
            'assessment_date': data['assessment_date'],
            'institution_type': data['institution_type'],
            'pcaf_part': 'Part C',
            'part_name': 'Insurance Emissions',
            'total_score': part_c_total,
            'max_score': part_c_max,
            'percentage': (part_c_total / part_c_max) * 100,
            'maturity_level': part_c_total // 8,
            'maturity_label': get_maturity_label(part_c_total, part_c_max)
        }
    ]
    
    df_parts = pd.DataFrame(part_summaries)
    parts_path = f'{output_dir}/pcaf_assessment_parts.csv'
    df_parts.to_csv(parts_path, index=False)
    print(f"✓ Exported: pcaf_assessment_parts.csv ({len(df_parts)} rows)")
    
    # TABLE 3: Overall Summary
    # For insurers: weighted 50% Part A, 50% Part C
    if data['institution_type'] == 'Insurance':
        weighted_score = ((part_a_total / part_a_max) * 50 + 
                          (part_c_total / part_c_max) * 50)
    elif data['institution_type'] == 'Bank':
        weighted_score = ((part_a_total / part_a_max) * 70 + 
                          (part_b_total / part_b_max) * 30)
    else:  # Asset Manager
        weighted_score = (part_a_total / part_a_max) * 100
    
    overall = [{
        'company': data['company'],
        'assessment_date': data['assessment_date'],
        'institution_type': data['institution_type'],
        'weighted_score': weighted_score,
        'maturity_level': int(weighted_score // 20),
        'maturity_label': get_overall_maturity_label(weighted_score),
        'part_a_score': (part_a_total / part_a_max) * 100,
        'part_b_score': 0.0 if part_b_max == 0 else (part_b_total / part_b_max) * 100,
        'part_c_score': (part_c_total / part_c_max) * 100,
        'part_a_points': f"{part_a_total}/{part_a_max}",
        'part_b_points': f"{part_b_total}/{part_b_max}",
        'part_c_points': f"{part_c_total}/{part_c_max}"
    }]
    
    df_overall = pd.DataFrame(overall)
    overall_path = f'{output_dir}/pcaf_assessment_overall.csv'
    df_overall.to_csv(overall_path, index=False)
    print(f"✓ Exported: pcaf_assessment_overall.csv ({len(df_overall)} rows)")
    
    # SUMMARY STATISTICS
    print("\n" + "="*70)
    print("ASSESSMENT SUMMARY")
    print("="*70)
    print(f"\nPart A (Financed):       {part_a_total}/{part_a_max} ({part_a_total/part_a_max*100:.1f}%) - {get_maturity_label(part_a_total, part_a_max)}")
    print(f"Part B (Facilitated):    N/A (Not applicable to insurers)")
    print(f"Part C (Insurance):      {part_c_total}/{part_c_max} ({part_c_total/part_c_max*100:.1f}%) - {get_maturity_label(part_c_total, part_c_max)}")
    print(f"\nWeighted Overall:        {weighted_score:.1f}% - {get_overall_maturity_label(weighted_score)}")
    print(f"Maturity Level:          Level {int(weighted_score // 20)}/5")
    
    print("\n" + "="*70)
    print("FILES READY FOR LOOKER STUDIO")
    print("="*70)
    print(f"\n1. {detailed_path}")
    print(f"2. {parts_path}")
    print(f"3. {overall_path}")
    print("\nNext steps:")
    print("  1. Upload these CSV files to Google Sheets")
    print("  2. Connect Google Sheets to Looker Studio")
    print("  3. Build dashboards using the data")
    print("\nSee: PCAF_Maturity_Assessment_Guide.md for detailed instructions")
    print("\n" + "="*70)
    
    return df_detailed, df_parts, df_overall


def get_maturity_label(score, max_score):
    """Convert score to maturity label"""
    percentage = (score / max_score) * 100
    if percentage >= 80:
        return "Advanced"
    elif percentage >= 60:
        return "Defined"
    elif percentage >= 40:
        return "Developing"
    elif percentage >= 20:
        return "Initial"
    else:
        return "Not Started"


def get_overall_maturity_label(percentage):
    """Convert weighted percentage to overall maturity label"""
    if percentage >= 80:
        return "Level 4-5: Advanced/Leading"
    elif percentage >= 60:
        return "Level 3-4: Defined/Advanced"
    elif percentage >= 40:
        return "Level 2-3: Developing/Defined"
    elif percentage >= 20:
        return "Level 1-2: Initial/Developing"
    else:
        return "Level 0-1: Not Started/Initial"


if __name__ == "__main__":
    # Run export
    export_for_looker(assessment_data, OUTPUT_DIR)
