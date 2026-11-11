$ErrorActionPreference = 'Stop'
$outputs = @{
11='work/options/selected_portfolio_decision.md';12='work/projects/case_p01_refining_pdm.md';13='work/projects/case_p03_deepwater_drilling.md';14='work/projects/case_p12_esaf_licensing.md';15='work/projects/case_p13_retail_station_demand.md';16='work/projects/reserve_cards.md';17='work/projects/chart_regeneration_spec.md';18='work/finance/portfolio_model_selected.xlsx';19='work/finance/cost_of_inaction.md';20='work/governance/gates_and_adoption.md';21='deliverables/report/full_strategy_report_draft.md'
}
New-Item -ItemType Directory -Force -Path tmp/issue_sync | Out-Null
foreach ($number in ($outputs.Keys | Sort-Object)) {
  $item = gh issue view $number --repo Xenodion/ai-transformations-navy --json body,title,state | ConvertFrom-Json
  if ($LASTEXITCODE -ne 0) { throw 'Issue read failed' }
  if ($item.body.Contains('## Authorized refinement')) { continue }
  $path = $outputs[$number]
  $body = $item.body.Replace('- [x]','- [ ]') + @"


## Authorized refinement — 10 November 2026

Active scope: P01/P02/P03/P05/P09/P12/P13/E01. Featured cases: P01/P03/P12/P13. Earlier output references above are historical and superseded. Current output: [$path](https://github.com/Xenodion/ai-transformations-navy/blob/main/$path). Revised files are local and not yet pushed.

Owners and dependencies remain unchanged. Revised downside includes delayed benefits and higher costs; no unsupported inaction cash uplift. H3 tests external technology licensing. Half-budget response is recalculated from the selected envelope. Independent arithmetic checks completed; graphics regeneration and final challenge remain open. No acceptance criterion is declared satisfied solely by file existence. This issue remains open and matches the refinement table in work/roadmap.md.
"@
  $bodyFile = "tmp/issue_sync/issue-$number.md"
  Set-Content -LiteralPath $bodyFile -Value $body -Encoding utf8
  gh issue edit $number --repo Xenodion/ai-transformations-navy --body-file $bodyFile
  if ($LASTEXITCODE -ne 0) { throw "Issue $number update failed" }
}
