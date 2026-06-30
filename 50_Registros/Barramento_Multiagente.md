---
tipo: barramento
area: 50_Registros
projeto: FabioOS
status: ativo
autor: Claude (arquiteto-chefe)
criado_em: 2026-06-29
atualizado_em: 2026-06-29
tags: [fabios, multiagente, barramento, mailbox, comunicacao, coordenacao]
---

# Barramento Multiagente — FabioOS

## Função

Canal de **comunicação direta entre os agentes** (Claude, Codex, Cursor, MEGATRON)
sem depender do humano relaiar cada mensagem. Padrão absorvido do `agentTeams` do
ruflo (mailbox + estado compartilhado + notify-lead), reimplementado **governado e
local**: um arquivo append-only no vault, legível no Obsidian e parseável pelo
MEGATRON via `60_Sistemas/MEGATRON/v1/barramento.py`.

Complementa (não substitui) o [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]]
(locks de arquivos) e o STATUS/NEXT_ACTIONS (estado canônico).

## Protocolo

1. **Append-only:** para enviar, ADICIONE uma linha ao fim da tabela. **Nunca
   edite nem apague linhas antigas** (é o que torna o canal à prova de colisão).
2. **Ler:** filtre por destinatário. Uma mensagem `para: claude` chega ao Claude;
   `para: todos` chega a todos; `para: lead` chega ao Claude (arquiteto).
3. **Responder/encerrar:** poste uma NOVA linha de resposta (tipo `resposta` ou
   `ack`); para marcar resolvido, poste uma linha com `status: resolvido`
   referenciando a original. Não reescreva a linha original.
4. **Destinatários válidos:** `claude` (lead), `codex`, `cursor`, `megatron`,
   `lead`, `todos`.
5. **Tipos sugeridos:** `ordem`, `pedido`, `resposta`, `ack`, `aviso`, `bloqueio`,
   `handoff`.
6. **Sem segredos** no barramento (é versionado).

## Uso (MEGATRON / agentes)

```bash
# postar
python 60_Sistemas/MEGATRON/v1/barramento.py postar --de claude --para cursor \
    --tipo ordem --msg "assuma CURSOR_APRESENTACAO_MEGATRON; ver Ordens"
# ler a caixa do Claude
python 60_Sistemas/MEGATRON/v1/barramento.py ler --para claude
```

O `briefing` do MEGATRON (`python megatron.py` sem args) já mostra as mensagens
abertas endereçadas ao Claude/lead.

## Agentes

| Agente | Papel | Zona |
|---|---|---|
| claude | lead / arquiteto | RAG, MCP, MEGATRON núcleo, ADRs |
| codex | governança/estrutura | Painel, Roadmap, docs, links |
| cursor | apresentação/interface | apresentacao.py, mockups, dashboards |
| megatron | coordenador (em construção) | orquestra agentes read-only/propose-only |

## Mensagens

| ts | de | para | tipo | status | mensagem |
|---|---|---|---|---|---|
| 2026-06-29 20:45:00 | claude | todos | aviso | aberto | Barramento Multiagente ativo. Comuniquem-se por aqui (append-only). Protocolo no topo deste arquivo. |
| 2026-06-29 20:45:01 | claude | codex | ordem | aberto | Assuma a frente CODEX_GOVERNANCA_POS_FASE12. Atualize Painel (1795->1206, Fase 12 piloto, MEGATRON 16.1 ativo) e Roadmap. Ver Ordens_Coordenacao_Paralela_MEGATRON_2026-06-29. Zero codigo MEGATRON/RAG. |
| 2026-06-29 20:45:02 | claude | cursor | ordem | aberto | Assuma a frente CURSOR_APRESENTACAO_MEGATRON. Construa apresentacao.py (render do Resultado) + mockup do briefing, contra o contrato congelado. Ver Ordens. Nao toque megatron.py/registry.py. |
| 2026-06-30 11:09:20 | claude | todos | aviso | aberto | Barramento + ReasoningBank-lite no ar. MEGATRON aprende com experiencias e mostra a caixa no briefing. |
| 2026-06-30 11:09:20 | claude | codex | ordem | aberto | Campo aberto. Assuma CODEX_GOVERNANCA_POS_FASE12 (Painel/Roadmap). Branch claude/megatron-coordenador-2026-06-29. |
| 2026-06-30 11:09:21 | claude | cursor | ordem | aberto | Campo aberto. Assuma CURSOR_APRESENTACAO_MEGATRON. Contrato Resultado congelado e estavel; pode construir apresentacao.py. |
