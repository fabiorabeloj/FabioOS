# Envia mensagem de teste via Evolution API (MEGATRON -> seu WhatsApp)
param(
  [string]$Text = "Oi, Fabio. MEGATRON online.",
  [string]$To = "5511982123896"
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$ApiKeyFile = Join-Path $env:USERPROFILE ".fabioos\secrets\evolution_api_key.txt"
$InstanceName = "fabioos-pessoal"
$EvolutionBase = "http://127.0.0.1:8080"

if (-not (Test-Path $ApiKeyFile)) {
  throw "Chave Evolution nao encontrada: $ApiKeyFile"
}

$key = (Get-Content $ApiKeyFile -Raw).Trim()
$headers = @{ apikey = $key }

Write-Host "=== MEGATRON -> WhatsApp (sendText) ===" -ForegroundColor Cyan

$state = (Invoke-RestMethod -Uri "$EvolutionBase/instance/connectionState/$InstanceName" -Headers $headers).instance.state
Write-Host "Evolution ($InstanceName): $state"

if ($state -ne "open") {
  Write-Host "WhatsApp nao conectado. Rode: .\start_whatsapp_pessoal.ps1" -ForegroundColor Yellow
  exit 1
}

$body = @{
  number = $To
  text   = $Text
} | ConvertTo-Json -Compress

$r = Invoke-RestMethod -Uri "$EvolutionBase/message/sendText/$InstanceName" `
  -Method POST -Headers $headers `
  -ContentType "application/json; charset=utf-8" `
  -Body ([System.Text.Encoding]::UTF8.GetBytes($body))

Write-Host "[OK] Mensagem enviada para +$To" -ForegroundColor Green
Write-Host "Texto: $Text" -ForegroundColor DarkCyan
$r | ConvertTo-Json -Depth 4
