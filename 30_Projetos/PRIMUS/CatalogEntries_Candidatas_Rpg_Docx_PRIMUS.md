---
tipo: catalogo-candidato
area: 30_Projetos
projeto: PRIMUS
status: rascunho-validavel
fonte: [[30_Projetos/PRIMUS/Mapa_Digestao_Rpg_Docx_PRIMUS]]
criado_em: 2026-07-01
tags: [primus, catalogentry, rpg-docx, fonte-restrita, validacao]
---

# CatalogEntries Candidatas - Rpg .docx

## Regra

Estas entradas nao sao canonicas. Elas sao candidatas de alto nivel extraidas de uma fonte mista e restrita.

Nao ha snippets longos neste arquivo. A validacao deve consultar a fonte local restrita quando necessario.

## Source

```yaml
source_id: SRC-RPG-DOCX-2024
license_status: Restricted
snippet_policy: none-in-git
validation_status: candidate
```

## Entradas Candidatas

| EntryID | Type | Name | Box | Affects | NeverAffects | Status |
|---|---|---|---|---|---|---|
| CE-RPGDOCX-0001 | generator | Premissas de Mundo de Campanha | E | configuracao inicial de mundo | regras DND e DeltaP | candidato |
| CE-RPGDOCX-0002 | world_rule | Mundo Selvagem como Pressao | E/P | tensoes regionais, viagem, risco | mapas canonicos sem V(E) | candidato |
| CE-RPGDOCX-0003 | world_rule | Mundo Antigo com Ruinas Ativas | E/P | ruinas, segredos, herancas | historia fechada sem DeltaP | candidato |
| CE-RPGDOCX-0004 | world_rule | Distribuicao de Magia | E | economia magica, raridade, risco | balanco mecanico DND | candidato |
| CE-RPGDOCX-0005 | procedure | Modelo Cosmologico Abstrato | E | planos, portais, zonas anomalas | lore oficial especifico | candidato |
| CE-RPGDOCX-0006 | procedure | Transito Planar como Complicacao | I/P | missao, custo, deslocamento | viagem sem consequencia | candidato |
| CE-RPGDOCX-0007 | faction | Faccao por Reputacao e Beneficio | E/P | relacoes, treino, recursos | tabelas oficiais copiadas | candidato |
| CE-RPGDOCX-0008 | region | Padrao de Regiao-Fronteira | E/P | perigo local, passagem, conflito | nomes externos como canon | candidato |
| CE-RPGDOCX-0009 | magic_item | Artefato como Vetor de Campanha | E/I | desejo, ambicao, conflito | IP externa literal | bloqueado-ate-analogizar |
| CE-RPGDOCX-0010 | mission | Missao por Violacao e Reparacao | I/P | problema, negociacao, consequencia | aventura integral | candidato |
| CE-RPGDOCX-0011 | encounter | Padrao de Encontro com Escolha Social | I | diplomacia, combate, retorno | texto de aventura | candidato |
| CE-RPGDOCX-0012 | encounter | Taticas de Ameaca Organizada | I | cerco, reconhecimento, pressao | statblock ou lore copiado | candidato |

## Cinco Entradas Mais Seguras para V(E)

1. `CE-RPGDOCX-0001` - Premissas de Mundo de Campanha.
2. `CE-RPGDOCX-0002` - Mundo Selvagem como Pressao.
3. `CE-RPGDOCX-0003` - Mundo Antigo com Ruinas Ativas.
4. `CE-RPGDOCX-0005` - Modelo Cosmologico Abstrato.
5. `CE-RPGDOCX-0010` - Missao por Violacao e Reparacao.

## Entradas Bloqueadas

`CE-RPGDOCX-0009` fica bloqueada ate ser convertida em analogia propria. O padrao e util, mas nomes e expressao de IP externa nao entram como canon.

## Proxima Acao

Validar as cinco entradas seguras contra [[80_Specs/PRIMUS/Spec_Validacao_VE_PRIMUS]] e, se passarem, criar paginas enciclopedicas abstratas, nao transcricoes.
