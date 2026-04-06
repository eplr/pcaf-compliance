"use client";

import { useState, useCallback } from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Cell,
  ResponsiveContainer,
  ReferenceLine,
} from "recharts";
import type { InstitutionOverall } from "@/lib/data";
import { MATURITY_COLORS, MATURITY_LABELS, MATURITY_BG } from "@/lib/meta";

interface Props {
  institutions: InstitutionOverall[];
  metaMap: Record<string, { country: string; flag: string; signatory: boolean }>;
}

const FILTERS = [
  { key: "All",              label: "All" },
  { key: "Bank",             label: "Banks" },
  { key: "Insurance",        label: "Insurance" },
  { key: "Asset Manager",    label: "Asset Managers" },
  { key: "Other",            label: "Other" },
];

const TYPE_GROUPS: Record<string, string[]> = {
  Bank:          ["Bank"],
  Insurance:     ["Insurance", "Reinsurance"],
  "Asset Manager": ["Asset Manager"],
  Other:         ["Bancassurance", "Exchange", "Investment Holding"],
};

// Custom tooltip shown on hover
function CustomTooltip({
  active,
  payload,
}: {
  active?: boolean;
  payload?: Array<{ payload: InstitutionOverall & { flag: string; signatory: boolean } }>;
}) {
  if (!active || !payload?.length) return null;
  const d = payload[0].payload;
  const ml = d.maturity_level;
  return (
    <div className="bg-white border border-slate-200 rounded-lg shadow-lg p-3 text-sm max-w-xs">
      <p className="font-semibold text-slate-900 mb-1">
        {d.flag} {d.company}
      </p>
      <p className="text-slate-500 mb-2">{d.institution_type}</p>
      <p className="text-2xl font-bold text-slate-900">
        {d.weighted_score.toFixed(1)}
        <span className="text-sm font-normal text-slate-500"> / 100</span>
      </p>
      <span
        className={`inline-block mt-1 px-2 py-0.5 rounded-full text-xs font-medium ${MATURITY_BG[ml] ?? ""}`}
      >
        {MATURITY_LABELS[ml] ?? d.maturity_label}
      </span>
      <div className="mt-2 space-y-0.5 text-xs text-slate-600">
        {d.part_a_score != null && (
          <div className="flex justify-between gap-4">
            <span className="text-blue-600 font-medium">Part A</span>
            <span>{d.part_a_score.toFixed(1)} %</span>
          </div>
        )}
        {d.part_b_score != null && (
          <div className="flex justify-between gap-4">
            <span className="text-orange-500 font-medium">Part B</span>
            <span>{d.part_b_score.toFixed(1)} %</span>
          </div>
        )}
        {d.part_c_score != null && (
          <div className="flex justify-between gap-4">
            <span className="text-purple-600 font-medium">Part C</span>
            <span>{d.part_c_score.toFixed(1)} %</span>
          </div>
        )}
      </div>
      {d.signatory && (
        <p className="mt-2 text-xs text-emerald-600 font-medium">✓ PCAF Signatory</p>
      )}
      <p className="mt-1 text-xs text-slate-400">Click to view details →</p>
    </div>
  );
}

export default function BenchmarkClient({ institutions, metaMap }: Props) {
  const [activeFilter, setActiveFilter] = useState("All");

  const filtered = institutions.filter((inst) => {
    if (activeFilter === "All") return true;
    const group = TYPE_GROUPS[activeFilter] ?? [];
    return group.includes(inst.institution_type);
  });

  // Sort ascending (bottom = lowest) for horizontal bar readability
  const sorted = [...filtered].sort((a, b) => a.weighted_score - b.weighted_score);

  const chartData = sorted.map((inst) => ({
    ...inst,
    flag: metaMap[inst.company]?.flag ?? "🏦",
    signatory: metaMap[inst.company]?.signatory ?? false,
  }));

  const handleBarClick = useCallback(
    (data: { activePayload?: Array<{ payload: { slug: string } }> }) => {
      const slug = data?.activePayload?.[0]?.payload?.slug;
      if (slug) window.location.href = `/institution/${slug}`;
    },
    []
  );

  const chartHeight = Math.max(400, sorted.length * 40);

  return (
    <div>
      {/* ─── Filter tabs ─────────────────────────────────── */}
      <div className="flex flex-wrap gap-2 mb-6">
        {FILTERS.map((f) => (
          <button
            key={f.key}
            onClick={() => setActiveFilter(f.key)}
            className={`px-4 py-1.5 rounded-full text-sm font-medium transition-colors ${
              activeFilter === f.key
                ? "bg-slate-800 text-white"
                : "bg-white border border-slate-200 text-slate-600 hover:bg-slate-50"
            }`}
          >
            {f.label}
            {f.key !== "All" && (
              <span className="ml-1.5 text-xs opacity-60">
                (
                {institutions.filter((i) =>
                  (TYPE_GROUPS[f.key] ?? []).includes(i.institution_type)
                ).length}
                )
              </span>
            )}
          </button>
        ))}
      </div>

      {/* ─── Maturity legend ─────────────────────────────── */}
      <div className="flex flex-wrap gap-3 mb-4">
        {Object.entries(MATURITY_LABELS).map(([level, label]) => (
          <div key={level} className="flex items-center gap-1.5 text-xs text-slate-600">
            <span
              className="w-3 h-3 rounded-sm inline-block"
              style={{ background: MATURITY_COLORS[Number(level)] }}
            />
            {label}
          </div>
        ))}
      </div>

      {/* ─── Chart ───────────────────────────────────────── */}
      <div className="bg-white rounded-xl border border-slate-200 p-4">
        <ResponsiveContainer width="100%" height={chartHeight}>
          <BarChart
            data={chartData}
            layout="vertical"
            margin={{ top: 4, right: 60, left: 140, bottom: 4 }}
            onClick={handleBarClick}
            style={{ cursor: "pointer" }}
          >
            <CartesianGrid horizontal={false} strokeDasharray="3 3" stroke="#e2e8f0" />
            <XAxis
              type="number"
              domain={[0, 100]}
              tickFormatter={(v) => `${v}`}
              tick={{ fontSize: 11, fill: "#64748b" }}
              tickLine={false}
              axisLine={false}
              label={{
                value: "Weighted score (%)",
                position: "insideBottom",
                offset: -2,
                fontSize: 11,
                fill: "#94a3b8",
              }}
            />
            <YAxis
              type="category"
              dataKey="company"
              tick={({ x, y, payload }) => {
                const inst = chartData.find((d) => d.company === payload.value);
                return (
                  <g>
                    <text
                      x={x - 4}
                      y={y + 4}
                      textAnchor="end"
                      fontSize={11.5}
                      fill="#1e293b"
                    >
                      {inst?.flag} {payload.value}
                    </text>
                  </g>
                );
              }}
              width={136}
              tickLine={false}
              axisLine={false}
            />
            <Tooltip content={<CustomTooltip />} cursor={{ fill: "#f1f5f9" }} />
            <ReferenceLine
              x={60}
              stroke="#94a3b8"
              strokeDasharray="4 4"
              label={{ value: "60 %", position: "top", fontSize: 10, fill: "#94a3b8" }}
            />
            <Bar dataKey="weighted_score" radius={[0, 3, 3, 0]} barSize={22}>
              {chartData.map((entry) => (
                <Cell
                  key={entry.company}
                  fill={MATURITY_COLORS[entry.maturity_level] ?? "#9ca3af"}
                />
              ))}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>

      <p className="mt-3 text-xs text-slate-400 text-center">
        Click any bar to view the institution&apos;s detailed scorecard
      </p>
    </div>
  );
}
