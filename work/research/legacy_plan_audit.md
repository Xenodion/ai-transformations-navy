# Audit of the historical draft (`legacy_plan_unverified.md`)

- **Step:** 07 — [#7](https://github.com/Xenodion/ai-transformations-navy/issues/7). Audited 8 November 2026 by Alexandre Waerniers, with Claude Code.
- **Acceptance criterion:** classify reusable claims and numbers as verified, to recalculate, assumption, unsupported, or discarded; flag portfolio and financial inconsistencies.
- **Inputs:** [strategy synthesis](../../sources/synthesis/2026-11-08_totalenergies_strategy_activities.md) (S04), [AI and organisation synthesis](../../sources/synthesis/2026-11-08_totalenergies_ai_data_organization.md) (S05), [competitor synthesis](../../sources/synthesis/2026-11-08_competitors_benchmarks.md) (S06), [register](../../sources/register.md), plus targeted checks in the URD 2025 (SRC-002).
- **References:** `L31` means line 31 of the draft. All arithmetic was recomputed from the draft's own numbers.

**Classes used**

| Class | Meaning |
| --- | --- |
| **Verified** | Matches a registered source; reusable as is, with the source cited |
| **To recalculate** | Idea or method usable, but the number is wrong, outdated or not reproducible |
| **Assumption** | Plausible design choice or estimate with no source; reusable only as a labelled assumption, with a formula and range |
| **Unsupported** | Presented as fact or benchmark but no source found; must not be reused unless a source is found |
| **Discarded** | Contradicted by evidence, or a decision taken before the evidence (AGENTS.md rule 5) |

## 1. Key findings

1. **Several use cases duplicate what TotalEnergies already runs or has funded:**
   - the data platform (Cognite and AspenTech rollouts, 2025–2028);
   - Copilot (deployed since 2024);
   - trading AI (Predictive Layer, insourced);
   - methane detection (AUSEA drones since 2022, 13,000 sensors, Methane Tracking Center);
   - the Pangea 5 "extension" (a > €100M supercomputer already contracted);
   - subsurface AI (the > €100M Mistral programme of Sept 2026).

   The draft never records existing capability. Its central thesis ("cross the OT data bottleneck by building a data fabric") proposes funding what the company is already funding.
2. **The financial model has arithmetic errors:**
   - **IRR is 46.8%, not 26.4%,** from the draft's own cash flows.
   - **The downside is sandbagged:** the scenario as described (gains at 40%, 12-month delay, cloud +20%) gives an NPV of about −€164M, not −€5.4M.
   - **The 3-year NPV of +€68.2M is not reproducible:** it relies on an undisclosed terminal value; without it, the 3-year NPV is −€15.8M.
3. **The portfolio canvas sums to 105%,** and the horizon split is ambiguous: "65% H1" includes the 20% platform line, and the 5% change-management line is outside the 65-20-10 split.
4. **The hurdle rate is built on an unsupported WACC.** The URD gives no WACC; the 4.2% is untraceable and far below the course examples (8.5–9%). The 6.8-point risk premium exceeds the course range of +2 to +6 points, although the draft attributes it to "the course".
5. **Most benchmarks are unnamed or unverifiable** ("Benchmark McKinsey Energy", "Gartner", "Wood Mackenzie", "BCG Tech Talent 2026"). Under AGENTS.md rule 3, an unnamed benchmark is not evidence. Every use-case gain therefore needs a new formula.
6. **Company figures are partly outdated.** The draft cites the URD 2023/2024: Digital Factory ~300 (now ~500 in France and India); production costs ~$5.5/b (now $5.0/boe); 15,000 stations and 60,000 EV chargers in Europe (actually ~13,000 stations in ~60 countries and ~90,000 chargers). It also uses € where TotalEnergies reports in $, with no exchange rate stated.
7. **Diagnosis and operating model were fixed before the evidence:** maturity scores without a method, the bottleneck, and "hub-and-spoke" as a formal recommendation. These are discarded as decisions; they remain candidate hypotheses for steps 09–10.
8. **The change-management design is the most reusable part:** failure modes, stakeholder classes, cadence, training tiers and kill criteria follow the course frameworks. Head-counts and budgets need recalculation.

## 2. Company facts

| Ref | Draft claim | Evidence | Class | Action |
| --- | --- | --- | --- | --- |
| L32 | Upstream breakeven < $30/b [URD] | Strategic objective "below $30/b"; organic cash breakeven before dividends $26.4/b in 2025 (SRC-002, pp. 13, 22) | Verified | Cite $26.4/b (2025) and the < $30/b objective |
| L33 | 34 GW renewables [URD] | 34.1 GW gross installed, end-2025 (CLM-006) | Verified | — |
| L33 | Integrated Power ROACE target ~12% | 12% by 2030 (CLM-009) | Verified | Add the year (2030) |
| L34, L97 | EU AI Act Annex III classes "energy infrastructure" and "critical industrial sites" as high risk | Annex III covers AI used as **safety components** in the management and operation of critical infrastructure, including the supply of gas and electricity. It does not cover industrial sites in general | To recalculate (restate) | Cite Regulation (EU) 2024/1689, Annex III point 2 precisely; register it before use |
| L93 | Upstream opex ~$5.5/b [URD] | $5.0/boe in 2025; $4.7/boe in Q3 2026 (CLM-005, SRC-005) | To recalculate | Update |
| L93 | $3.5–4bn/yr in Integrated Power [URD] | ~$4bn/yr low-carbon, incl. $3–4bn for Integrated Power (CLM-008) | Verified (restate) | Use "$3–4bn/yr Integrated Power; ~$4bn low-carbon" |
| L93 | 100 TWh net electricity by 2030 [URD] | 100–120 TWh/y by 2030 (CLM-009) | Verified | Use the range |
| L94 | Pangea 5, > €100M contract with Dell & NVIDIA at Pau "[URD/Presse 2024]" | Not in URD 2025. Trade press (2026) reports a > €100M Dell/NVIDIA contract, in service 2027; Pangea 4 dates from 2024 | Unsupported as dated | Register the official TotalEnergies page before use; fix the date |
| L94 | OT data "remain siloed per site in non-unified proprietary formats" | Consistent with the company's own aim of a foundation "which unifies our industrial data globally" (SRC-008), but the AspenTech and Cognite rollouts are under way (CLM-018, CLM-019) | Assumption | Restate as "unification in progress, completion 2027–2028"; test in step 09 |
| L95 | Digital Factory created 2020, ~300 engineers, "dozens of PoCs" | ~500 experts in France and India; nearly 100 solutions, 60% with AI; > 10,000 live models (CLM-016, CLM-017) | To recalculate | Update; note CON-001 |
| L95 | Group "struggles to industrialise beyond the pilot site" | No source supports or refutes it (CON-005) | Unsupported | Keep as `Unknown`; test with Q02 |
| L96 | Plant managers see algorithms as "black boxes" | No source | Assumption | Possibly a local observation: Vincent to record (Q11) |
| L97 | Cyber robustness (OIV sites, NIS 2) | URD describes cyber risk and blocked attacks (SRC-002, p. 136); OIV and NIS 2 status not verified | Unsupported (partly) | Cite the URD cyber risk factor only |
| L97 | No centralised, auditable model inventory | Not found either way (Q05) | Unsupported | Keep as `Unknown` |
| L101 | "23% of firms at this stage see significant P&L impact [Benchmark BCG/McKinsey]" | The 23% figure comes from the course deck (session 1, readiness stages), not BCG or McKinsey | To recalculate (re-attribute) | Cite the course deck |
| L107, L179 | 2.53 Mboe/d production; 1.53 Mb/d refined [URD 2025] | 2,529 kboe/d (CLM-005); refinery throughput 1,526 kb/d in 2025: France 470, rest of Europe 606, rest of world 449 (SRC-002, p. 55) | Verified | — |
| L114 | ~100,000 employees, 120 countries, 5 branches | 101,513; about 120 countries; 5 segments (CLM-001) | Verified | — |
| L115 | EU AI Act fines up to €35M or 7% of turnover | That ceiling applies to **prohibited** practices; high-risk obligations carry a lower ceiling (course session 2; Regulation (EU) 2024/1689, Art. 99) | To recalculate (restate) | Quote the tier that applies |
| L115 | SEVESO upper-tier sites | Plausible for refineries; not sourced | Unsupported | Find a source (French or EU SEVESO registry) or drop |
| L116 | AI talent concentrated in Paris (Digital Factory) and Pau (CSTJF) | Digital Factory is in France **and India** (SRC-002, p. 42); India AI centre (SRC-011) | To recalculate | Add India |
| L190 | 15,000 service stations and 60,000 EV charging points in Europe [URD] | Close to 13,000 stations in ~60 countries; close to 90,000 EV charging points (SRC-002, p. 13) | Discarded (wrong) | Use the URD figures |
| L203 | 34.1 GW and 48.1 TWh [URD 2025] | CLM-006 | Verified | — |
| L208 | 43.9 Mt LNG [URD 2025]; "~40 LNG carriers" | 43.9 Mt verified (SRC-002, p. 13); fleet size not sourced | Verified / Unsupported | Source the fleet or drop it |
| L213 | Group objective "near-zero methane emissions by 2030" [URD] | "aiming for near-zero methane emissions"; −80% 2020–2030 (SRC-002, pp. 36, 86) | Verified | Cite both |
| L231 | Northern Lights (Norway), Aramis (Netherlands) [URD] | TotalEnergies holds 33% of Northern Lights (operating); Aramis under study (SRC-002, pp. 34, 37, 86) | Verified | — |
| L293 | WACC 4.2% [URD 2024 / analyst consensus] | No WACC in URD 2025; no consensus source | Unsupported | Derive a WACC with a cited method (step 18) |
| L294 | Risk premium +6.8% "[Benchmark course Module 3]" | Course says +2 to +6 points over WACC, set by Finance | Discarded (misattributed) | Choose a premium within the course range and justify it |

## 3. Diagnosis and operating model

| Ref | Draft content | Class | Reason and action |
| --- | --- | --- | --- |
| L93–97 | Pillar scores 4.0 / 2.5 / 3.0 / 2.5 / 3.0 | Discarded | No scoring method or evidence; re-score in step 09 using S04–S06 |
| L100–103 | Stage 3 "Implementing", target stage 4 "Scaling" | Assumption | Plausible but must be argued in step 09. Evidence for: ~100 solutions "progressively being deployed". Against: > 10,000 live models, data platforms scaling |
| L106 | Bottleneck = real-time OT/IT data contextualisation | Assumption | One candidate among several. The company is already investing in it (CLM-018, CLM-019), so a "bottleneck" claim must show what remains blocked after those rollouts. Compare with value measurement (S06) and adoption |
| L114–116 | Three matching factors (size, regulation, talent) | Assumption (useful structure) | Reuse the structure in step 10; facts need the corrections in section 2 |
| L115 | "The federated model is strictly forbidden" | Discarded | Overstated, and decided before evidence |
| L118–146 | Formal recommendation: asymmetric hub-and-spoke by horizon; hub = Digital Factory + CSTJF | Discarded as a decision; kept as a candidate option | Ignores the existing OneTech Digital Line, which since Sept 2025 coordinates the branches' digital plans (CLM-015), and capabilities already inside the segments (CLM-027). Step 10 must start from the current structure |
| L148–160 | Forward Deployed Engineers; weekly business pair and finance pair | Assumption (design idea) | Reusable as options. The finance pair matches the course rule on benefits tracked by Finance |

## 4. Portfolio (11 use cases plus platform and enabler)

| Ref | Use case (draft horizon) | Existing capability the draft ignores | Figures | Horizon check | Class |
| --- | --- | --- | --- | --- | --- |
| L178 | H1.1 APM-SEVESO, refining predictive maintenance and energy (H1) | Cognite + AspenTech data foundation; "condition monitoring" named by the CDO (SRC-015) | −1.5% furnace energy "[McKinsey]"; −15% unplanned stops "[Gartner]"; +€45M/yr: no energy-bill base, unnamed benchmarks. "1.53 Mb/d on 5 platforms" mixes group throughput with 5 named sites | H1 correct | To recalculate. Strong candidate; rebuild from Equinor's maintenance benchmark (CLM-036, CLM-037) |
| L183 | H1.2 WellOps, ESP pumps (H1) | Cognite across all operated upstream assets (CLM-019) | +€35M/yr not derivable. 0.5% of 2.53 Mboe/d ≈ 12.7 kboe/d would be worth far more: the link between the 0.5% and the €35M is missing | H1 correct | To recalculate |
| L188 | H1.3 SmartStation & EV uptime (H1) | — | Network size wrong (see section 2); 91% → 98.5% uptime unsourced | H1 correct | To recalculate |
| L193 | H1.4 Contract & compliance Copilot (H1) | **Copilot for M365 deployed since 2024** (CLM-022) | 100,000 contracts, 600 lawyers, −40% review time: unsourced | H1 correct | To recalculate. Reposition as adoption and value capture on existing licences, not a new purchase |
| L202 | H2.1 PowerFlow trading (H2) | **Predictive Layer ML/AI trading insourced; Quadra forecasting** (CLM-027) | +€45M/yr "[Wood Mackenzie]"; implies ≈ 20 TWh × €2.2/MWh, volume not stated | H2 plausible | To recalculate. Must be incremental to the existing capability |
| L207 | H2.2 LNG marine optimiser (H2) | — | +€25M/yr unsourced; fleet unsourced | H1 or H2 (routing optimisation is proven technology) | Assumption |
| L212 | H2.3 AUSEA vision methane (H2) | **AUSEA drones since 2022 on all upstream sites; 13,000 sensors; Methane Tracking Center** (SRC-002, p. 29) | +€18M/yr unsourced | Course questions give H1: same customer, same model, proven technology | Discarded as framed (existing capability, wrong horizon); possible H1 extension |
| L217 | H2.4 Circular chemistry yield (H2) | — | +€20M/yr unsourced | H2 plausible (new feedstock process) | Assumption |
| L226 | H3.1 GeoMol SAF catalysts (H3) | Pangea 5 (already contracted) | No figures (fine for H3) | R&D discovery, not a new business model in itself; H3 only if tied to a new market. SAF production already exists | Assumption. Restate the option value and the new market |
| L230 | H3.2 Subsurface PINNs for CCS (H3) | **Mistral subsurface frontier-model programme, > €100M, 3 years** (CLM-021) | −70% 4D inversion time, unsourced | Tool improvement, so H2; not a new business model | Discarded as framed (overlaps an existing programme) |
| L234 | H3.3 Autonomous VPP & V2G (H3) | 6.0 million power clients (SRC-003, p. 9) | 500,000 assets, 10,000-vehicle proof of concept: unsourced | H3 plausible (new revenue model) | Assumption. Strongest H3 candidate |
| L245 | PLAT data & MLOps platform, 20% | **Cognite (upstream, 2025–2028) and AspenTech (industrial sites, 2025–2027) already funded** | 20% of budget | Course rule: fund each foundation with its first use case; a standalone 20% line breaks it | Discarded as framed; keep only the incremental slice tied to a use case |
| L257 | ENAB AI Academy & change, 5% | Digital Accelerator GenAI training already running (SRC-002, p. 388) | 5% = €9.75M, but the change line in the budget table is €25M (12.8%) | — | To recalculate |

**Portfolio inconsistencies:**
- **The canvas sums to 105%:** platform 20 + H1 45 + H2 25 + H3 10 + enabler 5. The memo's "65% H1" equals the H1 lines (45) plus the platform (20), so the platform is counted as H1 while the canvas lists it as a separate "Socle".
- **Use-case gains do not reconcile with the DCF.** H1 adds up to €115M/yr and H2 to €108M/yr, so €223M/yr at M24–M36. The DCF shows €142M in year 3 and €210M in year 5, and the memo claims "€142M recurring EBIT at M36". No ramp-up or bridge explains the difference.
- **The 65-25-10 deviation is justified only by a goal** ("accelerate flexibility and trading"), with no trigger. The course requires a trigger and a reason.

## 5. Financial model

| Ref | Draft figure | Recomputed | Class | Note |
| --- | --- | --- | --- | --- |
| L271–282 | Capex/opex table: €195M over 3 years (capex 85 / opex 110); €288M over 5 years | Rows and columns add up | Verified (arithmetic) | Amounts are assumptions: no cost basis per line |
| L285–287 | Tranches 65 / 70 / 60 | Matches the table | Verified (arithmetic) | — |
| L300–305 | DCF costs 65, 70, 60, 47, 46, 46 at t = 0…5 | Year 1 of the envelope is placed at t = 0, and a **sixth year of cost (−46) is added**; total cost 334 vs the 5-year envelope of 288 | To recalculate | Align the DCF years with the envelope years |
| L300–305 | Gains 25, 85, 142, 185, 210 | No link to use-case formulas | Assumption | Rebuild bottom-up (step 18) |
| L311 | NPV (5 years) +€173.1M at 11% | +€173.1M (reproduced) | To recalculate | The arithmetic holds, but the inputs (costs, gains, rate) are not supported |
| L312 | NPV (3 years) +€68.2M "including a normalised terminal value" | −€15.8M without terminal value; the terminal value is never shown | Unsupported | Remove, or show the terminal-value formula |
| L313, L61 | IRR 26.4% | **46.8%** from the same cash flows | Discarded (wrong) | The headline hurdle cushion (+15.4 points) is wrong too |
| L315 | Simple payback 2.9 years (2 + 85/95) | 2.89 (reproduced) | Verified (arithmetic) | Inputs unsupported |
| L316 | Discounted payback 3.2 years | 3.17 (reproduced) | Verified (arithmetic) | Inputs unsupported |
| L318 | ROI 93.7% = (647 − 334) / 334 | Reproduced | Verified (arithmetic) | Uses the 6-year cost base |
| L325–330 | Downside −€5.4M (5 years), base +€173.1M, upside +€295M; probabilities 20 / 60 / 20 | Expected values 64.4 (3 years) and 161.8 (5 years) are reproduced. **The downside as described gives about −€164M** | Discarded (downside sandbagged) | Course pitfall 5. The −€65M "loss cap" claim also needs proof that kill criteria actually stop spending |
| L293–295 | Hurdle 11% = WACC 4.2% + 6.8% | See section 2 | Discarded | Rebuild: cited WACC + premium of 2–6 points |
| L338–340 | Inaction, refining: 1.53 Mb/d × 365 × $0.25/b = $139.6M/yr | Arithmetic holds; the $0.25/b gap is unnamed; it applies a "European" margin gap to all refineries (Europe = 1,076 kb/d); 3-year total "−€150M" not reproducible | Unsupported | Rebuild with a named source or a transparent assumption |
| L342–344 | Inaction, power: 31 TWh × €1.5/MWh = €46.5M/yr | Arithmetic holds. €1.5/MWh "[CRE/EPEX]" not found. It assumes no algorithmic trading, yet the company already runs it (CLM-027). The 3-year total of −€90M is not 3 × 46.5 | Unsupported | — |
| L346–347 | Inaction, talent: −€70M | No formula, unnamed benchmark | Unsupported | — |
| L348 | Total inaction −€310M | Sum holds (150 + 90 + 70) | To recalculate | **Double-counting risk:** PowerFlow claims €45M/yr of gains from removing imbalance penalties, and the inaction case counts the same penalties as a loss. AGENTS.md rule 7 |
| — | Currency | € throughout, while TotalEnergies reports in $; no exchange rate | To recalculate | State a dated exchange rate |
| L279 | Talent: 60 experts for €35M over 3 years | ≈ €194k per FTE-year (calculation) | Assumption | Plausible fully loaded cost; source a salary benchmark |

## 6. Change management and governance

| Ref | Draft content | Class | Note |
| --- | --- | --- | --- |
| L67–70, L356–361 | Four failure modes with signals, mitigations, owners | Assumption (reusable) | Matches the course framework. Owners must map onto the real organisation (OneTech, CDO, CHRO, branch EVPs) |
| L365–390 | Stakeholder classes, inverted cadence, messengers | Assumption (reusable) | Matches the course; adjust to the real organisation |
| L77, L397–402 | Training tiers 95,000 / 3,500 / 250 | Assumption | 95,000 vs 101,513 employees. Must build on the existing Digital Accelerator programme (SRC-002, p. 388) |
| L69, L409–411 | Kill criteria at M12 (adoption < 45%), M18 (gain < €10M), M24 (run cost > 70% of value) | Assumption (reusable format) | Correct structure (metric, threshold, date, owner, action). Thresholds need justification |
| L360, L431 | Nanterre 2025 case; early CSE consultation | Verified (course session 4) | — |
| L422 | "70% of value lies in people" | Verified (course: BCG 10-20-70) | — |
| L428–429 | "Shell and BP buy off-the-shelf from Microsoft and Palantir" | Unsupported (partly) | Shell uses C3 AI on Azure (vendor sources, S06); the bp–Palantir agreement was not read (Q13) |

## 7. What to carry forward

- **Ideas for the step 08 long list,** each to be re-costed with an "existing capability" field:
  - H1.1 refining maintenance and energy;
  - H1.2 well surveillance;
  - H1.3 EV charging uptime;
  - H1.4 Copilot value capture;
  - H2.1 trading (incremental only);
  - H2.2 LNG routing;
  - H2.4 circular chemistry;
  - H3.1 SAF catalysts (with a market thesis);
  - H3.3 VPP / V2G.
- **Dropped as framed:** H2.3 methane (exists, H1); H3.2 subsurface CCS (overlaps the Mistral programme); a standalone PLAT platform line; "Pangea 5 extension" capex.
- **Frameworks and formats** reusable after correction: the sequencing-canvas columns, the capex/opex table layout, tranche logic, kill-criteria format, the change-management plan.
- **Numbers to rebuild from scratch:** every use-case gain, the WACC and hurdle, the DCF timeline, scenarios, and the cost of inaction.
