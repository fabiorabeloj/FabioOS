# MEGATRON shared library - FabioOS launcher
# Dot-source: . (Join-Path $PSScriptRoot "megatron_lib.ps1")

function Get-MegatronVaultRoot {
    param([string]$FromScriptPath)
    $dir = if ($FromScriptPath) { Split-Path -Parent $FromScriptPath } else { $PSScriptRoot }
    return (Resolve-Path (Join-Path $dir "..\..")).Path
}

function Get-MegatronPaths {
    param([string]$VaultRoot)

    @{
        VaultRoot       = $VaultRoot
        ConfigExample   = Join-Path $VaultRoot "megatron.env.example"
        ConfigLocal     = Join-Path $VaultRoot "megatron.local.env"
        ChangelogDir    = Join-Path $VaultRoot "50_Registros\Changelog"
        StatusPath      = Join-Path $VaultRoot "60_Sistemas\FabioOS\STATUS.md"
        NextActionsPath = Join-Path $VaultRoot "60_Sistemas\FabioOS\NEXT_ACTIONS.md"
        IntakeQueuePath = Join-Path $VaultRoot "60_Sistemas\MEGATRON\v1\state\intake_queue.json"
        RuntimeState    = Join-Path $VaultRoot "60_Sistemas\MEGATRON\v1\state\megatron_runtime.json"
        LauncherLog     = Join-Path $VaultRoot "60_Sistemas\MEGATRON\v1\state\megatron_launcher.log"
        AgentariumStart = Join-Path $VaultRoot "start_agentarium.ps1"
        MegatronCmd     = Join-Path $VaultRoot "MEGATRON.cmd"
        DashboardMd     = Join-Path $VaultRoot "10_Dashboard\MEGATRON.md"
    }
}

function Import-MegatronEnv {
    param(
        [string]$VaultRoot,
        [hashtable]$Defaults = @{}
    )

    $files = @(
        (Join-Path $VaultRoot "megatron.env.example"),
        (Join-Path $VaultRoot "megatron.local.env")
    )

    foreach ($file in $files) {
        if (-not (Test-Path $file)) { continue }
        Get-Content $file -Encoding UTF8 | ForEach-Object {
            $line = $_.Trim()
            if (-not $line -or $line.StartsWith("#")) { return }
            if ($line -match "^([A-Za-z_][A-Za-z0-9_]*)=(.*)$") {
                $name = $Matches[1]
                $value = $Matches[2].Trim().Trim('"').Trim("'")
                if ($value) {
                    Set-Item -Path "env:$name" -Value $value
                }
            }
        }
    }

    foreach ($key in $Defaults.Keys) {
        $existing = (Get-Item -Path "env:$key" -ErrorAction SilentlyContinue).Value
        if (-not [string]::IsNullOrWhiteSpace($existing)) { continue }
        if ($null -ne $Defaults[$key] -and "$($Defaults[$key])" -ne "") {
            Set-Item -Path "env:$key" -Value $Defaults[$key]
        }
    }
}

function Write-MegatronLog {
    param(
        [string]$LogPath,
        [string]$Message,
        [string]$Level = "INFO"
    )
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $line = "$ts [$Level] $Message"
    $dir = Split-Path -Parent $LogPath
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
    Add-Content -Path $LogPath -Value $line -Encoding UTF8
}

function Test-MegatronHttp {
    param(
        [string]$Url,
        [int]$TimeoutSec = 3
    )
    try {
        $r = Invoke-WebRequest -Uri $Url -UseBasicParsing -TimeoutSec $TimeoutSec
        return ($r.StatusCode -ge 200 -and $r.StatusCode -lt 400)
    } catch {
        return $false
    }
}

function Wait-MegatronHttp {
    param(
        [string]$Url,
        [string]$Label,
        [int]$MaxWaitSec = 45,
        [int]$IntervalSec = 2
    )
    $deadline = (Get-Date).AddSeconds($MaxWaitSec)
    while ((Get-Date) -lt $deadline) {
        if (Test-MegatronHttp -Url $Url -TimeoutSec 2) {
            return $true
        }
        Start-Sleep -Seconds $IntervalSec
    }
    return $false
}

function Get-MegatronServiceHealth {
    param(
        [string]$AgentariumHealth,
        [string]$AgentariumUi,
        [string]$N8nUrl
    )

    @{
        agentarium_backend = Test-MegatronHttp -Url $AgentariumHealth
        agentarium_ui      = Test-MegatronHttp -Url $AgentariumUi
        n8n                = Test-MegatronHttp -Url $N8nUrl
        docker_cli         = [bool](Get-Command docker -ErrorAction SilentlyContinue)
        python             = [bool](Get-Command python -ErrorAction SilentlyContinue)
        node               = [bool](Get-Command node -ErrorAction SilentlyContinue)
        git                = [bool](Get-Command git -ErrorAction SilentlyContinue)
    }
}

