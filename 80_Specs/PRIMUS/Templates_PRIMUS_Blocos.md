---
tipo: template
area: 80_Specs
projeto: PRIMUS
status: rascunho
fonte: [[05_Raw_Sources/PRIMUS/2026-06-30_pdf_primus_contexto_completo_final]]
criado_em: 2026-06-30
atualizado_em: 2026-06-30
tags: [primus, templates, race, class, plane, dungeon, mission, npc, creature, spell]
---

# Templates PRIMUS - Bloco 3

## Funcao

Definir templates por familia. A regra principal e que PRIMUS nao deve usar um template universal para todos os tipos.

## Template RACE

```yaml
tipo: race
estado: rascunho
nome:
fonte:
canon_status: rascunho
tracos:
atributos:
tamanho:
deslocamento:
idiomas:
cultura_opcional:
nomes_tipicos:
observacoes:
```

## Template CLASS

```yaml
tipo: class
estado: rascunho
nome:
fonte:
canon_status: rascunho
dado_de_vida:
proficiencias:
equipamento_inicial:
features_por_nivel:
spellcasting:
subclasses:
observacoes:
```

## Template PLANE

```yaml
tipo: plane
estado: rascunho
nome:
fonte:
canon_status: rascunho
propriedades_metafisicas:
leis_locais:
formas_de_acesso:
perigos:
habitantes:
relacao_com_outros_planos:
efeitos_em_missoes:
observacoes:
```

## Template DUNGEON

```yaml
tipo: dungeon
estado: rascunho
nome:
fonte:
canon_status: rascunho
localizacao:
camadas:
salas:
encontros:
tesouros:
perigos:
recompensas:
delta_p_possivel:
criterio_de_conclusao:
observacoes:
```

## Template MISSION

```yaml
tipo: mission
estado: rascunho
mission_id:
nome:
fonte:
canon_status: rascunho
objetivo:
local:
dificuldade:
duracao_estimada:
entradas_e:
instancia_i:
delta_p_previsto:
recompensas:
criterios_de_sucesso:
criterios_de_falha:
observacoes:
```

## Template NPC

```yaml
tipo: npc
estado: rascunho
nome:
fonte:
canon_status: rascunho
papel:
faccao:
motivacao:
relacoes:
segredos:
uso_em_missoes:
estado_atual:
delta_p_relevante:
observacoes:
```

## Template CREATURE

```yaml
tipo: creature
estado: rascunho
nome:
fonte:
canon_status: rascunho
categoria:
ambiente:
papel_narrativo:
ameaca:
habilidades_chave:
fraquezas:
uso_em_encontros:
delta_p_ao_derrotar:
observacoes:
```

## Template SPELL

```yaml
tipo: spell
estado: rascunho
nome:
fonte:
canon_status: rascunho
nivel:
escola:
tempo_de_conjuracao:
alcance:
componentes:
duracao:
efeito:
classes_relacionadas:
uso_narrativo:
observacoes:
```

## Proximas Acoes

- [x] Criar templates adicionais para `mission`, `npc`, `creature` e `spell`.
- [ ] Validar se os oito templates cobrem a Missao 0001.
- [ ] Converter templates para arquivos separados se virarem uso recorrente.
