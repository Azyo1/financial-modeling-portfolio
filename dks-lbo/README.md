# Dick's Sporting Goods — Leveraged Buyout Analysis

**Type:** Buy-side LBO Model
**Entry:** 9.0x LTM EBITDA | **Exit:** 10.5x LTM EBITDA (Year 5)
**Returns:** 28.1% IRR / 3.5x MOIC
**Leverage:** 5.5x Total Debt / EBITDA at entry

---

## Investment Thesis

Dick's Sporting Goods is the **last national big-box sporting goods retailer** standing — Sports Authority filed for bankruptcy in 2016, Modell's followed in 2020. The LBO thesis rests on four value creation drivers:

1. **Market Consolidation** — Capturing share from exited competitors drives 4–5% annual revenue growth with minimal incremental capex
2. **Private Label Expansion** — CALIA, DSG, and Alpine Design carry 60–70% gross margins vs. ~40% on Nike/Adidas; mix shift from ~15% toward 20%+ of revenue drives EBITDA margin expansion from 13.9% → 16.5%
3. **Experiential Differentiation** — "House of Sport" format (rock walls, batting cages, golf simulators) converts DKS from commodity retailer to destination, reducing e-commerce threat
4. **Cash Flow Deleveraging** — Strong FCF generation + mandatory cash sweep pays down ~$4.1B of debt over 5 years, amplifying equity returns

---

## Model Structure

```
DKS_LBO_Model.xlsx
├── Cover          — Deal summary, stats grid, investment thesis
├── Assumptions    — All hardcoded inputs (blue cells)
├── Operating Model — 5-year P&L, FCF build
├── Debt Schedule  — TLB amortization, cash sweep, revolver
├── Returns        — IRR / MOIC, equity bridge
└── Sensitivity    — Returns by entry/exit multiple matrix
```

---

## Key Assumptions

| Metric | Value |
|--------|-------|
| LTM Revenue | $13,440M |
| LTM EBITDA | $1,870M |
| Entry Multiple | 9.0x EBITDA |
| Transaction Enterprise Value | $16,830M |
| Sponsor Equity Check | $6,582M |
| Term Loan B | $10,285M (5.5x) |
| TLB Rate | SOFR + 350bps (7.2%) |
| Revenue CAGR | ~4.6% |
| Exit EBITDA Margin | 16.5% |
| Exit Multiple | 10.5x |
| Hold Period | 5 Years |

---

## Returns Summary

| Metric | Value |
|--------|-------|
| Exit EBITDA (Year 5) | $2,777M |
| Exit TEV | $29,158M |
| Net Debt at Exit | $6,153M |
| Equity Proceeds | $22,713M |
| MOIC | **3.5x** |
| IRR | **28.1%** |

---

## Files

| File | Description |
|------|-------------|
| `DKS_LBO_Model.xlsx` | Full Excel model — 6 tabs |
| `DKS_LBO_Deal_Memo.pdf` | 2-page investment memorandum |

---

*Model built to institutional standards. No circular references. Color-coded inputs (blue), cross-sheet links (green), and formulas (black) per sell-side convention.*
