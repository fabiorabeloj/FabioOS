---
tipo: decisao-arquitetural
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, obsidian, estrutura, llm-wiki, governanca]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Estrutura Canonica Completa do Obsidian

## Decisao

A estrutura abaixo e a arvore visual e operacional preferencial do FabioOS no Obsidian.

Ela consolida a mentalidade LLM Wiki:

```text
captura -> fonte preservada -> conhecimento processado -> sistema executavel -> registro verificavel
```

## Raiz canonica

`00_Arquitetura/` permanece como camada constitucional do FabioOS, mesmo nao aparecendo no rascunho visual inicial. Ela guarda modelo formal, principios e decisoes de arquitetura de mais alto nivel.

```text
00_Inbox/
├── Capturas/
├── Processar/
├── Ideias/
└── Triagem/

05_Raw_Sources/
├── _assets/
├── Cursos/
├── PDFs/
├── Prints/
├── Videos_Transcricoes/
├── Conversas/
├── Radar_Tecnologico/
├── EscolaOS/
├── TraderOS/
└── PRIMUS/

10_Dashboard/
├── FabioOS.md
├── LLM_Wiki_FabioOS.md
├── MEGATRON.md
├── RAG_MCP_Control_Plane.md
├── Governanca_FabioOS.md
├── Mapa_de_Conexoes_FabioOS.md
└── Projetos_Ativos.md

20_Areas/
├── EscolaOS/
├── TraderOS/
├── VidaOS/
├── FinanceOS/
├── Saude/
└── Estudos/

30_Projetos/
├── FabioOS/
├── MEGATRON/
├── OpenClaw/
├── Escola_SaaS/
├── PRIMUS/
└── TraderOS/

40_Wiki/
├── _MOCs/
├── FabioOS/
├── IA/
├── Engenharia_de_Agentes/
├── Modelos_e_IAs/
├── RAG/
├── MCP/
├── LLM_Wiki/
├── Obsidian/
├── GitHub/
├── n8n/
├── OpenClaw/
├── Python/
├── Docker_Linux/
├── Supabase/
├── Radar_Tecnologico/
├── EscolaOS/
├── TraderOS/
├── PRIMUS/
├── Filosofia/
└── Geografia/

50_Registros/
├── Decisoes/
├── ADR/
├── Changelog/
├── Auditoria/
├── Logs_Agentes/
├── Logs_RAG_MCP/
├── Reunioes/
└── Relatorios/

60_Sistemas/
├── Wiki/
├── Governanca/
├── Memoria/
├── RAG/
├── MCP/
├── Agentes/
├── Automacoes/
├── n8n/
├── OpenClaw/
├── GitHub/
├── Obsidian/
├── Seguranca/
├── Observabilidade/
└── Scripts/

70_Skills/
├── Skill_Obsidian.md
├── Skill_GitHub.md
├── Skill_n8n.md
├── Skill_RAG.md
├── Skill_MCP.md
├── Skill_EscolaOS.md
├── Skill_TraderOS.md
├── Skill_PRIMUS.md
└── Skill_Radar_Tecnologico.md

80_Specs/
├── FabioOS/
├── MEGATRON/
├── OpenClaw/
├── EscolaOS/
├── TraderOS/
├── PRIMUS/
├── RAG/
└── MCP/

90_Arquivo/
├── Antigo/
├── Superseded/
├── Projetos_Encerrados/
└── Referencias_Mortas/
```

## Regras de aplicacao

1. Arquivo novo sem classificacao entra em `00_Inbox/Processar/` ou `00_Inbox/Triagem/`.
2. Fonte bruta entra em `05_Raw_Sources/`, nunca direto em `40_Wiki/`.
3. Conhecimento ja processado entra em `40_Wiki/`.
4. Sistema, script, agente, automacao ou integracao entra em `60_Sistemas/`.
5. Decisao, ADR, changelog, auditoria, reuniao ou relatorio entra em `50_Registros/`.
6. Spec executavel entra em `80_Specs/`.
7. Material antigo, superado ou visualmente poluente entra em `90_Arquivo/`, sem apagar.

## Subpastas adicionais toleradas

Durante a transicao, algumas pastas operacionais podem existir alem da arvore preferencial quando ja possuem historico, scripts ou links relevantes.

Elas devem obedecer uma das regras:

- serem migradas em lote pequeno para a arvore preferencial;
- serem documentadas como excecao ativa;
- serem arquivadas em `90_Arquivo/` quando perderem funcao.

## Limpeza visual aplicada

Nesta rodada:

- `00_Inbox/Teste/` foi esvaziada e suas notas foram movidas para `00_Inbox/Triagem/`;
- `00_Inbox/Email_para_Processar_FabioOS.md` foi movido para `00_Inbox/Processar/`;
- `00_Inbox/Inbox.md` foi preservado como legado em `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/00_Inbox/`;
- arquivos soltos em `60_Sistemas/` foram movidos para subpastas de sistema coerentes;
- links textuais conhecidos foram atualizados para os novos caminhos.

## Criterio de aceite

- a raiz do vault deve mostrar apenas pastas canonicas e `10_Dashboard/_entrada/index.md` para uso humano;
- `00_Inbox/` deve expor as quatro gavetas de captura e triagem;
- `60_Sistemas/` nao deve conter arquivos `.md` soltos na raiz;
- nenhuma nota deve ser apagada;
- toda migracao deve passar por scan antes de commit.
