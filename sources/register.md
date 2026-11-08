# Evidence register

This file indexes sources, claims, and unresolved evidence. Add an entry when a source or material claim is first used. A synthesis in `sources/synthesis/` may explain evidence but never replaces an original document. An AI answer is a research lead until its underlying source has been read.

## Evidence classes and status

| Class | Use | Minimum support |
| --- | --- | --- |
| `Fact` | A statement directly supported by an original, attributable source. | Source ID, precise page/section or stable URL, document date, observed period, organizational/geographic scope, and limits. |
| `Calculation` | A result derived from stated inputs. | Input claim IDs, formula, units, period, scope, and reproducible arithmetic; label assumed inputs. |
| `Assumption` | A proposed value or causal premise that has not been observed. | Rationale, plausible range, sensitivity or test, and owner of verification. Never present it as a company result. |
| `Local observation` | First-hand experience, including Vincent's Argedis account. | Observer, entity, approximate period, what was actually seen, and what would test generalization. |
| `Unknown` | A consequential question without adequate evidence. | Exact question, why it matters, source or person to check, and decision affected. |

Use status `Pending` until the original evidence has been checked; `Verified` only after checking the document, location, date, period, and scope; `Disputed` when credible sources conflict; `Superseded` when replaced by a newer version; `Rejected` when unusable. A source can be verified while an inference drawn from it remains pending or rejected.

## Citation and calculation conventions

- Give each original source a stable `SRC-###` ID and each material statement a `CLM-###` ID. Never recycle IDs. Cite a PDF as `SRC-###, PDF p. N`; add the printed page number if different. Cite a web source with its exact URL and heading or table; record access date. A bare homepage or search result is insufficient.
- Distinguish **publication date** from the **period measured**. Preserve reported currency, scale, units, denominator, geography, business unit, and whether a figure is actual, forecast, or target. Note any currency conversion and its dated rate.
- For calculations, write the formula and the source or claim ID of every input. State whether a value is annual or cumulative, gross or net, nominal or real, and whether a baseline already contains another claimed benefit. Report a range when an input is uncertain.
- Record what a source actually supports and what it cannot establish. A group-level statement cannot establish a subsidiary-level outcome, or the reverse.
- When sources conflict, keep both claim rows, set status `Disputed`, and add a row in the contradiction log. Do not silently choose the more convenient figure. An unresolved issue stays `Unknown` in the report and decision work.

## Source index

