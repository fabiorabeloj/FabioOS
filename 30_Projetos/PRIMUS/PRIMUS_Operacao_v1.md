---
tipo: cockpit
area: 30_Projetos
projeto: PRIMUS
status: operacional-minimo
fonte: [[40_Wiki/PRIMUS/Changelog_PRIMUS_5_6]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, operacao, cockpit, worldcycle]
---

# PRIMUS - Operacao v1

## Funcao

Painel minimo para operar o PRIMUS sem depender da memoria do chat.

## Estado Atual

| Item | Estado |
|---|---|
| Changelog 5.6 | formalizado |
| WorldState | rascunho operacional |
| Tension Engine | rascunho operacional |
| Vector Engine | rascunho operacional |
| Cantina | prototipo seguro |
| Villain Engine | rascunho operacional |
| WorldCycle | procedimento v0 |
| Missao 0001 | bloqueada |

## Abrir Primeiro

1. [[40_Wiki/PRIMUS/Changelog_PRIMUS_5_6]]
2. [[30_Projetos/PRIMUS/WorldState_0001_PRIMUS]]
3. [[30_Projetos/PRIMUS/Vectors_0001_PRIMUS]]
4. [[30_Projetos/PRIMUS/Tensoes_Iniciais_PRIMUS]]
5. [[30_Projetos/PRIMUS/Conflitos_Candidatos_PRIMUS]]
6. [[30_Projetos/PRIMUS/Cantina_Board_0001_PRIMUS]]
7. [[30_Projetos/PRIMUS/Mission_Contract_0001_PRIMUS]]
8. [[30_Projetos/PRIMUS/DeltaP_Log_0001_PRIMUS]]

## Rodada Operacional Manual

Use este checklist para qualquer rodada:

- [ ] Ler WorldState.
- [ ] Escolher um vetor relevante.
- [ ] Verificar tensao associada.
- [ ] Verificar conflito candidato.
- [ ] Decidir se aparece na Cantina.
- [ ] Se virar missao, preencher Mission Contract.
- [ ] Prever sucesso, falha e ignorado.
- [ ] Registrar DeltaP previsto.
- [ ] Executar somente se fontes e validacao permitirem.
- [ ] Aplicar DeltaP no WorldState apenas depois da execucao.
- [ ] Registrar log e changelog.

## Proibicoes

- Nao executar Missao 0001 ainda.
- Nao promover lore a canon sem fonte.
- Nao alterar WorldState sem DeltaP.
- Nao criar vilao canonico sem CatalogEntry ou fonte validada.

## Proxima Acao Real

Validar pagina/trecho de 5 CatalogEntries prioritarias.

Depois disso:

1. promover parte do CatalogPool;
2. preencher WorldState v1.0;
3. selecionar um vetor jogavel;
4. criar Mission Contract 0001 validado.
