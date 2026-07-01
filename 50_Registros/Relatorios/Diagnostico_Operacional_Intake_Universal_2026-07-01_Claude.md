---
tipo: relatorio
area: 50_Registros
projeto: FabioOS
status: ativo
autor: Claude (arquiteto-chefe / auditor operacional)
criado_em: 2026-07-01
tags: [fabios, intake-universal, auditoria, prova-operacional, megatron-core]
---

# Diagnóstico operacional do Intake Universal FabioOS

> Auditoria em modo seguro (sem envio, sem apagar, sem token, sem RAG, sem ação externa).
> Contra o carimbo "COMPLETE ✅ tudo funcional" do OpenClaw: a espinha funciona **com
> evidência**, mas o fluxo NÃO fecha ponta a ponta — faltam a aprovação interativa e a
> escrita no Obsidian. Evidência abaixo, não afirmação.

## Tabela

| Módulo | Existe? | Funciona? | Evidência | Problema | Próxima ação | Prioridade |
|---|---|---|---|---|---|---|
| Intake Core (`megatron_core.py`) | Sim | **Sim** | teste email+comando → `escolaos/high/criar_tarefa/aprovação` | — | repetir prova p/ whatsapp+pdf | — |
| Intake Flow (`intake_flow.py`) | Sim | **Sim** | 5 payloads → fila + log; token redigido, não vaza | não escreve nota no Obsidian | ligar passo "aprovado → nota" | **alta** |
| Fila (`intake_queue.json` + sample) | Sim | **Sim** | arquivo gerado; `examples/intake_queue.sample.json` congelado | fila viva sem UI de aprovação | Cursor renderiza a fila | **alta** |
| Email (`email_intake_dry_run.py` + `universal_intake_adapter.py`) | Sim | **Parcial** | teste 1 roda dry-run: `escolaos`, requer humano | urgência diverge (deu "média", core dá "alta"); sem conector Gmail real | delegar classificação ao core | **alta** |
| Comando manual (linguagem natural) | Parcial | **Parcial** | core classifica `escolaos/high`, mas NÃO extrai série/tema/prazo/produto | pendência estruturada inexistente | campo de comando (Cursor) + extrator | média |
| Obsidian (memória / saída) | **Não** (no intake) | **Não** | `grep`: nenhum módulo de intake escreve `.md` | passo final "saída para Obsidian" ausente | arquivista grava nota aprovada | **alta** |
| WhatsApp/Pietra (`pietra_conversa.py`) | Sim | Parcial | motor de conversa (dry-run) + workflow n8n `FabioOS_WhatsApp_Pietra.json` inativo | não plugado ao intake universal; canal real desligado (correto) | bridge dry-run → core | média |
| PDF (`watch_pdf_drop.py`) | Sim | Parcial | watcher + pasta `00_Inbox/pdfs/` (vazia); extração PyMuPDF ok | não plugado à classificação do intake | payload pdf fake → core | média |
| n8n | Sim (6 workflows) | Parcial/inativo | 6 `.json`; `FabioOS_Intake_Orquestrador_Seguro` importado-inativo | tubulação não ativada (correto, gated) | manter inativo até prova | baixa |
| GitHub / versão | Sim | **Sim** | commits `d977f16a`, `36f11939`; `.gitignore` protege dado vivo | — | manter | — |
| Agentarium (mesa de despacho) | Sim | Parcial | backend+frontend em `apps/agentarium`; consome `maestro_state.json` | ainda não renderiza `intake_queue` como fila de aprovação | fila "Aguardando Fabio" | **alta** |
| Logs | Sim | **Sim** | `intake_log.jsonl` (§8: quem/quando/o quê/onde/próximo; sem segredo) | log local, não unificado | manter | baixa |
| Agentes / roteamento | Sim | **Sim** | core roteia p/ `agente_escolar`/`atendente_pietra`/`bloqueio` | destinos são sugestão, não executam (por design) | ok (propõe, não executa) | — |

