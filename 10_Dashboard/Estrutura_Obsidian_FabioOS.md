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
| schema ou criterio de qualidade | `schema/` |

## Pastas legadas

Nao criar novos arquivos nestas pastas sem justificativa:

- `10_Mapas/`
- `20_Projetos/`
- `30_Conhecimento/`
- `40_Decisoes/`
- `40_Repertorio/`
- `50_Fontes/`
- `sources/`
- `wiki/`

## Proxima acao

- [ ] Escolher uma migracao piloto pequena.
- [ ] Atualizar backlinks.
- [ ] Registrar no changelog.
- [ ] So reindexar RAG/Grafo depois de aprovacao.
