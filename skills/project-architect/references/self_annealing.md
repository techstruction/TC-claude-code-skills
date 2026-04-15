# Self-Annealing Loop

This section is appended to every generated specialist directive. It ensures the system continuously improves from its own errors.

---

## Boilerplate (appended to every directive)

```markdown
## Self-Annealing Loop

When this agent encounters an error, unexpected result, or suboptimal outcome, follow this loop:

### 1. Identify
- Capture the exact error message, stack trace, or description of what went wrong
- Note the context: what inputs led to this failure? What was the expected vs. actual output?
- Classify the failure: API issue, data quality, logic error, edge case, or resource constraint

### 2. Fix
- Update the execution script to handle this case
- If it's a paid API or resource-consuming operation, flag for human approval before retesting
- Keep the fix minimal and targeted — don't refactor unrelated code

### 3. Test
- Re-run the exact scenario that caused the failure
- Verify the fix doesn't break existing functionality (run any related test cases)
- If the fix involves a workaround, document the root cause and ideal long-term solution

### 4. Update Directive
- Add the failure scenario to the "Known Edge Cases" section below
- Update any assumptions or constraints that proved wrong
- Add timing expectations if the failure was related to performance

### 5. Strengthen
- The system is now more robust. This directive and its execution scripts have learned from experience.
- Each pass through this loop makes the system harder to break.

### Known Edge Cases
<!-- This section grows as the system encounters and resolves issues -->
| Date | Issue | Resolution | Script Updated |
|------|-------|------------|----------------|
| _System initialized_ | — | — | — |
```

---

## Why This Matters

LLMs are probabilistic — they'll make different mistakes on different runs. Deterministic scripts, once fixed, stay fixed. By pushing error handling into the execution layer and documenting lessons in the directive layer, each failure permanently strengthens the system.

The key discipline: **always update the directive**. A fix that only lives in code is invisible to future orchestration decisions. A fix documented in the directive means the orchestrator (and the human) can reason about what the system has learned.
