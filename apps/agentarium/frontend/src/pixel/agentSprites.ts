import { mergePalette } from "./pixelPalettes";
import type { PixelFrame, PixelSpriteDefinition } from "./pixelTypes";

function f(...rows: string[]): PixelFrame {
  return rows;
}

const pietraIdle = f(
  "....KKKK....",
  "...KWWWWK...",
  "...KWBWBK...",
  "...KWWWWK...",
  "...KKKKK....",
  "..KBBBBBBK..",
  "..KBYBBYBK..",
  "..KBBBBBBK..",
  "..KB....BK..",
  "..KDD..DDK..",
  "..KK....KK..",
);

const pietraIdle2 = f(
  "....KKKK....",
  "...KWWWWK...",
  "...KWBWBK...",
  "...KWWWWK...",
  "...KKKKK....",
  "..KBBBBBBK..",
  "..KBYBBYBK..",
  "..KBBBBBBK..",
  "..KB....BK..",
  "..KDD..DDK..",
  "..KK....KK..",
  "..K......K..",
);

const pietraWalk1 = f(
  "....KKKK....",
  "...KWWWWK...",
  "...KWBWBK...",
  "...KWWWWK...",
  "...KKKKK....",
  "..KBBBBBBK..",
  "..KBYBBYBK..",
  "..KBBBBBBK..",
  "..KB....BK..",
  "..KDD....K..",
  "...KK...KK..",
  "....KKKK....",
);

const pietraWalk2 = f(
  "....KKKK....",
  "...KWWWWK...",
  "...KWBWBK...",
  "...KWWWWK...",
  "...KKKKK....",
  "..KBBBBBBK..",
  "..KBYBBYBK..",
  "..KBBBBBBK..",
  "..KB....BK..",
  "..K....DDK..",
  "..KK...KK...",
  "....KKKK....",
);

const arquivistaIdle = f(
  "....KKKK....",
  "...KMMMMK...",
  "..KMMMMMMK..",
  "..KMGGGGMK..",
  "..KMGGGGMK..",
  "..KMMMMMMK..",
  "..KMSMMMSK..",
  "..KMSMMMSK..",
  "..KMMMMMMK..",
  "..KDD..DDK..",
  "..KK....KK..",
);

const arquivistaWalk1 = f(
  "....KKKK....",
  "...KMMMMK...",
  "..KMMMMMMK..",
  "..KMGGGGMK..",
  "..KMGGGGMK..",
  "..KMMMMMMK..",
  "..KMSMMMSK..",
  "..KMSMMMSK..",
  "..KMMMMMMK..",
  "..KDD....K..",
  "...KK...KK..",
  "....KKKK....",
);

const arquivistaWalk2 = f(
  "....KKKK....",
  "...KMMMMK...",
  "..KMMMMMMK..",
  "..KMGGGGMK..",
  "..KMGGGGMK..",
  "..KMMMMMMK..",
  "..KMSMMMSK..",
  "..KMSMMMSK..",
  "..KMMMMMMK..",
  "..K....DDK..",
  "..KK...KK...",
  "....KKKK....",
);

const codexIdle = f(
  "....KKKK....",
  "...KCCCCCK..",
  "..KCCCCCCCK.",
  "..KCWWWWCCK.",
  "..KCCCCCCCK.",
  "...KCCCCCK..",
  "...KGGGGGK..",
  "..KGG..GGK..",
  "..KGG..GGK..",
  "..KK....KK..",
);

const codexWalk1 = f(
  "....KKKK....",
  "...KCCCCCK..",
  "..KCCCCCCCK.",
  "..KCWWWWCCK.",
  "..KCCCCCCCK.",
  "...KCCCCCK..",
  "...KGGGGGK..",
  "..KGG....GK.",
  "..KGG....GK.",
  "...KK...KK..",
  "....KKKK....",
);

const codexWalk2 = f(
  "....KKKK....",
  "...KCCCCCK..",
  "..KCCCCCCCK.",
  "..KCWWWWCCK.",
  "..KCCCCCCCK.",
  "...KCCCCCK..",
  "...KGGGGGK..",
  ".GK....GGK..",
  ".GK....GGK..",
  "..KK...KK...",
  "....KKKK....",
);

const pesquisadorIdle = f(
  "....KKKK....",
  "...KPPPPPK..",
  "..KPCCCCPK..",
  "..KPCWWCPK..",
  "..KPCCCCPK..",
  "...KPCCCPK..",
  "...KPKKKPK..",
  "....KPPK....",
  "....K..K....",
  "...KK..KK...",
);

