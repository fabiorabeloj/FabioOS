---
tipo: plano
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, obsidian, normalizacao, migracao, governanca]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Plano de Normalizacao das Pastas do Obsidian

## Objetivo

Resolver incongruencias de nomes e numeros repetidos no vault sem apagar arquivos, sem quebrar links e sem atrapalhar RAG, Grafo, Claude, Codex, Cursor ou OpenClaw.

## Escopo desta rodada

Esta rodada faz:

- auditoria;
- mapa canonico v2;
- regra de criacao de novos arquivos;
- atualizacao dos pontos de entrada;
- plano de migracao futura.

Esta rodada nao faz:

- mover pastas inteiras;
- apagar pastas legadas;
- reindexar RAG;
- regenerar grafo;
- fazer commit;
- fazer push.

## Ordem de normalizacao

### Etapa 1 - Travar regra para novos arquivos

Status: em execucao.

Regra:

```text
Novo conteudo entra apenas na estrutura canonica v2.
Pasta legada so recebe manutencao de conteudo legado.
```

### Etapa 2 - Migrar mapas

Prioridade: alta.

Origem:

- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/`

Destino:

- dashboards vivos -> `10_Dashboard/`
- mapas de navegacao -> `40_Wiki/_MOCs/` ou compatibilidade `40_Wiki/_compat_wiki/indices/`

Observacao:

`90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/` tem muitos pontos de entrada humanos. Migrar com cuidado e preservar redirecionamentos.

### Etapa 3 - Migrar projetos

Prioridade: media.

Origem:

- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/`

Destino:

- projetos ativos -> `30_Projetos/`
- areas continuas -> `20_Areas/`
- projetos encerrados -> `90_Arquivo/`

Primeiros candidatos:

- FabioOS;
- PRIMUS;
- Trader;
- Escola;
- Atendimento Pietra.

### Etapa 4 - Migrar conhecimento

Prioridade: media.

Origem:

- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/`

Destino:

- conceitos compilados -> `40_Wiki/`
- repertorio/matrizes/catalogos -> `40_Wiki/`

Regra:

Nao migrar dump antigo sem curadoria. Conteudo promovido deve ganhar metadados e relacoes.

### Etapa 5 - Migrar decisoes

Prioridade: alta.

Origem:

- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Decisoes/`

Destino:

- `50_Registros/Decisoes/`

Regra:

Decisao futura deve ter contexto, decisao, consequencias e status.

### Etapa 6 - Migrar fontes

Prioridade: baixa/media.

Origem:

- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/50_Fontes/`

Destino:

- `05_Raw_Sources/`

Regra:

Fontes novas entram em `05_Raw_Sources/`; arquivos antigos de `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/50_Fontes/` podem virar indices historicos ou serem migrados para `05_Raw_Sources/` com metadados. `05_Raw_Sources/_compat_sources/` fica como compatibilidade operacional ate migracao de scripts/RAG/MCP.

## Politica de redirecionamento

Quando um arquivo antigo for movido e possuir links relevantes:

1. manter uma nota curta no caminho antigo;
2. indicar `Migrado para: [[novo/caminho]]`;
3. atualizar o mapa principal;
4. registrar no changelog;
5. so remover o redirecionamento depois de revisar backlinks.

## Critérios de qualidade

Uma migracao esta correta quando:

- o arquivo tem destino canonico claro;
- links internos foram atualizados;
- frontmatter continua valido;
- nenhum conteudo foi perdido;
- changelog registra a mudanca;
- RAG/Grafo so sao atualizados depois de aprovacao.

## Proxima acao recomendada

Depois de revisar este plano, executar uma migracao piloto pequena:

```text
Migrar 1 mapa de `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/` para `40_Wiki/_MOCs/` ou `10_Dashboard/`
ou
migrar 1 decisao de `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Decisoes/` para `50_Registros/Decisoes/`
```

A migracao piloto deve ser feita antes de qualquer lote maior.
