import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "PCAF Compliance Score",
  description:
    "Benchmark of PCAF compliance across 25 European financial institutions — Parts A, B and C.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-slate-50 text-slate-900 antialiased min-h-screen flex flex-col">
        {/* ─── Header ─────────────────────────────────────────── */}
        <header className="bg-gradient-to-r from-slate-900 to-slate-700 text-white">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5">
            <a href="/" className="flex items-baseline gap-3 w-fit">
              <span className="text-xl font-bold tracking-tight">
                PCAF Compliance Score
              </span>
              <span className="text-slate-400 text-sm font-normal">
                25 European financial institutions · 2024
              </span>
            </a>
          </div>
        </header>

        {/* ─── Main ───────────────────────────────────────────── */}
        <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
          {children}
        </main>

        {/* ─── Footer ─────────────────────────────────────────── */}
        <footer className="border-t border-slate-200 bg-white">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between text-xs text-slate-400">
            <span>
              PCAF Compliance Score · Assessment date 2024-12-31 · Methodology V2
            </span>
            <span>
              Partnership for Carbon Accounting Financials
            </span>
          </div>
        </footer>
      </body>
    </html>
  );
}
