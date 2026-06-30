# Inicia backend + frontend do Agentarium em janelas separadas.
# Uso: .\start_agentarium.ps1 [-Install]

param(
    [switch]$Install
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$Root = $PSScriptRoot
$Backend = Join-Path $Root "apps\agentarium\backend"
$Frontend = Join-Path $Root "apps\agentarium\frontend"

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

Start-Process powershell -ArgumentList @(
    "-NoExit",
    "-Command",
    "${utf8Init}Set-Location '$Backend'; Write-Host 'Agentarium BACKEND' -ForegroundColor Cyan; npm run dev"
)

Start-Sleep -Seconds 2

Start-Process powershell -ArgumentList @(
    "-NoExit",
    "-Command",
    "${utf8Init}Set-Location '$Frontend'; Write-Host 'Agentarium FRONTEND' -ForegroundColor Cyan; npm run dev"
)

Write-Host ""
Write-Host "== Agentarium iniciado ==" -ForegroundColor Green
Write-Host "Frontend:  http://127.0.0.1:5174"
Write-Host "Backend:   http://127.0.0.1:3847"
Write-Host "Health:    http://127.0.0.1:3847/health"
Write-Host "WebSocket: ws://127.0.0.1:3847/ws"
Write-Host ""
Write-Host "Teste manual: .\test_agentarium_event.ps1" -ForegroundColor DarkGray
Start-Process "http://127.0.0.1:5174/"
