# Audit of Steps 08–10: TotalEnergies AI transformation

## Executive verdict: CRITICAL REBALANCING REQUIRED

The evidence discipline is good and the register is worth keeping. The three things the pitch depends on are not ready: the value numbers, the bottleneck and the operating-model ask.

**The 5-year NPV will not restore the course's return mix; it makes the mix more H1-heavy.** Don't build the pitch on the hope that H2 and H3 will dominate.

**Limits of this audit**
- I could not open the URD, Factbook or lecture PDFs: the reader reported the URD as password-protected, and Python and the PDF parser needed approval. URD page citations are taken from the register and syntheses, not re-verified, and Q19 (drilling share) stays open.
- I did not run `git fetch`, so `02007db` is the local copy of `origin/main`.
- The cheat sheets weren't attached, so I used those in `course/exam/`.
- I changed no files.

## Four premises to correct

| Premise | Finding |
|---|---|
| P03 is "automated deepwater drilling" | It is "drilling performance and well-planning optimisation" (`long_list.md:48`). Automation would conflict with CLM-026 and rejected idea R08. |
| H2 is worth $29.5M | $9M of that is P10, whose 3–15 range is the **yield** lever, labelled H1. Real H2 is P09 at $20.5M, and P09 answers N, N, mostly, N, which isn't the H2 pattern. |
| H3 has "$0 return" | It is **not estimated** ("option value"). The 89% is a share of what was quantified, so H3 is excluded by construction. |
| $276.5M is a "1-year snapshot" | It is a full-scale run-rate that no year actually delivers. The list also says "Do not add these rows up" (`long_list.md:60`). I add them below only to test your claim. |

## Step 08: long list and horizons

### P03 should not stay in H1

- **Its own tags contradict H1.** It has "Very high" uncertainty, "dedicated drilling AI unknown", and a hard dependency on drilling data being live on Cognite.
- **The evidence is thin.** BP's well tool has no value figure (CLM-068), and the IEA's "up to 10%" is a scenario for new facilities only (CLM-044).
- **Q4 is measured inconsistently across the list.** It times first value at one pilot, while the dollar column is full scale. P01 has the same gap: first value in 6–12 months, scale-up in 24–36.
- **Recommendation: split it into slices, as the course allows.**
  - H1: post-well analytics on existing data.
  - H2: integrated well-planning workflow, which changes the process as the course's claims-agent example does.

### What reclassifying does

| Midpoint value, $M | H1 | H2 |
|---|---|---|
| As stated, run-rate | 247 (89.3%) | 29.5 (10.7%) |
| P10 yield corrected to H1 | 256 (92.6%) | 20.5 (7.4%) |
| P03 moved to H2 | 131.5 (47.6%) | 145 (52.4%) |
| Both changes | 140.5 (50.8%) | 136 (49.2%) |
| **5-yr PV of benefits, as stated** | 93.3% | 6.7% |
| **5-yr PV, P03 moved to H2** | 60.1% | 39.9% |
| **5-yr PV, both changes** | 63.2% | 36.8% |

The PV rows use my assumptions: a 12% rate and ramps of 25/70/100/100/100% for H1 and 0/20/50/85/100% for H2.

Moving P03 changes labels, not dollars. It makes H2 about 80% one row built on two assumed inputs.

Being honest about the delay cuts P03's NPV from about $309M to $185M.

### The return-mix paradox

- **Use a 5-year NPV.** It is the right frame for capital budgeting and is what Step 18 requires.
- **It cannot deliver "H3 earns 70%".** That would need an H3 run-rate of about **$1.55bn a year by year 5**, assuming a 50% ramp in Y4 and 100% in Y5. That is 61% of Integrated Power's entire FY2025 CFFO, from two projects costing $6.2M.
- **The roadmap already rules this out:** the course split "is not a forecast for our portfolio" (`roadmap.md:27`). Inventing H3 cash flows would also break AGENTS.md rule 7.
- **What to say instead:** "Within five years, returns are H1-heavy by design. H2 is judged on NPV and adoption. H3 is judged on learning gates and sits outside the NPV." The course supports this: never judge H3 by H1's ROI.
- **The capital mix is defensible.** Excluding E01 it is 69/12.5/19 as stated, or 59/22/19 with P03 in H2. State the trigger for any deviation from 70-20-10.

