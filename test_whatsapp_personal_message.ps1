# Teste WhatsApp pessoal -> Agentarium v0.5 (Hermes)
# Envia mensagem simulada para POST /integrations/whatsapp/message
# Nenhuma mensagem real e enviada.

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$ApiUrl = "http://127.0.0.1:3847/integrations/whatsapp/message"
$Payload = @{
  messageId      = "wa-test-001"
  conversationId = "test-personal"
  contactName    = "Contato Teste"
  from           = "5511999999999"
  direction      = "incoming"
  text           = "Fabio, consegue me responder depois sobre aquele assunto?"
  timestamp      = (Get-Date).ToUniversalTime().ToString("o")
  source         = "manual_test"
  provider       = "evolution_api"
} | ConvertTo-Json -Compress

Write-Host "=== Teste WhatsApp Pessoal -> Hermes ===" -ForegroundColor Cyan
Write-Host "POST $ApiUrl"

try {
  $r = Invoke-RestMethod -Uri $ApiUrl -Method POST `
    -ContentType "application/json; charset=utf-8" `
    -Body ([System.Text.Encoding]::UTF8.GetBytes($Payload))
} catch {
  Write-Host "[ERRO] Backend Agentarium offline? Rode: .\start_agentarium.ps1" -ForegroundColor Red
  throw
}

Write-Host "[OK] Resposta:" -ForegroundColor Green
$r | ConvertTo-Json -Depth 5

if ($r.approvalState -ne "draft_only" -and $r.approvalState -ne "blocked") {
  Write-Host "[WARN] approvalState inesperado: $($r.approvalState)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Verifique no painel http://127.0.0.1:5174:" -ForegroundColor Cyan
Write-Host "  - Hermes em Personal WhatsApp / Message Intake"
Write-Host "  - Event Log: [WHATSAPP] [MANUAL_TEST]"
Write-Host "  - Personal WhatsApp Intake: job $($r.jobId)"
Write-Host "  - approvalState: $($r.approvalState)"
Write-Host "  - Nenhuma mensagem enviada (draft_only)"
