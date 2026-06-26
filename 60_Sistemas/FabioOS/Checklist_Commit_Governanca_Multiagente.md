---
tipo: checklist
area: 60_Sistemas
projeto: FabioOS
status: rascunho
tags: [fabios, multiagente, commit, governanca, codex]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Checklist de Commit — Governança Multiagente

## Função

Definir o pacote de arquivos criados pelo Codex em frente paralela para futura revisão e commit separado, sem misturar com os quatro commits temáticos preparados pelo Claude.

## Arquivos desta frente

| Arquivo | Função | Status |
|---|---|---|
| `60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente.md` | Regras de coordenação entre Codex, Claude, MEGATRON e futuros agentes | rascunho |
| `60_Sistemas/FabioOS/Matriz_Frentes_Paralelas.md` | Matriz de divisão de trabalho e zonas de conflito | rascunho |
| `60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG.md` | Plano de teste da Fase 12 RAG antes de promoção a piloto | rascunho |
| `60_Sistemas/FabioOS/Checklist_Commit_Governanca_Multiagente.md` | Este checklist | rascunho |
| `60_Sistemas/MEGATRON/agentes/Revisao_Agentes_Checklist.md` | Checklist de revisão antes de promover agentes | rascunho |
| `60_Sistemas/MEGATRON/agentes/Revisao_Implementacao_Minima_2026-06-26.md` | Revisão técnica da implementação mínima dos agentes | rascunho |
| `50_Registros/Changelog/2026-06-26_governanca-revisao-multiagente.md` | Changelog da frente de governança/revisão | concluido |

## Correções de implementação associadas

Estas correções não são documentação; devem entrar em commit próprio de `fix`:

| Arquivo | Correção |
|---|---|
| `60_Sistemas/MEGATRON/agentes/implementacao/claude/safecommit.py` | Remove sugestão de `git add -A` e orienta stage explícito por grupo temático |
| `60_Sistemas/MEGATRON/agentes/implementacao/claude/arquivista.py` | Bloqueia destino `--dest` fora da raiz do vault |

## Não incluir nos commits do Claude

Estes arquivos não devem entrar nos commits atuais do Claude:

```text
60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente.md
60_Sistemas/FabioOS/Matriz_Frentes_Paralelas.md
60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG.md
60_Sistemas/FabioOS/Checklist_Commit_Governanca_Multiagente.md
50_Registros/Changelog/2026-06-26_governanca-revisao-multiagente.md
60_Sistemas/MEGATRON/agentes/Revisao_Agentes_Checklist.md
60_Sistemas/MEGATRON/agentes/Revisao_Implementacao_Minima_2026-06-26.md
```

## Commits futuros sugeridos

### Commit 1 — correção dos agentes

```text
fix: ajustar seguranca dos agentes MEGATRON
```

Arquivos:

```text
60_Sistemas/MEGATRON/agentes/implementacao/claude/safecommit.py
60_Sistemas/MEGATRON/agentes/implementacao/claude/arquivista.py
```

### Commit 2 — governança e revisão

```text
docs: adicionar governanca e revisao multiagente
```

Arquivos: os documentos listados na seção "Arquivos desta frente".

## Checklist antes do commit

- [ ] Confirmar que os quatro commits temáticos do Claude foram concluídos ou descartados.
- [ ] Rodar SafeCommit/check-secrets.
- [ ] Verificar se nenhum arquivo de log/runtime entrou.
- [ ] Decidir se estes documentos devem ser linkados no `wiki/indices/mapa-fabios.md`.
- [ ] Decidir se o Protocolo de Coordenação deve ser promovido de `rascunho` para `ativo`.
- [x] Gerar changelog da frente de governança multiagente.
- [ ] Pedir aprovação humana antes de commit.
- [ ] Não fazer push.

## Relações

- [[60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente]]
- [[60_Sistemas/FabioOS/Matriz_Frentes_Paralelas]]
- [[60_Sistemas/FabioOS/Plano_Validacao_Fase12_RAG]]
- [[60_Sistemas/MEGATRON/agentes/Revisao_Agentes_Checklist]]
- [[60_Sistemas/MEGATRON/agentes/Revisao_Implementacao_Minima_2026-06-26]]

## Próximas ações

- [ ] Aguardar conclusão dos commits temáticos do Claude.
- [ ] Revisar os documentos desta frente.
- [ ] Preparar changelog e commit separado.
