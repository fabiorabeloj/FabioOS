---
tipo: adr
area: 50_Registros
projeto: FabioOS
status: aceito
autor: Claude (arquiteto-chefe)
criado_em: 2026-06-29
atualizado_em: 2026-06-29
tags: [adr, ruflo, claude-flow, multiagente, avaliacao, radar-tecnologico, megatron]
---

# ADR 2026-06-29 — Avaliação do ruflo e decisão de absorção (não instalação)

## Contexto

O Fabio pediu para instalar `github.com/ruvnet/ruflo` (ex-claude-flow, v3.16.2) e
resolver a comunicação entre os agentes (Claude/Codex/Cursor). Ruflo é um
**meta-harness de orquestração**: 60+ agentes, swarms, memória vetorial
auto-aprendente, roteamento, consenso (hive-mind) e federação entre máquinas, com
integração nativa Claude Code/Codex. Como a ação modifica o ambiente e executa
código de terceiros, foi feita uma **avaliação isolada** (sandbox com `HOME`
redirecionado) antes de qualquer mudança no ambiente real.

## Avaliação (evidência do sandbox)

Um `ruflo init` padrão cria **12 diretórios / 106 arquivos** e:

- despeja no `.claude/` do projeto: **18 agentes, 148 arquivos de comando, 30
  skills, 42 helpers**;
- escreve `.claude/settings.json` com **9 hooks auto-executáveis** (PreToolUse,
  PostToolUse, UserPromptSubmit "route", SessionStart, Stop, PreCompact,
  SubagentStart/Stop, Notification) que interceptam cada prompt/edit/bash;
- liga `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` e um **daemon** com workers
  agendados (audit 4h, optimize 2h), auto-train e auto-scan-on-edit;
- registra MCP server `claude-flow` (topologia hierarchical-mesh, até 15 agentes);
- toca o **`~/.claude/CLAUDE.md` global** (afeta todos os projetos);
- baixa modelo ONNX e cria runtime `.claude-flow/`.

**Colisão com o FabioOS real:** o `.claude/` já contém superpowers + gsd +
FabioOS (agents/commands/hooks/skills); o overlay causaria clash e ruído enorme.
O `~/.claude/settings.json` já tem o `GITHUB_TOKEN`. E ruflo **se vende como o
coordenador** — sobreposição direta com o MEGATRON, que está sendo construído
exatamente para esse papel.

## Decisão

1. **Não instalar o ruflo** no ambiente FabioOS. O overlay invasivo, os 9 hooks
   autônomos, o daemon e a filosofia de swarm autônomo conflitam com o design
   governado, local-first, read-only/propose-only e humano-no-loop do FabioOS.
2. **Ruflo e MEGATRON são categorias diferentes:** ruflo é *substrato* genérico;
   MEGATRON é a *persona de domínio* do FabioOS. **MEGATRON não é substituído.**
3. **Absorver os padrões úteis** do ruflo, reimplementados de forma governada:
   - **Mailbox + estado compartilhado + notify-lead** (do `agentTeams`) →
     **Barramento Multiagente** leve, em arquivo append-only, lido pelos 3
     agentes e integrado ao MEGATRON. Resolve a comunicação pedida.
   - **ReasoningBank** (memória de experiências: registra resultado de tarefa →
     aprende estratégia que funciona) → **SPEC ReasoningBank-lite** para o
     MEGATRON, sobre os ADRs/changelogs/claude-mem já existentes.
   - **Hooks de coordenação** (SessionStart restaura, Stop persiste) → estender o
     padrão de hooks já existente no FabioOS para estado multiagente.
   - **Roteamento informado por sucesso** → evolução futura do `classificar()`.
4. **Descartar:** overlay de 240 arquivos, 9 hooks autônomos, daemon, hive-mind,
   poluição do `~/.claude` global, plugins IPFS.

## Consequências

- A comunicação entre agentes é resolvida sem instalar software invasivo nem
  arriscar o ambiente.
- O FabioOS fica mais inteligente por ter estudado o ruflo (Radar Tecnológico
  aplicado a um caso real, conforme NEXT_ACTIONS).
- Reavaliação futura do ruflo como **substrato sob o MEGATRON** fica em aberto,
  mas exige SPEC própria, taming dos hooks/daemon e aprovação humana — fora do
  escopo agora.
- Sandbox de avaliação em `scratchpad/ruflo-eval` é descartável (não tocou o real).

## Relações
- [[60_Sistemas/FabioOS/specs/2026-06-29_megatron-coordenador]]
- [[50_Registros/Barramento_Multiagente]]
- [[60_Sistemas/FabioOS/specs/2026-06-29_reasoningbank-lite-megatron]]
- [[50_Registros/Decisoes/ADR_2026-06-29_Auditoria_Arquitetura_Claude]]
- [[60_Sistemas/FabioOS/Ordens_Coordenacao_Paralela_MEGATRON_2026-06-29]]
