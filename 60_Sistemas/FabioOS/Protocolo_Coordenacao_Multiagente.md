---
tipo: protocolo
area: 60_Sistemas
projeto: FabioOS
status: rascunho
tags: [fabios, multiagente, codex, claude, coordenacao, git]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Protocolo de Coordenação Multiagente

## Função

Definir como Codex, Claude e outros agentes devem trabalhar em paralelo no FabioOS sem sobrescrever alterações, misturar commits ou quebrar a rastreabilidade do vault.

## Contexto

O FabioOS passou a operar com mais de um agente atuando no mesmo repositório. Isso aumenta velocidade, mas também cria risco de colisão: dois agentes podem editar o mesmo arquivo, gerar changelogs concorrentes, alterar o mapa ao mesmo tempo ou preparar commits com escopos misturados.

Este protocolo organiza a divisão de frentes.

---

## 1. Princípio central

```text
Um agente por frente.
Um conjunto claro de arquivos por frente.
Um commit por tema.
Nenhum push sem aprovação humana.
```

## 2. Papéis recomendados

| Agente | Papel preferencial | Evitar |
|---|---|---|
| Claude | Implementação local, execução de scripts, testes e commits supervisionados | Alterar documentação estratégica enquanto outro agente escreve arquitetura |
| Codex | Arquitetura, revisão estrutural, especificações, auditoria e tarefas paralelas sem conflito | Editar arquivos que Claude está prestes a commitar |
| MEGATRON | Orquestração futura, roteamento e consolidação de status | Executar ações sensíveis sem aprovação |

## 3. Antes de iniciar uma frente

O agente deve verificar:

- `git status --short`;
- quais arquivos o outro agente declarou estar editando;
- se a tarefa exige mexer em mapa, changelog ou painel;
- se há arquivos sensíveis envolvidos;
- se a frente pode ser feita em arquivo novo.

## 4. Zonas de trabalho

### Zona livre

Pode ser usada em paralelo quando criar arquivos novos:

- novas specs em `00_Arquitetura/`;
- novos protocolos em `60_Sistemas/FabioOS/`;
- novas notas de decisão em `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Decisoes/`;
- relatórios de revisão isolados.

### Zona compartilhada

Exige coordenação antes de editar:

- `40_Wiki/_compat_wiki/indices/mapa-fabios.md`;
- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Painel_Pendencias_FabioOS.md`;
- `60_Sistemas/FabioOS/bootstrap/CLAUDE.md`;
- `60_Sistemas/FabioOS/bootstrap/AGENTS.md`;
- `.gitignore`;
- `50_Registros/Changelog/`;
- qualquer arquivo já listado em plano de commit por outro agente.

### Zona sensível

Não mexer sem autorização explícita:

- `.codex/config.toml`;
- arquivos `.env`;
- logs com dados pessoais;
- credenciais;
- dados institucionais do PietraOS;
- arquivos de runtime ignorados pelo Git.

## 5. Regra de commits

Commits devem ser temáticos.

Exemplo:

```text
docs: modelo formal e especificacao dos agentes megatron
feat: implementacao minima dos agentes megatron
feat: scripts rag da fase 12
chore: integrar codex e governanca multiagente
```

Antes de cada commit:

- rodar scan de segredos;
- listar arquivos do commit;
- mostrar mensagem proposta;
- aguardar aprovação humana;
- não fazer push.

## 6. Regra para changelog

Se dois agentes trabalham em paralelo, apenas um deve criar o changelog final da leva. O outro pode criar relatório temporário ou deixar nota de "pendente registrar changelog".

Critério:

- mudança implementada e testada: changelog;
- análise ou revisão temporária: relatório;
- proposta ainda não executada: pendência.

## 7. Regra para conflitos

Se o agente perceber que outro agente alterou arquivo durante a execução:

1. parar edições naquele arquivo;
2. reler o arquivo;
3. comparar intenção atual com alteração nova;
4. continuar apenas se a mudança for compatível;
5. se houver dúvida, pedir decisão humana.

## 7.1 Regra de lock operacional

Antes de operar artefatos compartilhados ou destrutivos, o agente deve registrar a frente em `60_Sistemas/FabioOS/Registro_Frentes_Ativas.md`.

Artefatos que exigem lock:

- banco RAG (`60_Sistemas/RAG/fabioos_db/`);
- reindexação vetorial;
- workflows n8n;
- mapa/painel/status/changelog;
- arquivos de governança;
- `.gitignore`;
- qualquer arquivo declarado por outro agente.

Regra:

```text
Se pode apagar, recriar, reindexar, mover ou commitar trabalho de outro agente, exige lock.
```

Nenhum agente deve encerrar processo de outro agente sem confirmação humana explícita.

## 8. Checklist operacional

- [ ] Li o contexto obrigatório do FabioOS.
- [ ] Rodei `git status --short`.
- [ ] Verifiquei `60_Sistemas/FabioOS/Registro_Frentes_Ativas.md` antes de mexer em artefatos compartilhados.
- [ ] Sei quais arquivos pertencem à minha frente.
- [ ] Evitei arquivos que outro agente está preparando para commit.
- [ ] Não toquei em segredos nem credenciais.
- [ ] Não apaguei arquivos.
- [ ] Não fiz push.
- [ ] Registrei lacunas e próxima ação.

## Relações

- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]
- [[60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS]]
- [[60_Sistemas/MEGATRON/agentes/README_Agentes]]
- [[60_Sistemas/MEGATRON/agentes/specs/Agente_SafeCommit]]

## Próximas ações

- [ ] Validar este protocolo após os quatro commits temáticos propostos pelo Claude.
- [ ] Decidir se este arquivo entra em commit separado de governança.
- [ ] Adicionar referência ao mapa do FabioOS após a leva atual de commits estabilizar.
