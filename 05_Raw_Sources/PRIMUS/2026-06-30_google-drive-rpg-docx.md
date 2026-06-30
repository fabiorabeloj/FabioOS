---
tipo: fonte
origem: google-drive
area: 05_Raw_Sources
projeto: PRIMUS
status: processado-restrito
drive_file_ref: redacted-local-google-drive-doc
titulo: Rpg .docx
formato: docx
tamanho_bytes: 32826787
modificado_em: 2024-12-19T02:35:03.666Z
capturado_em: 2026-06-30
tags: [primus, google-drive, docx, fonte-restrita, digestor]
---

# Google Drive - Rpg .docx

## Identificacao

- Arquivo original: `Rpg .docx`
- Tipo: DOCX no Google Drive
- Link: redigido no Git; recuperar pelo Google Drive local usando o titulo `Rpg .docx`
- Status: fonte privada/restrita

## Conteudo Observado

O documento contem material amplo para campanha de RPG perpetua, incluindo:

- premissas de construcao de mundo;
- deuses, mundo selvagem, mundo antigo, magia e conflitos historicos;
- cosmologia, planos e modelos cosmologicos;
- planos anomalos e planos transitorios;
- exemplos de localidades, itens, faccoes, aventuras e ganchos;
- material misto de referencia, adaptacao e texto protegido.

## Decisao de Arquivamento

O corpo integral nao foi copiado para o repositorio.

Motivos:

- o arquivo e grande;
- contem texto de fontes potencialmente protegidas;
- PRIMUS precisa de catalogo rastreavel, nao de copia integral;
- a fonte deve alimentar digestor privado, validador e CatalogEntries.

## Uso Correto no PRIMUS

Este documento deve ser usado como entrada para:

- [[60_Sistemas/PRIMUS_Digestor/README]]
- [[80_Specs/PRIMUS/Spec_Digestor_PDF_PRIMUS]]
- [[30_Projetos/PRIMUS/Plano_Digestor_PRIMUS]]

Fluxo:

```text
DOCX/PDF -> extracao por pagina -> blocos -> CatalogEntry -> validacao -> Markdown Obsidian
```

## Restricoes

- Nao publicar conteudo protegido.
- Nao gerar markdowns integrais de capitulos.
- Nao tratar conteudo nao-SRD como livre.
- Usar snippets curtos apenas para rastreio privado.
- Marcar entradas duvidosas como `LicenseStatus: Restricted` e `Confidence: Low`.

## Proximas Acoes

- [ ] Usar o digestor em lote pequeno.
- [ ] Validar 20 entradas.
- [ ] Exportar somente CatalogEntries com metadados e snippet curto.
- [ ] Gerar Missao 0001 apenas depois de DeltaP previsto.
