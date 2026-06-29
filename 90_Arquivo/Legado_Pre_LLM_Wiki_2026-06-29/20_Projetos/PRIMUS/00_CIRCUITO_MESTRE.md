---
tipo: projeto
area: criatividade
status: ativo
tags: [PRIMUS, RPG, circuito, E-I-P, persistência]
criado_em: 2026-06-25
---

# PRIMUS — O Circuito Mestre (E → I → P → E → I → P...)

**PRIMUS não é um jogo. É um SISTEMA VIVO que evolui a cada ciclo.**

---

## 🔄 O Circuito Fundamental

```
┌─────────────────────────────────────────┐
│                                         │
│  E (Enciclopédia)                       │
│  ↓ Alimentada por ΔP anterior           │
│  I (Instância)                          │
│  ↓ Criada a partir de E                 │
│  P (Persistência)                       │
│  ↓ ΔP registrado (mudanças permanentes) │
│  └──→ Volta para E (próximo ciclo)      │
│                                         │
└─────────────────────────────────────────┘
```

**O sistema NÃO termina em P. Volta para E.**

---

## 🎯 O que significa cada componente

### **E — Enciclopédia**
**O banco conceitual do mundo PRIMUS**

- Raças, classes, backgrounds, feats, spells
- Criaturas, NPCs, deidades
- Planos, regiões, locais, dungeons
- Facções, organizações
- Regras, geradores

**Alimentação:** Todos os dados que a instância anterior não mudou + ΔP da instância anterior

**Saída:** 20+ entradas que vão gerar uma instância

---

### **I — Instância**
**O mundo MATERIALIZADO (uma missão, um encontro, um dungeon)**

Pipeline de materialização:
1. **T1 Captura** — Pega 20 entradas de E
2. **T2 Materialização** — Transforma em estrutura viva (dungeon, encontro)
3. **T3 Integração** — Conecta elementos (NPCs interagem, encontros se encadeiam)
4. **T4 Instanciamento** — Cria instância playable (pronta para jogar)

**Saída:** Uma missão (Missão 0001, 0002, etc) completamente funcional

---

### **P — Persistência (ΔP)**
**As mudanças que ficam permanentes**

O que muda em uma missão:
- **Flags** — Booleanos (rei morreu? sim/não)
- **Itens** — Tesouro conquistado
- **Mortes** — Criaturas/NPCs eliminados
- **Reputação** — Facções aumentam/diminuem
- **Conhecimento** — Novo lore descoberto
- **Danos** — Estruturas danificadas
- **Novos NPCs** — Personagens criados pela instância

**P não fica isolado. ΔP (Delta P) volta para E:**
```
ΔP = {flags[], items[], deaths[], reputation{}, knowledge[], damage[], newNPCs[]}
     ↓
Alimenta E da próxima instância
     ↓
Próxima I usa E modificado
```

---

## 📊 O Circuito em Ação (Exemplo)

### Ciclo 1:
```
E (v1): Rei vivo, 10 goblins, tesouro no baú
  ↓
I: Missão 0001 — Matar goblins, salvar rei
  ↓
P: ΔP₁ = {rei.morto=false, goblins.killed=10, tesouro.taken=true, reputacao.coroa+10}
  ↓
E (v2): E original + ΔP₁
        Rei vivo (mas com cicatriz), 0 goblins, baú vazio, coroa gosta de você
```

### Ciclo 2:
```
E (v2): Rei vivo, 0 goblins, baú vazio, coroa+10 reputação
  ↓
I: Missão 0002 — Rei te dá nova missão (porque está vivo + te gosta)
  ↓
P: ΔP₂ = {rei.confia_em_você=true, nova_inimizade_aparece=true}
  ↓
E (v3): E(v2) + ΔP₂
        Rei vivo + confia em você, inimigo X agora existe
```

**Vê? O mundo EVOLUI. Não reset. Não recomeça. MUDA.**

---

## 🏗️ Os 6 Blocos (Estrutura para Implementar)

| Bloco | Função | Saída |
|-------|--------|-------|
| **1. Mapa do Sistema** | Define E→I→P, Prisma, Pipeline | Página de definições |
| **2. Sistema de Tipos** | Lista 15+ tipos de entidades | Dicionário tipagem |
| **3. Templates por Família** | Define forma de cada tipo | 4-8 templates curtos |
| **4. Livro do Jogador** | O que o jogador pode fazer | Criação + jogo rápido |
| **5. Livro do Mestre** | Motor (como sistema funciona) | Regras operacionais |
| **6. Ciclo Completo** | Prova que funciona | Missão 0001 viva |

**Ordem é fixa: 1→2→3→4→5→6**

Se inverter, volta o "texto curto".

---

## ✨ O que torna PRIMUS especial

**Não é "um jogo".**

É **uma máquina de criar mundos que evoluem**.

- Mundo muda a cada missão (não reset)
- Mudanças afetam próximas missões
- Consequências importam
- História é viva

---

## 🚀 Próximos Passos

- [ ] BLOCO 1: Fixar Mapa do Sistema (E→I→P definidos)
- [ ] BLOCO 2: Criar Sistema de Tipos (dicionário)
- [ ] BLOCO 3: Definir Templates por Família
- [ ] BLOCO 4: Montar Livro do Jogador
- [ ] BLOCO 5: Montar Livro do Mestre
- [ ] BLOCO 6: Executar Missão 0001 completa

---

**Centro conceitual:** PRIMUS = [[Continuidade da Vida]] em RPG form  
**Filosofia:** Persistência > Reset  
**Objetivo:** Sistema vivo, não jogo morto

---

**Status:** 🟡 Estrutura em criação  
**Prioridade:** 🔴 Crítica (base de tudo)
