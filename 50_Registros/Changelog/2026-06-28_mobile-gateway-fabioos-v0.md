---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: registrado
tags: [fabios, changelog, mobile, gateway, inbox]
criado_em: 2026-06-28
---

# Changelog - Mobile Gateway FabioOS v0

## Resumo

Implementada a primeira borda mobile funcional do FabioOS: uma pagina web local, acessivel pelo celular na mesma rede, capaz de salvar capturas em Markdown dentro de `00_Inbox/mobile/`.

## Arquivos principais

- `60_Sistemas/FabioOS/scripts/mobile_gateway_fabioos.py`
- `60_Sistemas/FabioOS/Mobile_Gateway_FabioOS_v0.md`
- `60_Sistemas/FabioOS/specs/2026-06-28_mobile-gateway-fabioos-v0.md`
- `10_Mapas/Dashboard_Operacional_FabioOS.md`

## Decisoes

- Nao usar OpenClaw como dependencia da v0, pois o runtime/auth ainda esta instavel.
- Nao usar OpenRouter, Claude, GPT, Gemini ou outra API externa na v0.
- Nao ingerir capturas automaticamente em RAG/Grafo.
- Salvar tudo primeiro em Inbox, para triagem humana/agente Arquivista.

## Testes

- `py_compile` do script.
- `GET /health`.
- `POST /api/capture` com `dry_run`.
- `git diff --check`.
- scan de segredos antes do commit.

## Proximo passo

Testar acesso pelo celular em `http://IP_DO_PC:8787`. Se o Windows Firewall bloquear, permitir Python somente em rede privada/confiavel.
