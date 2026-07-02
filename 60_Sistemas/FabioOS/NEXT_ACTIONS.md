---
tipo: next-actions
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [fabios, proximas-acoes, continuidade]
criado_em: 2026-06-27
atualizado_em: 2026-07-01
---

# NEXT ACTIONS — FabioOS

> Reescrito em 2026-07-01. A lista fóssil anterior (interinato 27–29/06) foi
> substituída — histórico está no Git. **Fonte completa do feito × não-feito:**
> [[60_Sistemas/FabioOS/Plano_Mestre_FabioOS_2026-07-01|Plano Mestre]] (§4 = pendências por dono, §5 = ordem).

## Agora — por agente

### Claude (lead)
- [ ] Redigir `summary` dentro do `megatron_core.py` (Bugbot Onda 2 — core cru vaza `texto[:180]`)
- [ ] Encerrar `INTERINATO_CODEX` (zumbi) e encerrar/renovar `MCP_FABIOOS` no Registro
- [ ] Hardening RAG 12.1 + ficha técnica — **só em janela de CPU livre, com lock**

### Codex
- [ ] **Elo sensor nº1:** export Gmail → `universal_intake_adapter` (e-mail hoje só anda manual)
- [ ] Unificar formato de id `intake_flow` × `adapter`
- [ ] Teste mínimo do ADR OpenClaw borda (OpenClaw→Intake→Agentarium→aprovação)

### Cursor
- [ ] Telefone hardcoded `config.ts` L49 → env var (Bugbot Onda 2)
- [ ] Badge de modelo no chat + reset de histórico por sessão
- [ ] Ondas 3–7 do Bugbot — aguarda gate ⑤

## Aguardando Fabio — os 7 gates (Plano Mestre §4)

- [ ] ① Push + limpeza dos blobs PDF (19 commits locais sem backup remoto)
- [ ] ② Autorizar Gmail real (leitura)
- [ ] ③ Canal WhatsApp Pietra real + tenant piloto
- [ ] ④ E-mails pessoais versionados no wiki: aceitar ou mover p/ _restrito?
- [ ] ⑤ Autorizar Bugbot Ondas 3–7
- [ ] ⑥ Teto de custo OpenRouter (chat já usa haiku-4.5, ~$0.004/msg)
- [ ] ⑦ Primeira prova real EscolaOS (templates prontos, 1 prova de GEO destrava a vertical)

## Regras que não mudam

- Push, canal externo, n8n ativo, exclusão destrutiva → **aprovação humana explícita**
- Scan de segredos (linhas adicionadas) antes de todo commit
- Lock em [[60_Sistemas/FabioOS/Registro_Frentes_Ativas]] antes de artefato compartilhado
