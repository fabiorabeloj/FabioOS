---
tipo: sistema
area: 60_Sistemas
projeto: FabioOS
sistema: n8n
workflow: FabioOS_SPEC_Plano_Execucao
status: importado-inativo
data: 2026-06-29
tags: [fabios, n8n, spec-driven, autoconstrucao, excelencia]
---

# Workflow: FabioOS - SPEC para Plano de Execucao

## Objetivo

Transformar uma SPEC ou ideia estruturada em plano de execucao auditavel.

Este workflow existe para a autoconstrucao do FabioOS: antes de construir, o sistema verifica se a demanda tem objetivo, fora de escopo, criterios de aceite, testes, riscos, donos e limites.

## Por que isso importa

O FabioOS nao deve crescer por impulso.

Cada nova capacidade precisa passar por:

- clareza de objetivo;
- criterio de aceite;
- permissao;
- dono;
- teste;
- changelog;
- rollback.

## Endpoint

```text
POST http://127.0.0.1:5678/webhook/fabios-spec-plano
```

## Entrada esperada

```json
{
  "titulo": "Criar dashboard de agentes",
  "dominio": "FabioOS",
  "fase": "16.2",
  "spec": "Objetivo: ... Fora de escopo: ... Criterios de aceite: ... Testes: ... Riscos: ..."
}
```

## Cadeia

```text
SPEC
  -> normalizar
  -> gate de excelencia
  -> decompor tarefas
  -> gates de qualidade
  -> aceite e testes
  -> montar plano
  -> responder JSON/Markdown
```

## Saida

Retorna:

- `excellence_gate`: `pass` ou `needs_refinement`;
- `missing_sections`: lacunas da SPEC;
- `tasks`: tarefas com dono sugerido;
- `quality_gates`: regras obrigatorias;
- `acceptance`: criterios de aceite;
- `tests`: testes minimos;
- `markdown_plan`: plano em Markdown.

## Efeitos externos

Nenhum.

O workflow nao grava arquivo, nao chama API, nao cria issue, nao ativa runtime e nao faz commit.

## Uso ideal

1. Fabio descreve uma fase/capacidade.
2. Claude valida arquitetura.
3. Codex passa a SPEC por este workflow.
4. Cursor consome o plano quando houver interface.
5. So depois uma frente implementa.

## Visualizacao

http://127.0.0.1:5678/workflow/fabioosSpecPlanoExecucao
