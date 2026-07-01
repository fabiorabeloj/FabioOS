from __future__ import annotations

import argparse
import sqlite3
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

from primus_digestor_common import slugify


BOOKS = {
    "phb": {
        "title": "Livro do Jogador 2014",
        "source_id": "SRC-DND-PHB-2014",
        "index": "[[40_Wiki/PRIMUS/Fontes_Oficiais_DND/DND_Core_PHB_2014_Index_Seguro]]",
    },
    "dmg": {
        "title": "Guia do Mestre 2014",
        "source_id": "SRC-DND-DMG-2014",
        "index": "[[40_Wiki/PRIMUS/Fontes_Oficiais_DND/DND_Core_DMG_2014_Index_Seguro]]",
    },
    "mm": {
        "title": "Manual dos Monstros 2014",
        "source_id": "SRC-DND-MM-2014",
        "index": "[[40_Wiki/PRIMUS/Fontes_Oficiais_DND/DND_Core_MM_2014_Index_Seguro]]",
    },
}

CATEGORIES = {
    "ENTIDADES": {
        "folder": "entidades",
        "label": "Entidades",
        "suggested_type": "entity_stub",
        "target": "[[40_Wiki/PRIMUS/Enciclopedia/Criaturas/README]]",
    },
    "OBJETOS": {
        "folder": "objetos",
        "label": "Objetos",
        "suggested_type": "object_stub",
        "target": "[[40_Wiki/PRIMUS/Enciclopedia/Itens_e_Tesouros/README]]",
    },
    "FUNCOES": {
        "folder": "funcoes",
        "label": "Funcoes",
        "suggested_type": "procedure_stub",
        "target": "[[40_Wiki/PRIMUS/Enciclopedia/Regras_e_Procedimentos/README]]",
    },
    "GRUPOS": {
        "folder": "grupos",
        "label": "Grupos",
        "suggested_type": "faction_stub",
        "target": "[[40_Wiki/PRIMUS/Enciclopedia/Faccoes_e_Culturas/README]]",
    },
    "LOCAIS": {
        "folder": "locais",
        "label": "Locais",
        "suggested_type": "place_stub",
        "target": "[[40_Wiki/PRIMUS/Enciclopedia/Lugares/README]]",
    },
    "EVENTOS": {
        "folder": "eventos",
        "label": "Eventos",
        "suggested_type": "event_stub",
        "target": "[[40_Wiki/PRIMUS/Instancias/README]]",
    },
    "INDEFINIDO": {
        "folder": "indefinido",
        "label": "Indefinido",
        "suggested_type": "triage_stub",
        "target": "[[30_Projetos/PRIMUS/Plano_Markdownizacao_Livros_PRIMUS]]",
    },
}


@dataclass(frozen=True)
class StubRow:
    record_id: str
    book_key: str
    category: str
    subtype: str
    name: str
    page: int | None
    heading: str
    kind: str


def yaml_str(value: object) -> str:
    text = "" if value is None else str(value)
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def display_name(row: StubRow) -> str:
    base = row.name or row.heading or f"Registro {row.record_id[:8]}"
    return " ".join(base.split())


def category_meta(category: str) -> dict[str, str]:
    return CATEGORIES.get(category or "INDEFINIDO", CATEGORIES["INDEFINIDO"])


def stub_filename(row: StubRow) -> str:
    page = f"p{row.page:03d}" if row.page is not None else "p000"
    slug = slugify(display_name(row), fallback="registro")
    return f"{page}-{slug}-{row.record_id[:8]}.md"


