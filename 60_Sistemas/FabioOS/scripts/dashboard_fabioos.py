#!/usr/bin/env python3
"""Gera um dashboard operacional local do FabioOS.

Le apenas arquivos locais e estado Git. Nao chama APIs, nao envia dados,
nao reindexa RAG e nao executa workflows externos.
"""
from __future__ import annotations

import argparse
import json
import re
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
        if (parent / "60_Sistemas/FabioOS/bootstrap/CLAUDE.md").exists():
            return parent
    raise RuntimeError("Nao encontrei 60_Sistemas/FabioOS/bootstrap/CLAUDE.md acima do script.")


ROOT = vault_root()
PAINEL = ROOT / "10_Mapas" / "Painel_Pendencias_FabioOS.md"
NEXT_ACTIONS = ROOT / "60_Sistemas" / "FabioOS" / "NEXT_ACTIONS.md"
REGISTRO_FRENTES = ROOT / "60_Sistemas" / "FabioOS" / "Registro_Frentes_Ativas.md"
CHANGELOG_DIR = ROOT / "50_Registros" / "Changelog"
GRAFO_AUDITORIA = ROOT / "60_Sistemas" / "Grafo" / "data" / "auditoria_grafo.json"
RAG_DB = ROOT / "60_Sistemas" / "RAG" / "fabioos_db"
RAG_PYTHON = ROOT / "60_Sistemas" / "RAG" / ".venv" / "Scripts" / "python.exe"
RADAR_DIR = ROOT / "30_Conhecimento" / "Tecnologia" / "Radar"
CLASSIFICACOES_DIR = ROOT / "60_Sistemas" / "FabioOS" / "classificacoes"
SPECS_DIR = ROOT / "60_Sistemas" / "FabioOS" / "specs"
MOBILE_INBOX_DIR = ROOT / "00_Inbox" / "mobile"
EMAIL_SOURCES_DIR = ROOT / "05_Raw_Sources/_compat_sources" / "email"
DRIVE_SOURCES_DIR = ROOT / "05_Raw_Sources/_compat_sources" / "drive"
IA_TOOLS_INVENTORY = ROOT / "60_Sistemas" / "FabioOS" / "Inventario_Ferramentas_IA_Local_2026-06-28.md"
MCP_CODEX_CONFIG = Path.home() / ".codex" / "config.toml"
OUTPUT = ROOT / "10_Mapas" / "Dashboard_Operacional_FabioOS.md"


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        return ""


def run_git(args: list[str]) -> str:
    try:
        return subprocess.run(
            ["git", *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=20,
            check=False,
        ).stdout.strip()
    except Exception as exc:
        return f"erro: {exc}"


def git_status() -> tuple[str, int, str]:
    branch = run_git(["status", "-sb"]).splitlines()
    branch_line = branch[0] if branch else "desconhecido"
    porcelain = run_git(["status", "--porcelain"]).splitlines()
    head = run_git(["rev-parse", "--short", "HEAD"])
    return branch_line, len([l for l in porcelain if l.strip()]), head


def latest_changelog() -> str:
    if not CHANGELOG_DIR.exists():
        return "nao encontrado"
    arquivos = list(CHANGELOG_DIR.glob("*.md"))
    if not arquivos:
        return "nenhum"
    return max(arquivos, key=lambda p: p.stat().st_mtime).name


def open_tasks(path: Path) -> list[str]:
    tasks = []
    for line in read_text(path).splitlines():
        line = line.strip()
        if line.startswith("- [ ]"):
            tasks.append(re.sub(r"^- \[ \]\s*", "", line))
    return tasks


def active_fronts() -> list[str]:
    fronts = []
    for line in read_text(REGISTRO_FRENTES).splitlines():
        if line.startswith("|") and "em andamento" in line:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) >= 6:
                fronts.append(f"{cols[0]} ({cols[1]}): {cols[3]}")
    return fronts


