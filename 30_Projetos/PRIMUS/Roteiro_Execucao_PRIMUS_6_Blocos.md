---
tipo: roteiro
area: 30_Projetos
projeto: PRIMUS
status: ativo
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_pdf_primus_contexto_completo_final]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, execucao, roteiro, eip, worldstate, tension-engine]
---

# Roteiro de Execucao PRIMUS - 6 Blocos

## Funcao

Converter o PRIMUS de estrutura conceitual para sistema jogavel e persistente.

## Nota de Precedencia - Google Doc v5

O Google Doc multiaba do PRIMUS corrige a prioridade anterior: a Missao 0001 nao deve ser executada antes da arquitetura essencial. Este roteiro continua valido como sequencia editorial, mas a proxima implementacao deve ser WorldState -> Tension Engine -> Cantina Conflict Engine, nao a missao.

## Ordem Obrigatoria

```text
1 -> 2 -> 3 -> 4 -> 5 -> 6
```

Nao inverter. A propria fonte alerta que inverter a ordem faz o projeto voltar ao problema de "texto curto".

## Bloco 1 - Mapa do Sistema

**Entrega:** uma pagina oficial de definicoes.

Deve fixar:

- Circuito E -> I -> P;
- Prisma Enciclopedia + Instancia + Persistencia;
- Pipeline T1 -> T2 -> T3 -> T4.

**Status:** parcialmente existente em [[40_Wiki/PRIMUS/Circuito_EIP]].

## Bloco 2 - Sistema de Tipos

**Entrega:** apendice de tipagem universal.

Regra: nada entra na Enciclopedia sem tipo.

**Status:** parcialmente existente em [[40_Wiki/PRIMUS/Taxonomia_PRIMUS]].

## Bloco 3 - Templates por Familia

**Entrega:** templates oficiais curtos por familia.

Templates iniciais:

- `RACE`;
- `CLASS`;
- `PLANE`;
- `DUNGEON`;
- `MISSION`;
- `NPC`;
- `CREATURE`;
- `SPELL`.

**Status:** iniciado em [[80_Specs/PRIMUS/Templates_PRIMUS_Blocos]].

## Bloco 4 - Livro do Jogador

**Entrega:** estrutura minima para criar personagem e jogar rapido.

Conteudo:

- racas;
- classes;
- antecedentes;
- equipamento;
- talentos;
- magias;
- regras minimas de criacao.

**Status:** legado existe, precisa migracao controlada.

## Bloco 5 - Livro do Mestre

**Entrega:** motor de missoes fechadas.

Conteudo:

- contrato de missao;
- regras de encaixe;
- portabilidade;
- Delta P;
- Engrenagem 6;
- validacao V(E), V(I), V(P).

**Status:** legado existe, precisa consolidacao.

## Bloco 6 - Ciclo Completo

**Entrega:** Missao 0001 completa.

Fluxo:

```text
E: selecionar 20 entradas
I: gerar dungeon instanciada
P: registrar Delta P
```

**Status:** preparacao viva criada em [[Missao_0001_Preparacao]], mas congelada ate WorldState e Tension Engine existirem.

## Fase 0 - Fundacao Causal

**Entrega:** WorldState minimo e Tension Engine inicial.

Fluxo:

```text
WorldState -> Tensoes -> Conflitos -> Faccoes -> Missoes -> DeltaP -> WorldState
```

**Status:** iniciado em [[WorldState_0001_PRIMUS]], detalhado em [[Tensoes_Iniciais_PRIMUS]], convertido em [[Conflitos_Candidatos_PRIMUS]], projetado em [[PlayerView_Cantina_0001_PRIMUS]], especificado em [[80_Specs/PRIMUS/Spec_WorldState_PRIMUS]], [[80_Specs/PRIMUS/Spec_Tension_Engine_PRIMUS]] e [[80_Specs/PRIMUS/Spec_Cantina_Conflict_Engine_PRIMUS]].

## Checklist de Execucao

- [x] Fase 0 WorldState minimo criado.
- [x] Fase 0 Tension Engine inicial especificado.
- [x] Converter tensoes em conflitos candidatos.
- [x] Criar Player View da Cantina.
- [ ] Criar rumores seguros da Cantina.
- [ ] Bloco 1 validado como definicao oficial.
- [ ] Bloco 2 validado como taxonomia oficial.
- [x] Bloco 3 criado com templates iniciais.
- [ ] Bloco 4 reestruturado como livro jogavel minimo.
- [ ] Bloco 5 reestruturado como motor operacional.
- [x] Bloco 6 preparado como Missao 0001, mas nao liberado para execucao.
- [ ] Delta P definido em YAML.
- [ ] Decidir quando PRIMUS entra em RAG/Grafo separado.

## Proxima Acao

Criar `Cantina_Rumores_0001_PRIMUS.md` com rumores seguros antes de mexer no contrato final da [[Missao_0001_Preparacao]].