## 1. O que funciona agora (com evidência)

- **Classificação cognitiva** (`megatron_core.py`): entrada → domínio → sensibilidade →
  urgência → agente → ação → `requires_human_approval`. Teste 1 e 2 corretos.
- **Prova de fluxo** (`intake_flow.py`): entrada fake → payload universal → classificação →
  **redação da trava** (token nunca vaza) → fila "Aguardando Fabio" → log §8.
- **Fila consumível**: `intake_queue.json` + sample congelado.
- **Versionamento seguro**: dado vivo gitignored; segredo redigido.

## 2. O que está parcialmente funcional

- **Email**: dry-run roda, mas urgência diverge do core (dois classificadores).
- **Comando manual**: classifica, mas não extrai série/tema/prazo/produto.
- **WhatsApp/PDF**: módulos existem, ainda não plugados ao contrato universal.
- **Agentarium**: existe, ainda não é a "mesa de despacho" (fila de aprovação).

## 3. O que está travado

- **Aprovação humana interativa**: hoje é só um `status: waiting_approval` no JSON;
  não há botão que o Fabio clique para aprovar/rejeitar.
- **Saída para Obsidian**: NADA escreve a nota/tarefa aprovada. O critério de sucesso
  quebra exatamente neste último elo.

## 4. O que é apenas documentação

- MEGATRON Core Spec v0.1 (a spec — o código já a implementa).
- Orquestrador n8n `FabioOS_Intake_Orquestrador_Seguro` (importado, inativo).
- Roadmap v2 (histórico).

## 5. O teste mínimo que prova operação

```text
Email fake (coordenacao@escola.com, "Prova do 8º ano", "Geografia África até amanhã")
  → megatron_core → escolaos / urgência ALTA / criar_tarefa / aguardando Fabio  ✓
Comando manual ("prova do 8º ano sobre África para amanhã")
  → escolaos / ALTA / criar_tarefa / aguardando aprovação  ✓ (sem extração estruturada)
intake_flow → fila + log + redação de token  ✓
```
**Prova: a espinha entrada→classificação→pendência→log está VIVA.**
**Falta fechar: aprovação interativa + escrita no Obsidian.**

## 6. Próximo comando ao Codex

> Convergir os dois classificadores: `email_intake_dry_run.py` e `universal_intake_adapter.py`
> devem **delegar** a `megatron_core.classificar_intake()` em vez de manter taxonomia/urgência
> próprias (fim da divergência "média vs alta"). Criar payloads fake de WhatsApp e PDF no
> MESMO schema e rodá-los pelo core. Zero ação externa.

## 7. Próximo comando ao Cursor

> Transformar o Agentarium em **mesa de despacho**: renderizar `intake_queue.sample.json`
> como fila "Aguardando Fabio" com botão Aprovar/Rejeitar; e um **campo de comando natural**
> que extraia produto/série/tema/prazo (ex.: "prova do 8º sobre África amanhã" → pendência
> EscolaOS estruturada). O clique em Aprovar dispara a escrita (via Claude/arquivista).

## 8. Próximo comando ao Claude

> Implementar o **elo final**: "aprovado → escrita no Obsidian". Um `arquivista` que recebe
> um item aprovado da fila e grava a nota/tarefa `.md` (ex.: `00_Inbox/Triagem/` ou EscolaOS),
> com log de continuidade — fechando o critério de sucesso. Depois, repetir a prova §9 para
> WhatsApp e PDF fake.

## Veredito

Sistema **parcialmente destravado**: a espinha cognitiva funciona ponta a ponta até a
fila+log (provado). O critério de sucesso do Fabio (`...→ aprovação humana → log → saída
para Obsidian`) quebra nos **dois últimos elos**, que ainda não existem. Não é "COMPLETE":
é "espinha provada, pontas faltando". Três comandos acima fecham o ciclo.
