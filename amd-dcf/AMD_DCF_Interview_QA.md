# AMD DCF — Interview Q&A
**Advanced Micro Devices (NASDAQ: AMD) — Equity Research Initiation**
*OVERWEIGHT | $145 Price Target | +20.8% Upside*

---

## Q1: Walk me through your WACC. Why 9.0%?

Built bottom-up from CAPM. Risk-free rate is the current 10-year Treasury at ~4.2%. AMD's 5-year monthly beta against the S&P 500 is approximately 1.75 raw — but I apply a Blume mean-reversion adjustment toward 1.0 to get a levered beta of ~1.4. AMD is high-beta relative to the broad market, but it's not a pure-play AI speculative name like SMCI or NVDA. It has a diversified revenue base (CPU, GPU, embedded) that dampens tail risk. With an equity risk premium of 5.0% (Damodaran US estimate), cost of equity comes to ~11.2%.

AMD runs with minimal financial debt — roughly $1.7B gross against ~$5B in cash, making it effectively net cash. With essentially no meaningful debt capital in the structure, WACC collapses toward the cost of equity. The small after-tax debt benefit brings it to ~9.0%.

**If you push back:** If you use raw unadjusted beta of 1.75, cost of equity goes to ~13%+, WACC to ~12%. That's too punitive for a company that's net cash with a validated GPU revenue ramp. At 12% WACC, fair value would be ~$95 — which implies the market has been persistently wrong about AMD for 2+ years. Possible, but you'd need a very specific thesis for why.

---

## Q2: Why a 3.5% terminal growth rate? That seems aggressive.

The TGR reflects two structural realities: (1) secular demand for compute is growing faster than GDP, and (2) AMD's position as the only credible at-scale alternative to Nvidia in data center GPUs gives it a durable market share floor.

The global semiconductor industry has historically grown at roughly 2× nominal GDP. A 3.5% TGR assumes AMD maintains a moderate slice of a structurally growing market — it does not assume they sustain the 60–80% revenue growth rates of the MI300X ramp. That growth decelerates to teens by the terminal period. 3.5% is the steady-state assumption, not the current growth rate.

**Sensitivity check:** At 3.0% TGR (one notch down), price target moves from $145 to ~$130 — still OVERWEIGHT. At 2.5%, PT is ~$115. The model isn't fragile on this assumption.

---

## Q3: What's your data center revenue build and how did you stress test it?

Data center is the thesis-defining segment. AMD reported ~$12.6B of data center revenue in FY2024, driven primarily by MI300X GPU ramp. I model data center growing at a decelerating CAGR — roughly 30% in FY2025, 25% in FY2026, 18% in FY2027 — reaching ~$25B by FY2027. This assumes AMD holds and modestly grows its GPU attach rate in enterprise AI, while also continuing to take CPU market share from Intel (now above 30% of server CPU market).

**Stress test:** The sensitivity tab runs data center at ±20% versus base case. A 20% miss on data center revenue moves the PT by roughly –$22/share to ~$123. A 20% beat takes it to ~$168. In the bear scenario, data center GPU growth stalls at 15% CAGR — implying AMD's MI300X hits a ceiling because hyperscalers pivot to custom silicon (TPUs, Trainium). That's the tail risk. It doesn't break the thesis in Year 1, but by Year 3 the divergence from base is material.

---

## Q4: AMD is a buy on data center GPUs — but Nvidia has the same exposure and trades at a premium. Why AMD over Nvidia?

I'm not saying AMD is a better business than Nvidia — Nvidia almost certainly is. I'm saying AMD is mispriced relative to its own earnings power. Nvidia trades at 25–30× forward earnings. AMD at 20–22×. The spread has historically been 5–8 turns; it's currently 8–10 turns. That gap closes as AMD executes — not because Nvidia underperforms, but because the market is underpricing AMD's GPU ramp.

The differentiated reason to own AMD specifically: the Xilinx amortization roll-off (see Q5) adds $0.40–0.60 to EPS mechanically by FY2026, independent of any growth. And AMD's GAAP-to-non-GAAP EPS spread is wider than Nvidia's, which means GAAP investors are underweighting AMD relative to cash earnings.

---

## Q5: What's the Xilinx amortization roll-off and why is it a catalyst?

AMD acquired Xilinx in February 2022 for ~$35B. That purchase price created a large intangible asset balance — primarily customer relationships and developed technology — which is amortized into GAAP operating income over the useful life of the assets. AMD has been recording roughly $1.5B per year in purchase price amortization related to Xilinx.

As that amortization schedule runs down (largely complete by FY2026), GAAP EPS jumps by ~$0.40–0.60 per share on a purely mechanical basis — no revenue growth required. Most sell-side models already adjust for this on a non-GAAP basis, but some buy-side participants anchor to GAAP multiples. When GAAP EPS catches up to non-GAAP EPS, the multiple compression from GAAP investors reverses.

