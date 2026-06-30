# Envia evento de teste ao agente Codex (UTF-8 explicito).
# Requer backend em http://127.0.0.1:3847

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$body = '{"state":"waiting_approval","task":"PR aguardando Fabio","zone":"GitHub"}'

Write-Host "POST /agents/codex/state" -ForegroundColor Cyan

$result = Invoke-RestMethod -Uri "http://127.0.0.1:3847/agents/codex/state" -Method POST `
    -ContentType "application/json; charset=utf-8" `
    -Body ([System.Text.Encoding]::UTF8.GetBytes($body))

Write-Host "[OK] Agente atualizado:" -ForegroundColor Green
$result.agent | Format-List id, name, state, task, zone, updatedAt
