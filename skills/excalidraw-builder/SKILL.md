---
name: excalidraw-builder
description: Draw, map out, or visually represent project structures, architectures, data flows, and workflows using Excalidraw. Use this skill whenever the user asks for a visual layout, a diagram, a map of a folder or codebase, or a flowchart — even if they don't say "Excalidraw" explicitly. Good triggers include: "draw a diagram", "visualize this", "map out the architecture", "create a flowchart", "show me the structure", or "make an Excalidraw".
---

# Excalidraw Builder Skill

This skill lets you programmatically generate Excalidraw diagrams (`.excalidraw` files) that the user can open at excalidraw.com or a local Excalidraw instance.

## How It Works

Instead of attempting complex layouts by hand, construct a simple intermediate JSON file describing the `nodes` and `edges` of the diagram, then run a Python tool that generates the correct native Excalidraw format.

## Step 1: Create the intermediate JSON file

Understand what the user wants to visualize. Create a temporary JSON file (e.g., `.tmp/diagram.json`) with this structure:

```json
{
  "nodes": [
    {"id": "n1", "label": "User Input", "shape": "Rectangle", "x": 0, "y": 0, "width": 150, "height": 60, "backgroundColor": "#fff"},
    {"id": "n2", "label": "Decision", "shape": "Diamond", "x": 200, "y": 0, "width": 100, "height": 100, "backgroundColor": "#ffc9c9"}
  ],
  "edges": [
    {"from": "n1", "to": "n2", "label": "Submit"}
  ]
}
```

### Supported Shapes
- `Rectangle` (Default)
- `Diamond` (Good for decisions/conditions)
- `Ellipse` (Good for start/end states or databases)
- `Text` (Plain text label, no border)

### Coordinates (x, y)
You are responsible for the rough layout — the script does NOT auto-layout.
- Place shapes so they don't overlap.
- E.g., if Node 1 is at `(0,0)`, place Node 2 at `(250, 0)` for horizontal flow, or `(0, 150)` for vertical flow.

## Step 2: Run the Execution Script

The skill's `scripts/` directory contains the generator. Run it with:

```bash
SKILL_DIR="$(python3 -c "import subprocess; r = subprocess.run(['claude', 'skills', 'path', 'excalidraw-builder'], capture_output=True, text=True); print(r.stdout.strip())" 2>/dev/null || echo "$HOME/.claude/skills/excalidraw-builder")"
bash "$SKILL_DIR/scripts/generate.sh" .tmp/diagram.json my_diagram.excalidraw
```

Or more simply — if you know the skill install path:

```bash
bash ~/.claude/skills/excalidraw-builder/scripts/generate.sh .tmp/diagram.json my_diagram.excalidraw
```

If you just provide a filename (no directory), the file will be saved in `Excalidrawings/` in the current working directory (created if it doesn't exist).

## Step 3: Present to the User

After the `.excalidraw` file is successfully generated, tell the user where it was saved and that they can view it by dragging it into:
- https://excalidraw.com
- https://excalidraw.techstruction.co (if they have a local instance)

## Portability & Best Practices
- **Auto-organization**: Default to saving in `Excalidrawings/` at the project root.
- **Clean up**: Use `.tmp/` for intermediate JSON files.
- **Dependencies**: `generate.sh` auto-installs `Excalidraw_Interface` via pip if not present.

## Workflows

1. **Analyze a Project**: Read the directory structure with your tools, model it as connected `Rectangle` nodes, generate the file.
2. **Data Flow / Architecture**: Use `Ellipse` for databases, `Rectangle` for services, `Edges` with labels for API calls.
3. **Flowcharts**: Use `Diamond` for decisions, `Ellipse` for start/end, `Rectangle` for steps.
