#!/usr/bin/env python3
"""
Agente Dashboard (agent.dashboard) — implementação mínima.

Conforme specs/Agente_Dashboard.md. Lê o Registro de Agentes, o Painel de
Pendências, o último changelog e o log dos agentes, e gera um Markdown de status:
STATUS_Agentes.md. Leitura + escrita segura de painel. Não expõe segredos.

Uso:
    python dashboard.py
"""
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from _common import vault_root, agentes_dir, log_path, log_event

ROOT = vault_root()
AG = agentes_dir()
PAINEL = ROOT / "10_Mapas" / "Painel_Pendencias_FabioOS.md"
CHANGELOG_DIR = ROOT / "50_Registros" / "Changelog"
AGENTES = ["SafeCommit", "Arquivista", "Inbox", "RAG", "Dashboard"]


def ultima_execucao():
    """Mapeia agente -> (timestamp, ação) a partir do log."""
    out = {}
    lp = log_path()
    if lp.exists():
        for line in lp.read_text(encoding="utf-8").splitlines():
            cols = [c.strip() for c in line.split("|")]
            if len(cols) >= 5 and cols[1] and cols[2] in AGENTES:
                out[cols[2]] = (cols[1], cols[3])
    return out


def pendencias_abertas():
    if not PAINEL.exists():
        return 0, []
    linhas = [l.strip() for l in PAINEL.read_text(encoding="utf-8").splitlines()
              if l.strip().startswith("- [ ]")]
    return len(linhas), linhas[:5]


def ultimo_changelog():
    if not CHANGELOG_DIR.exists():
        return "—"
    arquivos = list(CHANGELOG_DIR.glob("*.md"))
    if not arquivos:
        return "—"
    return max(arquivos, key=lambda f: f.stat().st_mtime).stem


def git_pendente():
    out = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT,
                         capture_output=True, text=True).stdout
    return len([l for l in out.splitlines() if l.strip()])


def main():
    execs = ultima_execucao()
    n_pend, amostra = pendencias_abertas()
    chlog = ultimo_changelog()
    n_git = git_pendente()
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    linhas = [f"| {a} | {execs.get(a, ('—','nunca executado'))[0]} | "
              f"{execs.get(a, ('—','nunca executado'))[1]} |" for a in AGENTES]
    tabela = "\n".join(linhas)
    amostra_md = "\n".join(f"- {p[6:]}" for p in amostra) or "- (nenhuma)"

    conteudo = f"""---
tipo: painel
area: 60_Sistemas
projeto: FabioOS
sistema: MEGATRON
status: gerado
gerado_por: agent.dashboard
atualizado_em: {agora}
---

# STATUS dos Agentes MEGATRON

> Gerado automaticamente pelo agente Dashboard em {agora}. Não editar à mão.

## Agentes

| Agente | Última execução | Ação |
|---|---|---|
{tabela}

## Situação geral

- **Pendências abertas (Painel):** {n_pend}
- **Arquivos com mudança no Git:** {n_git}
- **Último changelog:** `{chlog}`

## Pendências críticas (amostra)

{amostra_md}

## Próxima ação recomendada

- {"Rodar SafeCommit e revisar o commit pendente." if n_git else "Working tree limpo — seguir o roadmap (Fase 12 RAG)."}

## Relações

- [[60_Sistemas/MEGATRON/agentes/Registro_Agentes]]
- [[10_Mapas/Painel_Pendencias_FabioOS]]
"""
    destino = AG / "STATUS_Agentes.md"
    destino.write_text(conteudo, encoding="utf-8")
    print(f"✅ Painel gerado: {destino.relative_to(ROOT).as_posix()}")
    print(f"   Agentes: {len(AGENTES)} | Pendências: {n_pend} | Git: {n_git} | Changelog: {chlog}")
    log_event("Dashboard", "painel_gerado", f"pend={n_pend} git={n_git}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
