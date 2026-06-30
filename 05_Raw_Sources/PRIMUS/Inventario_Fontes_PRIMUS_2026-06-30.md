---
tipo: inventario-fonte
origem: local
area: 05_Raw_Sources
projeto: PRIMUS
status: ativo
capturado_em: 2026-06-30
sensibilidade: media
tags: [primus, chatgpt, fontes, inventario, obsidian]
---

# Inventario de Fontes PRIMUS - 2026-06-30

## Funcao

Registrar onde o material do PRIMUS esta no PC e no vault antes de ingerir em massa.

## Resultado da Busca

Nao encontrei export oficial do ChatGPT ja importado no vault. Os diretorios reservados existem, mas estao vazios:

- `05_Raw_Sources/_compat_sources/chatgpt/exports/`
- `05_Raw_Sources/_compat_sources/chatgpt/conversas/`
- `05_Raw_Sources/_compat_sources/chatgpt/_restrito/`

Encontrei, porem, varios artefatos locais do PRIMUS que parecem derivados de conversas, exports ou consolidados gerados a partir do ChatGPT.

## Fontes Locais Relevantes

| Fonte | Caminho | Tipo | Uso sugerido | Acao |
|---|---|---|---|---|
| Sumario estrutural oficial | `C:\Users\user\Downloads\primus_sumario_estrutural_oficial.md` | markdown | Estrutura de alto nivel do livro PRIMUS | processar agora |
| Contexto completo final | `C:\Users\user\Downloads\PRIMUS - CONTEXTO COMPLETO FINAL (NAO PERDER).pdf` | pdf | Contexto consolidado critico | extrair depois |
| Documento base completo | `C:\Users\user\Downloads\PRIMUS_Documento_Base_Completo.docx` | docx | Base textual possivelmente consolidada | extrair depois |
| Corpus tecnico v1 | `C:\Users\user\Downloads\PRIMUS_Corpus_Tecnico_v1.docx` | docx | Corpo tecnico do sistema | extrair depois |
| Livro I Cosmologia | `C:\Users\user\Downloads\PRIMUS_Livro_I_Cosmologia_Extracao_Maxima.docx` | docx | Cosmologia | extrair depois |
| Livro II Atlas | `C:\Users\user\Downloads\PRIMUS_Livro_II_Atlas_v1.docx` | docx | Atlas | extrair depois |
| Livro Jogador e Mestre | `C:\Users\user\Downloads\PRIMUS_Completo_Livro_Jogador_e_Mestre.docx` | docx | Regras jogaveis e motor | extrair depois |
| Export PRIMUS-TAXON | `C:\Users\user\Downloads\primus_export.zip` | zip | Contem `prompt.txt`, `state.json` e PDF D&D | preservar como fonte restrita |
| Index outputs | `C:\Users\user\Downloads\primus_index_outputs_20251230_055200.zip` | zip/sqlite/json | Base indexada por livro/categoria | avaliar como banco auxiliar |
| PRIMUS site local | `C:\Users\user\Desktop\Projeto\primus-site\` | app local | Prototipo/visualizacao do corpus | inventariar depois |
| Banco PRIMUS local | `C:\Users\user\Desktop\Projeto\primus_out_20251230_055048\primus.sqlite` | sqlite | Banco estruturado com registros | avaliar depois |
| HTML prompt builder | `C:\Users\user\Documents\primus-taxon.html` | html | Gerador de prompt PRIMUS-TAXON | arquivar depois |

## Fontes Ja no Vault Legado

- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/PRIMUS/INDEX_PRIMUS.md`
- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/PRIMUS/00_CIRCUITO_MESTRE.md`
- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/PRIMUS/01_SISTEMA_DEFINICOES.md`
- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/PRIMUS/02_TIPOS_PRIMUS.md`
- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/PRIMUS/08_PROXIMOS_PASSOS.md`
- `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/PRIMUS_Obsidian_Starter_v0_1/`

## Classificacao

- Fonte bruta: Downloads, Desktop/Projeto, Documents.
- Fonte legada processada: `90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/20_Projetos/PRIMUS/`.
- Conhecimento vivo criado neste lote: `30_Projetos/PRIMUS/` e `40_Wiki/PRIMUS/`.

## Riscos

- O export `primus_export.zip` contem material de D&D. Nao deve ser copiado integralmente para notas wiki.
- Os arquivos DOCX/PDF podem conter duplicacao e versoes divergentes.
- `C:\Users\user\Documents\primus.sqlite` existe com tamanho 0; nao deve ser tratado como fonte valida.
- Falta export oficial completo do ChatGPT (`conversations.json` ou zip oficial).

## Proximas Acoes

- [ ] Exportar o historico oficial do ChatGPT e colocar em `05_Raw_Sources/_compat_sources/chatgpt/exports/`.
- [ ] Extrair primeiro o PDF `PRIMUS - CONTEXTO COMPLETO FINAL (NAO PERDER).pdf`.
- [ ] Extrair os DOCX por prioridade: documento base, corpus tecnico, cosmologia, atlas, jogador/mestre.
- [ ] Avaliar o `primus.sqlite` estruturado antes de copiar bancos para o vault.
- [ ] Manter D&D como referencia externa/licenciada, nao como copia textual em wiki.
