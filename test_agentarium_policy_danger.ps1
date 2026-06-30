# Teste de policy — elevar Codex para danger (demo)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$body = @{
  sandboxMode = "off"
  elevated = "enabled"
} | ConvertTo-Json -Compress

Write-Host "POST /agents/codex/policy (demo danger)" -ForegroundColor Cyan

$result = Invoke-RestMethod -Uri "http://127.0.0.1:3847/agents/codex/policy" -Method POST `
  -ContentType "application/json; charset=utf-8" `
  -Body ([System.Text.Encoding]::UTF8.GetBytes($body))

Write-Host "Risk:" $result.agent.policy.riskLevel -ForegroundColor Red
$result.agent.policy.riskNotes | ForEach-Object { Write-Host " - $_" }
