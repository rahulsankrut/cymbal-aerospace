---
name: itar-agent-architect
description: >-
  Designs ITAR-compliant agentic AI reference architectures, phased delivery
  plans, and production build-outs on Google Cloud and Gemini Enterprise Agent
  Platform using Assured Workloads (OFFERING_ITAR). Enforces an
  architecture-first workflow that replaces non-compliant managed agent
  components (Agent Engine Runtime, Memory Bundles, Managed Sandboxes, Hosted
  Cloud MCPs, Interactions API) with ITAR-authorized services (ADK on Cloud Run
  or GKE, Memorystore for Redis, AlloyDB pgvector, BigQuery Vector Search,
  Private BYO-MCP, Vertex AI US multi-region endpoints). Use when architecting,
  planning, or building ITAR, export-controlled, or defense/aerospace AI agents
  surfaced in Gemini Enterprise App or custom workbenches. Don't use for
  non-regulated commercial agent prototypes where standard global endpoints are
  permitted.
---

# ITAR Agent Architect & Build-Out Skill

Guides the end-to-end design, planning, and implementation of **ITAR-compliant (`OFFERING_ITAR`)** agentic AI systems on Google Cloud and the **Gemini Enterprise Agent Platform**.

## Why This Skill Exists (Critical Gotchas)

Without specialized guidance, agents designing Google Cloud AI architectures default to managed convenience services that **fail in ITAR environments**:

1. **Hard-Blocked Agent Platform APIs**: When `constraints/vertexai.allowOnlyITARCompliantAPIs` is active on an Assured Workloads ITAR folder, the platform's control plane and data plane **unconditionally reject** calls to:
   - **Managed Agent Service (`AgentService` / Sobi)**
   - **Interactions API (`InteractionsService`)**
   - **Managed Code/Agent Sandboxes (`SandboxEnvironmentService` / `EnvironmentService`)**
   - **Agent Memory Bundles (`MemoryBundleService`)**
   - **Agent Skill Registry & Collaborative Projects (`SkillRegistryService`, `CollaborativeProjectService`)**
   - **Gemini 2.x Models (`gemini-2*`)**
2. **Excluded by ITAR Policy**:
   - **Google Cloud Hosted MCP Servers**: Assured Workloads ITAR explicitly prohibits Google-hosted Cloud MCP servers because they lack US data residency controls for data in transit and in use.
   - **Gemini Enterprise Built-in Memory (`personalization-memory`)**: Must be set to `FEATURE_STATE_OFF` to comply with Zero Data Retention and sovereign boundary rules.
   - **Public Grounding (Google Search & Google Maps)**: Egresses outside the US compliance boundary and must be disabled via Organization Policy.
3. **Mandatory Jurisdictional Endpoint Pinning**:
   - Every compliant Vertex AI and Discovery Engine call must target the **US Multi-Region Jurisdictional Endpoint** (`https://aiplatform.us.rep.googleapis.com` and `https://discoveryengine.us.rep.googleapis.com`), never the global endpoint (`aiplatform.googleapis.com`).

---

## Core Operating Rule: Architecture-First Gatekeeping

Always respect the user's current lifecycle stage. **Never dump application code, SQL schemas, or Terraform scripts during Phases 1, 2, or 3** unless the user explicitly asks for code in that turn. Stay strictly in the **Architecture & Design Realm** until the architecture and phased delivery plan are reviewed and approved.

Copy this progress checklist into your active plan or artifact to track the engagement:

- [ ] **Phase 1: Workload & Boundary Discovery** (Requirements & ITAR scope confirmed)
- [ ] **Phase 2: ITAR Reference Architecture & Substitution Design** (Code-free architecture & Mermaid diagrams approved)
- [ ] **Phase 3: Phased Delivery & Hardening Plan** (Milestones, Org Policies & ATO checklist approved)
- [ ] **Phase 4: Guided Build-Out** (IaC, runtime, memory tier & verification generated on demand)

---

## Phase 1: Workload & Boundary Discovery (Architecture Realm)

