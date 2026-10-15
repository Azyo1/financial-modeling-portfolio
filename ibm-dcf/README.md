# IBM — Segment DCF with Quantum Optionality

**Type:** Sell-side Equity Research / 10-Year Segment DCF + Scenario Analysis
**Rating:** OVERWEIGHT | **Price Target:** $320 | **Current:** $227.88 (Oct 14, 2026) | **Upside:** +40.4% (+43.4% incl. dividend)
**Thesis:** "A Cash Machine With a Free Quantum Option — The Debate Is the Discount Rate"

---

## Investment Thesis

IBM is down 31% from its 52-week high after cutting 2026 guidance to 4–5% constant-currency growth, after IBM Z mainframe revenue fell 42% in Q2. We think the market is treating a cyclical Infrastructure slump as structural, while the growth engine keeps compounding.

1. **Software Is the Business** — 44% of FY2025A revenue ($30.0B, +11%) at a 33.1% segment margin; Red Hat +11% and Data +19% in Q2 2026. Confluent (closed Mar 17, 2026) adds real-time data streaming for AI.
2. **2026 Is a Mainframe Air-Pocket** — We model Infrastructure −4% in FY2026E and −2% in FY2027E before the next cycle, and the value still clears today's price.
3. **Quantum, Valued as an Option** — Starling (fault-tolerant) is targeted for 2H 2029, backed by a $10B+ five-year program that includes the Anderon quantum wafer foundry. With only ~$1B of cumulative bookings since 2017, we model quantum as loss-making until FY2030E. The base case is worth $23/share; the Dominant case lifts total value to $502.
4. **The Debate Is the Discount Rate** — Core IBM (ex-quantum) is worth $270/share, above the $228 price, so the market is pricing quantum at zero. Today's price implies a ~9.0% WACC against our 7.75%.

---

## Model Structure

```
IBM_DCF_Model.xlsx
├── Cover            — Rating, PT, key stats, thesis (every number formula-linked)
├── Assumptions      — ALL inputs (blue): segment growth & margins FY2026E–FY2035E, quantum revenue/opex/capex,
│                      FY2025A calibration, WACC, balance sheet, scenario parameters
├── Operating Model  — Segment revenue & profit, corporate costs, EBIT, UFCF, quantum standalone FCF
├── DCF              — WACC, stub + mid-year discounting, terminal value, equity bridge (core debt only),
│                      core vs. quantum value per share, PT & rating
└── Sensitivity      — WACC × g grid, core Bear/Base/Bull, quantum scenarios → probability-weighted PT,
                       market-implied WACC (live re-projection engine)
```

---

## Key Assumptions

| Metric | Value |
|--------|-------|
| FY2025A Revenue | $67.5B (Software $30.0B · Consulting $21.1B · Infrastructure $15.7B · Financing $0.7B) |
| FY2026E Revenue | $70.3B (+4.2%) |
| FY2030E EBIT Margin | 19.8% (GAAP basis; SBC treated as a cost) |
| WACC | 7.75% (Rf 5.1%, β 0.81, ERP 4.3%, core debt 18% of capital) |
| Terminal Growth | 2.5% (TV = 65% of EV) |
| Core Debt / Cash (Jun 30, 2026) | $49.0B / $8.2B ($13B Financing debt excluded, since it funds receivables) |
| Diluted Shares | 953.3M |
| Quantum Revenue (base) | $1.2B FY2030E → $7.0B FY2035E |

---

## Valuation Summary

| Scenario | Value / Share | vs. $227.88 |
|----------|---------------|-------------|
| Core Bear (−3pp growth, −2pp margin, +0.5pp WACC, g 2.0%) | $180 | -21.0% |
| **Base DCF** (core $270 + quantum $23) | **$294** | **+28.8%** |
| Core Bull (+2pp growth, +1.5pp margin, −0.5pp WACC, g 3.0%) | $445 | +95.4% |
| Quantum Stalls / Base / Breakout / Dominant (25/45/22/8%) | $262 / $294 / $377 / $502 | — |
| **Price Target (probability-weighted $320.69, rounded)** | **$320** | **+40.4%** |

At base g, value falls to $239 at an 8.75% WACC and $218 at 9.25%. Rating rule (formula): Overweight if PT upside ≥ +10%, Underweight if ≤ −10%.

---

## Files

| File | Description |
|------|-------------|
| `IBM_DCF_Model.xlsx` | Full Excel model, 5 tabs, all outputs formula-driven |
| `IBM_Initiation_Note.pdf` | 3-page initiation note (every figure read from the model) |

Sources: IBM FY2025 results (Jan 28, 2026) and 2025 Annual Report; Q2 2026 results (Jul 22, 2026) and 10-Q; Confluent closing (Mar 17, 2026); IBM $10B quantum plan and Anderon foundry (Jun 2026). Quantum revenue and costs are analyst estimates; IBM does not disclose quantum revenue. Q3 2026 results are due Oct 21, 2026.

---

*Model built to institutional standards. No circular references. Color-coded inputs (blue), cross-sheet links (green), and formulas (black) per sell-side convention.*
