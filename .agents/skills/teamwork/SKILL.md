---
name: teamwork
description: >-
  Orchestrate a team of specialised subagents to tackle a large, multi-phase
  research or engineering goal in Antigravity. Use when the work is too large
  for a single context window: multi-milestone builds, Spec-Driven Development,
  adversarial review chains, or parallel specialist roles.
trigger: /teamwork
---

# Teamwork — Multi-Agent Orchestration for Local Antigravity

Divide a large engineering goal into specialised roles, spawn subagents for each role, coordinate handoffs, and collect verified results. The output is a structured `.agents/teamwork/` tree in your workspace.

## 1. Pre-Dispatch Rule: Freeze Specs First (Spec-Driven Development)

Before dispatching parallel `worker` subagents on code:
1. Create and freeze the shared contracts in `specs/` (e.g., database DDL `01_schema.sql`, shared Pydantic models `02_domain_models.py`, API/MCP schemas `03_interfaces.md`, and golden test fixtures `04_fixtures/`).
2. State in `BRIEFING.md` that no `worker` may alter frozen files in `specs/` without `orchestrator` approval.

## 2. Archetypes

| Archetype | Role | Naming convention |
|---|---|---|
| `sentinel` | Top-level router and monitor. Owns the BRIEFING. | `sentinel` |
| `orchestrator` | Coordinates a phase or sub-team. Locks specs & dispatches workers. | `orchestrator_phase1` |
| `worker` | Writes production code & unit tests within an isolated module scope. | `worker_ingestion`, `worker_bq`, `worker_ui` |
| `reviewer` | Reviews worker output for spec compliance and code quality. | `reviewer_m1` |
| `challenger` | Adversarial stress-testing (malformed inputs, concurrency, no-mock check). | `challenger_m1` |
| `auditor` | Independent end-to-end verification (ensures zero hardcoded/mock fallbacks). | `auditor_m1` |

## 3. Directory Structure

```text
.agents/teamwork/
├── BRIEFING.md              ← team mission, frozen spec paths, invariants
├── ORIGINAL_REQUEST.md      ← verbatim user request (immutable)
├── workflow.json            ← structured DAG of agents and handoffs
├── orchestrator/
│   ├── BRIEFING.md
│   ├── progress.md
│   └── handoff.md
├── worker_ingestion/
│   ├── DISPATCH.md          ← scoped mission, allowed files, verification command
│   └── handoff.md           ← summary of changes + test output
├── worker_bq/
│   ├── DISPATCH.md
│   └── handoff.md
└── challenger_m1/
    ├── DISPATCH.md
    └── handoff.md
```

## 4. Parallel Execution & File-Overlap Rules

1. **Zero File Overlap in Parallel**: Never dispatch two `worker` agents in parallel if they modify the same file. Partition strictly by directory/module (`src/boeing_clm/ingestion/`, `src/boeing_clm/storage/`, `src/boeing_clm/server/`).
2. **Concurrency Ceiling (Max 3–4 Workers)**: Run at most 3–4 concurrent subagents per batch to avoid rate limits.
3. **Workspace Isolation**: If subagents run conflicting build/test suites, use `Workspace: "branch"` (or separate `git worktree` directories) and merge after `reviewer` approval.

## 5. Dispatch Template (`DISPATCH.md`)

When spawning a subagent via `invoke_subagent`, write `.agents/teamwork/{agent_id}/DISPATCH.md` and pass its path in the subagent prompt:

```markdown
## {ISO_TIMESTAMP} — {agent_id}
You are `{agent_id}` (`{archetype}`).

### Must Read First
- `.agents/teamwork/ORIGINAL_REQUEST.md`
- `.agents/teamwork/BRIEFING.md`
- Frozen specs: `specs/01_schema.sql`, `specs/02_domain_models.py`

### Strict Ownership Scope
- **Allowed to create/edit**: `{allowed_paths}`
- **Forbidden to edit**: `specs/*` and any directory outside `{allowed_paths}`

### Mission & Acceptance Criteria
1. {criterion_1}
2. {criterion_2}
3. Zero hardcoded/mock fallback rule: Never swallow exceptions to return fake data.

### Verification Gate
Run `{pytest_or_cli_command}` and paste the exact output into `.agents/teamwork/{agent_id}/handoff.md`.
```

## 6. Handoff & Adversarial Review Loop

1. **Worker completes** → runs local tests → writes `.agents/teamwork/{worker_id}/handoff.md`.
2. **Reviewer reads** `handoff.md` and code diff → verifies strict adherence to `specs/02_domain_models.py` → records `verdict: "APPROVED" | "NEEDS_WORK"`.
3. **Challenger runs** adversarial checks (edge-case `.docx` inputs, concurrent API calls, grepping for forbidden hardcoded mock data) → writes `handoff.md`.
4. **Orchestrator integrates** all approved modules and runs the full end-to-end test suite.
