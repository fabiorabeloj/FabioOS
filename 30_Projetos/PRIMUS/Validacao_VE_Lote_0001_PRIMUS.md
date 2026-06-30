---
tipo: validacao
area: 30_Projetos
projeto: PRIMUS
status: aplicado-preliminar
fonte: [[30_Projetos/PRIMUS/CatalogEntries_Lote_0001_PRIMUS]]
spec: [[80_Specs/PRIMUS/Spec_Validacao_VE_PRIMUS]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, validacao, ve, catalogentries]
---

# Validacao V(E) - Lote 0001

## Resultado Geral

| Criterio | Resultado |
|---|---|
| Type | ok |
| Class Base | ok |
| Source | ok em nivel de fonte; 5 entradas possuem evidencia local-index |
| Page/Snippet | parcial: 5 pass, 1 partial via PRIMUS Index |
| Box/Subbox | ok como bootstrap |
| Affects/NeverAffects | ok em padrao de lote |
| Instancing Hint | ok preliminar |
| Portability | ok preliminar |
| Precedence | pendente por fonte especifica |

## Decisao

O lote recebe `VE-pass-com-pendencia`: estrutura suficiente para organizar CatalogPool, mas insuficiente para gerar missao canonica.

Atualizacao 2026-06-30: 6 entradas foram verificadas via [[Validacao_VE_5_Entradas_PRIMUS_Index]]: 5 `pass` e 1 `partial`. Isso melhora a confianca do lote, mas ainda nao libera Missao 0001.

## Validacao por Grupo

| Grupo | Entries | Resultado | Pendencia |
|---|---|---|---|
| Jogador | CE-DND-0001 a CE-DND-0006 | VE-pass-com-pendencia com 5 evidencias locais | revisar CE-DND-0003 e CE-DND-0001 |
| Desafio | CE-DND-0007 a CE-DND-0010 | VE-pass-com-pendencia | pagina/trecho DMG/MM |
| Mundo | CE-WWN-0001, CE-WWN-0002, CE-WWN-0005, CE-WWN-0006 | VE-pass-com-pendencia | pagina/trecho WWN |
| Agentes coletivos | CE-WWN-0003, CE-WWN-0009 | VE-pass-com-pendencia | confirmar se fica em WWN ou SWN |
| Gatilhos | CE-WWN-0004, CE-WWN-0007, CE-WWN-0008, CE-WWN-0010 | VE-pass-com-pendencia | pagina/trecho WWN |

## Bloqueios

- Nenhuma entrada pode ser promovida a canon sem fonte/pagina.
- Nenhuma entrada pode gerar Missao 0001 sem DeltaP previsto.
- Faction turn deve aguardar decisao WWN vs SWN.

## Proxima Acao

Revisar `CE-DND-0003` para obter ancora generica melhor de `species/race`, ou iniciar `CE-DND-0007 creature` como primeira validacao do grupo Desafio.
