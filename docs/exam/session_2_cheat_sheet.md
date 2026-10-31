# AI Transformations — Session 2 Cheat Sheet: Operating model and portfolio

As of 31 Oct 2026 · Session of 12 Oct

The course logic runs in order: diagnose readiness → pick the operating model → sequence the portfolio → prove it financially → manage the change. This session covers the second and third steps; see [session_1_cheat_sheet.md](session_1_cheat_sheet.md) for the exam format and readiness.

## 1. AI operating models: who builds, who decides, who is accountable

**Rule of thumb: centralise the platform and governance, distribute delivery.** No model wins everywhere: each one trades speed, control and cost.

**Definition:** an AI operating model is the decision rights, funding routes and control points that determine how a firm builds, approves and runs AI. It has four parts: talent placement (where AI people sit), platform and tooling (who owns the stack), governance and risk (who sets and enforces rules), and funding (who pays, who says yes). A CoE is the *hub* of hub-and-spoke, not a synonym for the whole operating model.

Why it matters (McKinsey 2025): 99% of firms struggle to scale AI, 39% see any measurable EBIT impact, 60% lack a clear implementation strategy, only 33% feel they have enough AI talent, and only 6% are "high performers".

### The three archetypes (a spectrum, not three boxes)

| | Centralised CoE | Hub-and-spoke | Federated |
| --- | --- | --- | --- |
| How it works | One central team builds, deploys and runs everything; BUs submit requests | Hub owns platform, rules, model inventory, vendors; spokes in BUs pick and deliver use cases | Each BU runs its own AI team and tools; light shared standards |
| Who builds | The CoE | Embedded spokes | Each BU |
| Speed | Slow at scale | Fast on shared rails | Fastest |
| Risk control | Strongest | Strong | Weakest |
| Cost | High talent need, small pooled team | Core + embedded | 2–3× platform spend by year two |
| Failure mode | Bottleneck, ivory tower, ownership vacuum, talent leaves, shadow AI | Coordination drag, unclear decision rights | Sprawl, duplicated tools, no model inventory, governance blind spot until an incident |
| Best fit | Early maturity, heavy regulation, scarce talent | Enterprises past pilots | Diverse conglomerates, mature, light regulation |
| Example | JPMorgan Chase (ML CoE + AI/ML Council) | Airbnb (central for careers and standards, embedded in product) | Hard to run safely in banking or healthcare |

A CoE's 8 functions: strategy and responsible AI, skills, lead pilots, standards, intake (one front door), reusable assets, measure and report, optionally run shared AI services. It needs an executive sponsor, a steering committee and a leader accountable for outcomes.

### Matching the model: three factors

- **Size and complexity**: startup → embedded; mid-size single business → central CoE; large multi-BU → hub-and-spoke; conglomerate → federated with thin guardrails. Pure hub models struggle beyond about 4 BUs.
- **Regulatory exposure**: high regulation → CoE or strong hub. "An auditor won't accept four different answers from four BUs." Over half of 16 large banks chose a centralised approach.
- **Talent footprint**: scarce → concentrate in a CoE; deep talent in BUs → spokes or federated; spread across regions → hub with regional spokes; low literacy in BUs → keep delivery central and build literacy.

### Decision tree: regulation decides first, then market spread, then maturity

```
High regulatory exposure?
├── yes → CoE or strong hub
└── no  → Several BUs in distinct markets?
          ├── no  → Centralised CoE
          └── yes → Mature, with a strong shared platform?
                    ├── yes → Federated on shared rails
                    └── no  → Hub-and-spoke
```

The slide's decision tree asks three questions in order. Regulation overrides everything, and federating needs a mature shared platform first.

### Evolution: the right model today is rarely right in three years

The path runs experiment (siloed pilots) → centralise (CoE builds foundations) → hub-and-spoke → federated or advisory, once governance is embedded in the platform. Signals that it is time to move: approval delays, knowledge bottlenecks, the CoE and product teams arguing over priorities. **Maturity is the gate**: federating too early gives the look of autonomy and the reality of unmanaged risk. Revisit the model once a year.

Other drivers: inside the firm (maturity, talent, number of BUs, literacy, platform, C-suite sponsorship, governance, culture; firms overstate their own maturity) and outside it (regulation, market speed, talent scarcity, vendors, trust and cost pressure).

### EU AI Act timeline

| Date | What applies |
| --- | --- |
| 2 Feb 2025 | Prohibitions and AI-literacy duties |
| 2 Aug 2025 | General-purpose AI model rules |
| 2 Aug 2026 | Article 50 transparency duties; enforcement begins |
| 2 Dec 2027 | Annex III high-risk uses: hiring, credit, education |
| 2 Aug 2028 | Annex I regulated products |

