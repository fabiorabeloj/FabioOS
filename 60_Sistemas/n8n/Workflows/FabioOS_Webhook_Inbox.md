---
tipo: sistema
area: 60_Sistemas
projeto: FabioOS
sistema: n8n
workflow: FabioOS_Webhook_Inbox
status: pronto-para-importar
tags: [n8n, workflow, webhook, inbox, automação]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# Workflow: FabioOS — Webhook para Inbox

## Nome do workflow

`FabioOS - Webhook para Inbox`

## Objetivo

Receber uma mensagem via webhook HTTP POST e criar automaticamente uma nota em `05_Raw_Sources/_compat_sources/_inbox/` do vault, pronta para triagem pelo protocolo operacional do FabioOS.

**Critério de sucesso da Fase 10:**
> Um webhook gera uma nota no FabioOS.

## Gatilho

- **Tipo:** Webhook (HTTP POST)
- **Endpoint:** `http://localhost:5678/webhook/fabios-inbox`
- **Método:** POST
- **Content-Type:** `application/json`

## Entrada esperada

```json
{
  "titulo": "Título da nota",
  "conteudo": "Conteúdo em Markdown ou texto simples",
  "tipo": "texto",
  "origem": "webhook"
}
```

| Campo | Obrigatório | Padrão | Valores possíveis |
|---|---|---|---|
| `titulo` | Sim | — | texto livre |
| `conteudo` | Sim | — | texto / markdown |
| `tipo` | Não | `texto` | `texto`, `ideia`, `link`, `email`, `mensagem`, `decisão` |
| `origem` | Não | `webhook` | `webhook`, `pietra`, `n8n`, `manual` |

## Processamento (nós)

```
[Webhook] → [Gerar Nota] → [Salvar no Vault] → [Responder]
```

### Nó 1: Webhook
- Recebe o POST e passa o body para o próximo nó.

### Nó 2: Gerar Nota (Code)
- Gera o `filename` no padrão `YYYY-MM-DD_slug.md`
- Remove acentos e caracteres especiais do slug
- Monta o frontmatter YAML completo
- Retorna: `{filename, markdown, titulo, hoje}`

**Lógica do slug:**
```javascript
slug = titulo
  .toLowerCase()
  .normalize('NFD').replace(/[̀-ͯ]/g, '') // remove acentos
  .replace(/[^a-z0-9]+/g, '-')
  .replace(/^-|-$/g, '')
  .substring(0, 60);
filename = `${hoje}_${slug}.md`
```

### Nó 3: Salvar no Vault (HTTP Request)
- Método: `PUT`
- URL: `https://host.docker.internal:27124/vault/05_Raw_Sources/_compat_sources/_inbox/{filename}`
- Header: `Authorization: Bearer {OBSIDIAN_TOKEN}`
- Body: conteúdo markdown gerado
- SSL: verificação ignorada (certificado auto-assinado)

### Nó 4: Responder
- Retorna JSON confirmando o nome do arquivo criado

## Saída

**HTTP 200 — Sucesso:**
```json
{
  "status": "ok",
  "arquivo": "2026-06-26_titulo-da-nota.md",
  "mensagem": "Nota criada em 05_Raw_Sources/_compat_sources/_inbox/"
}
```

**HTTP 500 — Erro:**
```json
{
  "status": "erro",
  "mensagem": "Falha ao salvar no vault"
}
```

O arquivo criado no vault terá este formato:
```markdown
---
tipo: fonte
origem: webhook
status: bruto
tags: [inbox, texto]
capturado_em: 2026-06-26
---

# Título da nota

Conteúdo em Markdown ou texto simples
```

## Integrações

| Sistema | Como | Configuração |
|---|---|---|
| **n8n** | Executa o workflow | Docker, porta 5678 |
| **Obsidian REST API** | Recebe o arquivo criado | Porta 27124, token necessário |
| **Claude Code** | Pode acionar o webhook com Bash | `curl -X POST ...` |

## Como configurar e ativar

### Pré-requisito: credencial Obsidian

1. No Obsidian: Settings → Community Plugins → Local REST API → copiar o token
2. No n8n: Credentials → Add → **HTTP Header Auth**
   - Name: `Obsidian API Token`
   - Header Name: `Authorization`
   - Header Value: `Bearer [TOKEN_COPIADO]`
3. No workflow importado: abrir nó "Salvar no Vault" → selecionar a credencial criada

### Importar o workflow

1. n8n → Workflows → Import
2. Selecionar: `60_Sistemas/n8n/Workflows/FabioOS_Webhook_Inbox.json`
3. Configurar credencial no nó "Salvar no Vault"
4. Ativar o workflow (toggle no canto superior)

## Teste mínimo

```bash
curl -X POST http://localhost:5678/webhook/fabios-inbox \
  -H "Content-Type: application/json" \
  -d "{\"titulo\": \"Teste Fase 10\", \"conteudo\": \"Primeira nota criada via webhook do FabioOS.\", \"tipo\": \"texto\", \"origem\": \"webhook\"}"
```

**Resultado esperado:**
- Resposta JSON com `status: ok` e nome do arquivo
- Arquivo `05_Raw_Sources/_compat_sources/_inbox/2026-06-26_teste-fase-10.md` criado no vault

## Riscos

| Risco | Mitigação |
|---|---|
| n8n Docker parado | `docker start n8n` antes de acionar |
| Obsidian fechado | A API REST do Obsidian só funciona com o app aberto |
| Token inválido | Verificar em Settings → Local REST API |
| SSL do Obsidian | Nó configurado com `allowUnauthorizedCerts: true` |
| Conteúdo malicioso via webhook | Tratar como fonte bruta — triagem obrigatória em `_inbox/` |

## Próxima melhoria

- Adicionar nó de validação dos campos obrigatórios antes de processar
- Adicionar classificação automática por `tipo` → destino correto (não apenas `_inbox/`)
- Criar versão com autenticação no webhook (evitar chamadas não autorizadas)
- Workflow Pietra: mensagem WhatsApp → webhook → classificação → resposta sugerida

## Relações

- [[60_Sistemas/n8n/README]]
- [[40_Wiki/_compat_wiki/sistemas/n8n]]
- [[05_Raw_Sources/_compat_sources/README]]
- [[60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS]]
