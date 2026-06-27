---
tipo: wiki
area: wiki
projeto: FabioOS
status: ativo
tags: [índice, mapa, navegação, visão-geral, sistemas]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Mapa do FabioOS — Visão Geral Navegável

> Ponto de entrada único. Cada sistema linkado tem sua própria página wiki com função, contexto e próximas ações.

## Documento de referência mestre

**[[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]** — arquitetura completa, papel de cada ferramenta, fases 0–23 e regra estratégica de decisão. Leitura obrigatória no início de sessão.

**[[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]** — modelo formal do FabioOS/MEGATRON: ontologia, epistemologia, domínios, memória, agentes, governança, autoconstrução e implementação.

**[[60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente]]** — regras para Codex, Claude, MEGATRON e futuros agentes trabalharem em paralelo sem conflito.

**Fase atual:** 11 — OpenClaw (arquitetura + workflows criados, setup Evolution API pendente)
**Próxima fase:** 12 — RAG (recuperação inteligente de conhecimento)

---

## Camada 1 — Interface e Operação

O que o usuário vê e toca diariamente.

| Sistema | Função | Status | Wiki |
|---|---|---|---|
| **Obsidian** | Vault pessoal, interface de notas e grafos | ativo | [[wiki/sistemas/obsidian]] |
| **Claude Code** | Agente principal de execução e automação | ativo | [[wiki/sistemas/claude-code]] |
| **n8n** | Orquestrador de automações (localhost:5678) | ativo | [[wiki/sistemas/n8n]] |
| **GitHub** | Versionamento e backup do vault | ativo | [[wiki/sistemas/github]] |
| **ChatGPT** | Consultor estratégico e planejador | manual | [[wiki/sistemas/chatgpt]] |
| **OpenRouter** | Roteamento de IAs via API unificada | pendente | [[wiki/sistemas/openrouter]] |
| **OpenClaw** | Gateway conversacional externo (WhatsApp/Telegram) | pendente | [[wiki/sistemas/openclaw]] |
| **Hermes Agent** | Agência autônoma opcional | opcional | [[wiki/sistemas/hermes-agent]] |
| **Manus** | Executor externo de pesquisa e tarefas longas | pendente | [[wiki/sistemas/manus]] |
| **Cursor** | Oficina de desenvolvimento de software | pendente | [[wiki/sistemas/cursor]] |

---

## Camada 2 — Extensões do Agente (Skills e Plugins)

O que aumenta as capacidades do Claude Code.

**[[60_Sistemas/MEGATRON/agentes/README_Agentes]]** — especificação formal dos primeiros agentes funcionais do MEGATRON: SafeCommit, Arquivista, Inbox, RAG e Dashboard.

| Sistema | Tipo | Função | Wiki |
|---|---|---|---|
| **GSD Core** | Plugin formal | Meta-prompting, planejamento spec-driven, 70+ skills | [[wiki/sistemas/gsd-core]] |
| **Claude Mem** | Plugin formal | Memória persistente entre sessões | [[wiki/sistemas/claude-mem]] |
| **Superpowers** | Plugin formal | TDD, debugging sistemático, 13 skills de dev | [[wiki/sistemas/superpowers]] |
| **Huashu Design** | Skill SKILL.md | Protótipos HTML de alta fidelidade | [[wiki/sistemas/huashu-design]] |
| **Taste Skill** | Skill SKILL.md | Análise de design e extração de tokens visuais | [[wiki/sistemas/taste-skill]] |

---

## Camada 3 — Protocolo de Extensão (MCP)

Como o Claude se conecta ao mundo externo.

> Conceito central: [[wiki/conceitos/mcp]]

| MCP | Transporte | Sistema conectado | Wiki |
|---|---|---|---|
| `filesystem` | stdio | Arquivos do vault e home | — |
| `context7` | stdio | Documentação de bibliotecas | — |
| `github` | stdio | Repositório FabioOS no GitHub | — |
| `playwright-mcp` | stdio | Controle de browser em tempo real | [[wiki/sistemas/playwright-mcp]] |
| `n8n-docs` | stdio | Documentação dos nós do n8n | [[wiki/sistemas/n8n-mcp]] |
| `obsidian` | HTTP | Leitura avançada do vault Obsidian | — |
| `n8n-mcp` | HTTP | Execução de workflows n8n | — |
| `plugin:claude-mem` | interno | Busca de memórias de sessão | [[wiki/sistemas/claude-mem]] |

---

## Camada 4 — Infraestrutura de Conhecimento (LLM-Wiki)

Como o conhecimento é capturado, organizado e recuperado.

```
Captura bruta       Análise + Síntese     Conhecimento organizado
sources/            wiki-curator           wiki/
  repositorios/  →  (agente)           →  sistemas/
  artigos/                                 conceitos/
  pdfs/                                    entidades/
  aulas/                                   projetos/
                                           indices/  ← você está aqui
```

**Regras do fluxo:** [[schema/fluxo-wiki]]
**Critérios de qualidade:** [[schema/qualidade-wiki]]
**Validação RAG:** [[60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG]]
**Roteiro RAG:** [[60_Sistemas/FabioOS/Roteiro_Execucao_Fase12_RAG]]

---

## Camada 5 — Sistemas Operacionais do FabioOS

Projetos e domínios específicos em operação ou desenvolvimento.

| Sistema | Status | Descrição | Wiki |
|---|---|---|---|
| **Escola** | ativo | GEO e FIL, 6º ao 9º ano — provas, revisões, gabaritos, comunicados | [[wiki/projetos/escola]] |
| **Pietra** | ativo | Atendimento pedagógico — 11 categorias, classificação + respostas-modelo | [[wiki/projetos/pietra]] |
| **Trader** | reservado | Análise técnica e dados de mercado (sem execução de ordens) | — |
| **PRIMUS** | a definir | Sistema narrativo persistente | — |

**MCP futuro para Trader:** [[wiki/sistemas/tradingview-mcp]]

---

## Camada 6 — Criação de Extensões Customizadas

Como criar novos MCPs e ferramentas para o FabioOS.

| Recurso | Uso | Wiki |
|---|---|---|
| **FastMCP** | Criar MCPs customizados em Python | [[wiki/sistemas/fastmcp]] |
| **mcp/servers** | Referência de implementação TypeScript | *(a criar)* |

**Candidatos prioritários para MCPs customizados:**
1. MCP de busca no vault (fontes + wiki)
2. MCP do sistema Trader (dados, alertas, histórico)
3. MCP n8n customizado (disparar workflows com parâmetros estruturados)

---

## Índice de páginas wiki existentes

### sistemas/ — Camada 1 (concluída na Fase 7)
- [[wiki/sistemas/obsidian]] — Obsidian (vault central, território do FabioOS)
- [[wiki/sistemas/claude-code]] — Claude Code (operador técnico principal)
- [[wiki/sistemas/n8n]] — n8n (automação, Docker, porta 5678)
- [[wiki/sistemas/github]] — GitHub (versionamento e backup)
- [[wiki/sistemas/chatgpt]] — ChatGPT (consultor estratégico)
- [[wiki/sistemas/openrouter]] — OpenRouter (roteamento de IAs via API)
- [[wiki/sistemas/openclaw]] — OpenClaw (gateway conversacional externo)
- [[wiki/sistemas/hermes-agent]] — Hermes Agent (agência autônoma opcional)
- [[wiki/sistemas/manus]] — Manus (executor externo de pesquisa)
- [[wiki/sistemas/cursor]] — Cursor (oficina de desenvolvimento de software)

### sistemas/ — Camada 2 e 3
- [[wiki/sistemas/gsd-core]] — GSD Core (meta-prompting, spec-driven)
- [[wiki/sistemas/claude-mem]] — Claude Mem (memória persistente)
- [[wiki/sistemas/superpowers]] — Superpowers (skills de desenvolvimento)
- [[wiki/sistemas/playwright-mcp]] — Playwright MCP (controle de browser)
- [[wiki/sistemas/n8n-mcp]] — n8n MCP (documentação de nós)
- [[wiki/sistemas/fastmcp]] — FastMCP (framework para criar MCPs)
- [[wiki/sistemas/taste-skill]] — Taste Skill (análise de design)
- [[wiki/sistemas/huashu-design]] — Huashu Design (protótipos HTML)
- [[wiki/sistemas/tradingview-mcp]] — TradingView MCP (dados de mercado, reservado)

### conceitos/
- [[wiki/conceitos/mcp]] — MCP — Model Context Protocol

### projetos/
- [[wiki/projetos/escola]] — Sistema Escola (GEO e FIL, 6º ao 9º ano)
- [[wiki/projetos/pietra]] — Sistema Pietra (atendimento inteligente, 11 categorias)

### índices/
- [[wiki/indices/mapa-fabios]] — este arquivo

### documentos de sistema
- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]] — modelo formal do FabioOS/MEGATRON
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]] — arquitetura completa, fases 0–23
- [[60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS]] — fluxo operacional, rotinas e convenções de nome
- [[60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente]] — coordenação entre Codex, Claude, MEGATRON e futuros agentes
- [[60_Sistemas/FabioOS/Matriz_Frentes_Paralelas]] — divisão segura de frentes de trabalho multiagente
- [[60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG]] — critérios de teste para a memória semântica
- [[60_Sistemas/FabioOS/Roteiro_Execucao_Fase12_RAG]] — sequência operacional para executar e validar a Fase 12

---

## Próximas páginas a criar

**Fase 8.5 — comandos e agente escola:**
- [ ] Implementar `/criar-prova` e `/criar-revisao` em `.claude/commands/`
- [ ] Expandir agente `school-assistant`
- [ ] Criar cronograma bimestral GEO e FIL 2026

**Sistemas pendentes:**
- [ ] `wiki/projetos/pietra.md` — sistema Pietra (Fase 9)
- [ ] `wiki/projetos/trader.md` — sistema Trader (reservado)

**Conceitos pendentes:**
- [ ] `wiki/conceitos/llm-wiki.md` — conceito e arquitetura do LLM-Wiki
- [ ] `wiki/conceitos/rag.md` — RAG e banco vetorial no FabioOS

**Extensões de sistema:**
- [ ] `wiki/sistemas/mcp-servers.md` — referência oficial de implementação
- [ ] `wiki/sistemas/awesome-claude-code.md` — catálogo de padrões
