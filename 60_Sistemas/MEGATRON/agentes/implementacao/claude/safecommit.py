#!/usr/bin/env python3
"""
Agente SafeCommit (agent.safecommit) — implementação mínima.

Conforme specs/Agente_SafeCommit.md. Versão mínima = ADVISOR (não commita,
não faz stage, não faz push). Ele:
  - lista arquivos modificados/novos (git status, exclui gitignored);
  - escaneia possíveis segredos (sem exibir valores);
  - sugere mensagem Conventional Commit;
  - imprime o comando que o humano deve rodar após aprovar.

Uso:
    python safecommit.py
"""
import re
import subprocess
import sys
from pathlib import Path

from _common import vault_root, log_event

ROOT = vault_root()

# Padrões de alto sinal (exigem valor longo → poucos falsos positivos)
SECRET_PATTERNS = [
    (re.compile(r"ghp_[A-Za-z0-9]{30,}"), "github_pat"),
    (re.compile(r"gh[ous]_[A-Za-z0-9]{30,}"), "github_token"),
    (re.compile(r"sk-[A-Za-z0-9]{20,}"), "openai_key"),
    (re.compile(r"(?i)bearer\s+[A-Za-z0-9._\-]{20,}"), "bearer_token"),
    (re.compile(r"AKIA[0-9A-Z]{16}"), "aws_access_key"),
    (re.compile(r"-----BEGIN[A-Z ]+PRIVATE KEY-----"), "private_key"),
    (re.compile(r"(?i)(api[_-]?key|secret|password|senha|token)\s*[:=]\s*[\"'][^\"']{12,}[\"']"),
     "secret_assignment"),
]
SKIP_EXT = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".mp3", ".wav", ".zip",
            ".webp", ".ico", ".woff", ".woff2", ".ttf", ".exe", ".bin"}


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True,
                          text=True, encoding="utf-8").stdout


def changed_files():
    """Arquivos que um `git add -A` commitaria: modificados + novos, RESPEITANDO
    o .gitignore (via git ls-files --exclude-standard). Não inclui ignorados."""
    out = git("ls-files", "--modified", "--others", "--exclude-standard")
    files = []
    seen = set()
    for path in out.splitlines():
        path = path.strip()
        if not path or path in seen:
            continue
        seen.add(path)
        p = ROOT / path
        if p.is_file():
            files.append(p)
    return sorted(files)


def scan_secrets(files):
    findings = []
    for f in files:
        if f.suffix.lower() in SKIP_EXT:
            continue
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            for rx, label in SECRET_PATTERNS:
                if rx.search(line):
                    rel = f.relative_to(ROOT).as_posix()
                    findings.append((rel, i, label))  # valor NUNCA é guardado
                    break
    return findings


def suggest_message(files):
    rels = [f.relative_to(ROOT).as_posix() for f in files]
    only_md = all(r.endswith(".md") for r in rels)
    has_code = any(r.endswith((".py", ".js", ".ts", ".json")) for r in rels)
    if has_code:
        tipo = "feat"
    elif only_md:
        tipo = "docs"
    else:
        tipo = "chore"
    return f"{tipo}: atualização do FabioOS ({len(rels)} arquivo(s)) — revisar e editar"


def main():
    files = changed_files()
    print("=" * 60)
    print("AGENTE SafeCommit — diagnóstico (não commita, não faz push)")
    print("=" * 60)
    if not files:
        print("\nNada a commitar. Working tree limpo.")
        log_event("SafeCommit", "diagnostico", "nada a commitar")
        return 0

    print(f"\n📂 Arquivos a commitar ({len(files)}):")
    for f in files:
        print(f"   - {f.relative_to(ROOT).as_posix()}")

    print("\n🔍 Verificação de segredos:")
    findings = scan_secrets(files)
    if findings:
        print(f"   ⚠️  {len(findings)} possível(is) segredo(s) — REVISAR (valores ocultos):")
        for rel, line, label in findings:
            print(f"      - {rel}:{line}  [{label}]")
        print("\n🛑 Não sugiro commit enquanto houver match não resolvido.")
        print("   Verifique se é segredo real → mova para .env / gitignore.")
        log_event("SafeCommit", "scan", f"{len(findings)} match(es) — bloqueado")
        return 2

    print("   ✅ Nenhum segredo de alto sinal encontrado.")
    msg = suggest_message(files)
    print(f"\n✏️  Mensagem proposta:\n   {msg}")
    print("\n👤 APROVAÇÃO HUMANA NECESSÁRIA. Para commitar (sem push), rode:")
    print(f'   git add -A && git commit -m "{msg}"')
    log_event("SafeCommit", "diagnostico", f"{len(files)} arquivo(s), scan ok, aguarda aprovacao")
    return 0


if __name__ == "__main__":
    sys.exit(main())
