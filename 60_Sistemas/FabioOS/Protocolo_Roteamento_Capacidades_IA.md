---
tipo: protocolo
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, skills, agentes, subagentes, roteamento, megatron, codex, claude]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Protocolo de Roteamento de Capacidades de IA

## Funcao

Garantir que Claude, Codex, MEGATRON e futuros agentes usem as capacidades ja
instaladas no FabioOS antes de improvisar fluxos manuais.

Este protocolo responde a uma falha operacional observada: o sistema ja possui
skills, comandos, agentes, subagentes, MCPs, RAG e grafo, mas eles ainda nao
estavam sendo acionados de forma sistematica.

## Regra central

```text
Antes de executar uma tarefa, verificar se ja existe skill, comando, agente,
script, MCP, RAG ou grafo adequado para ela.
```

Se existir, usar a capacidade nativa ou explicar por que ela nao serve naquele
caso. Se nao existir, registrar a lacuna para evolucao do FabioOS.

Antes de escolher uma IA, modelo ou ferramenta externa, consultar tambem:

```text
90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/IA/Modelos_e_IAs/Matriz_de_Aptidao_das_IAs_FabioOS.md
```

Essa matriz define vocacao, limites, risco, teste e criterio de permanencia. Nenhum modelo deve ser acionado apenas por preferencia ou curiosidade.

Antes de criar, alterar ou consolidar conhecimento no vault, consultar tambem:

```text
index.md
log.md
60_Sistemas/Wiki/Schema_Wiki_FabioOS.md
```

Esses arquivos definem a LLM Wiki operacional e evitam duplicacao, notas soltas e respostas que morrem no chat.

## Ordem de roteamento

0. **Matriz de aptidao**: quando houver escolha entre IAs, modelos, agentes,
   plataformas ou ferramentas.
0.1. **LLM Wiki**: quando a tarefa criar, alterar, consultar ou consolidar
   conhecimento persistente.
1. **Comando/skill especifica**: quando o pedido coincide com um comando ja
   migrado (`/check-secrets`, `/source-to-wiki`, `/criar-prova`, etc.).
2. **Agente especializado**: quando a tarefa exige papel continuo ou julgamento
   de dominio (`vault-architect`, `wiki-curator`, `security-reviewer`,
   `school-assistant`).
3. **Script local do sistema**: quando ja existe implementacao versionada
   (`RAG`, `Grafo`, agentes MEGATRON minimos).
4. **MCP ou conector**: quando a tarefa precisa operar ferramenta externa
   controlada (`n8n`, `Playwright`, `Gmail`, `Drive`, `Obsidian`, etc.).
5. **RAG/Grafo**: quando a tarefa depende de memoria semantica ou relacao entre
   entidades.
6. **Execucao manual pelo agente principal**: somente quando nenhuma camada
   anterior resolve com seguranca.

## Matriz de roteamento

| Pedido do usuario | Capacidade prioritaria | Caminho/configuracao |
|---|---|---|
| Commit, revisao antes de commit, push | `security-reviewer`, `/check-secrets`, `/safe-commit` | `.claude/agents/security-reviewer.md`, `.agents/skills/source-command-check-secrets/` |
| Organizar vault, revisar estrutura, links, frontmatter | `vault-architect` | `.claude/agents/vault-architect.md`, `.codex/agents/vault-architect.toml` |
| Transformar fonte em wiki | `wiki-curator`, `/source-to-wiki`, `/check-source-quality` | `.claude/agents/wiki-curator.md`, `.agents/skills/source-command-source-to-wiki/` |
| Arquivar URL/PDF/DOC | `/ingest-url`, `/ingest-pdf`, `/ingest-doc`, `/archive-source` | `.claude/commands/`, `.agents/skills/` |
| Criar prova, revisao, gabarito ou comunicado | `school-assistant`, `/criar-prova`, `/criar-revisao`, `/criar-gabarito`, `/criar-comunicado` | `.claude/agents/school-assistant.md`, `.agents/skills/` |
| Consultar conhecimento do vault | RAG local | `60_Sistemas/RAG/scripts/query_rag.py` |
| Entender relacoes entre sistemas/notas | Grafo local | `60_Sistemas/Grafo/scripts/query_graph.py` |
| Planejar arquitetura ou fase | Modelo Formal + Plano Mestre + `vault-architect` | `00_Arquitetura/`, `60_Sistemas/FabioOS/` |
| Testar automacao n8n | n8n docs/MCP + workflow documentado | `60_Sistemas/n8n/`, `mcp__n8n_docs` |
| Design/prototipo HTML | `huashu-design`, `taste-skill`, plugins UI/UX | `.claude/skills/`, `60_Sistemas/Skills/Inventario_Skills.md` |
| Tarefa paralela independente | subagente Codex/Claude, se disponivel | `.codex/agents/`, `.claude/agents/` |

