# Advanced Micro Devices — DCF Equity Research Initiation

**Type:** Sell-side Equity Research / Discounted Cash Flow
**Rating:** OVERWEIGHT | **Price Target:** $215 | **Current:** $348.84 | **Upside:** -38.3% (PT Exceeded — stock has significantly outperformed)
**Thesis:** "AMD is the last credible challenger to Nvidia in AI silicon and the clear winner of Intel's CPU meltdown — thesis has played out, stock has significantly outperformed the $215 PT"

---

## Investment Thesis

**April 2026 Update:** The thesis has played out. AMD has run from ~$200 to ~$349 (+74%), exceeding the original $215 price target. Q1 2026 revenue was guided at ~$9.8B (+32% YoY), and management called for Data Center to grow 60%+ in FY2026 as the MI450 and Helios platform ramp begins in H2 2026. Q1 2026 earnings are scheduled for May 5, 2026.

AMD reported a record FY2025 ($34.6B revenue, +34% YoY) driven by Data Center GPU and EPYC CPU momentum. Four catalysts underpin the thesis:

1. **Data Center GPU Ramp** — MI350 Series is now in active deployment; MI450 and the Helios multi-rack AI platform begin ramping in H2 2026. Q4 2025 Data Center revenue hit $5.4B (+39% YoY, +24% QoQ), a new record driven by Instinct GPU and EPYC momentum. Management guided Data Center revenue growth of 60%+ for FY2026. Enterprise dual-sourcing away from Nvidia dependency continues to accelerate.
2. **CPU Market Share Gains** — Intel's structural struggles have continued to benefit EPYC. DA Davidson upgraded AMD to Buy (PT $375) following Intel's Q1 2026 results, noting a structural shift in AI workload CPU demand that favors AMD's architecture. EPYC now runs in 4 of 5 top cloud hyperscalers. Client segment surged 51.9% YoY in FY2025 driven by AI PC demand.
3. **Operating Leverage** — AMD's fabless model means incremental Data Center revenue drops at 65–70% gross margins. As Xilinx amortization rolls off (~$2.6B/yr declining to ~$2.1B by FY2029), GAAP EBIT will reconnect with cash earnings.
4. **Xilinx Embedded Recovery** — Embedded stabilized at $3.5B in FY2025 (flat YoY) after a severe inventory correction. Recovery to 10–15% annual growth expected through FY2029 as aerospace, automotive, and industrial customers resume design-in cycles.

---

## Model Structure

```
AMD_DCF_Model.xlsx
├── Cover          — Rating, PT, key stats, investment thesis
├── Assumptions    — Segment revenue growth rates, margins, D&A by year
├── Income Statement — FY2022A–FY2029E P&L and unlevered FCF build
├── DCF            — WACC build, PV of FCFs, terminal value, equity bridge
└── Sensitivity    — WACC × TGR matrix, bull/base/bear scenarios
```

---

## Key Assumptions

| Metric | Value |
|--------|-------|
| FY2025A Revenue | $34.6B |
| FY2025A EBITDA | $8.5B (Adj.) / $7.0B (GAAP) |
| FY2025A EBITDA Margin | ~24.6% (Adj.) |
| Revenue CAGR FY2025–FY2029E | ~16% |
| Exit EBITDA Margin (FY2029E) | 29.0% |
| Base WACC | ~10.3% |
| Terminal Growth Rate | 3.5% |
| Shares Outstanding | 1,620M |
| Net Cash | ~$4.0B |

---

## Valuation Summary

| Scenario | WACC | TGR | Implied Price |
|----------|------|-----|---------------|
| Bear | 10.5% | 3.0% | ~$112 |
| Base | 9.0% | 3.5% | ~$143 |
| Bull | 8.5% | 4.0% | ~$173 |
| **Price Target** | — | — | **$215** |

Price target reflects probability-weighted scenario analysis with upside weighting toward Data Center GPU outperformance.

---

## FY2025A Segment Actuals

| Segment | FY2025A Revenue | YoY Growth |
|---------|----------------|------------|
| Data Center | $16,635M | +31.6% |
| Client | $10,640M | +51.9% |
| Gaming | $3,910M | +53.3% |
| Embedded | $3,454M | -3.8% |
| **Total** | **$34,639M** | **+34.3%** |

---

## Files

| File | Description |
|------|-------------|
| `AMD_DCF_Model.xlsx` | Full Excel model — 5 tabs |
| `AMD_DCF_Initiation_Note.pdf` | Sell-side initiation note |

---

*Model built to institutional standards. No circular references. Color-coded inputs (blue), cross-sheet links (green), and formulas (black) per sell-side convention.*
