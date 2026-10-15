# Micron Technology — Memory-Cycle DCF

**Type:** Sell-side Equity Research / 10-Year Cycle DCF (bits × price) + Scenario Analysis
**Rating:** OVERWEIGHT | **Price Target:** $1,010 | **Current:** $914.13 (Oct 14, 2026) | **Upside:** +10.5%
**Thesis:** "Priced for the Boom, Not the Bust: The Payoff Is Asymmetric, the Base Case Is Not"

---

## Investment Thesis

Micron is in the biggest memory upcycle on record. FY2026 (ended Sept 3, 2026) revenue rose 256% to $133.2B at an 81% gross margin. Q4 alone brought in $54.2B, and Q1 FY2027 is guided to $61.5B at ~86% gross margin. Management sees supply *tighter* in FY2027–28 and has "no line of sight" to balance.

**The caveat:** our base case is worth **$876**, 4% *below* today's price. The $1,010 target sits above the price only because the scenario payoff is asymmetric. Memory pricing compounds, so a milder downturn (Bull, $1,830) adds far more value than a deeper one (Bear, $466) takes away.

1. **AI Turned Memory Into the Bottleneck.** More than 75% of FY2027 output is committed; calendar-2027 HBM is priced "much higher" than 2026; 26 strategic customer agreements cover 35%+ of revenue through 2030.
2. **Every Memory Boom Funds Its Own Bust.** FY2027 capex is guided "materially higher" than FY2026's $27.4B (H1 alone ~$25B). We hold pricing through FY2028E, then model DRAM/NAND prices −45% in FY2029E and −30% in FY2030E. Revenue troughs at $181B and gross margin at 45%.
3. **The New Mid-Cycle Is the Whole Debate.** The boom years (FY2027–28E) are only 28% of EV; terminal value is 41%. The base case assumes $257B of revenue by FY2036E at ~50% gross margin, roughly 7× pre-AI revenue.
4. **The Market Is Already Discounting a Bust.** 5.6x FY2027E earnings, but 17.1x trough (FY2031E) and 9.8x the through-cycle average.

---

## Model Structure

```
MU_DCF_Model.xlsx
├── Cover            — Rating, PT, key stats, cycle P/Es, thesis (every number formula-linked)
├── Assumptions      — ALL inputs (blue): DRAM/NAND bit growth & ASP FY2027E–FY2036E, margins, opex, capex,
│                      FY2026A calibration, WACC, balance sheet, scenario parameters
├── Operating Model  — DRAM + NAND revenue, gross profit, opex, EBIT, EPS proxy, UFCF
├── DCF              — WACC, stub + mid-year discounting, terminal value, boom-years share of EV, PT & rating
└── Sensitivity      — WACC × g grid, Bear/Base/Bull re-projection → probability-weighted PT,
                       P/E at current price on boom / bust / trough / through-cycle EPS
```

---

## Key Assumptions

| Metric | Value |
|--------|-------|
| FY2026A Revenue / Gross Margin | $133.2B / 81.1% |
| FY2027E Revenue | $269.3B (+102%; Q1 guide $61.5B) |
| Peak (FY2028E) Revenue | $338.6B |
| Trough Revenue / Operating Margin | $181.4B (FY2030E) / 38.7% (FY2031E) |
| FY2036E Revenue / Gross Margin | $257.0B / 50% |
| Capex Intensity | 20.5% (FY27E) → 25% of revenue through the cycle |
| WACC | 11.5% (Rf 5.1%, β 1.50, ERP 4.3%) |
| Terminal Growth | 3.0% |
| Cash / Debt (Sept 3, 2026) | $73.5B / $5.2B |
| Diluted Shares | 1,147M |

---

## Valuation Summary

| Scenario | Trough Revenue | Value / Share | vs. $914.13 | Weight |
|----------|----------------|---------------|-------------|--------|
| Bear: deeper bust (ASPs −15pp, GM −5pp, capex +2pp, WACC +1pp, g 2.5%) | $89B | $466 | -49% | 25% |
| **Base** | **$181B** | **$876** | **-4%** | **50%** |
| Bull: shortage lasts (ASPs +15pp, GM +5pp, capex −2pp, WACC −1pp, g 3.5%) | $280B | $1,830 | +100% | 25% |
| **Price Target (probability-weighted $1,012, rounded)** | — | **$1,010** | **+10.5%** | — |

The rating is only just inside the Overweight band (rule: ≥ +10%), so treat it as a positive skew, not a strong conviction call.

---

## Files

| File | Description |
|------|-------------|
| `MU_DCF_Model.xlsx` | Full Excel model, 5 tabs, all outputs formula-driven |
| `MU_Initiation_Note.pdf` | 3-page initiation note (every figure read from the model) |

Sources: Micron Q4 / FY2026 results (Sept 30, 2026), 8-K and earnings call; FY2025 10-K. The FY2026A DRAM/NAND split, bit growth, pricing paths, the FY2029E–FY2031E downturn and the scenario parameters are analyst estimates; management has given no view beyond FY2028.

---

*Model built to institutional standards. No circular references. Color-coded inputs (blue), cross-sheet links (green), and formulas (black) per sell-side convention.*
