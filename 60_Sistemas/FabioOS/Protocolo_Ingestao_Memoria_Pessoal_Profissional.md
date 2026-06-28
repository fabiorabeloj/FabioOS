---
tipo: protocolo
area: 60_Sistemas
projeto: FabioOS
status: rascunho
tags: [fabios, memoria, chatgpt, gmail, ingestao, privacidade]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Protocolo de Ingestao - Memoria Pessoal e Profissional

## Missao

Absorver para dentro do FabioOS o conhecimento produzido em conversas de IA, e-mails pessoais e e-mails de trabalho sem transformar privacidade, ruido ou credenciais em passivo operacional.

A meta nao e copiar tudo cegamente. A meta e converter informacao em memoria util: decisoes, projetos, compromissos, ideias, relacoes, aprendizados, documentos, perguntas recorrentes e contexto de longo prazo.

## Principios

1. **Consentimento por fonte**: cada conta, exportacao ou pasta precisa ser autorizada.
2. **Minimizacao**: preservar o necessario; resumir quando o bruto for sensivel.
3. **Separacao bruto/processado**: fontes em `sources/`; conhecimento consolidado em `wiki/`.
4. **Nao vazar segredos**: tokens, senhas, chaves, links privados e dados sensiveis nao entram no RAG sem filtro.
5. **Rastreabilidade**: toda nota processada deve apontar para fonte, data e criterio de selecao.
6. **Direito ao esquecimento**: qualquer fonte pode ser marcada como `restrito`, `nao-indexar` ou removida mediante decisao humana.

## Fontes previstas

| Fonte | Estado | Metodo preferido | Observacao |
|---|---|---|---|
| ChatGPT | pendente | exportacao oficial em `.zip`/`.json` ou copia controlada | Codex nao tem acesso direto ao historico do ChatGPT sem exportacao/local |
| Gmail pessoal | conectado | Gmail connector, buscas por escopo | Conta detectada: `fabiorabelo.j@gmail.com` |
| Gmail trabalho | pendente | pedir autorizacao explicita para conectar `fabiofilosofia@colegiopietra.com.br` ou exportar dados | Nao assumir acesso; conta apenas informada, nao acessada |
| Claude/Codex/OpenClaw | parcial | changelogs, handoffs e logs selecionados | Priorizar resumos e decisoes, nao logs brutos gigantes |

## Estrutura de pastas

```text
sources/
  chatgpt/
    exports/
    conversas/
    _restrito/
  email/
    pessoal/
    trabalho/
    _restrito/
wiki/
  memoria/
    pessoas/
    projetos/
    decisoes/
    ideias/
    compromissos/
```

## Camadas de ingestao

### Camada 0 - Inventario

Listar fontes, contas, periodo, volume aproximado e sensibilidade. Nao ler conteudo profundo nesta etapa.

Saida esperada:

- conta/fonte;
- periodo coberto;
- categorias provaveis;
- risco de privacidade;
- recomendacao de ingestao.

### Camada 1 - Amostra controlada

Ler uma amostra pequena por fonte, por exemplo:

- ultimos 10 e-mails importantes;
- threads com estrela;
- conversas ChatGPT exportadas com titulos relevantes;
- documentos explicitamente indicados por Fabio.

Saida esperada:

- resumo;
- topicos recorrentes;
- risco;
- decisao: arquivar bruto, resumir, ignorar, ou marcar restrito.

### Camada 2 - Triagem tematica

Agrupar por:

- FabioOS/MEGATRON;
- trabalho;
- escola/aulas;
- financas;
- familia/pessoal;
- saude;
- ideias e projetos;
- contas, acessos e operacao.

Dados de alta sensibilidade devem ficar fora do RAG por padrao.

### Camada 3 - Fonte normalizada

Criar notas em `sources/` com frontmatter:

```yaml
---
tipo: fonte
origem: chatgpt|gmail-pessoal|gmail-trabalho|outro
capturado_em: YYYY-MM-DD
periodo: YYYY-MM-DD/YYYY-MM-DD
status: bruto|processado|restrito|nao-indexar
sensibilidade: baixa|media|alta
tags: []
---
```

### Camada 4 - Conhecimento consolidado

Transformar fontes relevantes em notas `wiki/memoria/` com:

- fatos;
- decisoes;
- pessoas e entidades;
- projetos relacionados;
- proximas acoes;
- links para fontes.

