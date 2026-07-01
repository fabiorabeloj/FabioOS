---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: registrado
classe_dado: interno
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [fabios, obsidian, grafo, moc, dashboard]
---

# 2026-06-30 - Obsidian Revitalizacao

## Contexto

Claude abriu a frente `OBSIDIAN_REVITALIZACAO` para corrigir a sensacao de vault abandonado.

## Entrega

- `.obsidian/graph.json` atualizado para pastas canonicas.
- Dashboard criado: [[10_Dashboard/Obsidian_Revitalizacao_FabioOS]].
- MOC criado: [[40_Wiki/_MOCs/MOC_Obsidian_FabioOS]].
- Dashboards conectados:
  - [[10_Dashboard/FabioOS]];
  - [[10_Dashboard/Estrutura_Obsidian_FabioOS]];
  - [[10_Dashboard/Mapa_de_Conexoes_FabioOS]];
  - [[10_Dashboard/README]].
- MOCs conectados:
  - [[40_Wiki/README]];
  - [[40_Wiki/_MOCs/README]].

## Grupos Canonicos do Grafo

O grafo agora privilegia:

- `00_Inbox` e `00_Inbox/pdfs`;
- `05_Raw_Sources`;
- `10_Dashboard`;
- `30_Projetos/PRIMUS`;
- `40_Wiki` e `40_Wiki/_MOCs`;
- `50_Registros/Decisoes`, `Changelog` e `Relatorios`;
- `60_Sistemas/FabioOS`, `MEGATRON`, `RAG`, `MCP`, `n8n` e `OpenClaw`;
- `80_Specs/PRIMUS`.

## Limites

- Sem tocar codigo MEGATRON.
- Sem tocar codigo RAG.
- Sem reindex.
- Sem mover arquivos em massa.
