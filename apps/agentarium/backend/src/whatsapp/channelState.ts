import type { WhatsAppChannel } from "./config.js";

type ChannelSnapshot = {
  lastMessageAt: string | null;
  lastJobId: string | null;
  lastEventAt: string | null;
  connected: boolean;
};

class ChannelStateStore {
  private state: Record<WhatsAppChannel, ChannelSnapshot> = {
    personal: { lastMessageAt: null, lastJobId: null, lastEventAt: null, connected: false },
    school: { lastMessageAt: null, lastJobId: null, lastEventAt: null, connected: false },
  };

  recordMessage(channel: WhatsAppChannel, jobId: string): void {
    const now = new Date().toISOString();
    this.state[channel] = {
      ...this.state[channel],
      lastMessageAt: now,
      lastJobId: jobId,
      lastEventAt: now,
      connected: true,
    };
  }

  setConnected(channel: WhatsAppChannel, connected: boolean): void {
    this.state[channel].connected = connected;
  }

  get(channel: WhatsAppChannel): ChannelSnapshot {
    return { ...this.state[channel] };
  }

  all(): Record<WhatsAppChannel, ChannelSnapshot> {
    return {
      personal: this.get("personal"),
      school: this.get("school"),
    };
  }
}

export const channelState = new ChannelStateStore();
