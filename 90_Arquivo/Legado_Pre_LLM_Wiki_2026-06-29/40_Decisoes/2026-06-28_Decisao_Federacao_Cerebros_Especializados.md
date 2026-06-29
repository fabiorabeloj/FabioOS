---
tipo: decisao
area: 40_Decisoes
projeto: FabioOS
status: ativo
tags: [fabios, arquitetura, dominios, rag, megatron]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
fonte: [[05_Raw_Sources/_compat_sources/docs/2026-06-28_anuncios-ia-roadmap-fabioos]]
---

# Decisao - Federacao de Cerebros Especializados

## Pergunta

O FabioOS deve ser um cerebro unico ou uma federacao de cerebros especializados?

## Decisao

O FabioOS deve evoluir como **federacao de dominios/memorias especializadas**, coordenada por MEGATRON.

Isso nao significa criar varios sistemas agora. Significa desenhar limites desde ja para evitar que tudo vire uma memoria misturada.

## Motivo

Um unico vault/RAG generico tende a misturar:

- vida pessoal;
- trabalho docente;
- atendimento Pietra;
- trading;
- IA e automacao;
- PRIMUS;
- financas;
- saude;
- estudos.

Com o tempo, isso reduz precisao, aumenta risco de contexto errado e dificulta permissoes.

## Modelo adotado

```text
MEGATRON
  -> FabioOS central
  -> PietraOS / EscolaOS
  -> TraderOS
  -> PrimusOS
  -> IAOS
```

MEGATRON coordena. Cada dominio guarda sua propria memoria, vocabulario, permissoes e criterios.

## Efeito nas fases

- RAG geral continua existindo.
- RAGs ou indices especializados so surgem quando houver volume e risco suficientes.
- Grafo pode conectar dominios sem misturar tudo em uma unica resposta.
- MCP FabioOS deve permitir consultar dominios por escopo.
- Dashboard deve mostrar qual dominio esta ativo.

## Regra

Toda nova informacao importante deve responder:

1. Pertence ao FabioOS central?
2. Pertence a PietraOS/EscolaOS?
3. Pertence a TraderOS?
4. Pertence a PrimusOS?
5. Pertence a IAOS?
6. Pode ser compartilhada entre dominios?
7. Tem restricao de privacidade?

## Proxima acao

Criar uma matriz de dominios especializados e decidir criterios para RAG unico vs RAG separado.
