---
tipo: índice
area: criatividade
status: ativo
aliases: [PrimusOS]
tags: [PRIMUS, índice, roadmap, sistema]
criado_em: 2026-06-25
---

# 🎮 PRIMUS — Sistema Vivo de RPG Persistente

**Versão:** 1.0  
**Status:** Estrutura completa, aguardando execução  
**Conexão:** [[Continuidade da Vida]] → [[Criatividade]]  

---

## 📚 Arquitetura (8 documentos)

### Fundação Teórica
1. **[[00_CIRCUITO_MESTRE|00 — O Circuito Mestre]]**
   - O que é E→I→P (Enciclopédia → Instância → Persistência)
   - Por que é circular (não linear)
   - Exemplo prático do loop

2. **[[01_SISTEMA_DEFINICOES|01 — Mapa do Sistema (BLOCO 1)]]**
   - Fixações: Circuito, Prisma, Pipeline T1-T4
   - Imutável e oficial

### Tipagem & Estrutura
3. **[[02_TIPOS_PRIMUS|02 — Sistema de Tipos (BLOCO 2)]]**
   - 28 tipos obrigatórios (race, class, creature, plane, etc)
   - Tabela de tipos
   - Regra: sem tipo = não entra

4. **[[03_TEMPLATES_FAMILIA|03 — Templates por Família (BLOCO 3)]]**
   - 8 templates (RACE, CLASS, PLANE, DUNGEON, CREATURE, SPELL, ITEM, NPC)
   - Simetria: Template RACE ≠ Template PLANE
   - Estrutura pronta para preencher

### Conteúdo Executável
5. **[[04_LIVRO_DO_JOGADOR|04 — Livro do Jogador (BLOCO 4)]]**
   - Raças (5+)
   - Classes (5+)
   - Antecedentes (5+)
   - Equipamento (15+ itens)
   - Talentos (10+)
   - Magias (30+)
   - Regras mínimas de criação

6. **[[05_LIVRO_DO_MESTRE|05 — Livro do Mestre (BLOCO 5)]]**
   - Contrato de Missão (objeto YAML)
   - 3 Perguntas Críticas (validação)
   - Portabilidade (P/Per/L)
   - Persistência ΔP (tabelável)
   - Engrenagem 6 (geração procedural)
   - Validação V(E), V(I), V(P)

### Prova de Conceito
7. **[[06_MISSAO_0001|06 — Ciclo Completo: Missão 0001 (BLOCO 6)]]**
   - E: 20 entidades de entrada
   - I: Caverna do Dragão Verde (instância viva)
   - P: ΔP registrado
   - Validação: Prova que sistema funciona

### Integração & Execução
8. **[[07_INTEGRACAO_COMPLETA|07 — Integração Completa]]**
   - Como os 6 blocos formam um sistema
   - Cascata de alimentação (1→2→3→4→5→6)
   - Exemplo prático: Missão 0001 → E(v2) → Missão 0002
   - Integração com [[Continuidade_da_Vida]]

9. **[[08_PROXIMOS_PASSOS|08 — Próximos Passos (Roadmap)]]**
   - HOJE: Leia blocos 1-3 + comece BLOCO 4
   - Semana: Complete BLOCO 4
   - 2 semanas: Rode Missão 0001 real
   - Meta: Ciclo E→I→P→E completo

---

## 🔄 O Circuito E→I→P

```
E (Enciclopédia) ← Banco conceitual do mundo
     ↓ pega 20 entradas
I (Instância) ← Mundo materializado (uma missão)
     ↓ cria
P (Persistência) ← Mudanças que ficam (ΔP)
     ↓ alimenta próximo
E (v2) ← Enciclopédia modificada
     ↓ ciclo infinito
```

**Não termina em P. Volta para E.** O mundo evolui a cada ciclo.

---

## 🎯 Checklist de Uso