| ID | Status | Organization; exact title | Published / version | Original URL or local file | Locations used | Coverage and limits | Checked on / by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-001 | Pending | TotalEnergies; organization chart (exact title to verify) | To verify | `sources/primary/organigramme_compagnie_fr.pdf` | To record | Organizational structure as of the document date; does not itself establish AI decision rights. | Pending |
| SRC-002 | Verified | TotalEnergies; *Universal Registration Document 2025, including the Annual Financial Report* (English translation) | Filed with the AMF 27 Mar 2026; FY2025 | https://totalenergies.com/system/files/documents/totalenergies_universal-registration-document-2025_2026_en.pdf (19.5 MB, 666 pp.; not stored in repo) | PDF pp. 6, 13, 15, 29, 37, 39–43, 49–50, 74, 109–110, 136, 138, 211, 223, 225, 276, 282, 284, 388 | Group annual report; strongest source for organisation, R&D, digital and risk factors. Company's own statements; no external audit of digital claims. PDF page = printed page. | 2026-11-08 / Alexandre with Claude Code |
| SRC-003 | Verified | TotalEnergies; press release *Fourth quarter and full year 2025 results* | 11 Feb 2026; FY2025 and 2026 outlook | https://totalenergies.com/system/files/documents/totalenergies_pr-results-q4-2025_2026_en.pdf | PDF pp. 1–2, 4–6, 8–9, 13–14 | Non-GAAP adjusted measures defined pp. 24–25. Outlook section p. 14 is forward-looking. | 2026-11-08 / Alexandre with Claude Code |
| SRC-004 | Verified | TotalEnergies; press release *2025 Strategy and Outlook Presentation* | 29 Sep 2025; targets 2026–2030 | https://www.sec.gov/Archives/edgar/data/879764/000110465925095236/tm2526548d1_ex99-17.htm (also totalenergies.com PDF) | Full text, cited by paragraph | Press release, not the slide deck. Savings figure superseded by SRC-003. | 2026-11-08 / Claude Code (web read) |
| SRC-005 | Verified | TotalEnergies; press release *Third quarter 2026 results* | 29 Oct 2026; Q3 and 9M 2026 | https://www.sec.gov/Archives/edgar/data/0000879764/000110465926120831/tm2628570d1_ex99-9.htm | Sections 1–9 (highlights, key figures, production, segments, outlook) | Verbatim text read for sections 1–9; tables after section 9 not read. | 2026-11-08 / Claude Code (web read) |
| SRC-006 | Pending | TotalEnergies; *Impact of Middle East Conflict on TotalEnergies Activities* | Mar 2026 (exact date unverified) | https://totalenergies.com/node/28411 (HTTP 410); AI summary at https://www.investegate.co.uk/announcement/bzw/totalenergies-se--tte/impact-of-middle-east-conflict-on-totalenergi-/9474942 | None verbatim | Primary text not read. Figures (~15% of output, ~10% of upstream cash flow) only via secondary summaries. | Pending |
| SRC-007 | Verified | TotalEnergies; press release *Data & Digital: TotalEnergies and Emerson Sign a Strategic Collaboration to Boost the Value of Industrial Data* | 22 Jul 2025 | https://www.sec.gov/Archives/edgar/data/0000879764/000110465925072916/tm2521848d1_ex99-5.htm | Full text | Announcement; no measured results. | 2026-11-08 / Claude Code (web read) |
| SRC-008 | Verified | TotalEnergies; press release *Digital Transformation: TotalEnergies and Cognite Expand Their Partnership to Scale Industrial AI* | 26 Sep 2025 | https://www.sec.gov/Archives/edgar/data/0000879764/000110465925095236/tm2526548d1_ex99-13.htm | Full text | Announcement; no measured results. Body text omits the year; filing date confirms 2025. | 2026-11-08 / Claude Code (web read) |
| SRC-009 | Verified | TotalEnergies; press release *TotalEnergies to Collaborate with Mistral AI to Increase the Application of Artificial Intelligence in its Multi-Energy Strategy* | 12 Jun 2025 | https://www.sec.gov/Archives/edgar/data/0000879764/000110465925064345/tm2518391d1_ex99-7.htm | Full text | Announcement; contains the Digital Factory figures as of June 2025. | 2026-11-08 / Claude Code (web read) |
| SRC-010 | Pending | World Oil; *TotalEnergies, Mistral launch AI program for oil and gas exploration* | 15 Sep 2026 | https://www.worldoil.com/news/2026/9/15/totalenergies-mistral-launch-ai-program-for-oil-and-gas-exploration/ | Full article | Trade press. Official release (Business Wire, 15 Sep 2026) not read verbatim; partnership itself confirmed by SRC-005. | 2026-11-08 / Claude Code (web read) |
| SRC-011 | Verified | TotalEnergies; *The Shareholders' Newsletter* #79, "AI as a Performance Driver: TotalEnergies Steps Up" (p. 10) and data-centre article (p. 9) | Summer 2026 | https://journal-des-actionnaires.totalenergies.com/79-en/doc/article/10/ and .../article/9/ | Pages 9–10 | Company communication to shareholders; ambitions mixed with facts; no measured AI results. | 2026-11-08 / Claude Code (web read) |
| SRC-012 | Verified | TotalEnergies; *The Shareholders' Newsletter* #76, "AI at the heart of our long-standing businesses and the energy transition" | Spring 2025 | https://journal-des-actionnaires.totalenergies.com/76-en/doc/article/11/ | Page 11 | Company communication; contains the only published AI decision principle found. | 2026-11-08 / Claude Code (web read) |
| SRC-013 | Verified | TotalEnergies; press release *TotalEnergies unlocks the potential of generative artificial intelligence for its employees* | 27 Feb 2024 | https://corporate.totalenergies.no/news-overview/totalenergies-unlocks-potential-generative-artificial-intelligence-its-employees | Full text | Announcement; no licence count or metrics. | 2026-11-08 / Claude Code (web read) |
| SRC-014 | Pending | Baguete (Brazil), J. Facca; *TotalEnergies ganha produtividade com Copilot* | 10 Nov 2025 | https://www.baguete.com.br/noticias/totalenergies-ganha-produtividade-com-copilot | Full article | Journalist text; licence and usage figures unattributed, no method; the 70% base differs between lede and body. Lead only. | 2026-11-08 / Claude Code (web read) |
| SRC-015 | Pending | Artefact; blog on Frédéric Gimenez (CDO) at the Adopt AI Summit | Event 5 Jun 2024; post undated | https://www.artefact.com/blog/frederic-gimenez-cdo-at-totalenergies-at-the-adopt-ai-summit-how-ai-supports-digitalization-strategy | Full article | Third-party write-up of a talk; use for leads and named use cases only. | 2026-11-08 / Claude Code (web read) |
| SRC-016 | Pending | Ter@tec; TERATEC 2026 Forum, roundtable speaker bio of Frédéric Gimenez | 2026 (event 20 Oct) | https://teratec.eu/gb/forum/Table_Ronde_02_02.html | Speaker bio | Third-party bio; role dates not confirmed by the company. | 2026-11-08 / Claude Code (web read) |

