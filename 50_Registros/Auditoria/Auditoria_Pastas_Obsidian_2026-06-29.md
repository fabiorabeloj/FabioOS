---
tipo: auditoria
area: 50_Registros
projeto: FabioOS
status: ativo
tags: [fabios, obsidian, auditoria, pastas, governanca, llm-wiki]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Auditoria de Pastas do Obsidian - 2026-06-29

## Funcao

Registrar as incongruencias de pastas, nomes e numeros repetidos no vault do FabioOS antes de qualquer migracao fisica.

## Diagnostico

O vault esta em uma fase de transicao entre duas estruturas:

1. Estrutura inicial, criada para navegacao humana rapida.
2. Estrutura v2, criada para LLM Wiki, governanca, agentes, RAG, MCP, grafos e operacao profissional.

O problema nao e perda de dados. O problema e sobreposicao de funcoes.

## Duplicacoes encontradas

| Par ou grupo | Situacao | Decisao recomendada |
|---|---|---|
| `10_Mapas/` e `10_Dashboard/` | Ambos usam numero 10, mas cumprem funcoes diferentes. | `10_Dashboard/` vira canonico para paineis operacionais; mapas navegaveis devem ir para `40_Wiki/_MOCs/`; `10_Mapas/` fica legado ate migracao assistida. |
| `20_Projetos/` e `30_Projetos/` | `20_Projetos/` guarda projetos antigos; `30_Projetos/` nasceu como destino v2. | `30_Projetos/` vira canonico para projetos; `20_Projetos/` fica legado e deve ser migrado por lotes. |
| `30_Conhecimento/`, `40_Repertorio/` e `40_Wiki/` | `30_Conhecimento` e `40_Repertorio` guardam conhecimento antigo; `40_Wiki` e o destino v2. | `40_Wiki/` vira canonico para conhecimento processado; as pastas antigas ficam legadas. |
| `40_Decisoes/` e `50_Registros/Decisoes/` | Decisoes antigas e ADRs novos estao separados. | `50_Registros/Decisoes/` vira canonico para decisoes versionadas; `40_Decisoes/` fica legado. |
| `50_Fontes/`, `sources/` e `05_Raw_Sources/` | `50_Fontes` contem indices antigos; `sources` contem fontes brutas reais; `05_Raw_Sources` e o destino v2. | `05_Raw_Sources/` vira canonico para fonte bruta; `sources/` fica compatibilidade operacional. |
| `60_Sistemas/Agentes/` e `60_Sistemas/MEGATRON/agentes/` | Contratos gerais e specs/implementacoes do MEGATRON podem se confundir. | `60_Sistemas/Agentes/` = contratos transversais; `60_Sistemas/MEGATRON/agentes/` = agentes especificos do MEGATRON. |
| `wiki/`, `30_Conhecimento/` e `40_Wiki/` | Todos podem parecer conhecimento. | `40_Wiki/` = conhecimento processado alvo; `wiki/` fica compatibilidade operacional ate migracao de links/RAG/MCP. |

## Regra anti-caos

Nao mover pastas inteiras agora.

Motivos:

- ha muitos links Obsidian apontando para caminhos antigos;
- RAG e Grafo podem ter sido gerados com caminhos existentes;
- existem alteracoes de outras frentes no working tree;
- migracao fisica em massa criaria risco alto para pouco ganho imediato.

## Estrategia correta

1. Declarar a estrutura canonica v2.
2. Marcar pastas antigas como legado operacional.
3. Atualizar `CLAUDE.md`, mapa e status para impedir novas criacoes no lugar errado.
4. Migrar arquivos somente quando forem tocados, revisados ou promovidos.
5. Para cada migracao, atualizar backlinks, changelog, RAG/Grafo apenas depois de aprovacao.

## Pastas legadas

Estas pastas nao devem receber novos arquivos, salvo manutencao de conteudo ja existente:

- `10_Mapas/`
- `20_Projetos/`
- `30_Conhecimento/`
- `40_Decisoes/`
- `40_Repertorio/`
- `50_Fontes/`
- `sources/`
- `wiki/`

## Pastas canonicas v2

Novos arquivos devem preferir:

- `10_Dashboard/`
- `30_Projetos/`
- `40_Wiki/`
- `50_Registros/`
- `60_Sistemas/`
- `05_Raw_Sources/`
- `70_Skills/`
- `80_Specs/`
- `schema/`

## Criterio de aceite

A normalizacao desta rodada esta aceita quando:

- existe um mapa canonico de pastas;
- a regra aparece no `CLAUDE.md`;
- o painel e o indice principal apontam para a decisao;
- nenhum arquivo foi apagado;
- nenhuma migracao fisica em massa foi feita sem plano.
