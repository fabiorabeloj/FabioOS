---
tipo: politica
area: 60_Sistemas
projeto: PietraOS
status: rascunho
autor: Claude (arquiteto-chefe)
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [pietraos, lgpd, dados, privacidade, seguranca, escola]
---

# Política de Dados / LGPD — PietraOS

> PietraOS processa dados de **menores**, **saúde** (atestados) e **financeiro**.
> LGPD aqui é **pilar**, não nota de rodapé — e é também **argumento de venda**:
> *"os dados do aluno não saem da escola"*.

## Princípios

1. **Minimização:** coletar e reter só o necessário para a próxima ação. Não copiar
   conteúdo integral de documento sensível para log/Git/RAG (mesmo padrão
   copyright-safe do pipeline PDF: bruto em pasta isolada, gitignored).
2. **Isolamento por tenant:** dados de uma escola **nunca** se misturam com outra.
   `tenants/<tenant>/` é gitignored e, em produção, criptografado/segregado.
3. **Local-first:** dados ficam na infraestrutura da escola/FabioOS; sem envio a
   modelo externo sem base legal + consentimento + teto.
4. **Humano no loop:** risco alto/crítico (saúde, bullying, conflito, jurídico)
   **nunca** responde sozinho — bloqueia e escala.
5. **Rastreabilidade:** todo atendimento registra origem, categoria, risco, setor e
   próxima ação (auditável), sem expor o conteúdo sensível além do necessário.

## Bases legais (a confirmar com jurídico)

- Tratamento para **execução de contrato** (escola↔responsável) e **legítimo
  interesse** administrativo; **consentimento** para usos além do operacional.
- Dado de **saúde** = dado sensível (art. 11 LGPD): tratamento restrito, finalidade
  específica (encaminhar à secretaria/coordenação), retenção mínima.
- Dado de **menor**: melhor interesse da criança; consentimento de pelo menos um dos pais.

## Retenção e descarte

- Definir TTL por tipo (ex.: atendimento operacional 12 meses; sensível mínimo).
- Direito de eliminação/portabilidade do titular (responsável).

## Pendências antes de comercializar

- [ ] Termo de tratamento de dados (escola como controladora; PietraOS operador).
- [ ] DPA / contrato com cláusula LGPD.
- [ ] Política de retenção por categoria.
- [ ] Migrar de WhatsApp Evolution (não-oficial) para **WhatsApp Business API oficial**
      antes de escala comercial (compliance + evitar ban).
- [ ] Criptografia em repouso dos dados de tenant.

## Relações
- [[60_Sistemas/Pietra/PietraOS_Arquitetura_Multitenant]]
- [[60_Sistemas/FabioOS/specs/2026-06-30_pipeline-pdf-aprende]]
- [[60_Sistemas/Seguranca/Protocolo_de_Seguranca_FabioOS]]
