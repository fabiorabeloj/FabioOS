---
tipo: changelog
area: 50_Registros
projeto: FabioOS
sistema: Obsidian
status: concluido
classe_dado: interno
criado_em: 2026-07-02
tags: [changelog, obsidian, pkm, jardim-digital, graph-view]
---

# 2026-07-02 - Jardinagem Obsidian v0

## Mudancas

- Criado auditor local de jardinagem: `60_Sistemas/Obsidian/scripts/auditar_jardim_obsidian.py`.
- Gerada auditoria: [[50_Registros/Auditoria/Jardinagem_Obsidian_2026-07-02]].
- Criados hubs ponte:
  - [[40_Wiki/FabioOS/PietraOS]];
  - [[40_Wiki/Modelos_e_IAs/Matriz_de_Aptidao_das_IAs_FabioOS]];
  - [[40_Wiki/LLM_Wiki/LLM_Wiki_Pattern]].
- Adicionado frontmatter/status a READMEs centrais:
  - [[40_Wiki/FabioOS/README]];
  - [[40_Wiki/_MOCs/README]];
  - [[40_Wiki/LLM_Wiki/README]];
  - [[40_Wiki/Modelos_e_IAs/README]];
  - [[80_Specs/MEGATRON/README]].
- Corrigidos links de hubs vivos que apontavam para `90_Arquivo`.
- Atualizados MOCs e dashboards para apontar para notas vivas.

## Metricas

Recorte correto do vault, ignorando `.git`, `.claude`, `.agents`, `.codex`, `.obsidian`, `apps`, `node_modules`, `.venv` e `90_Arquivo`:

| Metrica | Antes | Depois |
|---|---:|---:|
| Notas auditadas | 707 | 710 |
| Sem frontmatter | 92 | 87 |
| Frontmatter sem status | 75 | 75 |
| Wikilinks quebrados | 529 | 504 |
| Candidatos a no solto | 86 | 86 |

## Decisao

Nao executar correcao massiva automatica. A jardinagem deve seguir por lotes:

1. hubs e dashboards;
2. MOCs;
3. `40_Wiki`;
4. `30_Projetos`;
5. `20_Areas`;
6. fontes/compatibilidade;
7. arquivo legado apenas como caminho textual.

## Sem runtime

- Nao houve RAG reindex.
- Nao houve API externa.
- Nao houve alteracao de tokens.
- Nao houve push.
