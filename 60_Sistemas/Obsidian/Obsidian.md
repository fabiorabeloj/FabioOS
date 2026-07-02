---
tipo: sistema
area: tecnologia
status: ativo
classe_dado: interno
tags: [tecnico, Obsidian, vault]
criado_em: 2026-06-25
atualizado_em: 2026-06-25
---

# Obsidian

## O que é?

Obsidian é aplicativo de notas baseado em markdown que permite criar um vault conectado (conhecimento em rede). Suporta plugins, temas e sincronização.

## Para que serve?

- Armazenar e organizar [[60_Sistemas/Conhecimento/Motor_de_Assimilacao_FabioOS|conhecimento]] do FabioOS
- Criar links bidirecionais entre notas
- Visualizar grafos de conceitos
- Usar templates e automações via plugins
- Interface local e rápida

## Plugins essenciais

- **Obsidian Git**: Sincronizar com [[60_Sistemas/GitHub/GitHub|GitHub]]
- **Dataview**: Queries estruturadas em MD
- **Templater**: Templates dinâmicos
- **Tasks**: Gerenciar tarefas e checkboxes
- **Sodalite Theme**: Tema integrado

## Onde entra no FabioOS?

[[10_Dashboard/FabioOS|FabioOS]] > [[60_Sistemas/Obsidian/Obsidian|Obsidian]] -> core:
- Interface principal de edição
- Armazenamento do vault
- Visualização de links
- Execução de automações via plugins

## Fluxo de sincronização

```
Local editing (Obsidian)
    ↓ [Obsidian Git plugin]
GitHub commit
    ↓ [GitHub webhook]
n8n trigger
    ↓ [Processing]
Sync back to Obsidian
```

## Relações

- [[60_Sistemas/GitHub/GitHub|GitHub]] - sincronizacao bidirecional
- [[60_Sistemas/n8n/README|n8n]] - automacoes
- [[60_Sistemas/MCP/Inventario_MCP|MCP]] - integracao com Claude
- [[60_Sistemas/Conhecimento/Motor_de_Assimilacao_FabioOS|Conhecimento]] - storage

## Próximas ações

- [ ] Atualizar plugins
- [ ] Revisar tema Sodalite
- [ ] Testar sincronização GitHub
- [ ] Documentar atalhos principais
