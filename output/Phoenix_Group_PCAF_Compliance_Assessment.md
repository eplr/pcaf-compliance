# Phoenix Group — PCAF® Compliance Assessment

**Source**: Annual Report and Accounts 2024 (PDF, 26 036 lines extracted text)
**Institution type**: Insurance (life/retirement, £292bn AUA)
**PCAF signatory**: Signatory
**Assessment date**: 2024-12-31
**Method**: Full reading of extracted text (`PHOENIXGROUP_2024_clean.txt`)

---

## Part A — Financed Emissions: 16/23 (69,6%)

### Asset Class Coverage: 2/5
8,0/18 = 44,4%

| Asset class | Status | Points | Evidence |
|---|---|---|---|
| Listed equity + corporate bonds | Reported (S1&S2+S3) | 6,0/6,0 | L2085-2103: 12,4 MtCO2e total S1&S2. S3 separately: 88 MtCO2e (L2231). |
| Business loans / unlisted equity | Missing | 0/6,0 | Not covered (life insurer, no lending). |
| Project finance | Missing | 0/2,0 | Not covered. |
| Commercial real estate | Reported (S1&S2&S3) | 1,0/1,0 | L2180: £5bn real estate. DQS 3,0. Physical risk analysis (L1956-2001). |
| Mortgages | Reported | 0,5/0,5 | L2183-2184: equity release mortgages £5bn. DQS 5,0. |
| Motor vehicle loans | Missing | 0/0,5 | Not covered. |
| Sovereign debt | Partial (S1 production) | 0,5/2,0 | L2178: £37bn sovereign debt. DQS 2,0. |

### Data Quality Score: 4/5
PCAF DQS total = 1,7 (L2284). Per asset class: Listed equity 1,4 · Listed credit 1,5 · Sovereign 2,0 · Real estate 3,0 · Illiquid credit 2,7 · Equity release 5,0. Score 4 (DQS in 1,5–2,5 range).

**Auto-scan failure**: DQS table was completely missed by regex extraction.

### Attribution Methodology: 4/5
Explicitly uses PCAF (L2150): "We use the financed emissions methodologies developed by the Partnership for Carbon Accounting Financials ('PCAF')." Signatory. NZAOA aligned targets (L2146). ISS data vendor. 6 asset classes covered. Score 4.

### Portfolio Coverage: 3/5
£198bn AUA covered / £284bn total = 70% (L2168). Covers 100% of 2025 target scope, 92% of 2030 scope.

**False positive corrected**: The 85% at L5835 was the scope of the 2030 decarbonisation target, not overall AUA portfolio coverage.

### Temporal Coverage: 3/3
2019 baseline. Data for 2019, 2021, 2023, 2024. 52% intensity reduction achieved. 2025/2030/2050 targets. Score 3.

---

## Part B — N/A
Phoenix Group is not a bank/bancassurance.

---

## Part C — Insurance-Associated Emissions: 0/13 (0%)

Phoenix Group is a life/retirement insurer (pensions, annuities, retirement income). No P&C underwriting. IAE under PCAF Part C not applicable.

---

## Score changes vs auto-generated

| Criterion | Old | New | Reason |
|---|---|---|---|
| Part A Asset Class Coverage | 1 | **2** | S3 included for listed assets; 8,0/18 vs 6,5/18 |
| Part A DQS | 0 | **4** | DQS 1,7 found in detailed table (L2284). Auto-scan missed it completely. |
| Part A Attribution | 2 | **4** | Explicit PCAF methodology, signatory, NZAOA. |
| Part A Portfolio Coverage | 4 | **3** | 70% actual coverage (L2168); 85% was 2030 target scope, not AUA coverage. |

**Part A**: 10 → **16**/23 (43,5% → 69,6%)
**Part C**: 0 → **0**/13 (unchanged, correct — no P&C underwriting)
