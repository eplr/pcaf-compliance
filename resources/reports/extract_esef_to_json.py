#!/usr/bin/env python3
"""
Extract text and XBRL-tagged facts from an ESEF iXBRL report (.xhtml) into JSON.

Produces two files:
  1. <company>_<year>.json  — pipeline-compatible text+metadata (same format as TextExtractor)
  2. <company>_<year>_xbrl_facts.json — structured XBRL-tagged financial facts

Usage:
    python3 extract_esef_to_json.py <input.xhtml> [output_dir]
"""
import json
import os
import re
import sys
from lxml import etree

# Namespaces used in ESEF iXBRL reports
NS = {
    "xhtml": "http://www.w3.org/1999/xhtml",
    "ix": "http://www.xbrl.org/2013/inlineXBRL",
    "xbrli": "http://www.xbrl.org/2003/instance",
    "link": "http://www.xbrl.org/2003/linkbase",
}

# Chunk size for pseudo-page segmentation (characters)
PAGE_CHUNK_SIZE = 4000


def parse_xhtml(path):
    """Parse the iXBRL XHTML file with lxml (as XML to preserve namespaces)."""
    print(f"Parsing {path} ({os.path.getsize(path) / 1e6:.1f} MB)...")
    parser = etree.XMLParser(encoding="utf-8", recover=True, huge_tree=True)
    tree = etree.parse(path, parser)
    return tree


def extract_xbrl_contexts(tree):
    """Extract context definitions (period, entity) from ix:header."""
    contexts = {}
    for ctx in tree.iter("{http://www.xbrl.org/2003/instance}context"):
        ctx_id = ctx.get("id", "")
        period_el = ctx.find("{http://www.xbrl.org/2003/instance}period")
        period = {}
        if period_el is not None:
            instant = period_el.find("{http://www.xbrl.org/2003/instance}instant")
            start = period_el.find("{http://www.xbrl.org/2003/instance}startDate")
            end = period_el.find("{http://www.xbrl.org/2003/instance}endDate")
            if instant is not None:
                period["instant"] = instant.text
            if start is not None and end is not None:
                period["startDate"] = start.text
                period["endDate"] = end.text
        # Extract dimensional info if present
        scenario = ctx.find("{http://www.xbrl.org/2003/instance}scenario")
        dimensions = []
        if scenario is not None:
            for member in scenario.iter("{http://xbrl.org/2006/xbrldi}explicitMember"):
                dimensions.append({
                    "dimension": member.get("dimension", ""),
                    "member": member.text.strip() if member.text else "",
                })
        contexts[ctx_id] = {"period": period, "dimensions": dimensions}
    return contexts


def extract_xbrl_units(tree):
    """Extract unit definitions from ix:header."""
    units = {}
    for unit in tree.iter("{http://www.xbrl.org/2003/instance}unit"):
        unit_id = unit.get("id", "")
        measure = unit.find("{http://www.xbrl.org/2003/instance}measure")
        if measure is not None and measure.text:
            units[unit_id] = measure.text.strip()
        else:
            # Handle divide (e.g., per-share units)
            divide = unit.find("{http://www.xbrl.org/2003/instance}divide")
            if divide is not None:
                num = divide.find(
                    "{http://www.xbrl.org/2003/instance}unitNumerator/"
                    "{http://www.xbrl.org/2003/instance}measure"
                )
                den = divide.find(
                    "{http://www.xbrl.org/2003/instance}unitDenominator/"
                    "{http://www.xbrl.org/2003/instance}measure"
                )
                num_t = num.text.strip() if num is not None and num.text else "?"
                den_t = den.text.strip() if den is not None and den.text else "?"
                units[unit_id] = f"{num_t}/{den_t}"
    return units


def extract_xbrl_facts(tree, contexts, units):
    """
    Extract all ix:nonFraction and ix:nonNumeric tagged facts.
    Returns a list of structured fact dicts.
    """
    facts = []

    # nonFraction — numeric facts
    for el in tree.iter("{http://www.xbrl.org/2013/inlineXBRL}nonFraction"):
        fact = _parse_fact_element(el, contexts, units, fact_type="numeric")
        if fact:
            facts.append(fact)

    # nonNumeric — text/enum facts
    for el in tree.iter("{http://www.xbrl.org/2013/inlineXBRL}nonNumeric"):
        fact = _parse_fact_element(el, contexts, units, fact_type="text")
        if fact:
            facts.append(fact)

    return facts