1. **Extract Context First**: Check the conversation history, attached documents, or user prompt before asking questions. Only ask about missing architectural decisions:
   - **Use Case & Agent Topology**: Single orchestrator agent vs. multi-agent workflow (e.g., Contract Lifecycle Management, Engineering Technical Data Assistant, Supply Chain Quality Agent).
   - **Experience Surface**: Surfaced inside the **Gemini Enterprise App** (`discoveryengine.us.rep.googleapis.com`) via Agent-to-Agent (A2A) registration, or via a custom IAP-protected web workbench on Cloud Run.
   - **Memory Horizon**:
     - *Short-term working state* (active conversation turns and scratchpad variables)
     - *Long-term user/program semantic memory* (cross-session facts, user preferences, episodic summaries)
     - *Institutional precedent memory* (searching across millions of historical contracts, engineering change orders, or technical manuals)
   - **Enterprise Tooling & Execution**: Which internal systems (ERP, PLM/Teamcenter, CLM, BigQuery) must the agent invoke, and does it require isolated code/document execution?
   - **Compliance Overlay**: Standalone Assured Workloads **ITAR (`OFFERING_ITAR`)** vs. combined **ITAR + DoD IL4/IL5 or FedRAMP High**.

---

## Phase 2: ITAR Reference Architecture & Substitution Design (No Code)

1. **Audit Against the Compliance Matrix**: Load [references/compliance-matrix.md](references/compliance-matrix.md) to verify every proposed service across the 4 Agent Platform pillars (**Build, Scale, Govern, Optimize**) and confirm its required `*.us.rep.googleapis.com` regional endpoint.
2. **Apply ITAR Substitution Patterns**: Load [references/substitution-patterns.md](references/substitution-patterns.md) to map every non-compliant Agent Platform feature to an Assured Workloads ITAR-authorized pattern:
   - **Agent Runtime**: Decouple **ADK (Agent Development Kit)** from managed `AgentService`/`ReasoningEngine` and host on **Cloud Run** (`run.googleapis.com/ephemeral-disk-disable: "true"`) or **GKE Private Clusters**.
   - **Short-Term Session State**: Replace managed sessions with **Memorystore for Redis** (hot turn cache with TLS & CMEK) + **AlloyDB / Cloud Spanner / Firestore (`disableEnhancedTextSearch: true`)** for the immutable event audit log.
   - **Long-Term Memory Bank**: Replace `MemoryBundleService` and Gemini Enterprise `personalization-memory` with **AlloyDB for PostgreSQL (`pgvector` / ScaNN)** + **Row-Level Security (RLS)** + **Pub/Sub & Cloud Run asynchronous memory consolidation** (paired with **BigQuery `VECTOR_SEARCH`** for large-scale institutional precedents).
   - **Tooling & Sandboxes**: Replace Google Cloud hosted MCP servers and `SkillRegistryService` with **self-hosted BYO-MCP (Streamable HTTP) / OpenAPI services** on Cloud Run/GKE, cataloged in **Service Directory** / **App Hub** and fronted by **Apigee**. Replace `SandboxEnvironmentService` with **GKE Sandbox (`gVisor`)** zero-egress pods or locked-down **Cloud Run Jobs**.
   - **Grounding & RAG**: Replace public Search/Maps grounding with **Vertex AI Search** (`discoveryengine.us.rep.googleapis.com`) over CMEK **Cloud Storage / BigQuery** or **Vertex AI Vector Search** (`aiplatform.us.rep.googleapis.com`).
3. **Generate the Architecture Document**: Compile the design using [assets/architecture-doc-template.md](assets/architecture-doc-template.md), including:
   - End-to-end **Mermaid Architecture Topology Diagram** (`flowchart TB`) showing the Assured Workloads ITAR folder, VPC-SC perimeter, and regional endpoints.
   - End-to-end **Mermaid Request & Memory Lifecycle Diagram** (`sequenceDiagram`).
   - Component-by-component substitution table and trade-off analysis (Cloud Run vs. GKE, AlloyDB `pgvector` vs. BigQuery `VECTOR_SEARCH`).
   - **Zero application code**—keep all descriptions at the architectural, data-flow, and control-boundary level.
