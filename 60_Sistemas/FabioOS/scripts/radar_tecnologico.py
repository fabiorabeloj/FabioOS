#!/usr/bin/env python3
"""Gera uma analise de Radar Tecnologico a partir de um texto local.

Le apenas arquivo local. Nao chama APIs, nao envia dados e nao altera RAG/Grafo.
O objetivo e transformar prompts, anuncios, prints transcritos ou demos em
conhecimento estruturado para o FabioOS.
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
class Signal:
    term: str
    category: str
    patterns: tuple[str, ...]
    concept: str
    fabioos_use: str
    priority: int


SIGNALS: tuple[Signal, ...] = (
    Signal("Agentes", "Agentes", ("agente", "agents", "multi-agent", "multiagente"), "Multi-Agent Systems / Tool Calling", "MEGATRON + agentes especializados com logs e permissoes", 5),
    Signal("MCP", "Integracao", ("mcp", "model context protocol"), "MCP Gateway / ferramentas padronizadas", "Fases 14-15; porta oficial entre IAs e ferramentas", 5),
    Signal("RAG", "Dados", ("rag", "retrieval", "banco vetorial", "vector"), "Recuperacao semantica com fontes", "Fase 12; memoria consultavel com citacoes", 5),
    Signal("Grafo", "Dados", ("grafo", "neo4j", "knowledge graph"), "Grafos de conhecimento", "Fase 13; relacoes, dependencias e dominios", 4),
    Signal("n8n", "Integracao", ("n8n", "workflow", "webhook"), "Automacao por workflows", "Fases 10-11 e 20; bordas externas e credenciais", 5),
    Signal("Python", "Desenvolvimento", ("python",), "Automacao local / workers", "Scripts locais, validadores, MCPs e dashboards", 5),
    Signal("Docker", "Infraestrutura", ("docker", "container"), "Infraestrutura reprodutivel", "Fase 23.5; servicos controlados e rollback", 4),
    Signal("Linux/VPS", "Infraestrutura", ("linux", "vps", "ssh", "nginx", "systemd"), "Ambiente profissional de servidores", "Fase 23.5; producao controlada", 4),
    Signal("Supabase/PostgreSQL", "Dados", ("supabase", "postgres", "postgresql", "sql"), "Data Platform relacional", "Subfase 20.5; estado, tarefas, custos e metadados", 4),
    Signal("MongoDB", "Dados", ("mongodb", "mongo", "nosql"), "Document store / logs flexiveis", "Candidato futuro para sessoes e memoria operacional", 3),
    Signal("Dashboard", "Observabilidade", ("dashboard", "painel", "metricas", "métricas"), "Observabilidade operacional", "Fase 21/21.5; status, custos, erros e agentes", 5),
    Signal("OpenClaw/WhatsApp", "Canais", ("openclaw", "whatsapp", "companion"), "Canal conversacional externo", "Fase 11; entrada controlada com autorizacao", 3),
    Signal("Google/Gmail/Drive", "Canais", ("gmail", "google drive", "calendar", "gemini", "google"), "Integracao com ecossistema Google", "Fase 20; privacidade por conta e tipo de dado", 4),
    Signal("Cursor", "Desenvolvimento", ("cursor",), "Oficina assistida de software", "Fase 16.5; dashboards, MCP robusto e testes", 3),
    Signal("Claude/Codex", "Desenvolvimento", ("claude", "codex", "claude code"), "Spec -> implementacao -> revisao", "Agentes de arquitetura, execucao e revisao", 5),
    Signal("OpenRouter", "IA", ("openrouter",), "Roteamento de modelos", "Uso com teto de custo, variavel local e dados classificados", 3),
    Signal("Spec-Driven Development", "Desenvolvimento", ("spec-driven", "spec driven", "specification"), "Especificacao antes de codigo", "Metodo transversal antes de software grande", 5),
    Signal("Context Engineering", "IA", ("context engineering", "contexto", "prompt engineering"), "Contexto recuperado > prompt isolado", "RAG/Grafo/MCP alimentando MEGATRON", 5),
    Signal("Vercel/Cloudflare", "Infraestrutura", ("vercel", "cloudflare"), "Deploy e borda", "Fase 23.5; app publico apenas quando houver produto", 3),
    Signal("Produto", "Produto", ("stripe", "resend", "posthog", "analytics", "roadmap", "backlog", "sprint"), "ProductOS / metricas / monetizacao", "Fase 25; quando houver usuarios externos", 3),
    Signal("Hardware local", "Infraestrutura", ("hardware", "gpu", "llm local", "modelo local", "mac studio"), "IA local / privacidade / latencia", "Fase 26; somente apos medir custo e privacidade", 2),
    Signal("Kafka/Kubernetes", "Infraestrutura", ("kafka", "kubernetes", "event streaming"), "Escala avancada / eventos", "Futuro distante; nao adotar antes da escala", 1),
)


DEFAULT_OUTPUT_DIR = Path("30_Conhecimento") / "Tecnologia" / "Radar"


def vault_root() -> Path:
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "60_Sistemas/FabioOS/bootstrap/CLAUDE.md").exists():
            return parent
    raise RuntimeError("Nao encontrei 60_Sistemas/FabioOS/bootstrap/CLAUDE.md acima do script.")


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
    return value[:80] or "radar-tecnologico"


def detect_signals(text: str) -> list[Signal]:
    lower = text.lower()
    found: list[Signal] = []
    for signal in SIGNALS:
        if any(pattern.lower() in lower for pattern in signal.patterns):
            found.append(signal)
    return found


def priority_label(score: int) -> str:
    labels = {
        5: "5/5 - Essencial",
        4: "4/5 - Muito importante",
        3: "3/5 - Importante",
        2: "2/5 - Opcional",
        1: "1/5 - Apenas referencia",
    }
    return labels.get(score, "1/5 - Apenas referencia")


def overall_priority(signals: list[Signal]) -> int:
    if not signals:
        return 1
    top = max(s.priority for s in signals)
    if top >= 5 and len([s for s in signals if s.priority >= 4]) >= 4:
        return 5
    return top


def infer_problem(signals: list[Signal]) -> str:
    categories = {s.category for s in signals}
    if {"Agentes", "Integracao", "Dados"} <= categories:
        return "Integrar agentes, ferramentas e memorias sem perder contexto, fontes, permissoes e rastreabilidade."
    if "Observabilidade" in categories:
        return "Tornar sistemas e agentes visiveis por status, metricas, custos, logs e alertas."
    if "Infraestrutura" in categories:
        return "Preparar uma base reprodutivel e confiavel para servicos permanentes."
    if "Produto" in categories:
        return "Transformar capacidade tecnica em produto com roadmap, metricas, usuarios e operacao."
    return "Identificar arquitetura, padroes e ferramentas potencialmente aplicaveis ao FabioOS."


def architecture_flow(signals: list[Signal]) -> list[str]:
    terms = {s.term for s in signals}
    flow = ["Usuario"]
    if terms & {"Claude/Codex", "Agentes", "Context Engineering"}:
        flow.extend(["MEGATRON / LLM", "Agentes especializados"])
    if terms & {"MCP", "n8n", "OpenClaw/WhatsApp", "Google/Gmail/Drive"}:
        flow.append("MCP / APIs / Webhooks")
    if terms & {"RAG", "Grafo", "Supabase/PostgreSQL", "MongoDB"}:
        flow.append("Camada de dados e memoria")
    if terms & {"Python", "Docker", "Linux/VPS", "Vercel/Cloudflare"}:
        flow.append("Processamento e infraestrutura")
    if terms & {"Dashboard", "Produto"}:
        flow.append("Dashboard / produto / metricas")
    flow.append("Resultado operacional com fonte, log e decisao")
    return flow


def table(rows: list[tuple[str, ...]], headers: tuple[str, ...]) -> str:
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    out.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(out)


def bullets(items: list[str], empty: str) -> str:
    return "\n".join(f"- {item}" for item in items) if items else f"- {empty}"


def render(title: str, source: Path, text: str, signals: list[Signal]) -> str:
    now = datetime.now().strftime("%Y-%m-%d")
    priority = overall_priority(signals)
    categories = sorted({s.category for s in signals})
    concepts = sorted({s.concept for s in signals})
    rows = [(s.term, s.category, s.fabioos_use, priority_label(s.priority)) for s in signals]
    flow = "\n".join(f"  -> {step}" if i else step for i, step in enumerate(architecture_flow(signals)))
    if not rows:
        rows = [("Nenhum sinal conhecido detectado", "-", "avaliacao humana necessaria", "1/5 - Apenas referencia")]

    immediate = [s.fabioos_use for s in signals if s.priority >= 5]
    future = [s.fabioos_use for s in signals if s.priority in (3, 4)]
    reference = [s.fabioos_use for s in signals if s.priority <= 2]

    return f"""---
