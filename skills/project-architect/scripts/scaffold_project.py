#!/usr/bin/env python3
"""
scaffold_project.py — Agent Orchestration Builder

Generates a complete 3-layer project directory from a domain, agent roster,
and coordination protocol selection.

Usage:
    python scaffold_project.py \
        --domain finance \
        --project-name "my-trading-system" \
        --output-dir /path/to/project \
        --agents "Fundamental Analyst,Quantitative Architect,Risk Manager" \
        --protocol writer-critic \
        --description "Automated equity research and portfolio management"

The script reads templates from ../templates/ and generates:
    directives/         — One .md file per agent
    execution/          — Python script stubs per agent + shared utilities
    ORCHESTRATOR.md     — Master coordination document
    AGENTS.md           — Runtime instructions (3-layer architecture)
    .env                — Credential template
    .gitignore          — Standard ignores
    .tmp/               — Intermediate file directory
    README.md           — Project overview
"""

import argparse
import os
import re
import sys
import shutil
from datetime import datetime
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
TEMPLATES_DIR = SKILL_DIR / "templates"
REFERENCES_DIR = SKILL_DIR / "references"


# ── Domain Agent Defaults ──────────────────────────────────────────────
# Brief role descriptions used when the user provides agent names but
# Claude hasn't yet enriched them with custom mission briefs.
DOMAIN_DEFAULTS = {
    "finance": {
        "agents": [
            "Fundamental Analyst",
            "Quantitative Architect",
            "Risk & Hedging Manager",
            "Data Harvester",
            "Macro Strategist",
        ],
        "protocol": "writer-critic",
        "tools": ["api_client", "data_pipeline", "risk_calculator", "report_generator"],
    },
    "social_media": {
        "agents": [
            "Trend Strategist",
            "Engagement Psychologist",
            "Visual Brand Guardian",
            "Community Architect",
            "Analytics & Attribution Specialist",
        ],
        "protocol": "expert-debate",
        "tools": ["social_listener", "content_analyzer", "engagement_tracker", "report_generator"],
    },
    "saas": {
        "agents": [
            "Product Strategist",
            "Growth Engineer",
            "Technical Architect",
            "Customer Intelligence Analyst",
        ],
        "protocol": "pipeline",
        "tools": ["analytics_pipeline", "experiment_runner", "customer_tracker", "report_generator"],
    },
    "research": {
        "agents": [
            "Literature Surveyor",
            "Methodology Designer",
            "Data Scientist",
            "Peer Reviewer",
        ],
        "protocol": "expert-debate",
        "tools": ["literature_search", "statistical_analysis", "visualization", "report_generator"],
    },
    "iot": {
        "agents": [
            "Embedded Systems Architect",
            "Sensor Data Engineer",
            "Reliability Engineer",
            "Security Specialist",
        ],
        "protocol": "pipeline",
        "tools": ["device_manager", "data_pipeline", "monitoring", "security_scanner"],
    },
    "ecommerce": {
        "agents": [
            "Conversion Optimizer",
            "Catalog & Pricing Strategist",
            "Customer Journey Mapper",
            "Supply Chain Analyst",
        ],
        "protocol": "writer-critic",
        "tools": ["price_tracker", "funnel_analyzer", "demand_forecaster", "report_generator"],
    },
}


# ── Utilities ──────────────────────────────────────────────────────────
def slugify(name: str) -> str:
    """Convert a name like 'Fundamental Analyst' to 'fundamental_analyst'."""
    s = name.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_")


def read_template(filename: str) -> str:
    """Read a template file from the templates directory."""
    path = TEMPLATES_DIR / filename
    if not path.exists():
        print(f"[WARN] Template not found: {path}")
        return ""
    return path.read_text()


def fill_template(template: str, variables: dict) -> str:
    """Simple {{ variable }} replacement."""
    result = template
    for key, value in variables.items():
        result = result.replace("{{ " + key + " }}", str(value))
    return result


