---
tipo: inventario
area: 60_Sistemas
projeto: FabioOS
status: rascunho
tags: [fabios, memoria, gmail, chatgpt, inventario]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Inventario - Memoria Pessoal e Profissional

## Escopo desta verificacao

Inventario nao destrutivo feito em 2026-06-27 durante o interinato Codex.

Foi verificado apenas o Gmail pessoal conectado ao Codex:

- conta: `fabiorabelo.j@gmail.com`;
- metodo: busca por IDs/metadados;
- corpo de e-mail: nao lido;
- anexos: nao lidos;
- acoes de escrita: nenhuma;
- conteudo salvo do Gmail: nenhum.

Atualizacao no interinato:

- conector Gmail confirmado por leitura de perfil da conta conectada;
- nenhuma mensagem foi listada ou aberta nesta checagem;
- nenhum anexo foi lido;
- nenhuma acao de escrita foi executada.

## Resultado inicial

| Fonte/filtro | Resultado | Observacao |
|---|---:|---|
| Gmail pessoal, ultimos 30 dias sem promocoes/spam/lixeira | pelo menos 10 mensagens | ha paginacao; volume maior que a amostra |
| Gmail pessoal, marcados com estrela | pelo menos 10 mensagens | bom candidato para primeiro lote humano |
| Gmail pessoal, ultimos 365 dias com `FabioOS OR MEGATRON OR Codex OR Claude` | pelo menos 10 mensagens | candidato direto para memoria do sistema |
| Gmail pessoal, ultimos 365 dias com anexos | pelo menos 10 mensagens | exige cuidado por dados pessoais e arquivos sensiveis |

## Fontes ainda pendentes

- ChatGPT: Codex nao tem acesso direto ao historico. Caminho recomendado: exportacao oficial do ChatGPT e ingestao do `.zip` local.
- Gmail de trabalho: conta informada como `fabiofilosofia@colegiopietra.com.br`; nao foi acessada. Antes de qualquer leitura, pedir autorizacao explicita e configurar conector/exportacao.
- Claude/Codex/OpenClaw: ja existem changelogs e handoffs no vault; usar esses artefatos antes de logs brutos.

## Recomendacao

Comecar por um piloto pequeno:

1. Gmail pessoal: ler somente 10 mensagens estreladas ou 10 mensagens relacionadas a FabioOS/MEGATRON.
2. ChatGPT: importar exportacao oficial, mas processar por conversa, nao como bloco unico.
3. Trabalho: aguardar conector/conta autorizada.
4. Salvar primeiro como fontes `restrito` ou `nao-indexar`; promover para RAG apenas apos revisao.

## Riscos

- Expor dados de terceiros.
- Indexar credenciais ou links privados.
- Misturar vida pessoal com base sem filtros.
- Aumentar custo de RAG/OpenClaw por excesso de contexto irrelevante.

## Decisao operacional

Nao executar ingestao em massa sem um filtro aprovado por Fabio.
