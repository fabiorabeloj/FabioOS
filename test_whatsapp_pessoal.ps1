# Teste pos-conexao WhatsApp pessoal FabioOS
# Requer: instancia fabioos-pessoal com state=open, n8n ativo, Agentarium online

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$key = (Get-Content "$env:USERPROFILE\.fabioos\secrets\evolution_api_key.txt" -Raw).Trim()

Write-Host "=== Verificacao WhatsApp Pessoal ===" -ForegroundColor Cyan

$state = (Invoke-RestMethod -Uri "http://127.0.0.1:8080/instance/connectionState/fabioos-pessoal" -Headers @{ apikey = $key }).instance.state
Write-Host "Estado Evolution: $state"

if ($state -ne "open") {
  Write-Host "Ainda nao conectado. Rode: .\start_whatsapp_pessoal.ps1" -ForegroundColor Yellow
  exit 1
}

Write-Host "[OK] WhatsApp conectado" -ForegroundColor Green

Write-Host ""
Write-Host "Testando n8n -> Hermes -> Agentarium..." -ForegroundColor Cyan
& "$PSScriptRoot\test_n8n_webhook_personal.ps1" -Text "/status"

Write-Host ""
Write-Host "Painel: http://127.0.0.1:5174" -ForegroundColor Cyan
Write-Host "Inbox:  00_Inbox/Processar/Hermes_Canal_Fabio.md" -ForegroundColor Cyan
