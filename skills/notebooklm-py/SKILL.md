---
name: notebooklm-py
description: >
  Use this skill whenever the user wants to interact with Google NotebookLM programmatically — creating notebooks, adding sources, generating audio/video/slide/quiz/flashcard/infographic outputs, downloading artifacts, or asking questions of a notebook. Trigger on any mention of NotebookLM, podcast generation, notebook automation, audio overviews, or batch content generation from documents. Also use when the user wants to automate research workflows involving NotebookLM, even if they phrase it as "make a podcast from my documents" or "summarize this research as a quiz."
---

# NotebookLM-py Skill

This skill helps you use **notebooklm-py**, an unofficial Python SDK and CLI for Google NotebookLM. It lets you automate notebook creation, add sources, generate content (audio, video, slides, quizzes, flashcards, infographics), and download artifacts — all from code or the command line.

> **Note**: This library uses undocumented Google APIs and is best for prototyping, research, and personal projects. It's not recommended for production systems.

## Installation

### macOS (Homebrew-managed Python)
macOS blocks `pip install` into the system Python. Use `pipx` instead:

```bash
brew install pipx && pipx ensurepath
# restart your shell, then:
pipx install "notebooklm-py[browser]"

# Install Chromium into the pipx venv
~/.local/pipx/venvs/notebooklm-py/bin/python -m playwright install chromium
```

### Linux / Ubuntu
```bash
pip install "notebooklm-py[browser]"
python3 -m playwright install chromium
# If playwright chromium download fails due to missing deps:
sudo apt-get install -y --no-install-recommends \
    libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 \
    libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 \
    libgbm1 libasound2 libpango-1.0-0 libcairo2
python3 -m playwright install chromium
```

### Headless servers (no display)
You cannot run `notebooklm login` on a headless server. Instead:
1. Authenticate on a machine with a browser (Mac/desktop)
2. Copy the session to the server:
   ```bash
   scp -r ~/.notebooklm user@your-server:~/
   ```
3. Ensure `notebooklm` is in PATH on the server — add to `~/.bashrc` if needed:
   ```bash
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   ```

## Authentication

Authenticate once on a machine with a browser — credentials saved to `~/.notebooklm/storage_state.json`:

```bash
notebooklm login
```

For Python scripts, use the stored credentials via `NotebookLMClient.from_storage()`.

## CLI Usage

```bash
# Create a notebook
notebooklm create "My Research Notebook"

# Add sources (URLs, files, or text)
notebooklm source add "https://example.com/paper.pdf"
notebooklm source add ./local_document.pdf

# Ask a question
notebooklm ask "What are the key findings?"

# Generate content
notebooklm generate audio --wait          # Audio podcast overview
notebooklm generate video --wait          # Video overview
notebooklm generate slides --wait         # Slide deck (PDF or PPTX)
notebooklm generate quiz --wait           # Quiz
notebooklm generate flashcards --wait     # Flashcards

# Download artifacts
notebooklm download audio ./podcast.mp3
notebooklm download slides ./slides.pdf
notebooklm download quiz ./quiz.json
```

## Python API

The Python API is fully async. Always use `async with` for the client.

```python
import asyncio
from notebooklm import NotebookLMClient

async def main():
    async with await NotebookLMClient.from_storage() as client:

        # Create a notebook
        nb = await client.notebooks.create("Research Project")

        # Add sources
        await client.sources.add_url(nb.id, "https://example.com/paper.pdf")
        await client.sources.add_file(nb.id, "./local_doc.pdf")

        # Chat / Q&A
        result = await client.chat.ask(nb.id, "Summarize the key points")
        print(result.answer)

        # Generate audio overview and wait for completion
        job = await client.generate.audio(nb.id)
        artifact = await job.wait()

        # Download it
        await client.download(artifact, "./podcast.mp3")

asyncio.run(main())
```

## Content Types Available

| Type | Formats | Notes |
|------|---------|-------|
| Audio overview | MP3 | 50+ languages supported |
| Video overview | MP4 | 9 visual styles |
| Slides | PDF, PPTX (editable) | |
| Quiz | JSON, Markdown, HTML | Structured data export |
| Flashcards | JSON, Markdown, HTML | Structured data export |
| Infographic | PNG/SVG | |
| Mind map | JSON + image | Graph data extractable |

## Workflow Tips

- **Batch processing**: Loop over multiple notebooks or sources to generate content at scale.
- **Structured exports**: Quizzes and flashcards can be exported as JSON for downstream use (e.g., feeding into Anki or a database).
- **Mind map extraction**: The SDK can extract the underlying graph data, not just the image.
- **Sharing management**: Use `client.notebooks.share()` to manage notebook access programmatically.

## Common Patterns

**Research pipeline** — add multiple papers and generate a podcast:
```python
async with await NotebookLMClient.from_storage() as client:
    nb = await client.notebooks.create("Literature Review")
    urls = ["https://arxiv.org/abs/...", "https://arxiv.org/abs/..."]
    for url in urls:
        await client.sources.add_url(nb.id, url)
    job = await client.generate.audio(nb.id)
    artifact = await job.wait()
    await client.download(artifact, "./review_podcast.mp3")
```

**Quiz generation from a document**:
```python
async with await NotebookLMClient.from_storage() as client:
    nb = await client.notebooks.create("Study Material")
    await client.sources.add_file(nb.id, "./textbook_chapter.pdf")
    job = await client.generate.quiz(nb.id)
    artifact = await job.wait()
    await client.download(artifact, "./quiz.json")  # structured JSON
```

## Source: [github.com/teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py)
