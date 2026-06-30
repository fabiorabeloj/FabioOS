---
tipo: matriz-operacional
area: 60_Sistemas
projeto: FabioOS
status: rascunho
tags: [fabios, multiagente, codex, claude, frentes-paralelas, coordenacao]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Matriz de Frentes Paralelas do FabioOS

## Função

Definir quais frentes podem ser executadas em paralelo por Claude, Codex, MEGATRON ou futuros agentes sem conflito de arquivos, contexto ou responsabilidade.

Esta matriz complementa o [[60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente]].

## Princípio

```text
Paralelizar por fronteira de responsabilidade, não por pressa.
```

Uma frente paralela é segura quando:

- usa arquivos próprios ou novos;
- não altera o mesmo mapa, changelog ou configuração que outro agente;
- tem critério de conclusão claro;
- pode virar commit temático separado;
- não depende de segredo, push ou ação externa.

---

## 1. Estado atual das frentes

| Frente | Dono sugerido | Status | Arquivos principais | Risco de conflito | Próxima ação |
|---|---|---|---|---|---|
| Commits temáticos pendentes | Claude | em preparação | múltiplos arquivos já listados pelo Claude | Alto | Claude deve stagear por grupo e pedir OK |
| Coordenação multiagente | Codex | em rascunho | `60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente.md` | Baixo | Validar após commits do Claude |
| Matriz de frentes paralelas | Codex | em rascunho | este arquivo | Baixo | Usar como referência de coordenação |
| Agentes MEGATRON | Claude | implementado mínimo | `60_Sistemas/MEGATRON/agentes/` | Alto | Revisar antes de promover estado |
| RAG Fase 12 | Claude ou Codex | parcialmente iniciado | `60_Sistemas/RAG/` | Médio | Validar dependências antes de executar |
| Grafo/Ontologia | Codex | futuro seguro | `00_Arquitetura/` ou `60_Sistemas/Grafo/` | Baixo | Só iniciar após Fase 12 estabilizar |

---

## 2. Frentes seguras para Codex enquanto Claude commita

| Frente | Por que é segura | Arquivo recomendado |
|---|---|---|
| Coordenação multiagente | Usa arquivos novos e não altera scripts | `60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente.md` |
| Matriz de paralelização | Arquivo novo, governança operacional | `60_Sistemas/FabioOS/Matriz_Frentes_Paralelas.md` |
| Revisão conceitual da ontologia | Pode ser rascunho separado | `00_Arquitetura/02_Ontologia_FabioOS.md` |
| Checklist de revisão dos agentes | Pode ser relatório novo, sem alterar implementação | `60_Sistemas/MEGATRON/agentes/Revisao_Agentes_Checklist.md` |
| Plano de validação RAG | Pode ser arquivo novo, sem instalar dependências | `60_Sistemas/RAG/Plano_Validacao_RAG.md` |

## 3. Frentes que Codex deve evitar enquanto Claude commita

| Frente | Motivo |
|---|---|
| Editar `60_Sistemas/MEGATRON/agentes/` | Claude está preparando specs/implementação e commits |
| Editar `40_Wiki/_compat_wiki/indices/mapa-fabios.md` | Já está em commit planejado |
| Editar `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/10_Mapas/Painel_Pendencias_FabioOS.md` | Já está em commit planejado |
| Editar `60_Sistemas/FabioOS/bootstrap/CLAUDE.md` ou `60_Sistemas/FabioOS/bootstrap/AGENTS.md` | Arquivos de governança no grupo do Claude |
| Editar `.gitignore` | Claude já ajustou regras de cache/logs/config |
| Criar changelog concorrente | Pode confundir a ordem dos commits |

---

## 4. Critério para escolher a próxima frente

Use esta ordem:

1. **Baixo conflito**: arquivo novo ou pasta isolada.
2. **Alto valor estrutural**: melhora coordenação, segurança ou continuidade.
3. **Sem dependência externa**: não exige instalação, token, Docker ou API.
4. **Commitável separadamente**: pode virar commit próprio depois.
5. **Ajuda o próximo agente**: reduz dúvida para Claude, Codex ou MEGATRON.

## 5. Regra de handoff entre agentes

Toda transferência de trabalho deve informar:

```text
Frente:
Arquivos tocados:
Arquivos que não devem ser tocados:
Estado:
Risco:
Próxima ação:
Precisa de aprovação humana:
```

## 6. Modelo de mensagem curta para coordenação

```text
Estou assumindo a frente: [nome].
Vou tocar apenas: [arquivos].
Não vou tocar: [arquivos em uso por outro agente].
Resultado esperado: [entrega].
Não farei commit nem push sem aprovação.
```

## 7. Próxima recomendação

Enquanto Claude prepara os quatro commits temáticos, Codex deve permanecer em governança paralela e não alterar arquivos compartilhados.

Próxima frente segura recomendada para Codex:

```text
Criar um checklist de revisão humana dos agentes MEGATRON antes de promover estado de "especificado" para "piloto".
```

Esse checklist deve ser arquivo novo e não deve alterar `Registro_Agentes.md` nesta rodada.

## Relações

- [[60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente]]
- [[60_Sistemas/MEGATRON/agentes/README_Agentes]]
- [[60_Sistemas/MEGATRON/agentes/Registro_Agentes]]
- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]

## Próximas ações

- [ ] Validar esta matriz após os commits temáticos do Claude.
- [ ] Criar checklist de revisão humana dos agentes MEGATRON.
- [ ] Decidir se a matriz entra no mesmo commit de governança multiagente que o protocolo.
