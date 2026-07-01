param(
  [string]$Text = "/status"
)

# Simula webhook Evolution (fabioos-pessoal) -> n8n -> Agentarium Hermes
$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$payload = @{
  event    = "messages.upsert"
  instance = "fabioos-pessoal"
  data     = @{
    key = @{
      remoteJid = "5511982123896@s.whatsapp.net"
      fromMe    = $true
    }
    message          = @{ conversation = $Text }
    pushName         = "Fabio"
    messageTimestamp = [int][double]::Parse((Get-Date -UFormat %s))
  }
} | ConvertTo-Json -Depth 6 -Compress

Write-Host "=== n8n webhook personal (texto: $Text) ===" -ForegroundColor Cyan

try {
  $r = Invoke-RestMethod -Uri "http://127.0.0.1:5678/webhook/whatsapp-pietra-v2" -Method POST `
    -ContentType "application/json; charset=utf-8" `
    -Body ([System.Text.Encoding]::UTF8.GetBytes($payload))
  Write-Host "[OK] n8n respondeu:" -ForegroundColor Green
  $r | ConvertTo-Json -Depth 5
} catch {
  Write-Host "[ERRO] n8n webhook falhou: $($_.Exception.Message)" -ForegroundColor Red
  Write-Host "Rode: .\sync_n8n_whatsapp_workflow.ps1" -ForegroundColor Yellow
  exit 1
}

Write-Host ""
Write-Host "=== Agentarium status ===" -ForegroundColor Cyan
Invoke-RestMethod -Uri "http://127.0.0.1:3847/integrations/whatsapp/status" | ConvertTo-Json -Depth 5

if ($r.sentToFabio) {
  Write-Host ""
  Write-Host "[OK] Resposta ENVIADA no seu WhatsApp (chat Voce)" -ForegroundColor Green
  Write-Host $r.replyToFabio -ForegroundColor DarkCyan
} elseif ($r.deliveryError) {
  Write-Host ""
  Write-Host "[ERRO] Nao enviou WPP: $($r.deliveryError)" -ForegroundColor Red
} elseif ($r.replyToFabio) {
  Write-Host ""
  Write-Host "Resposta preparada (nao enviada):" -ForegroundColor Yellow
  Write-Host $r.replyToFabio
}
