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

**Fase atual:** 6 — Bootstrap de contexto (em execução)
**Próxima fase:** 7 — Consolidação da Camada 1

---

## Camada 1 — Interface e Operação

O que o usuário vê e toca diariamente.

| Sistema | Função | Wiki |
|---|---|---|
| **Obsidian** | Vault pessoal, interface de notas e grafos | *(a criar)* |
| **Claude Code** | Agente principal de execução e automação | *(a criar)* |
| **n8n** | Orquestrador de automações (localhost:5678) | *(a criar)* |

---

## Camada 2 — Extensões do Agente (Skills e Plugins)

O que aumenta as capacidades do Claude Code.

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

---

## Camada 5 — Sistemas Operacionais do FabioOS

Projetos e domínios específicos em operação ou desenvolvimento.

| Sistema | Status | Descrição |
|---|---|---|
| **Escola** | Em estruturação | Materiais de aula, provas, revisões, planejamento pedagógico |
| **Pietra** | Em estruturação | Atendimento pedagógico individualizado |
| **Trader** | Reservado | Análise técnica e dados de mercado (sem execução de ordens) |
| **PRIMUS** | A definir | — |

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

### sistemas/
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

### índices/
- [[wiki/indices/mapa-fabios]] — este arquivo

---

## Próximas páginas a criar

**Alta prioridade (Camada 1):**
- [ ] `wiki/sistemas/obsidian.md` — papel do vault, estrutura, plugins
- [ ] `wiki/sistemas/claude-code.md` — configuração do agente no FabioOS
- [ ] `wiki/sistemas/n8n.md` — instância local, workflows, MCPs

**Média prioridade:**
- [ ] `wiki/sistemas/mcp-servers.md` — referência oficial de implementação
- [ ] `wiki/sistemas/awesome-claude-code.md` — catálogo de padrões
- [ ] `wiki/conceitos/llm-wiki.md` — conceito e arquitetura do LLM-Wiki
- [ ] `wiki/conceitos/rag.md` — RAG e banco vetorial no FabioOS

**Baixa prioridade (sistemas futuros):**
- [ ] `wiki/projetos/escola.md` — sistema Escola
- [ ] `wiki/projetos/trader.md` — sistema Trader
