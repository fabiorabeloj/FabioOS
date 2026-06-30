---
tipo: player-view
area: 30_Projetos
projeto: PRIMUS
status: rascunho-operacional
fonte: [[30_Projetos/PRIMUS/PlayerView_Cantina_0001_PRIMUS]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, cantina, rumores, player-view]
---

# Cantina - Rumores 0001

## Funcao

Primeiro quadro de rumores seguros da Cantina PRIMUS. Estes rumores sao operacionais, nao canon narrativo definitivo.

## Regras

- Rumor visivel nao e missao pronta.
- Rumor nao concede item, mapa, classe, magia ou vantagem.
- Rumor pode apontar para bloqueio.
- Rumor so vira missao depois de contrato, DeltaP previsto e validacao.

## Rumores Visiveis

| ID | Estado | Texto Visivel | Origem | Proxima Acao |
|---|---|---|---|---|
| RUM-0001 | V | "O quadro da Cantina tem espacos vazios: ha possibilidades, mas nem todas estao prontas para partida." | CCF-0002 | manter como aviso de sistema |
| RUM-0002 | V | "Voce pode ouvir falar de algo antes de conquistar acesso real a esse algo." | CCF-0004 | formalizar V/A/Oculto |
| RUM-0003 | V | "Alguns caminhos exigem que o mundo tenha nome, lugar e consequencia antes de abrir." | CCF-0001/CCF-0005 | manter bloqueado ate WorldState e DeltaP |

## Rumores Bloqueados

| ID | Motivo do Bloqueio |
|---|---|
| RUM-BLK-0001 | Falta primeira regiao segura. |
| RUM-BLK-0002 | Falta schema DeltaP completo. |
| RUM-BLK-0003 | Falta selecionar entradas E reais com instancing hint. |

## Uso pelo Mestre ou Agente

O mestre/agente pode mostrar `RUM-0001`, `RUM-0002` e `RUM-0003` ao jogador como interface de sistema. Nao deve transformar nenhum deles em aventura ate que exista:

- conflito candidato valido;
- ator/local/motivo;
- contrato de missao;
- recompensa e risco;
- DeltaP previsto.

## Proxima Acao

Selecionar uma fonte canonica/regiao segura ou criar um lote de entradas E reais para transformar o primeiro rumor em conflito jogavel.
