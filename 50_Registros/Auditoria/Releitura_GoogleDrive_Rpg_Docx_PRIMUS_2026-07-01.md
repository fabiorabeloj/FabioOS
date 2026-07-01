---
tipo: auditoria
area: 50_Registros
projeto: PRIMUS
status: concluido
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_google-drive-rpg-docx]]
criado_em: 2026-07-01
tags: [primus, auditoria, google-drive, rpg-docx, fonte-restrita]
---

# Releitura Google Drive - Rpg .docx - PRIMUS

## Fonte

- Arquivo: `Rpg .docx`
- Drive ID: `1b2-bN2m9eZ6S_s339cM3msrYmIutx0mZ`
- Tipo original: DOCX
- Modificado em: `2024-12-19T02:35:03.666Z`
- Nota-fonte local: [[05_Raw_Sources/PRIMUS/2026-06-30_google-drive-rpg-docx]]

## Resultado da Releitura

O arquivo nao deve ser tratado como livro do PRIMUS nem como fonte canonica direta.

Ele e uma fonte-mae restrita, grande e mista, contendo:

- premissas de campanha e construcao de mundo;
- cosmologia, planos e modelos planares;
- divindades, antagonistas e conflitos historicos;
- localidades, itens, faccoes, aventuras e ganchos;
- tabelas e procedimentos de jogo;
- material traduzido, adaptado ou copiado de fontes externas.

## Decisao

O corpo integral permanece fora do Git, fora do Obsidian publico e fora de qualquer exportacao RAG automatica.

O uso correto e transformar o arquivo em:

1. mapa de digestao;
2. CatalogEntries candidatas;
3. metadados rastreaveis;
4. abstracoes operacionais;
5. entradas autorais somente quando a origem for validada.

## Diagnostico Arquitetural

O documento ensina que PRIMUS precisa de um funil antes da Enciclopedia:

```text
Fonte mista
  -> classificador de origem
  -> bloco seguro
  -> CatalogEntry candidata
  -> V(E)
  -> CatalogPool
  -> instancia jogavel
```

Sem esse funil, o projeto vira acumulacao de lore. Com esse funil, a fonte vira motor.

## Classificacao dos Blocos Observados

| Classe | Pode virar no PRIMUS | Restricao |
|---|---|---|
| Premissas de mundo | regras de geracao e world assumptions | nao copiar expressao textual longa |
| Cosmologia e planos | nos `plane`, `procedure`, `region` | validar se e canon externo ou abstracao propria |
| Divindades e conflitos | `deity`, `faction`, `villain_pressure` | cuidado com lore oficial protegido |
| Localidades | `region`, `site`, `frontier_pattern` | separar nome proprio externo de padrao reutilizavel |
| Itens e artefatos | `magic_item`, `campaign_vector` | itens de IP externa ficam bloqueados ou analogicos |
| Aventuras | `mission`, `encounter`, `complication` | nunca exportar aventura integral |
| Tabelas e regras | `procedure`, `generator`, `reward` | regras DND ficam Restricted |
| Taticas de criaturas | `encounter_pattern` | nao copiar statblock ou texto de monstro |

## Impacto no PRIMUS

Esta releitura cria tres entregas operacionais:

- [[30_Projetos/PRIMUS/Mapa_Digestao_Rpg_Docx_PRIMUS]]
- [[30_Projetos/PRIMUS/CatalogEntries_Candidatas_Rpg_Docx_PRIMUS]]
- atualizacao de [[40_Wiki/PRIMUS/Matriz_Fontes_PRIMUS]]

## Lacuna Encontrada

O digestor ja existia como pipeline, mas faltava um contrato explicito para fonte mista:

- separar autoral de restrito;
- aceitar padroes sem copiar texto;
- bloquear material de IP externa;
- promover somente entradas com `source_id`, `license_status`, `affects` e `never_affects`.

## Proxima Acao Recomendada

Rodar um lote manual de 10 a 20 blocos do `Rpg .docx` somente como CatalogEntries candidatas, sem exportar corpo textual e sem reindexar RAG.
