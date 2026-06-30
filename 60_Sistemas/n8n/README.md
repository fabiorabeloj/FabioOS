---
tipo: sistema
area: 60_Sistemas
projeto: FabioOS
sistema: n8n
status: ativo
tags: [n8n, automação, docker, workflows]
criado_em: 2026-06-26
atualizado_em: 2026-06-26
---

# n8n no FabioOS

## Acesso

- **UI:** http://localhost:5678
- **API:** http://localhost:5678/api/v1/

## Comandos Docker

```powershell
# Verificar status
docker ps --filter "name=n8n"

# Iniciar (se parado)
docker start n8n

# Parar
docker stop n8n

# Ver logs em tempo real
docker logs n8n -f

# Reiniciar com vault montado (necessário para workflows que escrevem no vault diretamente)
docker stop n8n
docker run -d --name n8n -p 5678:5678 `
  -v n8n_data:/home/node/.n8n `
  -v "C:\Users\user\Desktop\FabioOs\FabioOs:/vault" `
  docker.n8n.io/n8nio/n8n
```

## Como importar um workflow

1. Abrir http://localhost:5678
2. Menu lateral → **Workflows**
3. Botão **Import** → selecionar o arquivo `.json` de `60_Sistemas/n8n/Workflows/`
4. Configurar credenciais necessárias (ver doc do workflow)
5. Ativar o workflow (toggle no canto superior)

## Configurar credencial Obsidian API

Para workflows que escrevem no vault via Obsidian REST API:

1. No n8n: **Credentials** → **Add Credential**
2. Tipo: **HTTP Header Auth**
3. Name: `Obsidian API Token`
4. Header Name: `Authorization`
5. Header Value: `Bearer [SEU_TOKEN_OBSIDIAN]`
6. Salvar

O token do Obsidian fica em: Obsidian → Settings → Community Plugins → Local REST API.

## Integração via Obsidian REST API

O n8n acessa o vault do Obsidian via REST API na porta 27124.

Da perspectiva do Docker, o host é `host.docker.internal` (não `localhost`):

```
URL base: https://host.docker.internal:27124
Endpoint para criar nota: PUT /vault/{caminho-relativo-ao-vault}
Header: Authorization: Bearer {token}
SSL: skip verification (certificado auto-assinado)
```

## Padrão de documentação de workflows

Todo workflow criado no FabioOS deve ter uma nota em `60_Sistemas/n8n/Workflows/` seguindo o padrão do 60_Sistemas/FabioOS/bootstrap/CLAUDE.md:

- Nome do workflow
- Objetivo
- Gatilho
- Entrada esperada
- Processamento
- Saída
- Integrações
- Riscos
- Teste mínimo
- Próxima melhoria

## Workflows disponíveis

| Arquivo | Status | Função |
|---|---|---|
| `FabioOS_Webhook_Inbox.json` | pronto para importar | Webhook → nota em 05_Raw_Sources/_compat_sources/_inbox/ |

## Relações

- [[40_Wiki/_compat_wiki/sistemas/n8n]]
- [[60_Sistemas/FabioOS/Plano_Mestre_Implantacao_FabioOS]]
- [[60_Sistemas/FabioOS/Protocolo_Operacional_FabioOS]]
