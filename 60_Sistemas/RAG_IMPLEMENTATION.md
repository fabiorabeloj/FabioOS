---
tipo: automação
area: tecnologia
status: planejamento
tags: [tecnico, RAG, banco-vetorial, IA, implementacao]
criado_em: 2026-06-25
atualizado_em: 2026-06-25
---

# RAG Implementation — Guia prático

## O que vamos fazer?

Implementar um sistema completo de RAG (Retrieval-Augmented Generation) que:
1. Lê todos os arquivos .md do FabioOS
2. Cria embeddings (vetores) usando OpenAI/local
3. Armazena em banco vetorial (Chroma)
4. Permite buscas semânticas
5. Integra com Claude para respostas contextualizadas

## Arquitetura

```
Arquivos .md (Obsidian)
    ↓ [Read & Parse]
Chunks de texto
    ↓ [Embedding]
Vetores + Metadados
    ↓ [Store]
Chroma DB (local)
    ↓ [Query + Retrieve]
Top-K docs similares
    ↓ [Pass to Claude]
Resposta contextualizada
```

## Escolha: Chroma vs Alternativas

| Sistema | Instalação | Velocidade | Custo | Recomendação |
|---------|-----------|-----------|-------|--------------|
| **Chroma** | pip install | Rápida | Grátis | ⭐⭐⭐⭐⭐ |
| Qdrant | Docker | Muito rápida | Grátis | ⭐⭐⭐⭐ |
| Weaviate | Docker | Rápida | Grátis | ⭐⭐⭐⭐ |
| Pinecone | Cloud | Rápida | Pago | ⭐⭐⭐ |

**Escolhido: Chroma** (mais simples, local, grátis)

---

## Fase 1: Setup básico

### Passo 1: Instalar dependências

```bash
pip install chroma-db openai langchain python-dotenv
```

### Passo 2: Criar arquivo .env

```env
OPENAI_API_KEY=sk-...
# ou usar local embeddings (sem custo)
USE_LOCAL_EMBEDDINGS=true
```

### Passo 3: Script de ingestão

Criar `scripts/ingest_obsidian.py`:

```python
#!/usr/bin/env python3
import os
from pathlib import Path
import chromadb
from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
import dotenv

dotenv.load_dotenv()

# Configuração
VAULT_PATH = Path("./FabioOs")
DB_PATH = "./fabioos_db"
USE_LOCAL = os.getenv("USE_LOCAL_EMBEDDINGS", "true").lower() == "true"

def load_markdown_files():
    """Carrega todos os .md do vault."""
    documents = []
    
    for md_file in VAULT_PATH.rglob("*.md"):
        # Skip especiais
        if md_file.name.startswith(".") or "RELATORIO" in md_file.name:
            continue
            
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            documents.append({
                "path": str(md_file.relative_to(VAULT_PATH)),
                "content": content,
                "filename": md_file.stem
            })
    
    return documents

def split_markdown(doc):
    """Divide markdown em chunks por headers."""
    splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]
    )
    
    splits = splitter.split_text(doc["content"])
    
    for split in splits:
        split["metadata"]["source"] = doc["path"]
        split["metadata"]["filename"] = doc["filename"]
    
    return splits

def ingest_to_chroma():
    """Ingere documentos no Chroma."""
    # Inicializar embeddings
    if USE_LOCAL:
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        print("✓ Usando embeddings local (grátis)")
    else:
        embeddings = OpenAIEmbeddings()
        print("✓ Usando OpenAI embeddings")
    
    # Inicializar Chroma
    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_or_create_collection(
        name="fabioos",
        metadata={"hnsw:space": "cosine"}
    )
    
    # Carregar documentos
    print("\n📖 Carregando documentos...")
    docs = load_markdown_files()
    print(f"   Encontrados {len(docs)} arquivos")
    
    # Processar
    print("\n✂️  Dividindo em chunks...")
    all_chunks = []
    for doc in docs:
        chunks = split_markdown(doc)
        all_chunks.extend(chunks)
    print(f"   Total: {len(all_chunks)} chunks")
    
    # Adicionar ao Chroma
    print("\n📊 Adicionando ao banco vetorial...")
    for i, chunk in enumerate(all_chunks):
        if (i + 1) % 10 == 0:
            print(f"   {i + 1}/{len(all_chunks)}...")
        
        collection.add(
            ids=[f"chunk_{i}"],
            documents=[chunk["page_content"]],
            metadatas=[chunk["metadata"]]
        )
    
    print(f"\n✅ Ingestão completa! {len(all_chunks)} documentos no banco.")

if __name__ == "__main__":
    ingest_to_chroma()
```

### Passo 4: Executar ingestão

