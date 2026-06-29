---
tipo: mapa
area: wiki/memoria
projeto: FabioOS
status: ativo
classe_dado: Privado
tags: [fabios, memoria, gmail, google-drive, conectores]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
---

# Mapa - Conectores Google no FabioOS

## Entradas disponiveis

- Gmail pessoal: conectado em modo leitura.
- Google Drive: conectado em modo leitura.

## Notas relacionadas

- [[60_Sistemas/FabioOS/Conectores_Google_Catalogo_v0]]
- `sources/email/_restrito/2026-06-28_catalogo_gmail_pessoal.md`
- `sources/drive/_restrito/2026-06-28_catalogo_google_drive_root.md`

## Rotas de processamento

```text
Gmail/Drive
  -> catalogo restrito local
  -> triagem por dominio/permissao
  -> resumo seguro
  -> wiki/memoria ou sistema especifico
  -> RAG/Grafo somente apos aprovacao
```

## Agentes envolvidos

- Inbox: identifica novas entradas e encaminha.
- Arquivista: transforma conteudo bruto em nota organizada.
- RAG: consulta apenas conteudo aprovado.
- Dashboard: mostra estado dos lotes.
- SafeCommit: impede vazamento de detalhes restritos no Git.

## Decisao

Conectores Google sao uteis agora, mas o padrao correto e metadata-first: inventariar, classificar, resumir, so depois ingerir.