def read_protocol_template(protocol: str) -> tuple[str, str]:
    """Return clean, directly-embeddable protocol content for ORCHESTRATOR.md."""
    protocols = {
        "writer-critic": (
            "Writer-Critic Loop",
            """### Flow
1. **Assignment** — Orchestrator assigns task to the Writer agent with clear deliverable spec
2. **Draft** — Writer produces output with citations and confidence levels
3. **Review** — Critic agent evaluates the draft against:
   - Factual accuracy (are claims supported by data?)
   - Logical consistency (do conclusions follow from premises?)
   - Completeness (are there obvious gaps or missing perspectives?)
   - Actionability (can a human act on this output?)
4. **Revision** — Writer addresses critique points, noting which feedback was accepted/rejected and why
5. **Approval** — Critic either approves or requests another revision round
6. **Escalation** — If no consensus after 3 rounds, orchestrator makes the final call and documents the disagreement

### Rules
- Critic must provide specific, actionable feedback (not "this could be better")
- Writer must respond to every critique point, even if the response is "disagree because..."
- Both agents must include citations for their claims
- Maximum 3 revision rounds to prevent infinite loops""",
        ),
        "expert-debate": (
            "Expert Debate",
            """### Flow
1. **Framing** — Orchestrator defines the question and distributes it to all relevant specialists
2. **Independent Analysis** — Each specialist analyzes from their domain perspective (no collaboration at this stage)
3. **Position Papers** — Each specialist submits their assessment, key evidence, risks they foresee, and what they'd need from others to increase confidence
4. **Cross-examination** — Each specialist reviews others' positions and submits points of agreement, disagreement with reasoning, and questions
5. **Synthesis** — Orchestrator produces a unified recommendation noting consensus areas, disagreements (fairly represented), explicit tradeoff decisions, and what additional data would resolve remaining uncertainty

### Rules
- Independent analysis must happen before cross-examination (prevent groupthink)
- Every disagreement must be documented, not silently resolved
- Orchestrator's synthesis must acknowledge uncertainty honestly
- Minority opinions get documented — they're often right when conditions change""",
        ),
        "pipeline": (
            "Pipeline",
            """### Flow
1. **Stage Definition** — Each pipeline stage has an input spec, assigned agent, process description, output spec, and validation criteria
2. **Execution** — Stages run sequentially. Each stage validates its input, performs its work, validates its output, and passes to the next stage
3. **Error handling** — Input validation failure kicks back to previous stage. Output validation failure retries current stage (max 2). After retries, escalate to orchestrator.

### Stage Template
| Stage | Agent | Input | Output | Validation |
|-------|-------|-------|--------|------------|
| 1 | [Agent] | [Input spec] | [Output spec] | [Check criteria] |
| 2 | [Agent] | [Input spec] | [Output spec] | [Check criteria] |
| 3 | [Agent] | [Input spec] | [Output spec] | [Check criteria] |

### Rules
- Every handoff must be explicitly typed (no "just pass the data along")
- Validation happens at both ends of every handoff
- Failed validations produce actionable error messages, not generic failures
- Pipeline stages should be independently testable""",
        ),
    }

    if protocol in protocols:
        return protocols[protocol]
    return "Writer-Critic Loop", "See references/protocols.md for coordination details."


# ── Generators ─────────────────────────────────────────────────────────
def generate_directive(agent_name: str, project_name: str, domain: str) -> str:
    """Generate a directive .md file for a specialist agent."""
    template = read_template("directive_template.md")
    slug = slugify(agent_name)

    variables = {
        "agent_name": agent_name,
        "agent_slug": slug,
        "project_name": project_name,
        "agent_mission": f"[TODO: Claude will enrich this with domain-specific methodology and best practices for the {agent_name} role in {domain}.]",
        "data_sources": "[TODO: Specify based on project requirements]",
        "upstream_agents": "[TODO: Specify based on coordination protocol]",
        "primary_output": f"[TODO: Define primary deliverable for {agent_name}]",
        "output_format": "[TODO: Markdown, JSON, CSV, etc.]",
        "output_destination": "[TODO: .tmp/, cloud service, etc.]",
    }

    return fill_template(template, variables)


