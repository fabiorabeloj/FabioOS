---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: concluido
tags: [changelog, fabios, dominios, permissoes, privacidade]
criado_em: 2026-06-28
atualizado_em: 2026-06-28
---

# Changelog - dominios, dados e permissoes v0

## O que foi feito

- Criada a matriz de dominios, dados e permissoes do FabioOS.
- Implementado o classificador local `classificar_dado_fabioos.py`.
- Gerada a primeira classificacao real sobre o Radar de Arquiteturas de Mercado.
- Atualizado o Dashboard Operacional para exibir classificacoes de dominio/dados.
- Plano Mestre, Estrutura Profissional, NEXT_ACTIONS e mapa navegavel foram conectados ao novo gate.
- Testado caso temporario de conteudo critico: classificador retornou `Critico`, RAG `Proibido` e modelo externo `Proibido`.

## Arquivos principais

- `60_Sistemas/FabioOS/Matriz_Dominios_Dados_Permissoes_2026-06-28.md`
- `60_Sistemas/FabioOS/scripts/classificar_dado_fabioos.py`
- `60_Sistemas/FabioOS/classificacoes/2026-06-28_radar-arquiteturas-de-mercado-fabioos.md`

## Resultado

O FabioOS agora possui um gate v0 antes de ingerir, reindexar, enviar a modelo externo ou conectar dominios.

## Limite

O classificador usa regras locais e palavras-chave. Ele ajuda a evitar erro grosseiro, mas nao substitui revisao humana.