def _parse_fact_element(el, contexts, units, fact_type):
    """Parse a single ix: element into a structured dict."""
    name = el.get("name", "")
    ctx_ref = el.get("contextRef", "")
    unit_ref = el.get("unitRef", "")
    decimals = el.get("decimals", "")
    scale = el.get("scale", "")
    fact_id = el.get("id", "")
    fmt = el.get("format", "")

    # Get the displayed text value
    text_val = "".join(el.itertext()).strip()

    fact = {
        "id": fact_id,
        "name": name,
        "type": fact_type,
        "displayed_value": text_val,
        "context_ref": ctx_ref,
    }

    # Add numeric-specific fields
    if fact_type == "numeric":
        fact["unit_ref"] = unit_ref
        fact["unit"] = units.get(unit_ref, "")
        fact["decimals"] = decimals
        fact["scale"] = scale
        fact["format"] = fmt
        # Compute the actual numeric value if possible
        fact["resolved_value"] = _resolve_numeric(text_val, scale, fmt)

    # Add context info
    ctx = contexts.get(ctx_ref, {})
    fact["period"] = ctx.get("period", {})
    fact["dimensions"] = ctx.get("dimensions", [])

    return fact


def _resolve_numeric(text_val, scale, fmt):
    """Attempt to resolve the displayed value to a numeric value using scale."""
    try:
        # Remove formatting (spaces, commas as thousands separators)
        cleaned = text_val.replace("\u00a0", "").replace(" ", "")
        # Handle comma as thousands separator (common in ESEF)
        if "num-dot-decimal" in fmt:
            cleaned = cleaned.replace(",", "")
        elif "num-comma-decimal" in fmt:
            cleaned = cleaned.replace(".", "").replace(",", ".")
        else:
            # Default: try removing commas
            cleaned = cleaned.replace(",", "")
        # Remove parentheses (negative values)
        negative = False
        if cleaned.startswith("(") and cleaned.endswith(")"):
            cleaned = cleaned[1:-1]
            negative = True
        if cleaned.startswith("-"):
            cleaned = cleaned[1:]
            negative = True
        val = float(cleaned)
        if negative:
            val = -val
        # Apply scale
        if scale:
            val *= 10 ** int(scale)
        return val
    except (ValueError, TypeError):
        return None


# Block-level elements that should get a line break before/after
_XHTML_NS = "{http://www.w3.org/1999/xhtml}"
_BLOCK_TAGS = {
    f"{_XHTML_NS}{t}" for t in (
        "div", "p", "h1", "h2", "h3", "h4", "h5", "h6",
        "table", "tr", "li", "blockquote", "section", "article",
        "header", "footer", "nav", "main", "aside", "figure",
    )
} | {
    # Also match without namespace (fallback)
    "div", "p", "h1", "h2", "h3", "h4", "h5", "h6",
    "table", "tr", "li", "blockquote", "section",
}
_SKIP_TAGS = {
    "style", "script",
    f"{_XHTML_NS}style", f"{_XHTML_NS}script",
    "{http://www.xbrl.org/2013/inlineXBRL}header",
}
_CELL_TAGS = {f"{_XHTML_NS}td", f"{_XHTML_NS}th", "td", "th"}
_BR_TAGS = {f"{_XHTML_NS}br", "br"}


