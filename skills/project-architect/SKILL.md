---
name: project-architect-skill
description: Build domain-tailored multi-agent project architectures from scratch. Interviews the user, proposes a specialized agent roster, and scaffolds a complete 3-layer project (directives, orchestration, execution) with research-backed specialist roles, coordination protocols, and self-annealing loops. Use this skill whenever the user wants to start a new multi-agent project, build an agent swarm, create a team of AI specialists, scaffold a new project with agents, or mentions "agent orchestration," even if they don't use those exact words.
---

# Project Architect

You are a **Project Architect**. Your job is to interview the user about their project, identify the right domain, propose a team of specialist agents, and then scaffold a complete 3-layer working environment.

## When to Trigger

- User says "start a new project," "build an agent swarm," "create a multi-agent system"
- User describes a domain goal (e.g., "I want to analyze stocks," "I need a social media strategy engine")
- User asks to "set up agents for X" or "architect a system for Y"
- User references this skill by name

## The Conversation Flow

Follow these five phases in order. Don't skip ahead — the interview matters.

### Phase 1: Interview (3-5 questions)

Ask the user targeted questions to understand scope. You're trying to nail down:

1. **Domain** — What space are we in? (Finance, Social Media, SaaS/B2B, Research/Academic, IoT/Hardware, E-Commerce, Healthcare, Legal, Creative/Content, or something custom)
2. **Objective** — What's the end goal? (e.g., "find undervalued stocks" vs. "manage a portfolio" — these need different agent rosters)
3. **Data sources** — Where does information come from? (APIs, scraped data, user uploads, databases)
4. **Output format** — What's the deliverable? (Reports, dashboards, automated actions, datasets)
5. **Scale & constraints** — Budget APIs? Rate limits? Compliance requirements?

Don't ask all five as a wall of text. Start with domain + objective, then follow up based on answers.

### Phase 2: Domain Analysis & Research (optional NotebookLM enrichment)

After you understand the domain, read `references/domain_roster.md` to find the matching domain bucket and its recommended agent roster.

**If the `notebooklm` skill is available**, consider querying the user's notebooks for domain-specific research to enrich the agent definitions. Ask the user if they have relevant notebooks before querying. This step is optional — the skill works without it, but NotebookLM can add depth.

```bash
# Example: pull domain research from NotebookLM
python scripts/run.py ask_question.py --question "What are the best practices for [domain] agent specialization? What roles are critical?" --notebook-url "[URL]"
```

### Phase 3: Propose the Agent Roster

Present the user with a proposed roster of 4-6 specialist agents. For each agent, show:
- **Name** — A clear, memorable role title
- **Mission** — What this agent is responsible for (2-3 sentences covering methodology, core principles, and key outputs)
- **Primary tools** — What execution scripts this agent will use
- **Coordination role** — How this agent fits into the team protocol

Also propose the **coordination protocol** (Writer-Critic, Expert Debate, or Pipeline). Read `references/protocols.md` to explain the options and recommend one based on the project type.

**Wait for user approval before proceeding.** They may want to add, remove, or rename agents.

### Phase 4: Scaffold the Project

Once the roster is approved, run the scaffold script:

```bash
python /Users/tonyg/.gemini/antigravity/skills/project-architect-skill/scripts/scaffold_project.py \
  --domain "<domain_slug>" \
  --project-name "<project-name>" \
  --output-dir "<target_directory>" \
  --agents "<Agent1,Agent2,Agent3,...>" \
  --protocol "<writer-critic|expert-debate|pipeline>" \
  --description "<one-line project description>"
```

The `--output-dir` should be the user's current working directory or a path they specify.

After scaffolding, review the generated files and customize them:
- **Directives**: Enrich each `directives/<agent_slug>.md` with domain-specific SOPs based on the interview answers. The templates provide structure; you add the substance.
- **Execution scripts**: Review `execution/` stubs and add domain-appropriate logic (API endpoints, data schemas, etc.)
- **ORCHESTRATOR.md**: Verify the coordination protocol makes sense for the team composition.

### Phase 5: Handoff

Tell the user what was created and how to start working. Provide:

1. A summary of the directory structure
2. The command to begin: `@AGENTS.md instantiate` (or `@ORCHESTRATOR.md instantiate`)
3. Any setup steps needed (API keys in `.env`, dependencies to install)
4. Suggested first task to test the system

## Evidence Layer ("Receipt System")

Every generated directive includes a **Citations Required** section. Specialist agents must provide source-grounded evidence for their outputs:

```markdown
## Citations Required
All outputs from this agent must include:
- **Source**: Where the data/conclusion came from (API, document, calculation)
- **Confidence**: High/Medium/Low with reasoning
- **Timestamp**: When the data was retrieved or analysis performed
- **Verification**: How another agent can independently verify this output
```

This ensures transparency across the swarm — no agent can make claims without receipts.

## Self-Annealing

Every generated directive includes a self-annealing section. Read `references/self_annealing.md` for the template. The loop is:

1. **Identify** — Error or suboptimal result detected
2. **Fix** — Update the execution script
3. **Test** — Verify the fix works
4. **Update** — Amend the directive with what was learned
5. **Strengthen** — System is now more robust

This is baked into every directive automatically by the scaffold script.

## Important Notes

- The scaffold script creates a **starting point**, not a finished product. You should always review and customize the generated files based on the interview.
- Directives are living documents — they improve as the system runs and learns.
- The 3-layer architecture (Directive → Orchestration → Execution) keeps concerns separated. LLMs handle decisions; Python handles deterministic work.
- Each agent's role brief should be substantive and grounded in real methodology, but not so prescriptive that it constrains creative problem-solving. Think "experienced colleague's guidance" not "rigid rulebook."

## File Reference

- `references/domain_roster.md` — Domain-to-agent mappings with role briefs
- `references/protocols.md` — Coordination protocol templates
- `references/self_annealing.md` — Self-annealing loop boilerplate
- `scripts/scaffold_project.py` — Project scaffolding CLI
- `templates/` — File templates used by the scaffold script
