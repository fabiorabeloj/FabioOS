---
tipo: plano
area: 30_Projetos
projeto: PRIMUS
status: ativo
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, ingestao, chatgpt, obsidian, roadmap]
---

# Plano de Ingestao PRIMUS

## Objetivo

Trazer o PRIMUS para a estrutura viva do FabioOS sem transformar o vault em deposito de arquivos soltos.

## Escopo Inicial

Fontes iniciais processadas:

- [[05_Raw_Sources/PRIMUS/2026-06-30_chatgpt_primus_sumario_estrutural]]
- [[05_Raw_Sources/PRIMUS/2026-06-30_pdf_primus_contexto_completo_final]]
- [[05_Raw_Sources/PRIMUS/2026-06-30_google-doc_primus_contexto_completo_final]]

Fontes inventariadas:

- [[05_Raw_Sources/PRIMUS/Inventario_Fontes_PRIMUS_2026-06-30]]

## Ordem de Ingestao

1. Sumario estrutural oficial.
2. Contexto completo final.
3. Documento base completo.
4. Corpus tecnico v1.
5. Cosmologia.
6. Atlas.
7. Livro do Jogador e Livro do Mestre.
8. Banco/JSON PRIMUS-TAXON.
9. Starter pack Obsidian legado.

## Regras

- Preservar fonte antes de sintetizar.
- Separar fato, interpretacao e decisao.
- Nao misturar canon PRIMUS com referencia externa.
- Nao copiar livros protegidos em massa para a wiki.
- Todo item PRIMUS deve ter tipo, fonte e estado.

## Estados de Conhecimento

| Estado | Significado |
|---|---|
| `canon` | aprovado como verdade do mundo/sistema |
| `rascunho` | ideia em elaboracao |
| `inspiracao` | referencia criativa sem virar canon |
| `externo` | material de terceiros/licenciado |
| `delta-p` | consequencia persistente de uma instancia |

## Saida Minima de Cada Lote

- fonte registrada em `05_Raw_Sources/PRIMUS/`;
- nota wiki ou projeto atualizada;
- lacunas explicitadas;
- proxima acao;
- registro em `50_Registros/Logs_Agentes/log.md`;
- changelog quando houver commit.

## Primeiro Lote Concluido

- Inventario das fontes PRIMUS locais.
- Nota fonte do sumario estrutural.
- MOC vivo em [[30_Projetos/PRIMUS/PRIMUS]].
- Wiki conceitual em [[40_Wiki/PRIMUS/PrimusOS]].
- Notas centrais sobre [[40_Wiki/PRIMUS/Circuito_EIP]] e [[40_Wiki/PRIMUS/Taxonomia_PRIMUS]].

## Segundo Lote Concluido

- PDF `PRIMUS - CONTEXTO COMPLETO FINAL (NAO PERDER)` extraido localmente.
- Nota-fonte criada em [[05_Raw_Sources/PRIMUS/2026-06-30_pdf_primus_contexto_completo_final]].
- Roteiro de execucao criado em [[Roteiro_Execucao_PRIMUS_6_Blocos]].
- Templates iniciais criados em [[80_Specs/PRIMUS/Templates_PRIMUS_Blocos]].

## Terceiro Lote Concluido

- Google Doc multiaba `PRIMUS - CONTEXTO COMPLETO FINAL (NAO PERDER)` lido via conector Google Drive.
- Nota-fonte criada em [[05_Raw_Sources/PRIMUS/2026-06-30_google-doc_primus_contexto_completo_final]].
- Notas estruturais criadas: [[40_Wiki/PRIMUS/Leis_do_PRIMUS]], [[40_Wiki/PRIMUS/Pipeline_PRIMUS]], [[40_Wiki/PRIMUS/Tipagem_Universal_PRIMUS]], [[40_Wiki/PRIMUS/Livros_do_PRIMUS]], [[40_Wiki/PRIMUS/Motor_Causal_PRIMUS]].
- SPEC criada em [[80_Specs/PRIMUS/Spec_WorldState_PRIMUS]].
- Roteiro corrigido para priorizar WorldState e Tension Engine antes da Missao 0001.

## Proxima Acao

Criar WorldState minimo e primeira lista de tensoes estruturais. A Missao 0001 fica congelada ate essa fundacao existir.
