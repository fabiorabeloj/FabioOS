# Bugbot — ciclo completo Intake Universal (ponta a ponta)
# Uso: .\60_Sistemas\FabioOS\scripts\smoke_intake_ciclo_completo.ps1
$ErrorActionPreference = "Continue"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
Set-Location $Root

$fail = 0
function Test-Step($Name, [scriptblock]$Block) {
    Write-Host "`n== $Name ==" -ForegroundColor Cyan
    try {
        & $Block
        if ($LASTEXITCODE -ne 0 -and $null -ne $LASTEXITCODE) { throw "exit $LASTEXITCODE" }
        Write-Host "OK" -ForegroundColor Green
    } catch {
        Write-Host "FAIL: $_" -ForegroundColor Red
        $script:fail++
    }
}

$Megatron = Join-Path $Root "60_Sistemas\MEGATRON\v1"
$Triagem = Join-Path $Root "00_Inbox\Triagem"

Test-Step "intake_flow gera fila" {
    python (Join-Path $Megatron "intake_flow.py") | Out-Null
    if (-not (Test-Path (Join-Path $Megatron "state\intake_queue.json"))) {
        throw "intake_queue.json ausente"
    }
}

Test-Step "aprovar item escolaos (nao sensivel)" {
    $out = python (Join-Path $Megatron "arquivista_intake.py") --aprovar escolaos 2>&1 | Out-String
    if ($out -notmatch "Gravado|executed|Aprovado") {
        throw "aprovacao escolaos falhou: $out"
    }
    $global:LASTEXITCODE = 0
}

Test-Step "nota .md em Triagem" {
    $notes = Get-ChildItem $Triagem -Filter "*.md" -ErrorAction SilentlyContinue | Where-Object {
        $_.LastWriteTime -gt (Get-Date).AddMinutes(-5)
    }
    if (-not $notes) { throw "nenhuma nota recente em 00_Inbox/Triagem" }
}

Test-Step "aprovar sensivel bloqueia gravacao" {
    $out = python (Join-Path $Megatron "arquivista_intake.py") --aprovar saude 2>&1 | Out-String
    if ($out -notmatch "NAO virou nota|blocked|trava") {
        throw "trava sensivel nao funcionou"
    }
    $global:LASTEXITCODE = 0
}

Test-Step "validator fila pos-aprovacao" {
    python 60_Sistemas/FabioOS/scripts/universal_intake_validator.py `
        --input 60_Sistemas/MEGATRON/v1/state/intake_queue.json | Out-Null
}

Test-Step "comando natural via adapter" {
    $out = python 60_Sistemas/FabioOS/scripts/universal_intake_adapter.py --stdout `
        --input 60_Sistemas/FabioOS/examples/intake_gmail_fake.json 2>&1 | Out-String
    if ($out -notmatch "escolaos") { throw "adapter falhou: $out" }
    $global:LASTEXITCODE = 0
}

Test-Step "extrator comando natural" {
    python 60_Sistemas/FabioOS/scripts/intake_command_extract.py --self-test | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "extrator self-test falhou" }
    $ext = python 60_Sistemas/FabioOS/scripts/intake_command_extract.py --text "prova do 8o ano sobre Africa para amanha" 2>&1 | Out-String
    if ($ext -notmatch "prova" -or $ext -notmatch "Africa") { throw "extracao falhou: $ext" }
    $global:LASTEXITCODE = 0
}

Write-Host "`n--- Ciclo intake: $($fail) falha(s) ---" -ForegroundColor $(if ($fail -eq 0) { "Green" } else { "Red" })
exit $fail
