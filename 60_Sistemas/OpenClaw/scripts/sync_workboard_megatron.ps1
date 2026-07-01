# Sincroniza cards MEGATRON no Workboard OpenClaw (board fabioos)
$ErrorActionPreference = 'Continue'

$Agents = @(
    @{ Title = 'MEGATRON SafeCommit (agent.safecommit)'; Notes = 'Scan git + segredos. Run: run_megatron_agent.ps1 -Agente safecommit'; Priority = 'normal' }
    @{ Title = 'MEGATRON Arquivista (agent.arquivista)'; Notes = 'Inbox bruto -> nota wiki. Run: run_megatron_agent.ps1 -Agente arquivista'; Priority = 'normal' }
    @{ Title = 'MEGATRON Inbox (agent.inbox)'; Notes = 'Triagem 00_Inbox. Run: run_megatron_agent.ps1 -Agente inbox'; Priority = 'normal' }
    @{ Title = 'MEGATRON RAG (agent.rag)'; Notes = 'Consulta RAG Fase 12. Run: run_megatron_agent.ps1 -Agente rag -Args pergunta'; Priority = 'high' }
    @{ Title = 'MEGATRON Dashboard (agent.dashboard)'; Notes = 'STATUS_Agentes.md. Run: run_megatron_agent.ps1 -Agente dashboard'; Priority = 'normal' }
)

foreach ($a in $Agents) {
    $cmd = @(
        'openclaw', 'workboard', 'create',
        '--board', 'fabioos',
        '--labels', 'megatron,agent,fabioos',
        '--status', 'todo',
        '--priority', $a.Priority,
        '--notes', $a.Notes,
        $a.Title
    )
    Write-Host "Criando card: $($a.Title)" -ForegroundColor Gray
    wsl -d OpenClawGateway -- @cmd 2>&1
}

Write-Host "`nListando board fabioos:" -ForegroundColor Cyan
wsl -d OpenClawGateway -- openclaw workboard list --board fabioos 2>&1