4. **Review Checkpoint**: Present the architecture and resolve open design choices with the user before advancing to Phase 3.

---

## Phase 3: Phased Delivery & Compliance Hardening Plan (No Application Code)

Once the architecture is aligned, load [references/hardening-checklist.md](references/hardening-checklist.md) and [assets/implementation-plan-template.md](assets/implementation-plan-template.md) to produce a structured **ITAR Delivery & Hardening Plan** across four workstreams:

1. **Workstream 1 — Assured Workloads ITAR Landing Zone & Guardrails**:
   - Assured Workloads `OFFERING_ITAR` folder provisioning, US Jurisdictional Console (`console.us.cloud.google.com`), VPC Service Controls perimeter, Private Service Connect (PSC) ingress/egress, and Cloud KMS CMEK key rings (`destroyScheduledDuration >= 30 days`).
   - Mandatory Organization Policy enforcement (`constraints/vertexai.allowOnlyITARCompliantAPIs`, `disableGenAIGoogleSearchGrounding`, `allowedGenAIModels`, `gcp.resourceLocations`, `gcp.restrictNonCmekServices`, `gcp.restrictServiceUsage`).
2. **Workstream 2 — ITAR Data, RAG & Dual-Tier Memory Foundation**:
   - Provisioning CMEK-encrypted **Memorystore for Redis**, **AlloyDB for PostgreSQL (`pgvector` + Row-Level Security)**, **Pub/Sub** memory consolidation topics, and **Vertex AI Search / BigQuery** grounding stores.
3. **Workstream 3 — Self-Hosted ADK Runtime, Sandboxes & Private BYO-MCP Tier**:
   - Deploying the containerized ADK orchestrator, async memory consolidation worker, isolated `gVisor` sandbox pool, private FastMCP/OpenAPI tool servers, **Service Directory** catalog, **Apigee** gateway, and **Cloud DLP** (`dlp.us.rep.googleapis.com`) inspection gates.
4. **Workstream 4 — Gemini Enterprise App Integration & ATO Verification**:
   - Locking down the Gemini Enterprise `Engine` resource (`personalization-memory: FEATURE_STATE_OFF`, `prompt-gallery: FEATURE_STATE_OFF`, `notebook-lm: FEATURE_STATE_OFF`, `disableUserEventsCollection: true`), registering the custom ADK agent via A2A with Workforce Identity propagation, and executing compliance verification gates.

Ask the user which workstream or component they want to build out first before entering Phase 4.

---

## Phase 4: Guided Build-Out (On Explicit Approval Only)

When the user instructs you to build out the solution (or a specific workstream), load [references/buildout-blueprints.md](references/buildout-blueprints.md) and generate modular, production-grade deliverables:

1. **Module 4.1 — Landing Zone, Org Policy & Gemini Enterprise Lockdown IaC**: Terraform and `gcloud` automation for the ITAR folder policies, CMEK keys, VPC-SC perimeter, and Discovery Engine `Engine.features` REST patch.
2. **Module 4.2 — ITAR Session & Memory Bank Tier**: AlloyDB `pgvector` DDL with Row-Level Security policies, ADK `DatabaseSessionService` + Redis write-through cache adapter, ADK `BaseMemoryService` (`pgvector` + `text-embedding-005` on `aiplatform.us.rep.googleapis.com`), and the Pub/Sub async memory consolidation worker.
3. **Module 4.3 — Self-Hosted ADK Runtime & A2A Server**: Containerized ADK `Agent` and `Runner` pinned to `https://aiplatform.us.rep.googleapis.com` with implicit caching disabled, A2A Agent Card (`/.well-known/agent.json`), and Cloud Run service YAML enforcing `run.googleapis.com/ephemeral-disk-disable: "true"`.
4. **Module 4.4 — Private BYO-MCP Tool Server & Cloud DLP Gate**: Self-hosted FastMCP server over Streamable HTTP with IAM/mTLS authentication and pre/post prompt redaction via `dlp.us.rep.googleapis.com`.
5. **Module 4.5 — ITAR Compliance Smoke-Test & Audit Script**: Automated verification checks confirming US multi-region endpoint routing, CMEK encryption on all stateful resources, RLS tenant isolation, and active rejection of non-compliant APIs/models.

