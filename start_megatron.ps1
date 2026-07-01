# MEGATRON — entrada unica do FabioOS (pre-MEGATRON.exe)
# Uso: .\start_megatron.ps1
#      .\start_megatron.ps1 -Diagnostico
#      .\start_megatron.ps1 -NoAgentarium

param(
    [switch]$NoOpenApps,
    [switch]$SkipDocker,
    [switch]$SkipContainers,
    [switch]$SkipBrowser,
    [switch]$NoAgentarium,
    [switch]$Diagnostico,
    [switch]$JsonOnly
)

$ErrorActionPreference = "Stop"
$Launcher = Join-Path $PSScriptRoot "60_Sistemas\Scripts\megatron_launcher.ps1"

if (-not (Test-Path $Launcher)) {
    Write-Error "Launcher nao encontrado: $Launcher"
}

$splat = @{}
if ($NoOpenApps) { $splat.NoOpenApps = $true }
if ($SkipDocker) { $splat.SkipDocker = $true }
if ($SkipContainers) { $splat.SkipContainers = $true }
if ($SkipBrowser) { $splat.SkipBrowser = $true }
if ($Diagnostico) { $splat.Diagnostico = $true }
if ($JsonOnly) { $splat.JsonOnly = $true }
if (-not $NoAgentarium -and -not $Diagnostico) { $splat.WithAgentarium = $true }

& $Launcher @splat
