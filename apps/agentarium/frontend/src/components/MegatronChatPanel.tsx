import { useCallback, useEffect, useRef, useState } from "react";

type ChatLine = {
  id: string;
  role: "user" | "megatron" | "system";
  text: string;
  source?: string;
};

type Props = {
  apiBase: string;
  onIntakeCreated?: () => void;
};

export function MegatronChatPanel({ apiBase, onIntakeCreated }: Props) {
  const [lines, setLines] = useState<ChatLine[]>([]);
  const [iaStatus, setIaStatus] = useState<string>("verificando IA...");
  const [input, setInput] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const scrollRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight, behavior: "smooth" });
  }, [lines, busy]);

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  useEffect(() => {
    let cancelled = false;
    void (async () => {
      try {
        const res = await fetch(`${apiBase}/integrations/megatron/chat/status`);
        const body = (await res.json()) as {
          configured?: boolean;
          model?: string;
          conversationalEnabled?: boolean;
        };
        if (cancelled) return;
        const bootText = body.configured
          ? `MEGATRON pronto. OpenRouter ativo (${body.model ?? "modelo padrao"}). Prefixo tarefa: envia para a mesa de despacho.`
          : "MEGATRON pronto. OpenRouter nao detectado — modo local. Coloque a chave em .fabioos/secrets/openrouter_api_key.txt";
        setIaStatus(body.configured ? `OpenRouter · ${body.model ?? "?"}` : "modo local");
        setLines([
          { id: "boot", role: "system", text: bootText },
        ]);
      } catch {
        if (!cancelled) {
          setIaStatus("status indisponivel");
          setLines([
            {
              id: "boot",
              role: "system",
              text: "MEGATRON pronto. Nao foi possivel ler status da IA.",
            },
          ]);
        }
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [apiBase]);

  const send = useCallback(async () => {
    const text = input.trim();
    if (!text || busy) return;

    setInput("");
    setError(null);
    setBusy(true);
    const userId = `u-${Date.now()}`;
    setLines((prev) => [...prev, { id: userId, role: "user", text }]);

    try {
      const res = await fetch(`${apiBase}/integrations/megatron/chat`, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ message: text }),
      });
      const body = (await res.json()) as {
        ok?: boolean;
        reply?: string;
        error?: string;
        source?: string;
        model?: string;
      };
      if (!res.ok) {
        throw new Error(body.error ?? body.reply ?? `HTTP ${res.status}`);
      }
      const meta =
        body.source === "openrouter"
          ? body.model
            ? ` [${body.model}]`
            : " [openrouter]"
          : " [local]";
      setLines((prev) => [
        ...prev,
        {
          id: `m-${Date.now()}`,
          role: "megatron",
          text: body.reply ?? "(sem resposta)",
          source: `${body.source ?? "fallback"}${meta}`,
        },
      ]);
      if ((body as { intake?: { ok?: boolean } }).intake?.ok) {
        onIntakeCreated?.();
      }
    } catch (e) {
      const msg = e instanceof Error ? e.message : "Falha no chat";
      setError(msg);
      setLines((prev) => [
        ...prev,
        { id: `e-${Date.now()}`, role: "system", text: `Erro: ${msg}` },
      ]);
    } finally {
      setBusy(false);
      inputRef.current?.focus();
    }
  }, [apiBase, busy, input, onIntakeCreated]);

  return (
    <section className="megatron-chat">
      <div className="megatron-chat__status pixel-label">{iaStatus}</div>
      <div className="megatron-chat__screen pixel-border" ref={scrollRef}>
        {lines.map((line) => (
          <div key={line.id} className={`megatron-chat__line megatron-chat__line--${line.role}`}>
            {line.role === "user" && <span className="megatron-chat__prompt">fabio&gt; </span>}
            {line.role === "megatron" && <span className="megatron-chat__prompt">megatron&gt; </span>}
            {line.role === "system" && <span className="megatron-chat__prompt">--- </span>}
            <span className="megatron-chat__text">{line.text}</span>
            {line.source && <span className="megatron-chat__meta">{line.source}</span>}
          </div>
        ))}
        {busy && (
          <div className="megatron-chat__line megatron-chat__line--megatron">
            <span className="megatron-chat__prompt">megatron&gt; </span>
            <span className="megatron-chat__text megatron-chat__blink">...</span>
          </div>
        )}
      </div>

      <form
        className="megatron-chat__input-row pixel-border"
        onSubmit={(e) => {
          e.preventDefault();
          void send();
        }}
      >
        <label className="megatron-chat__prompt" htmlFor="megatron-cmd-input">
          fabio&gt;
        </label>
        <input
          id="megatron-cmd-input"
          ref={inputRef}
          className="megatron-chat__input"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          disabled={busy}
          placeholder="fale com o MEGATRON... (tarefa: ... para despacho)"
          autoComplete="off"
          spellCheck={false}
        />
        <button type="submit" className="btn btn-tactical pixel-button" disabled={busy || !input.trim()}>
          Enter
        </button>
      </form>

      {error && <p className="megatron-chat__error">{error}</p>}
    </section>
  );
}
