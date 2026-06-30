---
tipo: spec
area: 80_Specs
projeto: PRIMUS
status: rascunho
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, chatgpt, ingestao, spec, obsidian]
---

# SPEC - Ingestao PRIMUS a partir de ChatGPT e Fontes Locais

## Missao

Ingerir o conhecimento do PRIMUS criado em ChatGPT, arquivos locais e legado Obsidian para transformar o projeto em dominio vivo do FabioOS.

## Entradas

- Export oficial do ChatGPT quando disponivel.
- Arquivos locais em `C:\Users\user\Downloads\PRIMUS*`.
- Banco/JSON em `C:\Users\user\Desktop\Projeto\primus_out_20251230_055048`.
- Legado em `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/PRIMUS/`.

## Saidas

- Fontes normalizadas em `05_Raw_Sources/PRIMUS/`.
- Projeto vivo em `30_Projetos/PRIMUS/`.
- Wiki processada em `40_Wiki/PRIMUS/`.
- Templates e tipos em `80_Specs/PRIMUS/` ou `40_Wiki/PRIMUS/`.
- Registro de ingestao em `50_Registros/Logs_Agentes/log.md`.

## Ferramentas

- Busca local com `rg`.
- Extração controlada de DOCX/PDF quando necessario.
- Obsidian para leitura e navegacao.
- Futuro: RAG/Grafo apos triagem e aceite.

## Permissoes

- Permitido: ler arquivos locais indicados, criar notas Markdown, inventariar fontes.
- Bloqueado: copiar livros protegidos em massa, reindexar RAG, chamar API externa, publicar, enviar ou sincronizar.
- Requer aprovacao: importar ZIP/PDF/DOCX pesados, processar export completo do ChatGPT, ativar RAG/Grafo sobre PRIMUS.

## Critérios de Aceite

- Cada nota possui origem rastreavel.
- PRIMUS fica visivel em `30_Projetos/PRIMUS/` e `40_Wiki/PRIMUS/`.
- O legado nao e apagado.
- O material externo/licenciado nao vira copia longa em wiki.
- O usuario consegue abrir uma pagina central e seguir proximos passos.

## Implementacao Minima

1. Criar inventario de fontes.
2. Criar MOC do projeto.
3. Criar wiki conceitual do PrimusOS.
4. Criar notas de Circuito EIP e Taxonomia.
5. Registrar log e changelog.

## Evolucao Futura

- Parser DOCX/PDF para PRIMUS.
- Conversor PRIMUS-TAXON SQLite/JSON para notas tipadas.
- Agente `primus-lorekeeper`.
- Dashboard PRIMUS com estado de E, I, P e Delta P.
- Graph RAG narrativo separado do FabioOS central.
