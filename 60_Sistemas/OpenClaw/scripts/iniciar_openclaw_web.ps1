# Inicia o gateway OpenClaw (WSL) e abre o chat no navegador.
# Corrige o caso comum: bind=lan impede http://127.0.0.1:18789 no Windows.

param(
    [string]$Session = "main",
    [switch]$NoBrowser
)

$ErrorActionPreference = "Continue"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$Distro = "OpenClawGateway"
$Port = 18789
$Url = "http://127.0.0.1:$Port/chat?session=$Session"

Write-Host "== OpenClaw Web ==" -ForegroundColor Cyan

$ensureScript = Join-Path $PSScriptRoot "ensure_openclaw_gateway.ps1"
& $ensureScript
if ($LASTEXITCODE -ne 0) {
    exit 1
}

Write-Host "URL: $Url" -ForegroundColor Cyan
if (-not $NoBrowser) {
    Start-Process $Url
}
