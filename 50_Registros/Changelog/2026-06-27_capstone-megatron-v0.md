---
tipo: changelog
area: registros
projeto: FabioOS
status: concluido
fase: 14-15-capstone
tags: [changelog, mcp, megatron, capstone, fase-14, fase-15, rag, grafo]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Changelog — Fases 14/15 (MCP) + MEGATRON v0 (capstone)

## Resumo

Fechamento do **caminho crítico ao MEGATRON** no nível mínimo. Com RAG (Fase 12) e Grafo (Fase 13) já existentes, foram construídos o **MCP FabioOS** (expõe as camadas cognitivas como ferramentas) e o **MEGATRON v0** (interface única que roteia, consulta e responde com fontes). Pela primeira vez o organismo cognitivo está ligado de ponta a ponta.

```
B1 RAG → B2 Agentes → B3 Grafo → B4 MCP FabioOS → B5 MEGATRON v0   (todos ✅ v0)
```

## Entregas

### Fase 15 — MCP FabioOS (`60_Sistemas/MCP_FabioOS/`)
- `server.py` (FastMCP) com 5 ferramentas **read-only**: `consultar_rag`, `consultar_grafo`, `buscar_nota`, `consultar_wiki`, `listar_projetos`.
- Reaproveita RAG (chroma + bge-m3 in-process) e Grafo (`query_graph.py`); não escreve/reindexa/apaga.
- Testado end-to-end (5/5 ferramentas). `fastmcp 3.4.2` instalado no venv do RAG.

### Capstone — MEGATRON v0 (`60_Sistemas/MEGATRON/v0/`)
- `megatron.py`: roteia a mensagem (acao/status/relacao/consulta), consulta via MCP e responde **com fontes**.
- **Read-only e propose-only**: ações (commit/criar/enviar) não são executadas — exigem aprovação humana.
- Sem LLM/API (recuperação, custo zero). Testado nas 4 rotas.

## Decisões registradas
- Dados gerados do Grafo tratados como **regeneráveis** (gitignore), não snapshot.
- MEGATRON v0 **não** chama LLM — só recuperação com fontes; síntese fica para v1.
- MCP e MEGATRON **reaproveitam** RAG/Grafo (zero duplicação), via cliente FastMCP in-memory.

## Gaps conhecidos → backlog v1
1. **Ignorância Explícita por limiar de relevância**: o Chroma sempre retorna top-k; falta usar a distância para declarar "não sei".
2. Síntese opcional com `--generate` + aprovação humana.
3. Ação → conectar aos agentes (SafeCommit/Arquivista) com aprovação.

## Estado
- Tudo no **PR #1** (`claude/megatron-rag-fase12`); `origin/main` intocado.
- Sem colisão: RAG/Grafo apenas lidos (read-only); locks respeitados.

## Relações
- [[60_Sistemas/MCP_FabioOS/README_MCP_FabioOS]]
- [[60_Sistemas/MEGATRON/v0/README_MEGATRON_v0]]
- [[60_Sistemas/FabioOS/Visao_Interface_FabioOS]]
- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]
- [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Painel_Pendencias_FabioOS]]
