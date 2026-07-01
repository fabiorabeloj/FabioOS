$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$body = @{
  messageId      = "wa-cmd-status-" + [DateTimeOffset]::UtcNow.ToUnixTimeMilliseconds()
  conversationId = "fabio-personal"
  contactName    = "Fabio"
  from           = "5511982123896"
  direction      = "incoming"
  text           = "/status"
  timestamp      = (Get-Date).ToUniversalTime().ToString("o")
  source         = "manual_test"
  provider       = "evolution_api"
} | ConvertTo-Json -Compress

Write-Host "=== /status via Hermes (personal) ===" -ForegroundColor Cyan
$r = Invoke-RestMethod -Uri "http://127.0.0.1:3847/integrations/whatsapp/personal/message" `
  -Method POST -ContentType "application/json; charset=utf-8" `
  -Body ([System.Text.Encoding]::UTF8.GetBytes($body))

$r | ConvertTo-Json -Depth 5
Write-Host ""
if ($r.sentToFabio) {
  Write-Host "[OK] Resposta ENVIADA para seu WhatsApp" -ForegroundColor Green
} elseif ($r.replyToFabio) {
  Write-Host "Resposta preparada (nao enviada):" -ForegroundColor Yellow
  Write-Host $r.replyToFabio
}
