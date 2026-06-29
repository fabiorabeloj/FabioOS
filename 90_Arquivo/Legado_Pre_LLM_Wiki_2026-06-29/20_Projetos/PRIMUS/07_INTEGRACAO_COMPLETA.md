---
tipo: projeto
area: criatividade
status: ativo
tags: [PRIMUS, integração, circuito, E-I-P]
criado_em: 2026-06-25
---

# INTEGRAÇÃO COMPLETA — Como os 6 Blocos Formam um Sistema Vivo

**Objetivo:** Mostrar visualmente como E→I→P funciona através dos blocos.

---

## 🔗 O Circuito em Cascata

```
┌─────────────────────────────────────────────────────────────────┐
│  BLOCO 1: MAPA DO SISTEMA                                       │
│  Define: Circuito E→I→P, Prisma, Pipeline T1-T4               │
│  ↓ Alimenta                                                      │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│  BLOCO 2: SISTEMA DE TIPOS                                      │
│  Define: 28 tipos (o que pode existir em E)                    │
│  Exemplo: race, class, creature, npc, plane, dungeon, etc      │
│  ↓ Alimenta                                                      │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│  BLOCO 3: TEMPLATES POR FAMÍLIA                                 │
│  Define: 8 templates (como cada tipo se estrutura)             │
│  Exemplo: Template RACE, Template CLASS, Template DUNGEON      │
│  ↓ Alimenta                                                      │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│  BLOCO 4: LIVRO DO JOGADOR                                      │
│  Preenche: Templates com conteúdo real                         │
│  Exemplo: Humano (preenchido), Mago (preenchido), etc         │
│  ↓ Alimenta (E = Enciclopédia)                                  │
└─────────────────────────────────────────────────────────────────┘
                            ↓
                      E (Enciclopédia)
                  20+ entidades tipadas
                    ↓
                Pipeline T1-T4
                (Do BLOCO 1)
                    ↓
┌─────────────────────────────────────────────────────────────────┐
│  T1 CAPTURA: Pega 20 entidades de E                            │
│  T2 MATERIALIZAÇÃO: Transforma em mundo vivo (I)               │
│  T3 INTEGRAÇÃO: Conecta encontros logicamente                  │
│  T4 INSTANCIAMENTO: Cria instância playable                    │
│  ↓ Alimenta (I = Instância)                                     │
└─────────────────────────────────────────────────────────────────┘
                            ↓
                    I (Instância)
                  Uma missão viva
              (BLOCO 5 + BLOCO 6 definem isto)
                    ↓
┌─────────────────────────────────────────────────────────────────┐
│  BLOCO 5: LIVRO DO MESTRE                                       │
│  Define: Contrato de Missão, Validação, ΔP                    │
│  Motor que transforma E em I playable                          │
│  ↓ Alimenta (P = Persistência)                                  │
└─────────────────────────────────────────────────────────────────┘
                            ↓
                  P (Persistência)
                ΔP = Mudanças mapeadas
              (BLOCO 6 prova que funciona)
                    ↓
         VOLTA PARA E (próxima missão)
           E(v2) = E(v1) + ΔP
```

---

## 📊 Exemplo Prático: Missão 0001

### BLOCO 1 — Circuito
```
Define que todo sistema segue E→I→P→E→I→P
```

### BLOCO 2 — Tipos
```
Temos: race, class, creature, npc, item, spell, dungeon, faction
```

### BLOCO 3 — Templates
```
Template RACE: name, traits, ability_scores, languages, culture
Template CLASS: name, hit_die, features, spellcasting
Template DUNGEON: name, layers, rooms, encounters, boss
Template CREATURE: name, type, AC, HP, abilities, actions
Template NPC: name, race, class, background, personality
```

### BLOCO 4 — Livro do Jogador
```
Humano: +2 atributo, 30 pés velocidade, 2 talentos extras
Mago: d6 hit die, Inteligência para spellcasting
Elfo: +2 DEX, +1 INT, visão 60 pés
(Preenchido com conteúdo real)
```

### E (Enciclopédia v1) — Pega de BLOCO 4
```
20 entidades:
- Raças: Humano, Elfo, Anão
- Classes: Mago, Guerreiro
- Criaturas: Goblin, Orc, Troll, Dragão
- NPCs: Taverna keeper, Rei, Sacerdotisa
- Itens: Espada, Escudo, Poção cura, Ouro
- Magias: Fireball, Cure Wounds
- Facções: Coroa Real
```

