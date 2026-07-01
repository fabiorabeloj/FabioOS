# Diagnostico rapido MEGATRON WhatsApp
$ErrorActionPreference = "Continue"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$ok = 0; $fail = 0
function Check($name, $scriptBlock) {
  try {
    & $scriptBlock
    Write-Host "[OK] $name" -ForegroundColor Green
    $script:ok++
  } catch {
    Write-Host "[FALHA] $name — $($_.Exception.Message)" -ForegroundColor Red
    $script:fail++
  }
}

Check "Agentarium /health" {
  $h = Invoke-RestMethod http://127.0.0.1:3847/health -TimeoutSec 5
  if (-not $h.ok) { throw "ok=false" }
  Write-Host "       v$($h.version)" -ForegroundColor DarkGray
}

Check "WhatsApp status" {
  Invoke-RestMethod http://127.0.0.1:3847/integrations/whatsapp/status -TimeoutSec 5 | Out-Null
}

Check "n8n container" {
  $n = docker ps --filter "name=n8n" --format "{{.Names}}" 2>$null
  if (-not $n) { throw "n8n parado" }
}

Check "Evolution open" {
  $k = (Get-Content "$env:USERPROFILE\.fabioos\secrets\evolution_api_key.txt" -Raw).Trim()
  $s = (Invoke-RestMethod "http://127.0.0.1:8080/instance/connectionState/fabioos-pessoal" -Headers @{apikey=$k}).instance.state
  if ($s -ne "open") { throw "state=$s" }
}

Check "n8n webhook (ola)" {
  $payload = @{
    event = "messages.upsert"; instance = "fabioos-pessoal"
    data = @{
      key = @{ remoteJid = "5511982123896@s.whatsapp.net"; fromMe = $true }
      message = @{ conversation = "ola" }
      pushName = "Fabio"; messageTimestamp = [int][double]::Parse((Get-Date -UFormat %s))
    }
  } | ConvertTo-Json -Depth 6 -Compress
  $r = Invoke-RestMethod -Uri "http://127.0.0.1:5678/webhook/whatsapp-pietra-v2" -Method POST `
    -ContentType "application/json; charset=utf-8" `
    -Body ([System.Text.Encoding]::UTF8.GetBytes($payload))
  if ($r.status -ne "hermes" -and $r.status -ne "ok") { throw ($r | ConvertTo-Json -Compress) }
  if (-not $r.jobId) { throw "sem jobId" }
  Write-Host "       jobId=$($r.jobId)" -ForegroundColor DarkGray
}

Write-Host ""
Write-Host "Resultado: $ok OK, $fail falha(s)" -ForegroundColor $(if ($fail -eq 0) { "Green" } else { "Yellow" })
if ($fail -gt 0) { Write-Host "Corrija com: .\start_megatron_whatsapp.ps1" -ForegroundColor Cyan }
