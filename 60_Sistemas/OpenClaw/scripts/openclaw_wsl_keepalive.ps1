# Mantem sessao WSL OpenClawGateway viva para o gateway systemd persistir.
# Executar em background apos ensure_openclaw_gateway.ps1 ou no login.

param(
    [switch]$Stop
)

$Distro = "OpenClawGateway"
$PidFile = Join-Path $env:LOCALAPPDATA "OpenClawTray\gateway-keepalive.pid"

if ($Stop) {
    if (Test-Path $PidFile) {
        $keepPid = Get-Content $PidFile -ErrorAction SilentlyContinue
        if ($keepPid) {
            Stop-Process -Id $keepPid -Force -ErrorAction SilentlyContinue
            Write-Host "Keepalive encerrado (PID $keepPid)" -ForegroundColor Yellow
        }
        Remove-Item $PidFile -Force -ErrorAction SilentlyContinue
    }
    exit 0
}

if (Test-Path $PidFile) {
    $existing = Get-Content $PidFile -ErrorAction SilentlyContinue
    if ($existing -and (Get-Process -Id $existing -ErrorAction SilentlyContinue)) {
        Write-Host "[OK] Keepalive ja ativo (PID $existing)" -ForegroundColor Green
        exit 0
    }
}

$proc = Start-Process -FilePath "wsl.exe" `
    -ArgumentList @("-d", $Distro, "--", "bash", "-lc", "systemctl --user start openclaw-gateway.service 2>/dev/null; exec sleep infinity") `
    -WindowStyle Hidden `
    -PassThru

New-Item -ItemType Directory -Force -Path (Split-Path $PidFile) | Out-Null
Set-Content -Path $PidFile -Value $proc.Id -Encoding ascii
Write-Host "[OK] Keepalive WSL iniciado (PID $($proc.Id))" -ForegroundColor Green
