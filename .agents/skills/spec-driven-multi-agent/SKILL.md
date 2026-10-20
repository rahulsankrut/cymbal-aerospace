---
name: spec-driven-multi-agent
description: >-
  Executes Spec-Driven Development (SDD) and parallel sub-agent orchestration
  for local Antigravity projects. Freezes database/Pydantic/API contracts first,
  dispatches isolated implementer subagents in parallel batches, and gates merge
  on independent reviewer and adversarial verifier passes.
trigger: /sdd
---

# Spec-Driven Multi-Agent Development (Local Antigravity)

Use this skill when building multi-module production systems in local Antigravity so parallel subagents build against machine-enforced contracts without integration drift or demo-ware shortcuts.

## Phase 1: Contract Freezing (Mandatory Before Implementation)

Do not dispatch any coding subagents until these 4 artifacts are committed in `specs/`:
1. **Data Schema (`specs/01_schema.sql`)**: Complete DDL for all tables, indexes, and vector models.
2. **Domain Models (`specs/02_domain_models.py`)**: Shared Pydantic v2 models (`ConfigDict(extra="forbid")`) for all internal boundaries, MCP tool I/O, and REST payloads.
3. **Service Interfaces (`specs/03_api_and_mcp_contract.md`)**: Exact MCP tool names/arguments and FastAPI routes.
4. **Golden Fixtures (`specs/04_fixtures/`)**: Real test files (e.g., `.docx` contracts with `<w:ins>`/`<w:del>` XML nodes) used for deterministic verification.

## Phase 2: Orthogonal Sub-Agent Dispatch (`[ROLE: implementer]`)

Partition implementation into modules that share **zero mutable files**:

```text
[ROLE: implementer]
GOAL: Implement <module_name> conforming strictly to specs/02_domain_models.py
SCOPE:
  - Allowed to edit: <exact_directory_or_files>
  - Read-only contracts: specs/01_schema.sql, specs/02_domain_models.py
CONSTRAINTS:
  - Never modify files in specs/
  - Never catch exceptions to return mock/hardcoded fallback data
  - All parsing, diffing, and SQL aggregations must be deterministic
VERIFICATION:
  - Run `pytest <test_file> -v` and confirm 0 failures before finishing
```

### Concurrency Rules
- **Max 3–4 Parallel Subagents**: Dispatch at most 3–4 subagents concurrently. Wait for batch completion before launching the next stage.
- **Sequential Rule for Shared Files**: If two tasks must edit the same file, run them sequentially—never in parallel.

## Phase 3: Two-Stage Independent Review (`[ROLE: reviewer]` & `[ROLE: verifier]`)

Never let the subagent that wrote the code be the final judge of its own work:
1. **Spec Compliance Audit**: Dispatch a read-only reviewer subagent to verify that all functions/endpoints strictly import and return the types in `specs/02_domain_models.py` and contain zero hardcoded mock arrays.
2. **Adversarial Verification**: Dispatch a verifier subagent to run edge-case tests (malformed documents, concurrent API writes, live database queries) and confirm end-to-end execution.
