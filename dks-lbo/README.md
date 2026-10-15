# Dick's Sporting Goods — Leveraged Buyout Analysis

**Type:** Buy-side LBO Model
**Entry:** 9.0x LTM EBITDA | **Exit:** 10.5x LTM EBITDA (Year 5)
**Returns:** 27.0% IRR / 3.3x MOIC
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
├── Debt Schedule  — TLB amortization, cash sweep, revolver, excess-cash build, net debt
├── Returns        — IRR / MOIC, equity bridge
└── Sensitivity    — IRR & MOIC by entry/exit multiple (live, centred on base case)
```

---

## Key Assumptions

| Metric | Value |
|--------|-------|
| LTM Revenue | $13,440M |
| LTM EBITDA | $1,870M |
| Entry Multiple | 9.0x EBITDA |
| Transaction Enterprise Value | $16,830M |
| Total Uses (incl. $300M net debt refinanced + fees) | $17,167M |
| Sponsor Equity Check | $6,882M |
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
| Exit TEV | $29,155M |
| Net Debt at Exit | $6,170M |
| Equity Proceeds | $22,693M |
| MOIC | **3.3x** |
| IRR | **27.0%** |

## Revision Log

- **Oct 2026:** Sources & uses now refinance the $300M of existing net debt (previously it dropped out of the deal), raising the sponsor cheque from $6,582M to $6,882M. The sensitivity tables were dividing exit equity by the purchase price rather than the sponsor's equity cheque; they now compute sponsor equity correctly, take their axes from the Assumptions tab, and reconcile to the Returns tab at the base case. Amortization and sweep are capped at the outstanding balance, with excess cash tracked into net debt. Returns move from 28.1% / 3.5x to 27.0% / 3.3x.
- **Data note:** LTM figures pre-date DKS's Sept 2025 acquisition of Foot Locker and exclude lease liabilities; the model is an illustrative standalone LBO as of February 2026.

---

## Files

| File | Description |
|------|-------------|
| `DKS_LBO_Model.xlsx` | Full Excel model — 6 tabs |
| `DKS_LBO_Deal_Memo.pdf` | 2-page investment memorandum |

---

*Model built to institutional standards. No circular references. Color-coded inputs (blue), cross-sheet links (green), and formulas (black) per sell-side convention.*