---

## Bundled References & Templates

| File | When to Load |
| :--- | :--- |
| [references/compliance-matrix.md](references/compliance-matrix.md) | Phase 1 & 2: Checking which Gemini Enterprise Agent Platform & GCP services are ITAR-compliant, blocked in code, or excluded by policy |
| [references/substitution-patterns.md](references/substitution-patterns.md) | Phase 2: Designing architectural replacements for Agent Runtime, Sessions, Memory Bank, Sandboxes, Cloud MCPs, and Grounding |
| [references/hardening-checklist.md](references/hardening-checklist.md) | Phase 2 & 3: Specifying Organization Policies, CMEK rules, `Engine.features` lockdowns, and `_itar.yaml` compensating controls |
| [references/buildout-blueprints.md](references/buildout-blueprints.md) | Phase 4 ONLY: Generating IaC, AlloyDB `pgvector` + Redis ADK memory adapters, Cloud Run manifests, and verification scripts |
| [assets/architecture-doc-template.md](assets/architecture-doc-template.md) | Phase 2: Template for generating the code-free ITAR Solution Architecture Document |
| [assets/implementation-plan-template.md](assets/implementation-plan-template.md) | Phase 3: Template for generating the Phased ITAR Implementation & Hardening Plan |

---

## Companion Skills Integration Matrix

When executing each phase, pair `itar-agent-architect` with these installed companion skills (while always enforcing `itar-agent-architect`'s ITAR overrides wherever a generic skill suggests non-compliant managed Agent Runtime or Memory Bank services):

| Lifecycle Phase | Companion Skill(s) | Purpose in ITAR Engagement |
| :--- | :--- | :--- |
| **All Phases (Foundation & Docs)** | `gcloud`, `google-cloud-recipe-auth`, `retrieving-developer-knowledge`, `finding-google-skills` | From the `google-cloud-developer` plugin: `gcloud` CLI safety guardrails, ADC/IAM credential setup, and live official Google Cloud documentation lookup. |
| **Phase 1 & 2 (Discovery & Compliance Assessment)** | `assuredworkloads-environment-assessor`, `assuredworkloads-frameworks-navigator` | Non-mutating pre-flight discovery of existing GCP folders/projects (`gcloud asset search-all-resources`, effective Org Policies) against `builtin-itar` and `builtin-il5`. |
| **Phase 2 (Architecture & Diagrams)** | `google-cloud-solution-architecture`, `google-cloud-waf-security`, `ai-fde-architecture-diagrams` | Well-Architected Framework security review and conversion of Mermaid topology diagrams into presentation-grade SVG/HTML/draw.io diagrams with official GCP icons. |
| **Phase 3 (Custom Controls & Landing Zone)** | `assuredworkloads-frameworks-author`, `google-cloud-recipe-foundation-builder` | Authoring custom Detective CEL cloud controls alongside `builtin-itar` and structuring the enterprise GCP foundation. |
| **Phase 4 (ADK Runtime & Gemini Enterprise A2A)** | `google-agents-cli-workflow`, `google-agents-cli-scaffold`, `google-agents-cli-adk-code`, `google-agents-cli-deploy`, `google-agents-cli-publish`, `google-agents-cli-observability` | Scaffolding ADK code, deploying to **Cloud Run / GKE** (never managed Agent Engine), registering into **Gemini Enterprise** via A2A, and wiring Cloud Trace / BigQuery Agent Analytics. |
| **Phase 4 (ITAR Memory Bank, Sandbox & BYO-MCP)** | `google-cloud-solution-hybrid-search-alloydb`, `alloydb-basics`, `cloud-run-basics`, `gke-platform-security`, `gke-workload-security`, `google-cloud-solution-multi-agent-security`, `apigee-agent-gateway-governance`, `api-gateway-mcp-server`, `network-tf-generation` | Implementing the AlloyDB `pgvector` + ScaNN memory bank, hardened Cloud Run services, `gVisor` GKE Sandbox pods, Apigee/Agent Gateway MCP governance, and VPC/PSC Terraform. |
