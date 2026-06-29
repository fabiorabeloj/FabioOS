---
tipo: sistema
area: 60_Sistemas
projeto: FabioOS
sistema: MCP_FabioOS
status: rascunho-implementacao
fase: 15
tags: [mcp, fastmcp, rag, grafo, megatron, fase-15, ferramentas]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# MCP FabioOS — Fase 15

## Função

MCP customizado (FastMCP) que expõe as camadas cognitivas do FabioOS — **RAG, Grafo e vault** — como **ferramentas padronizadas**. É o que permite ao [[60_Sistemas/FabioOS/Visao_Interface_FabioOS|MEGATRON]] (e a qualquer agente autorizado) consultar o conhecimento por uma interface única — o tijolo que conecta B1/B3 ao capstone.

## Contexto

Modelo Formal: o MEGATRON precisa de RAG + Grafo + **MCPs**. RAG e Grafo já existem (mínimos) mas isolados; este MCP os torna acionáveis como ferramentas. **v0 é read-only** (consulta) — sem escrever, reindexar ou apagar (respeita os locks do [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]]).

## Ferramentas (v0 — read-only)

| Ferramenta | O que faz |
|---|---|
| `consultar_rag(pergunta, k)` | Busca semântica no vault (chroma + bge-m3 local); retorna trechos + fonte |
| `consultar_grafo(termo, top)` | Busca nós relacionados ou lista hubs (via `query_graph.py`) |
| `buscar_nota(termo, limite)` | Procura `.md` por nome/conteúdo no vault |
| `consultar_wiki(termo, limite)` | Idem, escopado a `wiki/` |
| `listar_projetos()` | Lista projetos em `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/` |

Exclui dos resultados: `.venv`, `fabioos_db`, `.git`, `.obsidian`, `.claude`, `sources/_inbox`.

## Como usar

### 1. Instalar dependência (você executa)
Reaproveita o venv do RAG (já tem chromadb + sentence-transformers); falta só o servidor:
```powershell
uv pip install --python "60_Sistemas\RAG\.venv\Scripts\python.exe" -r 60_Sistemas\MCP_FabioOS\requirements.txt
```

### 2. Rodar/testar localmente
```powershell
60_Sistemas\RAG\.venv\Scripts\python.exe 60_Sistemas\MCP_FabioOS\server.py
```

### 3. Registrar no Claude Desktop / Codex (stdio)
Adicionar ao config MCP do cliente (não commitar tokens):
```json
{
  "mcpServers": {
    "fabioos": {
      "command": "C:\\Users\\user\\Desktop\\FabioOs\\FabioOs\\60_Sistemas\\RAG\\.venv\\Scripts\\python.exe",
      "args": ["C:\\Users\\user\\Desktop\\FabioOs\\FabioOs\\60_Sistemas\\MCP_FabioOS\\server.py"]
    }
  }
}
```

## Segurança

- **Read-only**: nenhuma ferramenta escreve, reindexa ou apaga.
- Consulta o `fabioos_db` apenas com `get_collection`/`query`.
- Não expõe `.codex/config.toml`, logs runtime nem dados sensíveis.

## Relações

- [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]]
- [[60_Sistemas/Grafo/README_Grafo]]
- [[60_Sistemas/FabioOS/Visao_Interface_FabioOS]]
- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]
- [[60_Sistemas/FabioOS/Protocolo_Roteamento_Capacidades_IA]]

## Próximas ações

- [ ] Instalar `fastmcp` no venv do RAG e testar o servidor
- [ ] Registrar o MCP no Claude Desktop e validar as 5 ferramentas
- [ ] v1: ferramentas de escrita segura (`registrar_decisao`, `gerar_changelog`) com aprovação humana
- [ ] Conectar ao MEGATRON v0 (capstone)
