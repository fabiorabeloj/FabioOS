# Watcher do Maestro (wrapper). Regenera maestro_state.json quando o roster/barramento
# mudam; o Agentarium (Cursor) observa o JSON e espelha no dashboard.
# Uso: .\watch_maestro_state.ps1
$venv = "..\..\RAG\.venv\Scripts\python.exe"
& $venv "$PSScriptRoot\watch_maestro_state.py" --intervalo 2
