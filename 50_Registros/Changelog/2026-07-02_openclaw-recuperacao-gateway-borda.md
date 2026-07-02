---
tipo: changelog
area: 50_Registros
projeto: FabioOS
sistema: OpenClaw
status: concluido
tags: [changelog, openclaw, gateway, borda]
criado_em: 2026-07-02
---

# 2026-07-02 - Recuperacao OpenClaw como gateway de borda

## Mudancas

- Diagnosticado o estado real do OpenClaw local.
- Registrada ADR reposicionando OpenClaw como gateway de borda, nao core.
- Criada SPEC de recuperacao com criterio de aceite.
- Criado plano operacional para teste local antes de QR/mobile.
- Atualizados documentos centrais do OpenClaw e painel MEGATRON.

## Decisao

OpenClaw nao sera usado como nucleo do FabioOS ate provar valor por teste minimo:

```text
OpenClaw -> Universal Intake -> MEGATRON -> Agentarium/Workboard -> aprovacao humana -> log
```

## Sem alteracao de runtime

- Nao foram alterados tokens.
- Nao foi aberto firewall.
- Nao foi criado QR Code.
- Nao houve envio externo.
- Nao houve RAG reindex.
- Nao houve compra ou recomendacao de compra imediata.
