import type { PdfPipelineSnapshot } from "../types";

type Props = {
  pipeline: PdfPipelineSnapshot | null;
  connected: boolean;
};

const STIRLING_LABELS: Record<string, string> = {
  online: "ONLINE",
  auth_required: "AUTH 401",
  offline: "OFFLINE",
  unknown: "DESCONHECIDO",
};

function formatBytes(n: number): string {
  if (n < 1024) return `${n} B`;
  if (n < 1024 * 1024) return `${(n / 1024).toFixed(1)} KB`;
  return `${(n / (1024 * 1024)).toFixed(1)} MB`;
}

function formatChars(n: number): string {
  if (n >= 1_000_000) return `${(n / 1_000_000).toFixed(2)}M`;
  if (n >= 1000) return `${(n / 1000).toFixed(1)}k`;
  return String(n);
}

function looksRestricted(name: string): boolean {
  return /d\s*[&e]\s*d|dungeons?\s*(&|e)\s*dragons?|manual dos|livro do jogador|guia do mestre/i.test(
    name,
  );
}

function pipelineStage(event: PdfPipelineSnapshot["events"][0]) {
  if (event.safety?.rag_reindexed || event.extraction?.rag_reindexed) {
    return { label: "INDEXADO", className: "pdf-stage--indexed" };
  }
  if (event.safety?.ocr_executed || event.status === "extracted") {
    return { label: "EXTRAIDO", className: "pdf-stage--ocr" };
  }
  if (looksRestricted(event.file_name)) {
    return { label: "RESTRICTED", className: "pdf-stage--restricted" };
  }
  return { label: "DETECTADO", className: "pdf-stage--detected" };
}

export function PdfPipelinePanel({ pipeline, connected }: Props) {
  if (!pipeline) {
    return (
      <section className="pdf-pipeline pixel-panel pixel-border">
        <h2>PDF Pipeline</h2>
        <p className="muted">Carregando fila do drop folder…</p>
      </section>
    );
  }

  const stirlingClass = `pdf-stirling pdf-stirling--${pipeline.stirling.status}`;

  return (
    <section className="pdf-pipeline pixel-panel pixel-border">
      <header className="pdf-pipeline__header">
        <div>
          <h2>PDF Pipeline — Drop → Aprende</h2>
          <p className="pdf-pipeline__meta pixel-label">
            {pipeline.pendingPdfCount} PDF(s) na pasta · {pipeline.eventCount} evento(s) ·{" "}
            {connected ? "tempo real" : "polling"} · scan{" "}
            {pipeline.scannedAt.slice(11, 19)}
          </p>
        </div>
        <div className={stirlingClass}>
          <span className="pdf-stirling__label">Stirling (OCR pesado)</span>
          <strong>{STIRLING_LABELS[pipeline.stirling.status] ?? pipeline.stirling.status}</strong>
          <span className="pdf-stirling__detail">
            {pipeline.stirling.detail} · extrator local pypdf = zona Maestro
          </span>
        </div>
      </header>

      {pipeline.blockers.length > 0 && (
        <ul className="pdf-pipeline__blockers">
          {pipeline.blockers.map((b) => (
            <li key={b}>{b}</li>
          ))}
        </ul>
      )}

      <div className="pdf-pipeline__flow pixel-label">
        <span>00_Inbox/pdfs</span>
        <span>→</span>
        <span>Codex watcher</span>
        <span>→</span>
        <span>documentalista</span>
        <span>→</span>
        <span>Arquivista</span>
        <span>→</span>
        <span>RAG</span>
      </div>

      <div className="pdf-pipeline__list">
        {pipeline.events.length === 0 && (
          <p className="muted pdf-pipeline__empty">
            Nenhum evento ainda. Jogue um PDF em <code>00_Inbox/pdfs/</code> e rode{" "}
            <code>watch_pdf_drop.py --once</code>.
          </p>
        )}
        {pipeline.events.map((ev) => {
          const stage = pipelineStage(ev);
          return (
            <article key={ev.event_id} className="pdf-event">
              <header className="pdf-event__head">
                <span className={`pdf-stage ${stage.className}`}>{stage.label}</span>
                <strong>{ev.file_name}</strong>
                <time>{ev.detected_at.replace("T", " ").slice(0, 19)}</time>
              </header>
              <p className="pdf-event__path mono">{ev.source_pdf}</p>
              <p className="pdf-event__meta">
                {formatBytes(ev.size_bytes)} · SHA {ev.sha256.slice(0, 12)}… · status{" "}
                <code>{ev.status}</code> · {ev.target_agent}
              </p>
              {ev.extraction && (
                <p className="pdf-event__extraction">
                  {ev.extraction.method} · {ev.extraction.pages} pg ·{" "}
                  {formatChars(ev.extraction.chars ?? 0)} chars · gitignored
                </p>
              )}
              {stage.label === "RESTRICTED" && (
                <p className="pdf-event__restricted">Trilha Codex/PRIMUS — sem extracao integral</p>
              )}
              {!ev.extraction && stage.label !== "RESTRICTED" && (
                <p className="pdf-event__action">{ev.next_action}</p>
              )}
            </article>
          );
        })}
      </div>

      <footer className="pdf-pipeline__footer pixel-label">
        Spec: 60_Sistemas/FabioOS/specs/2026-06-30_pipeline-pdf-aprende.md · zona Cursor =
        espelho visual apenas
      </footer>
    </section>
  );
}
