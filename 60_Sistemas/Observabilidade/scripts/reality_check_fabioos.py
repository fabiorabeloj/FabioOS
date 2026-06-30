from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parents[3]
REPORTS = ROOT / "60_Sistemas" / "Observabilidade" / "reports"

CANONICAL_ROOT = {
    "00_Arquitetura",
    "00_Inbox",
    "05_Raw_Sources",
    "10_Dashboard",
    "20_Areas",
    "30_Projetos",
    "40_Wiki",
    "50_Registros",
    "60_Sistemas",
    "70_Skills",
    "80_Specs",
    "90_Arquivo",
}


def run(cmd: list[str], timeout: int = 10) -> dict:
    try:
        proc = subprocess.run(
            cmd,
            cwd=ROOT,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
        return {
            "ok": proc.returncode == 0,
            "code": proc.returncode,
            "stdout": proc.stdout.strip(),
            "stderr": proc.stderr.strip(),
            "timeout": False,
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "ok": False,
            "code": None,
            "stdout": (exc.stdout or "").strip() if isinstance(exc.stdout, str) else "",
            "stderr": "timeout",
            "timeout": True,
        }


def sha256(path: Path) -> str | None:
    if not path.exists() or not path.is_file():
        return None
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_state() -> dict:
    branch = run(["git", "status", "--short", "--branch"])
    lines = branch["stdout"].splitlines()
    header = lines[0] if lines else ""
    ahead_match = re.search(r"\[ahead (\d+)\]", header)
    ahead = int(ahead_match.group(1)) if ahead_match else 0
    dirty = [line for line in lines[1:] if line.strip()]
    modified = [line for line in dirty if not line.startswith("??")]
    untracked = [line for line in dirty if line.startswith("??")]
    latest = run(["git", "log", "-5", "--oneline"])
    return {
        "header": header,
        "ahead": ahead,
        "dirty_count": len(dirty),
        "modified_count": len(modified),
        "untracked_count": len(untracked),
        "dirty_sample": dirty[:40],
        "latest_commits": latest["stdout"].splitlines(),
    }


def root_state() -> dict:
    items = []
    unexpected = []
    visible_unexpected = []
    technical_root = []
    for p in sorted(ROOT.iterdir(), key=lambda x: (x.is_file(), x.name.lower())):
        if p.name == ".git":
            continue
        info = {
            "name": p.name,
            "kind": "dir" if p.is_dir() else "file",
            "size": p.stat().st_size if p.is_file() else None,
        }
        items.append(info)
        if p.name not in CANONICAL_ROOT:
            unexpected.append(info)
            if p.name.startswith("."):
                technical_root.append(info)
            else:
                visible_unexpected.append(info)
    return {
        "items": items,
        "unexpected": unexpected,
        "visible_unexpected": visible_unexpected,
        "technical_root": technical_root,
    }


def docker_state() -> dict:
    ps = run(
        [
            "docker",
            "ps",
            "-a",
            "--format",
            "{{.Names}}|{{.Image}}|{{.Status}}|{{.Ports}}",
        ],
        timeout=10,
    )
    containers = []
    for line in ps["stdout"].splitlines():
        parts = line.split("|", 3)
        if len(parts) != 4:
            continue
        name, image, status, ports = parts
        public_bind = "0.0.0.0:" in ports or "[::]:" in ports
        containers.append(
            {
                "name": name,
                "image": image,
                "status": status,
                "ports": ports,
                "public_bind": public_bind,
            }
        )
    return {"available": ps["ok"], "containers": containers, "error": ps["stderr"]}


def n8n_state() -> dict:
    http_ok = False
    http_status = None
    try:
        with urlopen("http://127.0.0.1:5678/", timeout=5) as resp:
            http_status = resp.status
            http_ok = 200 <= resp.status < 400
    except Exception as exc:  # noqa: BLE001
        http_status = type(exc).__name__

    workflows = run(["docker", "exec", "n8n", "n8n", "list:workflow"], timeout=25)
    workflow_lines = workflows["stdout"].splitlines() if workflows["stdout"] else []

    mounts_raw = run(["docker", "inspect", "n8n", "--format", "{{json .Mounts}}"], timeout=10)
    vault_mounted = False
    mounts = []
    if mounts_raw["stdout"]:
        try:
            mounts = json.loads(mounts_raw["stdout"])
            vault_mounted = any(m.get("Destination") == "/vault" for m in mounts)
        except json.JSONDecodeError:
            mounts = []

    return {
        "http_ok": http_ok,
        "http_status": http_status,
        "workflow_list_ok": workflows["ok"],
        "workflow_list_timeout": workflows["timeout"],
        "workflow_count": len(workflow_lines),
        "workflows": workflow_lines,
        "vault_mounted": vault_mounted,
        "mounts": [
            {"name": m.get("Name"), "destination": m.get("Destination"), "type": m.get("Type")}
            for m in mounts
        ],
    }


def duplicate_state() -> dict:
    legacy = ROOT / "wiki" / "conceitos" / "rag.md"
    canonical = ROOT / "40_Wiki" / "_compat_wiki" / "conceitos" / "rag.md"
    legacy_hash = sha256(legacy)
    canonical_hash = sha256(canonical)
    return {
        "legacy_exists": legacy.exists(),
        "canonical_exists": canonical.exists(),
        "legacy_path": str(legacy.relative_to(ROOT)) if legacy.exists() else None,
        "canonical_path": str(canonical.relative_to(ROOT)) if canonical.exists() else None,
        "same_hash": bool(legacy_hash and canonical_hash and legacy_hash == canonical_hash),
    }


def blindspots(git: dict, root: dict, docker: dict, n8n: dict, dup: dict) -> list[dict]:
    out: list[dict] = []
    if git["ahead"] >= 20:
        out.append(
            {
                "level": "P1",
                "id": "git_ahead_no_remote_backup",
                "message": f"main esta {git['ahead']} commits a frente do origin/main; ha risco de perda local e PR desatualizado.",
            }
        )
    if git["dirty_count"]:
        out.append(
            {
                "level": "P1",
                "id": "dirty_parallel_worktree",
                "message": f"worktree tem {git['dirty_count']} itens alterados/novos; alta chance de colisao entre agentes.",
            }
        )
    if root["visible_unexpected"]:
        names = ", ".join(item["name"] for item in root["visible_unexpected"][:12])
        out.append(
            {
                "level": "P1",
                "id": "visible_root_drift",
                "message": f"raiz visivel do vault voltou a ter itens fora da taxonomia canonica: {names}.",
            }
        )
    if root["technical_root"]:
        names = ", ".join(item["name"] for item in root["technical_root"][:12])
        out.append(
            {
                "level": "P2",
                "id": "technical_root_sprawl",
                "message": f"raiz contem diretorios/arquivos tecnicos que podem aparecer em algumas ferramentas: {names}.",
            }
        )
    public = [c["name"] for c in docker["containers"] if c["public_bind"]]
    if public:
        out.append(
            {
                "level": "P1",
                "id": "runtime_public_bind",
                "message": f"containers expostos em 0.0.0.0/[::]: {', '.join(public)}.",
            }
        )
    if n8n["http_ok"] and not n8n["vault_mounted"]:
        out.append(
            {
                "level": "P2",
                "id": "n8n_without_vault_mount",
                "message": "n8n esta online, mas o vault nao esta montado em /vault; workflows devem usar REST API ou falharao ao escrever localmente.",
            }
        )
    if dup["legacy_exists"] and dup["same_hash"]:
        out.append(
            {
                "level": "P2",
                "id": "legacy_wiki_recreated",
                "message": "wiki/conceitos/rag.md reapareceu e e duplicata do arquivo canonico; alguma frente ainda escreve no caminho legado.",
            }
        )
    if n8n["workflow_list_timeout"]:
        out.append(
            {
                "level": "P2",
                "id": "n8n_cli_slow",
                "message": "listagem CLI do n8n excedeu timeout; monitorar estabilidade do container.",
            }
        )
    return out


def markdown_report(data: dict) -> str:
    lines = [
        "---",
        "tipo: relatorio-operacional",
        "area: 60_Sistemas",
        "projeto: FabioOS",
        "status: gerado",
        f"gerado_em: {data['generated_at']}",
        "tags: [fabios, observabilidade, reality-check, controle]",
        "---",
        "",
        "# Reality Check FabioOS",
        "",
        "## Resumo executivo",
        "",
    ]
    for item in data["blindspots"]:
        lines.append(f"- **{item['level']} {item['id']}**: {item['message']}")
    if not data["blindspots"]:
        lines.append("- Nenhum ponto cego critico detectado.")

    git = data["git"]
    lines += [
        "",
        "## Git",
        "",
        f"- Estado: `{git['header']}`",
        f"- Commits a frente: `{git['ahead']}`",
        f"- Itens sujos: `{git['dirty_count']}` (`{git['modified_count']}` modificados, `{git['untracked_count']}` novos)",
        "",
        "### Ultimos commits",
        "",
    ]
    lines += [f"- `{commit}`" for commit in git["latest_commits"]]

    lines += [
        "",
        "## Raiz do vault",
        "",
        "Itens fora da taxonomia canonica:",
        "",
    ]
    unexpected = data["root"]["visible_unexpected"]
    if unexpected:
        lines += [f"- `{item['name']}` ({item['kind']})" for item in unexpected]
    else:
        lines.append("- nenhum")

    lines += [
        "",
        "Itens tecnicos na raiz:",
        "",
    ]
    technical = data["root"]["technical_root"]
    if technical:
        lines += [f"- `{item['name']}` ({item['kind']})" for item in technical]
    else:
        lines.append("- nenhum")

    lines += [
        "",
        "## Docker",
        "",
    ]
    for c in data["docker"]["containers"]:
        marker = "PUBLICO" if c["public_bind"] else "local/internal"
        lines.append(f"- `{c['name']}`: {c['status']} | {marker} | `{c['ports']}`")

    n8n = data["n8n"]
    lines += [
        "",
        "## n8n",
        "",
        f"- HTTP local: `{n8n['http_status']}`",
        f"- Workflows listados: `{n8n['workflow_count']}`",
        f"- Vault montado em /vault: `{n8n['vault_mounted']}`",
        "",
    ]
    for wf in n8n["workflows"]:
        lines.append(f"- `{wf}`")

    dup = data["duplicates"]
    lines += [
        "",
        "## Duplicatas legadas",
        "",
        f"- `wiki/conceitos/rag.md` existe: `{dup['legacy_exists']}`",
        f"- Igual ao canonico: `{dup['same_hash']}`",
        "",
        "## Recomendacao de comando",
        "",
        "1. Nao fazer push ainda sem revisao do Claude.",
        "2. Nao apagar `wiki/` ate descobrir qual processo recria o caminho legado.",
        "3. Tratar publicacao de portas Docker como decisao de seguranca, nao detalhe tecnico.",
        "4. Antes da proxima frente grande, congelar/stagear por dono: Claude, Cursor, Codex.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    REPORTS.mkdir(parents=True, exist_ok=True)
    generated_at = datetime.now().isoformat(timespec="seconds")
    git = git_state()
    root = root_state()
    docker = docker_state()
    n8n = n8n_state()
    dup = duplicate_state()
    data = {
        "generated_at": generated_at,
        "git": git,
        "root": root,
        "docker": docker,
        "n8n": n8n,
        "duplicates": dup,
        "blindspots": blindspots(git, root, docker, n8n, dup),
    }
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    json_path = REPORTS / f"reality_check_{stamp}.json"
    md_path = REPORTS / f"Reality_Check_{stamp}.md"
    json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    md_path.write_text(markdown_report(data), encoding="utf-8")
    print(str(md_path.relative_to(ROOT)))
    print(str(json_path.relative_to(ROOT)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
