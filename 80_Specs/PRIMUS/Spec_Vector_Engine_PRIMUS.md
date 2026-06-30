---
tipo: spec
area: 80_Specs
projeto: PRIMUS
status: rascunho-operacional
fonte: [[40_Wiki/PRIMUS/Changelog_PRIMUS_5_6]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, spec, vector-engine, worldstate]
---

# Spec - Vector Engine PRIMUS

## Missao

Transformar forcas persistentes do mundo em objetos operacionais rastreaveis.

## Entrada

- [[30_Projetos/PRIMUS/WorldState_0001_PRIMUS]]
- [[30_Projetos/PRIMUS/Tensoes_Iniciais_PRIMUS]]
- [[30_Projetos/PRIMUS/CatalogPool_0001_PRIMUS]]
- [[40_Wiki/PRIMUS/Changelog_PRIMUS_5_6]]

## Saida

- [[30_Projetos/PRIMUS/Vectors_0001_PRIMUS]]
- conflitos candidatos;
- atualizacoes para WorldCycle;
- DeltaP previsto.

## Campos Minimos

```yaml
vector_id:
nome:
tipo:
estado:
direcao:
intensidade:
alvo:
bloqueio:
gatilhos:
atores_relacionados:
conflitos_relacionados:
delta_p_possivel:
fonte:
canon_status:
```

## Estados Permitidos

- ativo;
- latente;
- selado;
- oculto;
- derrotado;
- transformado;

## Algoritmo Manual v0

1. Ler WorldState.
2. Listar tensoes abertas.
3. Para cada tensao, perguntar qual forca pressiona o mundo.
4. Criar ou atualizar vetor.
5. Atribuir estado.
6. Definir alvo e bloqueio.
7. Definir consequencia se ignorado.
8. Registrar possivel DeltaP.
9. Expor apenas vetores seguros na Cantina.

## Permissoes

Pode:

- criar vetor rascunho;
- propor mudanca de estado;
- sugerir conflito candidato;
- sugerir DeltaP.

Nao pode:

- promover vetor a canon sem fonte;
- alterar WorldState sem DeltaP;
- executar Missao 0001.

## Criterios de Aceite

- todo vetor possui estado;
- todo vetor declara consequencia se ignorado;
- todo vetor possui fonte ou status de rascunho;
- todo vetor aponta para tensao/conflito ou justifica ausencia;
- nenhum vetor canonico nasce sem V(E), V(I) ou V(P) aplicavel.
