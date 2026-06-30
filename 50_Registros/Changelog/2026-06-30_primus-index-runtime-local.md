---
tipo: changelog
area: 50_Registros
projeto: PRIMUS
status: registrado
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, runtime, sqlite, fastapi]
---

# 2026-06-30 - PRIMUS Index Runtime Local

## Entrega

Foi descoberto, validado e ativado o runtime local antigo do PRIMUS:

```text
C:\Users\user\Desktop\Projeto\primus-site
```

## Resultado

- banco `primus.sqlite` com `10788` registros;
- app FastAPI local iniciado em `http://127.0.0.1:8819/`;
- busca `Juramento` no `phb` validada com HTTP 200;
- script de partida criado em [[60_Sistemas/Scripts/start_primus_index.ps1]];
- runtime documentado em [[30_Projetos/PRIMUS/Runtime_PRIMUS_Index_Local]].

## Observacao

O app externo precisou de correcao minima em `TemplateResponse` por mudanca de compatibilidade do FastAPI/Starlette. Essa correcao foi feita fora do repo FabioOS, porque o app esta em `C:\Users\user\Desktop\Projeto\primus-site`.

## Proxima Acao

Usar o indice para validar pagina/trecho de 5 CatalogEntries prioritarias e destravar a proxima etapa do PRIMUS.