## Inventario operacional atual

### Skills migradas para Codex

Local:

```text
.agents/skills/
```

Inclui:

- `source-command-archive-source`
- `source-command-check-secrets`
- `source-command-check-source-quality`
- `source-command-criar-comunicado`
- `source-command-criar-gabarito`
- `source-command-criar-prova`
- `source-command-criar-revisao`
- `source-command-ingest-doc`
- `source-command-ingest-pdf`
- `source-command-ingest-url`
- `source-command-normalize-source`
- `source-command-safe-commit`
- `source-command-session-changelog`
- `source-command-source-to-wiki`
- `source-command-update-index`

### Comandos Claude

Local:

```text
.claude/commands/
```

Os comandos Claude espelham as skills migradas e devem ser usados por Claude
Code quando a intencao do usuario bater com o comando.

### Agentes Claude/Codex

Locais:

```text
.claude/agents/
.codex/agents/
```

Agentes ativos:

- `vault-architect`
- `wiki-curator`
- `security-reviewer`
- `school-assistant`

### Agentes MEGATRON especificados

Local:

```text
60_Sistemas/MEGATRON/agentes/
```

Agentes:

- SafeCommit
- Arquivista
- Inbox
- RAG
- Dashboard

Estado oficial: especificado. Nao promover para piloto sem revisao humana e
relatorio de execucao.

## Como agir em cada sessao

No inicio de uma tarefa relevante, o agente deve responder internamente:

1. Qual e o tipo da tarefa?
2. Existe skill/comando/agente/script/MCP para isso?
3. A capacidade existente pode agir com seguranca?
4. Precisa de aprovacao humana antes de escrever, enviar, apagar, commitar ou
   fazer push?
5. A acao toca uma frente ativa registrada em
   `60_Sistemas/FabioOS/Registro_Frentes_Ativas.md`?

## Regra para subagentes

Subagentes devem ser usados quando:

- a tarefa puder ser separada em escopo claro;
- o escopo nao colidir com outra frente ativa;
- houver ganho real de paralelismo ou especializacao;
- o agente principal puder revisar o resultado.

Subagentes nao devem ser usados para:

- tarefas pequenas que o agente principal resolve melhor;
- trabalho em arquivos compartilhados sem lock;
- operacoes destrutivas;
- push, envio externo ou acoes irreversiveis.

## Lacuna observada em 2026-06-27

Na sessao Codex, a ferramenta de spawn de subagentes apareceu disponivel, mas
falhou ao tentar iniciar `vault-architect` por erro de resolucao de modelo.

Registro:

```text
spawn_agent could not resolve the child model for service tier validation
```

Proxima acao: testar subagentes em sessao limpa ou revisar configuracao do
ambiente Codex antes de depender deles em trabalho critico.

## Criterio de sucesso

Este protocolo estara funcionando quando:

- commits usarem `security-reviewer` ou `/check-secrets`;
- tarefas escolares acionarem `school-assistant` ou comandos escolares;
- fontes passarem por ingestao/curadoria em vez de colagem solta;
- arquitetura chamar `vault-architect`;
- conhecimento consultar RAG/Grafo antes de resposta solta;
- lacunas virem novas specs, skills ou agentes em vez de remendos invisiveis.

## Relacoes

- [[CLAUDE]]
- [[60_Sistemas/Claude_Code/Claude_Project_Config]]
- [[60_Sistemas/Claude_Code/Workstation_FabioOS]]
- [[60_Sistemas/Skills/Inventario_Skills]]
- [[60_Sistemas/MCP/Inventario_MCP]]
- [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Repertorio/IA/Modelos_e_IAs/Matriz_de_Aptidao_das_IAs_FabioOS]]
- [[60_Sistemas/MEGATRON/agentes/README_Agentes]]
- [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]]

## Proximas acoes

- [ ] Testar subagentes Codex em sessao limpa.
- [ ] Criar comando/skill `route-capability` se o roteamento manual virar repetitivo.
- [ ] Atualizar specs MEGATRON quando algum agente sair de `especificado`.
- [ ] Testar `taste-skill` e `huashu-design` em tarefa real de interface.
