# Grava chave OpenRouter para MEGATRON conversacional (sem commitar)
$ErrorActionPreference = "Stop"

$SecretsDir = Join-Path $env:USERPROFILE ".fabioos\secrets"
$KeyFile = Join-Path $SecretsDir "openrouter_api_key.txt"

if (-not (Test-Path $SecretsDir)) {
  New-Item -ItemType Directory -Path $SecretsDir -Force | Out-Null
}

$key = Read-Host "Cole a OPENROUTER_API_KEY (nao sera exibida depois)"
if (-not $key.Trim()) {
  throw "Chave vazia."
}

Set-Content -Path $KeyFile -Value $key.Trim() -Encoding UTF8 -NoNewline
Write-Host "[OK] Salvo em $KeyFile" -ForegroundColor Green
Write-Host "Reinicie o Agentarium: .\start_agentarium.ps1" -ForegroundColor Cyan
