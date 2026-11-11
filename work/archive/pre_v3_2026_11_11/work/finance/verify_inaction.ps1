# Read cached workbook values only; never saves or recalculates the workbook.
# Y0-Y5 cumulative cash is in Portfolio!B6:D11. Overlay inputs are the
# documented academic scenario in cost_of_inaction.md (USD m, after tax).
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
$workbook = Join-Path $PSScriptRoot 'portfolio_model_14_revised.xlsx'
$archive = [IO.Compression.ZipFile]::OpenRead($workbook)
try {
    $entry = $archive.GetEntry('xl/worksheets/sheet1.xml')
    if (-not $entry) { throw 'Portfolio worksheet not found at the expected workbook position.' }
    $reader = [IO.StreamReader]::new($entry.Open())
    try { [xml]$sheet = $reader.ReadToEnd() } finally { $reader.Dispose() }
    $ns = [Xml.XmlNamespaceManager]::new($sheet.NameTable)
    $ns.AddNamespace('x', 'http://schemas.openxmlformats.org/spreadsheetml/2006/main')
    $cash = @{}
    foreach ($column in @('B','C','D')) {
        $cumulative = @()
        foreach ($row in 6..11) {
            $cell = $sheet.SelectSingleNode("//x:c[@r='$column$row']", $ns)
            if (-not $cell -or -not $cell.v) { throw "Missing cached value: $column$row" }
            $cumulative += [double]::Parse([string]$cell.v, [Globalization.CultureInfo]::InvariantCulture)
        }
        $annual = @($cumulative[0])
        foreach ($year in 1..5) { $annual += $cumulative[$year] - $cumulative[$year-1] }
        $cash[$column] = $annual
    }
} finally { $archive.Dispose() }
function Get-Npv([double[]]$values, [double]$rate) {
    $result = 0.0
    for ($i = 0; $i -lt $values.Count; $i++) { $result += $values[$i] / [Math]::Pow(1 + $rate, $i) }
    return $result
}
function Get-Irr([double[]]$values) {
    $low = -0.99; $high = 1.0
    if ((Get-Npv $values $low) -le 0 -or (Get-Npv $values $high) -ge 0) { throw 'IRR not bracketed.' }
    for ($iteration = 0; $iteration -lt 120; $iteration++) {
        $mid = ($low + $high) / 2
        if ((Get-Npv $values $mid) -gt 0) { $low = $mid } else { $high = $mid }
    }
    return ($low + $high) / 2
}
$weighted = for ($i=0; $i -lt 6; $i++) { .25*$cash.B[$i] + .5*$cash.C[$i] + .25*$cash.D[$i] }
$overlay = @(0,0,.20,.45,.70,.95)
$expected = @{ Downside = 0.197; Base = 5.204; Upside = 8.891; Weighted = 4.874 }
foreach ($scenario in @(@('Downside',$cash.B),@('Base',$cash.C),@('Upside',$cash.D),@('Weighted',$weighted))) {
    [double[]]$flows = $scenario[1]
    [double[]]$adjusted = for ($i=0; $i -lt 6; $i++) { $flows[$i] + $overlay[$i] }
    $decisionNpv = Get-Npv $adjusted .10
    if ([Math]::Abs($decisionNpv - $expected[$scenario[0]]) -gt 0.0006) { throw "Decision NPV mismatch: $($scenario[0]) = $decisionNpv" }
    [pscustomobject]@{ Scenario=$scenario[0]; BeforeNpv=(Get-Npv $flows .10); AvoidedNpv=(Get-Npv $overlay .10); DecisionNpv=(Get-Npv $adjusted .10); DecisionIrr=(Get-Irr $adjusted) }
}