### T1 → T2 → T3 → T4 (Pipeline)
```
T1 Captura: Pega 20 entidades ✓
T2 Materialização: Cria Caverna do Dragão Verde com 2 layers
T3 Integração: Conecta Room 1→Room 2→Layer 2→Boss Chamber
T4 Instanciamento: Missão 0001 pronta para jogar
```

### I (Instância) — Missão 0001
```
Caverna do Dragão Verde
- Layer 1: Entrada (Goblins) → Câmara principal (Orc) → Boss
- Layer 2: Tesouro (Troll) → Princesa → Boss Chamber
- Boss: Dragão Verde
- Recompensa: 1000 XP, 500 gold, Artefato
```

### BLOCO 5 — Livro do Mestre
```
Define: Contrato, 3 perguntas, ΔP
Motor que torna I funcional
```

### P (Persistência) — ΔP
```
dragon_killed: true
princess_rescued: true
artifact_recovered: true
coroa_real_reputation: +10
dragon_siblings_appear: true (novo threat)
```

### E(v2) — Enciclopédia modificada
```
E(v1) + ΔP =
- Dragão está morto (não aparece mais)
- Princesa está livre (pode ser NPC)
- Coroa gosta de você (missões melhores)
- Irmãos do dragão existem (novo challenge)
```

### BLOCO 6 — Prova
```
Executar Missão 0001
Registrar ΔP real
Gerar Missão 0002 com E(v2)
Repetir infinitamente
```

---

## 🔄 Próximas Missões (Loop Infinito)

### Missão 0002 (usa E(v2))
```
Irmãos do dragão = novo bosses
Princesa = NPC que ajuda
Coroa = oferece recompensas maiores

Novo ΔP:
- siblings_killed: true
- princess_joins_party: true
- coroa_real_reputation: +20
```

### E(v3) — Enciclopédia evolui
```
E(v2) + ΔP da Missão 0002 =
- Dragão e irmãos mortos
- Princesa é aliada permanente
- Coroa é muito amigo
- Novo threat aparece
```

**O mundo não reseta. EVOLUI.**

---

## 🎯 Integração com FabioOS

PRIMUS é um **subsistema de [[Continuidade_da_Vida]]**:

```
[[Continuidade da Vida]] (6 pilares)
  ├─ [[Cérebro]] — Conhecimento
  │   └─ PRIMUS = Jogo com mundo que evolui
  │
  ├─ [[Trabalho]] — Produção
  │   └─ Pode usar PRIMUS para criar conteúdo
  │
  ├─ [[Patrimônio]] — Recursos
  │   └─ Sistemas de recompensa em PRIMUS
  │
  ├─ [[Saúde]] — Bem-estar
  │   └─ PRIMUS como exercício mental
  │
  ├─ [[Criatividade]] — Expressão
  │   └─ PRIMUS é pura criatividade
  │
  └─ [[Identidade]] — Persistência
      └─ PRIMUS é sobre mundo persistente
```

---

## ✨ O que torna PRIMUS especial

✅ **Não é filosofia** — São 6 blocos executáveis  
✅ **Ordem é fixa** — 1→2→3→4→5→6 (se inverter, volta o "texto curto")  
✅ **Circuito fechado** — E→I→P→E (evolução infinita)  
✅ **Tudo integrado** — Cada bloco alimenta o próximo  
✅ **Prova de conceito** — Missão 0001 mostra que funciona  
✅ **Vivo** — Mundo muda a cada ciclo  

---

## 📋 Checklist de Integração

- [x] BLOCO 1: Circuito definido
- [x] BLOCO 2: Tipos definidos
- [x] BLOCO 3: Templates definidos
- [x] BLOCO 4: Livro do Jogador estruturado
- [x] BLOCO 5: Livro do Mestre funcional
- [x] BLOCO 6: Missão 0001 definida
- [x] Integração: E→I→P→E ciclo fechado
- [ ] Próximo: Preencher BLOCO 4 com conteúdo real

---

**Status:** ✅ Estrutura integrada  
**Pronto para:** Executar primeira missão
