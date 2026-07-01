param(
    [string]$VaultRoot,
    [hashtable]$Paths,
    [string]$LogPath,
    [switch]$SkipDocker,
    [switch]$SkipContainers,
    [switch]$WithAgentarium,
    [switch]$Quiet
)

$Lib = Join-Path $PSScriptRoot "megatron_lib.ps1"
. $Lib

Import-MegatronEnv -VaultRoot $VaultRoot -Defaults @{
    AGENTARIUM_PORT          = "3847"
    AGENTARIUM_UI_PORT       = "5174"
    N8N_URL                  = "http://localhost:5678"
    EVOLUTION_API_URL        = "http://127.0.0.1:8080"
    EVOLUTION_INSTANCE       = "fabioos-pessoal"
    OPENCLAW_URL             = "http://127.0.0.1:18789"
    MEGATRON_WAIT_SERVICES   = "true"
    MEGATRON_WITH_OPENCLAW   = "true"
    MEGATRON_WITH_WHATSAPP   = "true"
    MEGATRON_WITH_N8N_SYNC   = "true"
    MEGATRON_WITH_MAESTRO_WATCH = "true"
    MEGATRON_WITH_INTAKE_WARM   = "true"
}

$WaitServices = ($env:MEGATRON_WAIT_SERVICES -eq "true")
$AgentariumHealth = "http://127.0.0.1:$($env:AGENTARIUM_PORT)/health"
$AgentariumUi = "http://127.0.0.1:$($env:AGENTARIUM_UI_PORT)"
$N8nUrl = $env:N8N_URL
$EvolutionBase = $env:EVOLUTION_API_URL
$OpenClawUrl = $env:OPENCLAW_URL
$InstanceName = $env:EVOLUTION_INSTANCE

$Phases = @()

function Add-Phase {
    param([string]$Name, [string]$Status, [string]$Detail = "")
    $script:Phases += @{ name = $Name; status = $Status; detail = $Detail; at = (Get-Date).ToString("o") }
    Write-MegatronLog -LogPath $LogPath -Message "Fase $Name : $Status $Detail"
}

function Start-ExitedContainers {
    param([string[]]$Names)
    if (-not (Get-Command docker -ErrorAction SilentlyContinue)) { return @() }
    $started = @()
    foreach ($pattern in $Names) {
        docker ps -a --filter "name=$pattern" --filter "status=exited" --format "{{.Names}}" 2>$null | ForEach-Object {
            docker start $_ 2>$null | Out-Null
            if ($LASTEXITCODE -eq 0) {
                $started += $_
                Write-MegatronOk "Container iniciado: $_" -Quiet:$Quiet
            }
        }
    }
    return $started
}

# --- Fase 1: Docker Desktop ---
if (-not $SkipDocker) {
    Write-MegatronSection "Fase 1 - Infra Docker" -Quiet:$Quiet
    $dockerDesktop = Join-Path $env:ProgramFiles "Docker\Docker\Docker Desktop.exe"
    if (-not (Get-Process -Name "Docker Desktop" -ErrorAction SilentlyContinue) -and (Test-Path $dockerDesktop)) {
        Start-Process $dockerDesktop
        Start-Sleep -Seconds 8
        Write-MegatronOk "Docker Desktop solicitado" -Quiet:$Quiet
    }
    Add-Phase "docker_desktop" "ok" ""
}

# --- Fase 2: Containers (Evolution + n8n) ---
if (-not $SkipDocker -and -not $SkipContainers) {
    Write-MegatronSection "Fase 2 - Containers" -Quiet:$Quiet
    if ($env:MEGATRON_WITH_WHATSAPP -eq "true") {
        $evo = Start-ExitedContainers @("evolution-postgres", "evolution-redis", "evolution-api")
        if ($evo.Count -gt 0) { Start-Sleep -Seconds 10 }
        Add-Phase "evolution_stack" $(if ($evo.Count -gt 0) { "started" } else { "skipped_or_running" }) ($evo -join ",")
    }
    $n8n = Start-ExitedContainers @("n8n")
    if ($n8n.Count -gt 0) { Start-Sleep -Seconds 5 }
    Add-Phase "n8n" $(if ($n8n.Count -gt 0) { "started" } else { "skipped_or_running" }) ($n8n -join ",")

    if ($WaitServices -and (Get-Command docker -ErrorAction SilentlyContinue)) {
        if ($env:MEGATRON_WITH_WHATSAPP -eq "true") {
            Wait-MegatronHttp -Url $EvolutionBase -MaxWaitSec 60 | Out-Null
        }
        Wait-MegatronHttp -Url $N8nUrl -MaxWaitSec 90 | Out-Null
    }
}

