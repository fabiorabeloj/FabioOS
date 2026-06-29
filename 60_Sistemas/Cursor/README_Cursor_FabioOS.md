---
tipo: documentacao
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [cursor, ide, agente, desenvolvimento, megatron, multiagente]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Cursor no FabioOS

## Funcao

Registrar o papel operacional do **Cursor** dentro do FabioOS: oficina de desenvolvimento assistido para codigo, scripts, validacao tecnica e interfaces — sem substituir Claude (lider estrutural) nem Codex (executor auxiliar/documentacao LLM Wiki).

Fonte canonica de aptidao: [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/IA/Modelos_e_IAs/Matriz_de_Aptidao_das_IAs_FabioOS#Cursor]].

## Contexto

O FabioOS opera com multiplos agentes no mesmo vault. Cursor entra quando a tarefa exige:

- editar e testar codigo Python/TypeScript com revisao visual;
- executar scripts locais (RAG, batch, dashboard);
- refatorar com diff revisavel;
- prototipar interface MEGATRON ou MCP robusto.

Cursor **nao** deve:

- editar arquivos em frente ativa de outro agente sem lock;
- fazer push, reindexar RAG ou tocar runtime externo sem aprovacao;
- assumir lideranca estrutural ou reescrever governanca compartilhada.

## Regras anti-colisao

Antes de cada sessao:

1. Ler [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]] (ou declarar frente isolada em arquivo novo).
2. Evitar zona compartilhada: `STATUS.md`, `NEXT_ACTIONS.md`, `mapa-fabios.md`, `60_Sistemas/FabioOS/bootstrap/CLAUDE.md`.
3. Preferir arquivos novos + scripts + relatorios proprios.
4. Persistir entrega: relatorio + changelog + sessao em `50_Registros/Sessoes/`.

## Historico de entregas

### 2026-06-29 — Validacao RAG Fase 12

| Entrega | Link |
|---|---|
| Frente e lock | [[60_Sistemas/FabioOS/Frente_Cursor_2026-06-29]] |
| Inventario completo | [[50_Registros/Sessoes/2026-06-29_cursor-sessao-validacao-rag]] |
| Relatorio tecnico | [[60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-29_Cursor]] |
| Changelog | [[50_Registros/Changelog/2026-06-29_validacao-rag-pos-ranking-cursor]] |
| Script batch | `60_Sistemas/RAG/scripts/batch_validate_rag.py` |
| Otimizacao | cache `get_model()` em `query_rag.py` |

Resultado: **10/10** perguntas de aceitacao em modo recuperacao; **0** falhas de seguranca.

## Como usar

Abrir o repositorio FabioOS no Cursor. Para tarefas RAG, usar sempre o venv:

```powershell
60_Sistemas\RAG\.venv\Scripts\python.exe 60_Sistemas\RAG\scripts\batch_validate_rag.py
```

Ver [[60_Sistemas/RAG/README_Scripts_RAG]] para detalhes.

## Relacoes

- [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/IA/Modelos_e_IAs/Matriz_de_Aptidao_das_IAs_FabioOS]]
- [[60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente]]
- [[60_Sistemas/FabioOS/Plano_Capacidades_Agentes_Cursor_Hermes_2026-06-28]]
- [[40_Wiki/_compat_wiki/conceitos/rag]]

## Proximas acoes

- [ ] Executar frente de interface MEGATRON quando existir SPEC aprovada
- [ ] Participar de testes de aptidao da matriz (implementacao vs documentacao)
- [ ] Confirmar CLI Cursor no PATH ou manter como IDE humana visual
