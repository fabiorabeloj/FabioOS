import fs from "node:fs";
import path from "node:path";
import type {
  PietraCartao,
  PietraCartaoUi,
  PietraInboxSnapshot,
  PietraResumo,
  PietraSession,
  PietraStateJson,
  PietraUiAction,
} from "./types.js";
import {
  resolvePietraUiStatePath,
  resolveTenantAtendimentos,
  resolveTenantPietraState,
  resolveTenantSessionsDir,
  defaultPietraTenant,
  resolvePietraSpecPath,
} from "./paths.js";

const DEFAULT_CORES = {
  baixo: "#22c55e",
  medio: "#eab308",
  alto: "#f97316",
  critico: "#dc2626",
};

function emptyResumo(tenant: string): PietraResumo {
  return { total: 0, por_risco: {}, sensiveis: 0, pendentes: 0 };
}

function loadCartoesFromJsonl(tenant: string): PietraCartao[] {
  const file = resolveTenantAtendimentos(tenant);
  if (!fs.existsSync(file)) return [];

  const lines = fs.readFileSync(file, "utf8").split(/\r?\n/).filter(Boolean);
  const cards: PietraCartao[] = [];
  for (const line of lines) {
    try {
      const parsed = JSON.parse(line) as PietraCartao;
      if (parsed.id) cards.push(parsed);
    } catch {
      /* skip */
    }
  }
  return cards.sort((a, b) => b.ts.localeCompare(a.ts));
}

function buildResumoFromCards(cards: PietraCartao[]): PietraResumo {
  const all = [...cards].reverse();
  const por_risco: PietraResumo["por_risco"] = {};
  for (const it of all) {
    por_risco[it.risco] = (por_risco[it.risco] ?? 0) + 1;
  }
  return {
    total: all.length,
    por_risco,
    sensiveis: (por_risco.alto ?? 0) + (por_risco.critico ?? 0),
    pendentes: all.filter((it) => it.acao !== "responder_auto").length,
  };
}

export function loadPietraState(tenant?: string): PietraStateJson | null {
  const file = resolveTenantPietraState(tenant);
  if (!fs.existsSync(file)) return null;
  try {
    return JSON.parse(fs.readFileSync(file, "utf8")) as PietraStateJson;
  } catch {
    return null;
  }
}

export function loadSessions(tenant?: string): PietraSession[] {
  const dir = resolveTenantSessionsDir(tenant);
  if (!fs.existsSync(dir)) return [];

  const sessions: PietraSession[] = [];
  for (const name of fs.readdirSync(dir)) {
    if (!name.endsWith(".json")) continue;
    try {
      const parsed = JSON.parse(
        fs.readFileSync(path.join(dir, name), "utf8"),
      ) as PietraSession;
      if (parsed.remetente) sessions.push(parsed);
    } catch {
      /* skip */
    }
  }
  return sessions.sort((a, b) =>
    (b.atualizado ?? b.criado).localeCompare(a.atualizado ?? a.criado),
  );
}

export function loadUiState(): Record<string, PietraCartaoUi> {
  const filePath = resolvePietraUiStatePath();
  if (!fs.existsSync(filePath)) return {};
  try {
    return JSON.parse(fs.readFileSync(filePath, "utf8")) as Record<string, PietraCartaoUi>;
  } catch {
    return {};
  }
}

export function saveUiAction(cardId: string, action: PietraUiAction, note?: string): PietraCartaoUi {
  const filePath = resolvePietraUiStatePath();
  const state = loadUiState();
  const entry: PietraCartaoUi = {
    action,
    at: new Date().toISOString(),
    note,
  };
  state[cardId] = entry;
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  fs.writeFileSync(filePath, JSON.stringify(state, null, 2), "utf8");
  return entry;
}

export function buildPietraInboxSnapshot(tenant?: string): PietraInboxSnapshot {
  const t = tenant ?? defaultPietraTenant();
  const statePath = resolveTenantPietraState(t);
  const state = loadPietraState(t);
  const sessions = loadSessions(t);

  if (state) {
    return {
      scannedAt: new Date().toISOString(),
      generatedAt: state.generatedAt,
      source: state.source,
      tenant: state.tenant,
      vertical: state.vertical,
      specPath: resolvePietraSpecPath(),
      statePath,
      coresRisco: { ...DEFAULT_CORES, ...state.cores_risco },
      acoes: state.acoes,
      resumo: state.resumo,
      cards: state.fila,
      persona: state.persona ?? {},
      sessions,
      uiState: loadUiState(),
      fallbackMode: false,
    };
  }

  const cards = loadCartoesFromJsonl(t);
  return {
    scannedAt: new Date().toISOString(),
    generatedAt: null,
    source: null,
    tenant: t,
    vertical: cards[0]?.vertical ?? "escola",
    specPath: resolvePietraSpecPath(),
    statePath,
    coresRisco: DEFAULT_CORES,
    acoes: ["Responder", "Encaminhar", "Pedir dados", "Arquivar"],
    resumo: buildResumoFromCards(cards),
    cards,
    persona: {},
    sessions,
    uiState: loadUiState(),
    fallbackMode: true,
  };
}
