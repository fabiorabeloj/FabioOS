---
tipo: dashboard
area: FabioOS
projeto: FabioOS
status: ativo
tags: [rag, mcp, control-plane, governanca, megatron]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# RAG MCP Control Plane

## Funcao

Centralizar o estado de RAGs e MCPs do FabioOS.

RAG e memoria consultavel. MCP e ferramenta acionavel. MEGATRON decide quando usar cada um.

## Regra central

Todo RAG e todo MCP deve possuir escopo, permissao, teste, log, metrica, risco e revisao periodica.

## RAGs

| RAG | Status | Escopo | Fonte principal | Teste |
|---|---|---|---|---|
| RAG_FabioOS_Geral | ativo/local | wiki, sistemas, conhecimento, decisoes, mapas | `60_Sistemas/RAG/fabioos_db/` | validacao registrada com 1795 chunks |
| RAG_EscolaOS | planejado | materiais escolares e PietraOS | a definir | golden questions escolares |
| RAG_TraderOS | planejado | regras, diario, risco e financas | a definir | golden questions de risco |
| RAG_PRIMUS | planejado | lore, campanhas e regras | a definir | continuidade narrativa |
| RAG_IA | planejado | repertorio IA e ferramentas | `40_Wiki/IA/`, `40_Wiki/Modelos_e_IAs/` e compatibilidade `wiki/sistemas/` | perguntas de modelos/ferramentas |
| RAG_Radar_Tecnologico | planejado | anuncios, demos e tendencias processadas | `40_Wiki/Radar_Tecnologico/` e compatibilidade `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/Tecnologia/` | aplicabilidade no FabioOS |
| RAG_Governanca | planejado | protocolos, decisoes e auditoria | `50_Registros/`, `60_Sistemas/FabioOS/` | permissoes/seguranca |
| RAG_Skills | planejado | skills e comandos | `70_Skills/`, `.agents/skills/`, `60_Sistemas/Skills/` | roteamento de capacidades |
| RAG_Specs | planejado | specs e planos | `80_Specs/` e compatibilidade `60_Sistemas/FabioOS/specs/` | spec por tarefa |

## MCPs

| MCP | Status | Risco | Permissao | Observacao |
|---|---|---|---|---|
| filesystem | configurado em Claude | 1-3 | leitura/escrita local conforme sessao | exigir cuidado antes de mover/apagar |
| github | configurado em Claude | 4 | acoes externas exigem aprovacao | sem push sem OK humano |
| playwright-mcp | configurado em Claude | 2-4 | browser controlado | cuidado com formularios externos |
| obsidian | configurado em Claude | 1-2 | leitura/escrita no vault | exige schema e log |
| n8n-mcp | configurado em Claude | 3-5 | workflows | nao alterar workflow critico sem decisao |
| n8n-docs | configurado | 0 | documentacao | seguro para consulta |
| MCP_FabioOS | em frente do Claude | 0-1 | leitura de RAG/Grafo/vault | nao tocar sem handoff |
| Codex MCP/tools | ativo nesta sessao | 0-3 | filesystem e shell local | sem automacao externa sem aprovacao |

## Matriz de risco

| Risco | Descricao | Aprovacao |
|---|---|---|
| 0 | leitura | nao exige, salvo dados sensiveis |
| 1 | escrita leve em Markdown | pode executar com registro |
| 2 | escrita estrutural | exige plano e changelog |
| 3 | execucao local | exige justificativa e log |
| 4 | acao externa | exige aprovacao humana |
| 5 | acao sensivel | exige aprovacao explicita e decisao registrada |

## Regras

- Nenhum MCP envia email sem aprovacao.
- Nenhum MCP envia WhatsApp sem aprovacao.
- Nenhum MCP apaga arquivo sem aprovacao.
- Nenhum MCP altera credenciais.
- Nenhum MCP mexe em financas ou regra de trade.
- Nenhum MCP publica conteudo externo sem autorizacao.
- Nenhum MCP altera workflow critico sem registrar decisao.

## Golden questions iniciais

FabioOS:

- O que e MEGATRON?
- Qual e a fase atual do FabioOS?
- Quais regras impedem apagar RAG DB?
- Onde esta a matriz de aptidao das IAs?

LLM Wiki:

- O que e fonte bruta?
- Quando criar pagina nova?
- Quando atualizar pagina existente?
- Qual e o papel de index.md e log.md?

Governanca:

- Quais acoes exigem aprovacao humana?
- O que significa tarefa concluida?
- Qual e o risco de MCP externo?

## Proximas revisoes

- [ ] Criar ficha tecnica formal do RAG_FabioOS_Geral.
- [ ] Criar ficha tecnica formal do MCP_FabioOS quando Claude concluir a frente.
- [ ] Definir golden questions por dominio.
- [ ] Definir formato de log de consulta RAG e chamada MCP.
- [ ] Conectar este dashboard ao futuro painel MEGATRON.
