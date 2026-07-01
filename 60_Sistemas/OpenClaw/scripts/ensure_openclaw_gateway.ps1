# Garante gateway OpenClaw operacional sem reiniciar se ja estiver OK.
# Usa bootstrap WSL unificado para evitar loops de SIGTERM.

param(
    [switch]$ForceRestart,
    [int]$MaxWaitSec = 120
)

$ErrorActionPreference = "Continue"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$Distro = "OpenClawGateway"
$Port = 18789
$Url = "http://127.0.0.1:$Port/"
$BootstrapSh = Join-Path $PSScriptRoot "bootstrap_gateway_wsl.sh"

function Test-GatewayHttp {
    param([string]$TargetUrl)
    $result = curl.exe -s -o NUL -w "%{http_code}" --connect-timeout 5 $TargetUrl 2>$null
    if ($LASTEXITCODE -ne 0) { return $false }
    $code = [int]$result
    return ($code -ge 200 -and $code -lt 400)
}

$mutexName = "Global\FabioOS_OpenClaw_Gateway_Ensure"
$mutex = New-Object System.Threading.Mutex($false, $mutexName)
$acquired = $false
if (-not $mutex.WaitOne(0)) {
    Write-Host "[AVISO] Outro ensure ja em execucao; aguardando..." -ForegroundColor Yellow
    $acquired = $mutex.WaitOne(120000)
    if (-not $acquired) {
        Write-Host "[ERRO] Timeout aguardando mutex do gateway." -ForegroundColor Red
        exit 1
    }
} else {
    $acquired = $true
}

$exitCode = 0
try {
    $null = wsl -d $Distro -- echo ok 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERRO] Distro WSL '$Distro' indisponivel." -ForegroundColor Red
        $exitCode = 1
    } elseif (-not $ForceRestart -and (Test-GatewayHttp -TargetUrl $Url)) {
        Write-Host "[OK] Gateway ja operacional em $Url" -ForegroundColor Green
        $exitCode = 0
    } else {
        if ($ForceRestart) {
            Write-Host "Reiniciando gateway via bootstrap WSL..." -ForegroundColor Yellow
        } else {
            Write-Host "Gateway parado; subindo via bootstrap WSL..." -ForegroundColor Yellow
        }

        if (-not (Test-Path $BootstrapSh)) {
            Write-Host "[ERRO] Script nao encontrado: $BootstrapSh" -ForegroundColor Red
            $exitCode = 1
        } else {
            if ($ForceRestart) {
                $env:FORCE_RESTART = "1"
            } else {
                Remove-Item Env:FORCE_RESTART -ErrorAction SilentlyContinue
            }
            $env:MAX_WAIT = "$MaxWaitSec"
            Get-Content $BootstrapSh -Raw | wsl -d $Distro -- bash -s
            if ($LASTEXITCODE -ne 0) {
                $exitCode = 1
            } elseif (Test-GatewayHttp -TargetUrl $Url) {
                Write-Host "[OK] Gateway acessivel do Windows em $Url" -ForegroundColor Green
                $keepalive = Join-Path $PSScriptRoot "openclaw_wsl_keepalive.ps1"
                if (Test-Path $keepalive) {
                    & $keepalive
                }
                $exitCode = 0
            } else {
                Write-Host "[ERRO] Gateway OK no WSL mas Windows nao alcanca $Url" -ForegroundColor Red
                Write-Host "Aguarde ~10s e tente novamente, ou reinicie a distro: wsl -d $Distro -- echo ok" -ForegroundColor Yellow
                $exitCode = 1
            }
        }
    }
} finally {
    if ($acquired) {
        $mutex.ReleaseMutex() | Out-Null
    }
    $mutex.Dispose()
}

exit $exitCode