### Camada 5 - RAG/Grafo

So entram no RAG/Grafo:

- fontes `processado`;
- sensibilidade `baixa` ou `media`;
- sem segredos;
- sem dados pessoais desnecessarios de terceiros;
- com origem rastreavel.

## Regras especificas para e-mail

1. Nao arquivar caixa inteira em bruto.
2. Comecar por buscas direcionadas:
   - `newer_than:30d -category:promotions -in:spam -in:trash`
   - `is:starred`
   - `from:...` ou `subject:...` por projeto.
3. Nunca enviar, arquivar, apagar, marcar ou responder e-mail sem ordem explicita.
4. Quando houver dados de terceiros, preferir resumo a copia integral.
5. Anexos exigem aprovacao por tipo e por pasta.

### Conversao de um e-mail especifico

Quando Fabio indicar uma thread ou mensagem especifica, converter o e-mail em conhecimento seguindo:

1. leitura integral da mensagem autorizada e do contexto da thread;
2. leitura de anexos apenas quando explicitamente permitido;
3. extracao de objetivo, resumo executivo, pessoas, instituicoes, datas, prazos, eventos, decisoes, solicitacoes, pendencias, links, arquivos citados, riscos e prioridades;
4. geracao de tarefas com descricao, prioridade, prazo, dependencias e contexto;
5. escolha do destino no vault, preferindo `sources/email/_restrito/` para bruto sensivel e `wiki/memoria/` para conhecimento consolidado;
6. criacao de Markdown com frontmatter, links internos, tags e referencias cruzadas;
7. verificacao de duplicacao antes de criar novas notas;
8. classificacao como conhecimento permanente, documentacao, decisao, projeto, procedimento, reuniao, tarefa, referencia futura ou material temporario.

Saida obrigatoria:

- nome do arquivo;
- pasta sugerida;
- conteudo Markdown;
- links internos;
- tags;
- relacoes com outras notas;
- tarefas e proximos passos.

Por padrao, e-mails convertidos ficam `nao-indexar` ate revisao humana.

## Roteamento de ferramentas

| Ferramenta | Uso recomendado | Limite |
|---|---|---|
| Gmail connector | Buscar e ler e-mail/thread autorizada | Nao enviar, arquivar, apagar ou rotular sem ordem explicita |
| Google Drive connector | Buscar e ler Docs, Sheets, Slides e anexos no Drive | Nao mover, compartilhar ou apagar sem ordem explicita |
| OpenClaw | Visualizar frentes, riscos, locks e progresso | Nao e autorizacao para agir em contas externas |
| Gemini | Motor opcional para lotes Google-native ou anexos multimodais | Usar so com custo, privacidade e escopo aprovados |

## Regras especificas para ChatGPT

1. Preferir exportacao oficial do ChatGPT.
2. Preservar o arquivo bruto exportado em `sources/chatgpt/exports/` apenas se o usuario aprovar.
3. Processar conversas por titulo/data, nao como bloco unico.
4. Marcar conversas sensiveis como `restrito` ou `nao-indexar`.
5. Extrair principalmente:
   - decisoes;
   - prompts uteis;
   - arquitetura do FabioOS;
   - ideias recorrentes;
   - perguntas ainda abertas.

## Primeiro lote recomendado

1. Gmail pessoal: inventario nao destrutivo da conta conectada.
2. ChatGPT: usuario exporta historico e informa o caminho do `.zip`.
3. Gmail trabalho: pedir autorizacao explicita antes de conectar `fabiofilosofia@colegiopietra.com.br` ou exportar dados.
4. Criar uma nota `wiki/memoria/Mapa_Memoria_Fabio.md` so com categorias e links, sem conteudo sensivel.

## Criterios de aceite

- Nenhum token, senha ou chave real entra no vault.
- Nenhum e-mail e enviado, apagado, arquivado ou rotulado.
- Todo item ingerido tem origem e data.
- Itens sensiveis ficam fora do RAG por padrao.
- Fabio consegue ver o que foi absorvido e desfazer a inclusao.

## Prompt operacional

Antes de ingerir memoria pessoal/profissional, o agente deve responder:

1. Qual fonte sera acessada?
2. Qual periodo e filtro?
3. Sera lido corpo integral ou apenas metadados/resumos?
4. Onde sera salvo?
5. O conteudo entra ou nao entra no RAG?

Sem essas cinco respostas, nao executar ingestao em massa.
