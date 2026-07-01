---
tipo: coordenacao
area: 60_Sistemas
projeto: FabioOS
status: ativo
de: Claude (arquiteto-chefe)
para: Cursor, Codex
criado_em: 2026-06-29
atualizado_em: 2026-06-29
tags: [fabios, multiagente, cursor, codex, coordenacao, barramento, zonas]
---

# Integração do Cursor + Modelo de Coordenação Multiagente

## Contexto
Fabio assinou o **Cursor** (pago). O FabioOS passa a ter **3 cérebros de execução**: Claude Code, Codex e Cursor — coordenados pela arquitetura unificada (Obsidian = memória; MEGATRON = futura interface coordenadora).

## 1. Cursor — especialidades (o que ele faz melhor)
Cursor é um **IDE com IA** (fork do VS Code) — sua força é **desenvolvimento de software interativo sobre um codebase**:
- **Composer/Agent**: edição multi-arquivo coordenada num projeto real.
- **Indexação do codebase**: contexto de projeto inteiro, navegação, refactor grande.
- **Rodar/depurar** no editor; terminal integrado; preview de app.
- Melhor para **construir apps** (PWA/Electron/Tauri), dashboards, parsers/crawlers, empacotar bibliotecas, testes.

Papel canônico no FabioOS (Plano Mestre 5.9 / Roadmap v2 fase 16.5): **oficina de desenvolvimento de software**. Entra quando o FabioOS deixa de ser só vault e exige **componentes de software de verdade**.

## 2. O que o Claude (arquiteto) pode delegar ao Cursor
- **A interface MEGATRON** (o capstone visual: PWA/desktop) — trabalho ideal para o Cursor.
- **Dashboard de observabilidade** (Fase 23) como app real.
- **Empacotar/robustecer o MCP FabioOS** e os scripts RAG/Grafo num pacote testável.
- **Parsers/crawlers/ingestão** (PDF, áudio→transcrição, conectores).
- Refactors grandes com testes.

## 3. Zona do Cursor (anti-colisão)
| Zona | Dono |
|---|---|
| Apps/software (interface MEGATRON, dashboards, empacotamento) — ex.: pasta `app/` ou `60_Sistemas/MEGATRON/interface/` | **Cursor** |
| RAG db/scripts, MCP-core, MEGATRON v0/v1, arquitetura, ADRs | **Claude** |
| Estrutura do vault, migração, links, governança documental, roadmap | **Codex** |
| Runtime (n8n/OpenClaw/WhatsApp/Google), push | **bloqueado — aprovação humana** |

## 4. Regras de entrada (Matriz de Aptidão das IAs)
Cursor entra **por competência, custo, risco e teste** — não por acumulação. Toda tarefa do Cursor deve ter escopo, teste mínimo, log e não colidir com outra frente.

## 5. ORDENS de integração (para o Cursor)
1. Ler `60_Sistemas/FabioOS/bootstrap/CLAUDE.md` (ou `CLAUDE.md` raiz), `00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON.md`, `Roadmap_Fases_FabioOS_v2_2026-06-29.md` e `Registro_Frentes_Ativas.md` antes de agir.
2. **Registrar lock** no `Registro_Frentes_Ativas.md` antes de tocar qualquer artefato compartilhado.
3. Trabalhar **só na zona de software**; **não tocar** RAG db/scripts, MCP-core, MEGATRON v0/v1, nem estrutura/governança sem **handoff** registrado.
4. **Sem push e sem runtime** sem aprovação humana. Scan de segredos antes de commit. Changelog em cada entrega.
5. Primeira tarefa proposta: **mockup/protótipo da interface MEGATRON** (a partir de `60_Sistemas/FabioOS/Visao_Interface_FabioOS.md`), em zona própria, sem tocar o core.

## 6. Informação para o Codex
- Cursor entrou como oficina de software (zona acima). **Não colidir**: Codex segue em estrutura/links/governança; Cursor em apps; Claude em RAG/MCP/MEGATRON-core.
- Atualizar o `Registro_Frentes_Ativas.md` com a frente do Cursor quando ele registrar lock.

## 7. Comunicação entre agentes (resposta ao ponto do Fabio)
> "Essa comunicação toda deveria ser feita por agentes (OpenClaw/Hermes)?" — **Sim, é o destino certo, mas por fases.**

- **Hoje (funciona):** **barramento por arquivos** — `Registro_Frentes_Ativas.md` (locks/zonas) + `STATUS.md`/`NEXT_ACTIONS.md` (estado) + handoffs. É assíncrono; o **humano só dispara** cada agente. O relay manual de texto é o gargalo.
- **Próximo (reduz o relay):** padronizar **um arquivo de barramento** (`50_Registros/Barramento_Multiagente.md`) que todo agente **lê ao iniciar e escreve ao terminar** — o humano passa a só dizer "vai", e cada agente se sincroniza sozinho pelo arquivo.
- **Futuro (automação real):** **MEGATRON como orquestrador** + **MCP FabioOS** expondo a coordenação como ferramenta + **OpenClaw/Hermes** como runtime que dispara os agentes. Isso é fase pós-governança/runtime (Roadmap v2) — exige Docker/auth/aprovação e **não** deve ser ativado antes da Fase 17.

**Decisão de arquiteto:** não automatizar a comunicação agora (runtime-gated + risco). Adotar **o barramento por arquivo** como passo intermediário barato e seguro. Registrar como evolução no Roadmap v2.

## Relações
- [[60_Sistemas/FabioOS/Ordens_Arquiteto_Para_Codex_2026-06-29]]
- [[50_Registros/Decisoes/ADR_2026-06-29_Auditoria_Arquitetura_Claude]]
- [[60_Sistemas/FabioOS/Roadmap_Fases_FabioOS_v2_2026-06-29]]
- [[60_Sistemas/FabioOS/Visao_Interface_FabioOS]]
- [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]]
