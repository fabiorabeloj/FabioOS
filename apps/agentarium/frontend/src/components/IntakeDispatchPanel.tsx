import { useCallback, useState } from "react";
import type { IntakeCard, IntakeDispatchSnapshot } from "../types";

type Props = {
  dispatch: IntakeDispatchSnapshot | null;
  connected: boolean;
  apiBase: string;
  onRefresh: () => void;
};

const SENSITIVE = new Set(["restricted", "forbidden_external", "no_rag"]);

function statusColor(status: string, cores: Record<string, string>): string {
  if (status === "waiting_approval") return cores.waiting_approval ?? "#eab308";
  if (status === "blocked") return cores.blocked ?? "#dc2626";
  if (status === "archived") return cores.archived ?? "#64748b";
  if (status === "executed") return "#22c55e";
  return cores.classified ?? "#38bdf8";
}

function urgencyClass(u: string): string {
  if (u === "critical" || u === "high") return "intake-urgency--high";
  if (u === "medium") return "intake-urgency--med";
  return "intake-urgency--low";
}

export function IntakeDispatchPanel({ dispatch, connected, apiBase, onRefresh }: Props) {
  const [busy, setBusy] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [command, setCommand] = useState("");
  const [lastResult, setLastResult] = useState<string | null>(null);

  const runAction = useCallback(
    async (path: string, label: string) => {
      setBusy(label);
      setError(null);
      try {
        const res = await fetch(`${apiBase}${path}`, {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: path.includes("command") ? JSON.stringify({ text: command }) : undefined,
        });
        const body = (await res.json()) as { error?: string; message?: string; blocked?: boolean; notaRef?: string };
        if (!res.ok) throw new Error(body.error ?? body.message ?? `HTTP ${res.status}`);
        setLastResult(body.message ?? "OK");
        if (path.includes("command")) setCommand("");
        onRefresh();
      } catch (e) {
        setError(e instanceof Error ? e.message : "Falha na acao");
      } finally {
        setBusy(null);
      }
    },
    [apiBase, command, onRefresh],
  );

  const approve = (card: IntakeCard) =>
    runAction(`/integrations/intake-dispatch/cards/${encodeURIComponent(card.id)}/approve`, card.id);

  const reject = (card: IntakeCard) =>
    runAction(`/integrations/intake-dispatch/cards/${encodeURIComponent(card.id)}/reject`, card.id);

  if (!dispatch) {
    return (
      <section className="intake-dispatch pixel-panel pixel-border">
        <h2>Mesa de Despacho — Aguardando Fabio</h2>
        <p className="muted">Carregando intake_queue…</p>
      </section>
    );
  }

  const { queue, pending, coordenacao, fallbackMode } = dispatch;
  const cores = queue.cores_status ?? {};
  const allCards = queue.fila ?? [];

  return (
    <section className="intake-dispatch pixel-panel pixel-border">
      <header className="intake-dispatch__header">
        <div>
          <h2>Mesa de Despacho — Aguardando Fabio</h2>
          <p className="intake-dispatch__meta pixel-label">
            {pending.length} pendente(s) · {queue.resumo.total} total · {queue.resumo.sensiveis} sensíveis ·{" "}
            {connected ? "tempo real" : "polling"}
            {fallbackMode && " · sample (fila live ausente)"}
          </p>
        </div>
        <div className="intake-dispatch__header-actions">
        <button
          type="button"
          className="btn btn-tactical pixel-button"
          disabled={!!busy}
          onClick={() => runAction("/integrations/intake-dispatch/refresh-flow", "refresh")}
        >
          Regenerar fila (intake_flow)
        </button>
        <button
          type="button"
          className="btn pixel-button"
          disabled={!!busy}
          onClick={() => runAction("/integrations/intake-dispatch/import-gmail-fake", "gmail-fake")}
        >
          Importar Gmail fake
        </button>
        </div>
      </header>

      {coordenacao && (
        <aside className="intake-coord pixel-panel">
          <h3>Coordenação multiagente</h3>
          <ul className="intake-coord__stats">
            <li>
              Barramento: <strong>{coordenacao.barramento.abertas}</strong> abertas
            </li>
            <li>
              Frentes ativas: <strong>{coordenacao.frentes_ativas.length}</strong>
            </li>
          </ul>
          {Object.keys(coordenacao.velocidade).length > 0 && (
            <div className="intake-coord__velocity">
              <span className="pixel-label">Última atividade</span>
              <ul>
                {Object.entries(coordenacao.velocidade)
                  .sort((a, b) => b[1].localeCompare(a[1]))
                  .slice(0, 5)
                  .map(([ag, ts]) => (
                    <li key={ag}>
                      {ag}: {ts.slice(0, 16)}
                    </li>
                  ))}
              </ul>
            </div>
          )}
        </aside>
      )}

      <form
        className="intake-command pixel-panel"
        onSubmit={(e) => {
          e.preventDefault();
          if (command.trim()) void runAction("/integrations/intake-dispatch/command", "cmd");
        }}
      >
        <label className="pixel-label" htmlFor="intake-cmd">
          Comando natural
        </label>
        <div className="intake-command__row">
          <input
            id="intake-cmd"
            className="intake-command__input"
            placeholder='Ex.: prova do 8o ano sobre Africa para amanha'
            value={command}
            onChange={(e) => setCommand(e.target.value)}
            disabled={!!busy}
          />
          <button type="submit" className="btn btn-tactical pixel-button" disabled={!!busy || !command.trim()}>
            Criar pendência
          </button>
        </div>
        <p className="muted intake-command__hint">
          Classifica via megatron_core → entra na fila live → exige aprovação antes de gravar no Obsidian.
        </p>
      </form>

      {error && <p className="banner banner--error">{error}</p>}
      {lastResult && <p className="banner banner--ok">{lastResult}</p>}

      <div className="intake-dispatch__queue">
        {allCards.length === 0 && (
          <p className="muted">
            Fila vazia. Rode{" "}
            <code>python 60_Sistemas/MEGATRON/v1/intake_flow.py</code> ou use Regenerar fila.
          </p>
        )}
        {allCards.map((card) => {
          const sensitive = SENSITIVE.has(card.sensitivity);
          const waiting = card.status === "waiting_approval";
          return (
            <article
              key={card.id}
              className={`intake-card pixel-panel ${card.alerta ? "intake-card--alert" : ""}`}
              style={{ borderLeftColor: statusColor(card.status, cores) }}
            >
              <header className="intake-card__head">
                <span className={`intake-badge ${urgencyClass(card.urgency)}`}>{card.urgency}</span>
                <span className="intake-badge intake-badge--domain">{card.domain}</span>
                <span className="intake-badge intake-badge--sens">{card.sensitivity}</span>
                <span className="intake-badge intake-badge--status">{card.status}</span>
              </header>
              <p className="intake-card__summary">{card.summary}</p>
              {card.extracao && card.extracao.confianca > 0 && (
                <dl className="intake-card__extracao">
                  <span className="pixel-label">Extração estruturada</span>
                  {card.extracao.produto && (
                    <div>
                      <dt>Produto</dt>
                      <dd>{card.extracao.produto}</dd>
                    </div>
                  )}
                  {card.extracao.serie && (
                    <div>
                      <dt>Série</dt>
                      <dd>{card.extracao.serie}</dd>
                    </div>
                  )}
                  {card.extracao.tema && (
                    <div>
                      <dt>Tema</dt>
                      <dd>{card.extracao.tema}</dd>
                    </div>
                  )}
                  {card.extracao.prazo && (
                    <div>
                      <dt>Prazo</dt>
                      <dd>{card.extracao.prazo}</dd>
                    </div>
                  )}
                </dl>
              )}
              <dl className="intake-card__meta">
                <div>
                  <dt>Fonte</dt>
                  <dd>{card.source}</dd>
                </div>
                <div>
                  <dt>Agente</dt>
                  <dd>{card.suggested_agent}</dd>
                </div>
                <div>
                  <dt>Ação</dt>
                  <dd>{card.suggested_action}</dd>
                </div>
                {card.sender && (
                  <div>
                    <dt>Remetente</dt>
                    <dd>{card.sender}</dd>
                  </div>
                )}
                {card.subject && (
                  <div>
                    <dt>Assunto</dt>
                    <dd>{card.subject}</dd>
                  </div>
                )}
              </dl>
              {card.nota_ref && (
                <p className="intake-card__note-ref">
                  Nota: <code>{card.nota_ref}</code>
                </p>
              )}
              {sensitive && waiting && (
                <p className="intake-card__warn">⛔ Sensível — aprovar escala/bloqueia gravação no Obsidian (trava §3).</p>
              )}
              {waiting && (
                <div className="intake-card__actions">
                  <button
                    type="button"
                    className="btn btn-tactical pixel-button intake-btn--approve"
                    disabled={busy === card.id}
                    onClick={() => approve(card)}
                  >
                    {sensitive ? "Escalar / Bloquear" : "Aprovar → Obsidian"}
                  </button>
                  <button
                    type="button"
                    className="btn pixel-button intake-btn--reject"
                    disabled={busy === card.id}
                    onClick={() => reject(card)}
                  >
                    Rejeitar
                  </button>
                </div>
              )}
            </article>
          );
        })}
      </div>
    </section>
  );
}
