#!/usr/bin/env python3
"""
Prepare PDF reports for the corporate-sustainability-tracker pipeline.
Renames files to the required format: {company_id}_{year}_{report_type}.pdf
"""

import os
import shutil
import re

# Configuration
SOURCE_DIR = "/Users/fidestra/Library/CloudStorage/OneDrive-fidestra/03_ACCOUNTS/Axylia/pcaf-compliance/reports"
TARGET_DIR = "/Users/fidestra/corporate-sustainability-tracker/data/raw/reports_pdf"

# Mapping: original filename -> (company_id, year, report_type)
# company_id uses a simple slug format for readability
PDF_MAPPING = {
    "AMUNDI_DEU_2024.pdf": ("AMUNDI", "2024", "AR"),
    "Admiral 2024 2024 Sustainability Report.pdf": ("ADMIRAL", "2024", "SR"),
    "Ageas-AR-FR-24.pdf": ("AGEAS", "2024", "AR"),
    "Commerzbank_Group_Annual_Report_2024.pdf": ("COMMERZBANK", "2024", "AR"),
    "DBG-annual-report-2024.pdf": ("DEUTSCHEBOERSE", "2024", "AR"),
    "DEU_2024_CREDIT_AGRICOLE.pdf": ("CREDITAGRICOLE", "2024", "AR"),
    "EZO2024_DEU_FR_MEL.pdf": ("EURAZEO", "2024", "AR"),
    "GBL_RA2024_ESG_FR.pdf": ("GBL", "2024", "SR"),
    "KBC-csr-sr-2024.pdf": ("KBC", "2024", "SR"),
    "SG-document-enregistrement-universel-2025.pdf": ("SOCGEN", "2024", "AR"),
    "Santander-2024-consolidated-annual-financial-report-en.pdf": ("SANTANDER", "2024", "AR"),
    "Schroders - Annual Report FY24 Full Report.pdf": ("SCHRODERS", "2024", "AR"),
    "Swiss-Re-2024-sustainability-report-en.pdf": ("SWISSRE", "2024", "SR"),
    "UniCredit-2024-Annual-Reports-and-Accounts.pdf": ("UNICREDIT", "2024", "AR"),
    "Zurich-Insurance-annual-report-2024-en.pdf": ("ZURICH", "2024", "AR"),
    "annual-report-nordea-bank-abp-2024-0.pdf": ("NORDEA", "2024", "AR"),
    "asr-nederland_2024.pdf": ("ASRNEDERLAND", "2024", "AR"),
    "aviva-plc-climate-related-financial-disclosure-2024 (2).pdf": ("AVIVA", "2024", "SR"),
    "axa_urd2024.pdf": ("AXA", "2024", "AR"),
    "en-allianz-group-annual-report-2024.pdf": ("ALLIANZ", "2024", "AR"),
    "legal-and-general-climate-and-nature-report-2024.pdf": ("LEGALGENERAL", "2024", "SR"),
    "nn-group-annual-report-2024.pdf": ("NNGROUP", "2024", "AR"),
    "phoenix_group_annual_report_2024_spread.pdf": ("PHOENIXGROUP", "2024", "AR"),
}


def prepare_pdfs(dry_run=True):
    """
    Rename and copy PDFs to the target directory.
    
    Args:
        dry_run: If True, only print what would be done without copying.
    """
    # Create target directory if it doesn't exist
    if not dry_run:
        os.makedirs(TARGET_DIR, exist_ok=True)
    
    print(f"{'DRY RUN - ' if dry_run else ''}Preparing PDFs for corporate-sustainability-tracker\n")
    print(f"Source: {SOURCE_DIR}")
    print(f"Target: {TARGET_DIR}\n")
    print("-" * 80)
    
    for original_name, (company_id, year, report_type) in PDF_MAPPING.items():
        source_path = os.path.join(SOURCE_DIR, original_name)
        new_name = f"{company_id}_{year}_{report_type}.pdf"
        target_path = os.path.join(TARGET_DIR, new_name)
        
        if not os.path.exists(source_path):
            print(f"WARNING: Source file not found: {original_name}")
            continue
        
        print(f"{original_name}")
        print(f"  -> {new_name}")
        
        if not dry_run:
            shutil.copy2(source_path, target_path)
            print(f"  [COPIED]")
        print()
    
    print("-" * 80)
    if dry_run:
        print("\nThis was a DRY RUN. To actually copy files, run:")
        print("  python prepare_pdfs.py --execute")
    else:
        print(f"\nDone! {len(PDF_MAPPING)} files copied to {TARGET_DIR}")
        print("\nNext steps:")
        print("  1. cd /Users/fidestra/corporate-sustainability-tracker")
        print("  2. python corporate_sustainability_tracker/main.py")


if __name__ == "__main__":
    import sys
    dry_run = "--execute" not in sys.argv
    prepare_pdfs(dry_run=dry_run)
