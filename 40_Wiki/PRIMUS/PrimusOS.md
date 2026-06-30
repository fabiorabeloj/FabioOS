---
tipo: wiki
area: 40_Wiki
projeto: PRIMUS
status: ativo
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_chatgpt_primus_sumario_estrutural]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, primusos, narrativa, rpg, continuidade]
---

# PrimusOS

## Definicao

PrimusOS e a especializacao narrativa do FabioOS. Ele organiza mundos, campanhas, entidades, regras, missoes e consequencias como conhecimento persistente.

## Tese

PRIMUS nao deve ser tratado como texto de RPG solto. Ele deve funcionar como um sistema operacional narrativo:

```text
fonte -> enciclopedia -> instancia -> persistencia -> nova enciclopedia
```

## Componentes

| Componente | Papel |
|---|---|
| Enciclopedia | banco conceitual do mundo |
| Instancia | missao, cena, dungeon ou execucao jogavel |
| Persistencia | mudancas permanentes do mundo |
| Taxonomia | tipos aceitos no sistema |
| Templates | estrutura minima por familia de item |
| Registro | memoria historica do mundo |

## Relacao com FabioOS

Dentro do FabioOS, PrimusOS deve:

- usar o mesmo principio de fonte rastreavel da LLM Wiki;
- usar RAG/Grafo apenas depois de triagem;
- manter separacao entre canon, rascunho, inspiracao e externo;
- possuir skills e specs proprias;
- futuramente ter agente narrativo/lorekeeper.

## Fatos

- O sumario estrutural define PRIMUS como Grimorio, Atlas e Motor de Campanha Perpetua.
- O PDF de contexto completo final define uma ordem operacional fixa em seis blocos.
- O Google Doc completo amplia o PRIMUS para v4/v5 e muda a prioridade: antes da Missao 0001, devem existir WorldState, Tension Engine e Cantina Conflict Engine.
- O legado do vault ja contem circuito EIP, sistema de tipos, templates, livro do jogador, livro do mestre e Missao 0001.
- Existem fontes locais adicionais em Downloads e Desktop que ainda nao foram ingeridas.

## Interpretacao

PRIMUS e um laboratorio perfeito para testar o FabioOS como arquitetura cognitiva distribuida: fonte, wiki, grafo, RAG, agentes e automacao podem operar sobre um dominio criativo sem risco institucional.

## Proximas Acoes

- [x] Extrair o contexto completo final.
- [x] Absorver o Google Doc multiaba do PRIMUS.
- [x] Criar WorldState minimo.
- [x] Especificar Tension Engine.
- [x] Converter tensoes em conflitos candidatos.
- [x] Criar Player View da Cantina.
- [x] Criar rumores seguros da Cantina.
- [ ] Selecionar fonte/regiao segura ou lote E real para primeiro conflito jogavel.
- [ ] Transformar os tipos em templates ativos.
- [ ] Criar a primeira missao executavel somente depois do WorldState.
- [ ] Definir agente futuro `primus-lorekeeper`.

## Relacoes

- [[Circuito_EIP]]
- [[Taxonomia_PRIMUS]]
- [[Leis_do_PRIMUS]]
- [[Pipeline_PRIMUS]]
- [[Livros_do_PRIMUS]]
- [[Motor_Causal_PRIMUS]]
- [[30_Projetos/PRIMUS/Roteiro_Execucao_PRIMUS_6_Blocos]]
- [[30_Projetos/PRIMUS/PRIMUS]]
- [[80_Specs/PRIMUS/Spec_Ingestao_PRIMUS_ChatGPT]]