# --- Fase 3: OpenClaw ---
if ($env:MEGATRON_WITH_OPENCLAW -eq "true") {
    Write-MegatronSection "Fase 3 - OpenClaw" -Quiet:$Quiet
    $ensure = Join-Path $VaultRoot "60_Sistemas\OpenClaw\scripts\ensure_openclaw_gateway.ps1"
    if (Test-Path $ensure) {
        $prev = $ErrorActionPreference
        $ErrorActionPreference = "Continue"
        & $ensure 2>&1 | Out-Null
        $ocOk = ($LASTEXITCODE -eq 0) -or (Test-MegatronHttp -Url $OpenClawUrl)
        $ErrorActionPreference = $prev
        if ($ocOk) {
            Write-MegatronOk "OpenClaw gateway online" -Quiet:$Quiet
            Add-Phase "openclaw" "ok" $OpenClawUrl
        } else {
            Write-MegatronWarn "OpenClaw indisponivel (WSL OpenClawGateway?)"
            Add-Phase "openclaw" "warn" "gateway offline"
        }
    } else {
        Add-Phase "openclaw" "skip" "script ausente"
    }
}

# --- Fase 4: n8n WhatsApp sync ---
if ($env:MEGATRON_WITH_N8N_SYNC -eq "true" -and (Test-MegatronHttp -Url $N8nUrl)) {
    Write-MegatronSection "Fase 4 - n8n sync" -Quiet:$Quiet
    $sync = Join-Path $VaultRoot "sync_n8n_whatsapp_workflow.ps1"
    if (Test-Path $sync) {
        $prev = $ErrorActionPreference
        $ErrorActionPreference = "Continue"
        & $sync 2>&1 | Out-Null
        $ErrorActionPreference = $prev
        Add-Phase "n8n_sync" "ok" "whatsapp workflow"
        Write-MegatronOk "Workflow n8n sincronizado" -Quiet:$Quiet
    }
}

# --- Fase 5: Agentarium (interface MEGATRON) ---
if ($WithAgentarium) {
    Write-MegatronSection "Fase 5 - Agentarium" -Quiet:$Quiet
    if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
        Write-MegatronWarn "Node ausente"
        Add-Phase "agentarium" "fail" "node ausente"
    } elseif (Test-MegatronHttp -Url $AgentariumHealth) {
        Write-MegatronOk "Agentarium ja online" -Quiet:$Quiet
        Add-Phase "agentarium" "ok" "ja ativo"
    } elseif (Test-Path $Paths.AgentariumStart) {
        & $Paths.AgentariumStart -NoBrowser
        if ($WaitServices) {
            Wait-MegatronHttp -Url $AgentariumHealth -MaxWaitSec 90 | Out-Null
            Wait-MegatronHttp -Url $AgentariumUi -MaxWaitSec 45 | Out-Null
        } else {
            Start-Sleep -Seconds 5
        }
        $up = Test-MegatronHttp -Url $AgentariumHealth
        Add-Phase "agentarium" $(if ($up) { "ok" } else { "warn" }) $AgentariumUi
        Write-MegatronOk "Agentarium solicitado" -Quiet:$Quiet
    }
}

