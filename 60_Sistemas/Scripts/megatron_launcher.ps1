param(
    [switch]$NoOpenApps,
    [switch]$SkipDocker,
    [switch]$SkipContainers,
    [switch]$SkipBrowser,
    [switch]$WithAgentarium,
    [switch]$Diagnostico,
    [switch]$Quiet,
    [switch]$JsonOnly
)

$ErrorActionPreference = "Continue"
[Console]::OutputEncoding = New-Object System.Text.UTF8Encoding $false
$OutputEncoding = [Console]::OutputEncoding

$Lib = Join-Path $PSScriptRoot "megatron_lib.ps1"
. $Lib

$VaultRoot = Get-MegatronVaultRoot -FromScriptPath $MyInvocation.MyCommand.Path
$Paths = Get-MegatronPaths -VaultRoot $VaultRoot
$Orchestrate = Join-Path $PSScriptRoot "megatron_orchestrate.ps1"

Import-MegatronEnv -VaultRoot $VaultRoot -Defaults @{
    AGENTARIUM_PORT       = "3847"
    AGENTARIUM_UI_PORT    = "5174"
    N8N_URL               = "http://localhost:5678"
    MEGATRON_OPEN_BROWSER = "true"
}

$AgentariumUi = "http://127.0.0.1:$($env:AGENTARIUM_UI_PORT)"
$Today = Get-Date -Format "yyyy-MM-dd"
$Now = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$ChangelogFile = Join-Path $Paths.ChangelogDir "${Today}_retomada-ambiente-fabioos.md"
$StartedAt = Get-Date

if ($Diagnostico) {
    $NoOpenApps = $true
    $SkipBrowser = $true
    $SkipDocker = $true
    $WithAgentarium = $false
}

function Ensure-Changelog {
    if (!(Test-Path $Paths.ChangelogDir)) {
        New-Item -ItemType Directory -Path $Paths.ChangelogDir -Force | Out-Null
    }
    if (!(Test-Path $ChangelogFile)) {
        @"
---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: ativo
tags: [fabios, retomada, megatron, orquestrador]
criado_em: $Today
atualizado_em: $Today
---

# Retomada MEGATRON - $Today

## Eventos

"@ | Set-Content -Path $ChangelogFile -Encoding UTF8
    }
    Add-Content -Path $ChangelogFile -Value "- $Now - MEGATRON Orchestrator v1.0 boot." -Encoding UTF8
    Write-MegatronOk "Retomada registrada" -Quiet:$Quiet
}

function Show-Briefing {
    Write-MegatronSection "Briefing" -Quiet:$Quiet
    if (Test-Path $Paths.StatusPath) {
        Write-Host "STATUS:" -ForegroundColor Cyan
        Get-Content $Paths.StatusPath -Encoding UTF8 |
            Select-String -Pattern "Proxima acao|Bloco C|recomendada" |
            Select-Object -First 4 |
            ForEach-Object { Write-MegatronInfo $_.Line.Trim() -Quiet:$Quiet }
    }
    if (Test-Path $Paths.NextActionsPath) {
        Write-Host "NEXT_ACTIONS:" -ForegroundColor Cyan
        Get-Content $Paths.NextActionsPath -Encoding UTF8 |
            Select-String -Pattern "^- \[ \]" | Select-Object -First 5 |
            ForEach-Object { Write-Host $_.Line }
    }
    $intake = Get-MegatronIntakeSummary -IntakeQueuePath $Paths.IntakeQueuePath
    if ($intake.present) {
        Write-MegatronInfo "Intake: $($intake.aguardando_fabio) aguardando Fabio / $($intake.total) total" -Quiet:$Quiet
    }
}

function Start-Cockpit {
    Write-MegatronSection "Cockpit" -Quiet:$Quiet
    $obsidianPath = Join-Path $env:LOCALAPPDATA "Obsidian\Obsidian.exe"
    if (Test-Path $obsidianPath) {
        Open-MegatronUrl "obsidian://open?path=$([uri]::EscapeDataString($VaultRoot))"
        Write-MegatronOk "Obsidian" -Quiet:$Quiet
    }
    if (Start-MegatronIfCommand -Command "cursor" -Arguments @($VaultRoot)) {
        Write-MegatronOk "Cursor" -Quiet:$Quiet
    } elseif (Start-MegatronIfCommand -Command "code" -Arguments @($VaultRoot)) {
        Write-MegatronOk "VS Code" -Quiet:$Quiet
    }
    $wtCmd = "Set-Location -LiteralPath '$VaultRoot'; Write-Host 'MEGATRON' -ForegroundColor Yellow"
    if (-not (Start-MegatronIfCommand -Command "wt" -Arguments @("powershell", "-NoExit", "-Command", $wtCmd))) {
        Start-Process powershell.exe -ArgumentList @("-NoExit", "-Command", $wtCmd)
    }
}

