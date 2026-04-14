#!/bin/bash
# excalidraw-builder wrapper script
# Usage: bash generate.sh <input_json> <output_path>
# Dependency: Excalidraw_Interface (auto-installed via pip if missing)

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

# Auto-install Excalidraw_Interface if not available
if ! python3 -c "import Excalidraw_Interface" 2>/dev/null; then
    echo "Installing Excalidraw_Interface..."
    pip3 install -q Excalidraw_Interface
fi

python3 "$DIR/excalidraw_generator.py" "$1" "$2"
