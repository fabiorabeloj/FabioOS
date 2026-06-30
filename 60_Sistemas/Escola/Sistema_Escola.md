---
tipo: sistema
area: 60_Sistemas
projeto: FabioOS
sistema: Escola
status: ativo
versao: 1.0
tags: [escola, docência, materiais, provas, aulas, pietra, camada-5]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Sistema Escola

## Função

Organizar a produção docente dentro do FabioOS — provas, revisões, gabaritos, aulas, comunicados e cronogramas — com padrão, velocidade e rastreabilidade.

**Critério de sucesso da Fase 8:**

> Produzir um material escolar do zero usando o FabioOS em menos de 30 minutos.

## Contexto

Sem sistema, a produção docente é caótica: provas em arquivos soltos, gabaritos perdidos, comunicados sem histórico, revisões refeitas do zero a cada bimestre. O FabioOS centraliza, versiona e reutiliza tudo.

---

## 1. Módulos do Sistema Escola

| Módulo | Função | Status |
|---|---|---|
| **Provas** | Criar avaliações estruturadas com habilidade, enunciado, gabarito e critério | ativo |
| **Revisões** | Produzir materiais de revisão com explicação, exemplos e exercícios | ativo |
| **Gabaritos** | Gabaritos separados do enunciado, com critério de correção | ativo |
| **Aulas** | Planos de aula e roteiros por disciplina, turma e bimestre | ativo |
| **Comunicados** | Comunicados para pais, alunos e equipe pedagógica | ativo |
| **Cronogramas** | Planejamento bimestral e anual por disciplina | ativo |
| **Correções** | Registro de correções, notas e análise de desempenho | pendente |
| **Modelos** | Templates reutilizáveis de cada tipo de material | ativo |

---

## 2. Disciplinas e turmas

| Disciplina | Código | Turmas atendidas |
|---|---|---|
| Geografia | GEO | 6A, 6B, 7A, 7B, 8A, 8B, 9A, 9B |
| Filosofia | FIL | 6A, 6B, 7A, 7B, 8A, 8B, 9A, 9B |

**Regra:** nunca misturar GEO e FIL no mesmo material sem indicar claramente. Cada arquivo serve uma única disciplina.

---

## 3. Convenções de nomenclatura

Padrão obrigatório:

```
[ANO]_[TURMA]_[DISCIPLINA]_[BIMESTRE]_[TIPO].md
```

| Campo | Valores |
|---|---|
| ANO | `2026` |
| TURMA | `6A`, `6B`, `7A`, `7B`, `8A`, `8B`, `9A`, `9B` |
| DISCIPLINA | `GEO`, `FIL` |
| BIMESTRE | `B1`, `B2`, `B3`, `B4` |
| TIPO | `PROVA`, `REVISAO`, `GABARITO`, `AULA`, `COMUNICADO`, `CRONOGRAMA`, `CORRECAO` |

Exemplos:

```
2026_9A_GEO_B2_PROVA.md
2026_8B_FIL_B1_REVISAO.md
2026_7A_GEO_B3_GABARITO.md
2026_9B_FIL_B4_AULA.md
```

---

## 4. Onde ficam os arquivos

```
60_Sistemas/Escola/
├── Sistema_Escola.md        ← este arquivo
├── templates/               ← modelos reutilizáveis
│   ├── TEMPLATE_PROVA.md
│   ├── TEMPLATE_REVISAO.md
│   ├── TEMPLATE_GABARITO.md
│   └── TEMPLATE_COMUNICADO.md
│
05_Raw_Sources/_compat_sources/docs/               ← materiais externos que chegam como fonte bruta
                               (ex: PDF do livro, aviso da escola)

30_Projetos/ ou 00_Inbox/   ← rascunhos em andamento

50_Registros/               ← registros de entregas, cronograma de aplicação

40_Wiki/_compat_wiki/projetos/escola.md     ← visão geral navegável do sistema
```

O destino final de cada material **produzido** é em `60_Sistemas/Escola/` ou em uma pasta de projeto ativo.

---

## 5. Fluxo de produção por módulo

### Prova

