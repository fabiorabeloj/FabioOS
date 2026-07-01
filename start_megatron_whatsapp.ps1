# Sobe e verifica a pilha MEGATRON WhatsApp (Evolution + n8n + Agentarium)
# Uso: .\start_megatron_whatsapp.ps1
# Depois: mande "ola" no chat Voce do WhatsApp

param(
  [switch]$SkipSync,
  [switch]$SkipTest
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$Root = $PSScriptRoot
$SecretsDir = Join-Path $env:USERPROFILE ".fabioos\secrets"
$EvolutionKeyFile = Join-Path $SecretsDir "evolution_api_key.txt"
$InstanceName = "fabioos-pessoal"
$PhoneNumber = "5511982123896"
$EvolutionBase = "http://127.0.0.1:8080"
$AgentariumBase = "http://127.0.0.1:3847"
$N8nWebhook = "http://host.docker.internal:5678/webhook/whatsapp-pietra-v2"
$BackendDir = Join-Path $Root "apps\agentarium\backend"

function Write-Step($msg) { Write-Host ""; Write-Host "== $msg ==" -ForegroundColor Cyan }
function Write-Ok($msg) { Write-Host "[OK] $msg" -ForegroundColor Green }
function Write-Warn($msg) { Write-Host "[AVISO] $msg" -ForegroundColor Yellow }

function Get-EvolutionKey {
  if (-not (Test-Path $EvolutionKeyFile)) { throw "Chave Evolution ausente: $EvolutionKeyFile" }
  return (Get-Content $EvolutionKeyFile -Raw).Trim()
}

function Test-PortListening($port) {
  $c = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue | Select-Object -First 1
  return $null -ne $c
}

function Wait-Health($url, $seconds = 45) {
  $deadline = (Get-Date).AddSeconds($seconds)
  while ((Get-Date) -lt $deadline) {
    try {
      $r = Invoke-RestMethod -Uri $url -TimeoutSec 3
      if ($r.ok) { return $r }
    } catch {
      Start-Sleep -Seconds 2
    }
  }
  throw "Timeout aguardando $url"
}

Write-Step "MEGATRON WhatsApp - subir stack"

Write-Step "Evolution API"
$evoStatus = docker ps -a --filter "name=evolution-api" --format "{{.Status}}" 2>$null
if ($evoStatus -match "Exited|Created") {
  Write-Warn "Iniciando containers Evolution..."
  docker start evolution-postgres evolution-redis evolution-api 2>$null | Out-Null
  Start-Sleep -Seconds 12
}
$key = Get-EvolutionKey
$headers = @{ apikey = $key }
$state = (Invoke-RestMethod -Uri "$EvolutionBase/instance/connectionState/$InstanceName" -Headers $headers).instance.state
Write-Host "Instancia ${InstanceName}: $state"
if ($state -ne "open") {
  Write-Warn "WhatsApp nao conectado. Rode: .\start_whatsapp_pessoal.ps1"
} else {
  Write-Ok "WhatsApp conectado"
}

try {
  $webhookBody = @{
    enabled = $true
    url = $N8nWebhook
    webhookByEvents = $false
    webhookBase64 = $false
    events = @("MESSAGES_UPSERT")
  } | ConvertTo-Json -Compress
  Invoke-RestMethod -Uri "$EvolutionBase/webhook/set/$InstanceName" -Method POST -Headers $headers `
    -ContentType "application/json; charset=utf-8" `
    -Body ([System.Text.Encoding]::UTF8.GetBytes($webhookBody)) | Out-Null
  Write-Ok "Webhook Evolution -> n8n configurado"
} catch {
  Write-Warn "Webhook Evolution: $($_.Exception.Message)"
}

Write-Step "n8n"
$n8n = docker ps --filter "name=n8n" --format "{{.Names}}" 2>$null
if (-not $n8n) {
  Write-Warn "Container n8n parado. Tente: docker start n8n"
} else {
  Write-Ok "n8n rodando"
  if (-not $SkipSync) {
    $prevEap = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    try {
      & (Join-Path $Root "sync_n8n_whatsapp_workflow.ps1")
    } catch {
      Write-Warn "Sync n8n: $($_.Exception.Message)"
    }
    $ErrorActionPreference = $prevEap
  }
}

Write-Step "Agentarium backend"
$backendUp = $false
try {
  $h = Invoke-RestMethod -Uri "$AgentariumBase/health" -TimeoutSec 3
  if ($h.ok) {
    $backendUp = $true
    Write-Ok "Backend ja online (v$($h.version))"
  }
} catch {
  $backendUp = $false
}

if (-not $backendUp) {
  Write-Warn "Backend offline - iniciando..."
  if (-not (Test-Path (Join-Path $BackendDir "node_modules"))) {
    Push-Location $BackendDir
    npm install --silent
    Pop-Location
  }
  if (-not (Test-Path (Join-Path $BackendDir "dist\index.js"))) {
    Push-Location $BackendDir
    npm run build
    Pop-Location
  }

  $env:WHATSAPP_REPLY_TO_FABIO = "true"
  $env:WHATSAPP_CONVERSATIONAL = "true"
  $env:MEGATRON_OPENROUTER_MODEL = "openrouter/free"
  $env:FABIO_WHATSAPP_NUMBER = $PhoneNumber
  $env:EVOLUTION_API_URL = $EvolutionBase
  $env:EVOLUTION_INSTANCE = $InstanceName

  Start-Process -FilePath "node" -ArgumentList "dist/index.js" -WorkingDirectory $BackendDir -WindowStyle Minimized
  $h = Wait-Health "$AgentariumBase/health"
  Write-Ok "Backend online (v$($h.version))"
}

if (-not (Test-PortListening 5174)) {
  Write-Warn "Frontend offline. Painel: .\start_agentarium.ps1"
} else {
  Write-Ok "Frontend http://127.0.0.1:5174"
}

if (-not $SkipTest) {
  Write-Step "Teste simulado (ola -> n8n -> MEGATRON -> WPP)"
  & (Join-Path $Root "test_n8n_webhook_personal.ps1") -Text "ola"
}

Write-Step "Pronto"
Write-Host "MEGATRON WhatsApp: mande 'ola' no chat VOCE do WhatsApp." -ForegroundColor Green
Write-Host "Apos reiniciar o PC: .\start_megatron_whatsapp.ps1" -ForegroundColor Cyan