# --- Fase 6: Evolution webhook + WhatsApp ---
if ($env:MEGATRON_WITH_WHATSAPP -eq "true" -and (Test-MegatronHttp -Url $EvolutionBase)) {
    Write-MegatronSection "Fase 6 - WhatsApp / Evolution" -Quiet:$Quiet
    $keyFile = Join-Path $env:USERPROFILE ".fabioos\secrets\evolution_api_key.txt"
    if (Test-Path $keyFile) {
        try {
            $key = (Get-Content $keyFile -Raw).Trim()
            $headers = @{ apikey = $key }
            $state = (Invoke-RestMethod -Uri "$EvolutionBase/instance/connectionState/$InstanceName" -Headers $headers -TimeoutSec 5).instance.state
            Write-MegatronInfo "WhatsApp $InstanceName : $state" -Quiet:$Quiet
            Add-Phase "whatsapp_state" $(if ($state -eq "open") { "ok" } else { "warn" }) $state

            $n8nWebhook = "http://host.docker.internal:5678/webhook/whatsapp-pietra-v2"
            $webhookBody = @{
                enabled = $true
                url = $n8nWebhook
                webhookByEvents = $false
                webhookBase64 = $false
                events = @("MESSAGES_UPSERT")
            } | ConvertTo-Json -Compress
            Invoke-RestMethod -Uri "$EvolutionBase/webhook/set/$InstanceName" -Method POST -Headers $headers `
                -ContentType "application/json; charset=utf-8" `
                -Body ([System.Text.Encoding]::UTF8.GetBytes($webhookBody)) -TimeoutSec 10 | Out-Null
            Add-Phase "evolution_webhook" "ok" $n8nWebhook
            Write-MegatronOk "Webhook Evolution configurado" -Quiet:$Quiet
        } catch {
            Add-Phase "whatsapp" "warn" $_.Exception.Message
            Write-MegatronWarn "WhatsApp/Evolution: $($_.Exception.Message)"
        }
    } else {
        Add-Phase "whatsapp" "skip" "evolution_api_key ausente"
        Write-MegatronInfo "Evolution key nao configurada - WhatsApp manual" -Quiet:$Quiet
    }
}

# --- Fase 7: Intake warm ---
if ($env:MEGATRON_WITH_INTAKE_WARM -eq "true" -and -not (Test-Path $Paths.IntakeQueuePath)) {
    Write-MegatronSection "Fase 7 - Intake warm" -Quiet:$Quiet
    $flow = Join-Path $VaultRoot "60_Sistemas\MEGATRON\v1\intake_flow.py"
    if ((Get-Command python -ErrorAction SilentlyContinue) -and (Test-Path $flow)) {
        python $flow 2>&1 | Out-Null
        Add-Phase "intake_warm" "ok" "intake_flow.py"
        Write-MegatronOk "Fila intake gerada" -Quiet:$Quiet
    }
}

# --- Fase 8: Maestro watcher (background) ---
if ($env:MEGATRON_WITH_MAESTRO_WATCH -eq "true") {
    $watcher = Join-Path $VaultRoot "60_Sistemas\MEGATRON\v1\watch_maestro_state.ps1"
    $already = Get-CimInstance Win32_Process -Filter "Name='python.exe'" -ErrorAction SilentlyContinue |
        Where-Object { $_.CommandLine -match "watch_maestro_state" }
    if (-not $already -and (Test-Path $watcher)) {
        Start-Process powershell.exe -ArgumentList @(
            "-WindowStyle", "Hidden",
            "-ExecutionPolicy", "Bypass",
            "-File", $watcher
        ) -WorkingDirectory (Split-Path $watcher)
        Add-Phase "maestro_watch" "ok" "background"
        Write-MegatronOk "Maestro watcher em background" -Quiet:$Quiet
    }
}

# --- Fase 9: Agentarium integrations sync ---
if (Test-MegatronHttp -Url $AgentariumHealth) {
    try {
        Invoke-RestMethod -Uri "http://127.0.0.1:$($env:AGENTARIUM_PORT)/integrations/maestro/sync" -Method POST -TimeoutSec 15 | Out-Null
        Add-Phase "maestro_sync" "ok" "via agentarium"
    } catch {
        Add-Phase "maestro_sync" "warn" $_.Exception.Message
    }
}

$health = Get-MegatronFullServiceHealth `
    -AgentariumHealth $AgentariumHealth `
    -AgentariumUi $AgentariumUi `
    -N8nUrl $N8nUrl `
    -EvolutionBase $EvolutionBase `
    -OpenClawUrl $OpenClawUrl `
    -InstanceName $InstanceName

@{
    phases   = $Phases
    health   = $health
    urls     = @{
        agentarium_ui = $AgentariumUi
        agentarium_api = "http://127.0.0.1:$($env:AGENTARIUM_PORT)"
        n8n = $N8nUrl
        evolution = $EvolutionBase
        openclaw = $OpenClawUrl
    }
}
