---
tipo: wiki
area: 40_Wiki
projeto: PRIMUS
status: ativo
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_chatgpt_project_primus_inventario_logs]]
criado_em: 2026-06-30
atualizado_em: 2026-07-01
tags: [primus, fontes, matriz, canon, frameworks]
---

# Matriz de Fontes PRIMUS

## Principio

Fonte nao entra no PRIMUS por acumulacao. Fonte entra quando resolve um gargalo especifico do motor.

## Camadas

| Camada | Funcao | Exemplos |
|---|---|---|
| Canon Core | regra-base e mecanica central | Livro do Jogador, Guia do Mestre, Manual dos Monstros |
| Canon Complementar | opcoes oficiais que ampliam o core | Xanathar, Tasha, Fizban, Mordenkainen, Volo |
| Setting Oficial | mundos oficiais com escopo proprio | Eberron, Ravenloft, Strixhaven, Sword Coast, Spelljammer |
| Framework Operacional | procedimentos reaproveitaveis sem trocar regra D&D | WWN, SWN, Blades, Tome of Adventure Design |
| Externo Controlado | material parceiro ou nao-D&D | SWE5, Pirate Adventurers, homebrews |
| Fonte Compilada Restrita | material misto privado que exige digestao e classificacao de origem | `Rpg .docx` |

## Fontes Prioritarias

| Fonte | Prioridade | Uso | Nunca Pode Afetar |
|---|---|---|---|
| D&D 5e Core | essencial | regras, personagem, combate, magia, monstros | geometria EIP |
| D&D 2024/5.5e | importante | comparacao e possivel atualizacao | canon 5e sem decisao |
| Worlds Without Number | essencial operacional | sandbox regional, mundo vivo, geracao controlada | regras D&D |
| Stars Without Number | muito importante | faction turn, setor vivo, projetos de faccao | classes, combate, magia D&D |
| Blades in the Dark | importante | clocks, downtime, heat, pressao, payoff | action economy D&D |
| Tome of Adventure Design | importante | geradores de aventura/dungeon/hook | lore canon |
| Eberron | importante | civilizacao, faccoes, economia magica | core mecanico |
| Ravenloft | importante | dominios fechados, medo, maldicao | estrutura global PRIMUS |
| Rpg .docx | importante operacional | mapa de padroes, CatalogEntries candidatas e funil do digestor | texto integral, canon direto ou IP externa literal |
| ACKS | futuro | dominio, renda, tropas, mercado | antes de WorldState e tempo |
| Godbound | futuro | escala divina e projetos amplos | antes de base mundana |

## Ordem de Uso

1. Core D&D para regras e limites.
2. WWN para sandbox operacional.
3. SWN para faccoes e projetos entre missoes.
4. Blades para medidores de pressao.
5. Tome of Adventure Design para Engrenagem 6.
6. Settings oficiais apenas quando houver regiao, faccao ou tema concreto.
7. `Rpg .docx` apenas via [[30_Projetos/PRIMUS/Mapa_Digestao_Rpg_Docx_PRIMUS]] e [[30_Projetos/PRIMUS/CatalogEntries_Candidatas_Rpg_Docx_PRIMUS]].
8. ACKS/Godbound somente depois de WorldState, tempo e escala de dominio.

## Regra de Integracao

Toda fonte deve declarar:

```yaml
source_id:
camada:
use:
affects:
never_affects:
status:
justificativa:
```

## Proxima Acao

Selecionar um lote minimo de CatalogEntries reais a partir de D&D Core + WWN, antes de adicionar novos frameworks.
