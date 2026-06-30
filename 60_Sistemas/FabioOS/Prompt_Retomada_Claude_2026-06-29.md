---
tipo: prompt-retomada
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, claude, retomada, handoff, rag]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Prompt de Retomada para Claude - 2026-06-29

## Prompt para colar

```text
Leia o contexto do FabioOS e continue a partir do ultimo changelog.

Contexto adicional obrigatorio:
- Leia 60_Sistemas/FabioOS/STATUS.md
- Leia 60_Sistemas/FabioOS/NEXT_ACTIONS.md
- Leia 60_Sistemas/FabioOS/Registro_Frentes_Ativas.md
- Leia 60_Sistemas/FabioOS/Incidente_Coordenacao_RAG_2026-06-27.md
- Leia 60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-27.md
- Leia 50_Registros/Changelog/2026-06-27_validacao-rag-continuidade.md

Estado real:
- Claude ficou indisponivel ate segunda-feira.
- Codex aplicou o protocolo de continuidade.
- A ingestao RAG foi restaurada e concluiu com 1795 chunks.
- As 10 perguntas de validacao foram executadas em modo recuperacao, sem --generate e sem API externa.
- Resultado: 8 boas, 1 parcial, 1 fraca.
- Problema P1 original: consultas genericas de status atual nao priorizavam Painel_Pendencias_FabioOS.md, mesmo ele estando indexado.
- Mitigacao aplicada: `query_rag.py` passou a priorizar fontes canonicas em consultas operacionais; consultas "fase atual" e "pendencias" agora recuperam Painel/STATUS no topo.
- Incidente: houve colisao de reindexacao; daqui em diante, verificar `Registro_Frentes_Ativas.md` antes de reindexar, mover, apagar ou commitar artefato compartilhado.
- Fase 12 NAO deve ser promovida para piloto ainda.

Arquivos criados pela continuidade Codex:
- 60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-27.md
- 60_Sistemas/FabioOS/STATUS.md
- 60_Sistemas/FabioOS/NEXT_ACTIONS.md
- 60_Sistemas/FabioOS/Prompt_Retomada_Claude_2026-06-29.md
- 60_Sistemas/FabioOS/Registro_Frentes_Ativas.md
- 60_Sistemas/FabioOS/Incidente_Coordenacao_RAG_2026-06-27.md
- 50_Registros/Changelog/2026-06-27_validacao-rag-continuidade.md

Arquivo ajustado por seguranca:
- 60_Sistemas/OpenClaw/setup/EVOLUTION_API_SETUP.md
  Motivo: trocar chave de exemplo por placeholder explicito.

Proxima acao recomendada:
1. Reexecutar as 10 perguntas apos o ajuste de ranking.
2. Atualizar o relatorio RAG com a revalidacao completa.
3. Rodar scan de segredos.
4. Preparar commits tematicos sem push.

Regras:
- Nao fazer push.
- Nao expor tokens.
- Nao apagar arquivos.
- Nao promover agentes nem RAG para piloto sem revisao humana.
- Respeitar as alteracoes do working tree e nao sobrescrever trabalho do Codex.
```

## Observacao

Este prompt existe para que o usuario nao precise recontar manualmente o que aconteceu durante a ausencia do Claude.
