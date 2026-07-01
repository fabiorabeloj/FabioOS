@echo off
setlocal
cd /d "%~dp0"
title MEGATRON - FabioOS
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0start_megatron.ps1" %*
set ERR=%ERRORLEVEL%
if %ERR% NEQ 0 (
  echo.
  echo [MEGATRON] Encerrado com erro %ERR%. Veja o log em 60_Sistemas\MEGATRON\v1\state\megatron_launcher.log
  pause
)
exit /b %ERR%
