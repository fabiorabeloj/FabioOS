#!/usr/bin/env python3
"""
FabioOS - Fase 13: consulta local do grafo.

Permite buscar nos, listar hubs e inspecionar vizinhanca sem depender de
Neo4j, RAG ou API externa.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except Exception:
        pass

SCRIPT_DIR = Path(__file__).resolve().parent
GRAPH_ROOT = SCRIPT_DIR.parent
GRAPH_JSON = GRAPH_ROOT / "data" / "grafo_fabioos.json"


def load_graph() -> dict[str, Any]:
    if not GRAPH_JSON.exists():
        raise FileNotFoundError(
            f"Grafo nao encontrado: {GRAPH_JSON}. Rode build_graph.py primeiro."
        )
    return json.loads(GRAPH_JSON.read_text(encoding="utf-8"))


def node_label(node: dict[str, Any]) -> str:
    return f"{node['id']} | {node.get('tipo', '')} | {node.get('nome', '')}"


def search_nodes(graph: dict[str, Any], term: str, limit: int) -> None:
    q = term.lower()
    matches = []
    for node in graph["nodes"]:
        haystack = " ".join(
            str(node.get(k, "")) for k in ("id", "nome", "tipo", "dominio", "caminho")
        ).lower()
        if q in haystack:
            matches.append(node)

    print(f"Resultados para {term!r}: {len(matches)}")
    for node in matches[:limit]:
        print(f"- {node_label(node)}")


def top_nodes(graph: dict[str, Any], limit: int) -> None:
    degree: dict[str, int] = defaultdict(int)
    incoming: dict[str, int] = defaultdict(int)
    outgoing: dict[str, int] = defaultdict(int)
    nodes = {node["id"]: node for node in graph["nodes"]}

    for edge in graph["edges"]:
        origem = edge["origem"]
        destino = edge["destino"]
        degree[origem] += 1
        degree[destino] += 1
        outgoing[origem] += 1
        incoming[destino] += 1

    ranking = sorted(degree.items(), key=lambda item: item[1], reverse=True)
    print(f"Top {limit} nos por grau:")
    for node_id, total in ranking[:limit]:
        node = nodes.get(node_id, {"id": node_id, "tipo": "", "nome": ""})
        print(
            f"- {node_label(node)} | grau={total} "
            f"in={incoming[node_id]} out={outgoing[node_id]}"
        )


def neighborhood(graph: dict[str, Any], node_id: str, limit: int) -> None:
    nodes = {node["id"]: node for node in graph["nodes"]}
    if node_id not in nodes:
        print(f"No nao encontrado: {node_id}")
        print("Dica: use --search para localizar o id exato.")
        return

    outgoing = [edge for edge in graph["edges"] if edge["origem"] == node_id]
    incoming = [edge for edge in graph["edges"] if edge["destino"] == node_id]
    print(f"No: {node_label(nodes[node_id])}")
    print(f"Saidas: {len(outgoing)} | Entradas: {len(incoming)}")

    if outgoing:
        print("\nSaidas:")
        for edge in outgoing[:limit]:
            dest = nodes.get(edge["destino"], {"id": edge["destino"], "tipo": "", "nome": ""})
            print(f"- {edge['tipo']} -> {node_label(dest)}")

    if incoming:
        print("\nEntradas:")
        for edge in incoming[:limit]:
            orig = nodes.get(edge["origem"], {"id": edge["origem"], "tipo": "", "nome": ""})
            print(f"- {node_label(orig)} -> {edge['tipo']}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--search", help="buscar nos por termo")
    parser.add_argument("--node", help="inspecionar vizinhanca de um no por id")
    parser.add_argument("--top", type=int, help="listar hubs por grau")
    parser.add_argument("--limit", type=int, default=15, help="limite de resultados")
    args = parser.parse_args()

    graph = load_graph()
    if args.search:
        search_nodes(graph, args.search, args.limit)
    elif args.node:
        neighborhood(graph, args.node, args.limit)
    elif args.top:
        top_nodes(graph, args.top)
    else:
        parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
