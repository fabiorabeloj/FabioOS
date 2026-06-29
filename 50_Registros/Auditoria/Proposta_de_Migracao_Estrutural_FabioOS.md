---
tipo: proposta-migracao
area: 50_Registros/Auditoria
projeto: FabioOS
status: ativo
tags: [fabios, migracao, obsidian, llm-wiki, auditoria]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Proposta de Migracao Estrutural do FabioOS

## Objetivo

Propor a migracao do vault para a estrutura LLM Wiki sem quebrar links, RAG, MCP, Grafo, agentes ou historico Git.

## Estrutura atual observada

Pastas principais existentes antes da criacao fisica:

- `00_Arquitetura/`
- `00_Inbox/`
- `10_Dashboard/`
- `10_Mapas/`
- `20_Projetos/`
- `30_Conhecimento/`
- `30_Projetos/`
- `40_Decisoes/`
- `40_Repertorio/`
- `50_Fontes/`
- `50_Registros/`
- `60_Sistemas/`
- `90_Arquivo/`
- `schema/`
- `sources/`
- `wiki/`

## Estrutura-alvo

- `00_Inbox/`
- `05_Raw_Sources/`
- `10_Dashboard/`
- `20_Areas/`
- `30_Projetos/`
- `40_Wiki/`
- `50_Registros/`
- `60_Sistemas/`
- `70_Skills/`
- `80_Specs/`
- `90_Arquivo/`

## Pastas equivalentes

| Atual | Alvo | Acao recomendada |
|---|---|---|
| `sources/` | `05_Raw_Sources/` | Manter como compatibilidade; migrar depois por lote |
| `wiki/` | `40_Wiki/` | Manter como compatibilidade; migrar depois por lote |
| `10_Mapas/` | `10_Dashboard/` ou `40_Wiki/_MOCs/` | Migrar mapas vivos para dashboard e mapas conceituais para MOCs |
| `20_Projetos/` | `30_Projetos/` ou `20_Areas/` | Separar projeto ativo de area continua |
| `30_Conhecimento/` | `40_Wiki/` | Migrar conhecimento processado apos curadoria |
| `40_Decisoes/` | `50_Registros/Decisoes/` ou `50_Registros/ADR/` | Migrar decisoes em formato ADR quando fizer sentido |
| `40_Repertorio/` | `40_Wiki/` ou manter como repertorio transitorio | Integrar gradualmente |
| `50_Fontes/` | `05_Raw_Sources/` | Converter indices antigos ou preservar em arquivo |
| `60_Sistemas/FabioOS/specs/` | `80_Specs/FabioOS/` | Migrar specs somente apos atualizar links |
| `60_Sistemas/Skills/` | `70_Skills/` | Manter inventario tecnico; espelhar conhecimento humano em `70_Skills/` |

## Arquivos ja corretos

- `CLAUDE.md`
- `AGENTS.md`
- `index.md`
- `log.md`
- `60_Sistemas/FabioOS/STATUS.md`
- `60_Sistemas/FabioOS/NEXT_ACTIONS.md`
- `60_Sistemas/FabioOS/Registro_Frentes_Ativas.md`
- `50_Registros/Changelog/`
- `60_Sistemas/RAG/`
- `60_Sistemas/MCP_FabioOS/`
- `60_Sistemas/MEGATRON/`

## Arquivos possivelmente fora de lugar

Exemplos a revisar:

- mapas de `10_Mapas/`;
- projetos em `20_Projetos/`;
- conhecimento em `30_Conhecimento/`;
- decisoes em `40_Decisoes/`;
- fontes antigas em `50_Fontes/`;
- specs dentro de `60_Sistemas/FabioOS/specs/`.

## Pastas redundantes

Redundantes nao significa apagaveis.

| Grupo | Risco |
|---|---|
| `sources/` e `05_Raw_Sources/` | Duplicar fontes se agentes escreverem nos dois sem regra |
| `wiki/` e `40_Wiki/` | Duplicar conhecimento processado |
| `10_Mapas/` e `10_Dashboard/` | Duplicar paineis/mapas |
| `40_Decisoes/` e `50_Registros/Decisoes/` | Perder historico de decisoes |

## O que nao deve ser movido agora

- `sources/`
- `wiki/`
- `60_Sistemas/RAG/fabioos_db/`
- `60_Sistemas/Grafo/data/`
- `.agents/skills/`
- `.claude/`
- `.codex/`
- arquivos restritos de email/drive;
- qualquer arquivo com links muito citados sem revisar backlinks.

## O que exige revisao humana

- migracao de fontes sensiveis;
- migracao de e-mails;
- migracao de dados pessoais;
- promocao de conteudo para RAG/Grafo;
- alteracao de scripts que dependem de `sources/` ou `wiki/`;
- remocao de qualquer pasta legada.

## Etapas recomendadas

1. Commitar a estrutura fisica v1.
2. Rodar auditoria de backlinks por grupo.
3. Migrar primeiro `40_Decisoes/` para `50_Registros/Decisoes/` em lote pequeno.
4. Migrar mapas selecionados de `10_Mapas/`.
5. Migrar specs para `80_Specs/` somente apos ajustar links.
6. Atualizar RAG/MCP para aceitar aliases.
7. So entao decidir se `sources/` e `wiki/` viram aliases permanentes ou sao migrados fisicamente.

## Recomendacao final

Adotar a estrutura fisica LLM Wiki agora, mas tratar `sources/` e `wiki/` como aliases operacionais ate que RAG, MCP, Grafo e backlinks estejam preparados.
