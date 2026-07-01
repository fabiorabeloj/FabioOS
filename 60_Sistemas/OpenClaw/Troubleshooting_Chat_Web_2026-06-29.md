---
tipo: troubleshooting
area: 60_Sistemas
sistema: OpenClaw
status: ativo
tags: [openclaw, gateway, 18789, wsl, loopback, chat]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# OpenClaw — chat web nao abre (127.0.0.1:18789)

## Sintoma

`http://127.0.0.1:18789/chat?session=main` no navegador Windows: **nao conecta**.

## Causas encontradas (2026-06-29)

1. **Gateway parado** — servico WSL caiu ou ainda subindo (~15–30 s apos start).
2. **`gateway.bind=lan`** — gateway ouvia em `0.0.0.0` dentro do WSL; Windows nao alcançava `127.0.0.1:18789`.
3. **Reinicios em loop** — `stop/start` repetidos (script antigo, diagnosticos ou Companion) enviam SIGTERM enquanto o gateway sobe; systemd reporta `running` mas a porta ainda nao escuta.
4. **Checagem prematura** — `openclaw gateway status` ou curl antes de ~15 s apos start da falsa impressao de falha.

**Regra:** nao reiniciar se HTTP 200 ja responde. Usar `ensure_openclaw_gateway.ps1`.

## Correcao definitiva (2026-06-29 tarde)

O gateway cai quando ha **varios stop/start concorrentes** (scripts, diagnosticos, browser control-ui). Solucao:

```powershell
# Um unico bootstrap WSL — aguarda ~20-35s ate HTTP 200
Get-Content 60_Sistemas\OpenClaw\scripts\bootstrap_gateway_wsl.sh -Raw | wsl -d OpenClawGateway -- bash -s

# Ou wrapper PowerShell (nao reinicia se ja OK):
60_Sistemas\OpenClaw\scripts\ensure_openclaw_gateway.ps1
```

**Nao** encadear multiplos `wsl ... systemctl stop/start` em paralelo.

### Persistencia WSL

Na distro `OpenClawGateway`, o gateway systemd pode cair quando a sessao WSL termina. O script `ensure_openclaw_gateway.ps1` inicia automaticamente `openclaw_wsl_keepalive.ps1` (processo `wsl ... sleep infinity`) para manter a sessao viva.

## Correcao aplicada

```powershell
wsl -d OpenClawGateway -- openclaw config set gateway.bind loopback
wsl -d OpenClawGateway -- bash -lc "systemctl --user stop openclaw-gateway.service; sleep 2; systemctl --user start openclaw-gateway.service"
```

Aguardar ate HTTP 200 em `http://127.0.0.1:18789/`.

## Script automatico (recomendado)

```powershell
# So reinicia se estiver parado (preferido)
60_Sistemas\OpenClaw\scripts\ensure_openclaw_gateway.ps1

# Keepalive WSL (iniciado automaticamente pelo ensure; ou manual)
60_Sistemas\OpenClaw\scripts\openclaw_wsl_keepalive.ps1

# Abre chat no navegador (nao reinicia se ja OK)
60_Sistemas\OpenClaw\scripts\iniciar_openclaw_web.ps1
60_Sistemas\OpenClaw\scripts\iniciar_openclaw_web.ps1 -Session fabioos-ponte

# Reinicio forcado (evitar uso rotineiro)
60_Sistemas\OpenClaw\scripts\ensure_openclaw_gateway.ps1 -ForceRestart
```

Tempo tipico: **~20s** ate HTTP 200 + **45s** hold interno + keepalive em background.

## URLs uteis

| URL | Uso |
|---|---|
| `http://127.0.0.1:18789/` | Dashboard |
| `http://127.0.0.1:18789/chat?session=main` | Chat agente default |
| `http://127.0.0.1:18789/chat?session=fabioos-ponte` | Chat ponte FabioOS |

## Alternativa

Abrir pelo **OpenClaw Companion** (bandeja do Windows) — conecta ao gateway sem depender do navegador.

## Diagnostico rapido

```powershell
wsl -d OpenClawGateway -- openclaw gateway status
curl.exe -I http://127.0.0.1:18789/
```

Esperado: `Connectivity probe: ok` e HTTP 200.

## Relacoes

- [[60_Sistemas/OpenClaw/ponte/STATUS_PONTE]]
- [[60_Sistemas/OpenClaw/ponte/MAPA_Agentes_MEGATRON_OpenClaw]]