tipo: radar-tecnologico
area: 30_Conhecimento
projeto: FabioOS
status: gerado
gerado_por: radar_tecnologico.py
fonte_original: {source_label(source)}
criado_em: {now}
atualizado_em: {now}
tags: [radar-tecnologico, arquitetura, fabios, megatron]
---

# Radar Tecnologico - {title}

> Gerado por `60_Sistemas/FabioOS/scripts/radar_tecnologico.py`.
> Leitura local, sem API, sem envio de dados e sem alteracao de RAG/Grafo.

## 1. Problema

{infer_problem(signals)}

## 2. Arquitetura

```text
{flow}
```

## 3. Tecnologias detectadas

{table(rows, ("Tecnologia / sinal", "Categoria", "Aplicacao no FabioOS", "Prioridade"))}

## 4. Conceitos

{bullets(concepts, "Nenhum conceito estruturante conhecido detectado automaticamente.")}

## 5. Padroes recorrentes

{bullets(categories, "Nenhuma categoria recorrente detectada automaticamente.")}

## 6. Aplicacao no FabioOS

### Imediatamente

{bullets(immediate, "Nada deve entrar imediatamente sem avaliacao humana.")}

### Futuramente

{bullets(future, "Nenhuma aplicacao futura detectada automaticamente.")}

