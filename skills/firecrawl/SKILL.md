---
name: firecrawl
description: >
  Use this skill whenever the user wants to scrape websites, extract structured data from web pages, crawl entire websites, search the web and get full page content, or use an AI agent to gather data from the web. Trigger on any mention of Firecrawl, web scraping, crawling websites, extracting web data into markdown or JSON, batch URL scraping, competitor research via scraping, or turning websites into clean text for AI use. Also trigger when the user wants to build a dataset from web content or needs to monitor changes on websites.
---

# Firecrawl Skill

This skill helps you use **Firecrawl** — a web data API that turns websites into clean, structured data for AI applications. It handles JavaScript rendering, proxy rotation, rate limiting, and bot detection automatically, so you just call an API and get back markdown, HTML, screenshots, or structured JSON.

> **Prerequisites**: You need a Firecrawl API key from [firecrawl.dev](https://firecrawl.dev). Set it as `FIRECRAWL_API_KEY` in your environment.

## Installation

```bash
# Python
pip install firecrawl-py

# Node.js
npm install @mendable/firecrawl-js

# CLI
npm install -g firecrawl
```

## Quick Start

```python
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR_API_KEY")
# Or set FIRECRAWL_API_KEY env var and just do: app = Firecrawl()

result = app.scrape("https://example.com")
print(result['markdown'])  # Clean markdown of the page
```

## Core Operations

### 1. Scrape a Single URL

Converts a URL to markdown, HTML, screenshot, or structured JSON.

```python
# Basic scrape → markdown
result = app.scrape("https://example.com")
print(result['markdown'])

# Get multiple formats at once
result = app.scrape("https://example.com", formats=["markdown", "html", "screenshot"])

# Structured extraction with a schema
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    in_stock: bool

result = app.scrape("https://shop.example.com/item", schema=Product)
print(result['data'])  # → {"name": "Widget", "price": 29.99, "in_stock": True}
```

**CLI:**
```bash
firecrawl scrape https://example.com
firecrawl scrape https://example.com --format markdown
```

### 2. Crawl an Entire Website

Recursively crawls all pages under a domain.

```python
# Start a crawl
job = app.crawl_url("https://docs.example.com", max_depth=3, limit=100)

# Check status / get results (async job)
results = app.check_crawl_status(job['id'])
for page in results['data']:
    print(page['url'], page['markdown'])
```

**CLI:**
```bash
firecrawl crawl https://docs.example.com --max-depth 3 --limit 100
```

### 3. Batch Scrape Multiple URLs

Efficiently scrape thousands of URLs in one call.

```python
urls = [
    "https://site.com/page-1",
    "https://site.com/page-2",
    "https://site.com/page-3",
]
results = app.batch_scrape(urls)
for r in results['data']:
    print(r['url'], r['markdown'][:200])
```

### 4. Search the Web

Search and get full page content from results (not just snippets).

```python
results = app.search("best Python web frameworks 2025")
for r in results['data']:
    print(r['url'])
    print(r['markdown'][:500])   # Full page content, not a snippet
```

**CLI:**
```bash
firecrawl search "best Python web frameworks 2025"
```

### 5. Agent Mode (Natural Language)

The most powerful feature — describe what you want in plain English, no URLs needed.

```python
result = app.agent("Find the pricing plans for Linear project management tool")
print(result['data'])
```

```bash
firecrawl agent "Find the pricing plans for Linear"
```

### 6. Web Interaction Before Scraping

Handle dynamic pages: click buttons, scroll, fill forms, then extract.

```python
result = app.scrape("https://example.com/dashboard", actions=[
    {"type": "click", "selector": "#load-more"},
    {"type": "wait", "milliseconds": 2000},
    {"type": "scroll", "direction": "down", "amount": 500},
])
```

## Output Formats

| Format | Description |
|--------|-------------|
| `markdown` | Clean, readable markdown (default) |
| `html` | Raw or cleaned HTML |
| `screenshot` | PNG screenshot of the page |
| `json` | Structured data (requires schema) |
| `links` | All links found on the page |

## Model Options (for structured extraction)

- **spark-1-mini**: 60% cheaper, good for simple extraction tasks
- **spark-1-pro**: More capable, for complex multi-field extraction

```python
result = app.scrape("https://example.com", schema=MySchema, model="spark-1-pro")
```

## Common Use Cases

**Competitor research:**
```python
pages = app.crawl_url("https://competitor.com/pricing")
# Extract all pricing info as structured JSON
```

**Dataset building from search:**
```python
queries = ["AI startups 2025", "machine learning tools comparison"]
for q in queries:
    results = app.search(q)
    # Save results['data'] to your dataset
```

**Monitor a page for changes:**
```python
import hashlib
result = app.scrape("https://example.com/blog")
current_hash = hashlib.md5(result['markdown'].encode()).hexdigest()
# Compare with stored hash to detect changes
```

**Feed a RAG pipeline:**
```python
results = app.crawl_url("https://docs.myapp.com")
documents = [r['markdown'] for r in results['data']]
# Feed documents into your vector store / RAG system
```

## Integration with MCP / Claude Code

Firecrawl has an official MCP server. Install it to give Claude Code direct web scraping capabilities:

```bash
# Check MCP registry for the Firecrawl connector
```

## Source: [github.com/firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)