def rag_status() -> str:
    if not RAG_DB.exists():
        return "ausente"
    try:
        import chromadb
        col = chromadb.PersistentClient(path=str(RAG_DB)).get_collection("fabioos")
        return f"presente, {col.count()} chunks"
    except Exception as exc:
        if RAG_PYTHON.exists():
            code = (
                "import chromadb, sys; "
                "col = chromadb.PersistentClient(path=sys.argv[1]).get_collection('fabioos'); "
                "print(col.count())"
            )
            try:
                result = subprocess.run(
                    [str(RAG_PYTHON), "-c", code, str(RAG_DB)],
                    cwd=ROOT,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    timeout=30,
                    check=False,
                )
                if result.returncode == 0 and result.stdout.strip().isdigit():
                    return f"presente, {result.stdout.strip()} chunks"
            except Exception:
                pass
        return f"presente, contagem indisponivel ({exc.__class__.__name__})"


def grafo_status() -> str:
    if not GRAFO_AUDITORIA.exists():
        return "auditoria ausente"
    try:
        data = json.loads(GRAFO_AUDITORIA.read_text(encoding="utf-8"))
    except Exception as exc:
        return f"auditoria ilegivel ({exc.__class__.__name__})"
    resumo = data.get("resumo", {})
    nodes = data.get("total_nodes") or data.get("nodes") or resumo.get("total_nos") or "?"
    edges = data.get("total_edges") or data.get("edges") or resumo.get("total_arestas") or "?"
    orphans = data.get("orphan_nodes") or data.get("orphans") or resumo.get("arestas_orfas") or 0
    isolated = resumo.get("nos_isolados", "?")
    connected = resumo.get("nos_conectados_percentual", "?")
    return f"{nodes} nos, {edges} arestas, {orphans} arestas orfas, {isolated} nos isolados, {connected}% conectados"


def mcp_fabioos_status() -> str:
    txt = read_text(MCP_CODEX_CONFIG)
    if "[mcp_servers.fabioos]" not in txt:
        return "nao registrado no config global do Codex"
    return "registrado no config global do Codex"


