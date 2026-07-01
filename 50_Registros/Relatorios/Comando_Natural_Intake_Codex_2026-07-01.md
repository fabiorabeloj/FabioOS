---
tipo: relatorio
area: MEGATRON
frente: INTAKE_COMMAND_EXTRACTOR
responsavel: Codex
data: 2026-07-01
status: concluido
tags: [fabios, megatron, intake, comando-natural, agentarium]
---

# Comando Natural no Intake - Codex

## Contexto

O relatorio do Cursor para a Mesa de Despacho marcou como pendencia externa:

- extracao estruturada de `serie`, `tema`, `prazo` e `produto` no comando natural.

Essa frente fecha a pendencia sem tocar no Agentarium e sem criar acao externa.

## Implementacao

- Criado/versionado `60_Sistemas/FabioOS/scripts/intake_command_extract.py`.
- O script opera sem LLM, sem API e sem efeitos externos.
- O `universal_intake_adapter.py` agora usa o extrator para anexar o campo opcional `extracao` nos cards quando ha pelo menos dois sinais estruturais.
- Itens com `sensitivity=forbidden_external` nao recebem `extracao`, preservando a trava de segredo.
- O resumo do card pode ser enriquecido com uma cabeca estruturada, por exemplo:
  - `Prova 8o ano sobre Africa (amanha) - ...`

## Campos extraidos

- `produto`: prova, revisao, atividade, planejamento, gabarito, redacao, apresentacao.
- `serie`: padroes como `8o ano`, `9 ano`, `fundamental 2`.
- `tema`: padroes `sobre ...` e `tema ...`.
- `prazo`: `hoje`, `amanha`, `ate sexta`, datas simples e urgencia.
- `confianca`: escore deterministico de 0 a 1.

## Testes executados

```powershell
python -m py_compile "60_Sistemas/FabioOS/scripts/intake_command_extract.py" "60_Sistemas/FabioOS/scripts/universal_intake_adapter.py"
```

Resultado: OK.

```powershell
python "60_Sistemas/FabioOS/scripts/intake_command_extract.py" --self-test
```

Resultado: `{"ok": true}`.

```powershell
'{"text":"prova do 8o ano sobre Africa para amanha"}' | python "60_Sistemas/FabioOS/scripts/intake_command_extract.py"
```

Resultado: `serie=8o ano`, `tema=Africa`, `prazo=amanha`, `produto=prova`, `confianca=1.0`.

```powershell
python "60_Sistemas/FabioOS/scripts/universal_intake_adapter.py" --input "60_Sistemas/FabioOS/examples/universal_intake_payloads_fake.json" --stdout | python "60_Sistemas/FabioOS/scripts/universal_intake_validator.py"
```

Resultado: `{"ok": true, "cards": 5}`.

## Validacao de seguranca

- O card escolar recebeu `extracao`.
- O card com segredo fake recebeu `sensitivity=forbidden_external`.
- O card com segredo fake nao recebeu `extracao`.
- O resumo sensivel permaneceu como placeholder redigido.

## Limites

- Nao chama Gmail real.
- Nao envia WhatsApp.
- Nao aprova item.
- Nao grava nota no Obsidian.
- Nao altera Agentarium.
- Nao usa RAG, API externa ou push.

## Proxima interface esperada

O Cursor pode exibir `card.extracao` na Mesa de Despacho como chips:

- produto;
- serie;
- tema;
- prazo;
- confianca.
