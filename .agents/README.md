# Repository conventions

## Locations

| Directory | Contents | Rule |
| --- | --- | --- |
| `course/` | Received guidelines, lectures, notes, and exam sheets | Preserve original course materials. |
| `sources/primary/` | Original TotalEnergies and institutional documents | Log title, date, and provenance in `sources/register.md`. |
| `sources/benchmark/` | Original competitor and sector sources | Distinguish announcements from measured results. |
| `sources/synthesis/` | Factual summaries of a source set or question | Use `spec-kit/source_synthesis.md`; these are not primary sources. |
| `work/research/` | Investigations, checks, open questions | Intermediate work. |
| `work/options/` | Competing diagnoses, accepted/rejected ideas, decisions | Team reasoning. |
| `work/projects/` | Long list, case studies, portfolio | Full card for each featured case; short cards for the rest. |
| `work/finance/` | Assumptions, model, calculation checks | Reconcile with project cards and report. |
| `deliverables/report/`, `memo/`, `slides/` | Submission-ready versions | Version clearly and use the same figures. |
| `deliverables/archive/` | Exact copies of submitted files | Record submission date and time. |

`work/roadmap.md` and GitHub issues jointly track progress. `work/legacy_plan_unverified.md` is a French historical draft for audit only. Empty directories need no placeholder files.

## Names and traceability

- Work files: `short_topic.md`; syntheses: `YYYY-MM-DD_topic.md`; original sources: keep recognizable names, adding the year if useful.
- Each synthesis cites original documents, pages or sections, and exact links. Enter every retained source in `sources/register.md`.
- Until final editing, mark claims as `Fact`, `Calculation`, `Assumption`, `Local observation`, or `Unknown`. A quantified assumption needs a formula and plausible range.
- Perplexity and other external AI outputs provide leads. Check links and read original sources before relying on a claim.

## Templates and issues

`spec-kit/` holds synthesis, project, and issue templates. `prompts/` holds topic-specific instructions for external research tools. Each GitHub issue matches one numbered roadmap step, has an output label (`report`, `memo`, `slides`, etc.), an owner and acceptance criterion, and links its output. Update the issue and roadmap together. Existence of a document alone does not meet its acceptance criterion.
