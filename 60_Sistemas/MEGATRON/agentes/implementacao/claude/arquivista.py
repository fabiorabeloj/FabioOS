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

from _common import vault_root, log_event, resultado

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


def _montar_nota(titulo: str, texto: str, dominio: str, hoje: str) -> str:
    return f"""---
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

# {titulo}

> Classificação provisória: **{dominio}**. Revisar e promover (fonte/40_Wiki/_compat_wiki/tarefa) conforme o Protocolo Operacional.

## Conteúdo bruto

{texto}

## Próximas ações
- [ ] Revisar classificação de domínio
- [ ] Decidir destino final (fonte, wiki, tarefa, decisão ou arquivo)
"""


def run(titulo: str, texto: str, dominio: str = None, dest: str = "00_Inbox",
        dry_run: bool = True) -> dict:
    """Contrato uniforme do agente (ver Ordens de Coordenação).

    dry_run=True (padrão): NÃO escreve — devolve a proposta da nota para aprovação.
    dry_run=False: cria o rascunho (escrita segura), sem sobrescrever.
    Sempre devolve um `Resultado`.
    """
    dom = dominio or classificar(texto, titulo)
    hoje = date.today().isoformat()
    dest_dir = ROOT / dest
    if not dentro_do_vault(dest_dir):
        log_event("Arquivista", "abortado", "destino fora do vault")
        return resultado("proposta", False, "Destino recusado",
                         "`--dest` deve permanecer dentro da raiz do vault FabioOS.")
    destino = dest_dir / f"{hoje}_{slug(titulo)}.md"
    rel = destino.relative_to(ROOT).as_posix()
    nota = _montar_nota(titulo, texto, dom, hoje)

    if dry_run:
        return resultado(
            "proposta", True, f"Proposta de nota: {titulo}",
            corpo=f"Criaria `{rel}` (domínio **{dom}**). Prévia:\n\n{nota}",
            sugestao="Para criar de fato, confirme (--confirmar).", artefato=None)

    if destino.exists():
        log_event("Arquivista", "abortado", "destino ja existe")
        return resultado("proposta", False, "Já existe",
                         f"`{rel}` já existe — não sobrescrevo.")
    dest_dir.mkdir(parents=True, exist_ok=True)
    destino.write_text(nota, encoding="utf-8")
    log_event("Arquivista", "nota_criada", f"{rel} dominio={dom}")
    return resultado("proposta", True, f"Nota criada: {titulo}",
                     corpo=f"Rascunho criado em `{rel}` (domínio **{dom}**).",
                     sugestao="Revisar classificação e promover.", artefato=rel)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--titulo", required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--texto")
    g.add_argument("--arquivo")
    ap.add_argument("--dominio", help="força o domínio (senão classifica)")
    ap.add_argument("--dest", help="pasta destino relativa ao vault (padrão 00_Inbox)")
    ap.add_argument("--confirmar", action="store_true",
                    help="cria de fato (sem isto, roda em dry-run e só propõe)")
    args = ap.parse_args()

    texto = args.texto if args.texto else Path(args.arquivo).read_text(encoding="utf-8")
    r = run(args.titulo, texto, dominio=args.dominio,
            dest=args.dest or "00_Inbox", dry_run=not args.confirmar)

    print(f"{'✅' if r['ok'] else '🛑'} {r['titulo']}")
    print(r["corpo"])
    if r["sugestao"]:
        print(f"💡 {r['sugestao']}")
    return 0 if r["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
