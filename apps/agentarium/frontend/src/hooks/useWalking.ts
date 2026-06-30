import { useEffect, useRef, useState } from "react";

const WALK_MS = 800;

export function useWalking(zone: string): boolean {
  const prev = useRef(zone);
  const [walking, setWalking] = useState(false);

  useEffect(() => {
    if (prev.current !== zone) {
      setWalking(true);
      const t = window.setTimeout(() => setWalking(false), WALK_MS);
      prev.current = zone;
      return () => window.clearTimeout(t);
    }
  }, [zone]);

  return walking;
}

export function useWalkPhase(isWalking: boolean, intervalMs = 220): 0 | 1 {
  const [phase, setPhase] = useState<0 | 1>(0);

  useEffect(() => {
    if (!isWalking) {
      setPhase(0);
      return;
    }
    const id = window.setInterval(() => {
      setPhase((p) => (p === 0 ? 1 : 0));
    }, intervalMs);
    return () => window.clearInterval(id);
  }, [isWalking, intervalMs]);

  return phase;
}
