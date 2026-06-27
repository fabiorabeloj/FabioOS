---
tipo: incidente-operacional
area: 60_Sistemas
projeto: FabioOS
status: resolvido
tags: [fabios, rag, multiagente, incidente, coordenacao]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Incidente de Coordenacao RAG - 2026-06-27

## Resumo

Durante trabalho paralelo entre Codex e Claude, Codex iniciou uma reindexacao RAG sem lock operacional explicito. A colecao Chroma `fabioos` foi apagada antes da nova ingestao completar.

## Impacto

- Colecao RAG ficou temporariamente ausente.
- Foi necessaria restauracao completa do indice.
- O risco principal foi um agente apagar/recriar artefato compartilhado enquanto outro agente ainda podia depender dele.

## Causa

Ausencia de protocolo pratico de lock para artefatos compartilhados.

O protocolo multiagente existia, mas ainda nao havia um registro operacional simples indicando:

- quem e dono da frente;
- quais artefatos estao em uso;
- que operacoes destrutivas estao bloqueadas;
- quando a frente foi concluida.

## Correcao executada

- Criado `60_Sistemas/FabioOS/Registro_Frentes_Ativas.md`.
- Atualizado `60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente.md` com regra de lock.
- Restaurada a colecao RAG por reingestao completa.
- Validado `COUNT=1795` no Chroma.
- Validado que nao ha caminhos proibidos no indice.
- Ajustado `query_rag.py` para priorizar fontes canonicas em consultas operacionais.

## Validacao

Consultas testadas em modo recuperacao, sem `--generate`:

- `Qual e a fase atual do FabioOS?`
- `Quais pendencias estao abertas antes da Fase 12?`

Resultado: ambas recuperam o Painel de Pendencias e STATUS operacional no topo.

## Regra nova

```text
Se uma acao pode apagar, recriar, reindexar, mover ou commitar trabalho de outro agente, ela exige lock em Registro_Frentes_Ativas.md.
```

Nenhum agente deve encerrar processo de outro agente sem confirmacao humana explicita.

## Licao operacional

O usuario nao deve ser responsavel por coordenar manualmente conflitos entre IAs. O proprio FabioOS deve manter estado compartilhado, locks, status e handoff.

## Relacoes

- [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]]
- [[60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente]]
- [[60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-27]]
- [[60_Sistemas/FabioOS/STATUS]]