### Para Entender
- [ ] Leia `00_CIRCUITO_MESTRE` (entenda E→I→P)
- [ ] Leia `01_SISTEMA_DEFINICOES` (fixações oficial)
- [ ] Leia `02_TIPOS_PRIMUS` (28 tipos)
- [ ] Leia `03_TEMPLATES_FAMILIA` (8 templates)

### Para Executar
- [ ] Preencha `04_LIVRO_DO_JOGADOR` (raças, classes, itens)
- [ ] Revise `05_LIVRO_DO_MESTRE` (motor funcional)
- [ ] Pronto `06_MISSAO_0001` (teste real)
- [ ] Execute `08_PROXIMOS_PASSOS` (roadmap)

### Para Validar
- [ ] Responde 3 perguntas de Encaixe?
- [ ] V(E) passa (todos os tipos válidos)?
- [ ] V(I) passa (instância é funcional)?
- [ ] V(P) passa (ΔP afeta próxima E)?

---

## 📊 Dependências Entre Blocos

```
BLOCO 1 (Definições)
    ↓ necessário para
BLOCO 2 (Tipos)
    ↓ necessário para
BLOCO 3 (Templates)
    ↓ necessário para
BLOCO 4 (Livro do Jogador)
    ↓ alimenta
E (Enciclopédia) + Pipeline T1-T4
    ↓ usa
BLOCO 5 (Livro do Mestre)
    ↓ cria
I (Instância)
    ↓ registra
BLOCO 6 (Missão 0001)
    ↓ prova
P (Persistência)
    ↓ alimenta próximo
E(v2) → BLOCO 4 novamente
    ↓ ciclo infinito
```

**Ordem é FIXA. Se inverter, volta o "texto curto".**

---

## 🚀 3 Fases de Execução

### Fase 1: Estruturação (HOJE)
**Status:** ✅ Completa  
**Saída:** 8 arquivos estruturados, prontos para preencher  

### Fase 2: Preenchimento (Esta semana)
**Status:** ⬜ Não começou  
**Ações:**
- Preencher BLOCO 4 com 5+ raças, classes, antecedentes
- Revisar BLOCO 5 e 6
- Preparar primeira execução

### Fase 3: Execução (Próximas 2 semanas)
**Status:** ⬜ Não começou  
**Ações:**
- Rodar Missão 0001 com jogadores reais
- Registrar ΔP real
- Gerar Missão 0002 com E(v2)
- Provar que ciclo funciona

---

## 🔗 Links de Integração

**[[Continuidade_da_Vida]]**
- Centro filosófico: Mundo persistente = Vida contínua
- 6 pilares que PRIMUS toca:
  - [[Cérebro]] — Conhecimento em design de sistemas
  - [[Criatividade]] — Criação de raças, dungeons, narrativas
  - [[Identidade]] — Persistência e evolução

**[[Mapa_de_PRIMUS]]**
- Versão compacta deste índice
- Visualização dos 6 blocos em mapa

**[[Escola]]** & **[[Trader]]**
- Pueden usar PRIMUS como motor (RPG para aprender)
- Exemplo: "Trader como jogo PRIMUS"

---

## 🎲 Resumo Executivo

**PRIMUS não é um jogo. É uma MÁQUINA DE CRIAR MUNDOS que evoluem.**

- ✅ **E→I→P é um circuito**, não uma sequência
- ✅ **28 tipos + 8 templates** formam a arquitetura
- ✅ **Ordem 1→2→3→4→5→6 é fixa** (imutável)
- ✅ **Persistência é o coração** (ΔP alimenta próxima E)
- ✅ **Mundo não reseta, EVOLUI**

**Próximo passo:** Preencher BLOCO 4 com conteúdo real.

---

**Criado em:** 2026-06-25  
**Versão:** 1.0 (estrutura completa)  
**Pronto para:** Fase 2 (preenchimento)  
**Liderança:** [[Continuidade_da_Vida]] (Criatividade)
