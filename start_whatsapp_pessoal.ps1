# WhatsApp pessoal FabioOS - Evolution API
# Metodos: -Method Pairing (codigo 8 digitos) | -Method Manager (painel web) | -Method Qr
# Numero: 5511982123896 (+55 11 98212-3896)

param(
  [ValidateSet("Pairing", "Manager", "Qr", "Auto")]
  [string]$Method = "Auto",
  [switch]$Reset
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

$SecretsDir = Join-Path $env:USERPROFILE ".fabioos\secrets"
$ApiKeyFile = Join-Path $SecretsDir "evolution_api_key.txt"
$InstanceName = "fabioos-pessoal"
$PhoneNumber = "5511982123896"
$EvolutionBase = "http://127.0.0.1:8080"
$ManagerUrl = "$EvolutionBase/manager"
$N8nWebhook = "http://host.docker.internal:5678/webhook/whatsapp-pietra-v2"
$LinkHtml = Join-Path $env:TEMP "fabioos-whatsapp-link.html"

function Get-EvolutionApiKey {
  if (-not (Test-Path $ApiKeyFile)) {
    throw "Chave nao encontrada em $ApiKeyFile"
  }
  return (Get-Content $ApiKeyFile -Raw).Trim()
}

function Invoke-Evolution {
  param([string]$Method, [string]$Path, [object]$Body = $null)
  $key = Get-EvolutionApiKey
  $headers = @{ apikey = $key }
  $uri = "$EvolutionBase$Path"
  if ($Body) {
    $json = $Body | ConvertTo-Json -Depth 8 -Compress
    return Invoke-RestMethod -Uri $uri -Method $Method -Headers $headers `
      -ContentType "application/json; charset=utf-8" `
      -Body ([System.Text.Encoding]::UTF8.GetBytes($json))
  }
  return Invoke-RestMethod -Uri $uri -Method $Method -Headers $headers
}

function Ensure-EvolutionUp {
  $status = docker ps -a --filter "name=evolution-api" --format "{{.Status}}" 2>$null
  if ($status -match "Exited|Created") {
    Write-Host "Iniciando stack Evolution..." -ForegroundColor Yellow
    docker start evolution-postgres evolution-redis evolution-api | Out-Null
    Start-Sleep -Seconds 15
  }
  Invoke-WebRequest -Uri $EvolutionBase -TimeoutSec 20 -UseBasicParsing | Out-Null
  Write-Host "[OK] Evolution API online" -ForegroundColor Green
}

function Ensure-Instance {
  $instances = @(Invoke-Evolution -Method GET -Path "/instance/fetchInstances")
  $existing = $instances | Where-Object { $_.name -eq $InstanceName -or $_.instanceName -eq $InstanceName }
  if (-not $existing) {
    Write-Host "Criando instancia $InstanceName ..." -ForegroundColor Yellow
    Invoke-Evolution -Method POST -Path "/instance/create" -Body @{
      instanceName = $InstanceName
      integration  = "WHATSAPP-BAILEYS"
      number       = $PhoneNumber
      qrcode       = $true
    } | Out-Null
    Start-Sleep -Seconds 4
  }
}

function Reset-InstanceSession {
  Write-Host "Reiniciando sessao (logout)..." -ForegroundColor Yellow
  try {
    Invoke-Evolution -Method DELETE -Path "/instance/logout/$InstanceName" | Out-Null
    Start-Sleep -Seconds 3
  } catch {
    Write-Host "[INFO] Logout opcional ignorado" -ForegroundColor DarkGray
  }
}

function Remove-InstanceCompletely {
  Write-Host "Removendo instancia $InstanceName (sessao corrompida)..." -ForegroundColor Yellow
  try {
    Invoke-Evolution -Method DELETE -Path "/instance/logout/$InstanceName" | Out-Null
    Start-Sleep -Seconds 2
  } catch { }
  try {
    Invoke-Evolution -Method DELETE -Path "/instance/delete/$InstanceName" | Out-Null
    Start-Sleep -Seconds 4
    Write-Host "[OK] Instancia removida" -ForegroundColor Green
  } catch {
    Write-Host "[WARN] Delete falhou ou instancia inexistente" -ForegroundColor DarkYellow
  }
}

function Open-ManagerPage {
  $managerHtml = Join-Path $env:TEMP "fabioos-evolution-manager.html"
  $html = @"
<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>FabioOS Evolution Manager</title>
<style>
body{background:#0a0f0a;color:#e5e7eb;font-family:Consolas,monospace;max-width:640px;margin:2rem auto;padding:1rem}
h1{color:#4ade80;font-size:1.1rem}
.steps li{margin:.6rem 0;line-height:1.55}
a.btn{display:inline-block;margin:1rem 0;padding:.75rem 1.25rem;background:#22c55e;color:#052e16;text-decoration:none;font-weight:bold;border-radius:6px}
.warn{color:#fbbf24}
</style></head>
<body>
<h1>MEGATRON - Evolution Manager (WhatsApp Web UI)</h1>
<p>Instancia: <strong>$InstanceName</strong></p>
<p class="warn">O WhatsApp Desktop no PC <em>nao</em> compartilha sessao com a Evolution.
Voce vincula um <strong>novo dispositivo</strong> (como mais um WhatsApp Web).</p>
<ol class="steps">
<li>Clique no botao abaixo para abrir o Manager</li>
<li>Se pedir API Key, use o arquivo em <code>%USERPROFILE%\.fabioos\secrets\evolution_api_key.txt</code></li>
<li>Selecione <strong>$InstanceName</strong> &rarr; <strong>Connect</strong></li>
<li>Escaneie o QR com o celular (Dispositivos conectados &rarr; Conectar dispositivo)</li>
</ol>
<a class="btn" href="$ManagerUrl" target="_blank">Abrir Evolution Manager</a>
</body></html>
"@
  Set-Content -Path $managerHtml -Value $html -Encoding UTF8
  Write-Host "[OK] Manager helper: $managerHtml" -ForegroundColor Green
  Start-Process $managerHtml
  Start-Process $ManagerUrl
}

function Get-ConnectionState {
  $r = Invoke-Evolution -Method GET -Path "/instance/connectionState/$InstanceName"
  if ($r.instance.state) { return $r.instance.state }
  return $r.state
}

function Request-PairingCode {
  Write-Host "Solicitando codigo de pareamento (estilo WhatsApp Web)..." -ForegroundColor Cyan
  $connect = $null
  $paths = @(
    "/instance/connect/$InstanceName`?number=$PhoneNumber",
    "/instance/connect/$InstanceName"
  )
  foreach ($p in $paths) {
    try {
      $connect = Invoke-Evolution -Method GET -Path $p
      if ($connect) { break }
    } catch {
      continue
    }
  }
  if (-not $connect) {
    try {
      $connect = Invoke-Evolution -Method POST -Path "/instance/connect" -Body @{
        instanceName = $InstanceName
        number       = $PhoneNumber
      }
    } catch {
      Write-Host "[WARN] POST /instance/connect falhou" -ForegroundColor DarkYellow
    }
  }
  return $connect
}

function Show-LinkPage {
  param($Connect, [string]$ModeLabel)
  $pairing = $null
  if ($Connect.pairingCode) { $pairing = $Connect.pairingCode }
  elseif ($Connect.qrcode.pairingCode) { $pairing = $Connect.qrcode.pairingCode }
  $b64 = $Connect.base64
  if (-not $b64) { $b64 = $Connect.qrcode.base64 }
  if ($b64 -and $b64 -notmatch "^data:image") { $b64 = "data:image/png;base64," + $b64 }

  $pairingBlock = if ($pairing) {
    "<div class='code'>$pairing</div><p>Digite em ate 60 segundos</p>"
  } else {
    "<p class='warn'>Codigo nao retornado - use o Manager abaixo</p>"
  }

  $qrBlock = if ($b64) {
    "<hr/><p>Ou escaneie QR (WhatsApp Web):</p><img src='$b64' alt='QR'/>"
  } else { "" }

  $html = @"
<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>FabioOS WhatsApp Link</title>
<meta http-equiv="refresh" content="45"/>
<style>
body{background:#0a0f0a;color:#e5e7eb;font-family:Consolas,monospace;max-width:520px;margin:2rem auto;padding:1rem}
h1{color:#4ade80;font-size:1.1rem}
.code{font-size:2.4rem;letter-spacing:.25em;color:#facc15;border:3px solid #facc15;padding:1rem;margin:1rem 0;font-weight:bold}
.steps li{margin:.5rem 0;line-height:1.5}
.warn{color:#fbbf24}
a{color:#22d3ee}
img{max-width:280px;border:3px solid #22c55e;margin-top:1rem}
</style></head>
<body>
<h1>MEGATRON - Vincular WhatsApp ($ModeLabel)</h1>
<p>Numero: +55 11 98212-3896</p>
<h2>Codigo de pareamento</h2>
$pairingBlock
<ol class="steps">
<li>Abra <strong>WhatsApp</strong> no celular</li>
<li><strong>Menu</strong> - <strong>Dispositivos conectados</strong></li>
<li><strong>Conectar dispositivo</strong></li>
<li><strong>Conectar com numero de telefone</strong> (nao QR)</li>
<li>Digite o codigo acima</li>
</ol>
$qrBlock
<p><a href="$ManagerUrl" target="_blank">Evolution Manager (painel web)</a></p>
<p class="warn">Pagina atualiza a cada 45s para codigo novo</p>
</body></html>
"@
  Set-Content -Path $LinkHtml -Value $html -Encoding UTF8
  Write-Host "[OK] Pagina: $LinkHtml" -ForegroundColor Green
  Start-Process $LinkHtml
}

Write-Host "=== FabioOS WhatsApp Pessoal ===" -ForegroundColor Cyan
Write-Host "Metodo: $Method | Instancia: $InstanceName"

Ensure-EvolutionUp

if ($Reset) {
  Remove-InstanceCompletely
}

Ensure-Instance

try {
  Invoke-Evolution -Method POST -Path "/webhook/set/$InstanceName" -Body @{
    enabled = $true; url = $N8nWebhook; webhookByEvents = $false
    webhookBase64 = $false; events = @("MESSAGES_UPSERT")
  } | Out-Null
} catch { }

$state = Get-ConnectionState
Write-Host "Estado: $state"

if ($state -eq "open") {
  Write-Host "[OK] Ja conectado! Rode: .\test_whatsapp_pessoal.ps1" -ForegroundColor Green
  exit 0
}

if ($Method -eq "Auto") { $Method = "Pairing" }

if ($Method -eq "Manager") {
  Write-Host "Abrindo Evolution Manager (WhatsApp Web UI)..." -ForegroundColor Cyan
  if ($state -ne "open") {
    Reset-InstanceSession
    try {
      Invoke-Evolution -Method GET -Path "/instance/connect/$InstanceName" | Out-Null
    } catch { }
  }
  Open-ManagerPage
  Write-Host "Aguardando conexao (120s). Escaneie QR ou use pairing no Manager..." -ForegroundColor Cyan
  $deadline = (Get-Date).AddSeconds(120)
  while ((Get-Date) -lt $deadline) {
    Start-Sleep -Seconds 5
    $state = Get-ConnectionState
    Write-Host "  estado: $state"
    if ($state -eq "open") {
      Write-Host "[OK] Conectado! Rode: .\test_whatsapp_pessoal.ps1" -ForegroundColor Green
      exit 0
    }
  }
  Write-Host "[INFO] Ainda nao conectou. Mantenha o Manager aberto e repita o scan." -ForegroundColor Yellow
  exit 1
}

Reset-InstanceSession
$connect = Request-PairingCode

if ($Method -eq "Pairing" -or $Method -eq "Auto") {
  Show-LinkPage -Connect $connect -ModeLabel "Pairing Code"
}

if ($Method -eq "Qr") {
  Show-LinkPage -Connect $connect -ModeLabel "QR Code"
}

Write-Host ""
Write-Host "Alternativa: .\start_whatsapp_pessoal.ps1 -Method Manager" -ForegroundColor Cyan
Write-Host "Manager: $ManagerUrl" -ForegroundColor Cyan
Write-Host "Apos conectar: .\test_whatsapp_pessoal.ps1"
