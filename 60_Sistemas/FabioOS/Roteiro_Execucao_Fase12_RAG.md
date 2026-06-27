---
tipo: roteiro
area: 60_Sistemas
projeto: FabioOS
status: rascunho
fase: 12
tags: [fabios, rag, fase-12, execucao, validacao]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Roteiro de Execução — Fase 12 RAG

## Função

Transformar a arquitetura e os scripts da Fase 12 em uma sequência operacional curta, segura e verificável.

Este roteiro não substitui a [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]] nem o [[60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG]]. Ele organiza a ordem prática de execução.

## Estado atual

| Item | Estado |
|---|---|
| Arquitetura RAG | documentada |
| Scripts RAG | criados |
| Agente RAG | implementação mínima criada |
| Plano de validação | criado |
| Dependências | pendentes de instalação |
| Primeira ingestão | pendente |
| 10 perguntas reais | pendente |
| Promoção para piloto | não autorizada |

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
python 60_Sistemas/RAG/scripts/ingest_vault.py
```

Critério:

- [ ] Indexa `wiki/`.
- [ ] Indexa `60_Sistemas/`.
- [ ] Indexa `30_Conhecimento/`.
- [ ] Indexa `40_Decisoes/`.
- [ ] Indexa `10_Mapas/`.
- [ ] Não indexa pastas proibidas.

## 4. Primeira consulta

Executar:

```powershell
python 60_Sistemas/RAG/scripts/query_rag.py "O que é o FabioOS?"
```

Critério:

- [ ] Retorna resposta em português.
- [ ] Cita fontes.
- [ ] Não inventa informação fora do vault.

## 5. Validação com 10 perguntas

Usar a lista do [[60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG]]:

- [ ] O que é o FabioOS em uma frase?
- [ ] Qual é a fase atual do FabioOS?
- [ ] Quais pendências estão abertas antes da Fase 12?
- [ ] O que o Modelo Formal define sobre conhecimento?
- [ ] Como MEGATRON deve declarar ignorância?
- [ ] Qual é o papel do SafeCommit?
- [ ] Como o Arquivista transforma conteúdo bruto?
- [ ] Quais pastas não devem entrar no índice RAG?
- [ ] Como PietraOS pode evoluir para SaaS?
- [ ] Como PrimusOS organiza memória narrativa?

## 6. Registro de resultado

Após os testes:

- [ ] Criar relatório de validação.
- [ ] Registrar falhas e lacunas.
- [ ] Atualizar Painel de Pendências.
- [ ] Rodar SafeCommit/check-secrets.
- [ ] Commitar somente após aprovação.

## 7. Critério de saída

A Fase 12 só pode ser considerada `piloto` se:

- [ ] 8/10 respostas forem úteis.
- [ ] 10/10 respostas com evidência citarem fonte.
- [ ] Perguntas sem fonte declararem ignorância.
- [ ] Nenhuma pasta sensível aparecer no índice.
- [ ] Agente RAG continuar como `especificado` até revisão humana.

## Relações

- [[60_Sistemas/RAG/Arquitetura_RAG_FabioOS]]
- [[60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG]]
- [[60_Sistemas/MEGATRON/agentes/specs/Agente_RAG]]
- [[60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente]]
- [[10_Mapas/Painel_Pendencias_FabioOS]]

## Próximas ações

- [ ] Pedir aprovação para instalar dependências da Fase 12.
- [ ] Executar ingestão da primeira leva.
- [ ] Rodar 10 perguntas reais.
