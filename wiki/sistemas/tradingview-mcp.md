---
tipo: wiki
area: wiki
projeto: FabioOS
status: reservado
fonte: [[sources/repositorios/tradingview-mcp]]
tags: [mcp, trading, mercado, dados, experimental, trader]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# TradingView MCP (Experimental)

## Função

[FATO] Servidor MCP comunitário que fornece dados de mercado em tempo real, análise técnica, screeners e backtesting ao Claude. Cobre ações, cripto, forex e futuros via TradingView.

## Contexto

[FATO] Repo `atilaahmettaner/tradingview-mcp`. **Não é oficial do TradingView Inc.** Projeto comunitário independente, atualizado em maio 2026.

[FATO] Status no FabioOS: clonado em `C:\Users\user\claude-extensions\tradingview-mcp\` apenas para estudo. Sem credenciais configuradas. Sem conexão com corretora ou exchange.

## Restrições ativas (por instrução explícita do usuário)

| Ação | Status |
|---|---|
| Configurar credenciais reais | ❌ Bloqueado |
| Conectar corretora/exchange | ❌ Bloqueado |
| Executar ordens | ❌ Bloqueado |
| Automatizar compra/venda | ❌ Bloqueado |
| Estudar documentação e estrutura | ✅ Permitido |
| Preparar configuração futura | ✅ Permitido |

[DECISÃO] Integração com o sistema Trader do FabioOS está reservada para fase futura, quando o escopo e as salvaguardas do sistema Trader forem definidas.

## Onde entra no FabioOS (futuro)

- **Sistema Trader**: análise técnica assistida por IA
- **Consulta de dados**: dados de mercado durante sessões do Claude
- **n8n**: workflows de estudo e análise de mercado (sem execução de ordens)

## Relações

- [[wiki/conceitos/mcp]]

## Próximas ações

- [ ] Estudar documentação e requisitos de autenticação do TradingView
- [ ] Definir escopo do sistema Trader antes de qualquer ativação
- [ ] Criar nota de decisão em `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Decisoes/` sobre o sistema Trader
