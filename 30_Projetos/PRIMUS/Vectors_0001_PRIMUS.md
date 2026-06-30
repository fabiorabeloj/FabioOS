---
tipo: registro
area: 30_Projetos
projeto: PRIMUS
status: rascunho-operacional
fonte: [[80_Specs/PRIMUS/Spec_Vector_Engine_PRIMUS]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, vetores, worldstate, worldcycle]
---

# Vectors 0001 PRIMUS

## Funcao

Registrar forcas persistentes que pressionam o PRIMUS.

## Tabela

| ID | Nome | Tipo | Estado | Intensidade | Alvo | Status Canonico |
|---|---|---|---|---|---|---|
| VEC-0001 | Catalogo sem fonte pontual | operacional | ativo | alta | CatalogPool | meta-operacional |
| VEC-0002 | Cantina como filtro de conflito | interface | ativo | media | Player View | prototipo |
| VEC-0003 | Vilao persistente a definir | narrativo | latente | baixa | Villain Engine | bloqueado |
| VEC-0004 | Faccoes sem movimento formal | narrativo | latente | media | Faction Engine futuro | bloqueado |

## VEC-0001 - Catalogo sem fonte pontual

```yaml
vector_id: VEC-0001
nome: Catalogo sem fonte pontual
tipo: operacional
estado: ativo
direcao: forcar validacao V(E)
intensidade: alta
alvo: CatalogPool_0001
bloqueio: falta pagina/trecho em 5 entradas prioritarias
consequencia_se_ignorado: Missao 0001 continua bloqueada ou vira aventura sem lastro
delta_p_possivel: nenhum narrativo; gera decisao operacional
fonte: [[Validacao_VE_Lote_0001_PRIMUS]]
canon_status: meta-operacional
```

## VEC-0002 - Cantina como filtro de conflito

```yaml
vector_id: VEC-0002
nome: Cantina como filtro de conflito
tipo: interface
estado: ativo
direcao: expor escolhas sem revelar Enciclopedia total
intensidade: media
alvo: PlayerView_Cantina_0001
bloqueio: falta Mission Contract validado
consequencia_se_ignorado: jogador ve lore demais ou recebe missao sem consequencia
delta_p_possivel: CantinaOptionCreated
fonte: [[Spec_Cantina_Conflict_Engine_PRIMUS]]
canon_status: prototipo
```

## VEC-0003 - Vilao persistente a definir

```yaml
vector_id: VEC-0003
nome: Vilao persistente a definir
tipo: narrativo
estado: latente
direcao: criar primeiro antagonista como vetor historico
intensidade: baixa
alvo: Villain_Engine
bloqueio: falta fonte/canon_status
consequencia_se_ignorado: PRIMUS segue sem arco longo de ameaca
delta_p_possivel: VillainCreated
fonte: [[Changelog_PRIMUS_5_6]]
canon_status: bloqueado
```

## VEC-0004 - Faccoes sem movimento formal

```yaml
vector_id: VEC-0004
nome: Faccoes sem movimento formal
tipo: narrativo
estado: latente
direcao: ligar faccoes a vetores e conflitos
intensidade: media
alvo: Faction Engine futuro
bloqueio: faction schema ainda nao formalizado
consequencia_se_ignorado: conflitos ficam individuais demais
delta_p_possivel: FactionShift
fonte: [[Changelog_PRIMUS_5_6]]
canon_status: bloqueado
```

## Proxima Acao

Resolver `VEC-0001`: validar 5 entradas prioritarias do CatalogPool.
