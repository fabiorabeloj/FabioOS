import { useEffect, useMemo, useRef, useState } from "react";
import type { BarramentoSnapshot } from "../types";
import {
  agentAvatar,
  formatBarramentoTime,
  matchesBarramentoFilter,
  tipoBadgeClass,
  TIPO_LABELS,
  uniqueBarramentoActors,
  type BarramentoAgentFilter,
} from "../barramentoUtils";

type Props = {
  barramento: BarramentoSnapshot | null;
  connected: boolean;
};

function Avatar({ id }: { id: string }) {
  const a = agentAvatar(id);
  return (
    <span
      className="barramento-avatar"
      style={{ background: a.bg, color: a.color }}
      title={a.name}
    >
      {a.label}
    </span>
  );
}

export function BarramentoPanel({ barramento, connected }: Props) {
  const [filter, setFilter] = useState<BarramentoAgentFilter>("all");
  const endRef = useRef<HTMLDivElement>(null);
  const listRef = useRef<HTMLDivElement>(null);

  const entries = barramento?.entries ?? [];

  const actors = useMemo(() => uniqueBarramentoActors(entries), [entries]);

  const filtered = useMemo(
    () => entries.filter((e) => matchesBarramentoFilter(e, filter)),
    [entries, filter],
  );

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [filtered.length, barramento?.generatedAt]);

  return (
    <section className="barramento-panel pixel-panel pixel-border">
      <header className="barramento-panel__header">
        <div>
          <h2>Barramento ao vivo</h2>
          <p className="barramento-panel__meta pixel-label">
            {barramento?.count ?? 0} mensagens
            {barramento?.generatedAt && (
              <> · sync {barramento.generatedAt.slice(0, 19).replace("T", " ")}</>
            )}
            {connected ? " · tempo real" : " · polling"}
          </p>
        </div>
        <div className="barramento-panel__filters">
          <label className="pixel-label" htmlFor="barramento-filter">
            Agente
          </label>
          <select
            id="barramento-filter"
            className="pixel-select"
            value={filter}
            onChange={(e) => setFilter(e.target.value as BarramentoAgentFilter)}
          >
            <option value="all">Todos ({entries.length})</option>
            {actors.map((id) => (
              <option key={id} value={id}>
                {agentAvatar(id).name} ({id})
              </option>
            ))}
          </select>
        </div>
      </header>

      <div className="barramento-panel__timeline" ref={listRef}>
        {filtered.length === 0 && (
          <p className="barramento-panel__empty muted">
            Nenhuma mensagem no barramento ainda.
          </p>
        )}
        {filtered.map((msg, i) => {
          const tipoKey = msg.tipo.toLowerCase();
          const tipoLabel = TIPO_LABELS[tipoKey] ?? msg.tipo.toUpperCase();
          return (
            <article
              key={`${msg.ts}-${msg.de}-${i}`}
              className={`barramento-msg barramento-msg--${tipoKey}`}
            >
              <div className="barramento-msg__head">
                <Avatar id={msg.de} />
                <span className="barramento-msg__route">
                  <strong>{agentAvatar(msg.de).name}</strong>
                  <span className="barramento-msg__arrow">→</span>
                  <strong>{agentAvatar(msg.para).name}</strong>
                </span>
                <span className={`barramento-badge ${tipoBadgeClass(msg.tipo)}`}>
                  {tipoLabel}
                </span>
                <time className="barramento-msg__time">{formatBarramentoTime(msg.ts)}</time>
              </div>
              <p className="barramento-msg__body">{msg.mensagem}</p>
              {msg.status && msg.status !== "aberto" && (
                <span className="barramento-msg__status pixel-badge">{msg.status}</span>
              )}
            </article>
          );
        })}
        <div ref={endRef} />
      </div>

      <footer className="barramento-panel__legend pixel-label">
        <span className="barramento-badge barramento-badge--ordem">ordem</span>
        <span className="barramento-badge barramento-badge--handoff">handoff</span>
        <span className="barramento-badge barramento-badge--ack">ack</span>
        <span className="barramento-badge barramento-badge--aviso">aviso</span>
        <span className="barramento-badge barramento-badge--bloqueio">bloqueio</span>
      </footer>
    </section>
  );
}
