---
tipo: wiki
area: sistemas
projeto: FabioOS
status: pendente
camada: camada-1
tags: [hermes, agente, autônomo, ia, opcional, camada-1]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Hermes Agent

## Função no FabioOS

[DECISÃO] O Hermes Agent é uma **camada opcional de agência autônoma** no FabioOS — entra apenas se existir uma função específica que Claude Code + n8n + OpenClaw não consigam resolver melhor. Não deve ser ativado por impulso.

## O que essa ferramenta faz

[FATO] Agente de IA com capacidade de execução autônoma prolongada: memória própria, subagentes, tarefas agendadas e operação sem supervisão humana contínua. Detalhes de implementação: referenciado no Plano Mestre, sem especificação técnica definida ainda.

Funções possíveis no FabioOS:

- Executar tarefas agendadas sem intervenção manual
- Manter memória própria de contexto entre sessões longas
- Despachar subagentes para tarefas paralelas
- Monitorar condições e acionar ações automaticamente

[FATO] Status atual: **não implantado**. Apenas referenciado como camada opcional no Plano Mestre.

## O que essa ferramenta não deve fazer

- Substituir o FabioOS como sistema central (Obsidian + GitHub + Claude Code)
- Ser ativado sem critério claro de entrada — "é legal ter" não é motivo suficiente
- Operar com acesso irrestrito ao vault ou sistemas externos
- Tomar decisões financeiras, pedagógicas ou pessoais de forma autônoma

## Critério de entrada

[DECISÃO] O Hermes Agent só deve ser integrado ao FabioOS quando houver uma função específica que:

1. Não possa ser resolvida por Claude Code + n8n + OpenClaw
2. Exija autonomia real (não apenas automação previsível)
3. Tenha escopo bem definido e reversível

## Relação com outras ferramentas

| Ferramenta | Relação |
|---|---|
| [[wiki/sistemas/claude-code]] | Claude Code é o operador principal — Hermes é complemento opcional |
| [[wiki/sistemas/n8n]] | n8n resolve automações previsíveis — Hermes cobre casos imprevisíveis |
| [[wiki/sistemas/openclaw]] | OpenClaw é o gateway externo — Hermes pode ser agente interno autônomo |

## Uso atual

- [ ] Nenhum — **opcional, aguardando critério de entrada** (Fase 17)

## Uso futuro

- [ ] Monitoramento contínuo de condições (ex: alertas de mercado para sistema Trader)
- [ ] Execução de rotinas agendadas sem interação humana
- [ ] Subagente especializado para domínio específico

## Riscos e cuidados

- **Autonomia descontrolada**: agentes autônomos podem tomar ações indesejadas sem supervisão — implementar limites estritos de escopo
- **Duplicação do FabioOS**: risco de criar um segundo sistema paralelo que enfraquece o centro (Obsidian + GitHub)
- **Custo operacional**: agentes autônomos têm custo de tokens contínuo — avaliar ROI antes de ativar

## Próximas ações

- [ ] Definir caso de uso específico antes de qualquer implementação
- [ ] Avaliar na Fase 17 se ainda há necessidade não coberta pelos outros sistemas

## Links internos

- [[wiki/indices/mapa-fabios]]
- [[wiki/sistemas/claude-code]]
- [[wiki/sistemas/n8n]]
- [[wiki/sistemas/openclaw]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
