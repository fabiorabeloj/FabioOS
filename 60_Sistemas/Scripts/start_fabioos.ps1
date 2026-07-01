# Compat: delega para megatron_launcher.ps1 (corrigido em 2026-06-29)
param(
    [switch]$NoOpenApps,
    [switch]$SkipDocker,
    [switch]$SkipContainers,
    [switch]$SkipBrowser,
    [switch]$WithAgentarium,
    [switch]$Diagnostico,
    [switch]$Quiet
)
$Launcher = Join-Path $PSScriptRoot "megatron_launcher.ps1"
& $Launcher @PSBoundParameters
