$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$body = @{
  messageId      = "wa-test-personal-" + [DateTimeOffset]::UtcNow.ToUnixTimeMilliseconds()
  conversationId = "test-personal"
  contactName    = "Contato Teste"
  from           = "5511999999999"
  direction      = "incoming"
  text           = "Fabio, consegue me responder depois sobre aquele assunto?"
  timestamp      = (Get-Date).ToUniversalTime().ToString("o")
  source         = "manual_test"
  provider       = "evolution_api"
} | ConvertTo-Json -Compress

Write-Host "=== Mensagem pessoal -> Hermes ===" -ForegroundColor Cyan
$r = Invoke-RestMethod -Uri "http://127.0.0.1:3847/integrations/whatsapp/personal/message" `
  -Method POST -ContentType "application/json; charset=utf-8" `
  -Body ([System.Text.Encoding]::UTF8.GetBytes($body))
$r | ConvertTo-Json -Depth 5
