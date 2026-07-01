---
tipo: metodo
area: 80_Specs
projeto: PRIMUS
status: ativo
autor: Claude (arquiteto-chefe)
criado_em: 2026-07-01
tags: [primus, metodo, markdownizacao, conceitos, livro, obsidian, nota-vs-dado]
---

# Método — Markdownizar um livro em NÓS DE CONCEITO (não stubs)

> Procedimento replicável para transformar um PDF de livro em conhecimento
> conectado, respeitando a lei [[50_Registros/Decisoes/ADR_2026-07-01_Nota_vs_Dado_Ingestao_Obsidian]].
> Para o Codex executar em qualquer livro. **Não gera stubs; não copia texto protegido.**

## Regra de ouro

Um livro NÃO vira mil notas. Ele vira: **índice/catálogo (dado)** + um **punhado de
nós de conceito forte (conhecimento)**. O teste, para cada candidato a nota:

> "Isso é uma **ideia** pensável e ligável a outras — ou é uma **linha de dado**?"
> Ideia → nó. Dado → índice.

## Passo a passo (por livro)

1. **Extrair texto** com o documentalista (PyMuPDF) → pasta gitignored
   (`00_Inbox/pdfs/_extracted/`). Nunca versionar o texto integral.
2. **Classificar a fonte:**
   - **Restrita (copyright, ex.: D&D):** só conceitos **abstratos/derivados** (a
     ideia-mecânica, não a tabela); zero trecho literal; dado vai só para o índice.
   - **Livre/aberta (ex.: SWN/WWN free):** pode ter mais nós; ainda assim só conceitos.
3. **Levantar os conceitos fortes** (não os itens): mecânicas-ideia, estruturas de
   design, princípios de mundo, procedimentos reutilizáveis. Alvo: **5–15 por livro**,
   não centenas.
4. **Escrever cada nó** no template abaixo, em `40_Wiki/PRIMUS/conceitos/`.
5. **Ligar** cada nó ao motor PRIMUS: [[WorldState_0001_PRIMUS]],
   [[Spec_Tension_Engine_PRIMUS]], [[Spec_DeltaP]], [[Spec_Cantina_Conflict_Engine_PRIMUS]].
6. **Mandar o dado** (tabelas, listas, stats) para o **PRIMUS Index/SQLite** —
   consultável, fora do grafo.
7. **Registrar** no CatalogPool/log o que virou nó e o que ficou como dado.

## Template do nó de conceito

```markdown
---
tipo: conceito
area: 40_Wiki
projeto: PRIMUS
classe_dado: interno
autoria: derivado (conceito abstrato; sem texto integral)
fonte_conceitual: <livro/edição>
tags: [primus, design, <tema>, conceito]
---
# <Nome do conceito>
## O conceito        (2-4 linhas, a IDEIA, sem copiar texto)
## Por que é forte    (pensável, ligável, reutilizável, abstrato)
## Relações no grafo  (wikilinks ao motor PRIMUS e a outros conceitos)
## Onde o DADO vive   (o que NÃO vira nota: índice/SQLite)
## Uso no PRIMUS      (como aplicar em jogo/mundo)
```

## Critério de aceite (para o Codex)

- [ ] 5–15 nós por livro, cada um passa no teste "ideia, não dado".
- [ ] Zero trecho literal de fonte protegida; D&D só conceito abstrato.
- [ ] Cada nó tem ≥2 wikilinks (ao motor PRIMUS ou a outros conceitos).
- [ ] Dado bruto foi para o índice/SQLite, não para `40_Wiki`.
- [ ] Nenhum stub massivo; nada em `40_Wiki` que seja "linha de dado".

## Padrão-exemplo (já criado por Claude)
- [[40_Wiki/PRIMUS/conceitos/faccoes-e-turnos-de-faccao]]

## Relações
- [[50_Registros/Decisoes/ADR_2026-07-01_Nota_vs_Dado_Ingestao_Obsidian]]
- [[80_Specs/PRIMUS/Spec_Markdownizacao_Segura_Livros_PRIMUS]]
