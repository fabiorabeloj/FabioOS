---
tipo: projeto
area: criatividade
status: ativo
tags: [PRIMUS, bloco-3, templates, família]
criado_em: 2026-06-25
---

# BLOCO 3 — Templates por Família (Estrutura por Tipo)

**Objetivo:** Simetria por tipo (RACE ≠ PLANE). Um template para cada família.

---

## 🎯 Princípio

Cada **família de tipos** tem seu próprio **template**.

Você **repete o template DENTRO da família**, não globalmente.

Exemplo: Template RACE não serve para PLANE. Template PLANE não serve para CREATURE.

---

## 📋 Templates Oficiais (4-8 templates)

### 1. Template RACE
```yaml
name: [Nome da raça]
subrace: [Sub-raças (lista)]
traits:
  - [Traço 1]
  - [Traço 2]
  - [Traço N]
ability_scores: [Bônus em +2, +1, etc]
size: [Small/Medium/Large]
speed: [em pés]
languages: [Linguagens]
typical_names:
  - male: [Nome masculino]
  - female: [Nome feminino]
culture: [Opcional - cultura típica]
```

### 2. Template CLASS
```yaml
name: [Nome da classe]
hit_die: [d8, d10, d12]
proficiencies:
  armor: [...]
  weapons: [...]
  tools: [...]
spellcasting:
  ability: [INT/WIS/CHA]
  spell_slots: [...]
features:
  level_1: [Feature X]
  level_3: [Feature Y]
  level_N: [Feature Z]
subclass_choice: [Nível em que escolhe]
```

### 3. Template PLANE
```yaml
name: [Nome do plano]
type: [Material/Astral/Inferno/etc]
properties: [Propriedades metafísicas]
laws: [Leis locais do plano]
access: [Como entra]
danger: [Nível de perigo]
inhabitants: [Quem vive ali]
resources: [O que pode pegar]
connections: [Portais para outros planos]
```

### 4. Template DUNGEON
```yaml
name: [Nome]
level: [Profundidade/Complexidade]
layers: [Quantas camadas]
rooms:
  room_1:
    description: [Descrição]
    creatures: [Quem está aqui]
    encounters: [Encontros possíveis]
    traps: [Armadilhas]
    rewards: [Tesouro]
    exit_to: [Próxima sala]
encounters: [Lista de encontros]
boss: [Chefe final]
delta_p: [O que muda quando completa]
```

### 5. Template CREATURE
```yaml
name: [Nome]
type: [Beast/Humanoid/Dragon/etc]
size: [Small/Medium/Large/Huge]
armor_class: [AC]
hit_points: [HP]
ability_scores: [STR/DEX/CON/INT/WIS/CHA]
skills: [Perícias]
actions:
  - name: [Ação 1]
    damage: [Dano]
  - name: [Ação 2]
    effect: [Efeito]
legendary_actions: [Ações lendárias (se houver)]
immunities: [Imunidades]
```

### 6. Template SPELL
```yaml
name: [Nome]
level: [0-9]
school: [Evocação/Abjuração/etc]
casting_time: [1 ação/1 bônus/etc]
range: [Alcance]
components: [V/S/M]
duration: [Instântaneo/1 minuto/Concentração/etc]
description: [O que faz]
at_higher_levels: [Se lançar em nível maior]
```

### 7. Template ITEM
```yaml
name: [Nome]
type: [Weapon/Armor/Adventuring Gear/etc]
rarity: [Common/Uncommon/Rare/etc]
properties: [Propriedades]
description: [O que é]
cost: [Em ouro]
weight: [Em libras]
if_magical:
  bonus: [+1, +2, etc]
  special: [Propriedades especiais]
```

### 8. Template NPC
```yaml
name: [Nome]
race: [[race]] (tipo race)
class: [[class]] (tipo class)
background: [[background]] (tipo background)
alignment: [Alinhamento]
personality:
  - [Traço 1]
  - [Traço 2]
motivation: [Por que faz o que faz]
secrets: [O que não conta]
relationships: [Com outros NPCs]
if_creature_stats: [Usa Template CREATURE]
```

---

## ✨ Regra Central

**Cada família tem UM template.**  
**Repete só DENTRO da família.**

Raça usa Template RACE.  
Plano usa Template PLANE.  
Nunca mistura.

---

## 🔗 Integração com Blocos Anteriores

- **Bloco 1** define: E→I→P (circuito)
- **Bloco 2** define: 28 tipos (o que existe)
- **Bloco 3** define: 8 templates (como se estrutura)
- **Bloco 4** usa: Templates para criar Livro do Jogador
- **Bloco 5** usa: Templates + ΔP para motor funcionar

---

## ✨ Saída deste Bloco

- [x] 8 templates oficiais definidos
- [x] Regra: Um template por família
- [x] Exemplos de estrutura pronta
- [ ] Próximo: BLOCO 4 (Livro do Jogador)

---

**Status:** ✅ Completo  
**Pode avançar?** Sim → BLOCO 4
