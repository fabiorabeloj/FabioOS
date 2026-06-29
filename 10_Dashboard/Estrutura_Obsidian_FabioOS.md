---
tipo: dashboard
area: 10_Dashboard
projeto: FabioOS
status: ativo
tags: [fabios, obsidian, dashboard, pastas, governanca]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Estrutura Obsidian FabioOS

## Funcao

Painel rapido para decidir onde salvar novos arquivos no vault.

Documento governante:

- [[60_Sistemas/FabioOS/Estrutura_Canonica_Completa_Obsidian_2026-06-29]]
- [[60_Sistemas/FabioOS/Mapa_Canonico_Pastas_Obsidian_v2_2026-06-29]]
- [[60_Sistemas/Wiki/Estrutura_de_Pastas_LLM_Wiki_FabioOS]]

Plano de migracao:

- [[60_Sistemas/FabioOS/Plano_Normalizacao_Pastas_Obsidian_2026-06-29]]

Auditoria:

- [[50_Registros/Auditoria/Auditoria_Pastas_Obsidian_2026-06-29]]
- [[50_Registros/Auditoria/Proposta_de_Migracao_Estrutural_FabioOS]]

## Destinos canonicos

| Se for... | Salvar em |
|---|---|
| captura temporaria | `00_Inbox/` |
| arquitetura conceitual | `00_Arquitetura/` |
| fonte bruta/evidencia | `05_Raw_Sources/` |
| painel vivo | `10_Dashboard/` |
| area continua | `20_Areas/` |
| projeto ativo | `30_Projetos/` |
| conhecimento processado | `40_Wiki/` |
| decisao, ADR, changelog, sessao ou auditoria | `50_Registros/` |
| sistema, agente, script ou protocolo | `60_Sistemas/` |
| skill reutilizavel | `70_Skills/` |
| spec executavel | `80_Specs/` |
| material encerrado | `90_Arquivo/` |
| schema ou criterio de qualidade | `60_Sistemas/Wiki/schema/` |

## Pastas legadas

Nao criar novos arquivos nestas pastas sem justificativa:

- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/`
- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/`
- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/`
- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Decisoes/`
- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/`
- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/50_Fontes/`
- `05_Raw_Sources/_compat_sources/`
- `40_Wiki/_compat_wiki/`

## Proxima acao

- [x] Aplicar a estrutura canonica completa proposta para a raiz visual do Obsidian.
- [x] Remover arquivos soltos da raiz de `60_Sistemas/`.
- [x] Atualizar backlinks conhecidos dos arquivos movidos.
- [ ] So reindexar RAG/Grafo depois de aprovacao.
