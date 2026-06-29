---
tipo: relatorio-validacao
area: 60_Sistemas
projeto: FabioOS
status: parcial
fase: 12
tags: [rag, validacao, fase-12, recuperacao, continuidade]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Relatorio de Validacao RAG - 2026-06-27

## Funcao

Registrar a validacao executada pelo Codex enquanto Claude estava indisponivel, seguindo o [[60_Sistemas/FabioOS/Protocolo_Gestao_Contexto_IA]].

Este relatorio nao promove a Fase 12 para piloto. Ele documenta evidencias, resultados, lacunas e proximas acoes.

## Estado verificado

| Item | Resultado |
|---|---|
| Banco Chroma | presente em `60_Sistemas/RAG/fabioos_db/` |
| Colecao | `fabioos` |
| Total de chunks | `1795` apos restauracao |
| Log de ingestao | concluiu com sucesso |
| Arquivos seguros encontrados na ingestao | `133` |
| Modelo local | `BAAI/bge-m3` |
| Modo de consulta | recuperacao, sem `--generate` |
| API externa | nao usada |

## Escopo indexado confirmado

Verificacao direta de metadados no Chroma:

| Fonte | Chunks |
|---|---:|
| `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Painel_Pendencias_FabioOS.md` | 13 |
| `wiki/indices/mapa-fabios.md` | 15 |
| `60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG.md` | 17 |
| `60_Sistemas/FabioOS/Roteiro_Execucao_Fase12_RAG.md` | 11 |

Conclusao: a ingestao atual foi restaurada e esta completa o suficiente para validacao inicial. O problema encontrado era de ranking/recencia, nao de ausencia do Painel no indice.

## Resultado das 10 perguntas reais

| # | Pergunta | Resultado | Fontes principais |
|---|---|---|---|
| 1 | O que e o FabioOS em uma frase? | bom | Modelo Formal, `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/FabioOS.md`, Plano Mestre |
| 2 | Qual e a fase atual do FabioOS? | fraco | recuperou relatorio antigo e documentos gerais; nao trouxe Painel no top 12 |
| 3 | Quais pendencias estao abertas antes da Fase 12? | parcial | trouxe Plano de Validacao/Roteiro; Painel aparece apenas em top 7/top 9 |
| 4 | O que o Modelo Formal define sobre conhecimento? | bom | Modelo Formal |
| 5 | Como MEGATRON deve declarar ignorancia? | bom | Modelo Formal, regra de ignorancia explicita |
| 6 | Qual e o papel do SafeCommit? | bom | spec SafeCommit e revisao de implementacao |
| 7 | Como o Arquivista transforma conteudo bruto? | bom | spec Arquivista |
| 8 | Quais pastas nao devem entrar no indice RAG? | bom | spec RAG, preflight RAG |
| 9 | Como PietraOS pode evoluir para SaaS? | bom | Modelo Formal, wiki Pietra |
| 10 | Como PrimusOS organiza memoria narrativa? | bom | Modelo Formal, Plano Mestre, nota de memoria |

Resumo:

- 8/10 respostas boas.
- 1/10 parcial.
- 1/10 fraca.
- 10/10 trouxeram fontes quando houve evidencia.
- O criterio de utilidade minima foi quase atingido, mas o criterio de status atual ainda falha.

## Testes de seguranca

Foram testadas consultas sobre:

- senha do banco vetorial;
- token, Bearer, API key e segredo;
- `.codex/config.toml`;
- `sources/_inbox`;
- logs runtime dos agentes.

Resultado:

- nenhum caminho proibido apareceu como hit;
- nenhum conteudo de `.codex`, `.obsidian`, `.claude`, `00_Inbox`, `sources/_inbox`, `.venv` ou logs runtime apareceu no resultado;
- houve falsos positivos documentais em guias que falam sobre credenciais, sem exposicao de valor real.

## Achado principal

### P1 - Consultas de status operacional precisam de ranking por recencia/autoridade

Perguntas genericas como:

```text
Qual e a fase atual do FabioOS?
```

recuperam relatorios antigos e documentos conceituais antes do Painel de Pendencias.

Quando a consulta inclui termos como:

```text
Proximo passo de execucao confirmado Fase 12 Painel de Pendencias FabioOS
```

o Painel aparece em primeiro lugar.

Interpretacao: o indice contem a fonte correta, mas a busca vetorial pura nao prioriza documentos operacionais atuais.

## Recomendacao tecnica

Antes de promover a Fase 12 para piloto, implementar pelo menos uma das opcoes:

1. aumentar `--k` padrao para consultas operacionais;
2. adicionar boost de fontes canonicas para perguntas de status:
   - `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Painel_Pendencias_FabioOS.md`;
   - `wiki/indices/mapa-fabios.md`;
   - ultimo changelog;
3. criar modo `--profile status` no `query_rag.py`;
4. no futuro, combinar busca vetorial com busca lexical e recencia.

## Decisao operacional

Fase 12 deve permanecer como:

```text
validacao parcial concluida; nao promover para piloto ainda.
```

## Atualizacao apos restauracao

Durante a continuidade, houve colisao operacional de reindexacao. A colecao `fabioos` foi restaurada com reingestao completa:

- arquivos seguros: `144`;
- chunks: `1795`;
- caminhos proibidos: nenhum;
- `STATUS.md` indexado;
- `NEXT_ACTIONS.md` indexado;
- Painel de Pendencias indexado.

Tambem foi aplicado ajuste em `query_rag.py` para consultas operacionais priorizarem fontes canonicas.

Validacao rapida apos ajuste:

- `Qual e a fase atual do FabioOS?` recupera Painel/STATUS no topo.
- `Quais pendencias estao abertas antes da Fase 12?` recupera Painel/STATUS no topo.

Ainda falta repetir a bateria completa das 10 perguntas antes de qualquer promocao para piloto.

## Proximas acoes

- [x] Corrigir ranking/recencia para consultas de status.
- [ ] Reexecutar as 10 perguntas apos ajuste.
- [ ] Testar ignorancia explicita com respostas geradas somente quando houver modo seguro.
- [ ] Registrar decisao de promocao para piloto apenas apos revisao humana.

## Relacoes

- [[60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG]]
- [[60_Sistemas/FabioOS/Roteiro_Execucao_Fase12_RAG]]
- [[60_Sistemas/RAG/Relatorio_Validacao_Parcial_RAG_2026-06-26]]
- [[60_Sistemas/FabioOS/Protocolo_Gestao_Contexto_IA]]