**Why it matters now:** The amortization peak impact was FY2023–FY2024. The roll-off accelerates in FY2025–FY2026. That's within the investment horizon and creates a near-term re-rating catalyst that doesn't depend on any GPU growth assumption.

---

## Q6: Walk me through your DCF. What's the biggest driver of the price target — the FCF or the terminal value?

Terminal value. In a 5-year DCF at 9.0% WACC, terminal value typically represents 70–80% of total enterprise value — and AMD is no different. The PV of 5-year FCFs contributes roughly $30–35/share; the terminal value contributes $110–115/share.

That means the model is really a terminal value estimation exercise with a 5-year FCF buildup as scaffolding. This is why the WACC × TGR sensitivity table is the most important output — small moves in either assumption dominate the PT.

I cross-reference the DCF against two sanity checks: (1) street consensus PT of $130–150, which triangulates with my $145; and (2) the implied NTM P/E at target, which is ~22–24× — reasonable for a semiconductor company with AMD's growth profile. All three methods point to the same range.

---

## Q7: What's your bull case and what has to go right?

**Bull case: $175–190/share.** Requires three things to converge:

1. **Data center GPU acceleration** — MI300X adoption in enterprise AI runs ahead of expectations, data center revenue reaches $20B+ in FY2026 vs. my $16B base case. AMD's ROCm software ecosystem closes more of the CUDA gap than modeled.
2. **PC/client recovery upside** — A stronger consumer PC upgrade cycle (post-pandemic fatigue clearing, Windows 11 refresh) adds $0.30–0.40 of incremental EPS in FY2025–FY2026 beyond my base.
3. **Multiple re-rating** — As GAAP EPS normalizes post-Xilinx amortization, P/E re-rates to 25× forward — historically the midpoint of AMD's range when growing at this rate.

The bull case is not heroic. It requires AMD to outperform on its primary growth driver by ~25% and the market to price that appropriately.

---

## Q8: What's the biggest risk to your thesis?

**Hyperscaler custom silicon displacement.** Microsoft (Maia), Google (TPU v5), Amazon (Trainium 2) are all accelerating their own AI chip development. If hyperscalers — AMD's biggest potential GPU customers — build enough proprietary silicon to reduce dependence on merchant GPUs, the total addressable market for AMD's MI-series contracts. AMD needs the ecosystem of enterprises and cloud customers who *can't* afford custom silicon programs to keep growing.

This is a risk that's hard to model because it plays out over 3–5 years and is driven by corporate strategic decisions, not publicly visible metrics. I stress test it by running the data center growth at 50% of base case — which cuts the PT to ~$105–115 — but even that is probably not severe enough for a scenario where hyperscaler custom silicon meaningfully displaces AMD.

**Secondary risk:** Nvidia's CUDA ecosystem moat proves more durable than expected, and enterprise AI software remains locked to CUDA in a way that makes AMD GPUs impractical for most workloads. AMD's ROCm software stack has improved significantly, but software lock-in is the reason AMD hasn't taken GPU share faster.

---

## Q9: Why AMD over Intel? Intel is arguably the bigger turnaround story.

Intel is a turnaround. AMD is a continuation of an execution track record. These are very different risk profiles.

Intel needs to: fix a broken foundry operation, rebuild manufacturing parity with TSMC (Intel is currently 1–2 process nodes behind), regain CPU market share it already lost to AMD, and ship competitive data center GPU silicon (Gaudi series has had limited traction). That's four simultaneous execution challenges, any one of which could derail the others.

AMD needs to: keep executing on a GPU ramp that's already generating $12.6B in revenue, continue taking CPU share from Intel's weakening position, and not lose ROCm ground to Nvidia's CUDA ecosystem. Their path is narrower but validated.

I own the cleaner story. AMD has already won the CPU battle — they just need to not lose the GPU war.

---

## Q10: What would make you downgrade?

Three specific triggers, in order of conviction:

1. **Data center revenue misses $4B in any single quarter** — the underlying quarterly run rate should be ~$4–5B if the ramp is on track. A miss signals MI300X adoption has stalled and the CUDA moat is holding better than expected. Two consecutive quarters below $4B and I'm revisiting the rating.

2. **AMD loses CPU market share to Intel** — specifically, if Granite Rapids (Intel's current-gen server CPU) takes back meaningful ground in hyperscaler sockets. AMD's server CPU share above 30% is a load-bearing assumption. If it slides back to 25%, the dual-catalyst thesis (GPU + CPU) loses a leg.

3. **Sustained risk-free rate rise above 5.5%** — this isn't business-specific, but a 10-year Treasury above 5.5% would push WACC above 10.5–11% and compress the PT to ~$100–110, where the risk/reward looks much less compelling.

The $105 bear case on my sensitivity table is my stop-loss thesis.

---

*Built alongside AMD_DCF_Model.xlsx — Francisco Rodriguez, 2026*
