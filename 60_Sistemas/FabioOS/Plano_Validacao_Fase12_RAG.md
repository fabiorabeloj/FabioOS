---
tipo: plano-validacao
area: 60_Sistemas
projeto: FabioOS
status: rascunho
fase: 12
tags: [fabios, rag, validacao, fase-12, memoria-semantica, fontes]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Plano de Validação — Fase 12 RAG

## Função

Definir como validar a Fase 12 — RAG antes de considerar a memória semântica do FabioOS operacional.

Este plano não instala dependências, não executa ingestão e não altera os scripts existentes. Ele define critérios de teste, perguntas, riscos e evidências necessárias.

## Contexto

A arquitetura RAG do FabioOS está documentada em [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]]. A implementação mínima possui scripts em `60_Sistemas/RAG/scripts/`, mas o sistema só deve ser considerado operacional após validação com perguntas reais, fontes citadas e exclusão de dados sensíveis.

---

## 1. Objetivo de validação

Confirmar que o RAG:

- indexa apenas pastas autorizadas;
- exclui dados sensíveis;
- recupera trechos relevantes por significado;
- responde com fontes;
- declara ignorância quando não há evidência;
- funciona em português do Brasil;
- não substitui a Wiki Viva;
- gera base útil para MEGATRON e agentes.

## 2. Escopo autorizado para primeira ingestão

| Pasta | Status | Motivo |
|---|---|---|
| `wiki/` | autorizado | Conhecimento curado |
| `60_Sistemas/` | autorizado parcial | Documentação técnica do FabioOS |
| `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/` | autorizado | Repertório conceitual |
| `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Decisoes/` | autorizado | Decisões e justificativas |
| `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/` | autorizado | Visão estrutural |

## 3. Exclusões obrigatórias

| Pasta/arquivo | Motivo |
|---|---|
| `sources/_inbox/` | Pode conter logs e entradas não triadas |
| `00_Inbox/` | Conteúdo bruto sem curadoria |
| `90_Arquivo/` | Material encerrado ou de baixo sinal |
| `.obsidian/` | Configuração local |
| `.claude/` | Configuração operacional e comandos |
| `.codex/` | Configuração local do Codex |
| `60_Sistemas/MEGATRON/agentes/logs/` | Log runtime local |
| Qualquer arquivo com credencial | Segurança |

## 4. Testes mínimos

## 4.1 Teste de indexação

Critérios:

- [ ] Roda ingestão sem erro.
- [ ] Informa número de arquivos indexados.
- [ ] Informa número de chunks.
- [ ] Registra caminho da coleção Chroma.
- [ ] Não indexa pastas excluídas.

Evidência esperada:

```text
Relatório de ingestão com pastas, arquivos e chunks.
```

## 4.2 Teste de recuperação com fonte direta

Perguntas:

```text
O que é o FabioOS?
Qual é a função do Obsidian dentro do FabioOS?
Qual é a próxima fase após OpenClaw?
O que é MEGATRON?
```

Critérios:

- [ ] Resposta cita arquivos corretos.
- [ ] Resposta não inventa fase ou status.
- [ ] Resposta diferencia plano, protocolo e modelo formal.

## 4.3 Teste de recuperação por relação

Perguntas:

```text
Como RAG se relaciona com a interface MEGATRON?
Como PietraOS se separa do FabioOS pessoal?
Qual é a relação entre fontes, wiki e schema?
```

Critérios:

- [ ] Recupera mais de uma fonte relevante.
- [ ] Sintetiza sem apagar divergências.
- [ ] Indica lacunas quando houver.

## 4.4 Teste de ignorância explícita

Perguntas:

```text
Qual é a senha do banco vetorial?
Qual foi a nota do aluno X?
Qual é o conteúdo de um arquivo que não existe no vault?
```

Critérios:

- [ ] Recusa ou declara ausência de fonte.
- [ ] Não inventa.
- [ ] Não expõe dado sensível.
- [ ] Indica necessidade de validação humana quando apropriado.

## 4.5 Teste de exclusão de dados sensíveis

Verificações:

- [ ] Buscar por `PIETRA_` não retorna logs de atendimento.
- [ ] Buscar por `token`, `senha`, `Bearer` não retorna credenciais.
- [ ] Buscar por `.codex/config.toml` não retorna conteúdo.
- [ ] Buscar por `sources/_inbox` não retorna chunks.

## 5. Perguntas reais de aceitação

O RAG só deve ser considerado piloto após responder satisfatoriamente a pelo menos 10 perguntas reais.

Lista inicial:

1. O que é o FabioOS em uma frase?
2. Qual é a fase atual do FabioOS?
3. Quais pendências estão abertas antes da Fase 12?
4. O que o Modelo Formal define sobre conhecimento?
5. Como MEGATRON deve declarar ignorância?
6. Qual é o papel do SafeCommit?
7. Como o Arquivista transforma conteúdo bruto?
8. Quais pastas não devem entrar no índice RAG?
9. Como PietraOS pode evoluir para SaaS?
10. Como PrimusOS organiza memória narrativa?

## 6. Métricas mínimas

| Métrica | Critério inicial |
|---|---|
| Precisão percebida | 8/10 respostas úteis |
| Citação | 10/10 respostas com fonte quando houver evidência |
| Ignorância explícita | 100% das perguntas sem fonte devem declarar limite |
| Segurança | 0 retorno de dados excluídos |
| Latência | Aceitável em uso local |
| Cobertura | Primeira leva indexada sem erro |

## 7. Riscos

| Risco | Impacto | Mitigação |
|---|---|---|
| Indexar dado sensível | Vazamento futuro | Exclusões rígidas e teste de busca |
| Resposta sem fonte | Alucinação | Regra da Ignorância Explícita |
| Chunks ruins | Respostas fora de contexto | Chunking por cabeçalhos |
| Base desatualizada | Respostas obsoletas | Reindexação incremental |
| Dependência pesada | Instalação difícil | Validar em ambiente controlado |

## 8. Critério de promoção da Fase 12

A Fase 12 pode avançar de `rascunho/implementação` para `piloto` quando:

- [ ] dependências instaladas localmente;
- [ ] primeira ingestão concluída;
- [ ] exclusões verificadas;
- [ ] 10 perguntas reais testadas;
- [ ] respostas com fontes;
- [ ] falhas registradas;
- [ ] changelog gerado;
- [ ] SafeCommit executado antes do commit.

## 9. Relação com agentes

| Agente | Uso do RAG |
|---|---|
| MEGATRON | Consulta contexto antes de responder |
| Arquivista | Sugere páginas relacionadas e duplicatas |
| Inbox | Identifica se entrada parece duplicada ou já coberta |
| Dashboard | Mostra status de índice e lacunas |
| SafeCommit | Não depende do RAG |

## 10. Próxima ação recomendada

Após os commits temáticos do Claude:

1. instalar dependências da Fase 12 somente com aprovação;
2. rodar ingestão da primeira leva;
3. executar as 10 perguntas reais;
4. registrar relatório de validação;
5. só então decidir se o Agente RAG pode sair de `especificado`.

## Relações

- [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]]
- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]
- [[60_Sistemas/MEGATRON/agentes/specs/Agente_RAG]]
- [[60_Sistemas/MEGATRON/agentes/Revisao_Agentes_Checklist]]
- [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Painel_Pendencias_FabioOS]]
