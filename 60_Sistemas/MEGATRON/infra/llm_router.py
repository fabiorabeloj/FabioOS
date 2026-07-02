#!/usr/bin/env python3
"""LLM Router v0 do MEGATRON.

Nao chama APIs. Seleciona um alias/modelo a partir de tarefa, classe de dado,
preferencia de custo/qualidade e restricoes de privacidade.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


BASE = Path(__file__).resolve().parent
DEFAULT_REGISTRY = BASE / "model_registry.example.json"
LOCAL_ONLY_CLASSES = {"restricted", "no_rag", "forbidden_external"}
STATUS_DEFAULT = {"active", "target"}
COST_SCORE = {"zero": 40, "electricity": 35, "subscription": 30, "low": 25, "medium": 10, "high": 0}
QUALITY_SCORE = {"deterministic": 20, "medium": 30, "high": 45}


def load_registry(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_registry(registry: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    models = registry.get("models")
    if not isinstance(models, list):
        return ["Campo 'models' deve ser uma lista."]

    seen: set[str] = set()
    for idx, model in enumerate(models):
        prefix = f"models[{idx}]"
        required = (
            "id",
            "alias",
            "provider",
            "model_ref",
            "status",
            "location",
            "execution_mode",
            "priority",
            "cost_tier",
            "quality_tier",
            "capabilities",
            "tasks",
            "data_classes",
        )
        for key in required:
            if key not in model:
                errors.append(f"{prefix}: campo obrigatorio ausente: {key}")
        model_id = model.get("id")
        if model_id in seen:
            errors.append(f"{prefix}: id duplicado: {model_id}")
        if model_id:
            seen.add(str(model_id))
        if model.get("status") not in {"active", "target", "future", "disabled"}:
            errors.append(f"{prefix}: status invalido: {model.get('status')}")
    return errors


def data_allowed(model: dict[str, Any], data_class: str) -> tuple[bool, str]:
    dc = data_class.strip().lower()
    location = str(model.get("location", "")).lower()
    if dc in LOCAL_ONLY_CLASSES and location not in {"local", "local_tool"}:
        return False, f"{dc} exige local/humano; modelo e {location}"
    if dc not in {str(item).lower() for item in model.get("data_classes", [])}:
        return False, f"{dc} nao permitido em {model.get('id')}"
    return True, "ok"


def task_matches(model: dict[str, Any], task: str) -> bool:
    wanted = task.strip().lower()
    tasks = {str(item).lower() for item in model.get("tasks", [])}
    caps = {str(item).lower() for item in model.get("capabilities", [])}
    return wanted in tasks or wanted in caps or any(wanted in item or item in wanted for item in tasks | caps)


def score_model(model: dict[str, Any], quality: str, prefer_local: bool) -> int:
    score = int(model.get("priority", 0))
    status = model.get("status")
    if status == "active":
        score += 15
    elif status == "target":
        score += 5
    if quality == "cheap":
        score += COST_SCORE.get(str(model.get("cost_tier")), 0)
    elif quality == "high":
        score += QUALITY_SCORE.get(str(model.get("quality_tier")), 0)
    else:
        score += COST_SCORE.get(str(model.get("cost_tier")), 0) // 2
        score += QUALITY_SCORE.get(str(model.get("quality_tier")), 0) // 2
    if prefer_local and model.get("location") in {"local", "local_tool"}:
        score += 25
    return score


def route(
    registry: dict[str, Any],
    task: str,
    data_class: str,
    quality: str = "balanced",
    prefer_local: bool = False,
    include_future: bool = False,
) -> dict[str, Any]:
    allowed_status = STATUS_DEFAULT | ({"future"} if include_future else set())
    rejected: list[dict[str, str]] = []
    candidates: list[tuple[int, dict[str, Any]]] = []

    for model in registry.get("models", []):
        if model.get("status") not in allowed_status:
            continue
        if not task_matches(model, task):
            continue
        ok, reason = data_allowed(model, data_class)
        if not ok:
            rejected.append({"model": str(model.get("id")), "reason": reason})
            continue
        candidates.append((score_model(model, quality, prefer_local), model))

    if not candidates:
        return {
            "ok": False,
            "task": task,
            "data_class": data_class,
            "reason": "nenhum modelo elegivel",
            "rejected": rejected[:5],
            "fallback": "usar humano, reduzir escopo, ativar modelo local ou registrar novo modelo",
        }

    candidates.sort(key=lambda item: item[0], reverse=True)
    score, model = candidates[0]
    approval_required = data_class in {"private", "restricted", "no_rag", "forbidden_external"} or model.get("location") == "cloud"
    return {
        "ok": True,
        "task": task,
        "data_class": data_class,
        "selected": {
            "id": model["id"],
            "alias": model["alias"],
            "provider": model["provider"],
            "model_ref": model["model_ref"],
            "status": model["status"],
            "location": model["location"],
            "execution_mode": model["execution_mode"],
            "cost_tier": model["cost_tier"],
            "quality_tier": model["quality_tier"],
            "score": score,
        },
        "approval_required": approval_required,
        "notes": [
            "roteamento deterministico; nenhuma API foi chamada",
            "agentes devem chamar alias, nao provedor direto",
        ],
    }


def list_models(registry: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "id": model["id"],
            "alias": model["alias"],
            "provider": model["provider"],
            "status": model["status"],
            "location": model["location"],
            "tasks": model.get("tasks", []),
        }
        for model in registry.get("models", [])
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Roteador deterministico de modelos do MEGATRON.")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate")
    sub.add_parser("list")
    route_parser = sub.add_parser("route")
    route_parser.add_argument("--task", required=True)
    route_parser.add_argument("--data-class", default="internal")
    route_parser.add_argument("--quality", choices=["cheap", "balanced", "high"], default="balanced")
    route_parser.add_argument("--prefer-local", action="store_true")
    route_parser.add_argument("--include-future", action="store_true")

    args = parser.parse_args()
    registry = load_registry(args.registry)
    if args.command == "validate":
        errors = validate_registry(registry)
        print(json.dumps({"ok": not errors, "errors": errors}, ensure_ascii=False, indent=2))
        return 0 if not errors else 1
    if args.command == "list":
        print(json.dumps(list_models(registry), ensure_ascii=False, indent=2))
        return 0
    if args.command == "route":
        result = route(
            registry,
            task=args.task,
            data_class=args.data_class,
            quality=args.quality,
            prefer_local=args.prefer_local,
            include_future=args.include_future,
        )
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result["ok"] else 2
    return 1


if __name__ == "__main__":
    sys.exit(main())