# --- MAIN ---
Show-MegatronBanner -Quiet:$Quiet
Set-Location $VaultRoot
Write-MegatronLog -LogPath $Paths.LauncherLog -Message "MEGATRON Orchestrator v1.0 boot"

Write-MegatronSection "Preflight" -Quiet:$Quiet
Write-MegatronOk "Vault: $VaultRoot" -Quiet:$Quiet
if (Get-Command python -ErrorAction SilentlyContinue) { Write-MegatronOk "Python OK" -Quiet:$Quiet }
if (Get-Command node -ErrorAction SilentlyContinue) { Write-MegatronOk "Node OK" -Quiet:$Quiet }
if (-not (Test-Path $Paths.ConfigLocal)) {
    Write-MegatronInfo "Copie megatron.env.example -> megatron.local.env" -Quiet:$Quiet
}

Ensure-Changelog

$orchResult = $null
if (-not $Diagnostico) {
    Write-MegatronSection "Orquestracao MEGATRON" -Quiet:$Quiet
    $orchResult = & $Orchestrate -VaultRoot $VaultRoot -Paths $Paths -LogPath $Paths.LauncherLog `
        -SkipDocker:$SkipDocker -SkipContainers:$SkipContainers -WithAgentarium:$WithAgentarium -Quiet:$Quiet
}

if (-not $NoOpenApps) { Start-Cockpit }

$health = $null
if ($orchResult) {
    $health = $orchResult.health
} else {
    if (-not $env:EVOLUTION_API_URL) { $env:EVOLUTION_API_URL = "http://127.0.0.1:8080" }
    if (-not $env:OPENCLAW_URL) { $env:OPENCLAW_URL = "http://127.0.0.1:18789" }
    if (-not $env:EVOLUTION_INSTANCE) { $env:EVOLUTION_INSTANCE = "fabioos-pessoal" }
    if (-not $env:AGENTARIUM_PORT) { $env:AGENTARIUM_PORT = "3847" }
    $health = Get-MegatronFullServiceHealth `
        -AgentariumHealth "http://127.0.0.1:$($env:AGENTARIUM_PORT)/health" `
        -AgentariumUi $AgentariumUi `
        -N8nUrl $env:N8N_URL `
        -EvolutionBase $env:EVOLUTION_API_URL `
        -OpenClawUrl $env:OPENCLAW_URL `
        -InstanceName $env:EVOLUTION_INSTANCE
}

$intake = Get-MegatronIntakeSummary -IntakeQueuePath $Paths.IntakeQueuePath

Write-MegatronSection "Saude" -Quiet:$Quiet
foreach ($svc in @("agentarium_ui", "agentarium_backend", "n8n", "evolution_api", "openclaw", "whatsapp_connected")) {
    if ($health.ContainsKey($svc)) {
        $on = $health[$svc]
        if ($on) { Write-MegatronOk "$svc online" -Quiet:$Quiet }
        else { Write-MegatronInfo "$svc offline" -Quiet:$Quiet }
    }
}

$runtime = @{
    version     = "1.0.0"
    product     = "MEGATRON Orchestrator"
    started_at  = $StartedAt.ToString("o")
    finished_at = (Get-Date).ToString("o")
    vault_root  = $VaultRoot
    mode        = if ($Diagnostico) { "diagnostico" } else { "full" }
    services    = $health
    phases      = if ($orchResult) { $orchResult.phases } else { @() }
    urls        = if ($orchResult) { $orchResult.urls } else { @{ agentarium_ui = $AgentariumUi } }
    intake      = $intake
    interface   = $AgentariumUi
}

Write-MegatronRuntimeState -RuntimePath $Paths.RuntimeState -Payload $runtime

if ($JsonOnly) {
    $runtime | ConvertTo-Json -Depth 8
    exit 0
}

if (-not $SkipBrowser -and ($env:MEGATRON_OPEN_BROWSER -eq "true")) {
    Write-MegatronSection "Interface MEGATRON" -Quiet:$Quiet
    Open-MegatronUrl $AgentariumUi
    Write-MegatronOk "Agentarium aberto - cockpit unico" -Quiet:$Quiet
}

Show-Briefing
Write-MegatronSection "Concluido" -Quiet:$Quiet
Write-MegatronOk "MEGATRON orquestrado. Interface: $AgentariumUi" -Quiet:$Quiet
Write-MegatronLog -LogPath $Paths.LauncherLog -Message "Boot concluido"