### What the CEO will attack

1. **Costs and benefits cover different scopes.** This is the most serious error.
   - P03's cost covers 4 fields, but its benefit uses 100% of E&P net investment. Each 10 points of base covered is worth about $11.6M a year at midpoint.
   - P03 pays back 106× its average annual cost, and breaks even at a saving of **0.018%** of the base.
   - P01 says it "counts only sites not yet covered" (`:117`), then applies the formula to all 1,526 kb/d (`:120`), with rollout to 8 sites.
   - P09 applies to all LNG sales despite "controlled ships only".
2. **The base is wrong.** Net investments normally include acquisitions and disposals, so check the definition at URD p. 37. Non-operated share is also unknown (Q18).
3. **Peer sanity check.** Equinor reports $130M of AI value for 2025, partners included, after six years. P03's midpoint alone is 89% of that. Normalisation is still open (Q15).
4. **Double counting.** P03 and P06 are 54% of the midpoint total and both sit against the $12.5bn plan. P06 is "not usable" by its own note.
5. **Costs are probably low.**
   - The rates are French market medians, not oil-major pay.
   - If only 45–60% of TCO is visible (course figure), $34.9M could be $58–78M.
   - It also looks small: $34.9M is under a third of the Mistral programme alone. Expect "why is this on my agenda?"
6. **H3 is weak.**
   - P12 changes neither customer nor business model.
   - P11 fails Q3: virtual power plants are commercial, including Shell's Next Kraftwerke (from memory; register it before citing).
7. **A2 can be tested now.** E&P cash flow per barrel is about $16.9/boe, or $22/boe including LNG, on S04 figures. That supports the lower half of $15–30.

## Step 09: Alexandre's B2/B4 vs Vincent's Pillar 4

**Neither survives as written.** Vincent has the better causal theory and Alexandre has the better evidence discipline.

| Test | Alexandre: B2 + B4 | Vincent: Pillar 4 |
|---|---|---|
| One-line kill | "We track value internally; you've only read our filings." CLM-029 is `Unknown`. | "One person, one year, one retail subsidiary." |
| Evidence | Almost entirely non-disclosure, which S06 itself says doesn't prove lower value | CLM-072, a conditional risk factor (CLM-014) and a survey of other firms |
| Internal flaw | Value tracking belongs to the pillar scored **highest** (AI strategy and experience, 3.5), yet is named the bottleneck under Governance | Central triage is the core complaint, but it is measured as `T_backlog` and credited to Hypothesis C, which is "refuted" (`:190`, `:232`) |
| Selection bias | Defines a bottleneck as what a Comex decision can unblock. Cheap to fix doesn't mean binding. | Adds skills + culture (33%) to beat data + infrastructure (30%), while refuting a talent shortage (`:105`, `:190`) |
| Scale | E01 at $1.64M over 10,000 models is about **$164 per model** for owner, baseline, risk tier and limits | M&S is 3.6% of net investment and has **no project** in the long list |

**Further points on Vincent's draft**
- A 2.0 maps to the draft's own "Planning" anchor, which is not credible with more than 10,000 live models. Alexandre scores this pillar 3.
- CLM-072 still feeds group-level conclusions (`:89`, `:120`, `:144`), which fails the Step 09 acceptance criterion.
- Round 5 of the Opus review already flagged several items that remain:
  - the summed use-case range, now $94–459M (`:209`);
  - Goldratt attributed to Session 1 (`:15`, `:152`);
  - "instances" presented as fact (`:23`, `:91`, `:142`);
  - `SRC-015` tagged `[Fact]`.
- The Month 3 gate can't see full cycles, because first value comes at 3–12 months. Six pilots is also too few to act on a 10% margin.

### Is B2 a physical constraint?

No. Missing value tracking doesn't slow delivery by itself. It does disable capital allocation: no kill decisions, no reallocation, and no way to tell whether more deliveries produce money.

### Your proposed unification

It is cohesive but not unassailable, and two causes break the "name the bottleneck pillar" requirement. I would use a tighter version:

> **Binding pillar: Organization and culture, specifically that no business P&L owner is accountable for deploying an AI solution and signing its benefit.**

