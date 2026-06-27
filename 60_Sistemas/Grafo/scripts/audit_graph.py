#!/usr/bin/env python3
"""
FabioOS - Fase 13: auditoria local do grafo.

Valida consistencia basica do JSON gerado, calcula cobertura e escreve um
relatorio Markdown em data/auditoria_grafo.md. Nao acessa rede, RAG ou Git.
"""
from __future__ import annotations

import json
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
DATA_DIR = GRAPH_ROOT / "data"
GRAPH_JSON = DATA_DIR / "grafo_fabioos.json"
REPORT_MD = DATA_DIR / "auditoria_grafo.md"
REPORT_JSON = DATA_DIR / "auditoria_grafo.json"


def load_graph() -> dict[str, Any]:
    if not GRAPH_JSON.exists():
        raise FileNotFoundError(
            f"Grafo nao encontrado: {GRAPH_JSON}. Rode build_graph.py primeiro."
        )
    return json.loads(GRAPH_JSON.read_text(encoding="utf-8"))


def top_items(counter: Counter[str], limit: int = 15) -> list[tuple[str, int]]:
    return counter.most_common(limit)


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    out = ["| " + " | ".join(headers) + " |"]
    out.append("|" + "|".join("---" for _ in headers) + "|")
    for row in rows:
        out.append("| " + " | ".join(str(item) for item in row) + " |")
    return "\n".join(out)


def audit(graph: dict[str, Any]) -> dict[str, Any]:
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    node_ids = {node["id"] for node in nodes}
    node_by_id = {node["id"]: node for node in nodes}

    orphan_edges = [
        edge for edge in edges
        if edge.get("origem") not in node_ids or edge.get("destino") not in node_ids
    ]

    degree: Counter[str] = Counter()
    incoming: Counter[str] = Counter()
    outgoing: Counter[str] = Counter()
    relation_counter: Counter[str] = Counter()
    domain_counter: Counter[str] = Counter()
    type_counter: Counter[str] = Counter()
    source_counter: Counter[str] = Counter()

    for node in nodes:
        domain_counter[str(node.get("dominio", "") or "sem_dominio")] += 1
        type_counter[str(node.get("tipo", "") or "sem_tipo")] += 1

    for edge in edges:
        origem = edge.get("origem", "")
        destino = edge.get("destino", "")
        relation_counter[str(edge.get("tipo", "") or "sem_tipo")] += 1
        source_counter[str(edge.get("fonte", "") or "sem_fonte")] += 1
        if origem in node_ids:
            outgoing[origem] += 1
            degree[origem] += 1
        if destino in node_ids:
            incoming[destino] += 1
            degree[destino] += 1

    isolated_nodes = [node for node in nodes if degree[node["id"]] == 0]
    referenced_concepts = [
        node for node in nodes
        if node["id"].startswith("Conceito:")
        and not node.get("caminho")
        and node.get("status") == "referenciado"
    ]

    top_hubs = []
    for node_id, total in degree.most_common(20):
        node = node_by_id[node_id]
        top_hubs.append({
            "id": node_id,
            "nome": node.get("nome", ""),
            "tipo": node.get("tipo", ""),
            "grau": total,
            "entrada": incoming[node_id],
            "saida": outgoing[node_id],
        })

    total_nodes = len(nodes)
    total_edges = len(edges)
    connected_nodes = total_nodes - len(isolated_nodes)
    connected_ratio = connected_nodes / total_nodes if total_nodes else 0.0

    return {
        "metadata": {
            "gerado_em": datetime.now().isoformat(timespec="seconds"),
            "grafo": str(GRAPH_JSON.relative_to(GRAPH_ROOT)),
        },
        "resumo": {
            "total_nos": total_nodes,
            "total_arestas": total_edges,
            "arestas_orfas": len(orphan_edges),
            "nos_isolados": len(isolated_nodes),
            "conceitos_referenciados_sem_arquivo": len(referenced_concepts),
            "nos_conectados_percentual": round(connected_ratio * 100, 2),
        },
        "contagens": {
            "nos_por_tipo": dict(sorted(type_counter.items())),
            "nos_por_dominio": dict(sorted(domain_counter.items())),
            "arestas_por_tipo": dict(sorted(relation_counter.items())),
            "fontes_mais_conectadas": dict(top_items(source_counter, 15)),
        },
        "top_hubs": top_hubs,
        "amostras": {
            "arestas_orfas": orphan_edges[:20],
            "nos_isolados": isolated_nodes[:20],
            "conceitos_referenciados_sem_arquivo": referenced_concepts[:30],
        },
    }