def radar_status() -> str:
    if not RADAR_DIR.exists():
        return "nenhuma analise gerada"
    arquivos = sorted(RADAR_DIR.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not arquivos:
        return "nenhuma analise gerada"
    latest = arquivos[0].name
    return f"{len(arquivos)} analise(s), ultima: {latest}"


def classificacoes_status() -> str:
    if not CLASSIFICACOES_DIR.exists():
        return "nenhuma classificacao gerada"
    arquivos = sorted(CLASSIFICACOES_DIR.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not arquivos:
        return "nenhuma classificacao gerada"
    latest = arquivos[0].name
    return f"{len(arquivos)} classificacao(oes), ultima: {latest}"


def specs_status() -> str:
    if not SPECS_DIR.exists():
        return "nenhuma SPEC gerada"
    arquivos = sorted(SPECS_DIR.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not arquivos:
        return "nenhuma SPEC gerada"
    latest = arquivos[0].name
    return f"{len(arquivos)} SPEC(s), ultima: {latest}"


def mobile_gateway_status() -> str:
    script = ROOT / "60_Sistemas" / "FabioOS" / "scripts" / "mobile_gateway_fabioos.py"
    if not script.exists():
        return "nao implementado"
    if not MOBILE_INBOX_DIR.exists():
        return "implementado, nenhuma captura mobile ainda"
    arquivos = sorted(MOBILE_INBOX_DIR.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not arquivos:
        return "implementado, nenhuma captura mobile ainda"
    return f"implementado, {len(arquivos)} captura(s), ultima: {arquivos[0].name}"


def connector_catalog_status() -> str:
    email_count = len(list(EMAIL_SOURCES_DIR.rglob("*.md"))) if EMAIL_SOURCES_DIR.exists() else 0
    drive_count = len(list(DRIVE_SOURCES_DIR.rglob("*.md"))) if DRIVE_SOURCES_DIR.exists() else 0
    return f"Gmail: {email_count} nota(s) locais; Drive: {drive_count} nota(s) locais"


def ia_tools_status() -> str:
    if not IA_TOOLS_INVENTORY.exists():
        return "inventario ainda nao gerado"
    return f"inventario gerado: {IA_TOOLS_INVENTORY.name}"


def n8n_workflows() -> list[str]:
    base = ROOT / "60_Sistemas" / "n8n" / "Workflows"
    if not base.exists():
        return []
    return sorted(p.name for p in base.glob("*.json"))


def inconsistencias() -> list[str]:
    painel = read_text(PAINEL)
    next_actions = read_text(NEXT_ACTIONS)
    out = []
    if "Fase 12" in painel and "validada 10/10" in painel and "Reexecutar as 10 perguntas" in next_actions:
        out.append("RAG aparece como validado no painel, mas NEXT_ACTIONS ainda pede reexecucao das 10 perguntas.")
    if "Reconciliar nomes" in painel or "Reconciliar nomes" in next_actions:
        out.append("n8n tem pendencia de reconciliar nomes/status de workflows documentados vs ambiente real.")
    return out


def render() -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    branch, dirty_count, head = git_status()
    painel_tasks = open_tasks(PAINEL)
    next_tasks = open_tasks(NEXT_ACTIONS)
    fronts = active_fronts()
    workflows = n8n_workflows()
    inc = inconsistencias()

    def bullets(items: list[str], empty: str = "nenhum") -> str:
        return "\n".join(f"- {item}" for item in items) if items else f"- {empty}"

    return f"""---
tipo: dashboard
area: 10_Mapas
projeto: FabioOS
status: gerado
gerado_por: dashboard_fabioos.py
atualizado_em: {now}
tags: [fabios, dashboard, python, automacao, status]
---

# Dashboard Operacional FabioOS

> Gerado automaticamente por `60_Sistemas/FabioOS/scripts/dashboard_fabioos.py`.
> Fonte local apenas: Git, Markdown do vault, RAG DB, auditoria do Grafo e config Codex sem exibir segredos.

## Estado Git

- Branch/status: `{branch}`
- HEAD local: `{head}`
- Arquivos modificados/untracked: `{dirty_count}`
- Ultimo changelog: `{latest_changelog()}`

## Frentes ativas

{bullets(fronts)}

## Camadas cognitivas

| Camada | Estado |
|---|---|
| RAG local | {rag_status()} |
| Grafo local | {grafo_status()} |
| MCP FabioOS | {mcp_fabioos_status()} |
| Radar Tecnologico | {radar_status()} |
| Classificacao de dominios/dados | {classificacoes_status()} |
| Specs FabioOS | {specs_status()} |
| Mobile Gateway | {mobile_gateway_status()} |
| Catalogos Google | {connector_catalog_status()} |
| Ferramentas IA locais | {ia_tools_status()} |
| Workflows n8n versionados | {len(workflows)} JSON |

## Workflows n8n versionados

{bullets(workflows)}

## Pendencias

- Pendencias abertas no Painel: `{len(painel_tasks)}`
- Pendencias abertas em NEXT_ACTIONS: `{len(next_tasks)}`

### Amostra do Painel

{bullets(painel_tasks[:8])}

### Amostra do NEXT_ACTIONS

{bullets(next_tasks[:8])}

## Inconsistencias detectadas

{bullets(inc, "nenhuma inconsistencia automatica detectada")}

## Proxima acao recomendada

- Resolver primeiro as inconsistencias detectadas antes de ativar automacoes externas.
- Manter Python para auditorias locais e n8n para bordas externas com credencial/aprovacao.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(OUTPUT), help="arquivo Markdown de saida")
    args = parser.parse_args()
    out = Path(args.output)
    if not out.is_absolute():
        out = ROOT / out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(), encoding="utf-8")
    print(f"Dashboard gerado: {out.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