- Vincent's passive business and Alexandre's missing value figure are then two symptoms of one cause.
- It matches the course definition of an operating model: decision rights, funding routes and control points.
- It has public support:
  - the Digital Line "coordinates" (CLM-015);
  - funding and decision rights are undisclosed (CLM-030);
  - about 100 solutions are "progressively being deployed" (CLM-017);
  - the Board is still assessing AI's impact (CLM-025).
- **Alexandre ranked this cause fourth (B6), and Vincent lists only `T_business`.** Yet all of Step 10 solves it.
- E01 becomes the control mechanism, funded with the first use cases.
- Present it as a hypothesis the CEO can confirm in 90 days. Keep Argedis to one illustrative sentence.

## Step 10: operating model

**Position: hub-and-spoke is the operating model, and the trio is the delivery unit inside each spoke.** They aren't alternatives. The course rule fits: centralise platform and governance, distribute delivery.

| Role | Home | Accountable for |
|---|---|---|
| Lead data scientist | Digital Factory, seconded | Model standards and reuse |
| Data engineer | Branch | The data slice for that use case |
| Business champion | Branch P&L, ring-fenced time | Adoption and signing the benefit |
| Digital Line | Hub | Platforms, register, risk tiers, vendors |
| Group Finance | Central | Baselines and releasing tranches |

Vary it by segment. Integrated Power already has embedded ML, so don't impose trios there. M&S sits outside the Cognite and AspenTech scope as described, so it needs a data slice first.

**Problems in Alexandre's draft**
- **"Formalise today's structure" invites "so you're keeping my org chart?"** Low disruption is being used as a reason, and the existing hub-and-spoke is itself inferred.
- **100/60/40 is Microsoft's pattern applied without knowing current funding (CLM-030).** Across all 13 candidates, branches would pay about $12M over three years, or about $2.4M per segment. That isn't skin in the game. Make branches fund champion time from day one.
- **The decision tree is misapplied.** "Yes" on regulation ends at "CoE or strong hub", and the draft then continues down the other branch. Say explicitly that regulation is mixed by use case.
- **Section 5 is stale.** It says Argedis isn't recorded, but Q11 is closed on `dev_vincent`.

**Problems on Vincent's side**
- The trio exists only as a line in Q11, with no document, cost or decision rights.
- The cash cost is small: about $338k per full trio-year at long-list rates. The real ask is scarce expert time.
- The long list budgets just 0.25 expert-year per site at rollout, exactly where Vincent says the constraint binds. Doubling it on P01 costs only about $172k.
- 13 projects over three years adds about 4 a year, against roughly 18 solutions a year historically. Nothing yet shows the design raises throughput.

## Merge blockers

- **`CLM-072` means two different things:** the AI Act timeline on `origin/main`, and Argedis on `dev_vincent`. The register forbids recycling IDs. Renumber before merging, because every citation changes meaning.
- **CLM-072 (Argedis) is marked `Verified`** on the observer's own word. Mark it as attested only.
- **Vincent's draft lists Alexandre as co-author** of a diagnosis Alexandre's own draft contradicts.
- **Step 09 now has two outputs for one issue,** which breaks AGENTS.md rule 6.

## Recommendations for Steps 11–15

| Step | Case | Why |
|---|---|---|
| 11 | Adopt the single thesis above; merge the two Step 09 files | One bottleneck, one owner, one issue |
| 12 | P01, H1 | The only value with a peer cross-check (Equinor, about $20M a year on predictive maintenance) |
| 13 | P03, split, scope-matched, H2 lead | Largest value, but only once rebuilt |
| 14 | P11, H3, with learning gates | The only real business-model change; check Q3 and existing flexibility offers |
| 15 | P05 + E01, H1 quick win | Year-one proof that also tests the ownership thesis |

P06 stays out until Q17 is answered, and P12 goes to reserve. Add one real H2 candidate where the customer changes, such as P08 recast as a paid service.

**The question that can sink the pitch:** "Your best project pays back 100 times over and breaks even at 0.018% of my E&P spend. If it's that easy, why haven't my drilling teams done it?" No draft answers this yet.

**Next action:** tonight, rebuild P03 first, with costs and benefits on the same fields, using the URD's E&P cost tables and the Factbook to close Q19. It drives 42% of the value and the whole horizon debate.
