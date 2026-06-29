#!/usr/bin/env python3
"""Classifica dominio, sensibilidade e permissoes de um arquivo do FabioOS.

Le apenas arquivo local. Nao chama APIs, nao envia dados, nao altera RAG/Grafo.
Serve como gate antes de ingestao, RAG, Grafo, MCP, automacao ou envio externo.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass


@dataclass(frozen=True)
class DomainRule:
    domain: str
    patterns: tuple[str, ...]
    description: str


@dataclass(frozen=True)
class SensitivityRule:
    level: str
    priority: int
    patterns: tuple[str, ...]
    reason: str


DOMAIN_RULES: tuple[DomainRule, ...] = (
    DomainRule("PietraOS / EscolaOS", ("pietra", "colegio", "colégio", "aluno", "aluna", "turma", "prova", "gabarito", "bimestre", "geografia", "filosofia", "comunicado escolar"), "Dominio institucional/docente"),
    DomainRule("TraderOS", ("trader", "trading", "trade", "winrate", "setup", "stop loss", "stop gain", "bingx", "operacao", "operação", "contrato", "entrada", "alavancagem"), "Dominio de trading e desempenho financeiro"),
    DomainRule("PrimusOS", ("primus", "d&d", "dnd", "rpg", "campanha", "npc", "lore", "forgotten realms", "greyhawk", "dragonlance", "eberron", "homebrew"), "Dominio narrativo/criativo"),
    DomainRule("IAOS", ("mcp", "rag", "agente", "agents", "n8n", "openclaw", "openrouter", "cursor", "codex", "claude", "python", "docker", "supabase", "dashboard", "context engineering", "spec-driven"), "Dominio tecnico de IA e automacao"),
    DomainRule("ProductOS", ("produto", "saas", "usuario", "usuário", "pagamento", "stripe", "resend", "posthog", "analytics", "roadmap", "backlog", "sprint", "cliente"), "Dominio futuro de produto/negocio"),
    DomainRule("FabioOS", ("fabioos", "megatron", "obsidian", "github", "vault", "changelog", "decisao", "decisão", "rotina", "sistema operacional"), "Plataforma base e dominio pessoal/operacional"),
)


# Literais de deteccao, nao valores de credenciais.
SENSITIVITY_RULES: tuple[SensitivityRule, ...] = (
    SensitivityRule("Critico", 5, ("api_key", "apikey", "api-key", "token", "password", "senha", "authorization", "bearer", "sk-", "ghp_", "gho_", "ghu_", "private key", "secret"), "Possivel credencial, chave ou segredo"),
    SensitivityRule("Restrito", 4, ("aluno", "aluna", "nota", "boletim", "responsavel", "responsável", "cpf", "rg", "prontuario", "prontuário", "diagnostico", "diagnóstico", "laudo", "gmail profissional"), "Dados de terceiros, estudantes, saude ou identidade"),
    SensitivityRule("Privado", 3, ("diario", "diário", "financas", "finanças", "patrimonio", "patrimônio", "trading", "corretora", "bingx", "saude", "saúde", "familia", "família", "pessoal"), "Dados pessoais, financeiros ou estrategicos"),
    SensitivityRule("Interno", 2, ("arquitetura", "roadmap", "changelog", "script", "dashboard", "mcp", "rag", "grafo", "n8n", "protocolo"), "Operacao interna sem indicio forte de dado sensivel"),
)


DEFAULT_OUTPUT_DIR = Path("60_Sistemas") / "FabioOS" / "classificacoes"


def vault_root() -> Path:
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "CLAUDE.md").exists():
            return parent
    raise RuntimeError("Nao encontrei CLAUDE.md acima do script.")


ROOT = vault_root()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def source_label(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.name


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:80] or "classificacao"


def count_matches(text: str, patterns: tuple[str, ...]) -> int:
    lower = text.lower()
    return sum(lower.count(pattern.lower()) for pattern in patterns)


def detect_domains(text: str) -> list[tuple[DomainRule, int]]:
    matches = [(rule, count_matches(text, rule.patterns)) for rule in DOMAIN_RULES]
    return sorted([item for item in matches if item[1] > 0], key=lambda item: item[1], reverse=True)


def detect_sensitivity(text: str) -> tuple[str, list[tuple[SensitivityRule, int]]]:
    matches = [(rule, count_matches(text, rule.patterns)) for rule in SENSITIVITY_RULES]
    found = sorted([item for item in matches if item[1] > 0], key=lambda item: (item[0].priority, item[1]), reverse=True)
    if not found:
        return "Publico", []
    return found[0][0].level, found


def policies(level: str) -> tuple[str, str, str, str]:
    if level == "Critico":
        return ("Proibido", "Proibido", "Proibido", "Remover do vault se contiver credencial real; mover para variavel local/cofre.")
    if level == "Restrito":
        return ("Somente resumo anonimizado", "Somente entidades anonimizadas", "Proibido sem autorizacao explicita", "Revisao humana obrigatoria antes de qualquer ingestao ou automacao.")
    if level == "Privado":
        return ("Permitido apos revisao", "Permitido com resumo/escopo", "Evitar bruto; preferir resumo minimo", "Revisar antes de RAG/Grafo e nao enviar a modelo externo sem necessidade.")
    if level == "Interno":
        return ("Permitido", "Permitido", "Permitido com criterio", "Pode entrar no fluxo normal se nao houver dados pessoais.")
    return ("Permitido", "Permitido", "Permitido", "Baixo risco; manter fonte e contexto.")


def render(title: str, source: Path, text: str) -> str:
    now = datetime.now().strftime("%Y-%m-%d")
    domains = detect_domains(text)
    primary_domain = domains[0][0].domain if domains else "FabioOS"
    level, sensitivity_matches = detect_sensitivity(text)
    rag, graph, external_model, decision = policies(level)

    domain_rows = domains or [(DomainRule("FabioOS", (), "Padrao quando nenhum dominio especifico e detectado"), 0)]
    sensitivity_rows = sensitivity_matches or []

    def table(rows: list[tuple[str, str, str]], headers: tuple[str, str, str]) -> str:
        out = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
        out.extend("| " + " | ".join(row) + " |" for row in rows)
        return "\n".join(out)

    domain_table = table(
        [(rule.domain, str(score), rule.description) for rule, score in domain_rows],
        ("Dominio", "Sinais", "Descricao"),
    )
    sensitivity_table = table(
        [(rule.level, str(score), rule.reason) for rule, score in sensitivity_rows] or [(level, "0", "Nenhum sinal restritivo detectado")],
        ("Classe", "Sinais", "Motivo"),
    )

    return f"""---