def render_markdown(result: dict[str, Any]) -> str:
    resumo = result["resumo"]
    contagens = result["contagens"]

    lines = [
        "---",
        "tipo: relatorio",
        "area: 60_Sistemas",
        "projeto: FabioOS",
        "fase: 13",
        "status: auditoria-local",
        "tags: [fabios, grafo, auditoria, fase-13]",
        f"criado_em: {datetime.now().date()}",
        f"atualizado_em: {datetime.now().date()}",
        "---",
        "",
        "# Auditoria Local do Grafo FabioOS",
        "",
        "## Funcao",
        "",
        "Registrar metricas de consistencia e cobertura do grafo minimo da Fase 13.",
        "",
        "## Resumo",
        "",
        markdown_table(
            ["Metrica", "Valor"],
            [
                ["Nos", resumo["total_nos"]],
                ["Arestas", resumo["total_arestas"]],
                ["Arestas orfas", resumo["arestas_orfas"]],
                ["Nos isolados", resumo["nos_isolados"]],
                ["Conceitos referenciados sem arquivo", resumo["conceitos_referenciados_sem_arquivo"]],
                ["Nos conectados", f"{resumo['nos_conectados_percentual']}%"],
            ],
        ),
        "",
        "## Nos por tipo",
        "",
        markdown_table(
            ["Tipo", "Quantidade"],
            [[key, value] for key, value in contagens["nos_por_tipo"].items()],
        ),
        "",
        "## Nos por dominio",
        "",
        markdown_table(
            ["Dominio", "Quantidade"],
            [[key, value] for key, value in contagens["nos_por_dominio"].items()],
        ),
        "",
        "## Arestas por tipo",
        "",
        markdown_table(
            ["Relacao", "Quantidade"],
            [[key, value] for key, value in contagens["arestas_por_tipo"].items()],
        ),
        "",
        "## Top hubs",
        "",
        markdown_table(
            ["No", "Tipo", "Grau", "Entrada", "Saida"],
            [
                [item["id"], item["tipo"], item["grau"], item["entrada"], item["saida"]]
                for item in result["top_hubs"][:15]
            ],
        ),
        "",
        "## Diagnostico",
        "",
    ]

    if resumo["arestas_orfas"] == 0:
        lines.append("- Aprovado: nenhuma aresta orfa encontrada.")
    else:
        lines.append(f"- Atencao: {resumo['arestas_orfas']} arestas orfas encontradas.")

    if resumo["nos_isolados"] == 0:
        lines.append("- Aprovado: nenhum no isolado encontrado.")
    else:
        lines.append(f"- Observacao: {resumo['nos_isolados']} nos isolados existem e devem ser revisados.")

    lines.extend([
        f"- Conceitos referenciados sem arquivo: {resumo['conceitos_referenciados_sem_arquivo']}.",
        "- Esta auditoria nao usa RAG, API externa, Neo4j ou Git.",
        "",
        "## Proximas acoes",
        "",
        "- [ ] Revisar conceitos referenciados sem arquivo e decidir quais devem virar notas wiki.",
        "- [ ] Revisar top hubs para detectar mapas excessivamente centrais.",
        "- [ ] Definir relacoes novas apenas quando houver fonte explicita.",
    ])
    return "\n".join(lines) + "\n"


def main() -> int:
    graph = load_graph()
    result = audit(graph)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    REPORT_MD.write_text(render_markdown(result), encoding="utf-8")
    resumo = result["resumo"]
    print(f"Auditoria Markdown: {REPORT_MD.relative_to(GRAPH_ROOT)}")
    print(f"Auditoria JSON: {REPORT_JSON.relative_to(GRAPH_ROOT)}")
    print(f"Nos: {resumo['total_nos']}")
    print(f"Arestas: {resumo['total_arestas']}")
    print(f"Arestas orfas: {resumo['arestas_orfas']}")
    print(f"Nos isolados: {resumo['nos_isolados']}")
    print(f"Conceitos sem arquivo: {resumo['conceitos_referenciados_sem_arquivo']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
