#!/usr/bin/env bash
# TC Claude Code Skills — Installer
# Copies all skills from this repo into ~/.claude/skills/

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="$SCRIPT_DIR/skills"
SKILLS_DEST="$HOME/.claude/skills"

echo "TC Claude Code Skills Installer"
echo "================================"
echo "Source:      $SKILLS_SRC"
echo "Destination: $SKILLS_DEST"
echo ""

if [ ! -d "$SKILLS_SRC" ]; then
  echo "Error: skills/ directory not found. Run from the repo root."
  exit 1
fi

mkdir -p "$SKILLS_DEST"

installed=0
skipped=0

for skill_dir in "$SKILLS_SRC"/*/; do
  skill_name=$(basename "$skill_dir")
  dest="$SKILLS_DEST/$skill_name"

  if [ -d "$dest" ]; then
    echo "  update  $skill_name"
    rm -rf "$dest"
  else
    echo "  install $skill_name"
  fi

  cp -r "$skill_dir" "$dest"
  ((installed++))
done

echo ""
echo "Done. $installed skills installed to $SKILLS_DEST"
echo ""
echo "Restart Claude Code to load new skills."
