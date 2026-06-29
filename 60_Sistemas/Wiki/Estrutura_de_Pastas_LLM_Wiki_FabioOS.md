---
tipo: documento-estrutural
area: 60_Sistemas/Wiki
projeto: FabioOS
status: ativo
tags: [fabios, llm-wiki, pastas, obsidian, governanca, estrutura]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Estrutura de Pastas LLM Wiki do FabioOS

## Tese

A estrutura de pastas do FabioOS deve seguir a mentalidade LLM Wiki.

Isso significa organizar o vault por funcao cognitiva, nao por IA, ferramenta ou conversa.

O FabioOS separa:

1. fontes brutas;
2. conhecimento processado;
3. areas continuas;
4. projetos;
5. registros historicos;
6. sistemas internos;
7. skills;
8. specs;
9. arquivo morto.

## Por que nao organizar por IA

Nao usar como estrutura principal:

```text
ChatGPT/
Claude/
Codex/
DeepSeek/
Qwen/
Gemini/
```

As IAs sao operadores. Elas produzem, revisam, consultam ou executam tarefas, mas nao sao categorias centrais do conhecimento.

Um conteudo gerado pelo ChatGPT sobre RAG deve ir para `40_Wiki/RAG/` ou `05_Raw_Sources/Conversas/`, conforme esteja processado ou bruto.

## Tres camadas fundamentais

```text
fonte bruta -> conhecimento processado -> operacao do sistema
```

| Camada | Pasta principal | Funcao |
|---|---|---|
| Fonte bruta | `05_Raw_Sources/` | Preservar evidencia original |
| Conhecimento processado | `40_Wiki/` | Criar wiki navegavel e consultavel |
| Operacao | `60_Sistemas/`, `70_Skills/`, `80_Specs/` | Fazer a maquina FabioOS funcionar |

## Estrutura-alvo

```text
00_Inbox/
05_Raw_Sources/
10_Dashboard/
20_Areas/
30_Projetos/
40_Wiki/
50_Registros/
60_Sistemas/
70_Skills/
80_Specs/
90_Arquivo/
```

## Funcao de cada pasta

| Pasta | Funcao | Regra |
|---|---|---|
| `00_Inbox/` | Entrada temporaria | Nada mora aqui para sempre |
| `05_Raw_Sources/` | Evidencia original | Nao editar destrutivamente |
| `10_Dashboard/` | Painel e mapa operacional | Mostrar estado e rotas |
| `20_Areas/` | Areas continuas | Dominios sem fim definido |
| `30_Projetos/` | Projetos ativos | Iniciativas com objetivo e entregas |
| `40_Wiki/` | Conhecimento processado | Paginas compiladas e linkaveis |
| `50_Registros/` | Historico auditavel | Decisoes, logs, changelogs, relatorios |
| `60_Sistemas/` | Mecanismos internos | RAG, MCP, agentes, protocolos, scripts |
| `70_Skills/` | Habilidades reutilizaveis | Competencias carregaveis por agentes |
| `80_Specs/` | Planos executaveis | Spec antes de implementacao relevante |
| `90_Arquivo/` | Arquivo morto | Antigo, substituido ou encerrado |

## Compatibilidade operacional

As pastas `sources/` e `wiki/` continuam existentes.

Motivo:

- ha muitos backlinks Obsidian apontando para esses caminhos;
- RAG, Grafo, MCP e scripts ainda usam esses nomes;
- renomear agora criaria risco alto;
- a migracao deve ocorrer por lotes.

Decisao:

```text
05_Raw_Sources/ = alvo fisico novo para fontes brutas.
sources/ = compatibilidade operacional ate migracao.

40_Wiki/ = alvo fisico novo para conhecimento processado.
wiki/ = compatibilidade operacional ate migracao.
```

## Relacao com RAG

O RAG deve consultar apenas conteudo autorizado.

Prioridade futura:

1. `40_Wiki/`
2. `60_Sistemas/`
3. `50_Registros/Decisoes/`
4. `50_Registros/ADR/`

Fontes brutas sensiveis, inbox e logs runtime nao devem entrar automaticamente no RAG.

## Relacao com MCP

MCPs devem usar esta estrutura como contrato de destino.

Exemplos:

- `criar_nota_fonte` -> `05_Raw_Sources/` ou `sources/` em modo compatibilidade.
- `consultar_wiki` -> `40_Wiki/` e `wiki/`.
- `registrar_decisao` -> `50_Registros/Decisoes/` ou `50_Registros/ADR/`.
- `criar_spec` -> `80_Specs/`.

## Relacao com MEGATRON

MEGATRON deve classificar toda entrada antes de agir:

```text
entrada -> classificar -> destino canonico -> acao permitida -> log
```

MEGATRON nao deve criar arquivos em pastas legadas sem justificativa.

## Relacao com multiplos cerebros

Os cerebros do FabioOS se manifestam por dominios:

| Cerebro | Area | Wiki | Specs |
|---|---|---|---|
| EscolaOS | `20_Areas/EscolaOS/` | `40_Wiki/EscolaOS/` | `80_Specs/EscolaOS/` |
| TraderOS | `20_Areas/TraderOS/` | `40_Wiki/TraderOS/` | `80_Specs/TraderOS/` |
| PRIMUS | `30_Projetos/PRIMUS/` | `40_Wiki/PRIMUS/` | `80_Specs/PRIMUS/` |
| MEGATRON | `30_Projetos/MEGATRON/` | `40_Wiki/FabioOS/` | `80_Specs/MEGATRON/` |

## Regra de classificacao

| Pergunta | Destino |
|---|---|
| Acabou de chegar? | `00_Inbox/` |
| E fonte original? | `05_Raw_Sources/` |
| E painel? | `10_Dashboard/` |
| E area continua? | `20_Areas/` |
| E projeto? | `30_Projetos/` |
| E conhecimento processado? | `40_Wiki/` |
| E decisao/log/historico? | `50_Registros/` |
| E mecanismo interno? | `60_Sistemas/` |
| E habilidade? | `70_Skills/` |
| E plano executavel? | `80_Specs/` |
| E antigo ou encerrado? | `90_Arquivo/` |

## Estrategia de migracao

1. Criar estrutura fisica.
2. Manter compatibilidade com `sources/` e `wiki/`.
3. Mapear equivalencias.
4. Migrar em lotes pequenos.
5. Atualizar backlinks.
6. Registrar changelog.
7. Reindexar RAG/Grafo somente apos aprovacao.

## Riscos

- quebrar links Obsidian;
- desalinhar scripts RAG/MCP;
- duplicar conteudo entre `wiki/` e `40_Wiki/`;
- criar confusao se agentes nao consultarem o mapa antes de escrever;
- versionar fontes sensiveis sem querer.

## Criterios de validacao

- pastas-alvo existem fisicamente;
- cada pasta nova tem README ou nota;
- `CLAUDE.md`, `index.md`, mapa e changelog apontam para a estrutura;
- nenhum arquivo foi apagado;
- `sources/` e `wiki/` continuam preservados;
- commit e feito com stage explicito e scan de segredos.
