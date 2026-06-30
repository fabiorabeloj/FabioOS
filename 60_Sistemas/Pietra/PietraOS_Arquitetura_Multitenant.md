---
tipo: referencia
area: 60_Sistemas
projeto: PietraOS
status: ativo
autor: Claude (arquiteto-chefe)
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [pietraos, multitenant, arquitetura, produto, escola, inbox-operacional]
---

# PietraOS — Arquitetura multi-tenant (o que é Pietra vs Colégio Pietra)

## A confusão resolvida (3 níveis)

| Nível | O que é | Quem usa |
|---|---|---|
| **Motor (Inbox Operacional)** | Genérico, agnóstico de domínio. Classifica→risco→roteia→sugere→registra→relatório. | qualquer vertical |
| **PietraOS** | O **produto da vertical Escola** — para **todas as escolas**. | qualquer escola-cliente |
| **Colégio Pietra** | A **primeira instância (tenant #0)** — o laboratório. | o piloto |

**PietraOS NÃO é só do Colégio Pietra.** É o produto para todas as futuras escolas.
Colégio Pietra é apenas o primeiro tenant. O nome homenageia a origem.

## Multi-tenant desde o dia 1

```text
PietraOS (vertical escola)
 ├── config da vertical (compartilhada)   60_Sistemas/Pietra/verticais/escola/config.json
 │     categorias, matriz de risco, matriz de roteamento, templates  ← o MOAT
 └── tenants/ (dados isolados por escola)  60_Sistemas/Pietra/tenants/<tenant>/   (gitignored)
       ├── colegio-pietra/ atendimentos.jsonl + overrides (setores, FAQ, base, nº WhatsApp)
       ├── escola-x/        ...
       └── escola-y/        ...
```

- **A config da vertical é compartilhada** (todas as escolas usam as mesmas categorias/risco).
- **Os dados são por tenant e isolados** (mensagens de pais nunca se misturam entre escolas; LGPD).
- Cada tenant pode **sobrescrever** setores, FAQ e base sem mudar código.

## Por que isso importa (negócio)

- **Implantar uma nova escola = criar um tenant + ajustar overrides.** Sem recodar.
- O **moat é a biblioteca de configs** (categorias/risco/templates por vertical), não o código.
- O mesmo motor vira **OdontoOS / ContábilOS / PetOS** trocando a config da vertical.

## Onde se encaixa no FabioOS

Modelo Formal separa **FabioOS** (o organismo do Fabio), **PietraOS** (produto escolar)
e **PrimusOS** (RPG). O motor Inbox Operacional vive no FabioOS; PietraOS é a primeira
productização comercial sobre ele.

## Relações
- [[60_Sistemas/Pietra/pietra_inbox]]
- [[60_Sistemas/FabioOS/specs/2026-06-30_inbox-operacional-pietraos]]
- [[60_Sistemas/Pietra/Politica_Dados_LGPD_PietraOS]]
- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]
