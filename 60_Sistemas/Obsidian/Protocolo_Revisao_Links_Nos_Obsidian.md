---
tipo: protocolo
area: 60_Sistemas
sistema: Obsidian
projeto: FabioOS
status: sprout
classe_dado: interno
criado_em: 2026-07-02
atualizado_em: 2026-07-02
tags: [obsidian, pkm, wikilinks, graph-view, llm-wiki]
---

# Protocolo de Revisao de Links e Nos no Obsidian

## Objetivo

Converter textos brutos em notas conectadas ao [[10_Dashboard/LLM_Wiki_FabioOS|LLM Wiki FabioOS]] sem criar bolinhas soltas no [[40_Wiki/_MOCs/MOC_Obsidian_FabioOS|Graph View]].

## Regra principal

Um link so deve ser criado se cumprir pelo menos uma condicao:

- aponta para um hub existente;
- aponta para uma nota existente;
- cria uma nota que sera imediatamente conectada a um MOC;
- representa um conceito com decisao, dono ou teste.

Se nao cumprir, fica como texto normal ate amadurecer.

## Frontmatter padrao

```yaml
---
tipo: nota
area: 40_Wiki
projeto: FabioOS
status: seed
classe_dado: interno
criado_em: AAAA-MM-DD
atualizado_em: AAAA-MM-DD
tags: [fabios]
---
```

## Status de Jardim Digital

| Status | Uso |
|---|---|
| `seed` | captura rapida, ideia inicial ou trecho bruto |
| `sprout` | ja tem conexoes, contexto e proximas acoes |
| `evergreen` | nota madura, densa, revisada e usada como referencia |

## Conversao de links

### Antes

```md
O Megatron precisa conectar intake, RAG, n8n, OpenClaw e Agentarium.
```

### Depois

```md
O [[10_Dashboard/MEGATRON|MEGATRON]] precisa conectar [[50_Registros/Relatorios/Inbox_Universal_v0.1_Codex_2026-07-01|Universal Intake]], [[10_Dashboard/RAG_MCP_Control_Plane|RAG/MCP]], [[60_Sistemas/n8n/README|n8n]], [[60_Sistemas/OpenClaw/OpenClaw|OpenClaw]] e [[60_Sistemas/OpenClaw/Agentarium|Agentarium]].
```

## Alias obrigatorios

| Quando aparecer | Usar |
|---|---|
| Fabio OS | `[[10_Dashboard/FabioOS|Fabio OS]]` |
| Megatron, orquestrador | `[[10_Dashboard/MEGATRON|MEGATRON]]` |
| busca semantica | `[[10_Dashboard/RAG_MCP_Control_Plane|busca semantica]]` |
| memoria operacional | `[[10_Dashboard/LLM_Wiki_FabioOS|memoria operacional]]` |
| painel de agentes | `[[60_Sistemas/OpenClaw/Agentarium|painel de agentes]]` |
| OpenClaw Companion | `[[60_Sistemas/OpenClaw/OpenClaw|OpenClaw Companion]]` |
| workflow | `[[60_Sistemas/n8n/README|workflow]]` |
| aprovacao humana | `[[50_Registros/Relatorios/Bugbot_Mesa_Despacho_Intake_v0.9.0_Cursor|aprovacao humana]]` |
| roteador de modelos | `[[60_Sistemas/MEGATRON/infra/Compute_Manager_LLM_Orchestrator|roteador de modelos]]` |

## Criterio anti-orfaos

Antes de criar um link, pergunte:

1. Existe nota destino?
2. A nota destino esta em um MOC ou dashboard?
3. O link ajuda uma decisao, fluxo ou consulta futura?
4. O conceito deve virar nota propria ou alias?
5. O mesmo conceito ja existe com outro nome?

Se a resposta 1 e 2 forem "nao", nao criar wikilink ainda.

## Processo para textos colados

1. Identificar tema central.
2. Escolher hub canônico.
3. Adicionar frontmatter com `status`.
4. Linkar apenas conceitos estruturais.
5. Usar alias para sinonimos.
6. Evitar link em toda palavra repetida.
7. Adicionar secao `Relacoes`.
8. Adicionar secao `Proxima acao` se houver execucao.
9. Se virar nota nova, conectar no MOC correspondente.

## Saida esperada

Texto revisado em Markdown, preservando a estrutura original, mas com:

- frontmatter;
- links internos;
- aliases;
- menos duplicatas;
- menos no solto;
- relacoes com hubs existentes.

## Relacoes

- [[40_Wiki/FabioOS/Gargalos_Sistemicos_FabioOS_MEGATRON]]
- [[40_Wiki/_MOCs/MOC_Obsidian_FabioOS]]
- [[10_Dashboard/LLM_Wiki_FabioOS]]
- [[10_Dashboard/RAG_MCP_Control_Plane]]
