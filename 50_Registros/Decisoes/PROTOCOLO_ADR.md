---
tipo: protocolo
area: 50_Registros
projeto: FabioOS
status: ativo
autor: Claude (arquiteto-chefe)
criado_em: 2026-07-02
tags: [fabios, adr, governanca, autoridade, decisao]
---

# Protocolo ADR — autoridade de decisão

> Criado após o achado de 2026-07-02: 4 ADRs de infraestrutura marcadas `aceito`
> pelo próprio agente autor, sem ratificação humana. Conteúdo era bom; o furo era
> de **autoridade** — se qualquer agente aceita a própria decisão de arquitetura,
> governança não existe.

## Regras

1. **ADR nasce `proposto`.** Sempre. Sem exceção, inclusive as do lead.
2. **Vira `aceito` apenas com ratificação:**
   - do **Fabio** (palavra dele no chat/digest/barramento basta — o agente registra), ou
   - do **lead (Claude)** para decisões dentro da zona técnica dele, com campo
     `ratificado_por: claude (lead)` + justificativa de 1 linha.
3. **Nenhum agente ratifica a própria ADR.** Autor ≠ ratificador, sempre.
4. **Frontmatter obrigatório:** `status:` (proposto | proposto-aguardando-ratificacao |
   aceito | rejeitado | superado) e, quando aceito, `ratificado_por:` + `ratificado_em:`.
5. **Rejeição/superação não apaga:** ADR rejeitada permanece no vault com o motivo.
6. ADRs de **infraestrutura/custo/canal externo** exigem ratificação do **Fabio**
   (não bastando o lead) — é onde mora o risco de escopo e dinheiro.

## Fila de ratificação atual

| ADR | Autor | Aguardando |
|---|---|---|
| [[ADR_2026-07-02_MEGATRON_Infra_Distribuida_Modular]] | codex | Fabio (infra) |
| [[ADR_2026-07-02_Tokens_vs_Hardware_MEGATRON]] | codex | Fabio (custo) |
| [[ADR_2026-07-02_LLM_Orchestrator_Compute_Manager_MEGATRON]] | codex | Fabio (infra) |
| [[ADR_2026-07-02_OpenClaw_Gateway_De_Borda]] | codex | Fabio (canal) |

*Estas 4 entram no digest da manhã como decisões em lote (a/b/c/d).*
