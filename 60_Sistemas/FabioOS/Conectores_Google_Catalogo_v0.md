---
tipo: catalogo-operacional
area: 60_Sistemas
projeto: FabioOS
status: implementado
classe_dado: Privado
tags: [fabios, gmail, google-drive, conectores, catalogacao, obsidian]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
---

# Conectores Google - Catalogo v0

## Resultado

Os conectores Gmail e Google Drive foram usados com sucesso em modo leitura. Esta nota e o resumo versionavel. Os detalhes com nomes de arquivos, metadados de conta, consultas e amostras ficam em:

- `sources/email/_restrito/2026-06-28_catalogo_gmail_pessoal.md`
- `sources/drive/_restrito/2026-06-28_catalogo_google_drive_root.md`

Essas pastas sao visiveis no Obsidian local, mas ficam fora do Git.

## Gmail

Estado observado:

- Conta pessoal conectada.
- Inbox com volume alto.
- Muitos nao lidos.
- Categorias com maior volume: Updates, Promotions, Personal.
- Existe volume pequeno de Spam, que nao deve entrar em qualquer ingestao.
- Leitura de amostra confirmou que newsletters podem gerar muito ruido e nao devem virar memoria automaticamente.

Decisao:

- Gmail nao entra em RAG/Grafo por padrao.
- Primeiro fluxo sera triagem por lotes pequenos.
- O agente Inbox deve separar: acao, pessoa, projeto, financeiro, escola, newsletter, descartavel.

## Google Drive

Estado observado:

- Raiz do Drive acessivel.
- Foram encontrados documentos escolares/profissionais, uma pasta de projeto, PDFs financeiros, boletos, CSVs e documentos sem titulo.
- PDFs financeiros e boletos sao classe Critico e nao devem ser enviados a modelos externos nem ingeridos automaticamente.
- Documentos escolares podem alimentar Sistema Escola apos triagem.
- Pasta/projeto relacionado a Primus deve ser tratado como conhecimento de projeto.

## Politica operacional

| Tipo | Acao imediata |
|---|---|
| Newsletter/promocional | catalogar como ruido; nao ingerir |
| E-mail pessoal | triagem humana antes de resumo |
| E-mail de projeto | resumo seguro em `wiki/memoria/projetos/` |
| Documento escolar | encaminhar para Sistema Escola |
| PDF financeiro/boleto | manter restrito; nao enviar a modelo externo |
| Documento sem titulo | catalogar, depois renomear/classificar manualmente |

## Proxima implementacao recomendada

Criar `catalogador_google_fabioos.py` somente como gerador de notas locais a partir de exportacoes seguras. Como os conectores Gmail/Drive vivem no Codex, a automacao completa deve ser feita por agente/conector, nao por script que tente recriar OAuth manualmente.
