#!/usr/bin/env python3
"""
Registro de agentes do coordenador MEGATRON.

Mapeia uma **capacidade** (classe de permissão da Fase 17) ao agente que a
executa. O orquestrador (`megatron.py`) consulta este registro em vez de
conhecer o interior dos agentes. Cada agente expõe `run(...) -> Resultado`
(contrato congelado — ver Ordens de Coordenação).

Apenas a classe `escrita_segura` é despachável; `sensivel` e `externa`
permanecem bloqueadas (requerem aprovação humana e não têm agente automático).
"""
import sys
from pathlib import Path

V1 = Path(__file__).resolve().parent
AGENTES = V1.parent / "agentes" / "implementacao" / "claude"
if str(AGENTES) not in sys.path:
    sys.path.insert(0, str(AGENTES))

# capacidade -> (nome do agente, descrição curta)
CAPACIDADES = {
    "escrita_segura": ("arquivista", "cria rascunho de nota em 00_Inbox (dry-run por padrão)"),
}


def resolver(classe: str):
    """Retorna a função `run` do agente da classe, ou None se não despachável.
    Import lazy: o agente só é carregado quando realmente usado."""
    if classe == "escrita_segura":
        import arquivista
        return arquivista.run
    return None
