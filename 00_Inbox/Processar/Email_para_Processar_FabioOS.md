---
tipo: inbox
area: 00_Inbox
projeto: FabioOS
status: em-processamento
tags: [fabios, inbox, email, memoria]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
---

# Email para Processar - FabioOS

## Estado

O primeiro lote de e-mails ja foi processado e convertido em conhecimento visivel no Obsidian.

Em 2026-07-01 foi criado o intake local em dry-run:

- [[60_Sistemas/FabioOS/specs/2026-07-01_email-intake-dry-run]]
- [[50_Registros/Relatorios/Diagnostico_Modulo_Email_Agente_Pessoal_Perfeito_2026-07-01]]

Ele nao le Gmail sozinho, mas transforma payload autorizado do conector/n8n em
triagem restrita, sem envio, sem apagar, sem arquivar e sem RAG.

## Processados

- [[40_Wiki/_compat_wiki/memoria/decisoes/2026-06-27_Piloto_Email_Protocolos_FabioOS]]
- [[40_Wiki/_compat_wiki/memoria/decisoes/2026-06-27_Email_Anthropic_Privacidade_Claude]]
- [[40_Wiki/_compat_wiki/memoria/projetos/2026-06-27_GitHub_Actions_Auto_Changelog_Falhas]]

## A processar

- [ ] Uma thread externa real escolhida por Fabio.
- [ ] E-mails com prazos, pessoas, instituicoes ou anexos relevantes.
- [ ] Gmail profissional somente apos autorizacao/conector.
- [ ] Lote real pequeno pelo `email_intake_dry_run.py` apos escopo aprovado.

## Regra

Fonte bruta de e-mail fica em `05_Raw_Sources/_compat_sources/email/_restrito/` e fora do Git. O Obsidian recebe a versao consolidada.
