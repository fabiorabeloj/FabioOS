---
tipo: índice
area: administração
status: ativo
criado_em: 2026-06-25
atualizado_em: 2026-06-25
tags: [estrutura, mapa, índice]
---

# INDEX.md — Mapa do FabioOS

Índice central e mapa de navegação do FabioOS.

## O que é FabioOS?

Sistema operacional pessoal baseado em [[Obsidian]], [[GitHub]], [[n8n]], [[Claude Code]], [[ChatGPT]], [[OpenRouter]] e [[MCP]].

Transforma ideias, conversas, PDFs, prints, áudios, aulas, avaliações, rotinas e projetos em **conhecimento organizado, consultável, versionável e acionável**.

---

## Estrutura do projeto

### 00_Inbox — Capturas e entrada bruta
Ponto de entrada para ideias, testes, materiais não processados.

- [[Inbox]] — log de entradas

---

### 10_Mapas — Visões gerais e dashboards
Mapas, dashboards e visões de alto nível do sistema.

- [[Dashboard]] — painel central
- [[Projetos]] — mapa de projetos ativos
- [[Conhecimento]] — mapa do repertório
- [[Sistemas]] — mapa de sistemas e integrações
- [[Vida]] — visão geral de vida pessoal e contexto

---

### 20_Projetos — Projetos ativos
Projetos em desenvolvimento, com status, objetivos e próximas ações.

**Educação:**
- [[Escola]] — materiais e organização escolar

**Automações:**
- [[Automacao_01_Conhecimento_Obsidian]] — integração Obsidian + n8n + GitHub

**Negócios e trading:**
- [[Trader]] — sistema de trading e análise de mercado
- [[Atendimento_Pietra]] — gestão de atendimento

**Produto:**
- [[PRIMUS]] — plataforma PRIMUS
- [[IA]] — projetos de IA e LLM

**Administração:**
- [[FabioOS]] — desenvolvimento do próprio FabioOS

---

### 30_Conhecimento — Repertório conceitual
Base de conhecimento reutilizável, notas conceituais e aprendizados.

**Conceitos e tecnologia:**
- [[IA]] — inteligência artificial e LLMs
- [[Automacao]] — princípios de automação e workflows
- [[Tecnologia]] — conceitos técnicos gerais
  - [[Memoria]] — arquitetura de memória
  - [[Persistencia]] — persistência de dados
  - [[Continuidade]] — continuidade de serviço

**Humano e aprendizado:**
- [[Filosofia]] — reflexões filosóficas
- [[Geografia]] — conhecimento geográfico
- [[RPG]] — design de jogos e narrativa

---

### 40_Decisoes — Registro de decisões
Decisões importantes, aprendizados e changelog do sistema.

- [[Decisoes]] — decisões arquiteturais e de produto
- [[Changelog]] — histórico de mudanças
- [[Aprendizado]] — lições aprendidas

---

### 50_Fontes — Referências externas
Fontes, referências, materiais externos e citações.

- [[Livros]] — referências de livros
- [[Artigos]] — referências de artigos
- [[Links]] — links relevantes
- [[PDF]] — coleção de PDFs

---

### 60_Sistemas — Documentação técnica e integrações
Documentação, scripts, integrações e automações.

**Ferramentas principais:**
- [[Obsidian]] — vault e plugins
- [[GitHub]] — versionamento e controle
- [[n8n]] — automações e workflows
- [[Claude_Code]] — CLI do Claude
- [[OpenRouter]] — roteamento de LLMs
- [[MCP]] — Model Context Protocol

**Agentes e processadores:**
- [[Arquivista_FabioOS]] — agente de arquivamento
- [[Hermes_Agent]] — agente de comunicação
- [[Prompt_Processador_Conhecimento]] — processador de conhecimento

**Especiais:**
- [[OpenClaw]] — cliente de chat integrado
- `integracao-n8n-github.md` — documentação técnica
- `integracao-n8n-github-obsidian.md` — documentação técnica

---

### 90_Arquivo — Materiais arquivados
Materiais antigos, descontinuados ou fora do escopo atual.

---

## Sistemas centrais (interconexões)

### Fluxo de conhecimento
Inbox → Processamento (n8n) → 30_Conhecimento → 10_Mapas → 20_Projetos

### Ciclo de versionamento
Local (Obsidian) → GitHub (backup + histórico) → Automações (n8n) → Consultas (Claude)

### Integrações principais
- **Obsidian + GitHub**: Sincronização automática via [[integracao-n8n-github-obsidian]]
- **n8n + GitHub**: Automações acionadas por eventos de repositório
- **Claude + FabioOS**: Leitura e escrita estruturada no vault

---

## Padrão de metadados (Frontmatter YAML)

Toda nota estrutural segue este modelo:

```yaml
---
tipo: [índice|conceito|projeto|fonte|decisão|automação|sistema]
area: [administração|educação|tecnologia|negócios|pessoal]
projeto: [nome do projeto ou null]
status: [ativo|arquivado|em_pausa|planejamento]
tags: [tag1, tag2, tag3]
criado_em: YYYY-MM-DD
atualizado_em: YYYY-MM-DD
---
```

**Tipos de nota:**
- `índice` — mapas e visões gerais
- `conceito` — conhecimento reutilizável
- `projeto` — projetos em desenvolvimento
- `fonte` — referência externa
- `decisão` — decisão registrada
- `automação` — workflow ou script
- `sistema` — documentação técnica

**Tags padronizadas:**
- `#projeto` — projeto específico
- `#automacao` — sobre automações
- `#conceito` — conhecimento geral
- `#escola` — materiais educacionais
- `#negocio` — negócios e trading
- `#tecnico` — documentação técnica
- `#decisao` — decisão importante

---

## Convenções de nomeação

- Arquivos em `PascalCase` (ex: `Dashboard.md`, `Claude_Code.md`)
- Pastas em `XX_Nome_Descritivo` (ex: `20_Projetos`)
- Números ordenam hierarquia (00, 10, 20...)
- Sem acentos em nomes de arquivo (salvo casos já estabelecidos)
- Extensão simples `.md` (nunca `.md.md`)

---

## Próximas ações

- [ ] Completar arquivos vazios (Filosofia, Geografia, RPG, Fontes)
- [ ] Criar RAG.md, Banco_Vetorial.md, MCP.md, Grafos_de_Conhecimento.md
- [ ] Implementar frontmatter YAML em todos os arquivos estruturais
- [ ] Revisar backlinks e links internos
- [ ] Testar abertura e navegação no Obsidian
- [ ] Documentar pipeline de automação completo
- [ ] Criar template padrão para novas notas

---

## Links rápidos

- **Dashboard principal:** [[Dashboard]]
- **Projetos ativos:** [[Projetos]]
- **Base de conhecimento:** [[30_Conhecimento|Conhecimento]]
- **Decisões do sistema:** [[Decisoes]]
- **Documentação técnica:** [[60_Sistemas|Sistemas]]
- **Configuração do Claude:** [[60_Sistemas/FabioOS/bootstrap/CLAUDE]]

---

**Última atualização:** 2026-06-25  
**Responsável:** Claude como arquiteto do FabioOS
