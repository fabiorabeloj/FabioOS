---
tipo: plano-operacional
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, capacidades, agentes, subagentes, cursor, hermes, mcp, rag, grafo]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
---

# Plano de Capacidades - Agentes, Cursor e Hermes

## Funcao

Reorganizar o uso das capacidades ja instaladas no FabioOS para evitar improviso, duplicacao e agentes soltos.

## Estado atual

- RAG local existe e foi usado em modo recuperacao, sem API externa.
- Grafo local existe e foi usado para localizar nos do MEGATRON.
- MCP FabioOS v0 foi configurado no Codex como servidor local read-only.
- Subagentes Claude funcionaram em rodadas anteriores; subagentes Codex falharam nesta sessao por erro de resolucao de modelo.
- Cursor esta instalado como oficina de desenvolvimento.
- Hermes esta instalado, mas ainda nao integrado nem autorizado como agente autonomo.

## Onde cada capacidade entra nas fases

| Capacidade | Fase principal | Papel correto |
|---|---:|---|
| RAG | 12 | Memoria semantica consultavel com fontes. Deve ser usado antes de responder sobre conhecimento ja documentado. |
| Grafo | 13 | Relacoes entre entidades, sistemas, agentes e decisoes. Deve ser usado para navegar dependencias. |
| MCP FabioOS | 15 | Porta padronizada para agentes consultarem RAG, Grafo e vault. v0 e read-only. |
| Subagentes | 4, 14, 15 e MEGATRON | Especializacao operacional: seguranca, vault, wiki, escola, execucao. |
| Cursor | 16.5 e 21 | Oficina de desenvolvimento para software maior: dashboards, MCPs robustos, testes e interface. |
| Hermes | 17 | Agente autonomo opcional, apenas para tarefas persistentes/agendadas que n8n + Claude + OpenClaw nao resolvam melhor. |
| OpenRouter | 14, 15, 20+ | Camada de modelos por API para sintese/geracao quando necessario. Nao e necessario para MCP v0. |

## Regra de uso

Antes de responder ou implementar, seguir esta ordem:

1. Procurar no vault por nota/protocolo existente.
2. Usar RAG para contexto semantico com fontes.
3. Usar Grafo para relacoes e dependencias.
4. Usar MCP quando disponivel como ferramenta nativa.
5. Usar skill ou subagente especializado.
6. So entao improvisar uma solucao manual.

## Cursor

Cursor nao deve virar agente autonomo. Ele deve ser usado como oficina quando houver:

- refatoracao grande;
- interface visual do MEGATRON;
- dashboard web;
- testes automatizados;
- MCP customizado mais robusto;
- scripts com arquitetura de software real.

Uso imediato recomendado:

- revisar e endurecer `60_Sistemas/MCP_FabioOS/server.py`;
- criar testes de consulta read-only;
- desenhar futuramente uma interface visual do MEGATRON.

## Hermes

Hermes so deve entrar quando houver caso de uso que exija autonomia persistente.

Casos possiveis:

- monitorar rotinas agendadas;
- vigiar filas de entrada com aprovacao humana;
- operar como agente interno acionado por OpenClaw;
- executar tarefas longas de baixa criticidade.

Limites:

- nao substituir FabioOS, Claude, n8n ou OpenClaw;
- nao acessar contas Google sem fluxo aprovado;
- nao agir em Git, e-mail, WhatsApp ou arquivos sensiveis sem permissao;
- nao guardar tokens no vault.

## Subagentes

Uso desejado:

| Subagente | Quando usar |
|---|---|
| `vault-architect` | Reorganizar estrutura, fases, mapas e coerencia do vault. |
| `wiki-curator` | Transformar fontes brutas em wiki. |
| `security-reviewer` | Antes de commits, push, configs e arquivos sensiveis. |
| `school-assistant` | Materiais escolares. |
| `worker` | Implementacao de arquivo/conjunto com escopo fechado. |
| `explorer` | Perguntas read-only especificas sobre o codigo/vault. |

Achado operacional: nesta sessao, o spawn de subagente Codex falhou com erro de resolucao de modelo. Conduta: registrar o diagnostico e retestar em nova sessao apos reload do Codex/MCP.

## MCP FabioOS

Configurado localmente no Codex em `C:\Users\user\.codex\config.toml`:

- servidor: `fabioos`;
- comando: `60_Sistemas\RAG\.venv\Scripts\python.exe`;
- script: `60_Sistemas\MCP_FabioOS\server.py`;
- modo: read-only;
- sem token OpenRouter.

Ferramentas esperadas apos reload:

- `consultar_rag`;
- `consultar_grafo`;
- `buscar_nota`;
- `consultar_wiki`;
- `listar_projetos`.

## OpenRouter

Nao e necessario para configurar ou usar o MCP FabioOS v0.

Quando for usado:

- a chave deve ficar em variavel local, arquivo gitignored ou secret;
- nunca colar token no chat;
- preferir roteamento por tarefa: modelo barato para triagem, modelo forte para sintese dificil.

## Proxima decisao

Prioridade recomendada:

1. Reiniciar/recarregar Codex para o MCP FabioOS aparecer como ferramenta nativa.
2. Retestar `fabioos.consultar_rag` e `fabioos.consultar_grafo` pela interface MCP.
3. Retestar subagentes Codex.
4. Se subagentes continuarem falhando, registrar bug operacional e usar Claude como executor de subagentes ate correção.
5. So depois avaliar Hermes como agente persistente.
