# Bugbot Onda 1 — smoke das entradas sensoriais FabioOS
# Uso: .\60_Sistemas\FabioOS\scripts\smoke_intake_onda1.ps1
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

Test-Step "email_intake_dry_run (sample)" {
    python 60_Sistemas/FabioOS/scripts/email_intake_dry_run.py `
        --input 60_Sistemas/FabioOS/examples/email_intake_sample.json --stdout | Out-Null
}

Test-Step "email_intake_dry_run (empty rejeita)" {
    python 60_Sistemas/FabioOS/scripts/email_intake_dry_run.py `
        --input 60_Sistemas/FabioOS/examples/email_empty.json 2>$null
    if ($LASTEXITCODE -ne 1) { throw "esperado exit 1, got $LASTEXITCODE" }
    $global:LASTEXITCODE = 0
}

Test-Step "intake_flow (MEGATRON Core)" {
    python 60_Sistemas/MEGATRON/v1/intake_flow.py | Out-Null
    if (-not (Test-Path "60_Sistemas/MEGATRON/v1/state/intake_queue.json")) {
        throw "intake_queue.json ausente"
    }
}

Test-Step "watch_pdf_drop (dry-run)" {
    python 60_Sistemas/FabioOS/scripts/watch_pdf_drop.py --once --dry-run | Out-Null
}

Test-Step "pietra_inbox (sensivel bloqueado)" {
    $out = python 60_Sistemas/Pietra/pietra_inbox.py "Segue o atestado do meu filho, passou mal" --tenant demo-pro 2>&1 | Out-String
    if ($out -notmatch "bloquear_humano|SENS") { throw "bloqueio sensivel nao detectado na saida" }
}

Test-Step "pietra_state (demo-pro)" {
    python 60_Sistemas/Pietra/pietra_state.py --tenant demo-pro | Out-Null
    if (-not (Test-Path "60_Sistemas/Pietra/tenants/demo-pro/pietra_state.json")) {
        throw "pietra_state.json ausente"
    }
}

Test-Step "dashboard_fabioos" {
    python 60_Sistemas/FabioOS/scripts/dashboard_fabioos.py | Out-Null
}

Test-Step "agentarium backend build" {
    Push-Location apps/agentarium/backend
    npm run build --silent 2>$null
    Pop-Location
}

Write-Host "`n--- Resultado: $($fail) falha(s) ---" -ForegroundColor $(if ($fail -eq 0) { "Green" } else { "Red" })
exit $fail
