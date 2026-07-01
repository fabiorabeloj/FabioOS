import type { EventLogEntry } from "../types";

type Props = {
  entries: EventLogEntry[];
};

export function EventLog({ entries }: Props) {
  return (
    <section className="event-log panel-tactical pixel-panel pixel-border">
      <h2 className="event-log__title">Event Log</h2>
      <ul className="event-log__list">
        {entries.length === 0 && (
          <li className="event-log__empty muted">Nenhum evento ainda.</li>
        )}
        {entries.slice(0, 40).map((e) => (
          <li key={e.id} className={`event-log__item event-log__item--${e.channel.toLowerCase()}`}>
            <span className="event-log__time">
              {new Date(e.timestamp).toLocaleTimeString("pt-BR")}
            </span>
            <span className="event-log__tags">
              <span className="pixel-badge">[{e.channel}]</span>
              {e.source && <span className="pixel-badge pixel-badge--state">{e.source}</span>}
            </span>
            <span className="event-log__msg">{e.message}</span>
            {e.maskedPhone && (
              <span className="event-log__phone mono">{e.maskedPhone}</span>
            )}
            {e.jobId && <span className="event-log__job mono">{e.jobId}</span>}
          </li>
        ))}
      </ul>
    </section>
  );
}
