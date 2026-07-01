---
tipo: spec
area: 60_Sistemas
projeto: FabioOS
status: aceito
fase: 20
autor: Claude (arquiteto-chefe / MEGATRON Core)
criado_em: 2026-07-01
tags: [fabios, megatron, core, intake-universal, taxonomia, sensibilidade, roteamento, governanca]
---

# MEGATRON Core Spec v0.1 — a lógica cognitiva do FabioOS

> O contrato que **Claude governa**, **Codex implementa** e **Cursor exibe**.
> Não é arquitetura nova: consolida o que já existe (PietraOS, Nota vs Dado, LGPD,
> classificar do MEGATRON) na regra única de decisão do sistema.
> **Núcleo do produto = Intake Universal + controle humano**, não o Gmail.

## 1. O contrato universal de entrada

Toda entrada — de qualquer canal — vira o MESMO objeto antes de qualquer ação:

```json
{
  "id": "intake_<ts>_<hash>",
  "source": "gmail|whatsapp|pdf|drive|mobile|manual|obsidian|github",
  "received_at": "ISO-8601",
  "sender": "...", "subject": "...",
  "raw_content_ref": "caminho gitignored (nunca o corpo bruto aqui)",
  "summary": "1-3 linhas",
  "domain": "fabios|pietraos|escolaos|primus|financeiro|pessoal|tecnico|juridico|saude|spam",
  "sensitivity": "public|internal|private|restricted|no_rag|forbidden_external",
  "urgency": "none|low|medium|high|critical",
  "suggested_agent": "...", "suggested_action": "...",
  "requires_human_approval": true,
  "status": "captured|classified|waiting_approval|approved|executing|executed|archived|blocked|failed",
  "log_ref": "..."
}
```

## 2. Taxonomia de domínios

`fabios` (o próprio sistema/IA) · `pietraos` (atendimento escolar/WhatsApp pais) ·
`escolaos` (produção pedagógica: provas/revisões/aulas) · `primus` (RPG/mundo) ·
`financeiro` · `pessoal` · `tecnico` (erros/infra) · `juridico` · `saude` · `spam`.

## 3. Política de sensibilidade (a trava)

| Nível | Significado | Regra |
|---|---|---|
| public | pode circular | livre |
| internal | interno da operação | sem exposição externa |
| private | dado de pessoa (pai, aluno) | humano no loop; sem RAG sem curadoria |
| restricted | sensível (saúde, jurídico, financeiro delicado) | **nunca auto**; escala humano |
| no_rag | jamais indexar | fica fora do RAG por definição |
| forbidden_external | jamais sair da máquina | token/senha/credencial |

**Regra máxima:** nada externo sai sem aprovação; nada sensível indexa sozinho;
token/credencial nunca aparece em log; nada é apagado/publicado automaticamente.

## 4. Roteamento (domínio → agente)

pai/responsável → `pietraos` · coordenação/prova/revisão → `escolaos` (agente escolar) ·
IA/sistema → `fabios` (MEGATRON) · RPG → `primus` (Codex) · fatura/banco → `financeiro` ·
erro de sistema → `tecnico` · saúde/jurídico → `restricted` + humano · irrelevante → `spam`.

## 5. Política de decisão — o que a entrada vira

| Vira | Quando |
|---|---|
| **nota** | tem valor de conhecimento/registro (regra [[ADR_2026-07-01_Nota_vs_Dado_Ingestao_Obsidian|Nota vs Dado]]: ideia, não dado bruto) |
| **tarefa** | exige ação futura (produzir prova, responder, providenciar doc) |
| **resposta sugerida** | pede resposta e risco permite (baixo/médio) |
| **alerta** | urgência alta/crítica ou sensível → sobe na fila |
| **descarte** | spam/irrelevante |
| **bloqueio+escala** | restricted/crítico → humano decide, sistema não age |

## 6. Aprovação humana

**Sempre exige aprovação:** enviar e-mail/WhatsApp real, apagar, arquivar externo,
marcar como lido, publicar, indexar RAG, qualquer ação sensível.
**Pode automático (baixo risco):** classificar, resumir, criar rascunho interno,
criar item na fila, gravar log. Padrão do sistema: **propõe, não executa.**

## 7. Gate de RAG

Nada entra no RAG sem: fonte aprovada + domínio + sensibilidade + data + responsável +
validação mínima + curadoria humana. `private/restricted/no_rag/forbidden_external`
**nunca** entram automaticamente.

## 8. Log e continuidade

Todo passo gera log (quem/quando/o quê/onde/próximo passo), sem segredo. A memória
operacional vive no Obsidian (`50_Registros`) + no barramento; a continuidade é
retomável por qualquer sessão lendo STATUS/NEXT_ACTIONS/barramento.

## 9. A prova mínima (a "porta")

```text
e-mail fake → payload universal → classificação → sensibilidade → fila "Aguardando Fabio"
→ log → nota/tarefa no Obsidian     (NENHUMA ação externa; NENHUM dado sensível exposto)
```
Depois: repetir o MESMO contrato para WhatsApp fake e PDF fake. Só então: canais reais.

## 10. Divisão (o que impede o ruído)

- **Claude (MEGATRON Core):** esta spec — taxonomia, política, roteamento, decisão, continuidade.
- **Codex (Intake Universal v0.1):** `universal_intake_schema`, dry-run seguro, conectores fake, validador, logs, saída consumível.
- **Cursor (Agentarium Secretário v0.1):** fila "Aguardando Fabio", cards, campo de comando natural, botões seguros, event log, link Obsidian.
- **n8n = tubulação · Obsidian = memória · GitHub = versão · RAG/MCP = consulta controlada.**

## Relações
- [[50_Registros/Decisoes/ADR_2026-07-01_Nota_vs_Dado_Ingestao_Obsidian]]
- [[60_Sistemas/Pietra/verticais/escola/config]] (o risco/roteamento já implementado)
- [[60_Sistemas/MEGATRON/v1/registry]] (capacidades) · [[50_Registros/Barramento_Multiagente]]
