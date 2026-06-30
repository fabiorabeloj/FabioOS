---
tipo: matriz
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [governanca, permissoes, agentes, seguranca, mcp]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Matriz de Permissoes FabioOS

## Funcao

Definir o que cada IA, agente ou ferramenta pode fazer no FabioOS.

## Niveis

| Nivel | Nome | Descricao |
|---:|---|---|
| 0 | Leitura | ler, buscar, resumir |
| 1 | Sugestao | propor plano, diff, resposta ou decisao |
| 2 | Escrita Markdown | criar/editar notas e registros |
| 3 | Arquivos do projeto | editar scripts, specs, config versionavel |
| 4 | Execucao local | rodar scripts e comandos nao destrutivos |
| 5 | Acoes externas | email, WhatsApp, GitHub, n8n, publicacao |
| 6 | Sensivel | apagar, credenciais, financeiro, trade, dados restritos |

## Matriz inicial

| Ator | Nivel padrao | Pode | Nao pode sem aprovacao |
|---|---:|---|---|
| ChatGPT | 1 | planejar, explicar, sintetizar | editar vault, enviar dados, acessar credenciais |
| Claude | 2 | arquitetura, documentos, revisao | push, envio externo, acao sensivel |
| Claude Code | 4 | editar repo, rodar testes, preparar commits | push, apagar, credenciais, envio externo |
| Codex | 4 | editar repo, validar, scripts locais | push, apagar, credenciais, envio externo |
| Cursor | 3 | oficina de software com supervisao | agir autonomamente no vault |
| OpenClaw | 1 | canal conversacional e visualizacao | WhatsApp real sem aprovacao |
| n8n | 5 | workflows aprovados e logados | workflow critico sem decisao |
| MEGATRON | 1 | rotear, consultar, propor acao | executar sensivel sem humano |
| Agentes futuros | definido por contrato | executar escopo proprio | sair do contrato |

## Regras obrigatorias

- Nenhum agente envia email sem aprovacao.
- Nenhum agente envia WhatsApp sem aprovacao.
- Nenhum agente apaga arquivo sem aprovacao.
- Nenhum agente executa comando destrutivo sem aprovacao.
- Nenhum agente altera regra de trade sem aprovacao.
- Nenhum agente mexe em credenciais.
- Nenhum agente publica conteudo externo sem aprovacao.
- Nenhum agente altera workflow critico sem decisao registrada.

## Escalada

Se houver duvida sobre permissao, escolher o nivel mais restritivo e pedir aprovacao humana.

## Relacoes

- [[50_Registros/Decisoes/Constituicao_Operacional_FabioOS]]
- [[60_Sistemas/FabioOS/Matriz_Dominios_Dados_Permissoes_2026-06-28]]
- [[10_Dashboard/RAG_MCP_Control_Plane]]
