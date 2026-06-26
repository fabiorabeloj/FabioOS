---
tipo: checklist
area: 60_Sistemas
projeto: FabioOS
sistema: MEGATRON
status: rascunho
tags: [megatron, agentes, revisao, checklist, qualidade]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Checklist de Revisão dos Agentes MEGATRON

## Função

Definir critérios mínimos de revisão humana antes de promover qualquer agente MEGATRON de `especificado` para `piloto`.

Este checklist não altera o estado dos agentes. Ele serve como controle de qualidade antes da promoção.

## Regra central

```text
Agente só vira piloto depois de revisão humana + execução controlada + log aceitável.
```

---

## 1. Checklist geral

Aplicar a todos os agentes.

### Especificação

- [ ] A missão está clara e não é genérica.
- [ ] Entradas e saídas estão definidas.
- [ ] Ferramentas estão listadas.
- [ ] Permissões estão explícitas.
- [ ] Limites estão claros.
- [ ] Riscos possuem mitigação.
- [ ] Critérios de aceite são verificáveis.
- [ ] Relação com MEGATRON está definida.
- [ ] Implementação mínima está descrita.
- [ ] Evolução futura não promete autonomia irrestrita.

### Segurança

- [ ] O agente não expõe tokens, chaves ou senhas.
- [ ] O agente não envia mensagens externas.
- [ ] O agente não faz push.
- [ ] O agente não apaga arquivos.
- [ ] O agente diferencia dado externo de instrução operacional.
- [ ] O agente respeita separação entre FabioOS, PietraOS e PrimusOS.

### Execução

- [ ] O agente roda sem erro no ambiente local.
- [ ] O agente gera saída compreensível.
- [ ] O agente registra log ou relatório.
- [ ] O agente falha de forma segura quando falta dependência.
- [ ] O agente não altera arquivos fora do escopo.

### Git

- [ ] Arquivos de cache não entram no Git.
- [ ] Logs de runtime não entram no Git se forem locais/sensíveis.
- [ ] Arquivos de teste descartáveis foram removidos.
- [ ] SafeCommit/check-secrets foi executado.

---

## 2. Revisão por agente

## 2.1 SafeCommit

- [ ] Lista arquivos modificados/staged antes de qualquer commit.
- [ ] Respeita `.gitignore`.
- [ ] Não escaneia caches ignorados como `__pycache__/`.
- [ ] Oculta valores de possíveis segredos.
- [ ] Bloqueia commit quando encontra credencial real.
- [ ] Propõe mensagem de commit coerente.
- [ ] Não executa push.
- [ ] Pede aprovação humana antes de commitar.

Status de promoção:

```text
especificado -> piloto somente após 1 commit real supervisionado sem falso negativo.
```

## 2.2 Arquivista

- [ ] Preserva fonte antes de sintetizar.
- [ ] Cria frontmatter completo.
- [ ] Classifica domínio e destino.
- [ ] Não inventa conteúdo.
- [ ] Linka fonte e relações internas.
- [ ] Não sobrescreve nota existente sem revisão.
- [ ] Não deixa nota de teste no vault após validação.

Status de promoção:

```text
especificado -> piloto somente após transformar 1 entrada real com revisão humana.
```

## 2.3 Inbox

- [ ] Lista entradas novas.
- [ ] Classifica tipo: fonte, wiki, tarefa, decisão ou arquivo.
- [ ] Sugere agente de destino.
- [ ] Marca sensibilidade.
- [ ] Não move arquivos na v1 sem confirmação.
- [ ] Não apaga entradas.
- [ ] Gera relatório de triagem.

Status de promoção:

```text
especificado -> piloto somente após triagem manual de uma inbox real.
```

## 2.4 RAG

- [ ] Não indexa `sources/_inbox/`.
- [ ] Não indexa logs Pietra.
- [ ] Não indexa `00_Inbox/` bruto.
- [ ] Usa embeddings locais por padrão.
- [ ] Responde com fontes.
- [ ] Declara quando não encontrou evidência suficiente.
- [ ] Falha de forma segura quando dependências não estão instaladas.

Status de promoção:

```text
especificado -> piloto somente após indexar a primeira leva autorizada e responder 10 perguntas reais.
```

## 2.5 Dashboard

- [ ] Lê Registro_Agentes, Painel de Pendências e changelogs.
- [ ] Mostra status dos agentes.
- [ ] Não expõe dados sensíveis.
- [ ] Diferencia pendência, alerta e conclusão.
- [ ] Não executa ações de outros agentes.
- [ ] Não marca tarefa como concluída sem evidência.

Status de promoção:

```text
especificado -> piloto somente após consolidar status real de pelo menos 3 agentes.
```

---

## 3. Critério de promoção

Um agente só pode sair de `especificado` quando:

- spec revisada;
- implementação mínima lida;
- execução local testada;
- logs verificados;
- riscos aceitos;
- usuário aprova promoção.

## 4. Resultado da revisão

Modelo de registro:

```text
Agente:
Data:
Revisor:
Status atual:
Resultado:
Bloqueios:
Riscos:
Próxima ação:
Pode promover? sim/não
```

## Relações

- [[60_Sistemas/MEGATRON/agentes/README_Agentes]]
- [[60_Sistemas/MEGATRON/agentes/Registro_Agentes]]
- [[60_Sistemas/FabioOS/Matriz_Frentes_Paralelas]]
- [[60_Sistemas/FabioOS/Protocolo_Coordenacao_Multiagente]]

## Próximas ações

- [ ] Aplicar este checklist à implementação mínima criada pelo Claude.
- [ ] Registrar resultado da revisão em arquivo separado antes de promover agentes.
- [ ] Só depois atualizar `Registro_Agentes.md`.
