---
tipo: schema
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [wiki, schema, llm-wiki, obsidian, governanca]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Schema Wiki FabioOS

## Funcao

Definir como agentes mantem a LLM Wiki do FabioOS.

Este schema complementa:

- [[60_Sistemas/Wiki/schema/fluxo-wiki]]
- [[60_Sistemas/Wiki/schema/qualidade-wiki]]
- [[30_Projetos/FabioOS/LLM_Wiki_FabioOS]]

## Estrutura

| Camada | Caminho preferencial | Regra |
|---|---|---|
| Fonte bruta | `05_Raw_Sources/` (`05_Raw_Sources/_compat_sources/` em compatibilidade), `00_Inbox/` | preservar evidencia, sem editar destrutivamente |
| Wiki processada | `40_Wiki/` (`40_Wiki/_compat_wiki/` em compatibilidade) | conhecimento compilado, linkado e revisavel |
| Schema | `60_Sistemas/Wiki/schema/` e `60_Sistemas/Wiki/` | regras de manutencao |
| Registro | `50_Registros/Logs_Agentes/log.md`, changelogs, auditorias | rastro cronologico |
| Navegacao | `10_Dashboard/_entrada/index.md`, `40_Wiki/_compat_wiki/README.md`, dashboards | entrada para humanos e agentes |

## Tipos de pagina

| Tipo | Uso |
|---|---|
| fonte | resumo de material bruto e sua origem |
| conceito | ideia reutilizavel |
| entidade | pessoa, empresa, modelo, ferramenta ou sistema |
| ferramenta | software, API, plataforma ou conector |
| sintese | consolidacao entre varias fontes |
| comparacao | tabela ou analise entre alternativas |
| decisao | decisao arquitetural ou operacional |
| protocolo | regra executavel do sistema |
| skill | competencia reutilizavel |
| spec | especificacao de implementacao |
| indice | mapa de navegacao |
| log | registro cronologico append-only |

## Frontmatter minimo

```yaml
---
tipo:
area:
projeto: FabioOS
status:
tags:
criado_em: YYYY-MM-DD
atualizado_em: YYYY-MM-DD
---
```

Campos adicionais recomendados:

```yaml
fonte:
relacionado:
responsavel:
risco:
revisao:
```

## Regras de links internos

- Usar links Obsidian `[[caminho/arquivo]]` quando apontar para nota interna.
- Toda pagina nova deve ter pelo menos um link de entrada previsto e um link de saida.
- Paginas centrais devem ser ligadas a `10_Dashboard/_entrada/index.md`, dashboard ou `40_Wiki/_compat_wiki/README.md`.
- Evitar criar pagina nova se uma pagina existente puder ser atualizada.

## Regra para criar nova pagina

Criar pagina nova somente quando:

1. nao existir equivalente claro;
2. o assunto tiver funcao operacional propria;
3. houver caminho de descoberta por index, dashboard ou link;
4. o conteudo tiver fonte, decisao ou utilidade definida;
5. a pagina puder ser mantida no futuro.

## Regra para atualizar pagina existente

Atualizar pagina existente quando:

- o conceito ja existir;
- a nova fonte so enriquecer ou corrigir a pagina;
- houver contradicao a registrar;
- a pagina estiver incompleta;
- a nova informacao mudar a aplicacao no FabioOS.

## Contradicoes

Toda contradicao deve registrar:

- fonte nova;
- afirmacao anterior;
- diferenca;
- impacto;
- decisao ou pendencia;
- data.

Formato:

```markdown
## Contradicoes e revisoes
- 2026-06-29: [fonte] contradiz [pagina/trecho]. Impacto: ... Proxima acao: ...
```

## Arquivamento

Nao apagar pagina por padrao.

Preferir:

- marcar `status: superseded`;
- apontar substituto;
- mover apenas com decisao registrada, se necessario;
- manter historico no Git.

## Lint

Lint deve verificar:

- frontmatter ausente;
- links quebrados;
- notas orfas;
- duplicatas;
- contradicoes;
- paginas sem funcao;
- fontes sem wiki;
- paginas importantes fora de index/dashboard.

Protocolo: [[60_Sistemas/Wiki/Protocolo_Lint_LLM_Wiki]]

## Index e log

- `10_Dashboard/_entrada/index.md` e entrada semantica compacta para agentes.
- `50_Registros/Logs_Agentes/log.md` e registro cronologico append-only.
- `40_Wiki/_compat_wiki/README.md` continua sendo indice da pasta `40_Wiki/_compat_wiki/`.
- `50_Registros/Changelog/` continua sendo changelog de engenharia e governanca.
