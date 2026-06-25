---
tipo: mapa
area: tecnologia
tags: [sistemas, infraestrutura, automação, integração]
criado_em: 2026-06-25
---

# Mapa de Sistemas — FabioOS

**Centro:** [[FabioOS]] como orquestrador de tecnologia

---

## Arquitetura de 4 camadas

### 🧠 Camada 1: Memória
**O que armazena**

- [[Obsidian]] — Notas e conhecimento
- [[GitHub]] — Código e versionamento
- [[Supabase]] — Dados estruturados
- [[Banco Vetorial]] — Embeddings para IA

**Responsabilidade:**
- Persistência de informação
- Segurança e backup
- Acessibilidade

### 🔄 Camada 2: Processamento
**O que transforma**

- [[Inteligência Artificial]] — Pensamento
- [[Claude]] — LLM principal
- [[Claude Code]] — Execução de scripts
- [[OpenRouter]] — Roteamento de modelos
- [[RAG]] — Augmentação de contexto

**Responsabilidade:**
- Análise inteligente
- Geração de conteúdo
- Tomada de decisão assistida

### ⚙️ Camada 3: Automação
**O que executa**

- [[n8n]] — Orquestrador de workflows
- [[OpenClaw]] — Interface de chat operacional
- [[Webhooks]] — Triggers e integrações
- [[APIs]] — Comunicação entre sistemas

**Responsabilidade:**
- Executar ações repetitivas
- Conectar sistemas
- Reduzir carga manual

### 🛠️ Camada 4: Infraestrutura
**O que suporta**

- [[GitHub]] — Versionamento
- [[PowerShell]] — Automação local
- [[WSL]] — Linux no Windows
- [[Docker]] — Containerização
- [[Git]] — Controle de versão

**Responsabilidade:**
- Deploy e manutenção
- Escalabilidade
- Disponibilidade

---

## Fluxos principais

### Fluxo 1: Captura → Armazenamento
```
Ideia (manual)
    ↓
[[Obsidian]] (escreve)
    ↓
[[GitHub]] (backup)
    ↓
[[Obsidian Git]] (sincroniza)
```

### Fluxo 2: Processamento com IA
```
Pergunta
    ↓
[[OpenClaw]] (interface)
    ↓
[[Claude]] (processa)
    ↓
[[RAG]] (busca contexto)
    ↓
[[Obsidian]] (armazena resultado)
```

### Fluxo 3: Automação com n8n
```
Trigger (evento)
    ↓
[[n8n]] (detecta)
    ↓
[[Processamento]] (lógica)
    ↓
[[Ação]] (executa)
    ↓
[[Obsidian]] (registra)
```

---

## Integrações críticas

| Sistema | Função | Conecta a |
|---------|--------|-----------|
| [[Obsidian]] | Memória | GitHub, n8n, IA |
| [[GitHub]] | Versionamento | Obsidian, Deploy |
| [[Claude]] | Inteligência | OpenRouter, RAG |
| [[n8n]] | Automação | Obsidian, APIs |
| [[OpenClaw]] | Interface | Claude, Obsidian |
| [[RAG]] | Contexto | Claude, Banco Vetorial |

---

## Para cada projeto

### Escola
- [[Obsidian]] — Materiais
- [[n8n]] — Email automation
- [[OpenClaw]] — Chatbot docente

### TraderOS
- [[Obsidian]] — Trade journal
- [[APIs]] — BingX integration
- [[n8n]] — Alertas automáticos

### IA & Programação
- [[Claude Code]] — Desenvolvimento
- [[GitHub]] — Repositórios
- [[n8n]] — CI/CD workflows

---

## Próximos passos

- [ ] Documentar cada sistema em detalhe
- [ ] Mapear webhooks específicos
- [ ] Criar templates de workflows
- [ ] Testar integrações

---

**Status:** 🟡 Em desenvolvimento
