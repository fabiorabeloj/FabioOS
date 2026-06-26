---
name: project-llmwiki-architecture
description: "FabioOS adopts LLM-Wiki 3-layer architecture — sources/wiki/schema inside the vault, repos outside"
metadata: 
  node_type: memory
  type: project
  originSessionId: bdbd4240-a9f3-4d7d-a892-ac2b9b0c9003
---

FabioOS vault will follow Karpathy LLM-Wiki pattern with 3 layers inside the vault root:

- **sources/**: raw inputs — repo summaries, articles, PDFs, transcribed notes, reference materials
- **wiki/**: AI-generated/organized pages — entities, concepts, syntheses, indices, connected pages
- **schema/**: rules, conventions, templates, categories, ingestion instructions, maintenance patterns

**Why:** Separates raw knowledge from organized knowledge and structural rules. Obsidian is just the interface; wiki/ becomes the official knowledge source for FabioOS.

**How to apply:**
- Technical repos with .git/node_modules go to `C:\Users\user\claude-extensions\` (outside vault)
- For every cloned repo, create a source note in `sources/repositorios/` inside the vault
- New documentation → prefer `sources/` or `wiki/` over `60_Sistemas/` going forward
- Do NOT migrate the entire vault now; build the 3-layer structure incrementally
- The migration to wiki/ as primary structure is approved for the FUTURE, not now

**Project-level .claude/ locations (inside vault):**
- Skills: `C:\Users\user\Desktop\FabioOs\FabioOs\.claude\skills\`
- Commands: `.claude\commands\`
- Hooks: `.claude\hooks\`
- Agents: `.claude\agents\`
- Subagents: `.claude\subagents\`

Note: Current skills were installed globally (`~/.claude/skills/`). Project-level vs global discrepancy is flagged; no move without user confirmation.
