---
tipo: protocolo
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [seguranca, tokens, credenciais, privacidade, commit]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Protocolo de Seguranca FabioOS

## Regras absolutas

- Nenhuma chave em Markdown.
- Nenhum token no Git.
- Nenhum `.env` versionado.
- Nenhuma senha em prompt.
- Nenhuma credencial em changelog.
- Nenhum envio externo sem aprovacao.
- Nenhuma acao destrutiva sem aprovacao.

## Dados sensiveis

Tratar como sensivel:

- dados escolares, alunos, responsaveis e notas;
- dados financeiros, corretoras e operacoes;
- documentos pessoais;
- emails e WhatsApp;
- tokens, cookies, chaves e senhas;
- dados de terceiros.

## Antes de qualquer commit

Checklist:

- [ ] Rodar scan de segredos.
- [ ] Verificar `.gitignore`.
- [ ] Conferir arquivos staged explicitamente.
- [ ] Confirmar que `.env`, tokens e configs locais nao entram.
- [ ] Revisar diffs de arquivos novos.
- [ ] Conferir se ha dados escolares/financeiros.
- [ ] Atualizar changelog sem expor segredo.

## Politica de modelo externo

Nao enviar dados privados, restritos ou criticos para modelo externo sem:

1. classificacao de dados;
2. finalidade;
3. aprovacao humana;
4. minimizacao do contexto;
5. registro do envio.

## Ambientes

| Ambiente | Regra |
|---|---|
| Local | pode conter config privada gitignored |
| Vault/Git | nao pode conter segredo |
| GitHub | somente conteudo versionavel e seguro |
| Cloud/API | somente com aprovacao e custo definido |

## Relacoes

- [[60_Sistemas/Governanca/Matriz_de_Permissoes_FabioOS]]
- [[60_Sistemas/FabioOS/Matriz_Dominios_Dados_Permissoes_2026-06-28]]
- [[60_Sistemas/MEGATRON/agentes/specs/Agente_SafeCommit]]