## Claim ledger

Add one row per material fact, calculation, assumption, local observation, or unknown. Split a claim if its sources, time periods, or scopes differ. The `Evidence / method` cell may link a detailed synthesis or model; the original source and location must still be visible here.

| ID | Class | Status | Statement / value and unit | Entity, geography, period | Evidence / method and exact location | Limits, alternative explanation, or test | Used in |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CLM-001 | Fact | Verified | 101,513 employees; present in about 120 countries; E&P in about 50 countries | Group, 31 Dec 2025 | SRC-002, pp. 6, 13, 49 | Older boilerplate says >130 countries; use URD. | S04 synthesis |
| CLM-002 | Fact | Verified | Adjusted net income $15.6bn; IFRS net income $13.1bn; adjusted EBITDA $40.6bn; CFFO $27.8bn | Group, FY2025 | SRC-003, p. 1 | Adjusted measures are non-GAAP. | S04 synthesis |
| CLM-003 | Fact | Verified | ROACE 12.6%; gearing 14.7% at 31 Dec 2025 | Group, FY2025 | SRC-003, pp. 4, 13 | "Best among majors" is a company claim. | S04 synthesis |
| CLM-004 | Fact | Verified | Net investments $17,091M (E&P 9,259; LNG 2,734; Integrated Power 2,776; R&C 1,437; M&S 609; Corporate 276) | Group, FY2025 | SRC-002, p. 37 | Column alignment checked by sum only. | S04 synthesis |
| CLM-005 | Fact | Verified | Hydrocarbon production 2,529 kboe/d; production costs $5.0/boe; proved reserves 11.2 Gboe | Group, FY2025 | SRC-003, p. 6; SRC-002, p. 74 | — | S04 synthesis |
| CLM-006 | Fact | Verified | Net power production 48.1 TWh (31.4 TWh renewables); 34.1 GW gross installed renewables | Integrated Power, FY2025 | SRC-003, p. 9 | Gross capacity includes affiliates' shares. | S04 synthesis |
| CLM-007 | Fact | Verified | Cost-savings plan (Capex + Opex) of $12.5bn over 2026–2030, incl. $2.5bn in 2026 | Group, 2026–2030 target | SRC-003, p. 14 | Supersedes $7.5bn (SRC-004). Levers and capex/opex split undisclosed; no AI contribution stated. | S04 synthesis |
| CLM-008 | Fact | Verified | Net investments ~ $15bn in 2026; $15–17bn/yr 2027–2030; low-carbon ~ $4bn/yr | Group, targets | SRC-003, p. 14; SRC-004, para. 3; SRC-005, §8 | Targets; downward flexibility to $14bn if Brent < $50/b (SRC-002, p. 37). | S04 synthesis |
| CLM-009 | Fact | Verified | Targets: O&G +3%/yr 2024–2030; electricity 100–120 TWh/y by 2030; Integrated Power ROACE 12% by 2030; shareholder return > 40% of cash flow | Group, to 2030 | SRC-004, paras. 4, 6, 7 | Targets, not results. | S04 synthesis |
| CLM-010 | Fact | Verified | 9M 2026 adjusted net income $20,518M; gearing 9.1% at 30 Sep 2026; Q3 Brent $97.0/b | Group, 9M 2026 | SRC-005, §2, §3.1 | High-price year; not a normalised baseline. | S04 synthesis |
| CLM-011 | Fact | Verified | Middle East conflict impact ~5% of production in Q3 2026; < 5% expected in Q4 2026 | Group, Q3–Q4 2026 | SRC-005, CEO quote, §3.3, §8 | — | S04 synthesis |
| CLM-012 | Fact | Pending | March 2026 shut-ins in Qatar, Iraq and offshore UAE ≈ 15% of output and ≈ 10% of upstream cash flow | Group, Mar 2026 | SRC-006 (secondary summaries only) | Read the primary release before use. | S04 synthesis |
| CLM-013 | Fact | Verified | R&D $810M in 2025; > $1bn in R&D, industrial innovation and digital developments; digital ≈ 30% of "overall efforts"; > 3,500 researchers | Group, FY2025 | SRC-002, p. 40 | "Overall efforts" base is undefined; no AI-specific budget. | S04, S05 syntheses |
| CLM-014 | Fact | Verified | Risk factor §3.1.5 names insufficient pace in adapting organisation and skills to digital and AI as a risk | Group, 2025 | SRC-002, p. 138 | Company risk statement. | S04, S05 syntheses |
| CLM-015 | Fact | Verified | Digital Line created in OneTech in Sept 2025; coordinates the branches' digital transformation plan; leads the Digital Plant and Digital for HSE programmes | OneTech, since Sept 2025 | SRC-002, pp. 39, 42 | Decision rights and funding not described. | S05 synthesis |
| CLM-016 | Fact | Disputed | Digital Factory: around 500 digital and AI experts in France and India | Digital Factory, URD filed Mar 2026 | SRC-002, pp. 42–43 | 300 in Jun 2025 (SRC-009, SRC-012); "500 engineers by 2027" target (SRC-011). See CON-001. | S05 synthesis |
| CLM-017 | Fact | Verified | Since 2020, nearly 100 solutions developed, 60% (p. 42) or half (p. 43) with AI, "progressively being deployed"; > 10,000 live AI models | Digital Factory, 2020–2025 | SRC-002, pp. 42–43 | No site, user or value figures. See CON-002. | S05 synthesis |
| CLM-018 | Fact | Verified | AspenTech Inmation data fabric: 2-year rollout across industrial sites worldwide (announced Jul 2025) | Industrial sites, 2025–2027 | SRC-007 | Planned; no results. | S05 synthesis |
| CLM-019 | Fact | Verified | Cognite platform scaled over 3 years across all operated upstream assets (announced Sep 2025) | Upstream, 2025–2028 | SRC-008 | Planned; no results. | S05 synthesis |
| CLM-020 | Fact | Verified | Mistral AI joint innovation lab; first use case an assistant for 1,000 researchers | Group R&D, Jun 2025 | SRC-009 | Announced; no results published. | S05 synthesis |
| CLM-021 | Fact | Pending | 3-year Mistral programme for subsurface frontier models, > €100M | Exploration & reservoir, Sep 2026 | SRC-010; partnership (not amount) confirmed in SRC-005 highlights | Read the official release for the amount. | S05 synthesis |
| CLM-022 | Fact | Verified | Copilot for Microsoft 365 and Power Platform: 300-employee test Sept 2023; deployment announced Feb 2024; "gradual provision" with training (Digital Accelerator season, 2024–2025) | Group employees | SRC-013; SRC-002, pp. 284, 388 | Official licence count unknown. | S05 synthesis |
| CLM-023 | Fact | Pending | > 30,000 Copilot licences; 70% of users use it weekly | Group employees, Nov 2025 | SRC-014 | Unattributed journalism, no method. Lead only. | S05 synthesis |
| CLM-024 | Fact | Verified | Four AI priorities for 2026: HSE, digital plant, AI for geosciences and reservoirs, Integrated Power modelling | Group, 2026 | SRC-011, p. 10 | Stated priorities. | S05 synthesis |
| CLM-025 | Fact | Verified | Board Strategy & CSR Committee examined digital ambitions and AI on 19 Mar 2025; 2026 Board action to review the impact of technological disruptions incl. AI | Board, 2025–2026 | SRC-002, pp. 211, 223, 225 | — | S05 synthesis |
| CLM-026 | Fact | Verified | Published AI principle: no entirely autonomous decision-making systems; final decisions by expert teams; traceability required | Group, Spring 2025 | SRC-012, p. 11 | Only governance principle found; no AI charter or model inventory found. | S05 synthesis |
| CLM-027 | Fact | Verified | Integrated Power runs in-house ML/AI for price forecasting and trading (Predictive Layer, acquired Dec 2023; Quadra Energy forecasting) | Integrated Power | SRC-002, pp. 109–110 | Shows capability inside a segment. | S05 synthesis |
| CLM-028 | Fact | Verified | Data-centre power: 4 GW of projects secured 2025–2026; ~10% PPA premium; > $250M annual EBITDA expected at maturity | Integrated Power | SRC-011, p. 9 | EBITDA is a target; this is AI as a market, not internal AI use. | S05 synthesis |
| CLM-029 | Unknown | Pending | Value realised (cost, revenue, safety) by any internal AI solution | Group | No source found in SRC-002 to SRC-016 | Needed for the financial case and readiness scoring. | S05 synthesis |
| CLM-030 | Unknown | Pending | Funding route and decision rights for Digital Factory solutions (central vs business units) | Group | Not described in SRC-002 | Needed for step 10 (operating model). | S05 synthesis |