### Descartar ou manter apenas como referencia

{bullets(reference, "Nenhum item classificado como apenas referencia.")}

## 7. Nivel de prioridade

**{priority_label(priority)}**

## 8. Decisao operacional sugerida

- Validar manualmente os sinais detectados.
- Converter itens essenciais em SPEC antes de implementar.
- Registrar custo, permissao e dados acessados antes de usar servico externo.
- Atualizar dashboard/changelog se alguma capacidade virar piloto.

## 9. Fonte

- Arquivo analisado: `{source_label(source)}`
- Tamanho aproximado: {len(text.split())} palavras
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera analise de Radar Tecnologico do FabioOS.")
    parser.add_argument("input", help="arquivo de texto/markdown a analisar")
    parser.add_argument("--title", default="", help="titulo da analise")
    parser.add_argument("--output", default="", help="arquivo Markdown de saida")
    args = parser.parse_args()

    src = Path(args.input)
    if not src.is_absolute():
        src = ROOT / src
    text = read_text(src)
    title = args.title or src.stem.replace("-", " ").replace("_", " ").title()
    signals = detect_signals(text)

    if args.output:
        out = Path(args.output)
        if not out.is_absolute():
            out = ROOT / out
    else:
        out = ROOT / DEFAULT_OUTPUT_DIR / f"{datetime.now().strftime('%Y-%m-%d')}_{slugify(title)}.md"

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(title, src, text, signals), encoding="utf-8")
    print(f"Radar gerado: {out.relative_to(ROOT).as_posix()}")
    print(f"Sinais detectados: {len(signals)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
