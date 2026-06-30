from __future__ import annotations

import sys
from pathlib import Path

from primus_digestor_common import read_jsonl, slugify


def yaml_value(value) -> str:
    if isinstance(value, list):
        if not value:
            return "[]"
        return "\n" + "\n".join(f"  - {item}" for item in value)
    if value is None:
        return ""
    text = str(value).replace("\n", " ").strip()
    return text


def render(entry: dict) -> str:
    frontmatter_fields = [
        "EntryID",
        "Type",
        "Name",
        "Box",
        "Subbox",
        "Source",
        "SourcePath",
        "Page",
        "Confidence",
        "LicenseStatus",
        "Affects",
        "NeverAffects",
        "InstancingHints",
    ]
    lines = ["---"]
    for field in frontmatter_fields:
        lines.append(f"{field}: {yaml_value(entry.get(field))}")
    lines.append("---")
    lines.append("")
    lines.append(f"# {entry.get('Name')}")
    lines.append("")
    lines.append("## Funcao no PRIMUS")
    lines.append(entry.get("Summary") or "Entrada gerada pelo PRIMUS Digestor; revisar antes de promover.")
    lines.append("")
    lines.append("## Fonte")
    lines.append(f"- Source: {entry.get('Source')}")
    lines.append(f"- Page: {entry.get('Page')}")
    lines.append(f"- LicenseStatus: {entry.get('LicenseStatus')}")
    lines.append("")
    lines.append("## Trecho de Rastreio")
    lines.append(entry.get("Snippet") or "")
    lines.append("")
    lines.append("## Encaixe")
    lines.append(f"- Type: {entry.get('Type')}")
    lines.append(f"- Box: {entry.get('Box')}")
    lines.append(f"- Subbox: {entry.get('Subbox')}")
    lines.append("")
    lines.append("## Como Vira Jogo")
    for hint in entry.get("InstancingHints") or []:
        lines.append(f"- {hint}")
    lines.append("")
    lines.append("## Revisao")
    lines.append("- [ ] Conferir fonte/pagina.")
    lines.append("- [ ] Confirmar tipo.")
    lines.append("- [ ] Aplicar V(E), V(I) ou V(P).")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Export PRIMUS CatalogEntries to Obsidian Markdown.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    entries = read_jsonl(Path(args.input))
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    for entry in entries:
        slug = slugify(f"{entry.get('Type')}-{entry.get('Name')}", fallback=entry.get("EntryID", "entry"))
        path = out_dir / f"{slug}.md"
        path.write_text(render(entry), encoding="utf-8", newline="\n")
    print(f"exported {len(entries)} markdown files -> {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
