# Importa/atualiza o workflow WhatsApp -> Hermes/Pietra no n8n (Docker)
$ErrorActionPreference = "Continue"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$WorkflowFile = Join-Path $RepoRoot "60_Sistemas\n8n\Workflows\FabioOS_WhatsApp_Pietra.json"
$ImportFile = Join-Path $env:TEMP "FabioOS_WhatsApp_Pietra_import.json"
$ContainerPath = "/tmp/FabioOS_WhatsApp_Pietra_import.json"
$WorkflowId = "fabioosWhatsappPietraV2"

Write-Host "=== Sync n8n WhatsApp Workflow ===" -ForegroundColor Cyan

$running = docker ps --filter "name=n8n" --format "{{.Names}}" 2>$null
if (-not $running) {
  Write-Host "n8n nao esta rodando. Execute: docker start n8n" -ForegroundColor Red
  exit 1
}

if (-not (Test-Path $WorkflowFile)) {
  throw "Arquivo nao encontrado: $WorkflowFile"
}

$wf = Get-Content $WorkflowFile -Raw -Encoding UTF8 | ConvertFrom-Json
$wf | Add-Member -NotePropertyName "id" -NotePropertyValue $WorkflowId -Force
$wf.active = $true
$json = @($wf) | ConvertTo-Json -Depth 30 -Compress:$false
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllText($ImportFile, $json, $utf8NoBom)

Write-Host "Copiando workflow para container n8n..." -ForegroundColor Yellow
docker cp $ImportFile "n8n:${ContainerPath}"

Write-Host "Importando (atualiza workflow $WorkflowId)..." -ForegroundColor Yellow
docker exec n8n n8n import:workflow --input=$ContainerPath 2>&1 | ForEach-Object { Write-Host $_ }

Write-Host "Publicando workflow..." -ForegroundColor Yellow
docker exec n8n n8n publish:workflow --id=$WorkflowId 2>&1 | ForEach-Object { Write-Host $_ }

Write-Host "Reiniciando n8n para aplicar webhook..." -ForegroundColor Yellow
docker restart n8n | Out-Null
Start-Sleep -Seconds 18

Write-Host ""
Write-Host "[OK] Workflow atualizado e publicado." -ForegroundColor Green
Write-Host "Webhook: http://127.0.0.1:5678/webhook/whatsapp-pietra-v2" -ForegroundColor Cyan
Write-Host "Teste:   .\test_n8n_webhook_personal.ps1" -ForegroundColor Cyan