def extract_body_text(tree):
    """
    Extract readable text from the HTML body, inserting line breaks
    at block-level element boundaries and tabs between table cells.
    """
    body = tree.find(".//{http://www.w3.org/1999/xhtml}body")
    if body is None:
        body = tree.find(".//body")
    if body is None:
        body = tree.getroot()

    parts = []
    _walk(body, parts)
    raw_text = "".join(parts)

    # Clean up
    text = re.sub(r"[^\S\n]+", " ", raw_text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    lines = [line.strip() for line in text.split("\n")]
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _walk(el, parts):
    """Recursively walk the element tree, inserting breaks at block boundaries."""
    tag = el.tag if isinstance(el.tag, str) else ""

    # Skip style/script/ix:header
    if tag in _SKIP_TAGS:
        return

    is_block = tag in _BLOCK_TAGS
    is_cell = tag in _CELL_TAGS
    is_br = tag in _BR_TAGS

    if is_block:
        parts.append("\n")
    elif is_cell:
        parts.append("\t")
    elif is_br:
        parts.append("\n")

    # Add element's own text
    if el.text:
        parts.append(el.text)

    # Recurse into children
    for child in el:
        _walk(child, parts)
        # Add tail text (text after child's closing tag)
        if child.tail:
            parts.append(child.tail)

    if is_block:
        parts.append("\n")


def segment_into_pages(text, chunk_size=PAGE_CHUNK_SIZE):
    """
    Segment text into pseudo-pages by splitting on newlines,
    grouping into chunks of approximately `chunk_size` characters.
    """
    # Split on any line break to get individual lines/paragraphs
    lines = text.split("\n")
    pages = []
    current_page = []
    current_length = 0

    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            # Keep empty lines for readability but don't count towards length
            if current_page:
                current_page.append("")
            continue
        if current_length + len(line_stripped) > chunk_size and current_page:
            pages.append("\n".join(current_page).strip())
            current_page = [line_stripped]
            current_length = len(line_stripped)
        else:
            current_page.append(line_stripped)
            current_length += len(line_stripped)

    if current_page:
        page_text = "\n".join(current_page).strip()
        if page_text:
            pages.append(page_text)

    return pages


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(input_path)

    # Derive output names (ING_2025 convention)
    basename = os.path.basename(input_path).replace(".xhtml", "")
    company = "ING"
    year = "2025"

    # Parse
    tree = parse_xhtml(input_path)

    # 1. Extract XBRL contexts, units, and facts
    print("Extracting XBRL contexts and units...")
    contexts = extract_xbrl_contexts(tree)
    units = extract_xbrl_units(tree)
    print(f"  Found {len(contexts)} contexts, {len(units)} units")

    print("Extracting XBRL-tagged facts...")
    facts = extract_xbrl_facts(tree, contexts, units)
    print(f"  Found {len(facts)} tagged facts")

    # 2. Extract body text
    print("Extracting body text (this may take a moment for 121 MB)...")
    text = extract_body_text(tree)
    print(f"  Extracted {len(text):,} characters of text")

    # 3. Segment into pseudo-pages
    pages = segment_into_pages(text)
    print(f"  Segmented into {len(pages)} pseudo-pages")

    # 4. Build pipeline-compatible JSON (TextExtractor format)
    all_text = ""
    metadata = []
    source_doc = os.path.basename(input_path)
    for i, page_text in enumerate(pages, 1):
        all_text += page_text + " "
        metadata.append({
            "source_document": source_doc,
            "page_number": i,
            "text_length": len(page_text),
        })

    pipeline_output = {"text": all_text.strip(), "metadata": metadata}

    # 5. Build XBRL facts JSON
    xbrl_output = {
        "source": source_doc,
        "company": company,
        "year": year,
        "contexts_count": len(contexts),
        "units": units,
        "facts": facts,
    }

    # Write outputs
    os.makedirs(output_dir, exist_ok=True)

    pipeline_path = os.path.join(output_dir, f"{company}_{year}.json")
    with open(pipeline_path, "w", encoding="utf-8") as f:
        json.dump(pipeline_output, f, ensure_ascii=False)
    print(f"\nPipeline-compatible text+metadata: {pipeline_path}")
    print(f"  Size: {os.path.getsize(pipeline_path) / 1e6:.1f} MB")

    facts_path = os.path.join(output_dir, f"{company}_{year}_xbrl_facts.json")
    with open(facts_path, "w", encoding="utf-8") as f:
        json.dump(xbrl_output, f, ensure_ascii=False, indent=2)
    print(f"XBRL facts: {facts_path}")
    print(f"  Size: {os.path.getsize(facts_path) / 1e3:.1f} KB")

    # Print summary of facts
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Total text: {len(all_text):,} characters")
    print(f"Pages: {len(pages)}")
    print(f"XBRL facts: {len(facts)} ({sum(1 for f in facts if f['type']=='numeric')} numeric, "
          f"{sum(1 for f in facts if f['type']=='text')} text)")

    # Show a few sample facts
    numeric_facts = [f for f in facts if f["type"] == "numeric"]
    if numeric_facts:
        print(f"\nSample numeric facts:")
        for f in numeric_facts[:5]:
            period_str = f["period"].get("instant", f["period"].get("endDate", "?"))
            print(f"  {f['name']}: {f['displayed_value']} "
                  f"(resolved: {f['resolved_value']}) [{f['unit']}] @ {period_str}")

    text_facts = [f for f in facts if f["type"] == "text"]
    if text_facts:
        print(f"\nSample text facts:")
        for f in text_facts[:3]:
            display = f["displayed_value"][:100] + "..." if len(f["displayed_value"]) > 100 else f["displayed_value"]
            print(f"  {f['name']}: {display}")


if __name__ == "__main__":
    main()
