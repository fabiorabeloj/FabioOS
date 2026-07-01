# Smoke - MEGATRON launcher
# Uso: .\60_Sistemas\FabioOS\scripts\smoke_megatron_launcher.ps1

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

Test-Step "MEGATRON.cmd existe" {
    if (-not (Test-Path (Join-Path $Root "MEGATRON.cmd"))) { throw "ausente" }
}

Test-Step "megatron_lib resolve vault" {
    $lib = Join-Path $Root "60_Sistemas\Scripts\megatron_lib.ps1"
    . $lib
    $v = Get-MegatronVaultRoot -FromScriptPath $lib
    if ($v -ne $Root) { throw "vault=$v esperado=$Root" }
}

Test-Step "launcher diagnostico + JsonOnly" {
    $out = powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $Root "start_megatron.ps1") -Diagnostico -JsonOnly 2>&1 | Out-String
    if ($out -notmatch "vault_root") { throw $out }
    $global:LASTEXITCODE = 0
}

Test-Step "megatron_health -Json" {
    powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $Root "60_Sistemas\Scripts\megatron_health.ps1") -Json | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "health exit $LASTEXITCODE" }
}

Test-Step "orchestrator spec existe" {
    if (-not (Test-Path (Join-Path $Root "60_Sistemas\FabioOS\specs\2026-06-29_MEGATRON_Orchestrator_v1.0.md"))) {
        throw "spec ausente"
    }
}

Test-Step "megatron_orchestrate.ps1 carrega" {
    powershell -NoProfile -Command "& { . '$Root\60_Sistemas\Scripts\megatron_lib.ps1'; 'ok' }" | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "lib falhou" }
}

Test-Step "runtime v1.0.0 gerado" {
    $state = Join-Path $Root "60_Sistemas\MEGATRON\v1\state\megatron_runtime.json"
    if (-not (Test-Path $state)) { throw "megatron_runtime.json ausente" }
    $j = Get-Content $state -Raw | ConvertFrom-Json
    if ($j.version -ne "1.0.0") { throw "versao=$($j.version)" }
}

Write-Host "`n--- MEGATRON launcher: $($fail) falha(s) ---" -ForegroundColor $(if ($fail -eq 0) { "Green" } else { "Red" })
exit $fail
