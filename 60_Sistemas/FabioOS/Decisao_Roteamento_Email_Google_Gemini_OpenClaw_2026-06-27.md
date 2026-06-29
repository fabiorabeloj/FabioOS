---
tipo: decisao-operacional
area: 60_Sistemas
projeto: FabioOS
status: rascunho
tags: [fabios, email, gmail, google, gemini, openclaw, memoria]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Decisao - Roteamento de E-mails, Google, Gemini e OpenClaw

## Pergunta

E cabivel usar OpenClaw ou avaliar Gemini agora para executar o protocolo de conversao de e-mails e absorcoes futuras do FabioOS?

## Decisao curta

Sim, e cabivel preparar a estrutura agora, mas **nao e cabivel executar ingestao real de e-mails em massa ainda**.

A rota recomendada e:

1. **Gmail/Google Drive connectors** para acesso controlado a e-mails e arquivos Google.
2. **FabioOS/Codex** para converter o conteudo em notas Obsidian, tarefas, decisoes e memoria permanente.
3. **OpenClaw Workboard** para visualizacao, locks, status e supervisao humana.
4. **Gemini** como motor opcional de analise em uma fase posterior, principalmente para conteudo Google-native, anexos multimodais ou lotes grandes.

## Por que nao usar Gemini como primeira camada agora

- E-mail pessoal/profissional tem dados sensiveis e dados de terceiros.
- O FabioOS ja possui conectores Gmail/Google Drive no Codex, com regras de leitura e seguranca.
- OpenClaw ja esta operacional como painel e ponte visual.
- Gemini acrescenta custo, superficie de privacidade e mais uma credencial/API para governar.
- Antes de qualquer modelo externo, o FabioOS precisa de filtro: escopo, periodo, conta, tipo de conteudo e politica de `nao-indexar`.

## Quando Gemini faz sentido

Gemini deve ser considerado quando houver:

- grande volume de documentos Google-native;
- anexos multimodais que exijam boa leitura de imagem, PDF, slide ou planilha;
- necessidade de usar recursos nativos do ecossistema Google;
- lote controlado ja filtrado e sem credenciais;
- limite de custo definido no painel da API/Google Cloud/OpenRouter.

## Avaliacao Gemini em 2026-06-27

Fontes oficiais consultadas:

- Gemini API pricing: `https://ai.google.dev/gemini-api/docs/pricing`
- Gemini API terms: `https://ai.google.dev/gemini-api/terms`
- Google Cloud data governance for Gemini: `https://docs.cloud.google.com/gemini/docs/discover/data-governance`
- Google Workspace with Gemini: `https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini/google-workspace-with-gemini`

Resumo:

- A API Gemini tem modelos com camada gratuita e camada paga por tokens; modelos leves podem ficar na faixa de centavos por milhao de tokens, enquanto modelos Pro sobem bastante em entradas e saidas grandes.
- Google Workspace inclui Gemini em Gmail, Docs, Drive e outros apps conforme o plano/subscricao.
- Para uso com dados profissionais, o caminho mais governavel e via Google Cloud/Workspace, com termos e processamento de dados empresariais.
- Para o FabioOS, Gemini deve ser uma etapa posterior: primeiro filtrar, classificar e reduzir os dados com conectores Gmail/Drive e politicas do vault.

## Quando OpenClaw faz sentido

OpenClaw deve ser usado agora para:

- mostrar cards das frentes ativas;
- sinalizar se a ingestao de memoria esta `todo`, `running`, `review` ou `done`;
- registrar riscos e bloqueios;
- evitar que Claude/Codex atuem no mesmo artefato sem lock;
- permitir que Fabio visualize o trabalho sem abrir todos os arquivos.

OpenClaw nao deve:

- ler e-mail automaticamente sem escopo aprovado;
- enviar WhatsApp/e-mail;
- guardar tokens;
- operar como autorizacao implicita para acoes externas.

## Protocolo operacional para um e-mail especifico

Antes de ler um e-mail, o agente deve registrar:

1. Conta: pessoal ou trabalho.
2. Identificador: link, remetente+assunto, busca Gmail, ou ID.
3. Escopo: thread inteira ou mensagem unica.
4. Anexos: ler ou ignorar; quais tipos.
5. Destino: `05_Raw_Sources/_compat_sources/email/pessoal`, `05_Raw_Sources/_compat_sources/email/trabalho`, `05_Raw_Sources/_compat_sources/email/_restrito` ou `40_Wiki/_compat_wiki/memoria`.
6. Indexacao: `nao-indexar` por padrao ate revisao.

Saida esperada:

- resumo executivo;
- pessoas e instituicoes;
- datas, prazos, eventos e compromissos;
- decisoes;
- tarefas executaveis;
- riscos;
- links e anexos;
- sugestao de notas Obsidian;
- relacao com projetos e areas do FabioOS.

## Protocolo para absorcao futura em lote

1. Inventario sem ler corpo profundo.
2. Amostra pequena autorizada.
3. Classificacao por sensibilidade.
4. Conversao para `05_Raw_Sources/_compat_sources/` com frontmatter.
5. Transformacao para `40_Wiki/_compat_wiki/memoria/`.
6. Revisao humana.
7. So depois promocao para RAG/Grafo.

## Estado em 2026-06-27

- Gmail pessoal ja aparece no inventario como conectado; a capacidade foi confirmada por leitura de perfil, sem abrir mensagens.
- Gmail de trabalho precisa de autorizacao/conexao explicita.
- ChatGPT exige exportacao oficial local.
- OpenClaw Workboard esta operacional.
- Gemini fica como avaliacao futura, nao como executor padrao imediato.

## Proxima acao recomendada

Executar um **piloto manual pequeno**:

1. Fabio escolhe uma unica thread de e-mail.
2. Codex usa conector Gmail apenas para essa thread.
3. A saida fica primeiro em `05_Raw_Sources/_compat_sources/email/_restrito/`.
4. Depois o resumo consolidado vai para `40_Wiki/_compat_wiki/memoria/`.
5. Nada entra no RAG sem revisao.
