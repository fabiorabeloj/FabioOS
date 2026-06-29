#!/usr/bin/env python3
"""Gera uma SPEC FabioOS a partir de argumentos locais.

Nao chama APIs, nao envia dados e nao altera RAG/Grafo. Serve para iniciar o
fluxo Spec-Driven: SPEC -> plano -> tarefas -> testes -> changelog.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


DEFAULT_OUTPUT_DIR = Path("60_Sistemas") / "FabioOS" / "specs"


def vault_root() -> Path:
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "CLAUDE.md").exists():
            return parent
    raise RuntimeError("Nao encontrei CLAUDE.md acima do script.")


ROOT = vault_root()


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:80] or "spec"


def source_label(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.name


def render(args: argparse.Namespace) -> str:
    now = datetime.now().strftime("%Y-%m-%d")
    title = args.title.strip()
    fase = args.phase or "a definir"
    dominio = args.domain or "FabioOS"
    classe = args.data_class or "Interno"
    permissao = args.permission or "propose-only ate aprovacao humana"
    problem = args.problem or "Problema ainda precisa ser refinado antes da implementacao."
    goal = args.goal or "Entregar uma capacidade minima, testavel, documentada e reversivel."
    out_scope = args.out_of_scope or "Acoes externas, custos recorrentes, push e automacoes sensiveis ficam fora desta SPEC v0."
    architecture = args.architecture or "Entrada -> processamento local -> saida Markdown -> dashboard/changelog"
    test_hint = args.test or "Executar script/comando local, validar arquivo gerado e rodar scan de seguranca."
    source = f"\nfonte: {args.source}\n" if args.source else ""

    return f"""---
tipo: spec
area: 60_Sistemas
projeto: FabioOS
status: rascunho
fase: {fase}
dominio: {dominio}
classe_dado: {classe}
permissao: {permissao}
criado_em: {now}
atualizado_em: {now}{source}tags: [fabios, spec, spec-driven]
---

# SPEC - {title}

## 1. Problema

{problem}

## 2. Objetivo

{goal}

## 3. Fora de escopo

{out_scope}

## 4. Dominio, dados e permissoes

| Campo | Valor |
|---|---|
| Dominio | {dominio} |
| Classe de dado | {classe} |
| RAG | consultar/classificar antes de ingestao |
| Grafo | consultar/classificar antes de ingestao |
| Modelo externo/API | somente com aprovacao e teto de custo |
| Aprovacao humana | obrigatoria para acao externa, custo, push ou dado sensivel |

## 5. Arquitetura proposta

```text
{architecture}
```

## 6. Plano de tarefas

- [ ] Validar contexto e arquivos existentes.
- [ ] Classificar dominio/dados/permissoes.
- [ ] Implementar menor unidade reversivel.
- [ ] Rodar teste minimo.
- [ ] Atualizar dashboard/mapa, se aplicavel.
- [ ] Gerar changelog.
- [ ] Fazer scan antes de commit.

## 7. Criterios de aceite

- [ ] A entrega resolve o problema declarado.
- [ ] A entrega e versionavel no vault.
- [ ] A entrega e visivel no Obsidian.
- [ ] A entrega tem teste minimo executado.
- [ ] A entrega nao expoe credenciais.
- [ ] A entrega possui changelog.

## 8. Testes minimos

- [ ] {test_hint}
- [ ] Rodar `git diff --check`.
- [ ] Rodar scan de segredos antes do commit.

## 9. Riscos

| Risco | Mitigacao |
|---|---|
| Escopo crescer demais | limitar a v0 a menor unidade testavel |
| Dado sensivel entrar no fluxo | aplicar matriz de dominios/dados/permissoes |
| Automacao agir sem aprovacao | manter propose-only ate autorizacao humana |
| Custo externo inesperado | nao usar API por padrao |

## 10. Rollback

Reverter ou ignorar os arquivos gerados nesta SPEC; como a v0 e local e Markdown/Python, nao ha estado externo obrigatorio.

## 11. Changelog esperado

Registrar em `50_Registros/Changelog/` o que foi implementado, testado, deixado fora e qual proxima decisao.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera uma SPEC FabioOS local.")
    parser.add_argument("--title", required=True, help="titulo da SPEC")
    parser.add_argument("--phase", default="", help="fase ou subfase relacionada")
    parser.add_argument("--domain", default="", help="dominio FabioOS/PietraOS/TraderOS/PrimusOS/IAOS/etc")
    parser.add_argument("--data-class", default="", help="classe de dado: Publico/Interno/Privado/Restrito/Critico")
    parser.add_argument("--permission", default="", help="permissao operacional")
    parser.add_argument("--problem", default="", help="problema que a SPEC resolve")
    parser.add_argument("--goal", default="", help="objetivo concreto")
    parser.add_argument("--out-of-scope", default="", help="fora de escopo")
    parser.add_argument("--architecture", default="", help="fluxo arquitetural proposto")
    parser.add_argument("--test", default="", help="teste minimo principal")
    parser.add_argument("--source", default="", help="fonte relacionada")
    parser.add_argument("--output", default="", help="arquivo Markdown de saida")
    args = parser.parse_args()

    if args.output:
        out = Path(args.output)
        if not out.is_absolute():
            out = ROOT / out
    else:
        filename = f"{datetime.now().strftime('%Y-%m-%d')}_{slugify(args.title)}.md"
        out = ROOT / DEFAULT_OUTPUT_DIR / filename

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(args), encoding="utf-8")
    print(f"SPEC gerada: {source_label(out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
