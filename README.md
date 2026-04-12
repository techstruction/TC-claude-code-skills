# TC Claude Code Skills

A curated collection of **106 Claude Code skills** gathered from across the community. Clone and run the install script to get all skills set up instantly.

---

## Quick Install

```bash
git clone https://github.com/techstruction/TC-claude-code-skills.git
cd TC-claude-code-skills
chmod +x install.sh
./install.sh
```

---

## What Are Skills?

Skills are reusable prompt modules stored in `~/.claude/skills/`. Each skill has a `SKILL.md` file with a frontmatter `description` field that tells Claude when to activate it — either automatically based on context, or explicitly via `/skill-name`. Skills can also include supporting scripts, agents, reference docs, and assets.

---

## Skill Sources

| Source | Skills | Description |
|--------|--------|-------------|
| [anthropics/skills](https://github.com/anthropics/skills) | 17 | Official Anthropic skills |
| [trailofbits/skills](https://github.com/trailofbits/skills) | 72 | Security & audit skills from Trail of Bits |
| [obra/superpowers](https://github.com/obra/superpowers) | 13 | Development workflow skills |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | 1 | Vercel web design guidelines |
| [rohunvora/x-research-skill](https://github.com/rohunvora/x-research-skill) | 1 | X/Twitter research |
| [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | 1 | Reddit fetching |
| [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | 1 | Reddit fetching |

---

## Skills by Category

### Design & Frontend

| Skill | Description |
|-------|-------------|
| `frontend-design` | Create distinctive, production-grade frontend interfaces with high design quality. Avoids generic AI aesthetics. Use for websites, landing pages, dashboards, React components, HTML/CSS layouts. |
| `canvas-design` | Create beautiful visual art in .png and .pdf documents. Use for posters, art pieces, designs, or other static visuals. |
| `algorithmic-art` | Create algorithmic/generative art using p5.js with seeded randomness and interactive parameter exploration. Use for generative art, flow fields, particle systems. |
| `web-artifacts-builder` | Build elaborate, multi-component claude.ai HTML artifacts using React, Tailwind CSS, shadcn/ui. Use for complex artifacts requiring state management or routing. |
| `theme-factory` | Style artifacts (slides, docs, HTML pages) with one of 10 pre-set themes or generate a custom theme on the fly. |
| `web-design-guidelines` | Review UI code for Web Interface Guidelines compliance. Use for accessibility audits, UX reviews, and design best practice checks. |

### Document & File Generation

| Skill | Description |
|-------|-------------|
| `pdf` | Work with PDF files: read, extract, merge, split, rotate, watermark, create, fill forms, encrypt/decrypt, extract images, OCR. |
| `docx` | Create, read, edit, and manipulate Word (.docx) files with full formatting support including TOC, headings, tracked changes, and comments. |
| `pptx` | Create, edit, and manipulate PowerPoint (.pptx) presentations. Triggers on any mention of decks, slides, or .pptx files. |
| `xlsx` | Work with spreadsheet files (.xlsx, .xlsm, .csv, .tsv): open, read, edit, create, convert, and clean tabular data. |
| `slack-gif-creator` | Create animated GIFs optimized for Slack with constraints, validation tools, and animation concepts. |

### Claude API & MCP

| Skill | Description |
|-------|-------------|
| `claude-api` | Build, debug, and optimize Claude API / Anthropic SDK applications in Python, TypeScript, Go, Java, Ruby, PHP, C#, and curl. Includes prompt caching and managed agents. |
| `mcp-builder` | Guide for creating high-quality MCP (Model Context Protocol) servers in Python (FastMCP) or Node/TypeScript. Includes best practices and evaluation scripts. |

### Development Workflow (obra/superpowers)

| Skill | Description |
|-------|-------------|
| `brainstorming` | Explore user intent and design collaboratively before any implementation. MUST be used before creative or feature work. Includes a hard gate preventing code until design is approved. |
| `writing-plans` | Write structured implementation plans from specs or requirements before touching code. |
| `executing-plans` | Execute a written implementation plan in a separate session with review checkpoints. |
| `subagent-driven-development` | Execute implementation plans with independent tasks using subagents in the current session. |
| `dispatching-parallel-agents` | Dispatch 2+ independent tasks as parallel agents when they have no shared state or sequential dependencies. |
| `test-driven-development` | Apply TDD methodology — write tests before implementation code for any feature or bugfix. |
| `systematic-debugging` | Structured debugging process to follow when encountering any bug, test failure, or unexpected behavior before proposing fixes. |
| `using-git-worktrees` | Create isolated git worktrees for feature work that needs separation from the current workspace. |
| `finishing-a-development-branch` | Guide for completing development work — structured options for merge, PR, or cleanup when implementation is done. |
| `requesting-code-review` | Prepare and verify work before requesting code review or merging. |
| `receiving-code-review` | Handle incoming code review feedback with technical rigor rather than blind agreement. |
| `verification-before-completion` | Run verification commands and confirm output before making any success claims, committing, or creating PRs. |
| `writing-skills` | Create, edit, and verify Claude Code skills before deployment. |
| `using-superpowers` | Meta-skill: establishes how to find and use all superpowers skills at conversation start. |

### Security Auditing & Analysis

| Skill | Description |
|-------|-------------|
| `agentic-actions-auditor` | Audit GitHub Actions workflows for security vulnerabilities in AI agent integrations (Claude Code Action, Gemini CLI, OpenAI Codex). Detects prompt injection risks and dangerous CI/CD configurations. |
| `audit-context-building` | Ultra-granular, line-by-line code analysis to build deep architectural context before vulnerability or bug finding. |
| `audit-prep-assistant` | Prepare codebases for security review using Trail of Bits' checklist: goals, static analysis, test coverage, dead code removal, documentation. |
| `constant-time-analysis` | Detect timing side-channel vulnerabilities in cryptographic code across C, C++, Go, Rust, Swift, Java, Kotlin, C#, PHP, JavaScript, TypeScript, Python, Ruby. |
| `differential-review` | Compare code changes and review diffs for security regressions and logic issues. |
| `entry-point-analyzer` | Analyze smart contract codebases to identify and categorize all state-changing entry points for security auditing (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm). |
| `fp-check` | Systematically verify suspected security bugs to eliminate false positives. Produces TRUE POSITIVE or FALSE POSITIVE verdicts with documented evidence. |
| `insecure-defaults` | Detect fail-open insecure defaults: hardcoded secrets, weak auth, permissive security configs that allow apps to run insecurely in production. |
| `sharp-edges` | Identify error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. |
| `supply-chain-risk-auditor` | Identify dependencies at heightened risk of exploitation or takeover. Assess supply chain attack surface and evaluate dependency health. |
| `variant-analysis` | Find similar vulnerabilities across codebases using pattern-based analysis. Build CodeQL/Semgrep queries to hunt bug variants after finding an initial issue. |
| `second-opinion` | Run external LLM code reviews (OpenAI Codex or Google Gemini CLI) on uncommitted changes, branch diffs, or specific commits. |
| `firebase-apk-scanner` | Scan Android APKs for Firebase security misconfigurations: open databases, storage buckets, auth issues, and exposed cloud functions. For authorized security research only. |
| `burpsuite-project-parser` | Search and explore Burp Suite project files (.burp) from the command line. Search headers/bodies with regex, extract findings, dump proxy history. |

### Static Analysis Tools

| Skill | Description |
|-------|-------------|
| `semgrep` | Run and work with Semgrep static analysis. |
| `semgrep-rule-creator` | Create custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. |
| `semgrep-rule-variant-creator` | Port existing Semgrep rules to additional target languages. |
| `codeql` | Work with CodeQL for code analysis and vulnerability detection. |
| `sarif-parsing` | Parse and analyze SARIF (Static Analysis Results Interchange Format) output files. |

### Fuzzing & Testing

| Skill | Description |
|-------|-------------|
| `harness-writing` | Write fuzzing harnesses for targets. |
| `aflpp` | Use AFL++ for coverage-guided fuzzing. |
| `libfuzzer` | Use libFuzzer for in-process coverage-guided fuzzing. |
| `cargo-fuzz` | Use cargo-fuzz for fuzzing Rust code. |
| `atheris` | Use Atheris for fuzzing Python code. |
| `libafl` | Use LibAFL for advanced fuzzing campaigns. |
| `ossfuzz` | Integrate with OSS-Fuzz for continuous fuzzing. |
| `ruzzy` | Use Ruzzy for fuzzing Ruby C extensions. |
| `fuzzing-dictionary` | Build fuzzing dictionaries to improve fuzzer effectiveness. |
| `fuzzing-obstacles` | Identify and work around obstacles that reduce fuzzing effectiveness. |
| `address-sanitizer` | Use AddressSanitizer to detect memory errors. |
| `coverage-analysis` | Analyze code coverage for testing completeness. |
| `constant-time-testing` | Test for constant-time implementation correctness. |
| `wycheproof` | Work with Project Wycheproof test vectors for cryptographic implementations. |
| `property-based-testing` | Apply property-based testing across multiple languages and smart contracts for stronger coverage. |
| `mutation-testing` | Configure mewt or muton mutation testing campaigns — scopes targets, tunes timeouts, optimizes runs. |
| `testing-handbook-generator` | Generate testing handbooks and documentation. |

### Smart Contract Security

| Skill | Description |
|-------|-------------|
| `algorand-vulnerability-scanner` | Scan Algorand smart contracts for 11 common vulnerabilities: rekeying attacks, unchecked fees, missing field validations, access control issues (TEAL/PyTeal). |
| `cairo-vulnerability-scanner` | Scan Cairo/StarkNet smart contracts for 6 critical vulnerabilities: felt252 arithmetic overflow, L1-L2 messaging issues, address conversion, signature replay. |
| `cosmos-vulnerability-scanner` | Scan Cosmos SDK modules and CosmWasm contracts for 25+ consensus-critical vulnerabilities including chain halts, fund loss, and state divergence. |
| `solana-vulnerability-scanner` | Scan Solana programs for 6 critical vulnerabilities: arbitrary CPI, improper PDA validation, missing signer/ownership checks, sysvar spoofing. |
| `substrate-vulnerability-scanner` | Scan Substrate/Polkadot pallets for 7 critical vulnerabilities: arithmetic overflow, panic DoS, incorrect weights, bad origin checks. |
| `ton-vulnerability-scanner` | Scan TON (The Open Network) smart contracts for 3 critical vulnerabilities: integer-as-boolean misuse, fake Jetton contracts, forward TON without gas checks. |
| `token-integration-analyzer` | Analyze token implementations for ERC20/ERC721 conformity, 20+ weird token patterns, owner privileges, and non-standard token handling. |
| `code-maturity-assessor` | Systematic code maturity assessment using Trail of Bits' 9-category framework: arithmetic, auditing, access controls, complexity, decentralization, documentation, MEV, low-level code, testing. |
| `secure-workflow-guide` | Trail of Bits' 5-step secure development workflow: Slither scans, special feature checks, visual security diagrams, fuzzing/verification properties, manual review areas. |
| `guidelines-advisor` | Smart contract development advisor based on Trail of Bits' best practices for architecture, upgradeability, testing, and dependencies. |
| `spec-to-code-compliance` | Verify code implements exactly what documentation specifies. Compare code against whitepapers, find gaps between specs and implementation. |
| `audit-prep-assistant` | Prepare codebases for security review using Trail of Bits' checklist. |

### Cryptography & Protocol Analysis

| Skill | Description |
|-------|-------------|
| `crypto-protocol-diagram` | Extract protocol message flows from source code, RFCs, papers, ProVerif, or Tamarin models and generate Mermaid sequence diagrams with cryptographic annotations. |
| `mermaid-to-proverif` | Translate Mermaid sequence diagrams of cryptographic protocols into ProVerif formal verification models (.pv files). |
| `vector-forge` | Mutation-driven cryptographic test vector generation. Find escaped mutants, generate test vectors targeting uncovered paths, compare before/after mutation kill rates. |
| `zeroize-audit` | Detect missing zeroization of sensitive data and identify zeroization removed by compiler optimizations, with assembly-level and control-flow verification. |

### Code Graph & Diagramming (Trailmark)

| Skill | Description |
|-------|-------------|
| `trailmark` | Build and query multi-language source code graphs for security analysis. Pre-analysis passes for blast radius, taint propagation, privilege boundaries, and entry point enumeration. Supports 16 languages including Solidity, Cairo, Circom, Rust, Go, Python, C/C++, TypeScript. |
| `trailmark-structural` | Full Trailmark structural analysis with all pre-analysis passes. Use for detailed structural data for a target. |
| `trailmark-summary` | Quick Trailmark summary: language detection, entry point count, dependency graph shape. |
| `diagramming-code` | Generate visual diagrams from code structures. |
| `graph-evolution` | Analyze how code graphs evolve over time. |
| `genotoxic` | Graph-informed mutation testing triage. Parse codebases with Trailmark, run mutation testing, use survived mutants and call graph data to identify false positives and fuzzing targets. |
| `audit-augmentation` | Augment security audits with automated graph-based analysis. |
| `vector-forge` | Mutation-driven test vector generation using code graph analysis. |

### Tooling & Environment

| Skill | Description |
|-------|-------------|
| `devcontainer-setup` | Create devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. |
| `modern-python` | Configure Python projects with modern tooling: uv, ruff, ty. Use when creating projects or migrating from pip/Poetry/mypy/black. |
| `seatbelt-sandboxer` | Generate minimal macOS Seatbelt sandbox configurations for isolating and restricting applications. |
| `dwarf-expert` | Expert guidance for analyzing DWARF debug files and the DWARF debug format/standard (v3-v5). |
| `dimensional-analysis` | Annotate codebases with dimensional analysis comments documenting units and decimal scaling. Prevents dimensional mismatches and catches formula bugs. |
| `git-cleanup` | Safely analyze and clean up local git branches and worktrees by categorizing them as merged, squash-merged, superseded, or active work. |
| `debug-buttercup` | Debugging assistant and guidance. |
| `claude-in-chrome-troubleshooting` | Diagnose and fix Claude in Chrome MCP extension connectivity issues when mcp__claude-in-chrome__* tools fail or behave erratically. |

### Documentation & Communication

| Skill | Description |
|-------|-------------|
| `doc-coauthoring` | Structured workflow for co-authoring documentation, proposals, technical specs, and decision docs. Efficiently transfers context and iterates toward a verified document. |
| `internal-comms` | Write all kinds of internal company communications: status reports, leadership updates, newsletters, FAQs, incident reports, project updates. |
| `brand-guidelines` | Apply Anthropic's official brand colors and typography to artifacts for consistent Anthropic look-and-feel. |

### Research & Data

| Skill | Description |
|-------|-------------|
| `x-research-skill` | Research and fetch content from X (Twitter) using the X API. Supports watchlists, caching, and formatted output. |
| `reddit-fetch` | Fetch content from Reddit using Gemini CLI or curl JSON API fallback. Handles 403/blocked errors. |

### Skill Development & Meta

| Skill | Description |
|-------|-------------|
| `skill-creator` | Create new skills, modify existing skills, and measure performance. Full eval pipeline: write → test → grade → iterate. Includes analyzer, comparator, and grader agents. |
| `skill-improver` | Iteratively review and fix Claude Code skill quality issues. Runs automated fix-review cycles until skills meet standards. |
| `designing-workflow-skills` | Design and build multi-step workflow skills. |

### Workflow Helpers

| Skill | Description |
|-------|-------------|
| `ask-questions-if-underspecified` | Clarify requirements before implementing when serious doubts arise about what's needed. |
| `let-fate-decide` | Draw 4 Tarot cards to inject entropy into planning when prompts are vague or casually delegated. Use when the user says "YOLO", "whatever", "idk", or makes nonchalant decisions. |
| `interpreting-culture-index` | Interpret Culture Index surveys and behavioral profiles. Supports individual profiles, team composition, burnout detection, hiring profiles, and conflict mediation. |

---

## Adding New Skills

To add a skill to this collection:

1. Find a skill repo or directory containing a `SKILL.md`
2. Copy the skill folder into `skills/`
3. Update the source table and skill listing in this README
4. Commit and push

To install a single skill manually:
```bash
cp -r skills/skill-name ~/.claude/skills/
```

---

## Updating Skills

To pull the latest versions from upstream sources:

```bash
# Anthropic official skills
git clone --depth=1 https://github.com/anthropics/skills.git /tmp/anthropics-skills
cp -r /tmp/anthropics-skills/skills/* ~/.claude/skills/
rm -rf /tmp/anthropics-skills

# Trail of Bits skills
git clone --depth=1 https://github.com/trailofbits/skills.git /tmp/tob-skills
find /tmp/tob-skills/plugins -name "SKILL.md" | while read f; do
  skill_dir=$(dirname "$f")
  cp -r "$skill_dir" ~/.claude/skills/
done
rm -rf /tmp/tob-skills

# obra/superpowers
git clone --depth=1 https://github.com/obra/superpowers.git /tmp/superpowers
cp -r /tmp/superpowers/skills/* ~/.claude/skills/
rm -rf /tmp/superpowers
```