```bash
python scripts/ingest_obsidian.py
```

---

## Fase 2: Buscas semânticas

### Script de consulta

Criar `scripts/query_rag.py`:

```python
#!/usr/bin/env python3
import os
import chromadb
from langchain.embeddings import HuggingFaceEmbeddings

DB_PATH = "./fabioos_db"

def query(question: str, top_k: int = 5):
    """Busca semântica no FabioOS."""
    
    # Conectar ao banco
    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_collection("fabioos")
    
    # Buscar
    results = collection.query(
        query_texts=[question],
        n_results=top_k
    )
    
    print(f"\n🔍 Busca: '{question}'")
    print(f"   Encontrados {len(results['documents'][0])} resultados\n")
    
    for i, (doc, metadata) in enumerate(
        zip(results['documents'][0], results['metadatas'][0]), 1
    ):
        print(f"[{i}] 📄 {metadata['source']}")
        print(f"    {doc[:200]}...")
        print()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python query_rag.py '<sua pergunta>'")
        sys.exit(1)
    
    question = " ".join(sys.argv[1:])
    query(question)
```

### Teste:

```bash
python scripts/query_rag.py "O que é FabioOS?"
python scripts/query_rag.py "Como funciona automação?"
python scripts/query_rag.py "Quais são os projetos ativos?"
```

---

## Fase 3: Integração com Claude

### Script RAG + Claude

Criar `scripts/rag_claude.py`:

```python
#!/usr/bin/env python3
import os
import chromadb
from anthropic import Anthropic

DB_PATH = "./fabioos_db"

def rag_query(question: str, top_k: int = 3):
    """RAG + Claude para respostas contextualizadas."""
    
    # Conectar ao Chroma
    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_collection("fabioos")
    
    # Buscar documentos relevantes
    results = collection.query(
        query_texts=[question],
        n_results=top_k
    )
    
    # Preparar contexto
    context = "Documentos do FabioOS relevantes:\n\n"
    for i, (doc, meta) in enumerate(
        zip(results['documents'][0], results['metadatas'][0]), 1
    ):
        context += f"[{i}] De {meta['source']}:\n{doc}\n\n"
    
    # Claude
    claude = Anthropic()
    
    response = claude.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        system="""Você é assistente do FabioOS. Responda baseado no contexto fornecido.
Se a informação não estiver no contexto, diga que não encontrou.
Cite as fontes (documentos) que usou.""",
        messages=[
            {
                "role": "user",
                "content": f"{context}\n\nPergunta: {question}"
            }
        ]
    )
    
    print(f"\n🤖 Pergunta: {question}")
    print(f"\n{response.content[0].text}")

if __name__ == "__main__":
    import sys
    question = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "O que é RAG?"
    rag_query(question)
```

---

## Integração com n8n

### Webhook n8n

1. Criar workflow: "RAG Query"
2. Trigger: Webhook HTTP POST
3. Body JSON:

```json
{
  "question": "Sua pergunta aqui",
  "top_k": 3
}
```

4. Nó: Executar Python script
5. Output: Resposta do Claude

---

## Checklist de implementação

### Fase 1 (Hoje)
- [ ] Instalar Chroma
- [ ] Criar script `ingest_obsidian.py`
- [ ] Rodar ingestão primeira vez
- [ ] Validar banco criado em `./fabioos_db`

### Fase 2 (Esta semana)
- [ ] Criar script `query_rag.py`
- [ ] Testar 10 buscas diferentes
- [ ] Documentar queries interessantes
- [ ] Otimizar chunk size

### Fase 3 (Próxima semana)
- [ ] Integrar Claude
- [ ] Criar webhook n8n
- [ ] Testar respostas completas
- [ ] Deploy em produção

### Fase 4 (Futuro)
- [ ] UI web para chatbot
- [ ] Histórico de conversas
- [ ] Analytics de buscas
- [ ] Fine-tuning de embeddings

---

## Troubleshooting

| Problema | Solução |
|----------|---------|
| "Module not found" | Verificar `pip install` de todas dependências |
| Embeddings lentos | Usar local (`all-MiniLM`) em vez de OpenAI |
| Poucos resultados | Aumentar `top_k` ou revisar chunk size |
| Muitos resultados irrelevantes | Verificar qualidade dos chunks |

---

**Status:** 🟡 Pronto para implementar  
**Esforço:** 4-6 horas  
**ROI:** Muito alto (busca inteligente no vault)

## Referências

- [Chroma Docs](https://docs.trychroma.com/)
- [LangChain RAG](https://python.langchain.com/docs/use_cases/question_answering/)
- [[RAG]] — conceito
- [[Banco_Vetorial]] — arquitetura
