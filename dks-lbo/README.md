# Dick's Sporting Goods — Leveraged Buyout Analysis

**Type:** Buy-side LBO Model
**Entry:** 9.0x LTM EBITDA | **Exit:** 10.5x LTM EBITDA (Year 5)
**Returns:** 30.4% IRR / 3.8x MOIC
**Leverage:** 5.5x Total Debt / EBITDA at entry

---

## Investment Thesis

Dick's Sporting Goods is the **last national big-box sporting goods retailer** standing — Sports Authority filed for bankruptcy in 2016, Modell's followed in 2020. The LBO thesis rests on four value creation drivers:

1. **Market Consolidation** — Capturing share from exited competitors drives 4–5% annual revenue growth with minimal incremental capex
2. **Private Label Expansion** — CALIA, DSG, and Alpine Design carry 60–70% gross margins vs. ~40% on Nike/Adidas; mix shift from 20% → 30% of revenue drives EBITDA margin expansion from 13% → 16.5%
3. **Experiential Differentiation** — "House of Sport" format (rock walls, batting cages, golf simulators) converts DKS from commodity retailer to destination, reducing e-commerce threat
4. **Cash Flow Deleveraging** — Strong FCF generation + mandatory cash sweep pays down ~$3.4B of debt over 5 years, amplifying equity returns

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
| LTM Revenue | $13,284M |
| LTM EBITDA | $1,475M |
| Entry Multiple | 9.0x EBITDA |
| Purchase Price | $13,275M |
| Equity Check | $6,644M (50%) |
| Term Loan B | $6,631M (5.5x) |
| Revenue CAGR | ~4.6% |
| Exit EBITDA Margin | 16.5% |
| Exit Multiple | 10.5x |
| Hold Period | 5 Years |

---

## Returns Summary

| Metric | Value |
|--------|-------|
| Exit TEV | $28,203M |
| Net Debt at Exit | $5,464M |
| Exit Equity Value | $22,454M |
| MOIC | **3.8x** |
| IRR | **30.4%** |

---

## Files

| File | Description |
|------|-------------|
| `DKS_LBO_Model.xlsx` | Full Excel model — 6 tabs |
| `DKS_LBO_Deal_Memo.pdf` | 2-page investment memorandum |
| `DKS_LBO_Interview_QA.md` | LBO interview Q&A (6 questions) |
| `build_dks_lbo.py` | Python script that generates the Excel model |
| `build_dks_memo.py` | Python script that generates the deal memo PDF |

---

## Interview Q&A

Common LBO interview questions answered in context of this deal — see [`DKS_LBO_Interview_QA.md`](./DKS_LBO_Interview_QA.md).

Topics covered:
- Why higher leverage increases IRR
- Exit multiple compression scenario
- Why 5.5x leverage vs. 7x
- Key downside risks and mitigants
- Sensitivity drivers: what moves returns most
- EBITDA -10% stress test

---

*Model built to institutional standards. No circular references. Color-coded inputs (blue), cross-sheet links (green), and formulas (black) per sell-side convention.*