const pesquisadorWalk1 = f(
  "....KKKK....",
  "...KPPPPPK..",
  "..KPCCCCPK..",
  "..KPCWWCPK..",
  "..KPCCCCPK..",
  "...KPCCCPK..",
  "...KPKKKPK..",
  "....KPPK....",
  "....K..K....",
  "...K....K...",
  "....KKKK....",
);

const pesquisadorWalk2 = f(
  "....KKKK....",
  "...KPPPPPK..",
  "..KPCCCCPK..",
  "..KPCWWCPK..",
  "..KPCCCCPK..",
  "...KPCCCPK..",
  "...KPKKKPK..",
  "....KPPK....",
  "....K..K....",
  "...K....K...",
  "....KKKK....",
);

const supervisorIdle = f(
  "....KKKK....",
  "...KRRRRK...",
  "..KRYAAAYK..",
  "..KRYWWAYK..",
  "..KRYAAAYK..",
  "...KRRRRK...",
  "..KRRRRRRK..",
  "..KR....RK..",
  "..KDD..DDK..",
  "..KK....KK..",
);

const supervisorWalk1 = f(
  "....KKKK....",
  "...KRRRRK...",
  "..KRYAAAYK..",
  "..KRYWWAYK..",
  "..KRYAAAYK..",
  "...KRRRRK...",
  "..KRRRRRRK..",
  "..KR....RK..",
  "..KDD....K..",
  "...KK...KK..",
  "....KKKK....",
);

const supervisorWalk2 = f(
  "....KKKK....",
  "...KRRRRK...",
  "..KRYAAAYK..",
  "..KRYWWAYK..",
  "..KRYAAAYK..",
  "...KRRRRK...",
  "..KRRRRRRK..",
  "..KR....RK..",
  "..K....DDK..",
  "..KK...KK...",
  "....KKKK....",
);

const megatronIdle = f(
  "....KKKK....",
  "...KRRRRK...",
  "..KRCWWCKK..",
  "..KRCWWCKK..",
  "..KRRRRRRK..",
  "...KRRRRK...",
  "..KRRRRRRK..",
  "..KR....RK..",
  "..KDD..DDK..",
  "..KK....KK..",
);

const hermesIdle = f(
  "....KKKK....",
  "...KGGGGK...",
  "..KGWWWWGK..",
  "..KGWBWBGK..",
  "..KGGGGGGK..",
  "..KGCCCCGK..",
  "..KG....GK..",
  "..KDD..DDK..",
  "..KK....KK..",
  "...KGGGK....",
);

const guardiaoIdle = f(
  "....KKKK....",
  "...KRRRRK...",
  "..KRYSSYRK..",
  "..KRYSSYRK..",
  "..KRRRRRRK..",
  "..KRRRRRRK..",
  "..KR....RK..",
  "..KDD..DDK..",
  "..KK....KK..",
);

const roteadorIdle = f(
  "....KKKK....",
  "...KOOOOK...",
  "..KOBBBOOK..",
  "..KOBBBBOK..",
  "..KOOBBBOOK.",
  "...KOOOOK...",
  "..KDD..DDK..",
  "..KK....KK..",
);

const memoriaIdle = f(
  "....KKKK....",
  "...KPPPPK...",
  "..KPWWWWPK..",
  "..KPWCCWPK..",
  "..KPWWWWPK..",
  "...KPPPPK...",
  "..KDD..DDK..",
  "..KK....KK..",
);

function walkFrom(idle: PixelFrame): [PixelFrame, PixelFrame] {
  const w1 = [...idle, "....KKKK...."];
  const w2 = [...idle, "..KK...KK..."];
  return [w1, w2];
}

const [megatronWalk1, megatronWalk2] = walkFrom(megatronIdle);
const [hermesWalk1, hermesWalk2] = walkFrom(hermesIdle);
const [guardiaoWalk1, guardiaoWalk2] = walkFrom(guardiaoIdle);
const [roteadorWalk1, roteadorWalk2] = walkFrom(roteadorIdle);
const [memoriaWalk1, memoriaWalk2] = walkFrom(memoriaIdle);

function thinkingVariant(base: PixelFrame): PixelFrame[] {
  const antenna = f(
    "...K.K.K....",
    "...K.K.K....",
    "...K.K.K....",
  );
  return [base, [...antenna, ...base]];
}

function executingVariant(base: PixelFrame): PixelFrame[] {
  const glow = f(
    "..KC..CK....",
    "..KC..CK....",
  );
  return [base, [...glow, ...base]];
}

