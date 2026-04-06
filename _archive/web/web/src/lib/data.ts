import fs from "fs";
import path from "path";

// ─── Types ────────────────────────────────────────────────────────────────────

export interface InstitutionOverall {
  company: string;
  slug: string;
  assessment_date: string;
  institution_type: string;
  weighted_score: number;
  maturity_level: number;
  maturity_label: string;
  part_a_score: number | null;
  part_b_score: number | null;
  part_c_score: number | null;
}

export interface PartScore {
  company: string;
  pcaf_part: string;
  part_name: string;
  total_score: number;
  max_score: number;
  percentage: number;
  maturity_level: number;
}

export interface CriterionScore {
  company: string;
  institution_type: string;
  pcaf_part: string;
  criterion: string;
  score: number | null;
  max_score: number | null;
  percentage: number | null;
  evidence: string;
  priority: string;
  gap_description: string;
  assessor_notes: string;
}

export interface ComplianceRow {
  company: string;
  pcaf_part: string;
  status: string;
  completeness_percent: number;
  missing_elements: string;
  priority: string;
}

// ─── CSV parser ───────────────────────────────────────────────────────────────

function parseCSVLine(line: string): string[] {
  const result: string[] = [];
  let current = "";
  let inQuotes = false;
  for (let i = 0; i < line.length; i++) {
    const c = line[i];
    if (c === '"') {
      inQuotes = !inQuotes;
    } else if (c === "," && !inQuotes) {
      result.push(current.trim());
      current = "";
    } else {
      current += c;
    }
  }
  result.push(current.trim());
  return result;
}

function parseCSV(filename: string): Record<string, string>[] {
  const filePath = path.join(process.cwd(), "src", "data", filename);
  const content = fs.readFileSync(filePath, "utf-8");
  const lines = content
    .split("\n")
    .map((l) => l.replace(/\r$/, ""))
    .filter((l) => l.trim() !== "");
  if (lines.length < 2) return [];
  const headers = parseCSVLine(lines[0]);
  return lines.slice(1).map((line) => {
    const values = parseCSVLine(line);
    return Object.fromEntries(headers.map((h, i) => [h, values[i] ?? ""]));
  });
}

function num(v: string): number {
  const n = parseFloat(v);
  return isNaN(n) ? 0 : n;
}

function numOrNull(v: string): number | null {
  if (!v || v === "N/A" || v === "null") return null;
  const n = parseFloat(v);
  return isNaN(n) ? null : n;
}

// ─── Slug helper ──────────────────────────────────────────────────────────────

export function toSlug(name: string): string {
  return name
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");
}

// ─── Loaders ──────────────────────────────────────────────────────────────────

export function loadOverall(): InstitutionOverall[] {
  return parseCSV("pcaf_assessment_overall.csv").map((r) => ({
    company: r.company,
    slug: toSlug(r.company),
    assessment_date: r.assessment_date,
    institution_type: r.institution_type,
    weighted_score: num(r.weighted_score),
    maturity_level: num(r.maturity_level),
    maturity_label: r.maturity_label,
    part_a_score: numOrNull(r.part_a_score),
    part_b_score: numOrNull(r.part_b_score),
    part_c_score: numOrNull(r.part_c_score),
  }));
}

export function loadParts(): PartScore[] {
  return parseCSV("pcaf_assessment_parts.csv").map((r) => ({
    company: r.company,
    pcaf_part: r.pcaf_part,
    part_name: r.part_name,
    total_score: num(r.total_score),
    max_score: num(r.max_score),
    percentage: num(r.percentage),
    maturity_level: num(r.maturity_level),
  }));
}

export function loadDetailed(): CriterionScore[] {
  return parseCSV("pcaf_assessment_detailed.csv")
    .filter((r) => r.score !== "N/A")
    .map((r) => ({
      company: r.company,
      institution_type: r.institution_type,
      pcaf_part: r.pcaf_part,
      criterion: r.criterion,
      score: numOrNull(r.score),
      max_score: numOrNull(r.max_score),
      percentage: numOrNull(r.percentage),
      evidence: r.evidence,
      priority: r.priority,
      gap_description: r.gap_description,
      assessor_notes: r.assessor_notes,
    }));
}

export function loadCompliance(): ComplianceRow[] {
  return parseCSV("pcaf_compliance.csv").map((r) => ({
    company: r.company,
    pcaf_part: r.pcaf_part,
    status: r.status,
    completeness_percent: num(r.completeness_percent),
    missing_elements: r.missing_elements,
    priority: r.priority,
  }));
}
