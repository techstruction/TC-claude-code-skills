# Coordination Protocols

Three coordination protocols govern how specialist agents interact. Choose based on the project's nature.

---

## 1. Writer-Critic Loop

**Best for**: Tasks where accuracy and rigor matter more than speed. Finance, compliance, technical documentation.

**How it works**: One specialist produces a draft output. A different specialist (the critic) reviews it for errors, omissions, and weak reasoning. The writer revises based on the critique. The loop continues until the critic approves or a maximum iteration count is reached (default: 3).

### Template for ORCHESTRATOR.md

```markdown
## Coordination Protocol: Writer-Critic Loop

### Flow
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
- Maximum 3 revision rounds to prevent infinite loops
```

---

## 2. Expert Debate

**Best for**: Complex decisions with legitimate tradeoffs. Strategy, research, multi-stakeholder problems.

**How it works**: Multiple specialists independently analyze the same question from their domain perspective. Each produces a position paper. The orchestrator synthesizes these perspectives into a unified recommendation, explicitly noting where experts agreed, disagreed, and what tradeoffs were made.

### Template for ORCHESTRATOR.md

```markdown
## Coordination Protocol: Expert Debate

### Flow
1. **Framing** — Orchestrator defines the question and distributes it to all relevant specialists
2. **Independent Analysis** — Each specialist analyzes from their domain perspective (no collaboration at this stage)
3. **Position Papers** — Each specialist submits:
   - Their assessment/recommendation
   - Key evidence and reasoning
   - Risks they foresee
   - What they'd need from other specialists to increase confidence
4. **Cross-examination** — Each specialist reviews others' positions and submits:
   - Points of agreement
   - Points of disagreement with reasoning
   - Questions for other specialists
5. **Synthesis** — Orchestrator produces a unified recommendation that:
   - Notes consensus areas (high confidence)
   - Notes disagreement areas with each perspective represented fairly
   - Makes an explicit tradeoff decision with reasoning
   - Identifies what additional data would resolve remaining disagreements

### Rules
- Independent analysis phase must happen before cross-examination (prevent groupthink)
- Every disagreement must be documented, not silently resolved
- Orchestrator's synthesis must acknowledge uncertainty, not pretend consensus exists where it doesn't
- Minority opinions get documented — they're often right when conditions change
```

---

## 3. Pipeline

**Best for**: Well-defined sequential workflows. Data processing, content production, build-test-deploy cycles.

**How it works**: Specialists hand off work in a defined sequence. Each stage has typed inputs and outputs — the output of stage N must match the expected input of stage N+1. If a stage fails validation, it kicks back to the previous stage with a specific error description.

### Template for ORCHESTRATOR.md

```markdown
## Coordination Protocol: Pipeline

### Flow
1. **Stage Definition** — Each pipeline stage has:
   - **Input spec**: What data/artifacts this stage expects
   - **Agent**: Which specialist handles this stage
   - **Process**: What the agent does
   - **Output spec**: What data/artifacts this stage produces
   - **Validation**: How to verify the output is correct before passing downstream
2. **Execution** — Stages run sequentially. Each stage:
   - Validates its input against the input spec
   - Performs its work
   - Validates its output against the output spec
   - Passes output to the next stage
3. **Error handling** — If validation fails:
   - Input validation failure → kick back to previous stage with specific error
   - Output validation failure → retry the current stage (max 2 retries)
   - After 2 retries → escalate to orchestrator for manual intervention

### Stage Template
| Stage | Agent | Input | Output | Validation |
|-------|-------|-------|--------|------------|
| 1. Data Collection | Data Harvester | Query parameters | Raw dataset | Schema check, completeness |
| 2. Processing | [Specialist] | Raw dataset | Cleaned dataset | Type checks, null handling |
| 3. Analysis | [Specialist] | Cleaned dataset | Analysis report | Statistical validity |
| 4. Review | [Reviewer] | Analysis report | Approved report | Quality checklist |

### Rules
- Every handoff must be explicitly typed (no "just pass the data along")
- Validation happens at both ends of every handoff
- Failed validations produce actionable error messages, not generic failures
- Pipeline stages should be independently testable
```

---

## Choosing a Protocol

| Factor | Writer-Critic | Expert Debate | Pipeline |
|--------|:---:|:---:|:---:|
| Accuracy is critical | ✅ | ✅ | ⚫ |
| Multiple perspectives needed | ⚫ | ✅ | ⚫ |
| Well-defined sequential process | ⚫ | ⚫ | ✅ |
| Speed matters | ⚫ | ⚫ | ✅ |
| Creative exploration | ⚫ | ✅ | ⚫ |
| Compliance/audit trail | ✅ | ⚫ | ✅ |

✅ = Strong fit · ⚫ = Neutral or weaker fit

Hybrid approaches are fine — e.g., a Pipeline where one stage internally uses a Writer-Critic loop.
