import { useMemo, useState } from "react";
import type { Agent, AgentLayer } from "../types";
import { LAYER_LABELS, STATUS_LABELS, RISK_LABELS } from "../types";
import { filterCatalogByLayer } from "../hooks/useAgents";

type Props = {
  catalog: import("../types").AgentCatalog | null;
  selectedId: string | null;
  onSelect: (id: string) => void;
};

export function AgentCatalogPanel({ catalog, selectedId, onSelect }: Props) {
  const [layer, setLayer] = useState<AgentLayer | "all">("all");

  const agents = useMemo(
    () => filterCatalogByLayer(catalog, layer),
    [catalog, layer],
  );

  if (!catalog) {
    return (
      <section className="agent-catalog pixel-panel pixel-border">
        <h2>Agent Catalog</h2>
        <p className="muted">Carregando catalogo...</p>
      </section>
    );
  }

  return (
    <section className="agent-catalog pixel-panel pixel-border">
      <header className="agent-catalog__header">
        <h2>Agent Catalog</h2>
        <p className="agent-catalog__counts pixel-label">
          {catalog.counts.active} ativos · {catalog.counts.planned} planejados ·{" "}
          {catalog.counts.total} total
        </p>
      </header>

      <div className="agent-catalog__filters">
        <label className="pixel-label" htmlFor="layer-filter">
          Camada
        </label>
        <select
          id="layer-filter"
          className="pixel-select"
          value={layer}
          onChange={(e) => setLayer(e.target.value as AgentLayer | "all")}
        >
          <option value="all">Todas</option>
          {catalog.layers.map((l) => (
            <option key={l} value={l}>
              {LAYER_LABELS[l]}
            </option>
          ))}
        </select>
      </div>

      <div className="agent-catalog__grid">
        {agents.map((a) => (
          <CatalogCard
            key={a.id}
            agent={a}
            selected={selectedId === a.id}
            onSelect={onSelect}
          />
        ))}
      </div>
    </section>
  );
}

function CatalogCard({
  agent,
  selected,
  onSelect,
}: {
  agent: Agent;
  selected: boolean;
  onSelect: (id: string) => void;
}) {
  return (
    <button
      type="button"
      className={`catalog-card catalog-card--${agent.status} ${selected ? "catalog-card--selected" : ""} ${agent.essential ? "catalog-card--essential" : ""}`}
      onClick={() => onSelect(agent.id)}
    >
      <header>
        <strong>{agent.name}</strong>
        <span className={`catalog-badge catalog-badge--${agent.status}`}>
          {STATUS_LABELS[agent.status]}
        </span>
      </header>
      <p className="catalog-card__layer pixel-label">{LAYER_LABELS[agent.layer]}</p>
      <p className="catalog-card__zone">{agent.catalogZone}</p>
      <p className="catalog-card__role">{agent.role}</p>
      <footer>
        <span className={`risk-pill risk-pill--${agent.policy.riskLevel}`}>
          {RISK_LABELS[agent.policy.riskLevel]}
        </span>
        {agent.essential && <span className="catalog-badge catalog-badge--essential">ESSENCIAL</span>}
      </footer>
    </button>
  );
}
