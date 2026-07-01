# Inicia backend + frontend do Agentarium em janelas separadas.
# Uso: .\start_agentarium.ps1 [-Install] [-NoBrowser]
# Config local: megatron.local.env (FABIO_WHATSAPP_NUMBER, EVOLUTION_*, etc.)

param(
    [switch]$Install,
    [switch]$NoBrowser
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$Root = $PSScriptRoot
$Backend = Join-Path $Root "apps\agentarium\backend"
$Frontend = Join-Path $Root "apps\agentarium\frontend"
$Lib = Join-Path $Root "60_Sistemas\Scripts\megatron_lib.ps1"

if (Test-Path $Lib) {
    . $Lib
    Import-MegatronEnv -VaultRoot $Root -Defaults @{
        AGENTARIUM_PORT            = "3847"
        AGENTARIUM_UI_PORT         = "5174"
        WHATSAPP_REPLY_TO_FABIO    = "true"
        WHATSAPP_CONVERSATIONAL    = "true"
        MEGATRON_OPENROUTER_MODEL  = "openrouter/free"
        EVOLUTION_API_URL          = "http://127.0.0.1:8080"
        EVOLUTION_INSTANCE         = "fabioos-pessoal"
    }
} else {
    $env:AGENTARIUM_PORT = "3847"
    $env:AGENTARIUM_UI_PORT = "5174"
}

if (-not (Test-Path $Backend) -or -not (Test-Path $Frontend)) {
    Write-Error "Pastas apps/agentarium/backend ou frontend nao encontradas."
}

function Ensure-Npm($Dir) {
    if ($Install -or -not (Test-Path (Join-Path $Dir "node_modules"))) {
        Write-Host "npm install em $Dir ..." -ForegroundColor Gray
        Push-Location $Dir
        npm install
        if ($LASTEXITCODE -ne 0) { Pop-Location; throw "npm install falhou em $Dir" }
        Pop-Location
    }
}

Ensure-Npm $Backend
Ensure-Npm $Frontend

$utf8Init = "[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new(`$false); `$OutputEncoding = [System.Text.UTF8Encoding]::new(`$false); "

$envPairs = @(
    "WHATSAPP_REPLY_TO_FABIO"
    "WHATSAPP_CONVERSATIONAL"
    "MEGATRON_OPENROUTER_MODEL"
    "FABIO_WHATSAPP_NUMBER"
    "EVOLUTION_API_URL"
    "EVOLUTION_INSTANCE"
    "PORT"
)

$backendEnvParts = @()
foreach ($name in $envPairs) {
    $val = (Get-Item -Path "env:$name" -ErrorAction SilentlyContinue).Value
    if ($val) {
        $escaped = $val -replace "'", "''"
        $backendEnvParts += "`$env:$name = '$escaped'"
    }
}
if (-not $env:PORT) {
    $backendEnvParts += "`$env:PORT = '$($env:AGENTARIUM_PORT)'"
}
$backendEnv = $backendEnvParts -join "; "

Start-Process powershell -ArgumentList @(
    "-NoExit",
    "-Command",
    "${utf8Init}${backendEnv}; Set-Location '$Backend'; Write-Host 'Agentarium BACKEND' -ForegroundColor Cyan; npm run dev"
)

Start-Sleep -Seconds 2

Start-Process powershell -ArgumentList @(
    "-NoExit",
    "-Command",
    "${utf8Init}Set-Location '$Frontend'; Write-Host 'Agentarium FRONTEND' -ForegroundColor Cyan; npm run dev"
)

$uiUrl = "http://127.0.0.1:$($env:AGENTARIUM_UI_PORT)"
$apiUrl = "http://127.0.0.1:$($env:AGENTARIUM_PORT)"

Write-Host ""
Write-Host "== Agentarium iniciado ==" -ForegroundColor Green
Write-Host "Frontend:  $uiUrl"
Write-Host "Backend:   $apiUrl"
Write-Host "Health:    $apiUrl/health"
Write-Host "WebSocket: ws://127.0.0.1:$($env:AGENTARIUM_PORT)/ws"
Write-Host ""

if (-not $NoBrowser) {
    Start-Process $uiUrl
}