def render_stub(row: StubRow) -> str:
    book = BOOKS[row.book_key]
    cat = category_meta(row.category)
    title = display_name(row)
    page = "" if row.page is None else row.page
    lines = [
        "---",
        "tipo: stub-catalogentry",
        "area: 40_Wiki",
        "projeto: PRIMUS",
        "status: stub-seguro",
        "classe_dado: Restricted",
        f"source_id: {book['source_id']}",
        f"book_key: {row.book_key}",
        f"book_title: {yaml_str(book['title'])}",
        f"record_id: {row.record_id}",
        f"category: {row.category or 'INDEFINIDO'}",
        f"subtype: {yaml_str(row.subtype)}",
        f"kind: {yaml_str(row.kind)}",
        f"page: {page}",
        "license_status: Restricted",
        "source_policy: no-full-text",
        "affects: [catalog_navigation, source_validation, primus_stub]",
        "never_affects: [public_export, canon_without_ve, full_text_storage]",
        "instancing_hint: review_before_promotion",
        "created_by: PRIMUS_Digestor_07_export_official_stubs",
        "tags: [primus, dnd, stub, restricted, official-core]",
        "---",
        "",
        f"# {title}",
        "",
        "## Funcao",
        "",
        "Stub seguro para localizar e classificar uma entrada de livro oficial dentro do PRIMUS.",
        "",
        "Este arquivo nao contem texto integral, regra completa, tabela, bloco de estatistica ou transcricao do livro.",
        "",
        "## Fonte",
        "",
        f"- Livro: {book['title']}",
        f"- SourceID: `{book['source_id']}`",
        f"- Pagina: `{page}`",
        f"- Registro tecnico: `{row.record_id}`",
        f"- Categoria detectada: `{row.category or 'INDEFINIDO'}`",
        f"- Tipo de bloco: `{row.kind or ''}`",
        f"- Indice seguro do livro: {book['index']}",
        "",
        "## Encaixe PRIMUS",
        "",
        f"- Tipo sugerido: `{cat['suggested_type']}`",
        f"- Destino de revisao: {cat['target']}",
        "- Estado: `stub-seguro`",
        "- Promocao exige V(E) e revisao humana.",
        "",
        "## Uso Permitido",
        "",
        "- localizar a pagina/fonte no acervo privado;",
        "- criar CatalogEntry com metadados;",
        "- gerar resumo transformativo curto;",
        "- criar versao autoral propria do PRIMUS;",
        "- alimentar mapas e MOCs sem copiar o livro.",
        "",
        "## Nao Fazer",
        "",
        "- nao publicar como conteudo livre;",
        "- nao substituir o livro oficial;",
        "- nao preencher com texto integral;",
        "- nao promover para canon PRIMUS sem validacao.",
        "",
        "## Links",
        "",
        "- [[40_Wiki/_MOCs/MOC_PRIMUS]]",
        "- [[40_Wiki/PRIMUS/Fontes_Oficiais_DND/Catalogo_DND_Core_Consolidado]]",
        "- [[80_Specs/PRIMUS/Spec_Markdownizacao_Segura_Livros_PRIMUS]]",
    ]
    return "\n".join(lines).rstrip() + "\n"


def render_category_readme(book_key: str, category: str, rows: list[StubRow]) -> str:
    book = BOOKS[book_key]
    cat = category_meta(category)
    lines = [
        "---",
        "tipo: indice",
        "area: 40_Wiki",
        "projeto: PRIMUS",
        "status: ativo",
        "classe_dado: Restricted",
        f"book_key: {book_key}",
        f"category: {category}",
        "tags: [primus, dnd, stubs, restricted, official-core]",
        "---",
        "",
        f"# {book['title']} - {cat['label']}",
        "",
        "## Funcao",
        "",
        "Indice de stubs seguros desta categoria.",
        "",
        "## Contagem",
        "",
        f"- Total: `{len(rows)}`",
        f"- Destino de revisao: {cat['target']}",
        "",
        "## Stubs",
        "",
    ]
    for row in rows:
        path = stub_filename(row)
        lines.append(f"- [[{path[:-3]}|{display_name(row)}]] - p. {row.page if row.page is not None else ''} - `{row.record_id[:8]}`")
    return "\n".join(lines).rstrip() + "\n"


def render_book_readme(book_key: str, counts: Counter[str]) -> str:
    book = BOOKS[book_key]
    lines = [
        "---",
        "tipo: indice",
        "area: 40_Wiki",
        "projeto: PRIMUS",
        "status: ativo",
        "classe_dado: Restricted",
        f"book_key: {book_key}",
        "tags: [primus, dnd, stubs, restricted, official-core]",
        "---",
        "",
        f"# Stubs - {book['title']}",
        "",
        "## Funcao",
        "",
        "Indice de stubs seguros gerados a partir do PRIMUS Index local.",
        "",
        "## Limite",
        "",
        "Estes arquivos nao transcrevem o livro. Eles preservam apenas metadados e apontam para validacao privada.",
        "",
        "## Categorias",
        "",
        "| Categoria | Total | Link |",
        "|---|---:|---|",
    ]
    for category, total in sorted(counts.items()):
        folder = category_meta(category)["folder"]
        label = category_meta(category)["label"]
        lines.append(f"| {label} | {total} | [[{folder}/README|abrir]] |")
    return "\n".join(lines).rstrip() + "\n"


