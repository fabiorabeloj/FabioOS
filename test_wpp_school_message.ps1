$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$env:WHATSAPP_SCHOOL_ENABLED = "true"

$body = @{
  messageId      = "wa-test-school-" + [DateTimeOffset]::UtcNow.ToUnixTimeMilliseconds()
  conversationId = "responsavel-001"
  contactName    = "Responsavel Teste"
  from           = "5511888888888"
  direction      = "incoming"
  text           = "Professor, meu filho perdeu a prova. O que faco?"
  timestamp      = (Get-Date).ToUniversalTime().ToString("o")
  source         = "manual_test"
  provider       = "evolution_api"
} | ConvertTo-Json -Compress

Write-Host "=== Mensagem escolar -> Pietra ===" -ForegroundColor Cyan
Write-Host "Nota: reinicie backend com WHATSAPP_SCHOOL_ENABLED=true para canal escolar permanente" -ForegroundColor Yellow

try {
  $r = Invoke-RestMethod -Uri "http://127.0.0.1:3847/integrations/whatsapp/school/message" `
    -Method POST -ContentType "application/json; charset=utf-8" `
    -Body ([System.Text.Encoding]::UTF8.GetBytes($body))
  $r | ConvertTo-Json -Depth 5
  Write-Host ""
  Write-Host "Rascunho sugerido (draft_only):" -ForegroundColor Green
  Write-Host $r.suggestedReply
} catch {
  Write-Host "Canal escolar desabilitado. Rode: `$env:WHATSAPP_SCHOOL_ENABLED='true'; .\start_agentarium.ps1" -ForegroundColor Red
  throw
}
