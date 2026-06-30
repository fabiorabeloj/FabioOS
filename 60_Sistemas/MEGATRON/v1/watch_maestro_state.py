#!/usr/bin/env python3
"""
Watcher do Maestro — regenera `maestro_state.json` quando o roster ou o barramento
mudam, fechando o loop com o Agentarium (Cursor), que já observa o JSON.

Lado Maestro (Claude): observa `registry.py` + `Barramento_Multiagente.md` e roda
`maestro_state.py` quando qualquer um muda. Polling leve (sem dependências extras).
Lado Interface (Cursor): file-watcher no JSON → resync via WebSocket (~300 ms).

Uso:
    python watch_maestro_state.py [--intervalo 2]
"""
import subprocess
import sys
import time
from pathlib import Path

V1 = Path(__file__).resolve().parent
sys.path.insert(0, str(V1))
from barramento import BUS  # caminho do arquivo do barramento  # noqa: E402

PY = sys.executable
WATCHED = [V1 / "registry.py", BUS]


def _snap():
    return tuple((f.stat().st_mtime if f.exists() else 0.0) for f in WATCHED)


def _regen():
    subprocess.run([PY, str(V1 / "maestro_state.py")], check=False)


def main() -> int:
    interval = 2.0
    if "--intervalo" in sys.argv:
        interval = float(sys.argv[sys.argv.index("--intervalo") + 1])
    _regen()
    last = _snap()
    print(f"[watch] Maestro observando {[f.name for f in WATCHED]} "
          f"a cada {interval}s — JSON regenerado no boot. Ctrl+C para sair.")
    try:
        while True:
            time.sleep(interval)
            cur = _snap()
            if cur != last:
                _regen()
                last = cur
                print("[watch] mudança detectada -> maestro_state.json regenerado")
    except KeyboardInterrupt:
        print("\n[watch] encerrado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