def generate_orchestrator(
    project_name: str,
    domain: str,
    description: str,
    agents: list[str],
    protocol: str,
) -> str:
    """Generate the ORCHESTRATOR.md master coordination document."""
    template = read_template("orchestrator_template.md")

    # Build agent roster table
    roster_lines = ["| Agent | Directive | Primary Role |", "|-------|-----------|-------------|"]
    for agent in agents:
        slug = slugify(agent)
        roster_lines.append(f"| {agent} | `directives/{slug}.md` | [See directive] |")
    agent_roster_table = "\n".join(roster_lines)

    # Get protocol template
    protocol_name, protocol_content = read_protocol_template(protocol)

    # Build directory listing
    directive_listing = ""
    for agent in agents:
        slug = slugify(agent)
        directive_listing += f"│   ├── {slug}.md\n"

    execution_listing = ""
    domain_tools = DOMAIN_DEFAULTS.get(domain, {}).get("tools", ["utils"])
    for tool in domain_tools:
        execution_listing += f"│   ├── {tool}.py\n"

    # Build workflow description based on protocol
    workflow_map = {
        "writer-critic": "1. Orchestrator assigns task to the appropriate Writer agent\n2. Writer produces draft with citations\n3. Critic agent reviews for accuracy and completeness\n4. Writer revises based on critique\n5. Approved output is delivered\n6. Directives updated with any learnings",
        "expert-debate": "1. Orchestrator frames the question and distributes to relevant specialists\n2. Each specialist analyzes independently (no collaboration)\n3. Specialists submit position papers with evidence\n4. Cross-examination phase: specialists review each other's positions\n5. Orchestrator synthesizes into unified recommendation\n6. Directives updated with any learnings",
        "pipeline": "1. Data flows through pipeline stages sequentially\n2. Each stage validates inputs, processes, validates outputs\n3. Failed validations kick back to previous stage\n4. Final stage produces the deliverable\n5. Directives updated with any learnings",
    }
    workflow_description = workflow_map.get(protocol, workflow_map["writer-critic"])

    variables = {
        "project_name": project_name,
        "domain": domain.replace("_", " ").title(),
        "description": description,
        "timestamp": datetime.now().strftime("%Y-%m-%d"),
        "agent_roster_table": agent_roster_table,
        "protocol_name": protocol_name,
        "protocol_content": protocol_content,
        "directive_listing": directive_listing,
        "execution_listing": execution_listing,
        "workflow_description": workflow_description,
    }

    return fill_template(template, variables)


def generate_execution_stub(tool_name: str, agent_name: str, project_name: str) -> str:
    """Generate a Python execution script stub."""
    template = read_template("execution_stub.py")

    variables = {
        "script_name": tool_name,
        "agent_name": agent_name,
        "project_name": project_name,
        "description": f"Execution script for {tool_name.replace('_', ' ')} operations",
    }

    return fill_template(template, variables)


def generate_readme(project_name: str, domain: str, description: str, agents: list[str], protocol: str) -> str:
    """Generate a README.md for the project."""
    agent_list = "\n".join([f"- **{a}** — see `directives/{slugify(a)}.md`" for a in agents])

    return f"""# {project_name}

{description}

**Domain**: {domain.replace('_', ' ').title()}
**Coordination Protocol**: {protocol.replace('-', ' ').title()}

## Quick Start

1. Fill in API keys in `.env`
2. Run `@ORCHESTRATOR.md instantiate` to begin
3. The orchestrator will coordinate your specialist agents

## Agent Roster

{agent_list}

## Directory Structure

- `ORCHESTRATOR.md` — Master coordination document (start here)
- `directives/` — Specialist agent SOPs
- `execution/` — Deterministic Python scripts
- `.tmp/` — Temporary/intermediate files (auto-cleaned)
- `.env` — API keys and credentials (never commit)

## Architecture

This project uses the **3-Layer Architecture**:

1. **Directives** (Layer 1) — What to do (Markdown SOPs)
2. **Orchestration** (Layer 2) — Decision making (ORCHESTRATOR.md)
3. **Execution** (Layer 3) — Doing the work (Python scripts)

Every specialist includes a **self-annealing loop**: errors are captured, scripts are fixed, and directives are updated so the system gets stronger over time.

---

_Scaffolded by the Agent Orchestration Builder skill._
"""


