# Read-only reconciliation of the six-project half-envelope illustration.
$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
$path=Join-Path $PSScriptRoot 'portfolio_model_14_revised.xlsx'
$zip=[IO.Compression.ZipFile]::OpenRead($path)
try {
  $sheets=@{}
  foreach($sheetIndex in @(5,8)) {
    $entry=$zip.GetEntry("xl/worksheets/sheet$sheetIndex.xml")
    $reader=[IO.StreamReader]::new($entry.Open())
    try { [xml]$xml=$reader.ReadToEnd() } finally {$reader.Dispose()}
    $ns=[Xml.XmlNamespaceManager]::new($xml.NameTable)
    $ns.AddNamespace('s','http://schemas.openxmlformats.org/spreadsheetml/2006/main')
    $sheets[$sheetIndex]=@{xml=$xml;ns=$ns}
  }
  function Cell([int]$sheet,[string]$address) {
    $data=$sheets[$sheet]
    $cell=$data.xml.SelectSingleNode("//s:c[@r='$address']",$data.ns)
    if(-not $cell -or -not $cell.v){throw "Missing numeric cache sheet $sheet cell $address"}
    return [double]::Parse([string]$cell.v,[Globalization.CultureInfo]::InvariantCulture)
  }
  # Inputs row order: P01..P13, E01; P01/P03/P05/P12/P13/E01 selected.
  $indices=@(0,2,4,11,12,13)
  $budget=0.0
  foreach($i in $indices) {
    $row=$i+2; $fx=Cell 5 "E$row"; $cost=0.0
    foreach($col in @('G','H','I','J','K','L','M','N')) {$cost += Cell 5 "$col$row"}
    $budget += $fx*$cost
  }
  if([Math]::Abs($budget-13.01708) -gt 0.000001){throw "Unexpected gross budget $budget"}
  $scenarios=@()
  foreach($scenario in 0..2) {
    $annual=@()
    foreach($year in 0..5) {
      $sum=0.0
      foreach($i in $indices) {
        $row=2+7*(3*$i+$scenario)+5; $column=[char](66+$year)
        $sum += Cell 8 "$column$row"
      }
      $annual += $sum
    }
    $scenarios += ,$annual
  }
  $weighted=for($year=0;$year -lt 6;$year++){.25*$scenarios[0][$year]+.5*$scenarios[1][$year]+.25*$scenarios[2][$year]}
  $npv=0.0
  for($year=0;$year -lt 6;$year++){$npv += $weighted[$year]/[Math]::Pow(1.1,$year)}
  if([Math]::Abs($npv-2.9019024331) -gt 0.000001){throw "Unexpected weighted NPV $npv"}
  [pscustomobject]@{GrossBudgetUsdM=$budget; WeightedNpvUsdM=$npv; Scope='P01 P03 P05 P12 P13 E01'; InactionOverlay='Not included'}
} finally {$zip.Dispose()}

