---
tipo: glossario
area: 00_Arquitetura
projeto: FabioOS
status: ativo
tags: [glossario, vocabulario, megatron, pietraos, primusos, dominios, aliases]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Glossário Canônico do FabioOS

## Função

Define o vocabulário oficial do FabioOS e os apelidos (aliases) que preservam os nomes antigos. Evita vocabulário dividido entre o modelo formal e o resto do vault.

## Contexto

A partir do [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON|Modelo Formal]], o sistema adota nomes de domínio no estilo "OS". Os nomes antigos continuam válidos como apelidos, então links existentes não quebram.

## Vocabulário oficial

| Termo canônico | Apelidos / nome antigo | Nota principal | O que é |
|---|---|---|---|
| **MEGATRON** | Interface, Interface única, JARVIS-do-Fabio | [[60_Sistemas/FabioOS/Visao_Interface_FabioOS]] | Interface cognitiva universal — orquestra o ecossistema de inteligências |
| **FabioOS** | — | [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]] | Plataforma cognitiva base + domínio pessoal |
| **PietraOS** | Sistema Pietra, Atendimento Pietra | [[40_Wiki/FabioOS/PietraOS]] | Domínio institucional (Colégio Pietra), futuro SaaS escolar |
| **PrimusOS** | PRIMUS | [[40_Wiki/PRIMUS/PrimusOS]] | Domínio narrativo — digestão de mundos persistentes |

## Regra de uso

- Em documentos **novos de arquitetura/domínio**, usar o termo canônico (MEGATRON, PietraOS, PrimusOS).
- Em documentos **operacionais existentes**, os nomes antigos continuam válidos (são aliases).
- [[40_Wiki/FabioOS/PietraOS|PietraOS]], [[40_Wiki/PRIMUS/PrimusOS|PrimusOS]] e [[10_Dashboard/MEGATRON|MEGATRON]] sao os hubs canonicos atuais.
- **Domínios compartilham infraestrutura, não compartilham dados automaticamente** (regra do Modelo Formal).

## Relações

- [[00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON]]
- [[60_Sistemas/FabioOS/Visao_Interface_FabioOS]]
- [[60_Sistemas/Pietra/Sistema_Pietra]]
- [[40_Wiki/PRIMUS/PrimusOS]]
- [[40_Wiki/_compat_wiki/indices/mapa-fabios]]

## Próximas ações

- [ ] Ao criar PietraOS como produto, separar dados institucionais dos pessoais por camada explícita
- [ ] Atualizar `40_Wiki/_compat_wiki/indices/mapa-fabios.md` com os termos canônicos quando conveniente
