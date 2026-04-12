#!/usr/bin/env bash
# TC Claude Code Skills — Installer
#
# Local install (from cloned repo):
#   ./install.sh
#
# Remote one-liner (no clone needed):
#   curl -fsSL https://raw.githubusercontent.com/techstruction/TC-claude-code-skills/main/install.sh | bash

set -e

REPO="techstruction/TC-claude-code-skills"
SKILLS_DEST="$HOME/.claude/skills"

echo "TC Claude Code Skills Installer"
echo "================================"

# Detect whether we're running locally (piped from curl) or from a cloned repo
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="$SCRIPT_DIR/skills"

if [ ! -d "$SKILLS_SRC" ]; then
  # Remote mode: clone into a temp directory then install
  echo "Mode:        remote (cloning from GitHub)"
  echo "Destination: $SKILLS_DEST"
  echo ""

  TMP_DIR="$(mktemp -d)"
  trap 'rm -rf "$TMP_DIR"' EXIT

  echo "Cloning $REPO..."
  git clone --depth=1 "git@github.com:$REPO.git" "$TMP_DIR" 2>&1 | grep -v "^$" || \
  git clone --depth=1 "https://github.com/$REPO.git" "$TMP_DIR" 2>&1 | grep -v "^$"

  SKILLS_SRC="$TMP_DIR/skills"
else
  # Local mode: install from the repo we're already in
  echo "Mode:        local"
  echo "Source:      $SKILLS_SRC"
  echo "Destination: $SKILLS_DEST"
  echo ""
fi

mkdir -p "$SKILLS_DEST"

installed=0

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
