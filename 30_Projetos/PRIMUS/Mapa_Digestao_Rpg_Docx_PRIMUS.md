---
tipo: mapa-operacional
area: 30_Projetos
projeto: PRIMUS
status: ativo
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_google-drive-rpg-docx]]
criado_em: 2026-07-01
tags: [primus, digestor, rpg-docx, fonte-restrita, catalogentry]
---

# Mapa de Digestao - Rpg .docx - PRIMUS

## Funcao

Transformar o arquivo `Rpg .docx` em conhecimento operacional sem despejar texto protegido no vault.

Este mapa e a ponte entre:

- fonte bruta restrita;
- CatalogEntries candidatas;
- Enciclopedia Funcional;
- motores de mundo do PRIMUS.

## Source ID

```yaml
source_id: SRC-RPG-DOCX-2024
source_name: Rpg .docx
source_type: docx
source_layer: fonte-compilada-restrita
license_status: Restricted
storage_policy: no-full-text-in-git
```

## Fluxo

```text
Rpg .docx
  -> blocos por secao
  -> classificador de origem
  -> classificador PRIMUS
  -> CatalogEntry candidata
  -> validacao V(E)
  -> CatalogPool
  -> uso em WorldCycle/ProblemGenerator
```

## Classificador de Origem

Cada bloco deve cair em uma destas classes antes de virar nota:

| Classe | Regra |
|---|---|
| `autoral-provavel` | pode virar nota apos revisao humana |
| `restrito-oficial` | apenas metadados, resumo curto e referencia |
| `adaptacao-ou-traducao` | nao exportar texto; extrair padrao operacional |
| `procedimento-generico` | pode virar regra abstrata se nao copiar expressao |
| `ip-externa` | bloquear ou converter em analogia propria |
| `tabela-regra` | tratar como Restricted salvo fonte aberta |

## Familia de Nos

| Familia | Destino no PRIMUS | Exemplo de uso seguro |
|---|---|---|
| Premissas de mundo | `40_Wiki/PRIMUS/Enciclopedia/Regras_e_Procedimentos/` | assumptions de geracao |
| Cosmologia e planos | `40_Wiki/PRIMUS/Enciclopedia/Lugares/` | modelo planar abstrato |
| Divindades e antagonistas | `40_Wiki/PRIMUS/Enciclopedia/Faccoes_e_Culturas/` | pressao divina como vetor |
| Localidades | `40_Wiki/PRIMUS/Enciclopedia/Lugares/` | regiao-fronteira, ruina, passagem |
| Itens e artefatos | `40_Wiki/PRIMUS/Enciclopedia/Itens_e_Tesouros/` | item como motor de conflito |
| Aventuras e ganchos | `40_Wiki/PRIMUS/Instancias/` | estrutura de missao, nao texto |
| Tabelas e reputacao | `40_Wiki/PRIMUS/Enciclopedia/Regras_e_Procedimentos/` | medidores e custos |
| Criaturas e taticas | `40_Wiki/PRIMUS/Enciclopedia/Criaturas/` | padrao de encontro |

## Lotes

### Lote 0 - ja feito

- registrar fonte;
- reler com otica atual;
- criar mapa de digestao;
- criar CatalogEntries candidatas sem texto protegido.

### Lote 1 - seguro e recomendado

- selecionar 10 a 20 blocos;
- classificar origem;
- gerar CatalogEntries candidatas;
- validar `affects`, `never_affects` e `instancing_hint`;
- nao exportar markdown enciclopedico final ainda.

### Lote 2 - promocao controlada

- promover apenas entradas `autoral-provavel` ou `procedimento-generico`;
- manter `restrito-oficial` como referencia;
- bloquear `ip-externa` ate existir analogia propria.

### Lote 3 - integracao com motores

- alimentar [[80_Specs/PRIMUS/Spec_Operadores_Mundo_PRIMUS]];
- alimentar `ProblemGenerator v0`;
- gerar conflitos, nao missoes canonicas completas.

## Criterios de Aceite

- nenhuma pagina contem trecho longo de fonte restrita;
- toda entrada tem `source_id`;
- toda entrada tem `license_status`;
- toda entrada declara `affects` e `never_affects`;
- material externo nao altera canon PRIMUS sem decisao;
- cada nota nova linka [[40_Wiki/_MOCs/MOC_PRIMUS]].

## Nao Fazer

- nao copiar o documento integral;
- nao criar centenas de notas sem V(E);
- nao misturar conteudo autoral com IP externa sem tag;
- nao reindexar RAG automaticamente;
- nao usar a fonte como canon direto.