# ── Main ───────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a 3-layer multi-agent project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--domain", required=True, help="Domain slug (finance, social_media, saas, research, iot, ecommerce, custom)")
    parser.add_argument("--project-name", required=True, help="Human-readable project name")
    parser.add_argument("--output-dir", required=True, help="Directory to create the project in")
    parser.add_argument("--agents", required=True, help="Comma-separated list of agent names")
    parser.add_argument("--protocol", required=True, choices=["writer-critic", "expert-debate", "pipeline"], help="Coordination protocol")
    parser.add_argument("--description", default="", help="One-line project description")

    args = parser.parse_args()

    # Parse agent list
    agents = [a.strip() for a in args.agents.split(",") if a.strip()]
    if not agents:
        print("[ERROR] No agents specified.")
        sys.exit(1)

    output_dir = Path(args.output_dir).resolve()
    project_name = args.project_name
    domain = args.domain.lower().replace(" ", "_")
    description = args.description or f"A {domain.replace('_', ' ')} multi-agent project"

    print(f"\n{'='*60}")
    print(f"  Agent Orchestration Builder")
    print(f"  Project: {project_name}")
    print(f"  Domain:  {domain}")
    print(f"  Agents:  {len(agents)}")
    print(f"  Protocol: {args.protocol}")
    print(f"  Output:  {output_dir}")
    print(f"{'='*60}\n")

    # ── Create directory structure ─────────────────────────────────────
    dirs_to_create = [
        output_dir,
        output_dir / "directives",
        output_dir / "execution",
        output_dir / "execution" / "utils",
        output_dir / ".tmp",
    ]
    for d in dirs_to_create:
        d.mkdir(parents=True, exist_ok=True)
        print(f"  [DIR]  {d.relative_to(output_dir) if d != output_dir else '.'}")

    # ── Generate directives ────────────────────────────────────────────
    print("\n  Generating directives...")
    for agent in agents:
        slug = slugify(agent)
        content = generate_directive(agent, project_name, domain)
        filepath = output_dir / "directives" / f"{slug}.md"
        filepath.write_text(content)
        print(f"  [FILE] directives/{slug}.md")

    # ── Generate execution stubs ───────────────────────────────────────
    print("\n  Generating execution scripts...")
    domain_tools = DOMAIN_DEFAULTS.get(domain, {}).get("tools", [])

    # Domain-specific tools
    for tool in domain_tools:
        first_agent = agents[0] if agents else "Orchestrator"
        content = generate_execution_stub(tool, first_agent, project_name)
        filepath = output_dir / "execution" / f"{tool}.py"
        filepath.write_text(content)
        print(f"  [FILE] execution/{tool}.py")

    # Shared utility init
    init_path = output_dir / "execution" / "utils" / "__init__.py"
    init_path.write_text('"""Shared utilities for execution scripts."""\n')
    print(f"  [FILE] execution/utils/__init__.py")

    # ── Generate ORCHESTRATOR.md ───────────────────────────────────────
    print("\n  Generating orchestrator...")
    orchestrator_content = generate_orchestrator(
        project_name, domain, description, agents, args.protocol
    )
    (output_dir / "ORCHESTRATOR.md").write_text(orchestrator_content)
    print(f"  [FILE] ORCHESTRATOR.md")

    # ── Copy AGENTS.md base (the 3-layer architecture reference) ──────
    # Look for the source AGENTS.md in the user's workspace
    agents_md_candidates = [
        Path.home() / "Documents" / "MBP Antigravity skills" / "Agent Orchestration builder Skill" / "AGENTS.md",
        SKILL_DIR / "AGENTS.md",
    ]
    agents_md_source = None
    for candidate in agents_md_candidates:
        if candidate.exists():
            agents_md_source = candidate
            break

    if agents_md_source:
        shutil.copy2(agents_md_source, output_dir / "AGENTS.md")
        print(f"  [FILE] AGENTS.md (copied from {agents_md_source.name})")
    else:
        print(f"  [SKIP] AGENTS.md — source not found, ORCHESTRATOR.md contains the architecture")

    # ── Generate .env ──────────────────────────────────────────────────
    env_content = read_template("env_template.txt")
    (output_dir / ".env").write_text(env_content)
    print(f"  [FILE] .env")

    # ── Generate .gitignore ────────────────────────────────────────────
    gitignore_content = read_template("gitignore_template.txt")
    (output_dir / ".gitignore").write_text(gitignore_content)
    print(f"  [FILE] .gitignore")

    # ── Generate README.md ─────────────────────────────────────────────
    readme_content = generate_readme(project_name, domain, description, agents, args.protocol)
    (output_dir / "README.md").write_text(readme_content)
    print(f"  [FILE] README.md")

    # ── Summary ────────────────────────────────────────────────────────
    total_files = len(agents) + len(domain_tools) + 5  # directives + tools + ORCHESTRATOR + AGENTS + .env + .gitignore + README
    print(f"\n{'='*60}")
    print(f"  ✅ Project scaffolded successfully!")
    print(f"  📁 {total_files} files created in {output_dir}")
    print(f"  🚀 Start with: @ORCHESTRATOR.md instantiate")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
