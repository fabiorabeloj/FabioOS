---
tipo: spec
area: 60_Sistemas
projeto: FabioOS
status: implementado
fase: inventario-ferramentas-ia-v0
dominio: FabioOS
classe_dado: Interno
permissao: leitura local; sem revelar tokens; sem instalar/alterar runtimes
criado_em: 2026-06-28
atualizado_em: 2026-06-28
tags: [fabios, spec, ia, ferramentas, cursor, hermes, openclaw, n8n, openrouter]
---

# SPEC - Inventario Ferramentas IA Local v0

## 1. Problema

Fabio instalou e citou varias ferramentas (Cursor, Hermes, OpenClaw, n8n, OpenRouter), mas o sistema ainda nao tinha uma visao objetiva do que esta instalado, rodando, configurado ou apenas planejado.

## 2. Objetivo

Criar um script local que gere um inventario seguro das ferramentas de IA do PC, sem revelar tokens, sem instalar nada e sem alterar runtime/auth.

## 3. Fora de escopo

- Instalar Cursor, Hermes, OpenClaw ou n8n.
- Configurar tokens.
- Iniciar/parar processos externos.
- Fazer chamadas a APIs pagas.
- Fazer push.

## 4. Arquitetura proposta

```text
PC local
  -> detectar comandos no PATH
  -> detectar processos e portas
  -> detectar diretorios conhecidos
  -> detectar presenca de env vars sem valores
  -> gerar Markdown no vault
```

## 5. Criterios de aceite

- [x] Relatorio gerado em Markdown.
- [x] Nenhum token exibido.
- [x] OpenClaw/n8n/Cursor/Hermes/OpenRouter aparecem com estado objetivo.
- [x] Relatorio e visivel no Obsidian.
- [x] Dashboard aponta para a capacidade.
