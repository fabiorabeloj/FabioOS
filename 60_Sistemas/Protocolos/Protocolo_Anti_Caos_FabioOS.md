---
tipo: protocolo
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [anti-caos, governanca, revisao, vault, manutencao]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Protocolo Anti-Caos FabioOS

## Funcao

Impedir que o FabioOS vire deposito de notas, agentes, automacoes e decisoes desconectadas.

## Rotina semanal

1. Revisar `00_Inbox/`.
2. Processar capturas.
3. Consolidar notas duplicadas.
4. Revisar decisoes pendentes.
5. Atualizar `STATUS.md`.
6. Atualizar `NEXT_ACTIONS.md`.
7. Atualizar changelog.
8. Verificar Git.
9. Verificar n8n.
10. Verificar OpenClaw.
11. Verificar arquivos sem categoria.
12. Verificar tarefas vencidas.
13. Arquivar projetos mortos.
14. Registrar relatorio semanal.

## Criterios de alerta

| Alerta | Criterio |
|---|---|
| nota duplicada | duas notas com mesma funcao e sem relacao |
| nota orfa | sem link de entrada, tag ou index |
| decisao sem consequencia | decisao sem tarefa, status ou efeito |
| projeto parado | sem proxima acao clara |
| automacao quebrada | workflow sem ultimo teste ou log |
| agente redundante | dois agentes com mesma missao sem diferenca |
| arquivo fora de padrao | sem frontmatter, local ou nome adequado |

## Regras

- Nao apagar durante revisao anti-caos sem aprovacao.
- Preferir marcar `status: revisar`.
- Consolidacao grande exige plano e changelog.
- Se houver conflito entre criar e consolidar, consolidar primeiro.

## Saida esperada

Relatorio em `50_Registros/Auditoria/` com:

- data;
- escopo;
- achados;
- acoes recomendadas;
- itens que exigem Fabio;
- proxima revisao.

## Relacoes

- [[60_Sistemas/Wiki/Protocolo_Lint_LLM_Wiki]]
- [[60_Sistemas/Protocolos/Definicao_de_Concluido_FabioOS]]
- [[wiki/conceitos/governanca-operacional-fabios]]