Maximum fine: EUR 35M or 7% of global turnover. Whatever the model, you need a central model inventory, documentation, logging and human oversight.

## 2. Sequencing the AI portfolio

**Four moves: place, allocate, connect, source.** Two rules hold throughout: imbalance fails both ways, and dependency claims are often excuses. The hook: you have 40 ideas and budget for 8. Only 11% of leaders say they are in the "reinvention" horizon (McKinsey, July 2026).

### Place: the Three Horizons (Baghai, Coley and White, 1999)

| | H1: Optimise | H2: Innovate | H3: Transform |
| --- | --- | --- | --- |
| Goal | Do the current business better | Do what you do today differently | New markets, mindsets, models |
| Time to value | Under about 12 months | 1–3 years | 3+ years, option value |
| Risk | Low: proven tech | Medium: evolutionary change | High: revolutionary change |
| KPI | Cost, productivity, margin | Growth, adoption, NPV | Learning, milestones, options |
| Management | Operate and optimise | Invest and scale | Explore, stage-gate, kill fast |
| AI examples | Enterprise chat, automating a factory process | Agents, fine-tuned models | New AI-native business models |

- Run all three **at the same time**, never in turn. The time axis shows ventures maturing H3 → H2 → H1.
- **H1 shouts loudest**: its urgency easily crowds out H2 and H3.
- **Judge each horizon by its own KPIs: never judge H3 by H1's ROI.**

**Four placement questions**: Q1 does it change the customer? Q2 does it change the business model? Q3 is the tech proven? Q4 is time to value under 12 months? Typical answers: H1 = No, No, Yes, Yes. H2 = Yes, No, Mostly, No. H3 = Yes, Yes, No, No.

**Misplacement traps**: an AI assistant (Copilot) rollout is H1, however new it feels. A website chatbot is H1 unless it creates a new revenue model. "New to us" is not H3: novel tech on an unchanged model is H1 or H2. One platform can serve several horizons, so place each slice.

### Allocate: the 70-20-10 rule (Nagji and Tuff, HBR 2012)

Spend about 70% on H1 core, 20% on H2 adjacent, 10% on H3 transformational. **Returns run the other way**: the 10% on H3 earns about 70% of returns. For H3 to work, give it separate talent, a separate budget, no forced pipeline funnel, and early non-economic metrics.

| Trigger | Move | Example split H1-H2-H3 |
| --- | --- | --- |
| Stable core, normal pace | Baseline | 70-20-10 |
| Fast-moving or AI-disrupted industry; disrupted core | Re-weight to H2 and H3 | 50-30-20 |
| Weak cash, turnaround, regulated or mission-critical | Re-weight to H1 | 80-15-5 |
| Startup or digital native | Can invert | H3-led |

**Deviate on purpose, never by drift.** Write down the trigger and the reason. **Rule 1**: an H1-dominated portfolio fails strategically (you optimise yourself into irrelevance: margins up, relevance down). An H3-dominated portfolio fails financially (moonshots with no P&L impact; the CFO cuts the budget).

**Six signs of drift**: no H3 beyond pilot, pilot purgatory, H2 starved, H1 savings not reinvested in H2 and H3, a split nobody chose, one KPI for all horizons.

### Connect: the dependency graph

Four steps: list nodes (initiatives and foundations: data, governance, skills, identity), draw edges only where B truly requires A, find the critical path (the longest chain sets the earliest date for H2/H3 value), then thin-slice (build the minimum viable foundation the first use case needs).

**A foundation with no use case attached is just a cost centre: fund each foundation with its first use case.**

**Rule 2: classify every dependency claim.** Hard = technical, B cannot run without A, so thin-slice A. Soft = a preference, easier with A but workable without. Political = delay, budget protection or risk avoidance, so name it. Five challenge questions: hard, soft or political? Can a thin slice unblock it? What would we do if it didn't exist? Who gains from the delay? What does waiting cost, and who owns that cost?

### Source: build, buy or blend (Gartner, 2025)

| Driver | Horizon | Sourcing | Why |
| --- | --- | --- | --- |
| Defend: augment productivity | H1 | Buy | AI embedded in your SaaS: fast and proven, but rivals buy it too |
| Extend: transform processes | H2 | Blend | Foundation model + your proprietary data + an integrator |
| Upend: disrupt markets | H3 | Build (or partner, minority stake) | The differentiating core |

**Build only where it differentiates and you own unique data or skills.** Over-buy and you look like your competitors; over-build and you pay for what is being commoditised.

