---
tipo: capacidade
area: 60_Sistemas
projeto: FabioOS
status: implementado
fase: comunicacao-mobile-v0
classe_dado: Privado
tags: [fabios, mobile, gateway, inbox, obsidian]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
---

# Mobile Gateway FabioOS v0

## Missao

Dar ao Fabio uma forma imediata de se comunicar com o FabioOS pelo celular, sem depender de OpenClaw, WhatsApp, n8n, QR Code ou APIs externas.

## Como funciona

```text
Celular
  -> navegador
  -> http://IP_DO_PC:8787
  -> script local em Python
  -> nota Markdown em 00_Inbox/mobile/
  -> Obsidian/FabioOS
```

## Comando

No PC:

```powershell
python 60_Sistemas/FabioOS/scripts/mobile_gateway_fabioos.py --bind 0.0.0.0 --port 8787
```

Depois, no celular, abrir:

```text
http://IP_DO_PC:8787
```

O IP do PC pode ser visto com:

```powershell
Get-NetIPAddress -AddressFamily IPv4
```

## Endpoints

| Endpoint | Funcao |
|---|---|
| `/` | Pagina mobile para capturar texto |
| `/health` | Status tecnico simples |
| `/api/status` | Contagem de capturas e ultimas notas |
| `/api/capture` | Salva texto em `00_Inbox/mobile/` |

## Seguranca

- A v0 nao usa API externa e nao envia nada para modelos.
- A v0 salva somente dentro de `00_Inbox/mobile/`.
- Use apenas em rede confiavel.
- Para exigir senha simples de sessao, iniciar com `--token <codigo-local>` e abrir a pagina com `?token=<codigo-local>`.
- O token da v0 e local e temporario; nao deve ser commitado.

## Papel no FabioOS

Este gateway e a borda mobile minima do sistema. Ele nao substitui OpenClaw, WhatsApp ou n8n; ele cria a primeira trilha funcional para entrada rapida:

- ideias no celular;
- lembretes;
- comandos para triagem posterior;
- texto bruto para o agente Arquivista;
- material que depois pode ser classificado, resumido, ingerido no RAG e conectado ao Grafo.

## Proximas evolucoes

- QR Code local.
- Modo autenticado por token gerado automaticamente.
- Integracao com OpenClaw Companion quando a auth estiver estavel.
- Webhook n8n para roteamento externo.
- Bot WhatsApp via Evolution API ou provedor equivalente.
- Bot Telegram como alternativa mais simples e barata.
- Envio opcional para OpenRouter com teto de custo e classificacao previa de privacidade.
