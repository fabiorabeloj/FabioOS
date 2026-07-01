---
tipo: guia
area: 60_Sistemas
projeto: PietraOS
status: ativo
autor: Claude (arquiteto-chefe)
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [pietraos, piloto, coordenacao, vendas, acesso, lgpd, escola]
---

# O que solicitar (e como) para a coordenação — Piloto PietraOS

> Objetivo: conseguir um **teste pequeno e supervisionado** organizando o WhatsApp
> de atendimento aos pais, para gerar o **estudo de caso** (antes/depois).
> Regra de ouro: **peça a partir da dor dela, não da tecnologia.**

## 1. A postura certa

- É um **favor/experimento**, não um produto para vender agora.
- **Baixo risco, supervisionado, reversível.** Ela continua no controle.
- **Você faz todo o trabalho técnico.** Ela só precisa **deixar** e **mostrar como funciona hoje**.
- Nada de "IA", "sistema", "automação" no começo. Fale de **organizar o WhatsApp**.

## 2. As 4 frases que destravam o "sim" (fale antes de qualquer coisa)

1. **"Nada é enviado para o pai automaticamente — sempre passa por uma pessoa."**
2. **"Casos delicados (saúde, briga, conflito) vão direto para um humano; o sistema nem responde."**
3. **"Os dados ficam aqui na escola, não vão para a internet nem para empresa nenhuma."**
4. **"Não substitui ninguém nem o sistema da escola — só organiza a bagunça do WhatsApp. E pode parar quando quiser."**

## 3. O que pedir (checklist)

**Permissão**
- [ ] Autorização para um **teste de 3-4 semanas** organizando o WhatsApp de atendimento.
- [ ] Um **OK por escrito** simples (a própria mensagem dela serve), porque envolve dados de alunos.

**Como funciona hoje (para configurar)**
- [ ] Qual **número de WhatsApp** a escola usa para falar com os pais (ou um número novo só para o teste).
- [ ] **Quem cuida de quê:** secretaria, financeiro, coordenação, direção, professores.
- [ ] **O que os pais mais pedem** (os 5-10 assuntos mais comuns).
- [ ] **Respostas padrão** que a escola já usa (horário, uniforme, calendário, valores, material).
- [ ] O **tom** que a escola gosta de usar com os pais (formal? acolhedor?).

**Para medir o resultado (o estudo de caso)**
- [ ] Uma noção dos **números de hoje:** quantas mensagens por dia/semana, quanto tempo para responder, se mensagens se perdem, o que mais dá retrabalho.

## 4. O que NÃO fazer

- Não prometer substituir a secretaria nem o Sophia.
- Não usar jargão (IA, RAG, agente, n8n) — assusta e não ajuda.
- Não prometer prazo/preço agora. É teste.
- Não pedir acesso a dados sensíveis sem necessidade.

## 5. Mensagem pronta (adapte para o seu jeito com sua tia)

> "Tia, tô mexendo num projeto que organiza o WhatsApp de atendimento da escola —
> aquela bagunça de mensagem de pai que se perde, demora pra responder e vira
> retrabalho. Ele **lê a mensagem, entende o assunto, sugere uma resposta e
> encaminha pro setor certo** — mas **nada vai pro pai sem uma pessoa aprovar**, e
> **caso delicado (saúde, briga) vai direto pra um humano**. Os dados **ficam na
> escola**. Queria fazer um **teste de umas 3 semanas**, do meu lado, só pra medir
> quanto tempo isso economiza. Você continua no controle e a gente para quando
> quiser. Posso te mostrar como funciona numa conversa rápida?"

## 6. Depois do "sim" — o que você me traz

Me passe: o número de WhatsApp (ou um de teste), a lista de setores/quem-cuida-de-quê,
os assuntos mais comuns e as respostas padrão. Eu configuro o **tenant `colegio-pietra`**
(setores, FAQ, tom) e a gente liga o piloto. No fim, gero o **relatório antes/depois**
que vira seu estudo de caso.

## Relações
- [[60_Sistemas/Pietra/PietraOS_Arquitetura_Multitenant]]
- [[60_Sistemas/Pietra/Politica_Dados_LGPD_PietraOS]]
- [[60_Sistemas/Pietra/pietra_conversa]]
