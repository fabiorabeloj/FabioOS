param(
    [int]$Port = 8819,
    [switch]$NoOpen
)

$ErrorActionPreference = "Stop"

$AppDir = "C:\Users\user\Desktop\Projeto\primus-site"
$DbPath = Join-Path $AppDir "primus.sqlite"
$AppPath = Join-Path $AppDir "app.py"
$OutLog = Join-Path $AppDir "primus_index_uvicorn.log"
$ErrLog = Join-Path $AppDir "primus_index_uvicorn.err.log"

if (-not (Test-Path -LiteralPath $AppPath)) {
    throw "PRIMUS Index app.py nao encontrado em $AppPath"
}

if (-not (Test-Path -LiteralPath $DbPath)) {
    throw "Banco PRIMUS nao encontrado em $DbPath"
}

$existing = Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue |
    Where-Object { $_.State -eq "Listen" }

if (-not $existing) {
    Start-Process -FilePath "python" `
        -ArgumentList @("-m", "uvicorn", "app:app", "--host", "127.0.0.1", "--port", "$Port") `
        -WorkingDirectory $AppDir `
        -WindowStyle Hidden `
        -RedirectStandardOutput $OutLog `
        -RedirectStandardError $ErrLog | Out-Null

    Start-Sleep -Seconds 3
}

$url = "http://127.0.0.1:$Port/"
$response = Invoke-WebRequest -UseBasicParsing -Uri $url -TimeoutSec 10

if ($response.StatusCode -ne 200) {
    throw "PRIMUS Index respondeu HTTP $($response.StatusCode)"
}

Write-Output "PRIMUS Index ativo: $url"

if (-not $NoOpen) {
    Start-Process $url | Out-Null
}
