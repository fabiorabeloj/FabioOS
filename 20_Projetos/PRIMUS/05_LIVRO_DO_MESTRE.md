---
tipo: projeto
area: criatividade
status: ativo
tags: [PRIMUS, bloco-5, mestre, motor]
criado_em: 2026-06-25
---

# BLOCO 5 — Livro do Mestre (O Motor Real)

**Objetivo:** PRIMUS virar "jogo de computador" (missões autossuficientes).

---

## 🔧 Conteúdo Mínimo (Motor funcional)

### 1. Contrato de Missão (Objeto)
```yaml
mission_id: [0001, 0002, etc]
name: [Nome da missão]
objective: [O que fazer - matar/resgatar/descobrir/etc]
location: [[dungeon]] ou [[site]]
npcs_involved: [Lista de NPCs relacionados]
difficulty: [Fácil/Médio/Difícil/Mortal]
estimated_duration: [X horas de jogo]
reward:
  xp: [Quanto XP]
  gold: [Quanto ouro]
  items: [Itens especiais]
  reputation: [Com qual facção ganha reputação]
failure_consequence: [O que acontece se falhar]
success_consequence: [O que muda se vencer]
```

### 2. Regras de Encaixe (3 Perguntas Críticas)
```
Pergunta 1: Onde entra?
  → Qual [[dungeon]] ou [[settlement]]?
  
Pergunta 2: Com quem interage?
  → Quais [[npc]] ou [[creature]] encontra?
  
Pergunta 3: O que muda?
  → Qual [[reward]] e qual [[consequence]]?
```

Se conseguir responder as 3, missão é válida.

### 3. Portabilidade (Classificação)
```
Portável (P): Pode acontecer em qualquer lugar
  Exemplo: "Matar 5 goblins" (não precisa de um dungeon específico)
  
Persistente (Per): Mudança permanente no mundo
  Exemplo: "Rei morre" (afeta próximas missões)
  
Local (L): Acontece em um lugar específico
  Exemplo: "Explorar Tomb of Horrors" (SÓ ali)
```

Classifique sua missão.

### 4. Persistência ΔP (Tabelável)
```yaml
delta_p:
  flags:          [boolean outcomes (morto? sim/não)]
  items_gained:   [tesouro conquistado]
  items_lost:     [o que perdeu]
  deaths:         [quem morreu]
  reputation:
    faction_1: [+X ou -X]
    faction_2: [+X ou -X]
  knowledge:      [novo lore descoberto]
  damage:         [estruturas danificadas]
  new_npcs:       [personagens criados]
  new_threats:    [inimigos que aparecem]
```

Este ΔP alimenta PRÓXIMA E (Enciclopédia).

### 5. Engrenagem 6 (Geração de Dungeon & Encontros)
```
Template de geração automática:

Para cada layer do dungeon:
  1. Role: tipo de sala (Combat/Social/Ambiental)
  2. Roll: criatura encontrada (usa [[creature]])
  3. Roll: hazard/trap (usa [[hazard]]/[[trap]])
  4. Roll: tesouro (usa [[reward]])
  5. Conectar logicamente
  
Resultado: Dungeon procedural funcional
```

### 6. Validação V(E), V(I), V(P)
```
V(E): Validação de Enciclopédia
  ✓ Todos os NPCs têm [[npc]]?
  ✓ Todos os itens têm [[item]] ou [[magic_item]]?
  ✓ Todas as criaturas têm [[creature]]?
  
V(I): Validação de Instância
  ✓ Dungeon tem 3-5 camadas?
  ✓ Encontros são conectados logicamente?
  ✓ Boss está no final?
  
V(P): Validação de Persistência
  ✓ ΔP é registrável em tabela?
  ✓ ΔP alimenta próxima E?
  ✓ Consequências fazem sentido?
```

Se passar nas 3, instância é válida.

---

## 🔄 Como Usar Este Livro

**Você é um programa gerador de missões.**

**Fluxo:**
1. Pegue 20 entradas de E (raças, criaturas, itens, etc)
2. Crie contrato de missão (responda 3 perguntas)
3. Gere dungeon (Engrenagem 6)
4. Valide (V(E), V(I), V(P))
5. Registre ΔP
6. ΔP alimenta próxima E
7. Próxima missão usa E modificado

**Loop infinito.**

---

## 🔗 Integração com Blocos Anteriores

- **Bloco 1** define: Circuito (este livro É o circuito)
- **Bloco 2** define: Tipos (cada elemento tem tipo)
- **Bloco 3** define: Templates (cada tipo tem forma)
- **Bloco 4** define: O que jogador cria (entrada)
- **Bloco 5** (ESTE): Cria missões a partir de E
- **Bloco 6** testa: Se uma missão funciona de verdade

---

## ✨ Saída deste Bloco

- [x] Contrato de Missão definido
- [x] Regras de Encaixe (3 perguntas)
- [x] Portabilidade (P/Per/L)
- [x] Persistência ΔP tabelável
- [x] Engrenagem 6 para gerar
- [x] Validação V(E), V(I), V(P)
- [ ] Próximo: BLOCO 6 (Ciclo Completo)

---

**Status:** ✅ Completo  
**Pode avançar?** Sim → BLOCO 6
