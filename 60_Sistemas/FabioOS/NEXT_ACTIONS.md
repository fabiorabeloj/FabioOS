---
tipo: next-actions
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, proximas-acoes, continuidade, rag]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# NEXT ACTIONS - FabioOS

## Agora

- [x] Ajustar `query_rag.py` para priorizar fontes canonicas em consultas de status operacional.
- [ ] Reexecutar as 10 perguntas do [[60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG]] apos o ajuste de ranking.
- [ ] Atualizar [[60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-27]] com o resultado pos-ajuste.
- [ ] Rodar scan de segredos antes de qualquer commit.

## Quando Claude voltar

- [ ] Ler [[60_Sistemas/FabioOS/STATUS]].
- [ ] Ler [[60_Sistemas/FabioOS/Prompt_Retomada_Claude_2026-06-29]].
- [ ] Ler [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]] antes de reindexar ou commitar.
- [ ] Ler [[60_Sistemas/FabioOS/Incidente_Coordenacao_RAG_2026-06-27]].
- [ ] Revisar a sequencia de commits por tema.
- [ ] Nao promover RAG para piloto sem resolver o ranking de status.

## Pendencias estruturais

- [ ] Decidir se `60_Sistemas/FabioOS/STATUS.md` e `NEXT_ACTIONS.md` viram arquivos canonicos permanentes.
- [ ] Integrar STATUS/NEXT_ACTIONS ao `start_fabioos.ps1`.
- [ ] Criar rotina mensal de limpeza segura somente leitura antes de qualquer remocao.

## Bloqueios

- Push para GitHub depende de aprovacao humana.
- Envio WhatsApp/n8n externo depende de aprovacao humana.
- Exclusao ou limpeza destrutiva depende de aprovacao humana.
