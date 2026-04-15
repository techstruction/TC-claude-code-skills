"""
{{ script_name }}.py — {{ description }}

Specialist: {{ agent_name }}
Project: {{ project_name }}

Usage:
    python execution/{{ script_name }}.py [arguments]

Environment Variables (from .env):
    See .env for required API keys and credentials.
"""

import os
import sys
import json
import logging
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# ── Setup ──────────────────────────────────────────────────────────────
load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
TMP_DIR = PROJECT_ROOT / ".tmp"
TMP_DIR.mkdir(exist_ok=True)


# ── Helpers ────────────────────────────────────────────────────────────
def save_intermediate(data: dict, filename: str) -> Path:
    """Save intermediate data to .tmp/ directory."""
    filepath = TMP_DIR / filename
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2, default=str)
    logger.info(f"Saved intermediate: {filepath}")
    return filepath


def load_intermediate(filename: str) -> dict:
    """Load intermediate data from .tmp/ directory."""
    filepath = TMP_DIR / filename
    with open(filepath, "r") as f:
        return json.load(f)


# ── Main Logic ─────────────────────────────────────────────────────────
def main():
    """
    TODO: Implement the core logic for this execution script.

    This script should:
    1. Accept inputs (CLI args, files, or environment variables)
    2. Perform deterministic processing
    3. Output results (to stdout, files, or external services)

    Remember:
    - This script handles the DETERMINISTIC work
    - The orchestrator handles DECISIONS
    - Keep it focused, testable, and well-commented
    """
    logger.info(f"Starting {{ script_name }}...")
    logger.info(f"Project root: {PROJECT_ROOT}")

    # TODO: Replace with actual implementation
    result = {
        "status": "success",
        "timestamp": datetime.now().isoformat(),
        "data": {},
    }

    # Save result as intermediate
    save_intermediate(result, f"{{ script_name }}_result.json")

    logger.info("Done.")
    return result


if __name__ == "__main__":
    main()
