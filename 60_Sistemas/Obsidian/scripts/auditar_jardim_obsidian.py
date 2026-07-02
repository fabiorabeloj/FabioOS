#!/usr/bin/env python
"""
Audita a jardinagem do vault FabioOS/Obsidian.

Verifica:
- frontmatter ausente;
- status de Jardim Digital ausente;
- wikilinks quebrados;
- candidatos a no solto;
- hubs mais conectados.

Nao altera arquivos. Gera relatorio Markdown quando usado com --write-report.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


IGNORE_PARTS = {
    ".git",
    ".agents",
    ".claude",
    ".codex",
    ".obsidian",
    "node_modules",
    ".venv",
    "__pycache__",
    "90_Arquivo",
    "apps",
}

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


@dataclass
class Note:
    path: Path
    rel: str
    text: str
    has_frontmatter: bool
    has_status: bool
    status: str | None
    links: list[str]


def should_skip(path: Path) -> bool:
    return any(part in IGNORE_PARTS or part.startswith(".") for part in path.parts)


def read_note(path: Path, root: Path) -> Note:
    text = path.read_text(encoding="utf-8", errors="replace")
    rel = path.relative_to(root).as_posix()
    has_frontmatter = text.startswith("---\n") or text.startswith("---\r\n")
    status = None
    has_status = False
    if has_frontmatter:
        parts = re.split(r"\r?\n---\r?\n", text, maxsplit=1)
        if parts:
            frontmatter = parts[0].replace("---", "", 1)
            match = re.search(r"(?m)^status:\s*([A-Za-z0-9_-]+)\s*$", frontmatter)
            if match:
                status = match.group(1)
                has_status = True
    links = [m.group(1).strip() for m in WIKILINK_RE.finditer(text)]
    return Note(path, rel, text, has_frontmatter, has_status, status, links)


def candidate_targets(notes: list[Note]) -> set[str]:
    targets: set[str] = set()
    for note in notes:
        no_ext = note.path.with_suffix("")
        rel_no_ext = no_ext.as_posix()
        name_no_ext = note.path.stem
        targets.add(note.rel[:-3] if note.rel.endswith(".md") else note.rel)
        targets.add(rel_no_ext)
        targets.add(name_no_ext)
    return targets


def resolve_target(target: str, valid_targets: set[str]) -> bool:
    clean = target.strip().replace("\\", "/")
    if clean in valid_targets:
        return True
    if clean.endswith(".md") and clean[:-3] in valid_targets:
        return True
    return False


def maturity_counts(notes: list[Note]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for note in notes:
        counts[note.status or "sem_status"] += 1
    return counts


def write_report(root: Path, notes: list[Note], report_path: Path) -> None:
    valid_targets = candidate_targets(notes)
    incoming: dict[str, int] = defaultdict(int)
    missing_links: list[tuple[str, str]] = []
    outlinks_count: Counter[str] = Counter()

    for note in notes:
        outlinks_count[note.rel] = len(note.links)
        for link in note.links:
            if resolve_target(link, valid_targets):
                incoming[link] += 1
            else:
                missing_links.append((note.rel, link))

    rel_set = {note.rel for note in notes}
    stem_to_rel: dict[str, list[str]] = defaultdict(list)
    for note in notes:
        stem_to_rel[note.path.stem].append(note.rel)
        stem_to_rel[note.rel[:-3] if note.rel.endswith(".md") else note.rel].append(note.rel)

    resolved_incoming: Counter[str] = Counter()
    for note in notes:
        for link in note.links:
            clean = link.replace("\\", "/")
            candidates = stem_to_rel.get(clean, [])
            if not candidates and clean.endswith(".md"):
                candidates = stem_to_rel.get(clean[:-3], [])
            if candidates:
                resolved_incoming[candidates[0]] += 1

    no_solto = []
    for note in notes:
        if note.rel.endswith("README.md"):
            continue
        if note.rel.startswith("50_Registros/Changelog/"):
            continue
        if resolved_incoming[note.rel] == 0 and len(note.links) == 0:
            no_solto.append(note.rel)

    no_frontmatter = [n.rel for n in notes if not n.has_frontmatter]
    no_status = [n.rel for n in notes if n.has_frontmatter and not n.has_status]
    maturity = maturity_counts(notes)
    top_incoming = resolved_incoming.most_common(20)
    top_outgoing = outlinks_count.most_common(20)

    lines: list[str] = []
    lines.append("---")
    lines.append("tipo: auditoria")
    lines.append("area: 50_Registros")
    lines.append("sistema: Obsidian")
    lines.append("projeto: FabioOS")
    lines.append("status: concluido")
    lines.append("classe_dado: interno")
    lines.append("criado_em: 2026-07-02")
    lines.append("tags: [obsidian, pkm, jardim-digital, auditoria]")
    lines.append("---")
    lines.append("")
    lines.append("# Auditoria de Jardinagem Obsidian")
    lines.append("")
    lines.append("## Resumo")
    lines.append("")
    lines.append(f"- Notas auditadas: `{len(notes)}`")
    lines.append(f"- Sem frontmatter: `{len(no_frontmatter)}`")
    lines.append(f"- Com frontmatter sem status: `{len(no_status)}`")
    lines.append(f"- Wikilinks quebrados: `{len(missing_links)}`")
    lines.append(f"- Candidatos a no solto: `{len(no_solto)}`")
    lines.append("")
    lines.append("## Maturidade")
    lines.append("")
    lines.append("| Status | Quantidade |")
    lines.append("|---|---:|")
    for status, count in sorted(maturity.items()):
        lines.append(f"| {status} | {count} |")
    lines.append("")
    lines.append("## Wikilinks quebrados - primeiros 50")
    lines.append("")
    if missing_links:
        lines.append("| Arquivo | Link |")
        lines.append("|---|---|")
        for rel, link in missing_links[:50]:
            lines.append(f"| `{rel}` | `[[{link}]]` |")
    else:
        lines.append("Nenhum wikilink quebrado encontrado.")
    lines.append("")
    lines.append("## Candidatos a no solto - primeiros 50")
    lines.append("")
    if no_solto:
        for rel in no_solto[:50]:
            lines.append(f"- `{rel}`")
    else:
        lines.append("Nenhum candidato critico encontrado.")
    lines.append("")
    lines.append("## Hubs por entrada")
    lines.append("")
    lines.append("| Nota | Inlinks |")
    lines.append("|---|---:|")
    for rel, count in top_incoming:
        lines.append(f"| `{rel}` | {count} |")
    lines.append("")
    lines.append("## Notas com mais saidas")
    lines.append("")
    lines.append("| Nota | Outlinks |")
    lines.append("|---|---:|")
    for rel, count in top_outgoing:
        lines.append(f"| `{rel}` | {count} |")
    lines.append("")
    lines.append("## Proximas acoes")
    lines.append("")
    lines.append("- Corrigir wikilinks quebrados que estejam em hubs vivos.")
    lines.append("- Adicionar `status` primeiro em dashboards, MOCs, specs e notas evergreen.")
    lines.append("- Arquivar ou conectar candidatos a no solto apenas depois de verificar valor real.")
    lines.append("- Evitar criar stubs massivos sem MOC.")
    lines.append("")
    lines.append("## Relacoes")
    lines.append("")
    lines.append("- [[60_Sistemas/Obsidian/Protocolo_Revisao_Links_Nos_Obsidian]]")
    lines.append("- [[40_Wiki/_MOCs/MOC_Obsidian_FabioOS]]")
    lines.append("- [[40_Wiki/FabioOS/Gargalos_Sistemicos_FabioOS_MEGATRON]]")

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--write-report", default="")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    notes = [
        read_note(path, root)
        for path in root.rglob("*.md")
        if not should_skip(path.relative_to(root))
    ]
    valid_targets = candidate_targets(notes)
    missing_links = []
    for note in notes:
        for link in note.links:
            if not resolve_target(link, valid_targets):
                missing_links.append((note.rel, link))

    no_frontmatter = sum(1 for n in notes if not n.has_frontmatter)
    no_status = sum(1 for n in notes if n.has_frontmatter and not n.has_status)
    print(f"notes={len(notes)}")
    print(f"missing_frontmatter={no_frontmatter}")
    print(f"frontmatter_without_status={no_status}")
    print(f"missing_wikilinks={len(missing_links)}")

    if args.write_report:
        write_report(root, notes, root / args.write_report)
        print(f"report={args.write_report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
