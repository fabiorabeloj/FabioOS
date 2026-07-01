$ErrorActionPreference = "Stop"
Invoke-RestMethod -Uri "http://127.0.0.1:3847/integrations/whatsapp/status" | ConvertTo-Json -Depth 6
