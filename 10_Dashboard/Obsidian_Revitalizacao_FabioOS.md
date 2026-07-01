---
tipo: dashboard
area: 10_Dashboard
projeto: FabioOS
status: ativo
classe_dado: interno
fonte: [[50_Registros/Barramento_Multiagente]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [fabios, obsidian, grafo, dashboard, revitalizacao]
---

# Obsidian Revitalizacao FabioOS

## Funcao

Painel para manter o vault visualmente vivo: grafo, MOCs, dashboards e higiene de pastas.

## Estado Atual

| Item | Status | Evidencia |
|---|---|---|
| Graph View | atualizado | `.obsidian/graph.json` usa pastas canonicas |
| MOC Obsidian | ativo | [[40_Wiki/_MOCs/MOC_Obsidian_FabioOS]] |
| Estrutura | ativa | [[10_Dashboard/Estrutura_Obsidian_FabioOS]] |
| Conexoes | ativo | [[10_Dashboard/Mapa_de_Conexoes_FabioOS]] |
| PDF Drop | ativo | [[00_Inbox/pdfs/README]] |
| PRIMUS anchors | ativo | [[30_Projetos/PRIMUS/Ancoras_PRIMUS_Index_DND_Core]] |

## Grupos Visuais do Grafo

| Tipo | Caminhos |
|---|---|
| Entrada | `00_Inbox/`, `00_Inbox/pdfs/` |
| Fontes | `05_Raw_Sources/`, `05_Raw_Sources/PRIMUS/` |
| Dashboards | `10_Dashboard/` |
| Projetos | `30_Projetos/`, `30_Projetos/PRIMUS/` |
| Wiki | `40_Wiki/`, `40_Wiki/_MOCs/`, `40_Wiki/PRIMUS/` |
| Registros | `50_Registros/`, `Decisoes/`, `Changelog/`, `Relatorios/` |
| Sistemas | `60_Sistemas/`, `FabioOS/`, `MEGATRON/`, `RAG/`, `MCP/`, `n8n/`, `OpenClaw/` |
| Specs | `80_Specs/`, `80_Specs/PRIMUS/` |
| Arquivo | `90_Arquivo/` |

## Regras

- Nao criar notas soltas fora das pastas canonicas.
- Notas novas devem aparecer em um MOC, dashboard ou README de pasta.
- PDFs e extracoes brutas continuam fora do Git.
- Graph View deve privilegiar caminhos canonicos, nao compatibilidade legada.

## Proxima Higiene

- [ ] Revisar `40_Wiki/_compat_wiki/` em janela propria.
- [ ] Revisar `05_Raw_Sources/_compat_sources/` em janela propria.
- [ ] Criar MOCs tematicos para PRIMUS, MEGATRON, RAG/MCP e PietraOS.
