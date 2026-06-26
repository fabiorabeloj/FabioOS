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

Estrutura completa de ingestão do FabioOS: 7 subpastas em `sources/`, 5 comandos slash de captura e normalização, e README atualizado com fluxo completo.

## Arquivos criados

### Subpastas em sources/ (com .gitkeep para versionamento)

| Pasta | Função |
|---|---|
| `sources/web/` | Páginas web e links capturados via /ingest-url |
| `sources/docs/` | Documentos locais via /ingest-doc |
| `sources/pdfs/` | PDFs via /ingest-pdf |
| `sources/drive/` | Google Docs/Drive (comandos futuros) |
| `sources/research/` | Relatórios externos e outputs do Manus |
| `sources/extracted/` | Texto extraído de PDFs/DOCX para Markdown |
| `sources/_inbox/` | Entrada bruta não classificada |

### Comandos slash (.claude/commands/)

| Comando | Função |
|---|---|
| `/ingest-url` | Captura URL com playwright-mcp, preserva em sources/web/ |
| `/ingest-pdf` | Preserva PDF (ou texto extraído) em sources/pdfs/ |
| `/ingest-doc` | Processa DOCX/TXT/conteúdo colado em sources/docs/ |
| `/normalize-source` | Padroniza frontmatter e estrutura de fontes brutas |
| `/check-source-quality` | Avalia fonte em 10 pontos antes de transformar em wiki |

## Arquivos atualizados

- `sources/README.md` — reescrito com estrutura completa, fluxo, convenções e índice
- `wiki/indices/mapa-fabios.md` — fase 7.5 concluída, próxima: 9 (Pietra)
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

- [[sources/README]]
- [[schema/fluxo-wiki]]
- [[60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS]]
- [[50_Registros/Changelog/2026-06-26_fase8-sistema-escola]]
