#!/usr/bin/env python3
"""Registro local de nos do MEGATRON.

v0: configuracao estatica, sem rede e sem dependencias externas.
Serve para validar a topologia e escolher um no por capacidade.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


BASE = Path(__file__).resolve().parent
DEFAULT_REGISTRY = BASE / "nodes.megatron.example.json"


def load_registry(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_registry(registry: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not isinstance(registry.get("nodes"), list):
        return ["Campo 'nodes' deve ser uma lista."]

    seen: set[str] = set()
    for idx, node in enumerate(registry["nodes"]):
        prefix = f"nodes[{idx}]"
        for key in ("id", "role", "status", "host", "priority", "capabilities", "services", "limits"):
            if key not in node:
                errors.append(f"{prefix}: campo obrigatorio ausente: {key}")

        node_id = node.get("id")
        if node_id in seen:
            errors.append(f"{prefix}: id duplicado: {node_id}")
        if node_id:
            seen.add(str(node_id))

        if node.get("status") not in {"active", "target", "future", "disabled"}:
            errors.append(f"{prefix}: status invalido: {node.get('status')}")

        if not isinstance(node.get("capabilities"), list):
            errors.append(f"{prefix}: capabilities deve ser lista")

        if not isinstance(node.get("services"), list):
            errors.append(f"{prefix}: services deve ser lista")
        else:
            for sidx, service in enumerate(node["services"]):
                sprefix = f"{prefix}.services[{sidx}]"
                for key in ("name", "protocol", "endpoint", "health", "data_classes"):
                    if key not in service:
                        errors.append(f"{sprefix}: campo obrigatorio ausente: {key}")

    return errors


def eligible_nodes(registry: dict[str, Any], capability: str, include_future: bool = False) -> list[dict[str, Any]]:
    wanted = capability.strip().lower()
    allowed_status = {"active", "target"} | ({"future"} if include_future else set())
    nodes = []
    for node in registry.get("nodes", []):
        caps = {str(cap).lower() for cap in node.get("capabilities", [])}
        if wanted in caps and node.get("status") in allowed_status:
            nodes.append(node)
    return sorted(nodes, key=lambda node: int(node.get("priority", 0)), reverse=True)


def route(registry: dict[str, Any], capability: str, include_future: bool = False) -> dict[str, Any]:
    nodes = eligible_nodes(registry, capability, include_future=include_future)
    if not nodes:
        return {
            "ok": False,
            "capability": capability,
            "reason": "nenhum no ativo/target oferece esta capacidade",
            "fallback": "registrar no, ativar servico ou usar execucao humana/manual",
        }

    node = nodes[0]
    return {
        "ok": True,
        "capability": capability,
        "node": node["id"],
        "role": node["role"],
        "status": node["status"],
        "host": node["host"],
        "priority": node.get("priority", 0),
        "services": [service["name"] for service in node.get("services", [])],
    }


def list_nodes(registry: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "id": node["id"],
            "role": node["role"],
            "status": node["status"],
            "host": node["host"],
            "capabilities": node.get("capabilities", []),
        }
        for node in registry.get("nodes", [])
    ]


def list_services(registry: dict[str, Any]) -> list[dict[str, Any]]:
    services: list[dict[str, Any]] = []
    for node in registry.get("nodes", []):
        for service in node.get("services", []):
            services.append(
                {
                    "node": node["id"],
                    "service": service["name"],
                    "protocol": service["protocol"],
                    "endpoint": service["endpoint"],
                    "health": service["health"],
                    "data_classes": service["data_classes"],
                }
            )
    return services


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida e consulta o registro de nos do MEGATRON.")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY, help="Caminho do JSON de nos.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate", help="Valida estrutura minima do registro.")
    sub.add_parser("list", help="Lista nos.")
    sub.add_parser("services", help="Lista servicos.")
    route_parser = sub.add_parser("route", help="Escolhe no por capacidade.")
    route_parser.add_argument("--capability", required=True)
    route_parser.add_argument("--include-future", action="store_true", help="Inclui nos futuros no roteamento.")

    args = parser.parse_args()
    registry = load_registry(args.registry)

    if args.command == "validate":
        errors = validate_registry(registry)
        print(json.dumps({"ok": not errors, "errors": errors}, ensure_ascii=False, indent=2))
        return 0 if not errors else 1
    if args.command == "list":
        print(json.dumps(list_nodes(registry), ensure_ascii=False, indent=2))
        return 0
    if args.command == "services":
        print(json.dumps(list_services(registry), ensure_ascii=False, indent=2))
        return 0
    if args.command == "route":
        print(json.dumps(route(registry, args.capability, include_future=args.include_future), ensure_ascii=False, indent=2))
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
