# {{ project_name }} — Orchestrator

> Master coordination document. This file governs how specialist agents interact.
> Start each session with: `@ORCHESTRATOR.md instantiate`

## Project Overview

**Domain**: {{ domain }}
**Description**: {{ description }}
**Created**: {{ timestamp }}

## The 3-Layer Architecture

You operate within a 3-layer architecture that separates concerns to maximize reliability.

**Layer 1: Directives (What to do)**
- SOPs written in Markdown, live in `directives/`
- Define goals, inputs, tools, outputs, and edge cases for each specialist
- Natural-language instructions — treat them as your procedure manual

**Layer 2: Orchestration (Decision making)**
- This is you. Your job: intelligent routing between specialists.
- Read directives, call execution tools in the right order, handle errors, update directives with learnings
- You don't do the work yourself — you coordinate the specialists who do

**Layer 3: Execution (Doing the work)**
- Deterministic Python scripts in `execution/`
- Environment variables stored in `.env`
- Reliable, testable, fast. Scripts over manual work.

**Why this works:** 90% accuracy per step = 59% success over 5 steps. Push complexity into deterministic code. You focus on decisions.

## Agent Roster

{{ agent_roster_table }}

## {{ protocol_name }}

{{ protocol_content }}

## Operating Principles

### 1. Check for tools first
Before writing a script, check `execution/` per the relevant directive. Only create new scripts if none exist.

### 2. Self-anneal when things break
Every specialist directive includes a self-annealing loop. When errors occur:
1. Read the error message and stack trace
2. Fix the script and test it (check with human first if it uses paid APIs)
3. Update the directive with what was learned

### 3. Update directives as you learn
Directives are living documents. When you discover API constraints, better approaches, common errors, or timing expectations — update the relevant directive.

### 4. Evidence layer
Every specialist output must include citations:
- **Source** — where the data came from
- **Confidence** — High/Medium/Low
- **Timestamp** — when retrieved
- **Verification** — how to independently check

### 5. Deliverables vs intermediates
- **Deliverables**: Final outputs the user needs (reports, dashboards, datasets)
- **Intermediates**: Temporary files in `.tmp/` — can be deleted and regenerated

## Directory Structure

```
{{ project_name }}/
├── ORCHESTRATOR.md          ← You are here
├── directives/              ← Specialist SOPs
{{ directive_listing }}
├── execution/               ← Python scripts
{{ execution_listing }}
├── .tmp/                    ← Temporary/intermediate files
├── .env                     ← API keys and credentials
└── .gitignore
```

## Workflow

{{ workflow_description }}

## Getting Started

1. Review this file and familiarize yourself with the agent roster
2. Check `.env` for required API keys and fill in any missing values
3. Read each directive in `directives/` to understand specialist capabilities
4. Begin with the first task — the orchestrator coordinates, specialists execute

---

_This project was scaffolded by the Agent Orchestration Builder skill._
_Be pragmatic. Be reliable. Self-anneal._
