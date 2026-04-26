# Nautilus Biotechnology — DCF & Initiation of Coverage

**Type:** Discounted Cash Flow (Pre-Revenue Biotech / Life Science Tools)
**Rating:** OVERWEIGHT
**Price Target:** $5.00
**Current Price:** ~$2.97 (April 2026)
**Upside:** +68.4%

---

## Thesis

Nautilus Biotechnology (NASDAQ: NAUT) is developing **Voyager**, a single-molecule proteomics platform that quantifies 10 billion intact proteins simultaneously with 1.5% coefficient of variation — roughly 27× more reproducible than legacy mass spectrometry. The first commercial assay (Tau Proteoforms, targeting Alzheimer's biomarker research) launched in January 2026; Baylor College of Medicine became the first paying Early Access customer in March 2026.

**April 2026 Update:** Voyager was publicly debuted at US HUPO on February 24, 2026, where the first field evaluation unit (installed at the Buck Institute for Research on Aging) demonstrated highly reproducible insights into tau proteoform biology — a key technical de-risking event. Commercial launch timeline: Voyager pre-orders open in **late 2026**, with instrument installations beginning in **early 2027** (slight timeline refinement vs. original full-launch estimate). Nautilus also hired Amber Faust as VP of Sales in April 2026, building out the commercialization team ahead of launch. The thesis remains intact.

At ~$2.97/share, the stock trades at an enterprise value of ~$220M — still pricing near-total failure into a platform executing on its commercialization milestones. The $156M net cash balance ($1.23/share) provides ~41% downside support. Our base case DCF yields a $5.00 blended price target.

---

## Model Structure

```
NAUT_DCF_Model.xlsx
├── Cover            — Rating, PT, company snapshot, thesis, valuation summary
├── Assumptions      — All hardcoded inputs (blue cells): revenue ramp, gross margin,
│                      R&D/G&A by year, WACC components, terminal value inputs, balance sheet
├── Operating Model  — FY2026E–FY2035E P&L: revenue, gross profit, opex, EBIT, NOPAT,
│                      unlevered FCF bridge (NOPAT + D&A – capex – ΔNWC)
├── DCF              — WACC build, PV of FCFs, terminal value (EV/Revenue method),
│                      equity bridge (EV + net cash → intrinsic value per share)
└── Sensitivity      — WACC × Terminal EV/Revenue matrix, WACC × Terminal Revenue matrix,
                       bull / base / bear scenario summary
```

---

## Key Assumptions

| Input | Value | Rationale |
|-------|-------|-----------|
| WACC (Base) | 20.0% | Pre-revenue micro-cap; CAPM + 5% size/illiquidity premium |
| WACC (Bull) | 17.0% | De-risked post commercial launch |
| WACC (Bear) | 20.0% | Bear uses revenue haircut vs. WACC increase |
| Terminal EV/Revenue | 8.0x (base) | Discount to Illumina's comparable-stage 12x; consistent with Bruker/Waters |
| Terminal Revenue (2035E) | $490M | ~310 installed instruments; consumables ~55% of revenue |
| Projection Period | 10 years (2026–2035) | Standard for pre-revenue platform company |
| Tax Rate | 25% (when EBIT > 0) | NOL carryforward not modeled (conservative) |
| Profitability Inflection | FY2031E | EBIT turns positive at ~$200M revenue / 63% gross margin |
| Net Cash (FY2025) | $156.1M | Cash + short + long-term investments; no material debt |
| Shares Outstanding | 126.6M | FY2025 10-K weighted average |

---

## Valuation Summary

| Scenario | WACC | Term. Revenue | EV/Revenue | Price Target | Upside |
|----------|------|--------------|------------|-------------|--------|
| Bull Case | 17.0% | $700M | 10.0x | $7.65 | +189% |
| **Base Case ★** | **20.0%** | **$490M** | **8.0x** | **$4.81** | **+81%** |
| Bear Case | 20.0% | $200M | 6.0x | $1.55 | -41% |
| **Blended PT (55/25/20)** | — | — | — | **$5.00** | **+89%** |

---

## Files

| File | Description |
|------|-------------|
| `NAUT_DCF_Model.xlsx` | Full 5-tab Excel DCF model (Cover, Assumptions, Operating Model, DCF, Sensitivity) |
| `NAUT_DCF_Initiation_Note.pdf` | 2-page equity research initiation note with thesis, projections, valuation, risks |
| `build_naut_dcf.py` | Python (openpyxl) script that generates the Excel workbook |
| `build_naut_memo.py` | Python (reportlab) script that generates the PDF initiation note |

---

## Methodology Notes

- **Pre-revenue DCF approach:** Negative FCFs for FY2026–FY2031E are discounted at a high WACC (20%) to reflect development-stage execution risk. The terminal value is computed using an EV/Revenue multiple (rather than a growth-in-perpetuity method) consistent with how life science tools comps are traded.
- **Net cash treatment:** The $156.1M liquid balance is added to enterprise value at the equity bridge — it offsets near-term negative FCFs and provides a floor. Future dilutive equity raises are not modeled explicitly (noted as a risk).
- **Razor / blade gross margin ramp:** Gross margins expand from 50% at commercial launch (instrument-heavy) to 65% by 2032+ as consumables (high-margin, recurring) become the revenue majority — consistent with Illumina and 10x Genomics at equivalent stages.
- **WACC:** 20% base reflects: 4.5% risk-free rate + 1.8 beta × 5.5% ERP + 5.0% size/illiquidity premium for a pre-revenue micro-cap with no debt in the capital structure.
