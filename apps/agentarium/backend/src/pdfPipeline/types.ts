export type PdfDropEvent = {
  event_id: string;
  detected_at: string;
  status: string;
  source: string;
  source_pdf: string;
  file_name: string;
  size_bytes: number;
  sha256: string;
  target_agent: string;
  spec: string;
  next_action: string;
  safety?: {
    ocr_executed?: boolean;
    rag_reindexed?: boolean;
    content_copied?: boolean;
    requires_sensitive_data_gate?: boolean;
    requires_human_curation_before_rag?: boolean;
  };
  extraction?: {
    method?: string;
    pages?: number;
    chars?: number;
    output_gitignored?: string;
    rag_reindexed?: boolean;
  };
};

export type StirlingProbeStatus =
  | "online"
  | "auth_required"
  | "offline"
  | "unknown";

export type PdfPipelineSnapshot = {
  scannedAt: string;
  dropFolder: string;
  eventsFolder: string;
  pendingPdfCount: number;
  eventCount: number;
  events: PdfDropEvent[];
  stirling: {
    url: string;
    status: StirlingProbeStatus;
    detail: string;
  };
  blockers: string[];
  specPath: string;
};
