---
tipo: spec
area: 60_Sistemas
projeto: FabioOS
status: implementado
fase: comunicacao-mobile-v0
dominio: FabioOS
classe_dado: Privado
permissao: local-first; escrita apenas em 00_Inbox/mobile; sem API externa
criado_em: 2026-06-28
atualizado_em: 2026-06-28
tags: [fabios, spec, mobile, gateway, inbox]
---

# SPEC - Mobile Gateway FabioOS v0

## 1. Problema

Fabio precisa ver algo funcional no celular agora, sem depender do OpenClaw instavel, de WhatsApp/QR Code, de n8n externo ou de API paga.

## 2. Objetivo

Criar um gateway HTTP local, acessivel pelo navegador do celular na mesma rede, para capturar ideias, comandos, textos e lembretes diretamente no vault/Obsidian em `00_Inbox/mobile/`.

## 3. Fora de escopo

- WhatsApp real.
- QR Code obrigatorio.
- Envio para modelo externo.
- OpenRouter, Claude, GPT ou Gemini automaticos.
- Alteracao de OpenClaw auth/runtime.
- Ingestao em RAG/Grafo.
- Push para GitHub.

## 4. Dominio, dados e permissoes

| Campo | Valor |
|---|---|
| Dominio | FabioOS |
| Classe de dado | Privado |
| RAG | nao ingerir automaticamente |
| Grafo | nao ingerir automaticamente |
| Modelo externo/API | nao usar na v0 |
| Aprovacao humana | obrigatoria para enviar a modelo externo, WhatsApp, email ou n8n |

## 5. Arquitetura proposta

```text
Celular na mesma rede
  -> navegador web
  -> http://IP_DO_PC:8787
  -> mobile_gateway_fabioos.py
  -> 00_Inbox/mobile/*.md
  -> Obsidian / FabioOS
```

## 6. Plano de tarefas

- [x] Registrar frente ativa.
- [x] Criar script HTTP local sem dependencias externas.
- [x] Criar pagina mobile minima.
- [x] Salvar capturas em Markdown com frontmatter.
- [x] Expor `/health` e `/api/status`.
- [x] Atualizar dashboard operacional.
- [x] Criar documentacao e changelog.
- [x] Testar compilacao e endpoint local.

## 7. Criterios de aceite

- [x] O PC sobe um servidor local.
- [x] O celular consegue abrir a URL se estiver na mesma rede e o firewall permitir.
- [x] Uma captura real vira nota Markdown em `00_Inbox/mobile/`.
- [x] O gateway nao usa API externa.
- [x] O gateway nao exige token externo.
- [x] O gateway nao toca RAG DB, Grafo data, MCP_FABIOOS, OpenClaw auth/runtime ou n8n.

## 8. Testes minimos

- [x] `python -m py_compile 60_Sistemas/FabioOS/scripts/mobile_gateway_fabioos.py`.
- [x] `GET /health`.
- [x] `POST /api/capture` em modo `dry_run`.
- [x] `git diff --check`.
- [x] Scan de segredos antes do commit.

## 9. Riscos

| Risco | Mitigacao |
|---|---|
| Expor captura na rede local | usar apenas rede confiavel; token opcional por `--token`; desligar ao terminar |
| Firewall bloquear acesso do celular | testar localhost primeiro; se necessario permitir Python no Windows Firewall |
| Captura virar bagunca | salvar em Inbox com status `inbox` para o Arquivista processar depois |
| Escopo crescer para WhatsApp/n8n | manter v0 local; integrar bordas externas em fases futuras |

## 10. Rollback

Parar o processo Python do gateway e ignorar/remover capturas de teste de `00_Inbox/mobile/` apos revisao humana.

## 11. Changelog esperado

Registrar `50_Registros/Changelog/2026-06-28_mobile-gateway-fabioos-v0.md`.
