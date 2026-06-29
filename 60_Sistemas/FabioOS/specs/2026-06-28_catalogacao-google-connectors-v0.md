---
tipo: spec
area: 60_Sistemas
projeto: FabioOS
status: implementado
fase: catalogacao-google-v0
dominio: FabioOS
classe_dado: Privado/Restrito
permissao: leitura por conector; resumo seguro versionavel; detalhe restrito fora do Git
criado_em: 2026-06-28
atualizado_em: 2026-06-28
tags: [fabios, spec, gmail, google-drive, conectores, catalogacao]
---

# SPEC - Catalogacao Google Connectors v0

## 1. Problema

Gmail e Google Drive estavam conectados, mas nao havia uma forma visivel no Obsidian de provar o que foi inventariado, quais riscos existem e quais proximos lotes podem ser processados.

## 2. Objetivo

Criar uma catalogacao inicial segura de Gmail e Google Drive usando os conectores do Codex, separando resumo versionavel de detalhe local/restrito.

## 3. Fora de escopo

- Arquivar, apagar, enviar ou rotular e-mails.
- Baixar anexos.
- Exportar documentos completos.
- Enviar conteudo a modelo externo.
- Ingerir automaticamente em RAG/Grafo.

## 4. Dominio, dados e permissoes

| Campo | Valor |
|---|---|
| Dominio | FabioOS / memoria pessoal-profissional |
| Classe de dado | Privado/Restrito |
| RAG | somente apos triagem e resumo seguro |
| Grafo | somente metadados aprovados |
| Modelo externo/API | nao usar na v0 |
| Aprovacao humana | obrigatoria para conteudo integral, anexos, finanças, documentos pessoais e qualquer envio externo |

## 5. Arquitetura proposta

```text
Gmail/Drive connector
  -> inventario de metadados
  -> detalhe local em sources/*/_restrito/
  -> resumo seguro versionavel
  -> mapa Obsidian
  -> triagem posterior para wiki/RAG/Grafo
```

## 6. Plano de tarefas

- [x] Verificar conector Gmail.
- [x] Verificar conector Google Drive.
- [x] Obter contagens/rotulos do Gmail sem modificar mensagens.
- [x] Listar raiz do Drive sem baixar conteudo.
- [x] Criar resumo seguro versionavel.
- [x] Criar arquivos detalhados em area restrita ignorada pelo Git.
- [x] Atualizar dashboard e changelog.

## 7. Criterios de aceite

- [x] Existe uma nota versionavel explicando o estado dos conectores.
- [x] Existem catalogos locais/restritos no Obsidian.
- [x] Nenhum e-mail foi enviado, apagado, arquivado ou rotulado.
- [x] Nenhum documento integral foi exportado.
- [x] Nenhum conteudo foi enviado para API externa.

## 8. Testes minimos

- [x] `gmail.get_profile`.
- [x] `gmail.list_labels`.
- [x] `gmail.search_email_ids` com filtro seguro.
- [x] `google_drive.list_folder root`.
- [x] Confirmar `.gitignore` para `sources/drive/_restrito/`.

## 9. Riscos

| Risco | Mitigacao |
|---|---|
| Conteudo privado entrar no Git | detalhes ficam em `_restrito/` ignorado |
| Ingestao excessiva de e-mail | lotes pequenos e escopo aprovado |
| PDF financeiro entrar no RAG | classe Critico; nao ingerir automaticamente |
| Modelo externo receber dado sensivel | bloqueado na v0 |

## 10. Rollback

Manter o resumo versionavel e remover/revisar manualmente os arquivos locais em `_restrito/` caso Fabio nao queira preservar o inventario detalhado.

## 11. Changelog esperado

Registrar `50_Registros/Changelog/2026-06-28_catalogacao-google-connectors-v0.md`.
