param(
    [switch]$NoOpenApps,
    [switch]$SkipDocker,
    [switch]$SkipContainers,
    [switch]$SkipBrowser
)

$ErrorActionPreference = "Continue"
[Console]::OutputEncoding = New-Object System.Text.UTF8Encoding $false
$OutputEncoding = [Console]::OutputEncoding

$VaultRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Today = Get-Date -Format "yyyy-MM-dd"
$Now = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$ChangelogDir = Join-Path $VaultRoot "50_Registros\Changelog"
$ChangelogFile = Join-Path $ChangelogDir "${Today}_retomada-ambiente-fabioos.md"
$PainelPath = Join-Path $VaultRoot "10_Mapas\Painel_Pendencias_FabioOS.md"

function Write-Section {
    param([string]$Title)
    Write-Host ""
    Write-Host "== $Title ==" -ForegroundColor Cyan
}

function Write-Ok {
    param([string]$Message)
    Write-Host "[OK] $Message" -ForegroundColor Green
}

function Write-Warn {
    param([string]$Message)
    Write-Host "[AVISO] $Message" -ForegroundColor Yellow
}

function Write-Info {
    param([string]$Message)
    Write-Host "[INFO] $Message" -ForegroundColor Gray
}

function Start-IfCommand {
    param(
        [string]$Command,
        [string[]]$Arguments
    )
    $cmd = Get-Command $Command -ErrorAction SilentlyContinue
    if ($cmd) {
        Start-Process -FilePath $cmd.Source -ArgumentList $Arguments
        return $true
    }
    return $false
}

function Open-Url {
    param([string]$Url)
    try {
        Start-Process $Url | Out-Null
        Write-Ok "Aberto: $Url"
    } catch {
        Write-Warn "Nao foi possivel abrir: $Url"
    }
}

function Ensure-Changelog {
    if (!(Test-Path $ChangelogDir)) {
        New-Item -ItemType Directory -Path $ChangelogDir -Force | Out-Null
    }

    if (!(Test-Path $ChangelogFile)) {
        @"
---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: ativo
tags: [fabios, retomada, ambiente, automacao]
criado_em: $Today
atualizado_em: $Today
---

# Retomada do Ambiente FabioOS - $Today

## Eventos

"@ | Set-Content -Path $ChangelogFile -Encoding UTF8
    }

    "- $Now - Ambiente FabioOS retomado via start_fabioos.ps1." | Add-Content -Path $ChangelogFile -Encoding UTF8
    Write-Ok "Retomada registrada em $ChangelogFile"
}

