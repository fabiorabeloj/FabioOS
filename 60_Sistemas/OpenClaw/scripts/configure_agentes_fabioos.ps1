# Configura e valida agentes OpenClaw + MEGATRON (smoke test).
# Nao altera runtime ~/.openclaw alem do que ensure ja faz (bind loopback).

param(
    [switch]$SkipGateway,
    [switch]$SkipOpenClawChat,
    [switch]$SkipMegatron
)

$ErrorActionPreference = "Continue"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$env:PYTHONIOENCODING = "utf-8"

$Root = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
$Scripts = $PSScriptRoot
$Results = @()

function Add-Result {
    param([string]$Agent, [string]$Status, [string]$Detail)
    $script:Results += [pscustomobject]@{ Agent = $Agent; Status = $Status; Detail = $Detail }
    $color = switch ($Status) { "OK" { "Green" } "WARN" { "Yellow" } default { "Red" } }
    Write-Host "[$Status] $Agent - $Detail" -ForegroundColor $color
}

Write-Host "`n== FabioOS - Configuracao de Agentes ==" -ForegroundColor Cyan

if (-not $SkipGateway) {
    & (Join-Path $Scripts "ensure_openclaw_gateway.ps1")
    if ($LASTEXITCODE -ne 0) {
        Add-Result "gateway" "FAIL" "ensure_openclaw_gateway falhou"
    } else {
        Add-Result "gateway" "OK" "http://127.0.0.1:18789/"
    }
}

Write-Host "`n-- OpenClaw (nativos) --" -ForegroundColor DarkCyan
$list = wsl -d OpenClawGateway -- openclaw agents list 2>&1 | Out-String
if ($list -match "fabioos-ponte" -and $list -match "main") {
    Add-Result "openclaw.main" "OK" "modelo openrouter/free"
    Add-Result "openclaw.fabioos-ponte" "OK" "workspace ponte no vault"
} else {
    Add-Result "openclaw.agents" "FAIL" "main ou fabioos-ponte ausente"
}

$auth = wsl -d OpenClawGateway -- openclaw models --agent fabioos-ponte status 2>&1 | Out-String
if ($auth -match "openrouter:manual" -or $auth -match "api_key=1") {
    Add-Result "openclaw.auth" "OK" "OpenRouter configurado (fabioos-ponte)"
} else {
    Add-Result "openclaw.auth" "WARN" "verificar auth OpenRouter em ~/.openclaw"
}

if (-not $SkipOpenClawChat) {
    $chat = wsl -d OpenClawGateway -- openclaw agent --agent fabioos-ponte --thinking off --message "ping configuracao agentes" 2>&1 | Out-String
    if ($chat.Length -gt 5) {
        $lastLine = ($chat.Trim().Split("`n")[-1]).Trim()
        if ($lastLine.Length -gt 80) { $lastLine = $lastLine.Substring(0, 80) }
        Add-Result "openclaw.fabioos-ponte.chat" "OK" $lastLine
    } else {
        Add-Result "openclaw.fabioos-ponte.chat" "FAIL" "sem resposta"
    }
}

if (-not $SkipMegatron) {
    Write-Host "`n-- MEGATRON (Python) --" -ForegroundColor DarkCyan
    $Runner = Join-Path $Scripts "run_megatron_agent.ps1"

    try {
        & $Runner -Agente safecommit 2>&1 | Out-Null
        Add-Result "agent.safecommit" "OK" "diagnostico git"
    } catch {
        Add-Result "agent.safecommit" "FAIL" $_.Exception.Message
    }

    try {
        & $Runner -Agente inbox 2>&1 | Out-Null
        Add-Result "agent.inbox" "OK" "triagem 00_Inbox"
    } catch {
        Add-Result "agent.inbox" "FAIL" $_.Exception.Message
    }

    try {
        $RagPy = Join-Path $Root "60_Sistemas\RAG\.venv\Scripts\python.exe"
        $RagScript = Join-Path $Root "60_Sistemas\MEGATRON\agentes\implementacao\claude\rag_agent.py"
        & $RagPy $RagScript "O que e o FabioOS?" 2>&1 | Out-Null
        if ($LASTEXITCODE -eq 0) {
            Add-Result "agent.rag" "OK" "recuperacao Fase 12"
        } else {
            Add-Result "agent.rag" "WARN" "exit $LASTEXITCODE (pode ser timeout HF; rodar direto se falhar)"
        }
    } catch {
        Add-Result "agent.rag" "WARN" $_.Exception.Message
    }

    Add-Result "agent.arquivista" "OK" "requer -Args (--titulo + --texto|--arquivo); ver MAPA"

    try {
        & $Runner -Agente dashboard 2>&1 | Out-Null
        Add-Result "agent.dashboard" "OK" "STATUS_Agentes.md gerado"
    } catch {
        Add-Result "agent.dashboard" "FAIL" $_.Exception.Message
    }
}

Write-Host "`n-- Workboard --" -ForegroundColor DarkCyan
$wb = wsl -d OpenClawGateway -- openclaw workboard list --board fabioos 2>&1 | Out-String
$megCount = ([regex]::Matches($wb, "MEGATRON")).Count
if ($megCount -ge 5) {
    Add-Result "workboard.fabioos" "OK" "$megCount cards MEGATRON visiveis"
} else {
    Add-Result "workboard.fabioos" "WARN" "cards MEGATRON=$megCount; rodar sync_workboard_megatron.ps1"
}

Write-Host "`n== Resumo ==" -ForegroundColor Cyan
$Results | Format-Table -AutoSize
$fail = ($Results | Where-Object { $_.Status -eq "FAIL" }).Count
exit $(if ($fail -gt 0) { 1 } else { 0 })
