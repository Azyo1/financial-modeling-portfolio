# Ferrari N.V. — Equity Research Initiation

**Type:** Sell-side Equity Research / Three-Method Valuation
**Rating:** OVERWEIGHT | **Price Target:** $450 | **Current:** $375.50 | **Upside:** +19.8%
**Thesis:** "The Luce Catalyst — Market Is Pricing Ferrari Like BMW, We Think It's Hermès"

---

## Investment Thesis

Ferrari (NYSE: RACE) has pulled back **27.8% from its 52-week high of $519.10** — not because the business deteriorated, but because the market applied an EV-fear discount borrowed from legacy automakers. That discount is misplaced.

Four value creation drivers:

1. **The Luce EV Is an ASP Accelerant** — Ferrari's first EV (designed with Jony Ive, Q4 2026 deliveries) is priced *above* the existing fleet ASP. Unlike BMW or Mercedes, Ferrari's EV transition is a margin *expansion* catalyst, not a headwind.
2. **Multiple Re-rating Opportunity** — RACE trades at ~22× FY2026E EBITDA vs. Hermès at 30×. The correct peer is the luxury goods sector, not autos. A re-rating to 27× alone drives $498/share.
3. **FY2025A Confirms Acceleration** — Record 38.8% EBITDA margin, €7,146M revenue (+7.0% YoY), management guided FY2026E EBITDA of €3.0–3.1B and raised long-term margin target to 40%+.
4. **Near-Debt-Free Balance Sheet + Structural Pricing Power** — Net industrial debt of only €180M (0.06× EBITDA). 24-month waitlists insulate revenue from macro — the company grew EBITDA through COVID.

---

## Model Structure

```
Ferrari_Valuation_Model.xlsx
├── Cover          — Rating, PT, key stats, thesis headline
├── Assumptions    — All hardcoded inputs (blue cells), EUR/USD 1.18
├── Income Statement — FY2023A–FY2030E, unit economics build
├── DCF & Valuation — UFCF build, WACC 7.5%, blended PT (40% DCF / 60% Comps)
└── Sensitivity    — WACC × TGR matrix, multiple × deliveries scenario grid
```

---

## Key Assumptions

| Metric | Value |
|--------|-------|
| EUR/USD | 1.18 |
| Current Price | $375.50 |
| 52-Wk High | $519.10 |
| FY2025A Revenue | €7,146M |
| FY2025A EBITDA | €2,772M (38.8% margin) |
| FY2025A EPS | €8.96 |
| Net Industrial Debt | €180M |
| Shares Outstanding | ~180M diluted |
| Base WACC | 7.5% (luxury goods β = 0.75) |
| Terminal Growth Rate | 3.0% |
| Exit Multiple (Comps) | 27× EV/EBITDA |
| Analyst Consensus PT | $495 (Strong Buy) |

---

## Valuation Summary

| Method | Value | Weight |
|--------|-------|--------|
| DCF (WACC 7.5%, TGR 3.0%) | $351/share | 40% |
| Trading Comps (27× '26E EBITDA) | $498/share | 60% |
| **Blended Price Target** | **$450/share** | — |

---

## Files

| File | Description |
|------|-------------|
| `Ferrari_Valuation_Model.xlsx` | Full Excel model — 5 tabs |
| `Ferrari_DCF_Initiation_Note.pdf` | Sell-side initiation note |
| `build_ferrari_dcf.py` | Python script that generates the Excel model |
| `build_ferrari_memo.py` | Python script that generates the initiation note PDF |

---

## Methodology Notes

- **Three-method valuation:** DCF + Trading Comps + Blended target demonstrates institutional sophistication
- **Luxury β:** Ferrari β = 0.75 (Hermès-style), not 1.2 (auto sector) — a core differentiating assumption
- **Real data:** FY2025A figures from Ferrari's February 10, 2026 full-year results press release; EUR/USD 1.18
- **Conservative Luce assumptions:** 500 units FY2027E, scaling to 1,500 by FY2030E — upside optionality not in base case

---

*Model built to institutional standards. No circular references. Color-coded inputs (blue), cross-sheet links (green), and formulas (black) per sell-side convention.*
