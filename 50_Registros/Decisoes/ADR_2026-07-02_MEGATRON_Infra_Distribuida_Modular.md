---
tipo: adr
area: 50_Registros
projeto: MEGATRON
status: proposto-aguardando-ratificacao
tags: [adr, fabios, megatron, hardware, infraestrutura, nos]
criado_em: 2026-07-02
---

# ADR - MEGATRON como Infraestrutura Distribuida Modular

## Contexto

Fabio solicitou uma arquitetura de hardware para o MEGATRON/FabioOS com operacao 24/7, baixo consumo, energia solar futura, IA local, crescimento modular e alta disponibilidade.

O risco seria tratar a compra de um mini PC ou GPU como "o MEGATRON". Isso tornaria o sistema dependente de hardware especifico e fragil frente a expansoes futuras.

## Decisao

O MEGATRON sera tratado como infraestrutura distribuida por capacidades.

O hardware alvo pode incluir AOOSTAR/Core, eGPU, NAS e workers, mas o codigo deve depender de:

- `capabilities`;
- `services`;
- `data_classes`;
- `health`;
- `priority`;
- `policy`.

E nao depender de:

- nome comercial do equipamento;
- caminho local unico;
- GPU obrigatoria;
- banco unico;
- porta externa aberta sem controle.

## Consequencias

### Positivas

- O Core pode mudar de maquina sem reescrever agentes.
- A GPU pode entrar depois.
- O NAS pode entrar depois.
- RAG pode migrar de Chroma para Qdrant/pgvector quando fizer sentido.
- O Agentarium pode exibir topologia real no futuro.

### Custos

- Mais disciplina de configuracao.
- Necessidade de healthchecks.
- Necessidade de separar dados, modelos e runtime.

## Regra de compra

Nenhum hardware caro deve ser comprado sem responder:

1. qual capacidade ele adiciona;
2. qual servico vai rodar nele;
3. qual dado ele armazena/processa;
4. qual custo energetico mensal esperado;
5. qual fallback existe;
6. qual teste de aceite comprova valor.

## Relacoes

- [[60_Sistemas/MEGATRON/infra/Arquitetura_Hardware_MEGATRON_FabioOS_v1]]
- [[60_Sistemas/MEGATRON/infra/Roadmap_Hardware_Software_MEGATRON]]
- [[80_Specs/MEGATRON/2026-07-02_infra-distribuida-hardware-megatron]]
- [[00_Arquitetura/Plano_Orcamento_FabioOS_MEGATRON_2026]]

> [!warning] Ratificação pendente
> Rebaixada de "aceito" para "proposto" em 2026-07-02 (regra: agente não aceita a própria ADR;
> ver [[50_Registros/Decisoes/PROTOCOLO_ADR|Protocolo ADR]]). Conteúdo intacto — aguarda assinatura do Fabio.
