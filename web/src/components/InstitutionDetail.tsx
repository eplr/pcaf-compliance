"use client";

import { useState } from "react";
import type { PartScore, CriterionScore, ComplianceRow } from "@/lib/data";
import {
  MATURITY_BG,
  MATURITY_LABELS,
  PART_NAMES,
  PART_TEXT_COLORS,
  PART_BORDER_COLORS,
  PART_BG_COLORS,
  PART_COLORS,
} from "@/lib/meta";

interface Props {
  partScores: PartScore[];
  criteria: CriterionScore[];
  compliance: ComplianceRow[];
}

const PART_ORDER = ["Part A", "Part B", "Part C"];

function ScoreBar({ pct, part }: { pct: number; part: string }) {
  const colorMap: Record<string, string> = {
    "Part A": "bg-blue-500",
    "Part B": "bg-orange-400",
    "Part C": "bg-purple-500",
  };
  return (
    <div className="flex items-center gap-2">
      <div className="flex-1 h-2 bg-slate-100 rounded-full overflow-hidden">
        <div
          className={`h-full rounded-full ${colorMap[part] ?? "bg-slate-400"}`}
          style={{ width: `${Math.min(pct, 100)}%` }}
        />
      </div>
      <span className="text-xs font-mono text-slate-600 w-10 text-right">
        {pct.toFixed(0)} %
      </span>
    </div>
  );
}

