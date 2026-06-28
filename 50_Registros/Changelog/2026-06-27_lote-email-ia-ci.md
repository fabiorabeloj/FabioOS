---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: concluido
tags: [changelog, email, gmail, anthropic, github-actions, memoria]
criado_em: 2026-06-27
atualizado_em: 2026-06-27
---

# Changelog - Lote Email IA/CI

## O que foi feito

- Processadas 3 threads Gmail do filtro FabioOS/MEGATRON/Codex/Claude.
- Nenhum e-mail foi enviado, arquivado, apagado ou rotulado.
- Nenhum anexo foi lido.
- Fontes restritas locais foram criadas em `sources/email/_restrito/` e continuam fora do Git.
- Conteudo seguro foi consolidado em notas de memoria.

## Notas criadas

- `wiki/memoria/decisoes/2026-06-27_Email_Anthropic_Privacidade_Claude.md`
- `wiki/memoria/projetos/2026-06-27_GitHub_Actions_Auto_Changelog_Falhas.md`

## Achados

- Anthropic comunicou mudancas de privacidade relevantes para conectores, dados e uso de conversas.
- GitHub Actions `Auto Changelog` falhou em duas execucoes no `main`.
- Links de notificacao do GitHub tinham parametros `email_token` e foram sanitizados.

## Proximas acoes

1. Investigar workflow `Auto Changelog` em frente separada.
2. Criar matriz de privacidade por provedor IA.
3. Escolher uma thread externa real para validar pessoas, prazos e anexos.
