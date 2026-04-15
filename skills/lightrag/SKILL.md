---
name: lightrag
description: >
  Use this skill whenever the user wants to build a Retrieval-Augmented Generation (RAG) system that understands relationships between concepts, not just keyword or semantic similarity. Trigger on any mention of LightRAG, knowledge graph RAG, graph-based retrieval, entity-relationship extraction from documents, or building a Q&A system over a document corpus. Also use when the user wants to go beyond naive RAG (simple vector search) and needs more structured, relationship-aware retrieval — for example, "I want to ask questions across many documents and get answers that understand how concepts relate," or "build a knowledge base from my files."
---

# LightRAG Skill

This skill helps you use **LightRAG** — a Retrieval-Augmented Generation framework (published at EMNLP 2025) that combines knowledge graph technology with traditional vector search. Unlike naive RAG (which just finds similar chunks), LightRAG automatically extracts entities and relationships from your documents and builds a structured knowledge graph, enabling richer, more accurate answers to complex questions.

**When LightRAG shines over basic RAG:**
- Questions that require understanding *relationships* between concepts (not just finding similar text)
- Multi-document corpora where connections across documents matter
- Domain-specific Q&A where structure and reasoning chains improve accuracy
- When you need source attribution / citations in answers

## Installation

```bash
# From PyPI
pip install lightrag-hku

# With API server
pip install "lightrag-hku[api]"

# From source
git clone https://github.com/HKUDS/LightRAG.git
cd LightRAG
pip install -e .
```

**Recommended models:**
- LLM: 32B+ parameters, 32K+ context (e.g., GPT-4o, Claude 3.5, Llama 3 70B)
- Embeddings: `BAAI/bge-m3` or `text-embedding-3-large`
- Reranker (optional but improves quality): `BAAI/bge-reranker-v2-m3`

## Quick Start

```python
import asyncio
from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed

async def main():
    # Initialize with your LLM and embedding functions
    rag = LightRAG(
        working_dir="./my_rag_storage",
        llm_model_func=gpt_4o_mini_complete,
        embedding_func=openai_embed,
    )

    # Insert documents
    with open("my_document.txt") as f:
        await rag.ainsert(f.read())

    # Query using different modes
    result = await rag.aquery(
        "What is the relationship between X and Y?",
        param=QueryParam(mode="hybrid")
    )
    print(result)

asyncio.run(main())
```

## Inserting Documents

```python
# Single document
await rag.ainsert("Your document text here...")

# Multiple documents
texts = [open(f).read() for f in ["doc1.txt", "doc2.txt", "doc3.txt"]]
await rag.ainsert(texts)

# Delete a document (updates the knowledge graph automatically)
await rag.adelete_by_doc_id("doc_id_here")
```

LightRAG automatically:
1. Chunks the text
2. Extracts entities (people, places, concepts, etc.)
3. Extracts relationships between entities
4. Stores everything in both a vector index and a knowledge graph

## Query Modes

LightRAG offers 4 retrieval modes — choose based on your question type:

| Mode | Best For | Description |
|------|----------|-------------|
| `naive` | Simple factual lookup | Traditional chunk-based vector search |
| `local` | Entity-specific questions | Focuses on directly relevant entities and their immediate context |
| `global` | High-level, thematic questions | Uses the full knowledge graph for broad understanding |
| `hybrid` | Most questions (recommended) | Combines local + global for comprehensive answers |

```python
# Recommended: hybrid mode
result = await rag.aquery(
    "How does concept A influence concept B across different domains?",
    param=QueryParam(mode="hybrid")
)

# With citations
result = await rag.aquery(
    "What are the main findings?",
    param=QueryParam(mode="hybrid", return_citations=True)
)
```

## REST API Server

Run LightRAG as a server with a web UI:

```bash
# Start the server
lightrag-server --working-dir ./storage --port 8000

# Or with Docker
docker run -p 8000:8000 -v ./storage:/app/storage lightrag-hku/lightrag
```

The server exposes REST endpoints and a built-in web UI for document management and querying.

```python
# Python client for the server
import requests

# Insert document
requests.post("http://localhost:8000/documents", json={"text": "Your content..."})

# Query
result = requests.post("http://localhost:8000/query", json={
    "query": "Your question",
    "mode": "hybrid"
})
print(result.json()["response"])
```

## Storage Backends

LightRAG supports multiple backends for production deployments:

```python
from lightrag.storage import PostgreSQLStorage, Neo4jStorage

# PostgreSQL (vector + graph)
rag = LightRAG(
    working_dir="./storage",
    storage_backend=PostgreSQLStorage(
        connection_string="postgresql://user:pass@localhost/rag_db"
    ),
    llm_model_func=gpt_4o_mini_complete,
    embedding_func=openai_embed,
)
```

| Backend | Best For |
|---------|----------|
| Default (file-based) | Development and small corpora |
| PostgreSQL | Production, SQL integration |
| MongoDB | Document-heavy workloads |
| Neo4j | When you need to query the graph directly |
| OpenSearch | Large-scale deployments |

## Using with Claude / Anthropic

```python
from lightrag.llm.anthropic import claude_complete, anthropic_embed

rag = LightRAG(
    working_dir="./storage",
    llm_model_func=claude_complete,        # Claude for generation
    embedding_func=anthropic_embed,        # Anthropic embeddings
)
```

## Evaluation with RAGAS

```python
from lightrag.eval import evaluate_with_ragas

scores = await evaluate_with_ragas(
    rag=rag,
    questions=["Q1", "Q2"],
    ground_truths=["A1", "A2"],
)
print(scores)  # faithfulness, answer_relevancy, context_precision, etc.
```

## Observability with Langfuse

```python
from lightrag.observability import LangfuseObserver

rag = LightRAG(
    working_dir="./storage",
    llm_model_func=gpt_4o_mini_complete,
    embedding_func=openai_embed,
    observer=LangfuseObserver(public_key="...", secret_key="..."),
)
```

## Complete Working Example

```python
import asyncio
from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed

async def build_knowledge_base():
    rag = LightRAG(
        working_dir="./research_kb",
        llm_model_func=gpt_4o_mini_complete,
        embedding_func=openai_embed,
    )

    # Load research papers
    import glob
    for filepath in glob.glob("./papers/*.txt"):
        with open(filepath) as f:
            await rag.ainsert(f.read())
        print(f"Indexed {filepath}")

    # Ask cross-document questions
    questions = [
        "What methods are most commonly used across these papers?",
        "How do the findings in paper A relate to the conclusions of paper B?",
        "What are the open problems identified across all papers?",
    ]
    for q in questions:
        result = await rag.aquery(q, param=QueryParam(mode="hybrid"))
        print(f"\nQ: {q}\nA: {result}\n")

asyncio.run(build_knowledge_base())
```

## Source: [github.com/hkuds/lightrag](https://github.com/hkuds/lightrag)
