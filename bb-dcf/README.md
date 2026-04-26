# BlackBerry Limited — DCF & Segment Comps Equity Research Initiation

**Type:** Sell-side Equity Research / Two-Segment DCF + Trading Comps (Blended)
**Rating:** OVERWEIGHT | **Price Target:** $7.00 | **Current:** $5.50 | **Upside:** +27.3%
**Thesis:** "QNX Is the Safety OS for the Physical AI Era — Street Consensus Is Stale at $4.84"

---

## Investment Thesis

**April 2026 Update:** On April 20, 2026 at Hannover Messe, QNX and NVIDIA deepened their collaboration to integrate **QNX OS for Safety 8.0** with **NVIDIA IGX Thor** — the edge AI compute platform for safety-critical applications in robotics, medical devices, and industrial automation. Wall Street consensus stands at $4.84 (Hold, 7 analysts) — below the current price of $5.50 and predating the NVIDIA catalyst. Our $7.00 PT reflects QNX's deserved re-rating as the safety OS layer for the physical AI era.

Four value creation drivers:

1. **QNX Is the Safety Layer for Physical AI** — QNX + NVIDIA IGX Thor is the reference architecture for every safety-certified edge AI deployment (humanoid robots, AMRs, surgical systems, industrial automation). QNX's IEC 61508 / ISO 26262 certifications are a 10-year structural moat. TAM expands from ~$19B automotive software to the full edge AI systems market as physical AI scales.
2. **$950M Royalty Backlog = 2.5+ Years of Locked Revenue** — QNX earns a per-unit royalty for every OEM vehicle or device shipped. The $950M backlog is committed production volumes — already awarded, pending manufacturing. Q4 FY2026 QNX revenue hit $78.7M (+20% YoY, record quarter). New design wins include Mercedes-Benz, BMW, Volvo, Leapmotor, and defense contractor TKMS.
3. **Street Consensus Hasn't Repriced the NVIDIA Catalyst** — Consensus PT $4.84 implies ~5× blended enterprise revenue — reasonable for a mixed-segment company but wrong for QNX as a standalone asset. We assign QNX 8× FY2028E EV/Revenue ($2.97B segment EV) and CySec 3.5× FY2028E ($1.02B), yielding a $7.51 comps-implied PT vs. $6.11 DCF. Blended: $7.00.
4. **FCF Inflection + Active Buyback = Institutional-Grade Downside Support** — FY2026A FCF of $46.5M (3× YoY growth), GAAP profitability ($53.2M net income), $432M net cash, and 15.5M shares repurchased since May 2025. FCF yield grows toward 3.5%+ by FY2028E, removing the last institutional ownership barrier.

---

## Model Structure

```
BB_DCF_Model.xlsx
├── Cover          — Rating, PT, thesis, formula-linked stats
├── Assumptions    — All hardcoded inputs (blue cells)
├── Operating Model — Two-segment P&L (QNX + CySec), EBITDA bridge, UFCF
├── DCF            — PV of FCFs, terminal value (16× FY2031E EBITDA), equity bridge, segment comps
└── Sensitivity    — WACC × Exit Multiple matrix, WACC × QNX EV/Revenue matrix
```

---

## Key Assumptions

| Metric | Value |
|--------|-------|
| FY2026A Total Revenue | $549.1M |
| FY2026A QNX Revenue | $268.0M (+14% YoY) |
| FY2026A CySec Revenue | $281.1M |
| FY2026A Adj. EBITDA | $107.1M (19.5% margin) |
| FY2026A FCF | $46.5M (+3× YoY) |
| FY2027E Revenue Guidance (Mgmt) | $584M–$611M |
| QNX Revenue CAGR FY2026A–FY2031E | ~14.2% |
| Exit EBITDA Margin (FY2031E) | 31.0% |
| Base WACC | 9.0% (RF 4.5% + ERP 5.5% × β 0.82) |
| Exit EV/EBITDA Multiple | 16× FY2031E EBITDA |
| Cash & Investments | $432.4M (Feb 28, 2026) |
| Shares Outstanding (Diluted) | 588M |

---

## Valuation Summary

| Method | Value | Weight |
|--------|-------|--------|
| DCF (WACC 9.0%, 16× FY2031E EBITDA) | $6.11/share | 40% |
| Segment Comps (QNX 8× / CySec 3.5× FY2028E Rev) | $7.51/share | 60% |
| **Blended Price Target** | **$7.00/share** | — |

---

## Files

| File | Description |
|------|-------------|
| `BB_DCF_Model.xlsx` | Full Excel model — 5 tabs |
| `BB_DCF_Initiation_Note.pdf` | Sell-side initiation note |
| `build_bb_dcf.py` | Python (openpyxl) script that generates the Excel workbook |
| `build_bb_memo.py` | Python (reportlab) script that generates the PDF initiation note |

---

## Methodology Notes

- **Two-segment model:** QNX (high-growth embedded OS royalties, 14–18% CAGR) and Cybersecurity (stable government comms, 1–2% growth) modeled separately and priced at differentiated multiples
- **Blended valuation:** 40% DCF / 60% segment comps — comps weighted higher given QNX's comparable-stage premium vs. pure-play software peers
- **WACC rationale:** β = 0.82 reflects royalty revenue stability (below software sector avg of 1.1×); 9.0% appropriate for a profitable, FCF-generating company with $432M net cash
- **All inputs in Assumptions tab:** Operating Model, DCF, and Sensitivity use Excel formula strings for full audit trail — no hardcoded values outside the Assumptions tab

---

*Model built to institutional standards. No circular references. Color-coded inputs (blue), cross-sheet links (green), and formulas (black) per sell-side convention.*
