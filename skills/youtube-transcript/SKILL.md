---
name: youtube-transcript
description: Fetch full transcripts from YouTube videos using autocli. Use when the user provides a YouTube URL or video ID and wants a transcript, summary, or content extraction from a video.
---

# YouTube Transcript

Fetches full transcripts from YouTube videos via autocli, which reuses your local Chrome session. No API key needed.

> **⚠️ Requires local Chrome:** Chrome must be open and logged into YouTube. The autocli Chrome Extension must be installed. Does not work on headless servers.

## Basic Usage

```bash
autocli youtube transcript "https://www.youtube.com/watch?v=VIDEO_ID"
```

Always pass the full URL — not just the video ID.

## Output Formats

```bash
# Default table (speaker | text | timestamp)
autocli youtube transcript "https://www.youtube.com/watch?v=VIDEO_ID"

# JSON — best for parsing or saving
autocli youtube transcript "https://www.youtube.com/watch?v=VIDEO_ID" --format json

# Save to file
autocli youtube transcript "https://www.youtube.com/watch?v=VIDEO_ID" --format json > /tmp/transcript.json
```

## Language Selection

```bash
# Request a specific language (if available)
autocli youtube transcript "https://www.youtube.com/watch?v=VIDEO_ID" --lang en
autocli youtube transcript "https://www.youtube.com/watch?v=VIDEO_ID" --lang es
```

## Typical Workflow

1. User provides a YouTube URL
2. Run the transcript command
3. Output is large — save to a temp file if you need to process it:
   ```bash
   autocli youtube transcript "URL" > /tmp/transcript.txt
   ```
4. Read the file and summarize, extract key points, answer questions, etc.

## What to Do With the Transcript

- **Summarize:** Read the full output and write a structured summary
- **Extract specifics:** Pull out lists, steps, quotes, names, or data points the user asks about
- **Create a document:** Format into a clean Markdown file with headers and sections
- **Answer questions:** Use as context to answer specific questions about the video content

## Troubleshooting

| Problem | Fix |
|---|---|
| `Chrome extension not connected` | Open Chrome, verify the autocli extension is installed and enabled |
| No transcript available | Some videos have transcripts disabled by the creator — nothing to fetch |
| Wrong language returned | Add `--lang en` (or target language code) to the command |
| Output truncated in terminal | Pipe to a file: `> /tmp/transcript.txt`, then read the file |
