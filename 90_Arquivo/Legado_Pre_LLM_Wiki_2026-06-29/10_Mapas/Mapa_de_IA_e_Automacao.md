---
tipo: mapa
area: tecnologia
tags: [IA, automação, agentes, inteligência]
criado_em: 2026-06-25
---

# Mapa de IA e Automação

**Centro:** [[Inteligência Artificial]] como multiplicador de capacidade

---

## Stack de IA

### 🧠 Modelos de Linguagem

- [[Claude]] — Pensamento profundo, análise, escrita
- [[ChatGPT]] — Brainstorming, prototipagem
- [[OpenRouter]] — Roteamento entre modelos
- [[Agentes de IA]] — Autonomia operacional

**Usos:**
- Geração de conteúdo (provas, revisões)
- Análise de dados (geografia, padrões)
- Automação de escrita
- Suporte a decisões

### 🔍 Recuperação de Contexto

- [[RAG]] — Retrieval-Augmented Generation
- [[Banco Vetorial]] — Storage de embeddings
- [[Embeddings]] — Vetores de significado
- [[Grafos de Conhecimento]] — Relações semânticas

**Usos:**
- Busca inteligente em Obsidian
- Chatbots com memória
- Análise de padrões

### 🛠️ Infraestrutura

- [[APIs]] — Integração com serviços
- [[MCP]] — Model Context Protocol
- [[Webhooks]] — Triggers automáticos
- [[Token de API]] — Autenticação

---

## Agentes Operacionais

### Agente 1: Processador de Conhecimento
**Responsável por:** Transformar entrada bruta em notas estruturadas

- Input: Áudio, PDF, print, conversa
- Processamento: [[Claude]] + [[RAG]]
- Output: Nota MD estruturada em [[Obsidian]]
- Trigger: Manual ou automático

**Implementação**: [[OpenClaw]] + [[n8n]]

### Agente 2: Gerador de Materiais Pedagógicos
**Responsável por:** Criar provas, revisões, gabaritos

- Input: Tópicos, objetivos, nível
- Processamento: [[Claude]] com prompt padrão
- Output: Documento pronto para usar
- Trigger: Demanda manual

**Implementação**: [[Claude Code]] + [[Obsidian]]

### Agente 3: Atendimento Inteligente
**Responsável por:** Triagem e resposta automática de mensagens

- Input: Mensagem WhatsApp/email
- Processamento: [[Claude]] + categorização
- Output: Resposta automática ou redirecionamento
- Trigger: Webhook de mensagem

**Implementação**: [[n8n]] + [[OpenClaw]]

### Agente 4: Análise de Trader
**Responsável por:** Monitorar sinais e alertar

- Input: Dados de [[BingX]]
- Processamento: [[APIs]] + análise técnica
- Output: Sinais e alertas
- Trigger: Horário ou evento

**Implementação**: [[Claude Code]] + [[n8n]]

---

## Fluxo de Integração

```
Entrada (manual, API, webhook)
    ↓
Processamento ([[Claude]] + contexto)
    ↓
Ação (escrever, enviar, armazenar)
    ↓
Armazenamento ([[Obsidian]] ou destino)
    ↓
Log e feedback
```

---

## Usos Específicos por Projeto

### Escola
- [[Claude]]: Geração de provas, revisões, gabaritos
- [[OpenClaw]]: Chatbot de atendimento
- [[n8n]]: Automação de emails
- [[RAG]]: Busca em banco de provas antigas

### TraderOS
- [[APIs]]: Dados de mercado
- [[Claude]]: Análise de gráficos
- [[n8n]]: Monitoramento de alertas
- [[Agentes]]: Execução automática de ordens

### Desenvolvimento (Carreira)
- [[Claude Code]]: Escrita de scripts
- [[GitHub]]: Versionamento
- [[n8n]]: CI/CD automático

---

## Paradigma: Menos cliques, mais pensamento

**Objetivo:** Máquinas fazem repetitivo, você faz criativo

| Tarefa | Manual | Com IA | Ganho |
|--------|--------|--------|-------|
| Prova | 2h | 20min | -90% |
| Revisão | 1h | 10min | -83% |
| Email (triagem) | 1h | 0 | -100% |
| Análise gráfico | 30min | 5min | -83% |

---

## Próximos Passos

### HOJE
- [ ] Criar notas separadas para:
  - [[Agente Processador de Conhecimento]]
  - [[Agente Gerador de Materiais]]
  - [[Agente Atendimento Inteligente]]
  - [[Agente Análise Trading]]

### Esta semana
- [ ] Documentar cada agente com especificações
- [ ] Criar 10 prompts padrão (Geografia, Filosofia, Trading)
- [ ] Testar Claude + Obsidian com 3 queries
- [ ] Documentar fluxo RAG completo

### Este mês
- [ ] Implementar Agente 1: Processador de Conhecimento
  - [ ] Setup n8n webhook
  - [ ] Integração com Claude API
  - [ ] Testar com 3 captures
- [ ] RAG funcionando para Obsidian
  - [ ] Instalar Chroma ou alternativa
  - [ ] Indexar 50+ notas atuais
  - [ ] Testar 5 buscas semânticas
- [ ] Dashboard básico de automações

### Próximos 2 meses
- [ ] Implementar Agente 2: Gerador de Materiais
  - [ ] Gerar 5 provas automáticas
  - [ ] Criar 10 gabaritos
  - [ ] Testar qualidade
- [ ] Implementar Agente 3: Atendimento Inteligente
  - [ ] Triagem de 100 mensagens
  - [ ] Resposta automática para 80%
- [ ] Implementar Agente 4: Análise Trading
  - [ ] Monitorar BingX
  - [ ] Enviar alertas
  - [ ] Análise de gráficos

### Próximos 3 meses
- [ ] Agentes para cada projeto (Escola, Trader, IA, PRIMUS)
- [ ] Aprendizado contínuo (feedback loop)
- [ ] Otimização automática (melhorar prompts)
- [ ] Sistema de reputação (qual agente é melhor)

---

## Prompts a criar

### Escola
- [ ] "Gerar prova de Geografia sobre [tema]"
- [ ] "Criar gabarito comentado para [prova]"
- [ ] "Resumir para revisão: [tópico]"
- [ ] "Analisar resposta do aluno"

### Trading
- [ ] "Analisar gráfico H1 de BTC"
- [ ] "Identificar padrão no gráfico"
- [ ] "Sugerir entrada com SL"
- [ ] "Revisar trade journal"

### Geral
- [ ] "Processar captura em nota estruturada"
- [ ] "Conectar nota com outras no vault"
- [ ] "Sugerir tags e links"

---

## Referências

- [[Mapa de Sistemas]]
- [[Mapa de Escola]]
- [[Mapa de TraderOS]]
- [[RAG_IMPLEMENTATION]]

---

**Status:** 🟠 Em implementação
**Prioridade:** 🔴 Crítica (multiplica capacidade)
**ROI estimado:** 10x redução de tempo operacional
