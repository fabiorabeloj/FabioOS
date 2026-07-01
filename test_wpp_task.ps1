param(
  [string]$Prompt = "tarefa: revisar estrutura do FabioOS e sugerir proximo passo"
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$body = @{
  messageId      = "wa-task-test-" + [DateTimeOffset]::UtcNow.ToUnixTimeMilliseconds()
  conversationId = "fabio-personal"
  contactName    = "Fabio"
  from           = "5511982123896"
  direction      = "outgoing"
  text           = $Prompt
  timestamp      = (Get-Date).ToUniversalTime().ToString("o")
  source         = "manual_test"
  provider       = "evolution_api"
} | ConvertTo-Json -Compress

Write-Host "=== Teste tarefa WPP -> MEGATRON ===" -ForegroundColor Cyan
Write-Host "Prompt: $Prompt"

$r = Invoke-RestMethod -Uri "http://127.0.0.1:3847/integrations/whatsapp/personal/message" `
  -Method POST -ContentType "application/json; charset=utf-8" `
  -Body ([System.Text.Encoding]::UTF8.GetBytes($body))

$r | ConvertTo-Json -Depth 5

if ($r.taskCaptured) {
  Write-Host ""
  Write-Host "[OK] Tarefa capturada" -ForegroundColor Green
  Write-Host "Arquivo: $($r.taskFile)" -ForegroundColor Cyan
  Write-Host "Agente: $($r.suggestedAgent)" -ForegroundColor Cyan
}

if ($r.sentToFabio) {
  Write-Host "[OK] Confirmacao enviada no WhatsApp" -ForegroundColor Green
}
