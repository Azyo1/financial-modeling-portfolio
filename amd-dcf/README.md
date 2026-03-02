# Advanced Micro Devices — DCF Equity Research Initiation

**Type:** Sell-side Equity Research / Discounted Cash Flow
**Rating:** OVERWEIGHT | **Price Target:** $215 | **Current:** $200 | **Upside:** +7.5%
**Thesis:** "AMD is the last credible challenger to Nvidia in AI silicon and the clear winner of Intel's CPU meltdown"

---

## Investment Thesis

AMD reported a record FY2025 ($34.6B revenue, +34% YoY) driven by Data Center GPU and EPYC CPU momentum. Four catalysts underpin the thesis:

1. **Data Center GPU Ramp** — MI300X / MI350 series positions AMD as the only credible alternative to Nvidia H100/B200. Enterprise buyers increasingly dual-source to reduce Nvidia dependency. Data Center grew 31.6% YoY in FY2025 to $16.6B.
2. **CPU Market Share Gains** — Intel's manufacturing struggles have structurally shifted server CPU share to AMD EPYC. EPYC now runs in 4 of 5 top cloud hyperscalers. Client segment surged 51.9% YoY in FY2025 driven by AI PC demand.
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
