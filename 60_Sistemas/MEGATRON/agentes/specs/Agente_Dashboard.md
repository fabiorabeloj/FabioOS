---
tipo: especificacao-agente
area: 60_Sistemas
projeto: FabioOS
sistema: MEGATRON
agente: Dashboard
status: especificado
prioridade: 5
tags: [megatron, agente, dashboard, status, pendencias, observabilidade]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Agente Dashboard

## Identidade

| Campo | Valor |
|---|---|
| Nome | Dashboard |
| ID | `agent.dashboard` |
| Domínio | FabioOS |
| Estado | especificado |
| Prioridade | 5 |
| Dono humano | Fabio |
| Identidade pública | MEGATRON interno |

## Missão

Consolidar status dos agentes, tarefas, pendências, riscos, logs e próximos passos em uma visão operacional única para MEGATRON e Fabio.

## Entradas

| Entrada | Origem | Formato |
|---|---|---|
| Registro de agentes | `Registro_Agentes.md` | Markdown |
| Pendências | `10_Mapas/Painel_Pendencias_FabioOS.md` | Markdown |
| Changelogs | `50_Registros/Changelog/` | Markdown |
| Logs de agentes | `50_Registros/Agentes/` | Markdown |
| Estado Git | repositório | status textual |
| Status RAG/n8n | scripts ou notas | relatório |

## Saídas

| Saída | Destino | Formato |
|---|---|---|
| Painel textual | `10_Mapas/` ou `60_Sistemas/MEGATRON/` | Markdown |
| Alertas | MEGATRON / Fabio | lista priorizada |
| Próximas ações | Painel de Pendências | checklist |
| Status de agentes | Registro_Agentes | tabela atualizada |
| Relatório de lacunas | MEGATRON | Markdown |

## Ferramentas

- Leitura de Markdown.
- `rg` para tarefas `[ ]`, changelogs e status.
- Git status.
- Futuramente Dataview, Obsidian Canvas ou interface MEGATRON.

## Permissões

| Classe de ação | Permitida | Condição |
|---|---|---|
| Leitura | Sim | Arquivos de status e logs |
| Escrita segura | Sim | Atualizar painéis e resumos |
| Escrita sensível | Não | Encaminhar para humano |
| Alteração de pendências | Sim | Apenas adicionar ou marcar com evidência clara |
| Exclusão | Não | Nunca |
| Commit | Não | Encaminhar para SafeCommit |
| Push | Não | Fora do escopo |

## Limites

- Não executa tarefas de outros agentes; apenas consolida e recomenda.
- Não altera specs sem confirmação.
- Não apaga pendências.
- Não exibe dados sensíveis em painéis.
- Não substitui changelog; lê e resume.

## Riscos

| Risco | Impacto | Mitigação |
|---|---|---|
| Painel desatualizado | Decisão ruim | Atualizar a partir de fontes oficiais |
| Excesso de informação | Baixa utilidade | Priorizar por risco e próxima ação |
| Exposição de dados sensíveis | Risco de privacidade | Sanitizar logs e ocultar detalhes |
| Marcar tarefa indevidamente | Perda de controle | Exigir evidência de conclusão |

## Critérios de aceite

- [ ] Mostra status dos cinco agentes iniciais.
- [ ] Lista pendências críticas.
- [ ] Mostra última entrega registrada em changelog.
- [ ] Indica riscos abertos.
- [ ] Recomenda próxima ação.
- [ ] Não expõe segredos ou dados sensíveis.

## Logs

Registrar:

- fontes consultadas;
- status consolidado;
- pendências adicionadas ou marcadas;
- alertas emitidos;
- lacunas de informação.

## Relação com MEGATRON

MEGATRON usa Dashboard como painel de consciência operacional. Dashboard responde "qual é o estado do sistema?", "o que está bloqueado?", "qual agente deve agir agora?" e "qual próxima ação faz mais sentido?".

## Implementação mínima

1. Criar painel Markdown mínimo a partir do Registro_Agentes e Painel de Pendências.
2. Atualizar manualmente após cada changelog relevante.
3. Consolidar status dos cinco agentes iniciais.
4. Sugerir próxima ação em ordem de prioridade.

## Evolução futura

- Dataview no Obsidian.
- Dashboard visual em PWA MEGATRON.
- Status automático de n8n, RAG, Git e MCPs.
- Métricas por agente.
- Alertas de inbox acumulada, índice RAG desatualizado e commits pendentes.

## Relações

- [[60_Sistemas/MEGATRON/agentes/Registro_Agentes]]
- [[10_Mapas/Painel_Pendencias_FabioOS]]
- [[60_Sistemas/MEGATRON/agentes/specs/Agente_SafeCommit]]
- [[60_Sistemas/MEGATRON/agentes/specs/Agente_Inbox]]