function Show-OperationalSummary {
    Write-Section "Resumo operacional"

    if (Test-Path $PainelPath) {
        $painel = Get-Content -Path $PainelPath -Encoding UTF8
        $next = $painel | Select-String -Pattern "Proximo passo|Pr.ximo passo|COME.CAR AQUI|Fase 12" | Select-Object -First 5
        if ($next) {
            $next | ForEach-Object { Write-Info ($_.Line.Trim()) }
        } else {
            Write-Warn "Painel encontrado, mas sem proximo passo destacado."
        }

        $openTasks = $painel | Select-String -Pattern "^- \[ \]" | Select-Object -First 8
        if ($openTasks) {
            Write-Host ""
            Write-Host "Pendencias abertas mais proximas:" -ForegroundColor Cyan
            $openTasks | ForEach-Object { Write-Host $_.Line }
        }
    } else {
        Write-Warn "Painel de pendencias nao encontrado."
    }

    $statusFiles = Get-ChildItem -Path $VaultRoot -Recurse -File -Include STATUS.md,NEXT_ACTIONS.md,TASKS.md -ErrorAction SilentlyContinue |
        Where-Object { $_.FullName -notmatch "\\\.git\\|\\node_modules\\|\\\.venv\\|\\__pycache__\\" } |
        Select-Object -First 20

    if ($statusFiles) {
        Write-Host ""
        Write-Host "Arquivos de status encontrados:" -ForegroundColor Cyan
        $statusFiles | ForEach-Object { Write-Host ("- " + $_.FullName.Replace($VaultRoot + "\", "")) }
    } else {
        Write-Info "Nenhum STATUS.md, NEXT_ACTIONS.md ou TASKS.md encontrado no vault."
    }
}

Write-Section "FabioOS - retomada de ambiente"
Write-Info "Vault: $VaultRoot"

Set-Location $VaultRoot
Ensure-Changelog

Write-Section "Git"
if (Get-Command git -ErrorAction SilentlyContinue) {
    git -C $VaultRoot status --short
} else {
    Write-Warn "Git nao encontrado no PATH."
}

if (!$NoOpenApps) {
    Write-Section "Aplicativos"

    $obsidianPath = Join-Path $env:LOCALAPPDATA "Obsidian\Obsidian.exe"
    if (Test-Path $obsidianPath) {
        $vaultUri = "obsidian://open?path=$([uri]::EscapeDataString($VaultRoot))"
        Start-Process $vaultUri | Out-Null
        Write-Ok "Obsidian solicitado no vault FabioOS."
    } else {
        Write-Warn "Obsidian nao encontrado no caminho padrao."
    }

    if (Start-IfCommand -Command "cursor" -Arguments @($VaultRoot)) {
        Write-Ok "Cursor aberto no projeto."
    } elseif (Start-IfCommand -Command "code" -Arguments @($VaultRoot)) {
        Write-Ok "VS Code aberto no projeto."
    } else {
        Write-Warn "Cursor/VS Code nao encontrados no PATH."
    }

    $terminalArgs = @("-NoExit", "-Command", "Set-Location -LiteralPath '$VaultRoot'; git status --short")
    if (Start-IfCommand -Command "wt" -Arguments @("powershell", "-NoExit", "-Command", "Set-Location -LiteralPath '$VaultRoot'; git status --short")) {
        Write-Ok "Windows Terminal aberto no projeto."
    } else {
        Start-Process powershell.exe -ArgumentList $terminalArgs
        Write-Ok "PowerShell aberto no projeto."
    }
}

if (!$SkipDocker) {
    Write-Section "Docker / n8n"

    $dockerDesktop = Join-Path $env:ProgramFiles "Docker\Docker\Docker Desktop.exe"
    $dockerProcess = Get-Process -Name "Docker Desktop" -ErrorAction SilentlyContinue
    if (!$dockerProcess -and (Test-Path $dockerDesktop)) {
        Start-Process $dockerDesktop
        Write-Ok "Docker Desktop solicitado."
        Start-Sleep -Seconds 5
    } elseif ($dockerProcess) {
        Write-Ok "Docker Desktop ja esta em execucao."
    } else {
        Write-Warn "Docker Desktop nao encontrado no caminho padrao."
    }

    if (Get-Command docker -ErrorAction SilentlyContinue) {
        docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

        if (!$SkipContainers) {
            $n8nStopped = docker ps -a --filter "name=n8n" --filter "status=exited" --format "{{.Names}}" 2>$null
            if ($n8nStopped) {
                $n8nStopped | ForEach-Object {
                    docker start $_ | Out-Null
                    Write-Ok "Container n8n iniciado: $_"
                }
            } else {
                Write-Info "Nenhum container n8n parado encontrado para iniciar."
            }
        }
    } else {
        Write-Warn "Docker CLI nao encontrado no PATH."
    }
}

if (!$SkipBrowser) {
    Write-Section "Paginas essenciais"
    Open-Url "http://localhost:5678"

    if (Get-Command git -ErrorAction SilentlyContinue) {
        $remote = git -C $VaultRoot remote get-url origin 2>$null
        if ($remote) {
            if ($remote -match "github.com[:/](.+?)(\.git)?$") {
                $repoPath = $Matches[1] -replace "\.git$", ""
                Open-Url "https://github.com/$repoPath"
            }
        }
    }

    Open-Url "https://claude.ai/"
    Open-Url "https://chatgpt.com/"
}

Show-OperationalSummary

Write-Section "Concluido"
Write-Ok "Ambiente FabioOS retomado. Continue pelo painel de pendencias e pelo ultimo changelog."