function approvalVariant(base: PixelFrame): PixelFrame[] {
  const alert = f(
    "....KYK.....",
    "....KYK.....",
    "....KKK.....",
  );
  return [[...alert, ...base], base];
}

function doneVariant(base: PixelFrame): PixelFrame[] {
  const check = f(
    "....KGK.....",
    "...KG.GK....",
    "....KGK.....",
  );
  return [[...check, ...base], base];
}

function errorVariant(base: PixelFrame): PixelFrame[] {
  const xmark = f(
    "....KRK.....",
    "....KRK.....",
    "....KKK.....",
  );
  return [[...xmark, ...base], base];
}

function dangerVariant(base: PixelFrame): PixelFrame[] {
  const hazard = f(
    "..KRRRRK....",
    "..KRYKYK....",
    "..KRRRRK....",
  );
  return [[...hazard, ...base], base];
}

function mkSprite(
  id: string,
  name: string,
  scale: number,
  palette: ReturnType<typeof mergePalette>,
  idle: PixelFrame,
  walk1: PixelFrame,
  walk2: PixelFrame,
): PixelSpriteDefinition {
  return {
    id,
    name,
    scale,
    palette,
    frames: {
      idle: [idle, idle],
      walk1: [walk1],
      walk2: [walk2],
      thinking: thinkingVariant(idle),
      executing: executingVariant(idle),
      approval: approvalVariant(idle),
      done: doneVariant(idle),
      error: errorVariant(idle),
      danger: dangerVariant(idle),
    },
  };
}

const pietraBase = mkSprite(
  "pietra",
  "Pietra",
  3,
  mergePalette({ B: "#2563eb", Y: "#fde047" }),
  pietraIdle,
  pietraWalk1,
  pietraWalk2,
);
pietraBase.frames.idle = [pietraIdle, pietraIdle2];

export const AGENT_SPRITES: Record<string, PixelSpriteDefinition> = {
  megatron: mkSprite(
    "megatron",
    "MEGATRON",
    3,
    mergePalette({ R: "#991b1b", C: "#22d3ee" }),
    megatronIdle,
    megatronWalk1,
    megatronWalk2,
  ),
  hermes: mkSprite(
    "hermes",
    "Hermes",
    3,
    mergePalette({ G: "#15803d", W: "#ffffff", B: "#86efac" }),
    hermesIdle,
    hermesWalk1,
    hermesWalk2,
  ),
  pietra: pietraBase,
  arquivista: mkSprite(
    "arquivista",
    "Arquivista",
    3,
    mergePalette({ M: "#78350f", G: "#16a34a" }),
    arquivistaIdle,
    arquivistaWalk1,
    arquivistaWalk2,
  ),
  codex: mkSprite(
    "codex",
    "Codex",
    3,
    mergePalette({ C: "#06b6d4", G: "#4ade80" }),
    codexIdle,
    codexWalk1,
    codexWalk2,
  ),
  pesquisador: mkSprite(
    "pesquisador",
    "Pesquisador",
    3,
    mergePalette({ P: "#9333ea", C: "#22d3ee" }),
    pesquisadorIdle,
    pesquisadorWalk1,
    pesquisadorWalk2,
  ),
  supervisor: mkSprite(
    "supervisor",
    "Supervisor",
    3,
    mergePalette({ R: "#991b1b", A: "#ca8a04" }),
    supervisorIdle,
    supervisorWalk1,
    supervisorWalk2,
  ),
  guardiao: mkSprite(
    "guardiao",
    "Guardião",
    3,
    mergePalette({ R: "#dc2626", Y: "#eab308", S: "#64748b" }),
    guardiaoIdle,
    guardiaoWalk1,
    guardiaoWalk2,
  ),
  roteador: mkSprite(
    "roteador",
    "Roteador",
    3,
    mergePalette({ O: "#ea580c", B: "#2563eb" }),
    roteadorIdle,
    roteadorWalk1,
    roteadorWalk2,
  ),
  memoria: mkSprite(
    "memoria",
    "Memória",
    3,
    mergePalette({ P: "#7c3aed", C: "#22d3ee", W: "#e2e8f0" }),
    memoriaIdle,
    memoriaWalk1,
    memoriaWalk2,
  ),
};

export const DEFAULT_SPRITE = AGENT_SPRITES.codex;

export function getAgentSprite(agentId: string): PixelSpriteDefinition {
  return AGENT_SPRITES[agentId] ?? DEFAULT_SPRITE;
}
