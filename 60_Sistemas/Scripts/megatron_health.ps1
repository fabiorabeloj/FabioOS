# Health check rapido do MEGATRON (sem subir servicos)
# Uso: .\60_Sistemas\Scripts\megatron_health.ps1
#      .\60_Sistemas\Scripts\megatron_health.ps1 -Json

param([switch]$Json)

$Lib = Join-Path $PSScriptRoot "megatron_lib.ps1"
. $Lib

$VaultRoot = Get-MegatronVaultRoot -FromScriptPath $MyInvocation.MyCommand.Path
$Paths = Get-MegatronPaths -VaultRoot $VaultRoot
Import-MegatronEnv -VaultRoot $VaultRoot -Defaults @{
    AGENTARIUM_PORT    = "3847"
    AGENTARIUM_UI_PORT = "5174"
    N8N_URL            = "http://localhost:5678"
}

$health = Get-MegatronServiceHealth `
    -AgentariumHealth "http://127.0.0.1:$($env:AGENTARIUM_PORT)/health" `
    -AgentariumUi "http://127.0.0.1:$($env:AGENTARIUM_UI_PORT)" `
    -N8nUrl $env:N8N_URL

$payload = @{
    checked_at = (Get-Date).ToString("o")
    vault_root = $VaultRoot
    services   = $health
    intake     = Get-MegatronIntakeSummary -IntakeQueuePath $Paths.IntakeQueuePath
    runtime    = if (Test-Path $Paths.RuntimeState) {
        Get-Content $Paths.RuntimeState -Raw -Encoding UTF8 | ConvertFrom-Json
    } else { $null }
}

if ($Json) {
    $payload | ConvertTo-Json -Depth 8
    exit 0
}

Write-Host "MEGATRON health @ $($payload.checked_at)" -ForegroundColor Cyan
foreach ($k in $health.Keys | Sort-Object) {
    $ok = $health[$k]
    $color = if ($ok) { "Green" } else { "DarkGray" }
    Write-Host ("  {0,-20} {1}" -f $k, $(if ($ok) { "online" } else { "offline" })) -ForegroundColor $color
}
if ($payload.intake.present) {
    Write-Host ""
    Write-Host "  intake aguardando Fabio: $($payload.intake.aguardando_fabio) / $($payload.intake.total)" -ForegroundColor Yellow
}
