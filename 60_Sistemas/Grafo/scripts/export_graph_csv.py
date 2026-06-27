#!/usr/bin/env python3
"""
FabioOS - Fase 13: exportacao CSV do grafo.

Le data/grafo_fabioos.json e gera arquivos CSV simples para Neo4j, Gephi
ou auditoria em planilha. Nao acessa rede, nao usa RAG e nao altera arquivos
fora de 60_Sistemas/Grafo/data/.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path
from typing import Any

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8")
    except Exception:
        pass

SCRIPT_DIR = Path(__file__).resolve().parent
GRAPH_ROOT = SCRIPT_DIR.parent
DATA_DIR = GRAPH_ROOT / "data"
GRAPH_JSON = DATA_DIR / "grafo_fabioos.json"
NODES_CSV = DATA_DIR / "neo4j_nodes.csv"
EDGES_CSV = DATA_DIR / "neo4j_edges.csv"
GEPHI_EDGES_CSV = DATA_DIR / "gephi_edges.csv"


def load_graph() -> dict[str, Any]:
    if not GRAPH_JSON.exists():
        raise FileNotFoundError(
            f"Grafo nao encontrado: {GRAPH_JSON}. Rode build_graph.py primeiro."
        )
    return json.loads(GRAPH_JSON.read_text(encoding="utf-8"))


def clean(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value).replace("\r", " ").replace("\n", " ").strip()


def neo4j_label(tipo: str) -> str:
    label = "".join(ch for ch in tipo.title() if ch.isalnum())
    return label or "Entidade"


def neo4j_relationship(tipo: str) -> str:
    rel = "".join(ch.upper() if ch.isalnum() else "_" for ch in tipo)
    rel = "_".join(part for part in rel.split("_") if part)
    return rel or "RELACIONA"


def export_nodes(nodes: list[dict[str, Any]]) -> None:
    fields = [
        "id:ID",
        "nome",
        "tipo",
        "dominio",
        "status",
        "caminho",
        "fonte_principal",
        "confianca:float",
        ":LABEL",
    ]
    with NODES_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for node in nodes:
            writer.writerow({
                "id:ID": clean(node.get("id")),
                "nome": clean(node.get("nome")),
                "tipo": clean(node.get("tipo")),
                "dominio": clean(node.get("dominio")),
                "status": clean(node.get("status")),
                "caminho": clean(node.get("caminho")),
                "fonte_principal": clean(node.get("fonte_principal")),
                "confianca:float": clean(node.get("confianca")),
                ":LABEL": neo4j_label(clean(node.get("tipo"))),
            })


def export_edges(edges: list[dict[str, Any]]) -> None:
    fields = [
        ":START_ID",
        ":END_ID",
        "tipo",
        "fonte",
        "confianca:float",
        "observacao",
        ":TYPE",
    ]
    with EDGES_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for edge in edges:
            writer.writerow({
                ":START_ID": clean(edge.get("origem")),
                ":END_ID": clean(edge.get("destino")),
                "tipo": clean(edge.get("tipo")),
                "fonte": clean(edge.get("fonte")),
                "confianca:float": clean(edge.get("confianca")),
                "observacao": clean(edge.get("observacao")),
                ":TYPE": neo4j_relationship(clean(edge.get("tipo"))),
            })


def export_gephi_edges(edges: list[dict[str, Any]]) -> None:
    fields = ["Source", "Target", "Type", "Label", "Weight", "Fonte"]
    with GEPHI_EDGES_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for edge in edges:
            writer.writerow({
                "Source": clean(edge.get("origem")),
                "Target": clean(edge.get("destino")),
                "Type": "Directed",
                "Label": clean(edge.get("tipo")),
                "Weight": clean(edge.get("confianca")),
                "Fonte": clean(edge.get("fonte")),
            })


def main() -> int:
    graph = load_graph()
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    export_nodes(nodes)
    export_edges(edges)
    export_gephi_edges(edges)
    print(f"Nos exportados: {len(nodes)} -> {NODES_CSV.relative_to(GRAPH_ROOT)}")
    print(f"Arestas Neo4j: {len(edges)} -> {EDGES_CSV.relative_to(GRAPH_ROOT)}")
    print(f"Arestas Gephi: {len(edges)} -> {GEPHI_EDGES_CSV.relative_to(GRAPH_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
