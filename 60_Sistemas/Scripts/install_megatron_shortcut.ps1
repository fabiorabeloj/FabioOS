# Cria atalho MEGATRON na Area de Trabalho (Windows)
# Uso: .\60_Sistemas\Scripts\install_megatron_shortcut.ps1
#      .\60_Sistemas\Scripts\install_megatron_shortcut.ps1 -AlsoStartMenu

param(
    [switch]$AlsoStartMenu,
    [switch]$DiagnosticoShortcut
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$VaultRoot = (Resolve-Path (Join-Path $ScriptDir "..\..")).Path
$EntryCmd = Join-Path $VaultRoot "MEGATRON.cmd"

if (-not (Test-Path $EntryCmd)) {
    Write-Error "MEGATRON.cmd nao encontrado em $VaultRoot"
}

$arguments = if ($DiagnosticoShortcut) { "-Diagnostico" } else { "" }

function New-MegatronShortcut {
    param([string]$TargetPath)

    $shell = New-Object -ComObject WScript.Shell
    $shortcut = $shell.CreateShortcut($TargetPath)
    $shortcut.TargetPath = $EntryCmd
    $shortcut.Arguments = $arguments
    $shortcut.WorkingDirectory = $VaultRoot
    $shortcut.WindowStyle = 1
    $shortcut.Description = "Iniciar MEGATRON / FabioOS - cockpit unificado (pre-MEGATRON.exe)"
    $shortcut.Save()
}

$desktop = [Environment]::GetFolderPath("Desktop")
$desktopLink = Join-Path $desktop "MEGATRON.lnk"
New-MegatronShortcut -TargetPath $desktopLink
Write-Host "[OK] Atalho criado: $desktopLink" -ForegroundColor Green

if ($AlsoStartMenu) {
    $programs = [Environment]::GetFolderPath("Programs")
    $menuLink = Join-Path $programs "MEGATRON.lnk"
    New-MegatronShortcut -TargetPath $menuLink
    Write-Host "[OK] Atalho criado: $menuLink" -ForegroundColor Green
}

Write-Host ""
Write-Host "Duplo-clique em MEGATRON.lnk para ligar o cockpit completo." -ForegroundColor Cyan
Write-Host "Alternativa: duplo-clique em MEGATRON.cmd na raiz do vault." -ForegroundColor Gray
Write-Host "Diagnostico: .\MEGATRON.cmd -Diagnostico" -ForegroundColor Gray
Write-Host "Health: .\60_Sistemas\Scripts\megatron_health.ps1" -ForegroundColor Gray
