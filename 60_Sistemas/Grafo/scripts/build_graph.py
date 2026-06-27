#!/usr/bin/env python3
"""
FabioOS - Fase 13: construtor minimo do grafo de conhecimento.

Le Markdown curado do vault, extrai wikilinks/frontmatter/tags e gera
60_Sistemas/Grafo/data/grafo_fabioos.json.

Nao usa API, nao chama LLM, nao toca no RAG e nao escreve fora de data/.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except Exception:
        pass

SCRIPT_DIR = Path(__file__).resolve().parent
GRAPH_ROOT = SCRIPT_DIR.parent
VAULT_ROOT = GRAPH_ROOT.parents[1]
OUT_PATH = GRAPH_ROOT / "data" / "grafo_fabioos.json"

INCLUDE_DIRS = [
    "00_Arquitetura",
    "10_Mapas",
    "20_Projetos",
    "30_Conhecimento",
    "40_Decisoes",
    "50_Registros",
    "60_Sistemas",
    "wiki",
]

EXCLUDE_PARTS = {
    ".git",
    ".obsidian",
    ".claude",
    ".codex",
    ".venv",
    "__pycache__",
    "node_modules",
    "site-packages",
    "fabioos_db",
    "logs",
    "_inbox",
    "00_Inbox",
    "90_Arquivo",
}

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
TAG_RE = re.compile(r"(?<!\w)#([A-Za-z0-9_\-/]+)")
HEADING_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
KEY_VALUE_RE = re.compile(r"^([A-Za-z0-9_\-]+):\s*(.*)$")


def rel_path(path: Path) -> str:
    return path.relative_to(VAULT_ROOT).as_posix()


def note_id_from_path(path: Path) -> str:
    return rel_path(path.with_suffix(""))


def stable_slug(value: str) -> str:
    value = value.strip().replace("\\", "/")
    value = re.sub(r"\s+", "_", value)
    value = re.sub(r"[^A-Za-z0-9_\-./]", "", value)
    return value.strip("_") or "sem_nome"


def is_safe(path: Path) -> bool:
    parts = set(path.relative_to(VAULT_ROOT).parts)
    if parts & EXCLUDE_PARTS:
        return False
    text_path = rel_path(path)
    if "/logs/" in text_path or "agentes_log" in text_path:
        return False
    return True


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    raw = parts[1]
    body = parts[2].lstrip()
    meta: dict[str, Any] = {}
    current_key = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        match = KEY_VALUE_RE.match(line)
        if match:
            key, value = match.groups()
            value = value.strip()
            if value.startswith("[") and value.endswith("]"):
                items = [item.strip().strip("'\"") for item in value[1:-1].split(",") if item.strip()]
                meta[key] = items
            else:
                meta[key] = value.strip("'\"")
            current_key = key
        elif current_key and line.strip().startswith("- "):
            meta.setdefault(current_key, [])
            if not isinstance(meta[current_key], list):
                meta[current_key] = [str(meta[current_key])]
            meta[current_key].append(line.strip()[2:].strip("'\""))
    return meta, body


def collect_markdown() -> list[Path]:
    files: list[Path] = []
    for folder in INCLUDE_DIRS:
        base = VAULT_ROOT / folder
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            if is_safe(path):
                files.append(path)
    return sorted(files)


def title_from(path: Path, body: str) -> str:
    match = HEADING_RE.search(body)
    if match:
        return match.group(1).strip()
    return path.stem.replace("_", " ").replace("-", " ")


def infer_domain(path: Path, meta: dict[str, Any]) -> str:
    raw_project = str(meta.get("projeto", "")).lower()
    p = rel_path(path).lower()
    if "primus" in p or "primus" in raw_project:
        return "PrimusOS"
    if "pietra" in p or "pietra" in raw_project:
        return "PietraOS"
    return "FabioOS"


def infer_type(path: Path, meta: dict[str, Any]) -> str:
    explicit = str(meta.get("tipo", "")).strip().lower()
    p = rel_path(path).lower()
    if explicit in {"sistema", "protocolo", "plano-mestre"} or p.startswith("60_sistemas/"):
        return "Sistema" if p.count("/") <= 2 else "Nota"
    if explicit in {"conceito", "wiki"} or p.startswith("wiki/conceitos/") or p.startswith("30_conhecimento/"):
        return "Conceito"
    if "projeto" in explicit or p.startswith("20_projetos/") or p.startswith("wiki/projetos/"):
        return "Projeto"
    if "decis" in explicit or p.startswith("40_decisoes/"):
        return "Decisao"
    if "changelog" in explicit or p.startswith("50_registros/"):
        return "Log"
    return "Nota"


def normalize_tags(meta: dict[str, Any], body: str) -> list[str]:
    tags: set[str] = set()
    raw = meta.get("tags", [])
    if isinstance(raw, str):
        raw = raw.strip("[]")
        tags.update(t.strip().strip("'\"#") for t in raw.split(",") if t.strip())
    elif isinstance(raw, list):
        tags.update(str(t).strip().strip("#") for t in raw if str(t).strip())
    tags.update(tag.strip("/") for tag in TAG_RE.findall(body))
    return sorted(t for t in tags if t)


def build_aliases(files: list[Path], notes: dict[str, dict[str, Any]]) -> dict[str, str]:
    aliases: dict[str, str] = {}
    for path in files:
        node_id = note_id_from_path(path)
        stem = path.stem
        aliases.setdefault(stem.lower(), node_id)
        aliases.setdefault(stem.replace("_", " ").lower(), node_id)
        aliases.setdefault(rel_path(path.with_suffix("")).lower(), node_id)
        title = notes[node_id]["nome"]
        aliases.setdefault(title.lower(), node_id)
    return aliases


def resolve_wikilink(target: str, aliases: dict[str, str]) -> str:
    key = target.strip().lower()
    if key in aliases:
        return aliases[key]
    key_md = key.removesuffix(".md")
    if key_md in aliases:
        return aliases[key_md]
    return f"Conceito:{stable_slug(target)}"


def add_node(nodes: dict[str, dict[str, Any]], node: dict[str, Any]) -> None:
    nodes.setdefault(node["id"], node)


def edge_key(edge: dict[str, Any]) -> tuple[str, str, str, str]:
    return (
        edge["origem"],
        edge["destino"],
        edge["tipo"],
        str(edge.get("fonte", "")),
    )


def main() -> int:
    files = collect_markdown()
    nodes: dict[str, dict[str, Any]] = {}
    note_bodies: dict[str, str] = {}

    for path in files:
        text = read_text(path)
        meta, body = parse_frontmatter(text)
        node_id = note_id_from_path(path)
        domain = infer_domain(path, meta)
        node = {
            "id": node_id,
            "tipo": infer_type(path, meta),
            "nome": title_from(path, body),
            "caminho": rel_path(path),
            "dominio": domain,
            "status": str(meta.get("status", "")),
            "fonte_principal": rel_path(path),
            "confianca": 1.0,
        }
        add_node(nodes, node)
        note_bodies[node_id] = body

    aliases = build_aliases(files, nodes)
    edges: dict[tuple[str, str, str, str], dict[str, Any]] = {}

    def add_edge(origem: str, destino: str, tipo: str, fonte: str, confianca: float, observacao: str = "") -> None:
        edge = {
            "origem": origem,
            "destino": destino,
            "tipo": tipo,
            "fonte": fonte,
            "confianca": confianca,
            "observacao": observacao,
        }
        edges.setdefault(edge_key(edge), edge)

    for path in files:
        node_id = note_id_from_path(path)
        body = note_bodies[node_id]
        text = read_text(path)
        meta, _ = parse_frontmatter(text)
        source = rel_path(path)
        domain = infer_domain(path, meta)

        domain_id = f"Dominio:{domain}"
        add_node(nodes, {
            "id": domain_id,
            "tipo": "Dominio",
            "nome": domain,
            "caminho": "",
            "dominio": domain,
            "status": "ativo",
            "fonte_principal": "00_Arquitetura/01_Modelo_Formal_FabioOS_MEGATRON.md",
            "confianca": 0.9,
        })
        add_edge(node_id, domain_id, "pertence_a", source, 0.9, "dominio inferido pelo caminho/metadados")

        top_folder = source.split("/", 1)[0]
        folder_id = f"Dominio:{top_folder}"
        add_node(nodes, {
            "id": folder_id,
            "tipo": "Dominio",
            "nome": top_folder,
            "caminho": top_folder,
            "dominio": domain,
            "status": "ativo",
            "fonte_principal": source,
            "confianca": 0.8,
        })
        add_edge(node_id, folder_id, "pertence_a", source, 0.8, "pasta raiz do vault")

        project = str(meta.get("projeto", "")).strip()
        if project:
            project_id = f"Projeto:{stable_slug(project)}"
            add_node(nodes, {
                "id": project_id,
                "tipo": "Projeto",
                "nome": project,
                "caminho": "",
                "dominio": domain,
                "status": "ativo",
                "fonte_principal": source,
                "confianca": 0.8,
            })
            add_edge(node_id, project_id, "pertence_a", source, 0.85, "frontmatter projeto")

        for tag in normalize_tags(meta, body):
            tag_id = f"Tag:{stable_slug(tag)}"
            add_node(nodes, {
                "id": tag_id,
                "tipo": "Tag",
                "nome": tag,
                "caminho": "",
                "dominio": domain,
                "status": "ativo",
                "fonte_principal": source,
                "confianca": 0.8,
            })
            add_edge(node_id, tag_id, "classifica", source, 0.8, "tag declarada")

        if source.startswith("60_Sistemas/"):
            system_name = source.split("/")[1] if "/" in source else Path(source).stem
            system_id = f"Sistema:{stable_slug(system_name)}"
            add_node(nodes, {
                "id": system_id,
                "tipo": "Sistema",
                "nome": system_name,
                "caminho": f"60_Sistemas/{system_name}",
                "dominio": domain,
                "status": "ativo",
                "fonte_principal": source,
                "confianca": 0.8,
            })
            add_edge(node_id, system_id, "documenta", source, 0.8, "documento dentro de 60_Sistemas")

        for target in WIKILINK_RE.findall(body):
            dest = resolve_wikilink(target, aliases)
            if dest not in nodes:
                add_node(nodes, {
                    "id": dest,
                    "tipo": "Conceito",
                    "nome": target.strip(),
                    "caminho": "",
                    "dominio": domain,
                    "status": "referenciado",
                    "fonte_principal": source,
                    "confianca": 0.55,
                })
            add_edge(node_id, dest, "referencia", source, 0.75, "wikilink")

    node_list = sorted(nodes.values(), key=lambda n: n["id"])
    edge_list = sorted(edges.values(), key=lambda e: (e["tipo"], e["origem"], e["destino"]))
    node_counts = Counter(node["tipo"] for node in node_list)
    edge_counts = Counter(edge["tipo"] for edge in edge_list)
    degree = defaultdict(int)
    for edge in edge_list:
        degree[edge["origem"]] += 1
        degree[edge["destino"]] += 1
    top_nodes = sorted(degree.items(), key=lambda item: item[1], reverse=True)[:20]

    payload = {
        "metadata": {
            "gerado_em": datetime.now().isoformat(timespec="seconds"),
            "fase": 13,
            "status": "minimo-funcional",
            "vault_root": str(VAULT_ROOT),
            "arquivos_markdown_lidos": len(files),
            "sem_rag": True,
            "sem_api_externa": True,
        },
        "metricas": {
            "total_nos": len(node_list),
            "total_arestas": len(edge_list),
            "nos_por_tipo": dict(sorted(node_counts.items())),
            "arestas_por_tipo": dict(sorted(edge_counts.items())),
            "top_nos_por_grau": [{"id": node_id, "grau": count} for node_id, count in top_nodes],
        },
        "nodes": node_list,
        "edges": edge_list,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Grafo gerado: {OUT_PATH.relative_to(VAULT_ROOT).as_posix()}")
    print(f"Arquivos lidos: {len(files)}")
    print(f"Nos: {len(node_list)}")
    print(f"Arestas: {len(edge_list)}")
    print("Nos por tipo:")
    for key, value in sorted(node_counts.items()):
        print(f"  {key}: {value}")
    print("Arestas por tipo:")
    for key, value in sorted(edge_counts.items()):
        print(f"  {key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
