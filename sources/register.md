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

## Claim ledger

Add one row per material fact, calculation, assumption, local observation, or unknown. Split a claim if its sources, time periods, or scopes differ. The `Evidence / method` cell may link a detailed synthesis or model; the original source and location must still be visible here.

| ID | Class | Status | Statement / value and unit | Entity, geography, period | Evidence / method and exact location | Limits, alternative explanation, or test | Used in |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Contradictions and unresolved questions

| ID | Claim IDs or question | Conflict / missing evidence | Decision affected | Next check and owner | Status |
| --- | --- | --- | --- | --- | --- |

## Entry checks

- [ ] Original source opens and its title, organization, version, and date are recorded.
- [ ] Page/section or URL points to the exact supporting passage.
- [ ] Claim type and status match what has actually been verified.
- [ ] Period, organizational/geographic scope, unit, and denominator are explicit where relevant.
- [ ] Formula and input IDs are present for each derived figure; assumed inputs are labeled.
- [ ] Limits, contradictions, and unknowns remain visible in downstream work.
