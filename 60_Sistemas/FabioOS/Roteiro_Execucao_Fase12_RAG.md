---
tipo: roteiro
area: 60_Sistemas
projeto: FabioOS
status: rascunho
fase: 12
tags: [fabios, rag, fase-12, execucao, validacao]
criado_em: 2026-06-26
atualizado_em: 2026-06-29
---

# Roteiro de Execução — Fase 12 RAG

## Função

Transformar a arquitetura e os scripts da Fase 12 em uma sequência operacional curta, segura e verificável.

Este roteiro não substitui a [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]] nem o [[60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG]]. Ele organiza a ordem prática de execução.

## Estado atual

| Item | Estado |
|---|---|
| Arquitetura RAG | documentada |
| Scripts RAG | criados + batch de validacao |
| Agente RAG | implementação mínima criada |
| Plano de validação | criado |
| Dependências | instaladas em `60_Sistemas/RAG/.venv/` |
| Primeira ingestão | concluída; reindex pos-limpeza Obsidian com `1206` chunks |
| 10 perguntas reais | **concluídas 10/10** (2026-06-29, Cursor) |
| Promoção para piloto | aguarda revisão Claude |

---

## 1. Preparação

- [ ] Confirmar que o working tree está limpo.
- [ ] Confirmar que `.env`, tokens e credenciais não serão usados.
- [ ] Ler [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]].
- [ ] Ler [[60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG]].
- [ ] Confirmar que `sources/_inbox/`, `00_Inbox/`, logs Pietra e configs locais estão excluídos.

## 2. Instalação controlada

Executar somente após aprovação humana:

```powershell
pip install -r 60_Sistemas/RAG/requirements.txt
```

Critério:

- [ ] Dependências instaladas sem erro.
- [ ] Nenhum token exigido.
- [ ] Nenhum dado sensível enviado a serviço externo.

## 3. Primeira ingestão

Executar:

```powershell
60_Sistemas\RAG\.venv\Scripts\python.exe 60_Sistemas\RAG\scripts\ingest_vault.py
```

Critério:

- [x] Indexa `wiki/`.
- [x] Indexa corpus operacional selecionado de `60_Sistemas/`.
- [x] Indexa painel legado necessario em `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/`.
- [x] Indexa decisoes legadas em `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/40_Decisoes/`.
- [x] Não indexa pastas proibidas.

## 4. Primeira consulta

Executar:

```powershell
60_Sistemas\RAG\.venv\Scripts\python.exe 60_Sistemas\RAG\scripts\query_rag.py "O que é o FabioOS?"
```

Critério:

- [ ] Retorna resposta em português.
- [ ] Cita fontes.
- [ ] Não inventa informação fora do vault.

## 5. Validação com 10 perguntas

**Batch automatizado (recomendado):**

```powershell
60_Sistemas\RAG\.venv\Scripts\python.exe 60_Sistemas\RAG\scripts\batch_validate_rag.py --k 5
```

Relatório: [[60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-29_Cursor]].

Usar a lista do [[60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG]]:

- [x] O que é o FabioOS em uma frase?
- [x] Qual é a fase atual do FabioOS?
- [x] Quais pendências estão abertas antes da Fase 12?
- [x] O que o Modelo Formal define sobre conhecimento?
- [x] Como MEGATRON deve declarar ignorância?
- [x] Qual é o papel do SafeCommit?
- [x] Como o Arquivista transforma conteúdo bruto?
- [x] Quais pastas não devem entrar no índice RAG?
- [x] Como PietraOS pode evoluir para SaaS?
- [x] Como PrimusOS organiza memória narrativa?

## 6. Registro de resultado

Após os testes:

- [x] Criar relatório de validação — [[60_Sistemas/RAG/Relatorio_Validacao_RAG_2026-06-29_Cursor]]
- [x] Registrar falhas e lacunas — ranking status corrigido; 10/10 pos-ajuste
- [x] Atualizar STATUS/NEXT_ACTIONS e Registro de Frentes com resultado pos-reindex
- [x] Rodar SafeCommit/check-secrets
- [x] Commitar somente após aprovação

## 7. Critério de saída

A Fase 12 só pode ser considerada `piloto` se:

- [x] 8/10 respostas forem úteis — **10/10**
- [x] 10/10 respostas com evidência citarem fonte (modo recuperação)
- [ ] Perguntas sem fonte declararem ignorância.
- [ ] Nenhuma pasta sensível aparecer no índice.
- [ ] Agente RAG continuar como `especificado` até revisão humana.

## Relações

- [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]]
- [[60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG]]
- [[60_Sistemas/MEGATRON/agentes/specs/Agente_RAG]]
- [[60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente]]
- [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Painel_Pendencias_FabioOS]]

## Próximas ações

- [ ] Claude decidir promoção Fase 12 → piloto
- [x] Commitar entregas Cursor/Codex após scan de segredos
- [ ] Reindexação incremental quando houver novos documentos relevantes
