import { notFound } from "next/navigation";
import {
  loadOverall,
  loadParts,
  loadDetailed,
  loadCompliance,
  toSlug,
} from "@/lib/data";
import { getMeta, MATURITY_BG, MATURITY_LABELS } from "@/lib/meta";
import InstitutionDetail from "@/components/InstitutionDetail";

interface PageProps {
  params: { slug: string };
}

// Pre-generate all institution pages at build time
export function generateStaticParams() {
  const institutions = loadOverall();
  return institutions.map((i) => ({ slug: toSlug(i.company) }));
}

export function generateMetadata({ params }: PageProps) {
  const institutions = loadOverall();
  const inst = institutions.find((i) => toSlug(i.company) === params.slug);
  if (!inst) return { title: "Not found" };
  return { title: `${inst.company} — PCAF Compliance Score` };
}

export default function InstitutionPage({ params }: PageProps) {
  const institutions = loadOverall();
  const inst = institutions.find((i) => toSlug(i.company) === params.slug);
  if (!inst) notFound();

  const allParts     = loadParts();
  const allDetailed  = loadDetailed();
  const allCompliance = loadCompliance();

  const partScores = allParts.filter((p) => p.company === inst.company);
  const criteria   = allDetailed.filter((c) => c.company === inst.company);
  const compliance = allCompliance.filter((c) => c.company === inst.company);

  const meta = getMeta(inst.company);

  return (
    <div>
      {/* ─── Back link ───────────────────────────────────── */}
      <a
        href="/"
        className="inline-flex items-center gap-1 text-sm text-slate-500 hover:text-slate-800 mb-6 transition-colors"
      >
        ← All institutions
      </a>

      {/* ─── Institution header ──────────────────────────── */}
      <div className="bg-white rounded-xl border border-slate-200 px-6 py-5 mb-6 flex flex-col sm:flex-row sm:items-center gap-4">
        <div className="flex-1">
          <div className="flex items-center gap-3 mb-1">
            <span className="text-3xl">{meta.flag}</span>
            <h1 className="text-2xl font-bold text-slate-900">{inst.company}</h1>
          </div>
          <div className="flex flex-wrap items-center gap-2 text-sm text-slate-500">
            <span>{inst.institution_type}</span>
            <span>·</span>
            <span>{meta.country}</span>
            <span>·</span>
            <span>Assessment {inst.assessment_date}</span>
            {meta.signatory && (
              <>
                <span>·</span>
                <span className="text-emerald-600 font-medium">✓ PCAF Signatory</span>
              </>
            )}
          </div>
        </div>

        {/* Overall score */}
        <div className="text-right shrink-0">
          <p className="text-xs text-slate-400 uppercase tracking-wide mb-0.5">
            Weighted score
          </p>
          <p className="text-4xl font-bold text-slate-900 leading-none">
            {inst.weighted_score.toFixed(1)}
            <span className="text-lg font-normal text-slate-400"> %</span>
          </p>
          <span
            className={`inline-block mt-1 px-3 py-0.5 rounded-full text-xs font-semibold ${MATURITY_BG[inst.maturity_level] ?? ""}`}
          >
            {MATURITY_LABELS[inst.maturity_level] ?? inst.maturity_label}
          </span>
        </div>
      </div>

      {/* ─── Part details (client component) ────────────── */}
      <InstitutionDetail
        partScores={partScores}
        criteria={criteria}
        compliance={compliance}
      />

      {/* ─── Recommendation note ─────────────────────────── */}
      {compliance.length > 0 && compliance[0].priority && compliance[0].priority !== "—" && (
        <div className="mt-6 p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-600">
          <span className="font-semibold text-slate-700">Priority recommendation: </span>
          {compliance[0].priority}
        </div>
      )}
    </div>
  );
}
