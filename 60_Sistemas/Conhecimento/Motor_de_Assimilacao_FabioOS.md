---
tipo: protocolo
area: 60_Sistemas
projeto: FabioOS
status: ativo
tags: [conhecimento, assimilacao, llm-wiki, radar, fontes]
criado_em: 2026-06-29
atualizado_em: 2026-06-29
---

# Motor de Assimilacao FabioOS

## Funcao

Transformar cursos, videos, PDFs, prints, livros, documentacoes, repositorios, conversas, anuncios e demonstracoes em conhecimento operacional.

## Fluxo

```text
fonte bruta
-> resumo
-> conceitos
-> nota Markdown
-> links internos
-> aplicacao no FabioOS
-> Skill possivel
-> Spec possivel
-> tarefa pratica
-> radar/repertorio
-> log/changelog
```

## Templates conceituais

### Nota de fonte

```yaml
tipo: fonte
origem:
status: preservada
sensibilidade:
```

Secoes:

- Origem
- Conteudo preservado
- Conceitos
- Aplicacao no FabioOS
- Destino

### Nota conceitual

Secoes:

- Funcao
- Definicao
- Problema que resolve
- Como entra no FabioOS
- Riscos
- Relacoes
- Proximas acoes

### Aplicacao pratica

Secoes:

- Ideia extraida
- Fase relacionada
- Teste minimo
- Custo/risco
- Criterio de aceite
- Decisao: implementar, estudar, descartar ou adiar

## Regras

- Anuncio nao entra como propaganda; entra como padrao arquitetural.
- Curso nao vira apenas resumo; vira aplicacao, Skill, Spec ou tarefa.
- Fonte externa nao vira regra sem decisao.
- Tudo que gerar decisao deve apontar para ADR ou changelog.

## Relacoes

- [[90_Arquivo/Legado_Pre_LLM_Wiki_2026-06-29/30_Conhecimento/Tecnologia/Arquiteturas_de_Mercado_Radar_Tecnologico]]
- [[60_Sistemas/FabioOS/Catalogo_Caminhos_Ferramentas_Demonstradas_2026-06-28]]
- [[60_Sistemas/Wiki/Protocolo_Ingest_LLM_Wiki]]
