# Advanced Micro Devices — DCF Equity Research (Coverage Update)

**Type:** Sell-side Equity Research / Discounted Cash Flow
**Rating:** UNDERWEIGHT | **Price Target:** $405 | **Current:** $570.82 (Oct 14, 2026) | **Upside:** -29.0%
**Thesis:** "The Thesis Played Out — Now the Price Has Run Past the Cash Flows"

---

## Investment Thesis

**October 2026 Update:** We initiated in February 2026 on the AI data center ramp and the business has delivered: FY2025A revenue grew 34% to $34.6B, Q2 2026 revenue hit a record $11.5B (+50% YoY) and Data Center revenue more than doubled to $6.7B. The stock has moved further and faster, to ~$950B of market value (~48x our FY2027E EBITDA).

We rebuilt the model on current data: FY2025A segment actuals, Q1/Q2 2026 results, the ~$13.0B Q3 2026 guide, the Jun 27, 2026 balance sheet, and a **10-year forecast that fades growth to the terminal rate** rather than cutting off a 20%+ grower after five years.

1. **Data Center Is Now the Business** — Q2 2026 Data Center revenue was $6.7B (+107% YoY), 58% of revenue. MI450 and the Helios rack-scale platform ramp in H2 2026 alongside the first gigawatt of the OpenAI agreement. We model 75% Data Center growth in FY2026E and 60% in FY2027E.
2. **The Current Price Needs the Bull Case** — Our base case compounds Data Center revenue at ~46% a year through FY2030E (below the >60% Analyst Day target) and is worth $343/share. Only the Bull case ($625) and the DC Super Bull scenario ($684) clear today's price.
3. **Margins Are Expanding** — GAAP gross margin reached 54% in Q2 2026 (40% a year earlier). We treat SBC as a real cost and model EBITDA margin rising from 20.3% (FY2025A) to 35.0% (FY2030E).
4. **What Would Change Our View** — Evidence Data Center can compound above ~55% through FY2030E, a lower cost of capital, or a pullback toward our probability-weighted value.

---

## Model Structure

```
AMD_DCF_Model.xlsx
├── Cover            — Rating, PT, key stats, thesis (every number formula-linked)
├── Assumptions      — ALL inputs (blue): segment growth FY2026E–FY2035E, margins, capex, WACC, balance sheet, scenarios
├── Income Statement — FY2022A–FY2035E P&L and unlevered FCF build
├── DCF              — WACC build, stub-period + mid-year discounting, terminal value, equity bridge, PT & rating
└── Sensitivity      — WACC × g grid, Bear/Base/Bull, Data Center scenarios → probability-weighted PT (live re-projection engine)
```

---

## Key Assumptions

| Metric | Value |
|--------|-------|
| FY2025A Revenue | $34.6B (+34% YoY) |
| FY2025A EBITDA (GAAP) | $7.0B (20.3% margin) |
| FY2026E Revenue | $48.6B |
| Revenue CAGR FY2025A–FY2030E | 31.7% |
| FY2030E EBITDA Margin | 35.0% |
| WACC | 11.1% (Rf 5.1%, β 1.40, ERP 4.3%) |
| Terminal Growth Rate | 3.5% (TV = 63% of EV, 10.6x terminal EBITDA) |
| Cash / Debt (Jun 27, 2026) | $13.1B / $3.2B |
| Diluted Shares | 1,667M (OpenAI warrant excluded) |

---

## Valuation Summary

| Scenario | Value / Share | vs. $570.82 |
|----------|---------------|-------------|
| Bear (−10pp growth, −5pp margin, +1pp WACC, g 3.0%) | $128 | -77.6% |
| **Base DCF** | **$343** | **-39.9%** |
| Bull (+6pp growth, +3pp margin, −0.5pp WACC, g 4.0%) | $625 | +9.6% |
| DC Downside / Base / Bull / Super Bull (20/40/30/10%) | $265 / $343 / $488 / $684 | — |
| **Price Target (probability-weighted, rounded)** | **$405** | **-29.0%** |

Rating rule (formula): Overweight if PT upside ≥ +10%, Underweight if ≤ −10%, otherwise Equal-Weight.

---

## Revision Log

- **Oct 2026:** Fixed a rating/model mismatch — the published $215 Overweight was never supported by the workbook (the DCF computed $113). Rebuilt on FY2025A actuals and 2026 data; removed the already-reported FY2025 cash flow from the discounted period; replaced hardcoded sensitivity and scenario tables with live formulas; moved every input to the Assumptions tab; corrected cash/debt/shares to the latest balance sheet.

---

## Files

| File | Description |
|------|-------------|
| `AMD_DCF_Model.xlsx` | Full Excel model — 5 tabs, all outputs formula-driven |
| `AMD_DCF_Initiation_Note.pdf` | Coverage update note (every figure read from the model) |

Sources: AMD 10-K FY2022–FY2025, Q4 2025 / Q1 2026 / Q2 2026 earnings releases, Q3 2026 outlook, Nov 11 2025 Financial Analyst Day.

---

*Model built to institutional standards. No circular references. Color-coded inputs (blue), cross-sheet links (green), and formulas (black) per sell-side convention.*
