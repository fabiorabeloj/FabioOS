---
tipo: runtime
area: 30_Projetos
projeto: PRIMUS
status: ativo-local
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, runtime, sqlite, fastapi, interface]
---

# Runtime PRIMUS Index Local

## Funcao

Registrar a interface local ja existente do PRIMUS para consulta do indice extraido de livros/fontes.

## Localizacao

```text
C:\Users\user\Desktop\Projeto\primus-site
```

Banco:

```text
C:\Users\user\Desktop\Projeto\primus-site\primus.sqlite
```

Saida original:

```text
C:\Users\user\Desktop\Projeto\primus_out_20251230_055048
```

## Estado Validado

Servidor local validado em:

```text
http://127.0.0.1:8819/
```

Busca de teste:

```text
http://127.0.0.1:8819/?q=Juramento&book=phb&limit=5
```

Resultado: HTTP 200, interface carregando registros do PHB.

## Banco

| Item | Valor |
|---|---|
| tabela principal | records |
| total de registros | 10788 |
| phb | 3880 |
| dmg | 3629 |
| mm | 3094 |
| classes_compendio | 185 |

Categorias:

- ENTIDADES;
- EVENTOS;
- FUNCOES;
- GRUPOS;
- INDEFINIDO;
- LOCAIS;
- OBJETOS.

## Correcao Aplicada Fora do Repo

O app externo `C:\Users\user\Desktop\Projeto\primus-site\app.py` usava a assinatura antiga de `TemplateResponse`.

Foi feita correcao minima para a assinatura atual:

```text
TemplateResponse(request=request, name="index.html", context={...})
```

Essa alteracao nao esta versionada no FabioOS porque o app esta fora do repositorio.

## Como Iniciar

Use:

```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\user\Desktop\FabioOs\FabioOs\60_Sistemas\Scripts\start_primus_index.ps1"
```

Ou abra diretamente se ja estiver rodando:

```text
http://127.0.0.1:8819/
```

## Relacao com PRIMUS 5.6

Este runtime resolve uma parte concreta do gargalo do PRIMUS:

- permite consultar entidades por nome/texto;
- mostra livro e pagina;
- ajuda a validar `CatalogEntries`;
- pode alimentar V(E);
- pode servir como primeira UI tecnica antes da Cantina completa.

## Limites

- classificacao heuristica;
- muitos registros ainda em `INDEFINIDO`;
- nao substitui validacao humana;
- nao altera WorldState;
- nao executa missoes;
- nao e ainda parte do repositotio FabioOS.

## Proxima Acao

Usar o PRIMUS Index para validar as 5 CatalogEntries prioritarias em [[30_Projetos/PRIMUS/Validacao_VE_Lote_0001_PRIMUS]].
