---
tipo: wiki
area: projetos
projeto: FabioOS
sistema: Escola
status: ativo
camada: camada-5
tags: [escola, docência, materiais, provas, geografia, filosofia, camada-5]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Sistema Escola

## Função no FabioOS

[DECISÃO] O Sistema Escola é o **módulo de produção docente** do FabioOS — centraliza, padroniza e versiona a criação de provas, revisões, gabaritos, aulas e comunicados, reduzindo o tempo de produção e aumentando a rastreabilidade dos materiais.

## O que este sistema faz

[FATO] Organiza o fluxo de trabalho docente de Fabio Rabelo para as disciplinas de **Geografia (GEO)** e **Filosofia (FIL)**, do 6º ao 9º ano do ensino fundamental.

Módulos ativos:

- **Provas** — avaliações estruturadas com habilidade, enunciado, gabarito e critério de correção separados
- **Revisões** — materiais de revisão com explicação, exemplos e exercícios progressivos
- **Gabaritos** — separados do enunciado para controle interno
- **Aulas** — planos e roteiros por turma, disciplina e bimestre
- **Comunicados** — textos para pais, alunos e equipe pedagógica
- **Cronogramas** — planejamento bimestral e anual

## O que este sistema não deve fazer

- Enviar materiais a alunos ou pais sem aprovação humana explícita
- Misturar GEO e FIL no mesmo arquivo sem separação clara
- Armazenar dados individuais de alunos (nomes, notas, desempenho) em arquivos commitados sem anonimização
- Substituir o julgamento pedagógico do professor

## Convenção de nomenclatura

```
[ANO]_[TURMA]_[DISCIPLINA]_[BIMESTRE]_[TIPO].md

2026_9A_GEO_B2_PROVA.md
2026_8B_FIL_B1_REVISAO.md
2026_7A_GEO_B3_GABARITO.md
```

## Relação com outras ferramentas

| Ferramenta | Relação |
|---|---|
| [[wiki/sistemas/claude-code]] | Claude Code gera e organiza os materiais |
| [[wiki/sistemas/obsidian]] | Vault armazena e versiona todos os arquivos |
| [[wiki/sistemas/github]] | GitHub versiona o histórico de provas e materiais |
| [[wiki/projetos/pietra]] | Pietra distribui comunicados gerados pelo Escola |

## Uso atual

- [x] Documentação do sistema: `60_Sistemas/Escola/Sistema_Escola.md`
- [x] Templates: PROVA, REVISAO, GABARITO, COMUNICADO
- [x] Agente `school-assistant` (esqueleto) em `.claude/agents/`
- [x] Convenções de nome definidas no Protocolo Operacional
- [ ] Comandos `/criar-prova`, `/criar-revisao` ainda não implementados
- [ ] Nenhum material real produzido ainda — aguardando primeiro uso

## Uso futuro

- [ ] Comando `/criar-prova` — gerar rascunho por parâmetros
- [ ] Comando `/criar-revisao` — revisão estruturada por bimestre
- [ ] Cronograma bimestral 2026 para GEO e FIL
- [ ] Análise de desempenho por turma e questão (Fase 8.5)
- [ ] Integração com Sistema Pietra para distribuição de comunicados

## Critério de sucesso

[DECISÃO] A Fase 8 estará concluída quando:

> "Produzo uma prova do zero usando o FabioOS em menos de 30 minutos."

Teste objetivo: criar `2026_9A_GEO_B2_PROVA.md` com 5 questões, gabarito separado e critério de correção, do zero, em até 30 min com auxílio do Claude Code.

## Links internos

- [[60_Sistemas/Escola/Sistema_Escola]]
- [[wiki/indices/mapa-fabios]]
- [[60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
