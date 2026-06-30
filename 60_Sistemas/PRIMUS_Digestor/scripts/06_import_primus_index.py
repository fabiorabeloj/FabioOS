from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

from primus_digestor_common import short_snippet, stable_id, write_jsonl


TYPE_BY_CATEGORY = {
    "ENTIDADES": "creature",
    "EVENTOS": "encounter",
    "FUNCOES": "procedure",
    "GRUPOS": "faction",
    "LOCAIS": "site",
    "OBJETOS": "item",
    "INDEFINIDO": "rule",
}


def box_for(type_name: str) -> str:
    if type_name in {"creature", "npc", "deity"}:
        return "Bestiario"
    if type_name in {"site", "region", "settlement", "dungeon", "plane"}:
        return "Atlas"
    if type_name in {"encounter", "procedure", "reward", "consequence"}:
        return "Motor"
    return "Grimorio"


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Import records from the existing PRIMUS Index SQLite.")
    parser.add_argument("--db", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--query", default="")
    parser.add_argument("--book", default="")
    parser.add_argument("--category", default="")
    parser.add_argument("--limit", type=int, default=50)
    args = parser.parse_args()

    db_path = Path(args.db)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    where = []
    params: list[object] = []
    if args.query:
        where.append("(name LIKE ? OR text LIKE ?)")
        params.extend([f"%{args.query}%", f"%{args.query}%"])
    if args.book:
        where.append("book_key = ?")
        params.append(args.book)
    if args.category:
        where.append("category = ?")
        params.append(args.category)
    where_sql = "WHERE " + " AND ".join(where) if where else ""
    params.append(args.limit)

    rows = conn.execute(
        f"""
        SELECT id, category, COALESCE(name, '') AS name, book_key, page, text
        FROM records
        {where_sql}
        ORDER BY book_key, page, name
        LIMIT ?
        """,
        params,
    ).fetchall()
    conn.close()

    entries = []
    for row in rows:
        type_name = TYPE_BY_CATEGORY.get(row["category"], "rule")
        name = row["name"] or short_snippet(row["text"], limit=60) or row["id"]
        entries.append(
            {
                "EntryID": stable_id("primus-index", row["id"], prefix="ce"),
                "Type": type_name,
                "Name": name,
                "Box": box_for(type_name),
                "Subbox": "Canon",
                "Source": f"PRIMUS Index:{row['book_key']}",
                "SourcePath": str(db_path),
                "Page": row["page"],
                "Snippet": short_snippet(row["text"]),
                "Summary": short_snippet(row["text"], limit=140),
                "Affects": ["catalog", "validation"],
                "NeverAffects": ["worldstate_without_delta_p", "public_export_without_license_review"],
                "InstancingHints": ["review_for_catalog_pool"],
                "Confidence": "Low" if row["category"] == "INDEFINIDO" else "Medium",
                "LicenseStatus": "Restricted",
                "Notes": f"Imported from primus.sqlite record {row['id']}; review before promotion.",
            }
        )

    write_jsonl(Path(args.out), entries)
    print(f"imported {len(entries)} entries -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
