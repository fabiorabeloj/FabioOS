import type { SecurityMatrix } from "../types";
import { LAYER_LABELS, RISK_LABELS, STATUS_LABELS } from "../types";

type Props = {
  matrix: SecurityMatrix | null;
  onSelect: (id: string) => void;
  selectedId: string | null;
};

export function SecurityMatrixPanel({ matrix, onSelect, selectedId }: Props) {
  if (!matrix) {
    return (
      <section className="security-matrix panel-tactical pixel-panel pixel-border">
        <h2>Security Matrix</h2>
        <p className="muted">Carregando matriz...</p>
      </section>
    );
  }

  return (
    <section className="security-matrix panel-tactical pixel-panel pixel-border">
      <h2>Security Matrix</h2>
      {matrix.globalAlerts.length > 0 && (
        <ul className="global-alerts">
          {matrix.globalAlerts.map((a) => (
            <li key={a} className="alert alert--danger">
              {a}
            </li>
          ))}
        </ul>
      )}
      <div className="matrix-scroll">
        <table className="matrix-table">
          <thead>
            <tr>
              <th>Agent</th>
              <th>Status</th>
              <th>Layer</th>
              <th>Sandbox</th>
              <th>Access</th>
              <th>Exec</th>
              <th>Write</th>
              <th>Elevated</th>
              <th>Risk</th>
            </tr>
          </thead>
          <tbody>
            {matrix.rows.map((row) => (
              <tr
                key={row.id}
                className={`matrix-row matrix-row--${row.riskLevel} ${selectedId === row.id ? "matrix-row--selected" : ""}`}
                onClick={() => onSelect(row.id)}
              >
                <td>{row.name}</td>
                <td>
                  <span className={`catalog-badge catalog-badge--${row.status}`}>
                    {STATUS_LABELS[row.status]}
                  </span>
                </td>
                <td className="pixel-label">{LAYER_LABELS[row.layer]}</td>
                <td>{row.sandboxMode}</td>
                <td>{row.workspaceAccess}</td>
                <td>{row.exec ? "yes" : "no"}</td>
                <td>{row.write ? "yes" : "no"}</td>
                <td>{row.elevated}</td>
                <td>
                  <span className={`risk-pill risk-pill--${row.riskLevel}`}>
                    {RISK_LABELS[row.riskLevel]}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