function CriteriaTable({
  criteria,
  part,
}: {
  criteria: CriterionScore[];
  part: string;
}) {
  const [showEvidence, setShowEvidence] = useState(false);

  const relevant = criteria.filter(
    (c) => c.pcaf_part === part && c.score !== null && c.max_score !== null
  );

  if (relevant.length === 0) return null;

  const priorityDot: Record<string, string> = {
    Critical: "bg-red-500",
    High:     "bg-amber-400",
    Medium:   "bg-yellow-300",
    Low:      "bg-green-400",
    "N/A":    "bg-slate-200",
    "—":      "bg-slate-200",
  };

  return (
    <div>
      <div className="flex items-center justify-between mb-2">
        <h4 className="text-sm font-semibold text-slate-700">Criteria breakdown</h4>
        <button
          onClick={() => setShowEvidence((v) => !v)}
          className="text-xs text-slate-500 hover:text-slate-800 underline underline-offset-2"
        >
          {showEvidence ? "Hide evidence" : "Show evidence"}
        </button>
      </div>
      <div className="overflow-x-auto">
        <table className="w-full text-sm border-collapse">
          <thead>
            <tr className="border-b border-slate-100">
              <th className="text-left py-2 pr-4 font-medium text-slate-500 text-xs w-44">
                Criterion
              </th>
              <th className="text-left py-2 pr-4 font-medium text-slate-500 text-xs w-24">
                Score
              </th>
              <th className="text-left py-2 font-medium text-slate-500 text-xs">
                Progress
              </th>
              {showEvidence && (
                <th className="text-left py-2 pl-4 font-medium text-slate-500 text-xs">
                  Evidence
                </th>
              )}
            </tr>
          </thead>
          <tbody>
            {relevant.map((c) => {
              const pct = c.percentage ?? 0;
              const dot = priorityDot[c.priority] ?? "bg-slate-300";
              return (
                <tr key={c.criterion} className="border-b border-slate-50 hover:bg-slate-50">
                  <td className="py-2 pr-4 font-medium text-slate-800 text-xs align-top">
                    <div className="flex items-start gap-1.5">
                      <span
                        className={`mt-0.5 w-2 h-2 rounded-full shrink-0 ${dot}`}
                        title={`Priority: ${c.priority}`}
                      />
                      {c.criterion}
                    </div>
                  </td>
                  <td className="py-2 pr-4 text-xs text-slate-600 font-mono align-top whitespace-nowrap">
                    {c.score} / {c.max_score}
                  </td>
                  <td className="py-2 align-top min-w-[120px]">
                    <ScoreBar pct={pct} part={part} />
                  </td>
                  {showEvidence && (
                    <td className="py-2 pl-4 text-xs text-slate-500 align-top max-w-xs">
                      {c.evidence || "—"}
                    </td>
                  )}
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
      {/* Priority legend */}
      <div className="flex gap-3 mt-3">
        {["Critical", "High", "Medium", "Low"].map((p) => (
          <div key={p} className="flex items-center gap-1 text-xs text-slate-500">
            <span className={`w-2 h-2 rounded-full ${priorityDot[p]}`} />
            {p}
          </div>
        ))}
      </div>
    </div>
  );
}

export default function InstitutionDetail({ partScores, criteria, compliance }: Props) {
  const presentParts = PART_ORDER.filter((part) =>
    partScores.some((p) => p.pcaf_part === part)
  );

  const [activeTab, setActiveTab] = useState(presentParts[0] ?? "Part A");

  const activePartScore = partScores.find((p) => p.pcaf_part === activeTab);
  const activeCompliance = compliance.find((c) => c.pcaf_part.startsWith(activeTab));

  return (
    <div>
      {/* ─── Part score cards row ─────────────────────────── */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-8">
        {PART_ORDER.map((part) => {
          const ps = partScores.find((p) => p.pcaf_part === part);
          const comp = compliance.find((c) => c.pcaf_part.startsWith(part));
          if (!ps) {
            return (
              <div
                key={part}
                className="rounded-xl border border-dashed border-slate-200 px-5 py-4 opacity-40"
              >
                <p className={`text-xs font-semibold uppercase tracking-wide mb-1 ${PART_TEXT_COLORS[part]}`}>
                  {part}
                </p>
                <p className="text-slate-400 text-sm">Not applicable</p>
              </div>
            );
          }
          const ml = ps.maturity_level;
          return (
            <div
              key={part}
              className={`rounded-xl border px-5 py-4 cursor-pointer transition-shadow hover:shadow-md ${
                activeTab === part
                  ? `${PART_BG_COLORS[part]} ${PART_BORDER_COLORS[part]} ring-2 ${PART_BORDER_COLORS[part]}`
                  : "bg-white border-slate-200"
              }`}
              onClick={() => setActiveTab(part)}
            >
              <p className={`text-xs font-semibold uppercase tracking-wide mb-1 ${PART_TEXT_COLORS[part]}`}>
                {part} — {PART_NAMES[part]}
              </p>
              <p className="text-3xl font-bold text-slate-900 mb-1">
                {ps.percentage.toFixed(1)}
                <span className="text-base font-normal text-slate-400"> %</span>
              </p>
              <p className="text-xs text-slate-500 mb-2">
                {ps.total_score} / {ps.max_score} pts
              </p>
              <ScoreBar pct={ps.percentage} part={part} />
              <div className="flex items-center gap-2 mt-2">
                <span
                  className={`px-2 py-0.5 rounded-full text-xs font-medium ${MATURITY_BG[ml] ?? ""}`}
                >
                  {MATURITY_LABELS[ml] ?? `Level ${ml}`}
                </span>
                {comp && (
                  <StatusBadge status={comp.status} />
                )}
              </div>
            </div>
          );
        })}
      </div>

      {/* ─── Criteria detail for selected part ──────────── */}
      {activePartScore && (
        <div className={`rounded-xl border ${PART_BORDER_COLORS[activeTab]} p-6`}>
          <div className="flex items-center gap-3 mb-5">
            <span
              className={`px-3 py-1 rounded-full text-xs font-bold text-white ${PART_COLORS[activeTab]}`}
            >
              {activeTab}
            </span>
            <h3 className="font-semibold text-slate-800">
              {PART_NAMES[activeTab]}
            </h3>
            {activeCompliance && (
              <span className="ml-auto text-xs text-slate-500">
                Completeness:{" "}
                <span className="font-semibold text-slate-700">
                  {activeCompliance.completeness_percent} %
                </span>
              </span>
            )}
          </div>

          <CriteriaTable criteria={criteria} part={activeTab} />

          {activeCompliance?.missing_elements &&
            activeCompliance.missing_elements !== "Minor gaps" &&
            activeCompliance.missing_elements !== "—" && (
              <div className="mt-4 p-3 bg-amber-50 border border-amber-200 rounded-lg text-xs text-amber-800">
                <span className="font-semibold">Gaps: </span>
                {activeCompliance.missing_elements}
              </div>
            )}
        </div>
      )}
    </div>
  );
}

function StatusBadge({ status }: { status: string }) {
  const map: Record<string, string> = {
    REPORTED: "bg-green-100 text-green-700",
    PARTIAL:  "bg-amber-100 text-amber-700",
    MISSING:  "bg-red-100 text-red-700",
  };
  return (
    <span className={`px-2 py-0.5 rounded-full text-xs font-medium ${map[status] ?? "bg-slate-100 text-slate-600"}`}>
      {status}
    </span>
  );
}
