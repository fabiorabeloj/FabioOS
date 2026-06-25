---
tipo: projeto
area: criatividade
status: ativo
tags: [PRIMUS, próximos-passos, roadmap, execução]
criado_em: 2026-06-25
---

# PRÓXIMOS PASSOS — Roteiro Executável

**Objetivo:** Transformar PRIMUS de estrutura em jogo vivo.

---

## 🎯 HOJE (2-3 horas)

### [ ] 1. Ler os 6 Blocos (revisão)
**Tempo:** 30 min  
**Arquivos:**
- `00_CIRCUITO_MESTRE.md` — Entenda o E→I→P
- `01_SISTEMA_DEFINICOES.md` — 3 fixações
- `02_TIPOS_PRIMUS.md` — 28 tipos

**Resultado:** Você sabe exatamente o que PRIMUS é.

### [ ] 2. Começar a Preencher BLOCO 4 (Livro do Jogador)
**Tempo:** 1 hora  
**O que fazer:**
- Abra `04_LIVRO_DO_JOGADOR.md`
- Preencha Seção 1: 3 raças (Humano, Elfo, Anão)
  - Nome, traços, atributos, linguagens, nomes típicos
- Use `03_TEMPLATES_FAMILIA.md` como guia

**Exemplo preenchido:**
```yaml
# Humano
name: Human
traits:
  - +1 atributo geral
  - +2 talentos
size: Medium
speed: 30 pés
languages: Common

# Elfo
name: Elf
traits:
  - +2 Dexterity
  - Darkvision 60 pés
  - Advantage contra encantamentos
ability_scores:
  dexterity: +2
  intelligence: +1
size: Medium
speed: 30 pés
languages: Common, Elvish
```

**Resultado:** 3 raças jogáveis prontas.

### [ ] 3. Documentar 2 Classes
**Tempo:** 1 hora  
**O que fazer:**
- Seção 2: Mago e Guerreiro
  - Nome, hit die, proficiências, features por nível

**Exemplo:**
```yaml
# Mago
name: Wizard
hit_die: d6
spellcasting:
  ability: Intelligence
  spell_slots: [2, 2, 2, 2, 2]
features:
  level_1: Spellcasting
  level_2: Spell Recovery
  level_6: Portent

# Guerreiro
name: Fighter
hit_die: d10
proficiencies:
  armor: All
  weapons: All
features:
  level_1: Fighting Style
  level_2: Action Surge
  level_5: Extra Attack
```

**Resultado:** 2 classes jogáveis prontas.

---

## 📅 ESTA SEMANA (5-7 horas)

### [ ] 4. Completar BLOCO 4 (Livro do Jogador)
**Tempo:** 3 horas  
**O que fazer:**
- Seção 3: 3 antecedentes (Soldado, Mercador, Criminoso)
- Seção 4: Listar 15 itens comuns
- Seção 5: Descrever 10 talentos

### [ ] 5. Revisar e Testar BLOCO 5
**Tempo:** 2 horas  
**O que fazer:**
- Ler `05_LIVRO_DO_MESTRE.md` completamente
- Entender: Contrato, 3 perguntas, ΔP

### [ ] 6. Preparar BLOCO 6 (Missão 0001)
**Tempo:** 2 horas  
**O que fazer:**
- Revisar `06_MISSAO_0001.md`
- Garantir que todas as 20 entidades estão definidas
- Testar: Consegue responder as 3 perguntas?
  - Onde entra? → Caverna do Dragão Verde
  - Com quem interage? → Goblins, Orc, Troll, Dragão
  - O que muda? → ΔP registrado

---

## 🎮 PRÓXIMAS 2 SEMANAS (Execução)

### [ ] 7. Rodar Missão 0001 (Teste Real)
**Tempo:** 3-4 horas  
**O que fazer:**
- Convida um ou mais jogadores
- Executar Caverna do Dragão Verde
- Registrar ΔP REAL (o que realmente aconteceu)

**Checklist:**
- [ ] Personagem criado com BLOCO 4 ✓
- [ ] Entrou em Caverna do Dragão Verde ✓
- [ ] Completou Layer 1 ✓
- [ ] Completou Layer 2 ✓
- [ ] Venceu Dragão ✓
- [ ] ΔP registrado em YAML ✓

### [ ] 8. Modificar E com ΔP Real
**Tempo:** 1 hora  
**O que fazer:**
- Pegue o ΔP real da Missão 0001
- Crie E(v2) = E(v1) + ΔP_real
- Documente em novo arquivo

### [ ] 9. Gerar Missão 0002
**Tempo:** 2 horas  
**O que fazer:**
- Use BLOCO 5 (Livro do Mestre)
- Pegue E(v2)
- Crie nova missão que MUDA o mundo
- Exemplo: "Irmãos do dragão atacam. Princesa ajuda."

### [ ] 10. Rodar Missão 0002
**Tempo:** 3-4 horas  
**O que fazer:**
- Execute com mesmos jogadores
- Veja como E(v2) mudou a história
- Registre novo ΔP

---

## 🚀 META FINAL (Este mês)

**Provar que PRIMUS funciona:**

✅ E→I→P→E ciclo completo rodado  
✅ Mundo evoluiu de Missão 0001 para 0002  
✅ Consequências importam (o que você fez mudou próxima missão)  
✅ Sistema é vivo (não reset)  

**Se conseguir isto, PRIMUS está pronto para escala.**

---

## 📊 Métricas de Sucesso

| Objetivo | Métrica | Status |
|----------|---------|--------|
| Raças criadas | 5+ raças completas | ⬜ Não começou |
| Classes criadas | 5+ classes completas | ⬜ Não começou |
| Itens documentados | 20+ itens | ⬜ Não começou |
| Missão 0001 rodada | 1 execução completa | ⬜ Não começou |
| ΔP registrado | YAML com mudanças reais | ⬜ Não começou |
| Missão 0002 rodada | 1 execução com E(v2) | ⬜ Não começou |
| Mundo evoluiu | Diferenças visíveis | ⬜ Não começou |

---

## 🎯 Checklist Rápido (HOJE)

- [ ] Leu CIRCUITO_MESTRE
- [ ] Leu BLOCO 1, 2, 3
- [ ] Entendeu E→I→P→E
- [ ] Começou BLOCO 4 (3 raças)
- [ ] Documentou 2 classes
- [ ] Sabe o que fazer próxima semana

---

## ⚠️ Armadilhas a Evitar

❌ **Não comece a pensar em novas coisas** — Execute blocos 1-6 PRIMEIRO  
❌ **Não inverta a ordem** — 1→2→3→4→5→6 é fixo  
❌ **Não misture templates** — Template RACE ≠ Template PLANE  
❌ **Não skip ΔP** — Persistência é o coração do sistema  
❌ **Não desista após Missão 0001** — A prova está em rodar 0002 com E modificado  

---

## 📝 Integração com [[Continuidade_da_Vida]]

PRIMUS alimenta:
- **[[Cérebro]]**: Conhecimento sobre worldbuilding e design de sistemas
- **[[Criatividade]]**: Criação de raças, classes, dungeons
- **[[Identidade]]**: Persistência e evolução (Continuidade)

Este projeto é **100% [[Continuidade da Vida]]**.

---

**Status:** 🟡 Blocos estruturados, aguardando execução  
**Próximo passo imediato:** Comece HOJE com Blocos 1-3 + BLOCO 4 (3 raças)
