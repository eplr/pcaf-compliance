import { loadOverall } from "@/lib/data";
import { getMeta, MATURITY_BG, MATURITY_LABELS } from "@/lib/meta";
import BenchmarkClient from "@/components/BenchmarkClient";

export default function HomePage() {
  const institutions = loadOverall();

  // Build meta map for client component
  const metaMap = Object.fromEntries(
    institutions.map((i) => [i.company, getMeta(i.company)])
  );

  // Summary stats
  const avg = institutions.reduce((s, i) => s + i.weighted_score, 0) / institutions.length;
  const above60 = institutions.filter((i) => i.weighted_score >= 60).length;
  const signatories = institutions.filter((i) => getMeta(i.company).signatory).length;

  // Maturity distribution
  const maturityDist = [0, 1, 2, 3, 4].map((level) => ({
    level,
    count: institutions.filter((i) => i.maturity_level === level).length,
  }));

  return (
    <div>
      {/* ─── Summary stats ───────────────────────────────── */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 mb-8">
        <StatCard label="Institutions" value={String(institutions.length)} />
        <StatCard
          label="Average score"
          value={`${avg.toFixed(1)} %`}
          sub="weighted"
        />
        <StatCard
          label="Score ≥ 60 %"
          value={String(above60)}
          sub={`${Math.round((above60 / institutions.length) * 100)} % of total`}
        />
        <StatCard
          label="PCAF signatories"
          value={String(signatories)}
          sub={`${Math.round((signatories / institutions.length) * 100)} % of panel`}
        />
      </div>

      {/* ─── Maturity distribution ───────────────────────── */}
      <div className="flex flex-wrap gap-2 mb-8">
        {maturityDist.map(({ level, count }) => (
          <span
            key={level}
            className={`px-3 py-1 rounded-full text-xs font-medium ${MATURITY_BG[level] ?? ""}`}
          >
            {MATURITY_LABELS[level]}: {count}
          </span>
        ))}
      </div>

      {/* ─── Chart heading ───────────────────────────────── */}
      <h2 className="text-lg font-semibold text-slate-800 mb-4">
        Weighted PCAF Compliance Score by Institution
      </h2>

      {/* ─── Interactive chart (client) ──────────────────── */}
      <BenchmarkClient institutions={institutions} metaMap={metaMap} />
    </div>
  );
}

function StatCard({
  label,
  value,
  sub,
}: {
  label: string;
  value: string;
  sub?: string;
}) {
  return (
    <div className="bg-white rounded-xl border border-slate-200 px-5 py-4">
      <p className="text-xs font-medium text-slate-500 uppercase tracking-wide mb-1">
        {label}
      </p>
      <p className="text-2xl font-bold text-slate-900">{value}</p>
      {sub && <p className="text-xs text-slate-400 mt-0.5">{sub}</p>}
    </div>
  );
}
