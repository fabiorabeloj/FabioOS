---
tipo: handoff
area: 60_Sistemas
projeto: FabioOS
status: ativo
autor: Cursor (Interface)
destinatario: Claude (Maestro)
criado_em: 2026-06-30
tags: [pietraos, cursor, agentarium, inbox]
---

# Handoff Cursor → Claude — PietraOS Inbox v0.8.0

```text
de: cursor
para: claude
tipo: handoff
status: aberto
mensagem: |
  Ordem pietra_state.json ENTREGUE (v0.8.1):
  - Fonte primaria: tenants/<tenant>/pietra_state.json (pietra_state.py)
  - cores_risco do JSON aplicadas na borda/badge; acoes[] nos botoes; resumo do JSON
  - Badge de acao (bloquear_escalar/sugerir_aprovar/responder_auto)
  - Sessoes: sessions/*.json — clique no remetente para ver historico multi-turno
  - Fallback jsonl se state ausente; watcher em pietra_state.json + sessions/
  - NAO toquei pietra_conversa.py, pietra_state.py, config, RAG
  Para demo local: PIETRA_TENANT=demo-pro antes de subir backend.
```

## Teste local

```powershell
python 60_Sistemas/Pietra/pietra_inbox.py "Quero matricular meu filho" --tenant colegio-pietra --confirmar
python 60_Sistemas/Pietra/pietra_inbox.py "Segue atestado" --tenant colegio-pietra --confirmar
# reiniciar backend Agentarium -> aba PietraOS Inbox
```
