#!/usr/bin/env python3
"""Gera inventario local de ferramentas de IA do FabioOS.

Le apenas o ambiente local. Nao revela valores de variaveis, nao instala nada,
nao inicia/paralisa servicos e nao chama APIs externas.
"""
from __future__ import annotations

import argparse
import csv
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


def vault_root() -> Path:
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "CLAUDE.md").exists():
            return parent
    raise RuntimeError("Nao encontrei CLAUDE.md acima do script.")


ROOT = vault_root()
DEFAULT_OUTPUT = ROOT / "60_Sistemas" / "FabioOS" / "Inventario_Ferramentas_IA_Local_2026-06-28.md"


COMMANDS = [
    "openclaw",
    "cursor",
    "cursor.cmd",
    "hermes",
    "hermes-agent",
    "n8n",
    "node",
    "python",
    "uv",
    "git",
    "claude",
]

ENV_VARS = [
    "OPENROUTER_API_KEY",
    "OPENAI_API_KEY",
    "ANTHROPIC_API_KEY",
    "GEMINI_API_KEY",
    "GOOGLE_API_KEY",
    "OPENCLAW_GATEWAY_TOKEN",
]

PROCESS_KEYWORDS = [
    "openclaw",
    "cursor",
    "hermes",
    "n8n",
    "node",
    "claude",
    "python",
]

PORTS = [18789, 5678, 8787, 3000, 5173, 8000, 8080]


def run(args: list[str], timeout: int = 15) -> str:
    try:
        result = subprocess.run(
            args,
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            timeout=timeout,
            check=False,
        )
        return result.stdout.strip()
    except Exception as exc:
        return f"erro: {exc}"


def command_table() -> list[tuple[str, str]]:
    rows = []
    for cmd in COMMANDS:
        rows.append((cmd, shutil.which(cmd) or "nao encontrado no PATH"))
    return rows


def env_table() -> list[tuple[str, str]]:
    rows = []
    for name in ENV_VARS:
        rows.append((name, "configurado" if os.environ.get(name) else "ausente"))
    return rows


def known_paths() -> list[tuple[str, str]]:
    local = Path(os.environ.get("LOCALAPPDATA", ""))
    profile = Path(os.environ.get("USERPROFILE", ""))
    paths = {
        "OpenClaw Tray local": local / "OpenClawTray",
        "OpenClaw usuario": profile / ".openclaw",
        "Cursor Local Programs": local / "Programs" / "Cursor",
        "Cursor AppData": local / "Cursor",
        "Hermes AppData": local / "Hermes",
        "n8n FabioOS": ROOT / "60_Sistemas" / "n8n",
        "OpenClaw FabioOS": ROOT / "60_Sistemas" / "OpenClaw",
        "MCP FabioOS": ROOT / "60_Sistemas" / "MCP_FabioOS",
    }
    return [(name, "existe" if path.exists() else "nao encontrado") for name, path in paths.items()]


def process_rows() -> list[tuple[str, str, str]]:
    output = run(["tasklist", "/fo", "csv", "/nh"], timeout=20)
    rows: list[tuple[str, str, str]] = []
    if not output or output.startswith("erro:"):
        return rows
    for item in csv.reader(output.splitlines()):
        if len(item) < 2:
            continue
        image, pid = item[0], item[1]
        lower = image.lower()
        if any(key in lower for key in PROCESS_KEYWORDS):
            rows.append((image, pid, "rodando"))
    return rows


def port_rows() -> list[tuple[str, str, str]]:
    rows = []
    for port in PORTS:
        command = [
            "powershell",
            "-NoProfile",
            "-Command",
            f"Get-NetTCPConnection -State Listen -LocalPort {port} -ErrorAction SilentlyContinue | Select-Object -First 1 -ExpandProperty OwningProcess",
        ]
        out = run(command, timeout=8).strip()
        rows.append((str(port), "ouvindo" if out else "livre/nao detectado", out or "-"))
    return rows


def role_matrix() -> list[tuple[str, str, str]]:
    return [
        ("Claude", "lider estrutural", "arquitetura, revisao, commits tematicos e governanca"),
        ("Codex", "executor/engenheiro", "implementacao local, testes, scripts, conectores e handoffs"),
        ("Cursor", "IDE aumentada", "edicao visual, refactors, navegacao de codigo e pair programming"),
        ("Hermes", "pendente de confirmacao", "avaliar como agente local se houver CLI/API utilizavel"),
        ("OpenClaw", "painel/companion", "visualizar agentes e operar workboard quando auth/runtime estiver estavel"),
        ("n8n", "orquestrador de borda", "webhooks, WhatsApp, email, Drive e automacoes com aprovacao"),
        ("OpenRouter", "broker de modelos", "usar com teto de custo e por tarefas especificas, nunca por padrao"),
        ("RAG FabioOS", "memoria semantica", "consulta com fontes; ingestao apenas apos triagem"),
        ("Grafo FabioOS", "mapa relacional", "relacionar notas, fases, agentes e projetos"),
    ]


def table(headers: list[str], rows: list[tuple[str, ...]]) -> str:
    if not rows:
        rows = [tuple("-" for _ in headers)]
    header = "| " + " | ".join(headers) + " |"
    sep = "| " + " | ".join("---" for _ in headers) + " |"
    body = "\n".join("| " + " | ".join(str(cell).replace("\n", " ") for cell in row) + " |" for row in rows)
    return "\n".join([header, sep, body])


def render() -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""---
tipo: inventario
area: 60_Sistemas
projeto: FabioOS
status: gerado
classe_dado: Interno
gerado_por: inventario_ferramentas_ia.py
atualizado_em: {now}
tags: [fabios, ia, ferramentas, cursor, hermes, openclaw, n8n, openrouter]
---

# Inventario Local de Ferramentas IA - FabioOS

> Este arquivo nao exibe valores de tokens. Ele mostra apenas presenca/ausencia e estado operacional local.

## Comandos no PATH

{table(["Comando", "Estado"], command_table())}

## Variaveis de ambiente

{table(["Variavel", "Estado"], env_table())}

## Diretorios conhecidos

{table(["Item", "Estado"], known_paths())}

## Processos detectados

{table(["Processo", "PID", "Estado"], process_rows())}

## Portas relevantes

{table(["Porta", "Estado", "PID"], port_rows())}

## Papeis recomendados

{table(["Ferramenta", "Papel", "Uso no FabioOS"], role_matrix())}

## Leitura operacional

- Se `OpenClaw` estiver rodando mas `openclaw` nao estiver no PATH, o Companion existe, mas a automacao por CLI precisa de ajuste de ambiente.
- Se `n8n` nao estiver no PATH e a porta `5678` estiver livre, ha workflows versionados, mas nao ha servico n8n local ativo.
- Se `OPENROUTER_API_KEY` estiver ausente, nao ha base segura para chamadas pagas via OpenRouter nesta sessao.
- Cursor pode ser usado como IDE humana/visual, mesmo sem CLI detectada, se o aplicativo estiver instalado fora do PATH.
- Hermes precisa de confirmacao de caminho/CLI antes de virar agente operacional.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera inventario local de ferramentas IA do FabioOS.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="arquivo Markdown de saida")
    args = parser.parse_args()
    out = Path(args.output)
    if not out.is_absolute():
        out = ROOT / out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(), encoding="utf-8")
    print(f"Inventario gerado: {out.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