function Get-MegatronFullServiceHealth {
    param(
        [string]$AgentariumHealth,
        [string]$AgentariumUi,
        [string]$N8nUrl,
        [string]$EvolutionBase,
        [string]$OpenClawUrl,
        [string]$InstanceName
    )

    $base = Get-MegatronServiceHealth -AgentariumHealth $AgentariumHealth -AgentariumUi $AgentariumUi -N8nUrl $N8nUrl

    $base.evolution_api = Test-MegatronHttp -Url $EvolutionBase
    $base.openclaw = Test-MegatronHttp -Url $OpenClawUrl
    $base.whatsapp_connected = $false

    if ($base.agentarium_backend) {
        try {
            $wpp = Invoke-RestMethod -Uri ($AgentariumHealth -replace "/health$", "/integrations/whatsapp/status") -TimeoutSec 5
            if ($wpp.ok -or $wpp.connected -or $wpp.state -eq "open") {
                $base.whatsapp_connected = $true
            }
        } catch { }
    }

    if (-not $base.whatsapp_connected -and $base.evolution_api) {
        $keyFile = Join-Path $env:USERPROFILE ".fabioos\secrets\evolution_api_key.txt"
        if (Test-Path $keyFile) {
            try {
                $key = (Get-Content $keyFile -Raw).Trim()
                $s = (Invoke-RestMethod -Uri "$EvolutionBase/instance/connectionState/$InstanceName" -Headers @{ apikey = $key } -TimeoutSec 5).instance.state
                $base.whatsapp_connected = ($s -eq "open")
                $base.whatsapp_state = $s
            } catch { }
        }
    }

    $base
}

function Get-MegatronIntakeSummary {
    param([string]$IntakeQueuePath)

    if (-not (Test-Path $IntakeQueuePath)) {
        return @{ present = $false; aguardando_fabio = 0; total = 0 }
    }
    try {
        $q = Get-Content $IntakeQueuePath -Raw -Encoding UTF8 | ConvertFrom-Json
        $aguardando = 0
        $total = 0
        $sensiveis = 0
        if ($q.resumo) {
            if ($null -ne $q.resumo.aguardando_fabio) { $aguardando = [int]$q.resumo.aguardando_fabio }
            if ($null -ne $q.resumo.total) { $total = [int]$q.resumo.total }
            if ($null -ne $q.resumo.sensiveis) { $sensiveis = [int]$q.resumo.sensiveis }
        }
        return @{
            present          = $true
            aguardando_fabio = $aguardando
            total            = $total
            sensiveis        = $sensiveis
        }
    } catch {
        return @{ present = $true; error = "ilegivel" }
    }
}

function Write-MegatronRuntimeState {
    param(
        [string]$RuntimePath,
        [hashtable]$Payload
    )

    $dir = Split-Path -Parent $RuntimePath
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
    $json = $Payload | ConvertTo-Json -Depth 8
    [System.IO.File]::WriteAllText($RuntimePath, $json, (New-Object System.Text.UTF8Encoding $false))
}

function Start-MegatronIfCommand {
    param(
        [string]$Command,
        [string[]]$Arguments
    )
    $cmd = Get-Command $Command -ErrorAction SilentlyContinue
    if ($cmd) {
        Start-Process -FilePath $cmd.Source -ArgumentList $Arguments
        return $true
    }
    return $false
}

function Open-MegatronUrl {
    param([string]$Url)
    Start-Process $Url | Out-Null
}

function Show-MegatronBanner {
    param([switch]$Quiet)
    if ($Quiet) { return }
    Write-Host ""
    Write-Host "  __  __ ______ ______ __  __  _____ _______   __" -ForegroundColor DarkYellow
    Write-Host " |  \/  |  ____|  ____|  \/  |/ ____|__   __| / /" -ForegroundColor DarkYellow
    Write-Host " | \  / | |__  | |__  | \  / | (___    | |   / / " -ForegroundColor Yellow
    Write-Host " | |\/| |  __| |  __| | |\/| |\___ \   | |  / /  " -ForegroundColor Yellow
    Write-Host " | |  | | |____| |____| |  | |____) |  | | / /   " -ForegroundColor DarkYellow
    Write-Host " |_|  |_|______|______|_|  |_|_____/   |_|/_/    " -ForegroundColor DarkYellow
    Write-Host " FabioOS cockpit - MEGATRON Orchestrator v1.0" -ForegroundColor DarkGray
    Write-Host ""
}

function Write-MegatronSection {
    param([string]$Title, [switch]$Quiet)
    if ($Quiet) { return }
    Write-Host ""
    Write-Host "== $Title ==" -ForegroundColor Cyan
}

function Write-MegatronOk {
    param([string]$Message, [switch]$Quiet)
    if ($Quiet) { return }
    Write-Host "[OK] $Message" -ForegroundColor Green
}

function Write-MegatronWarn {
    param([string]$Message)
    Write-Host "[AVISO] $Message" -ForegroundColor Yellow
}

function Write-MegatronInfo {
    param([string]$Message, [switch]$Quiet)
    if ($Quiet) { return }
    Write-Host "[INFO] $Message" -ForegroundColor Gray
}
