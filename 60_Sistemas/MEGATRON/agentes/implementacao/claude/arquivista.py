#!/usr/bin/env python3
"""
Agente Arquivista (agent.arquivista) — implementação mínima.

Conforme specs/Agente_Arquivista.md. Recebe texto bruto, classifica o domínio,
gera nota Markdown com frontmatter e salva em 00_Inbox/ (escrita segura), com log.
Não apaga nada, não commita, não inventa conteúdo.

Uso:
    python arquivista.py --titulo "Ideia X" --texto "conteúdo..."
    python arquivista.py --titulo "Aula" --arquivo entrada.txt
    python arquivista.py --titulo "Y" --texto "..." --dominio PietraOS
"""
import argparse
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

from _common import vault_root, log_event

ROOT = vault_root()

DOMINIOS = {
    "PietraOS": ["pietra", "aluno", "matrícula", "matricula", "secretaria",
                 "coordenação", "responsável", "mensalidade", "colégio", "colegio"],
    "Escola": ["prova", "revisão", "revisao", "gabarito", "geografia", "filosofia",
               "bimestre", "turma", "aula", "comunicado"],
    "PrimusOS": ["primus", "rpg", "personagem", "missão", "missao", "facção",
                 "faccao", "lore", "campanha", "mundo", "npc"],
}


def classificar(texto: str, titulo: str) -> str:
    base = f"{titulo}\n{texto}".lower()
    placar = {d: sum(base.count(k) for k in kws) for d, kws in DOMINIOS.items()}
    melhor = max(placar, key=placar.get)
    return melhor if placar[melhor] > 0 else "FabioOS"


def slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:60] or "nota"


def dentro_do_vault(path: Path) -> bool:
    """Retorna True apenas se o caminho resolvido permanecer dentro do vault."""
    try:
        path.resolve().relative_to(ROOT.resolve())
        return True
    except ValueError:
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--titulo", required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--texto")
    g.add_argument("--arquivo")
    ap.add_argument("--dominio", help="força o domínio (senão classifica)")
    ap.add_argument("--dest", help="pasta destino relativa ao vault (padrão 00_Inbox)")
    args = ap.parse_args()

    texto = args.texto if args.texto else Path(args.arquivo).read_text(encoding="utf-8")
    dominio = args.dominio or classificar(texto, args.titulo)

    hoje = date.today().isoformat()
    dest_dir = ROOT / (args.dest or "00_Inbox")
    if not dentro_do_vault(dest_dir):
        print("🛑 Destino recusado: --dest deve permanecer dentro da raiz do vault FabioOS.")
        log_event("Arquivista", "abortado", "destino fora do vault")
        return 2
    dest_dir.mkdir(parents=True, exist_ok=True)
    destino = dest_dir / f"{hoje}_{slug(args.titulo)}.md"
    if destino.exists():
        print(f"⚠️  Já existe: {destino.relative_to(ROOT).as_posix()} — não sobrescrevo.")
        log_event("Arquivista", "abortado", "destino ja existe")
        return 1

    nota = f"""---
tipo: nota
area: 00_Inbox
projeto: FabioOS
dominio: {dominio}
status: rascunho
origem: arquivista
tags: [inbox, {dominio.lower()}, rascunho]
criado_em: {hoje}
atualizado_em: {hoje}
---

# {args.titulo}

> Classificação provisória: **{dominio}**. Revisar e promover (fonte/40_Wiki/_compat_wiki/tarefa) conforme o Protocolo Operacional.

## Conteúdo bruto

{texto}

## Próximas ações
- [ ] Revisar classificação de domínio
- [ ] Decidir destino final (fonte, wiki, tarefa, decisão ou arquivo)
"""
    destino.write_text(nota, encoding="utf-8")
    rel = destino.relative_to(ROOT).as_posix()
    print(f"✅ Nota criada: {rel}")
    print(f"   Domínio classificado: {dominio}")
    log_event("Arquivista", "nota_criada", f"{rel} dominio={dominio}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
