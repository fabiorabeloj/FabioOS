---
project: PRIMUS
object: prompt
type: procedure
status: ready
face: E
tags: [primus, n8n, captura]
---

# Prompt — n8n capturar entrada PRIMUS

```text
Quando eu enviar uma captura para o PRIMUS, classifique-a como T1 Captura.
Não trate como verdade PRIMUS.

Crie uma nota markdown em:
30_Projetos/PRIMUS/00_Inbox/

A nota deve conter:
- conteúdo bruto
- data
- origem
- suspeita de tipo PRIMUS
- fonte, se existir
- campo "status: inbox"

Depois, aguarde processamento T2 para materialização em CatalogEntry.
```
