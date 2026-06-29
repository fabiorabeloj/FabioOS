---
tipo: matriz
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, megatron, dominios, permissoes, privacidade, rag, grafo]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
---

# Matriz de Dominios, Dados e Permissoes

## Funcao

Definir como o FabioOS separa dominios, dados, permissoes e politicas de uso antes de enviar qualquer conteudo para RAG, Grafo, MCP, agentes, n8n, OpenClaw, Google ou modelos externos.

Esta matriz implementa a regra do Modelo Formal:

```text
Dominios compartilham infraestrutura.
Dominios nao compartilham dados automaticamente.
```

## Dominios oficiais v0

| Dominio | Funcao | Exemplos | Memoria | Regra |
|---|---|---|---|---|
| FabioOS | Plataforma base e dominio pessoal/operacional | arquitetura, decisoes, rotinas, finances pessoais em resumo | RAG geral + Grafo geral | Compartilha infraestrutura; dados pessoais exigem cuidado |
| PietraOS / EscolaOS | Dominio institucional/docente | turmas, provas, cronogramas, comunicados, alunos, Colegio Pietra | Memoria escolar separada quando crescer | Dados de alunos e instituicao sao restritos |
| TraderOS | Dominio de trading | diario operacional, setups, prints, metricas, corretoras | RAG separado quando houver volume | Financeiro/trading e privado; nao enviar bruto a modelos externos |
| PrimusOS | Dominio narrativo e criativo | lore, campanhas, NPCs, regras, mundos | RAG/Grafo narrativo futuro | Separar canonico, rascunho e inspiracao externa |
| IAOS | Dominio tecnico de IA/automacao | MCP, RAG, agentes, Python, n8n, OpenClaw, Cursor | Pode ficar no RAG geral tecnico | Alto valor de aprendizado; baixo risco se sem credenciais |
| ProductOS | Dominio futuro de produto/negocio | usuarios, roadmap, backlog, metricas, pagamentos | So quando houver produto externo | Depende de politica de usuarios e compliance |

## Classes de dados

| Classe | Definicao | Exemplos | RAG | Grafo | Modelo externo | Requer aprovacao |
|---|---|---|---|---|---|---|
| Publico | Pode ser publicado sem dano | docs publicos, notas tecnicas sem dados pessoais | Permitido | Permitido | Permitido | Nao |
| Interno | Operacional do FabioOS, sem dado sensivel | specs, scripts, decisoes tecnicas | Permitido | Permitido | Permitido com criterio | Depende do impacto |
| Privado | Vida pessoal, finances, estrategia ou rotina | metas pessoais, diario, trading resumido | Permitido apos revisao | Permitido com resumo | Evitar bruto | Sim, se externo |
| Restrito | Dados de terceiros, alunos, escola, saude, anexos pessoais | nomes de alunos, notas, e-mails profissionais | Apenas resumo anonimizado | Apenas entidades anonimizadas | Proibido sem autorizacao explicita | Sim |
| Critico | Credenciais e dados bancarios completos | documentos oficiais sensiveis, credenciais | Proibido | Proibido | Proibido | Sempre |

## Politica por destino

| Destino | Publico | Interno | Privado | Restrito | Critico |
|---|---|---|---|---|---|
| Obsidian/Git | Sim | Sim | Sim, com cuidado | Preferir resumo/anonimizacao | Nao |
| RAG geral | Sim | Sim | Sim, se revisado | Nao bruto | Nunca |
| RAG de dominio | Sim | Sim | Sim, se escopo correto | Somente anonimizado | Nunca |
| Grafo | Sim | Sim | Sim, por entidade abstrata | Entidades anonimizadas | Nunca |
| MCP read-only | Sim | Sim | Sim, se origem permitida | Somente resumo | Nunca |
| MCP escrita/acao | Aprovacao se alterar estado | Aprovacao se alterar estado | Aprovacao obrigatoria | Aprovacao obrigatoria + log | Proibido |
| n8n/OpenClaw/WhatsApp | Sim, com log | Sim, com log | Evitar bruto | Somente com aprovacao | Proibido |
| Google/Gmail/Drive | Conforme conta e finalidade | Conforme conta e finalidade | Evitar mistura de contas | Exige autorizacao | Proibido |
| LLM externo/API | Sim | Sim, se necessario | Resumo minimo | Proibido sem autorizacao explicita | Proibido |
| Hardware/LLM local | Sim | Sim | Preferencial para privado | Preferencial para restrito anonimizado | Ainda proibido para credenciais |

## Ponte entre dominios

Toda ponte entre dominios deve declarar:

- origem;
- destino;
- finalidade;
- dados transferidos;
- permissao;
- retencao;
- auditoria;
- risco.

Exemplo:

```yaml
origem: PietraOS
destino: FabioOS
finalidade: lembrar pendencia docente sem expor alunos
dados_transferidos: resumo de tarefa, sem nomes de alunos
permissao: aprovada por Fabio
retencao: ate conclusao da tarefa
auditoria: changelog ou log local
risco: baixo se anonimizado
```

## Regras praticas

1. Se contem credencial, nao entra no vault.
2. Se contem aluno, turma, nota ou situacao escolar individual, tratar como restrito.
3. Se contem trading bruto, corretora, posicao ou financeiro, tratar como privado.
4. Se contem lore/campanha, classificar como PrimusOS e separar canonico de rascunho.
5. Se contem ferramenta, arquitetura, IA, automacao ou codigo, classificar como IAOS ou FabioOS tecnico.
6. Se a classificacao for duvidosa, escolher a classe mais restritiva.
7. Nenhum conteudo restrito deve ir para RAG/Grafo sem resumo anonimizado.
8. Nenhuma acao externa deve ocorrer sem aprovacao humana registrada.

## Implementacao v0

Script:

`60_Sistemas/FabioOS/scripts/classificar_dado_fabioos.py`

Saida padrao:

`60_Sistemas/FabioOS/classificacoes/`

O script le um arquivo local e gera uma nota de classificacao com:

- dominio provavel;
- classe de dado;
- permissao para RAG;
- permissao para Grafo;
- permissao para modelo externo;
- sinais detectados;
- decisao recomendada.

## Limites

O classificador v0 usa regras locais e palavras-chave. Ele nao substitui revisao humana, mas cria um gate minimo antes de ingestao, RAG, Grafo, automacao ou envio externo.
