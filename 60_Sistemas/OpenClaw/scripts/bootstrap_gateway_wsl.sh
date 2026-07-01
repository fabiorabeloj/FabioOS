#!/usr/bin/env bash
# Bootstrap gateway OpenClaw em uma unica sessao WSL (evita stop/start externo).
set -euo pipefail

PORT=18789
MAX_WAIT="${MAX_WAIT:-120}"
FORCE="${FORCE_RESTART:-0}"

if [ "$FORCE" != "1" ]; then
  if ss -tlnp 2>/dev/null | grep -q ":${PORT}"; then
    code=$(curl -s -o /dev/null -w "%{http_code}" "http://127.0.0.1:${PORT}/" || echo "000")
    if [ "$code" = "200" ]; then
      ip=$(hostname -I | awk '{print $1}')
      echo "OK already_running HTTP=${code} wsl_ip=${ip}"
      exit 0
    fi
  fi
fi

systemctl --user stop openclaw-gateway.service 2>/dev/null || true
sleep 2
systemctl --user start openclaw-gateway.service

elapsed=0
while [ "$elapsed" -lt "$MAX_WAIT" ]; do
  if ss -tlnp 2>/dev/null | grep -q ":${PORT}"; then
    code=$(curl -s -o /dev/null -w "%{http_code}" "http://127.0.0.1:${PORT}/" || echo "000")
    echo "LISTEN elapsed=${elapsed}s HTTP=${code}"
    if [ "$code" = "200" ]; then
      ip=$(hostname -I | awk '{print $1}')
      echo "Holding session 45s for linger persistence..."
      sleep 45
      code2=$(curl -s -o /dev/null -w "%{http_code}" "http://127.0.0.1:${PORT}/" || echo "000")
      echo "OK gateway=${code2} wsl_ip=${ip}"
      exit 0
    fi
  else
    echo "wait elapsed=${elapsed}s (no listener yet)"
  fi
  sleep 5
  elapsed=$((elapsed + 5))
done

echo "FAIL gateway nao respondeu em ${MAX_WAIT}s"
journalctl --user -u openclaw-gateway.service -n 15 --no-pager || true
exit 1
