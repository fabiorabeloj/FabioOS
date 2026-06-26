---
description: Simula o fluxo Pietra: classifica uma mensagem de pai/responsável e sugere resposta-modelo. Usa sem precisar de WhatsApp ou n8n.
allowed-tools: [Read, Glob]
---

# /simular-mensagem-pietra

Simula o processamento completo de uma mensagem pelo Sistema Pietra — classificação de intent, nível de sensibilidade e sugestão de resposta — sem depender de WhatsApp ou n8n.

## Como usar

```
/simular-mensagem-pietra [mensagem]
```

Exemplos:
```
/simular-mensagem-pietra "Boa tarde, quando é a prova de geografia do 9A?"
/simular-mensagem-pietra "Meu filho não fez a prova, posso pedir segunda chamada?"
/simular-mensagem-pietra "Quero falar com a coordenação sobre uma ocorrência"
```

## Fluxo

1. Ler `60_Sistemas/Pietra/intents/INTENTS_CATALOGO.md`
2. Comparar a mensagem fornecida com os gatilhos de cada categoria
3. Identificar a categoria com mais correspondências
4. Determinar o nível de sensibilidade (baixo / médio / alto)
5. Verificar se há condições de escalonamento obrigatório
6. Ler `60_Sistemas/Pietra/respostas-modelo/RESPOSTAS_MODELO.md`
7. Selecionar e preencher a resposta-modelo correspondente
8. Apresentar o resultado estruturado

## Resultado esperado

```
MENSAGEM RECEBIDA:
"[mensagem do usuário]"

CLASSIFICAÇÃO PIETRA:
· Categoria: [nome]
· Nível: [baixo / médio / alto]
· Escalonar: [sim / não — motivo]

RESPOSTA-MODELO SUGERIDA:
[texto da resposta com variáveis marcadas para preenchimento]

AÇÃO RECOMENDADA:
[enviar resposta / escalonar para coordenação / triagem manual]

NOTAS:
[qualquer alerta de privacidade, LGPD ou sensibilidade]
```

## Regras

- Esta é uma simulação para testes — não substitui o fluxo real com WhatsApp
- Se a mensagem não se encaixar claramente em nenhuma categoria, apresentar as 2 mais prováveis com justificativa
- Nunca inventar respostas: sempre usar o texto de RESPOSTAS_MODELO.md como base
- Sinalizar claramente se a situação exige escalonamento obrigatório