tipo: classificacao-dado
area: 60_Sistemas
projeto: FabioOS
status: gerado
gerado_por: classificar_dado_fabioos.py
fonte_original: {source_label(source)}
dominio: {primary_domain}
classe_dado: {level}
criado_em: {now}
atualizado_em: {now}
tags: [fabios, classificacao, dominios, permissoes, privacidade]
---

# Classificacao de dado - {title}

> Gerado por `60_Sistemas/FabioOS/scripts/classificar_dado_fabioos.py`.
> Leitura local, sem API, sem envio de dados e sem alteracao de RAG/Grafo.

## Resultado

| Campo | Valor |
|---|---|
| Dominio provavel | {primary_domain} |
| Classe de dado | {level} |
| Permissao RAG | {rag} |
| Permissao Grafo | {graph} |
| Modelo externo/API | {external_model} |

## Dominios detectados

{domain_table}

## Sensibilidade detectada

{sensitivity_table}

## Decisao recomendada

{decision}

## Politica aplicada

- Se a classificacao parecer duvidosa, usar a classe mais restritiva.
- Conteudo restrito nao deve ir bruto para RAG/Grafo.
- Conteudo critico nao deve entrar no vault.
- Acoes externas exigem aprovacao humana registrada.

## Fonte

- Arquivo analisado: `{source_label(source)}`
- Tamanho aproximado: {len(text.split())} palavras
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Classifica dominio e permissoes de um arquivo do FabioOS.")
    parser.add_argument("input", help="arquivo local a classificar")
    parser.add_argument("--title", default="", help="titulo da classificacao")
    parser.add_argument("--output", default="", help="arquivo Markdown de saida")
    args = parser.parse_args()

    src = Path(args.input)
    if not src.is_absolute():
        src = ROOT / src
    text = read_text(src)
    title = args.title or src.stem.replace("-", " ").replace("_", " ").title()

    if args.output:
        out = Path(args.output)
        if not out.is_absolute():
            out = ROOT / out
    else:
        out = ROOT / DEFAULT_OUTPUT_DIR / f"{datetime.now().strftime('%Y-%m-%d')}_{slugify(title)}.md"

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(title, src, text), encoding="utf-8")
    print(f"Classificacao gerada: {source_label(out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