## Contradictions and unresolved questions

| ID | Claim IDs or question | Conflict / missing evidence | Decision affected | Next check and owner | Status |
| --- | --- | --- | --- | --- | --- |
| CON-001 | CLM-016 | Digital Factory headcount: 300 (SRC-009, Jun 2025; SRC-012, Spring 2025) vs ~500 "digital and AI experts in France and India" (SRC-002, Mar 2026) vs goal of "500 engineers by 2027" (SRC-011, Summer 2026). Possibly growth plus India, or different scopes. | Readiness scoring (talent), operating-model sizing | Careers page, LinkedIn headcount or a 2026 interview; owner to assign | Disputed |
| CON-002 | CLM-017 | Share of Digital Factory solutions with AI: 60% (SRC-002, p. 42) vs "half" (p. 43) vs 60 of "over a hundred" (SRC-009). | Minor; quote as "about half to 60%" | None needed unless used as a headline figure | Disputed |
| CON-003 | CLM-007 | Savings plan $7.5bn (SRC-004, Sep 2025) vs $12.5bn (SRC-003, Feb 2026), same 2026–2030 period. | Financial case anchor | Use $12.5bn | Superseded |
| CON-004 | CLM-011, CLM-012 | Middle East impact ~15% of output (Mar 2026, secondary) vs ~5% (Q3 2026, primary). Likely a gradual restart; primary March text unread. | Context and risk section | Read the March 2026 release (SEC Form 6-K or totalenergies.com); owner to assign | Pending |
| CON-005 | Legacy draft vs SRC-002 | The draft says the Digital Factory has ~300 engineers and that the group "struggles to industrialise beyond the initial pilot site". The URD gives ~500 experts and ~100 solutions "progressively being deployed"; no source measures the replication rate. | Step 07 audit; step 09 bottleneck | Classify in step 07: headcount outdated; industrialisation claim `Unknown` | Pending |

## Entry checks

- [ ] Original source opens and its title, organization, version, and date are recorded.
- [ ] Page/section or URL points to the exact supporting passage.
- [ ] Claim type and status match what has actually been verified.
- [ ] Period, organizational/geographic scope, unit, and denominator are explicit where relevant.
- [ ] Formula and input IDs are present for each derived figure; assumed inputs are labeled.
- [ ] Limits, contradictions, and unknowns remain visible in downstream work.