def render_root_readme(book_counts: dict[str, Counter[str]]) -> str:
    total = sum(sum(counter.values()) for counter in book_counts.values())
    lines = [
        "---",
        "tipo: indice",
        "area: 40_Wiki",
        "projeto: PRIMUS",
        "status: ativo",
        "classe_dado: Restricted",
        "tags: [primus, dnd, stubs, restricted, official-core]",
        "---",
        "",
        "# Stubs Oficiais DND Core - PRIMUS",
        "",
        "## Funcao",
        "",
        "Navegacao massiva e segura dos livros oficiais DND Core no Obsidian.",
        "",
        "Cada stub aponta para livro, pagina, categoria e destino de revisao, sem texto integral.",
        "",
        "## Contagem",
        "",
        f"- Total de stubs: `{total}`",
        "",
        "| Livro | Total | Indice |",
        "|---|---:|---|",
    ]
    for book_key in BOOKS:
        if book_key not in book_counts:
            continue
        subtotal = sum(book_counts[book_key].values())
        lines.append(f"| {BOOKS[book_key]['title']} | {subtotal} | [[{book_key}/README|abrir]] |")
    lines.extend(
        [
            "",
            "## Regras",
            "",
            "- `Restricted` por padrao.",
            "- Nao contem transcricao.",
            "- Nao substitui posse/licenca dos livros.",
            "- Promocao para Enciclopedia exige V(E).",
            "",
            "## Links",
            "",
            "- [[40_Wiki/_MOCs/MOC_PRIMUS]]",
            "- [[40_Wiki/PRIMUS/Fontes_Oficiais_DND/README]]",
            "- [[80_Specs/PRIMUS/Spec_Markdownizacao_Segura_Livros_PRIMUS]]",
            "- [[30_Projetos/PRIMUS/Plano_Markdownizacao_Livros_PRIMUS]]",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def fetch_rows(db_path: Path, books: list[str]) -> list[StubRow]:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    placeholders = ", ".join("?" for _ in books)
    rows = conn.execute(
        f"""
        SELECT id, book_key, category, subtype, name, page, heading, kind
        FROM records
        WHERE book_key IN ({placeholders})
        ORDER BY book_key, page, category, name, id
        """,
        books,
    ).fetchall()
    conn.close()
    return [
        StubRow(
            record_id=row["id"],
            book_key=row["book_key"],
            category=row["category"] or "INDEFINIDO",
            subtype=row["subtype"] or "",
            name=row["name"] or "",
            page=row["page"],
            heading=row["heading"] or "",
            kind=row["kind"] or "",
        )
        for row in rows
    ]


def export_stubs(db_path: Path, out_dir: Path, books: list[str]) -> dict[str, Counter[str]]:
    rows = fetch_rows(db_path, books)
    by_book_category: dict[str, dict[str, list[StubRow]]] = defaultdict(lambda: defaultdict(list))
    for row in rows:
        by_book_category[row.book_key][row.category].append(row)

    book_counts: dict[str, Counter[str]] = {}
    for book_key, categories in by_book_category.items():
        counts: Counter[str] = Counter()
        book_dir = out_dir / book_key
        book_dir.mkdir(parents=True, exist_ok=True)
        for category, cat_rows in categories.items():
            cat = category_meta(category)
            category_dir = book_dir / cat["folder"]
            category_dir.mkdir(parents=True, exist_ok=True)
            for row in cat_rows:
                (category_dir / stub_filename(row)).write_text(render_stub(row), encoding="utf-8", newline="\n")
            (category_dir / "README.md").write_text(
                render_category_readme(book_key, category, cat_rows),
                encoding="utf-8",
                newline="\n",
            )
            counts[category] = len(cat_rows)
        (book_dir / "README.md").write_text(render_book_readme(book_key, counts), encoding="utf-8", newline="\n")
        book_counts[book_key] = counts

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "README.md").write_text(render_root_readme(book_counts), encoding="utf-8", newline="\n")
    return book_counts


def main() -> int:
    parser = argparse.ArgumentParser(description="Export safe Markdown stubs for official DND Core records.")
    parser.add_argument("--db", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--books", nargs="+", default=["phb", "dmg", "mm"], choices=sorted(BOOKS))
    args = parser.parse_args()

    db_path = Path(args.db)
    out_dir = Path(args.out)
    counts = export_stubs(db_path, out_dir, args.books)
    total = sum(sum(counter.values()) for counter in counts.values())
    print(f"exported {total} official stubs -> {out_dir}")
    for book_key in args.books:
        if book_key in counts:
            subtotal = sum(counts[book_key].values())
            print(f"- {book_key}: {subtotal}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
