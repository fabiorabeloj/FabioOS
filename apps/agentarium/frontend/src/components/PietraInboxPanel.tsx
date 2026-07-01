import { useCallback, useMemo, useState } from "react";
import type {
  PietraCartao,
  PietraInboxSnapshot,
  PietraRisco,
  PietraUiAction,
} from "../types";

type Props = {
  inbox: PietraInboxSnapshot | null;
  connected: boolean;
  apiBase: string;
  onRefresh: () => void;
};

const ACTION_KEY: Record<string, PietraUiAction> = {
  Responder: "responder",
  Encaminhar: "encaminhar",
  "Pedir dados": "pedir_dados",
  Arquivar: "arquivar",
};

const ACTION_LABEL: Record<PietraUiAction, string> = {
  responder: "Responder",
  encaminhar: "Encaminhar",
  pedir_dados: "Pedir dados",
  arquivar: "Arquivar",
};

function acaoBadgeClass(acao: string): string {
  if (acao.includes("bloquear") || acao.includes("escalar")) return "pietra-acao--blocked";
  if (acao.includes("responder_auto")) return "pietra-acao--auto";
  return "pietra-acao--review";
}

function formatAcao(acao: string): string {
  return acao.replace(/_/g, " ").toUpperCase();
}

export function PietraInboxPanel({ inbox, connected, apiBase, onRefresh }: Props) {
  const [busy, setBusy] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [selectedRemetente, setSelectedRemetente] = useState<string | null>(null);

  const session = useMemo(() => {
    if (!inbox || !selectedRemetente) return null;
    return inbox.sessions.find((s) => s.remetente === selectedRemetente) ?? null;
  }, [inbox, selectedRemetente]);

  const runAction = useCallback(
    async (card: PietraCartao, action: PietraUiAction) => {
      setBusy(card.id);
      setError(null);
      try {
        const res = await fetch(`${apiBase}/integrations/pietra-inbox/cards/${card.id}/action`, {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: JSON.stringify({ action }),
        });
        if (!res.ok) {
          const body = (await res.json()) as { error?: string };
          throw new Error(body.error ?? `HTTP ${res.status}`);
        }
        onRefresh();
      } catch (e) {
        setError(e instanceof Error ? e.message : "Falha na acao");
      } finally {
        setBusy(null);
      }
    },
    [apiBase, onRefresh],
  );

  if (!inbox) {
    return (
      <section className="pietra-inbox pixel-panel pixel-border">
        <h2>PietraOS Inbox</h2>
        <p className="muted">Carregando pietra_state.json…</p>
      </section>
    );
  }

  const { resumo, cards, uiState, coresRisco, acoes } = inbox;

  return (
    <section className="pietra-inbox pixel-panel pixel-border">
      <header className="pietra-inbox__header">
        <div>
          <h2>PietraOS Inbox — {inbox.tenant}</h2>
          <p className="pietra-inbox__meta pixel-label">
            {cards.length} na fila · {resumo.total} total · {resumo.sensiveis} sensíveis ·{" "}
            {connected ? "tempo real" : "polling"}
            {inbox.generatedAt && <> · sync {inbox.generatedAt.slice(0, 19)}</>}
            {inbox.fallbackMode && <> · fallback jsonl</>}
          </p>
        </div>
      </header>

      <aside className="pietra-inbox__report pixel-panel">
        <h3>Resumo</h3>
        <ul className="pietra-report__stats">
          <li>
            <strong>{resumo.total}</strong> atendimentos
          </li>
          <li>
            <strong>{resumo.sensiveis}</strong> sensíveis
          </li>
          <li>
            <strong>{resumo.pendentes}</strong> pendentes
          </li>
        </ul>
        {Object.keys(resumo.por_risco).length > 0 && (
          <div className="pietra-report__cats">
            <span className="pixel-label">Por risco</span>
            <ul>
              {(Object.entries(resumo.por_risco) as [PietraRisco, number][]).map(([r, n]) => (
                <li key={r}>
                  <span
                    className="pietra-risco-dot"
                    style={{ background: coresRisco[r] ?? "#64748b" }}
                  />
                  {r}: {n}
                </li>
              ))}
            </ul>
          </div>
        )}
        {session && (
          <div className="pietra-session">
            <h4>Conversa · {session.remetente}</h4>
            <p className="pixel-label">
              {session.estado} · {session.categoria ?? "—"}
            </p>
            <ul className="pietra-session__hist">
              {session.historico.map((h, i) => (
                <li key={i} className={`pietra-session__line pietra-session__line--${h.de}`}>
                  <strong>{h.de === "user" ? "Pai" : "Bot"}:</strong> {h.txt}
                </li>
              ))}
            </ul>
          </div>
        )}
      </aside>

      {error && <p className="banner banner--error">{error}</p>}

      <div className="pietra-inbox__queue">
        {cards.length === 0 && (
          <p className="muted pietra-inbox__empty">
            Fila vazia. Rode{" "}
            <code>python 60_Sistemas/Pietra/pietra_state.py --tenant {inbox.tenant}</code> após
            atendimentos.
          </p>
        )}
        {cards.map((card) => {
          const ui = uiState[card.id];
          const cor = coresRisco[card.risco] ?? "#64748b";
          const selected = selectedRemetente === card.remetente;
          return (
            <article
              key={card.id}
              className={`pietra-card ${card.bloqueado ? "pietra-card--blocked" : ""} ${selected ? "pietra-card--selected" : ""}`}
              style={{ borderLeftColor: cor, borderLeftWidth: "3px" }}
            >
              <header className="pietra-card__head">
                <span className="pietra-risco" style={{ borderColor: cor, color: cor }}>
                  {card.risco.toUpperCase()}
                </span>
                <span className={`pietra-acao ${acaoBadgeClass(card.acao)}`}>
                  {formatAcao(card.acao)}
                </span>
                <strong>{card.categoria}</strong>
                <span className="pietra-card__setor">{card.setor}</span>
                <time>{card.ts.replace("T", " ").slice(0, 19)}</time>
              </header>
              <p className="pietra-card__from">
                <button
                  type="button"
                  className="pietra-card__link"
                  onClick={() => setSelectedRemetente(card.remetente)}
                >
                  {card.remetente}
                </button>
                · {card.prioridade}
              </p>
              <p className="pietra-card__text">{card.texto}</p>
              {card.slots && Object.keys(card.slots).length > 0 && (
                <p className="pietra-card__slots">
                  Slots:{" "}
                  {Object.entries(card.slots)
                    .map(([k, v]) => `${k}=${v}`)
                    .join(" · ")}
                </p>
              )}
              {card.bloqueado && (
                <p className="pietra-card__blocked">
                  Sensível — não responder automaticamente; escalar humano.
                </p>
              )}
              {card.resposta_sugerida && (
                <blockquote className="pietra-card__suggestion">
                  {card.resposta_sugerida}
                </blockquote>
              )}
              {ui && (
                <p className="pietra-card__ui pixel-label">
                  UI: {ACTION_LABEL[ui.action]} · {ui.at.slice(11, 19)}
                </p>
              )}
              <footer className="pietra-card__actions">
                {acoes.map((label) => {
                  const action = ACTION_KEY[label];
                  if (!action) return null;
                  return (
                    <button
                      key={label}
                      type="button"
                      className="pixel-button pietra-action-btn"
                      disabled={
                        busy === card.id || (action === "responder" && card.bloqueado)
                      }
                      onClick={() => runAction(card, action)}
                    >
                      {label}
                    </button>
                  );
                })}
              </footer>
            </article>
          );
        })}
      </div>

      <footer className="pietra-inbox__footer pixel-label">
        Fonte: tenants/&lt;tenant&gt;/pietra_state.json · sessões em sessions/ · persona:{" "}
        {inbox.persona.nome_bot ?? "Assistente"}
      </footer>
    </section>
  );
}
