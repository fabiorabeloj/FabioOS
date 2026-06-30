# MEGATRON com CÉREBRO LOCAL (Ollama, CPU). O Maestro RACIOCINA sem Claude/API.
# Uso:   .\brain.ps1 "Qual e a fase atual do FabioOS?"
# Nota:  GTX 1050 Ti quebra com CUDA -> roda em CPU (lento, ~1-3 min). GPU moderna = instantâneo.
param([Parameter(ValueFromRemainingArguments = $true)][string[]]$Pergunta)
$ErrorActionPreference = "SilentlyContinue"
$env:OLLAMA_NUM_GPU = "0"            # força CPU (1050 Ti incompatível)
$env:CUDA_VISIBLE_DEVICES = "-1"

# 1. Garante o servidor Ollama no ar
$up = $false
try { $up = (Invoke-WebRequest http://localhost:11434/api/tags -UseBasicParsing -TimeoutSec 3).StatusCode -eq 200 } catch {}
if (-not $up) {
    Write-Host "[brain] subindo Ollama (CPU-only)..." -ForegroundColor Cyan
    Start-Process -FilePath "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe" -ArgumentList "serve" -WindowStyle Hidden
    Start-Sleep 5
}

if (-not $Pergunta) {
    Write-Host "Uso: .\brain.ps1 `"sua pergunta`"" -ForegroundColor Yellow
    exit 1
}

# 2. MEGATRON com cérebro local (--llm)
$venv = Join-Path $PSScriptRoot "..\..\RAG\.venv\Scripts\python.exe"
Write-Host "[brain] MEGATRON raciocinando localmente (CPU, pode levar 1-3 min)..." -ForegroundColor Cyan
& $venv (Join-Path $PSScriptRoot "megatron.py") @Pergunta --llm
