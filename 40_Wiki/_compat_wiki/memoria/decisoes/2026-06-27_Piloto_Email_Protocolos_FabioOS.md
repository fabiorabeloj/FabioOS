---
tipo: decisao
area: wiki
projeto: FabioOS
status: revisar
tags: [fabios, memoria, email, gmail, governanca, openclaw]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
fonte: sources/email/_restrito/2026-06-27_piloto_gmail_protocolos_fabioos.md
indexacao: revisar
---

# Piloto Email - Protocolos FabioOS

## Resumo

Foi executado um piloto controlado de conversao de e-mail para memoria do FabioOS usando uma thread do Gmail pessoal enviada por Fabio para si mesmo. A thread continha protocolos e diretrizes para retomada de ambiente, coordenacao multiagente, limpeza segura, conversao de e-mails e absorcao integral de conhecimento.

## Decisao

O conteudo nao deve ser copiado integralmente para notas versionadas. A forma correta e consolidar o conhecimento em documentos canonicos do FabioOS e manter a fonte restrita fora do Git.

## Conhecimento consolidado

- [[60_Sistemas/FabioOS/Protocolo_Retomada_Ambiente_FabioOS]]
- [[60_Sistemas/FabioOS/Protocolo_Gestao_Contexto_IA]]
- [[60_Sistemas/FabioOS/Protocolo_Limpeza_Segura_FabioOS_PC]]
- [[60_Sistemas/FabioOS/Protocolo_Ingestao_Memoria_Pessoal_Profissional]]
- [[60_Sistemas/FabioOS/Decisao_Roteamento_Email_Google_Gemini_OpenClaw_2026-06-27]]

## Tarefas geradas

| Tarefa | Prioridade | Prazo | Dependencias | Contexto |
|---|---|---|---|---|
| Manter fontes de e-mail sensiveis fora do Git | alta | imediato | `.gitignore` | Evita publicar conteudo pessoal ou IDs privados |
| Validar se a memoria consolidada pode entrar no RAG/Grafo | media | apos revisao | revisao humana | A fonte bruta permanece `nao-indexar` |
| Repetir piloto com uma thread externa real | media | quando Fabio escolher | thread especifica | Testa pessoas, prazos, anexos e decisoes reais |
| Definir politica para Gmail de trabalho | alta | antes de qualquer acesso | autorizacao/conector | Evita mistura de dados pessoais e institucionais |

## Riscos

- Duplicar protocolos ja existentes.
- Versionar fonte pessoal por engano.
- Promover conteudo para RAG antes de revisar sensibilidade.
- Usar Gemini ou outro modelo externo antes de filtrar dados.

## Proximo passo

Fabio escolhe uma thread externa real para o segundo piloto, ou autoriza apenas um filtro restrito com ate 3 mensagens para triagem.