```
1. Identificar: turma, disciplina, bimestre, conteúdo, habilidades
2. Usar TEMPLATE_PROVA.md como base
3. Redigir questões com: enunciado, alternativas (se objetiva), habilidade avaliada
4. Separar gabarito em TEMPLATE_GABARITO.md
5. Revisar: nível de linguagem, clareza dos comandos, adequação ao bimestre
6. Nomear: 2026_[TURMA]_[DISC]_[BIM]_PROVA.md
7. Commitar
```

### Revisão

```
1. Identificar: turma, disciplina, bimestre, pontos de dificuldade
2. Usar TEMPLATE_REVISAO.md como base
3. Estruturar: explicação → exemplo → exercício → gabarito do exercício
4. Linguagem adequada ao nível dos alunos
5. Nomear: 2026_[TURMA]_[DISC]_[BIM]_REVISAO.md
6. Commitar
```

### Comunicado

```
1. Definir destinatário: pais, alunos, equipe
2. Usar TEMPLATE_COMUNICADO.md como base
3. Redigir com: data, assunto, corpo, assinatura
4. Revisar antes de enviar
5. Nomear: COMUNICADO_[YYYY-MM-DD]_[ASSUNTO-SLUG].md
6. Aprovação humana obrigatória antes do envio
```

---

## 6. Regras do sistema

1. **Separar sempre:** ano, turma, disciplina, bimestre e tipo antes de criar qualquer arquivo.
2. **Nunca misturar** GEO e FIL no mesmo arquivo sem separação clara de seção.
3. **Linguagem adequada ao nível:** 6º ano ≠ 9º ano — ajustar vocabulário, complexidade e comandos.
4. **Para provas, diferenciar sempre:**
   - conteúdo avaliado;
   - habilidade esperada;
   - comando da questão (o que o aluno deve fazer);
   - gabarito;
   - critério de correção (o que vale pontos e o que não vale).
5. **Para revisões:** priorizar explicação clara, exemplos concretos, exercícios progressivos.
6. **Aprovação humana obrigatória** antes de qualquer envio a alunos, pais ou equipe.
7. **Dados de alunos** (nomes, notas, desempenho individual) nunca entram em arquivos públicos ou commitados sem anonimização.

---

## 7. Comandos planejados para o Claude Code

| Comando | Função |
|---|---|
| `/criar-prova` | Gerar rascunho de prova a partir de parâmetros |
| `/criar-revisao` | Gerar revisão estruturada por bimestre e conteúdo |
| `/criar-gabarito` | Extrair gabarito de uma prova existente |
| `/criar-comunicado` | Gerar comunicado por tipo e destinatário |
| `/preparar-aula` | Gerar roteiro de aula por disciplina e turma |
| `/organizar-cronograma` | Montar cronograma bimestral de conteúdos |
| `/corrigir-simulado` | Estruturar análise de desempenho por questão |

Status: planejados — implementação na Fase 8.5.

---

## 8. Agente escolar

O agente `school-assistant` (`.claude/agents/school-assistant.md`) é o executor especializado do Sistema Escola dentro do Claude Code.

Funções:
- Aplicar as regras desta seção
- Gerar materiais no padrão do FabioOS
- Separar GEO de FIL automaticamente
- Adequar linguagem ao nível das turmas

Status atual: esqueleto criado — expansão prevista para Fase 8.5.

---

## 9. Relação com o Sistema Pietra

O Sistema Escola gera os materiais. O Sistema Pietra comunica.

```
Sistema Escola
  ↓ produz
Prova / Comunicado / Aviso
  ↓ distribui
Sistema Pietra (OpenClaw → WhatsApp de pais)
```

Nenhuma comunicação sai pelo Pietra sem aprovação do Sistema Escola.

---

## Relações

- [[40_Wiki/_compat_wiki/projetos/escola]]
- [[60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
- [[40_Wiki/_compat_wiki/indices/mapa-fabios]]

## Próximas ações

- [ ] Testar TEMPLATE_PROVA.md com uma prova real de GEO B2 para 9A
- [ ] Testar TEMPLATE_REVISAO.md com revisão de FIL B1 para 8B
- [ ] Implementar comandos `/criar-prova` e `/criar-revisao`
- [ ] Expandir agente `school-assistant` com regras desta documentação
- [ ] Criar cronograma bimestral de 2026 para GEO e FIL
