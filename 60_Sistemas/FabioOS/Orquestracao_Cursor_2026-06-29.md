---
tipo: ordem-coordenacao
area: 60_Sistemas
projeto: FabioOS
status: ativo
autor: Claude (arquiteto-chefe)
criado_em: 2026-06-29
atualizado_em: 2026-06-29
tags: [fabios, multiagente, cursor, agentarium, orquestracao, interface]
---

# Orquestração do Cursor — Agentarium como Interface oficial

> O Cursor **não lê o barramento** (é agente de IDE, dirigido pelo Fabio). Então
> esta é a relay: **Fabio cola as ordens abaixo no Cursor**. Eu (Maestro) já
> entreguei o meu lado da costura — o `maestro_state.json`.

## Reconhecimento

O Cursor **over-entregou na sua zona**: em vez do `apresentacao.py` mínimo que eu
havia nomeado, construiu o **Agentarium** — dashboard visual multiagente completo
(catálogo, matriz de segurança, EventLog, painel WhatsApp, ZoneMap, pixel art,
WebSocket). Isso É a camada Interface do FabioOS. **Ratificado como a frente
oficial de Apresentação/Interface do Cursor.** O `apresentacao.py` fica cancelado
(o Agentarium o subsume).

## Problema que esta orquestração resolve

Hoje há **dois rosters de agentes divergentes**: o do Agentarium (backend/
simulador) e o do MEGATRON Maestro (`registry.py`, 8 agentes reais). Dois cérebros
brigando pela verdade. **Decisão de lead: o Maestro é a fonte única de verdade do
roster; o Agentarium consome.**

## Ordens ao Cursor (colar no Cursor)

1. **Consumir o estado do Maestro como fonte de verdade do roster.** Ler
   `60_Sistemas/MEGATRON/v1/state/maestro_state.json` (gerado pelo Maestro) e
   mapear `agents[]` → o tipo `Agent` do Agentarium:
   - `id`, `name`, `layer`, `status` (active/planned), `role` (= ferramenta),
     `capabilities` (= capacidades). Use `rawStatus` (ativo/planejado/**gated**)
     para o badge de risco (gated = badge laranja "GATED").
   - Marcar `lastEventSource: "real"` quando o agente vier do Maestro.
2. **EventLog real:** usar `barramento[]` do JSON como fonte de eventos (canal
   `AGENT`), além da simulação. Cada item: `ts, de, para, tipo, mensagem`.
3. **ZoneMap:** os 8 agentes ativos do Maestro aparecem com status real; os 8
   planejados/gated aparecem esmaecidos com o badge.
4. **NÃO tocar** o núcleo cognitivo (zona Claude): `megatron.py`, `registry.py`,
   `barramento.py`, `reasoningbank.py`, `maestro_state.py`. O Cursor **consome** o
   JSON; não edita o backend do Maestro.
5. **Backend do Agentarium:** pode ler o `maestro_state.json` no boot e quando ele
   mudar (watcher de arquivo) e emitir `catalog`/`snapshot` via WebSocket. Assim a
   simulação vira espelho do sistema real.

## Meu lado da costura (já entregue)

- `60_Sistemas/MEGATRON/v1/maestro_state.py` — exporta roster + barramento em JSON.
- `60_Sistemas/MEGATRON/v1/state/maestro_state.json` — amostra real (8 ativos / 16
  total). Regenero a cada mudança de roster (`python maestro_state.py`).

## Como o Cursor reporta de volta

Como o Cursor não usa o barramento, ele reporta **pelo Fabio** (no Cursor) ou,
quando o Agentarium estiver lendo o `maestro_state.json`, o próprio dashboard vira
o canal visual de status. Futuro: um pequeno endpoint que o Cursor chama para
postar no barramento.

## Relações
- [[60_Sistemas/FabioOS/Ordens_Coordenacao_Paralela_MEGATRON_2026-06-29]]
- [[60_Sistemas/MEGATRON/v1/maestro_state]]
- [[50_Registros/Barramento_Multiagente]]
