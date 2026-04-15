# {{ agent_name }}

> Specialist Agent Directive — {{ project_name }}

## Mission

{{ agent_mission }}

## Inputs

- **Data sources**: {{ data_sources }}
- **Upstream dependencies**: {{ upstream_agents }}
- **Required credentials**: Listed in `.env`

## Process

1. Review incoming data/request against this directive
2. Execute using tools in `execution/` (check existing scripts before creating new ones)
3. Validate outputs against the quality criteria below
4. Provide output with citations (see Citations Required section)

## Outputs

- Primary deliverable: {{ primary_output }}
- Format: {{ output_format }}
- Destination: {{ output_destination }}

## Quality Criteria

- [ ] All claims are supported by cited data sources
- [ ] Confidence level stated (High / Medium / Low)
- [ ] Edge cases documented
- [ ] Output validated against expected schema/format

## Tools & Scripts

Check `execution/` for existing scripts before creating new ones:
- `execution/{{ agent_slug }}_*.py` — Scripts specific to this agent
- Shared utilities in `execution/utils/`

## Citations Required

All outputs from this agent must include:
- **Source**: Where the data/conclusion came from (API, document, calculation)
- **Confidence**: High/Medium/Low with reasoning
- **Timestamp**: When the data was retrieved or analysis performed
- **Verification**: How another agent can independently verify this output

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
- Verify the fix doesn't break existing functionality

### 4. Update Directive
- Add the failure scenario to the "Known Edge Cases" section below
- Update any assumptions or constraints that proved wrong

### 5. Strengthen
- The system is now more robust. This directive has learned from experience.

### Known Edge Cases

| Date | Issue | Resolution | Script Updated |
|------|-------|------------|----------------|
| _System initialized_ | — | — | — |
