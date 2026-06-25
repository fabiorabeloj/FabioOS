---
tipo: conceito
area: tecnologia
status: ativo
tags: [conceito, tecnologia, arquitetura]
criado_em: 2026-06-25
atualizado_em: 2026-06-25
---

# Tecnologia

## O que é?

Tecnologia é o conjunto de ferramentas, métodos, sistemas e padrões utilizados para ampliar capacidades humanas, aumentar produtividade e criar sistemas resilientes.

## Princípios fundamentais

### 1. Continuidade acima de novidade
Sistemas que duram são mais valiosos que inovações descartáveis. Priorizar estabilidade e manutenibilidade.

### 2. Simplicidade operável
Escolher a ferramenta mais simples que resolve o problema. Complexidade desnecessária aumenta custo de manutenção.

### 3. Integrabilidade
Qualquer tecnologia deve ser integrável com o resto do stack. Silos são custos ocultos.

### 4. Automatização liberta criatividade
Repetição manual é desperdício de tempo cognitivo. Automatizar para focar no estratégico.

## Conceitos-chave

### Fundamentals
- [[Memoria]] — arquitetura e padrões
- [[Persistencia]] — durabilidade de dados
- [[Continuidade]] — uptime e resiliência

### Arquitetura
- **Monolítico vs Distribuído** — trade-offs
- **Síncrono vs Assíncrono** — latência vs throughput
- **Local vs Cloud** — custo vs escalabilidade

### DevOps
- Versionamento (Git)
- CI/CD (automação)
- Monitoring e logs
- Disaster recovery

## Stack do FabioOS

### Core
- [[Obsidian]] — conhecimento e notas
- [[GitHub]] — versionamento e backup
- [[n8n]] — automações e workflows
- [[OpenRouter]] — roteamento de LLMs

### Integração
- [[Claude Code]] — automação CLI
- [[MCP]] — protocolo de contexto
- [[RAG]] — buscas semânticas
- [[Banco_Vetorial]] — storage de embeddings

### Análise
- [[Grafos_de_Conhecimento]] — relações
- Dataview — queries estruturadas
- GitHub Analytics — activity tracking

## Padrões de design recomendados

| Padrão | Uso | Exemplo |
|--------|-----|---------|
| Event-driven | Reatividade | n8n triggers |
| Observer | Sincronização | Git hooks |
| Factory | Criação dinâmica | Templates |
| Adapter | Integração | MCP servers |
| Cache | Performance | Embeddings |

## Boas práticas

1. **Versionamento tudo** — Se não está no Git, não existe
2. **Logging estruturado** — Rastreabilidade de problemas
3. **Testes automatizados** — Confiança nas mudanças
4. **Documentação inline** — Código é comentado
5. **Backups redundantes** — Múltiplas cópias
6. **Monitoramento ativo** — Alertas para anomalias

## Próximas ações

- [ ] Expandir seção de Arquitetura
- [ ] Documentar padrões específicos do FabioOS
- [ ] Criar guias de setup por sistema
- [ ] Registrar decisões técnicas
- [ ] Medir performance e uptime

## Relações

- → [[20_Projetos|Projetos]] — usam tecnologia
- → [[60_Sistemas|Sistemas]] — documentação técnica
- → [[40_Decisoes|Decisões]] — escolhas arquiteturais
- ↔ [[IA]] — amplificação com LLMs
