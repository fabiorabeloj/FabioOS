---
tipo: changelog
area: registros
projeto: FabioOS
status: concluído
fase: 7.5
tags: [changelog, fase-7.5, ingestão, sources, comandos]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Changelog — Fase 7.5: Ingestão Externa

## Resumo

Estrutura completa de ingestão do FabioOS: 7 subpastas em `05_Raw_Sources/_compat_sources/`, 5 comandos slash de captura e normalização, e README atualizado com fluxo completo.

## Arquivos criados

### Subpastas em 05_Raw_Sources/_compat_sources/ (com .gitkeep para versionamento)

| Pasta | Função |
|---|---|
| `05_Raw_Sources/_compat_sources/web/` | Páginas web e links capturados via /ingest-url |
| `05_Raw_Sources/_compat_sources/docs/` | Documentos locais via /ingest-doc |
| `05_Raw_Sources/_compat_sources/pdfs/` | PDFs via /ingest-pdf |
| `05_Raw_Sources/_compat_sources/drive/` | Google Docs/Drive (comandos futuros) |
| `05_Raw_Sources/_compat_sources/research/` | Relatórios externos e outputs do Manus |
| `05_Raw_Sources/_compat_sources/extracted/` | Texto extraído de PDFs/DOCX para Markdown |
| `05_Raw_Sources/_compat_sources/_inbox/` | Entrada bruta não classificada |

### Comandos slash (.claude/commands/)

| Comando | Função |
|---|---|
| `/ingest-url` | Captura URL com playwright-mcp, preserva em 05_Raw_Sources/_compat_sources/web/ |
| `/ingest-pdf` | Preserva PDF (ou texto extraído) em 05_Raw_Sources/_compat_sources/pdfs/ |
| `/ingest-doc` | Processa DOCX/TXT/conteúdo colado em 05_Raw_Sources/_compat_sources/docs/ |
| `/normalize-source` | Padroniza frontmatter e estrutura de fontes brutas |
| `/check-source-quality` | Avalia fonte em 10 pontos antes de transformar em wiki |

## Arquivos atualizados

- `05_Raw_Sources/_compat_sources/README.md` — reescrito com estrutura completa, fluxo, convenções e índice
- `40_Wiki/_compat_wiki/indices/mapa-fabios.md` — fase 7.5 concluída, próxima: 9 (Pietra)
- `60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS.md` — fase 7.5 marcada concluída

## Inventário completo de comandos (.claude/commands/)

| Comando | Sistema |
|---|---|
| `/archive-source` | FabioOS — arquivar fonte manual |
| `/source-to-wiki` | FabioOS — transformar fonte em wiki |
| `/update-index` | FabioOS — atualizar mapa |
| `/check-secrets` | Segurança |
| `/session-changelog` | FabioOS |
| `/safe-commit` | Git |
| `/criar-prova` | Escola |
| `/criar-revisao` | Escola |
| `/criar-gabarito` | Escola |
| `/criar-comunicado` | Escola |
| `/ingest-url` | Ingestão — web |
| `/ingest-pdf` | Ingestão — PDF |
| `/ingest-doc` | Ingestão — documento |
| `/normalize-source` | Ingestão — normalização |
| `/check-source-quality` | Ingestão — avaliação |

**Total: 15 comandos ativos**

## Pendências (Fase 14+)

- `/ingest-drive-doc` — depende de MCP Google Drive (Fase 20)
- `/ingest-repo` — usar `/archive-source` por enquanto

## Próxima fase

**Fase 9 — Sistema Pietra**

## Relações

- [[05_Raw_Sources/_compat_sources/README]]
- [[60_Sistemas/Wiki/schema/fluxo-wiki]]
- [[60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS]]
- [[50_Registros/Changelog/2026-06-26_fase8-sistema-escola]]