Decision matrix: score 6 factors from 1 (buy) to 5 (build): differentiation, proprietary data, time to market, skills available, regulation and sovereignty, total cost of ownership. Weight them, then average: under 2 = buy, 2–4 = blend or partner, over 4 = build. Sovereignty at 5 can force a build on its own.

**The sequencing canvas** has one row per initiative: horizon, capital %, depends on, build/buy/partner, first milestone, owner and date. The capital column sums to 100%, and dependencies name a slice, not a lake.

**Six common mistakes**: calling a Copilot rollout H3, a split that happened by drift, foundations with no use case, accepting every dependency claim, building what is being commoditised, the same KPI for every horizon.

## 3. Spotting planted flaws in a strategy memo

For each claim in the memo, ask which course rule it breaks, then name the rule in your answer. This checklist is built from the course rules above. It is not an official list.

| Flaw you might see | Why it is wrong | Rule to cite |
| --- | --- | --- |
| A Copilot or chatbot rollout called "transformational" or H3 | Same customer, same model, proven tech: H1 productivity | Four placement questions |
| H3 bets judged on year-one ROI | Wrong KPI: H3 earns learning and milestone metrics first | Judge each horizon by its own KPIs |
| Nearly all budget on H1, or on moonshots | Fails strategically, or fails financially | Rule 1: imbalance fails both ways |
| A split off 70-20-10 with no stated reason | Drift, not a choice | Deviate on purpose: name the trigger |
| "Nothing until the data lake is finished" | A soft or political dependency accepted as hard | Rule 2: classify, then thin-slice |
| A data platform funded with no use case | A cost centre with no value case | Fund each foundation with its first use case |
| Federated model for an early-maturity, heavily regulated bank | Governance blind spot; auditors want one answer | Regulation factor; maturity is the gate |
| A central CoE for a mature 15-brand conglomerate | Bottleneck and shadow AI | Size factor; pure hubs struggle beyond about 4 BUs |
| "The CoE is our operating model" | The CoE is only the hub | Definition of an operating model |
| Building commodity AI in-house, or buying the differentiating core | Paying for what is commoditised, or looking like rivals | Buy to defend, blend to extend, build to upend |
| "We are scaling" with 12 siloed pilots on different tools | Really exploring or implementing, with an operating-model problem | Readiness stages; operating model definition |
| An AI hiring or credit tool with no human oversight or logging | High-risk under Annex III from 2 Dec 2027 | EU AI Act |
| The operating model is fixed for good | The right model today is rarely right in three years | Revisit the model yearly |

## 4. Cases and numbers worth citing

| Fact | Figure | Source |
| --- | --- | --- |
| Firms struggling to scale AI | 99% | McKinsey 2025 |
| Firms seeing any measurable EBIT impact | 39% | McKinsey 2025 |
| AI "high performers" | 6% | McKinsey 2025 |
| Leaders in the "reinvention" horizon | 11% | McKinsey, July 2026 |
| Firms skipping a software purchase because teams can build with AI | 32% | McKinsey 2025 |
| CIOs running 10+ AI projects | 29% | Gartner 2025 |

Examples: **JPMorgan Chase** (centralised ML CoE + AI/ML Council), **Airbnb** (moved from central data science to hub-and-spoke).

## 5. Practice questions with answers

These are suggested answers that apply the course frameworks.

1. **Place these: sales-rep AI assistant, FAQ chatbot, end-to-end claims agent, product configurator, pay-per-km mobility service, minority stake in an AI biotech.**
    - H1, H1, H2, H2, H3, H3. The first two use proven tech on an unchanged model. The claims agent and configurator change the process or customer experience, not the business model. The last two create new revenue logic or buy options.
2. **Pick an operating model: EuroBank (40,000 staff, 5 BUs, heavily regulated, scarce talent, early maturity).**
    - Centralised CoE or a strong hub. Regulation, scarce talent and early maturity all point to central control. Plan the move to hub-and-spoke once governance lives in the platform.
3. **RetailCo (15 diverse brands, 30 countries, fast market, talent in the brands, mid-high maturity).**
    - Federated on shared rails if a strong shared platform exists; otherwise hub-and-spoke first. Low regulation, distinct markets and distributed talent favour delivery in the brands.
4. **ScaleUp (SaaS, 300 people, AI-native squads, low regulation).**
    - Embedded or federated: small, AI-native, low regulation. Add light coordination as it scales.
5. **Maison Lumière's CIO says: "No personalisation, service agent or pricing until the data platform is finished. That's 24 months." Respond.**
    - Mostly soft or political, not hard. Each use case needs a **slice** of data (customer data for personalisation, the knowledge base for the service agent, a forecast for pricing), not the whole platform. Propose a thin slice for one use case to deliver value this year, and fund the platform alongside it. Ask who gains from the delay and what waiting costs.
