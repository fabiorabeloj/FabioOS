# Bugbot Onda 2 — seguranca e segredos FabioOS
# Uso: .\60_Sistemas\FabioOS\scripts\smoke_seguranca_onda2.ps1
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

Test-Step "_restrito: so .gitkeep versionado" {
    $tracked = git ls-files | Select-String "_restrito" | Where-Object { $_ -notmatch "\.gitkeep$" }
    if ($tracked) { throw "Arquivos restritos no Git: $tracked" }
}

Test-Step "tenants Pietra nao versionados" {
    $tracked = git ls-files | Select-String "60_Sistemas/Pietra/tenants/"
    if ($tracked) { throw "Tenants no Git: $tracked" }
}

Test-Step "intake_queue live nao versionada" {
    $tracked = git ls-files | Select-String "intake_queue\.json|intake_log\.jsonl"
    if ($tracked) { throw "State intake versionado: $tracked" }
}

Test-Step "validator sample codex" {
    python 60_Sistemas/FabioOS/scripts/universal_intake_validator.py `
        --input 60_Sistemas/FabioOS/examples/universal_intake_queue.codex_sample.json | Out-Null
}

Test-Step "validator sample MEGATRON" {
    python 60_Sistemas/FabioOS/scripts/universal_intake_validator.py `
        --input 60_Sistemas/MEGATRON/v1/examples/intake_queue.sample.json | Out-Null
}

Test-Step "validator fila live (se existir)" {
    $live = "60_Sistemas/MEGATRON/v1/state/intake_queue.json"
    if (Test-Path $live) {
        python 60_Sistemas/FabioOS/scripts/universal_intake_validator.py --input $live | Out-Null
    } else {
        Write-Host "(skip - fila live ausente)" -ForegroundColor Yellow
        $global:LASTEXITCODE = 0
    }
}

Test-Step "adapter rejeita payload vazio" {
    python 60_Sistemas/FabioOS/scripts/universal_intake_adapter.py `
        --input 60_Sistemas/FabioOS/examples/email_empty.json 2>$null
    if ($LASTEXITCODE -ne 1) { throw "esperado exit 1" }
    $global:LASTEXITCODE = 0
}

Test-Step "git grep sk- em arquivos versionados" {
    git grep -E "sk-[A-Za-z0-9]{8,}" -- "*.py" "*.ts" "*.tsx" "*.md" "*.json" 2>$null
    if ($LASTEXITCODE -eq 0) { throw "Possivel token sk- encontrado no Git" }
    $global:LASTEXITCODE = 0
}

Test-Step "email triagem mascara remetente" {
    $md = python 60_Sistemas/FabioOS/scripts/email_intake_dry_run.py `
        --input 60_Sistemas/FabioOS/examples/email_intake_sample.json --stdout 2>&1 | Out-String
    if ($md -notmatch '\*\*\*@') { throw "remetente nao mascarado" }
}

Write-Host "`n--- Resultado: $($fail) falha(s) ---" -ForegroundColor $(if ($fail -eq 0) { "Green" } else { "Red" })
exit $fail
