---
tipo: sistema
area: 60_Sistemas
projeto: FabioOS
status: ativo
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [fabios, observabilidade, reality-check, controle-operacional]
---

# Reality Check FabioOS

## Funcao

Gerar uma leitura objetiva do estado operacional do FabioOS.

Ele responde a pergunta:

> O que nao estamos vendo enquanto construimos?

## O que verifica

- Git: commits locais a frente, worktree sujo, ultimos commits.
- Raiz do vault: itens fora da taxonomia canonica.
- Docker: containers rodando e portas publicadas.
- n8n: painel local, quantidade de workflows e mount do vault.
- Duplicata legada: `wiki/conceitos/rag.md` versus caminho canonico.

## Como executar

```powershell
python 60_Sistemas/Observabilidade/scripts/reality_check_fabioos.py
```

## Saida

Gera dois arquivos em:

```text
60_Sistemas/Observabilidade/reports/
```

- Markdown para leitura humana.
- JSON para automacao futura.

## Principio de excelencia

O FabioOS nao deve depender da memoria do operador para saber se esta saudavel.

Estado real precisa ser:

- visivel;
- repetivel;
- auditavel;
- separado de opiniao;
- sem tocar em credenciais.
