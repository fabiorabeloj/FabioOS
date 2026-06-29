---
tipo: changelog
area: 50_Registros
projeto: FabioOS
status: registrado
tags: [fabios, changelog, gmail, google-drive, conectores]
criado_em: 2026-06-28
---

# Changelog - Catalogacao Google Connectors v0

## Resumo

Foi criada a primeira catalogacao real de Gmail e Google Drive usando conectores do Codex em modo leitura.

## Entregas

- Resumo versionavel em `60_Sistemas/FabioOS/Conectores_Google_Catalogo_v0.md`.
- SPEC em `60_Sistemas/FabioOS/specs/2026-06-28_catalogacao-google-connectors-v0.md`.
- Mapa Obsidian em `wiki/memoria/Mapa_Conectores_Google_FabioOS.md`.
- Catalogos detalhados locais em `sources/email/_restrito/` e `sources/drive/_restrito/`.
- `.gitignore` atualizado para impedir versionamento de detalhes restritos do Drive.

## Seguranca

- Nenhum e-mail foi enviado, apagado, arquivado ou rotulado.
- Nenhum documento do Drive foi exportado.
- Nenhuma API externa/modelo foi chamado.
- Conteudo detalhado fica fora do Git.

## Proximo passo

Implementar lotes pequenos de triagem por tema: FabioOS/IA, escola, projetos e financeiro restrito.
