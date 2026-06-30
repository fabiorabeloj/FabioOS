# MEGATRON Maestro (modo padrão: recuperação, custo-zero, sem LLM, rápido).
# Uso:   .\megatron.ps1                       -> briefing "bom dia"
#        .\megatron.ps1 "o que voce pode fazer?"
#        .\megatron.ps1 "pesquise https://exemplo.com"
#        .\megatron.ps1 "criar nota X" --confirmar
# Para o cérebro local (raciocínio): use .\brain.ps1 "..."
param([Parameter(ValueFromRemainingArguments = $true)][string[]]$CmdArgs)
$venv = Join-Path $PSScriptRoot "..\..\RAG\.venv\Scripts\python.exe"
& $venv (Join-Path $PSScriptRoot "megatron.py") @CmdArgs
