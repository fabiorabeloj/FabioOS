# Executar agente MEGATRON (implementacao minima)
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('safecommit', 'arquivista', 'inbox', 'rag', 'dashboard')]
    [string]$Agente,

    [string[]]$Args = @()
)

$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$env:PYTHONIOENCODING = 'utf-8'

$Root = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
$Impl = Join-Path $Root '60_Sistemas\MEGATRON\agentes\implementacao\claude'
$RagVenv = Join-Path $Root '60_Sistemas\RAG\.venv\Scripts\python.exe'

$Map = @{
    safecommit = 'safecommit.py'
    arquivista = 'arquivista.py'
    inbox      = 'inbox.py'
    rag        = 'rag_agent.py'
    dashboard  = 'dashboard.py'
}

$Script = Join-Path $Impl $Map[$Agente]
if (-not (Test-Path $Script)) {
    Write-Error "Script nao encontrado: $Script"
}

$Python = if ($Agente -eq 'rag' -and (Test-Path $RagVenv)) { $RagVenv } else { 'python' }

Write-Host "[MEGATRON] $Agente via $Python" -ForegroundColor Cyan
& $Python $Script @Args
