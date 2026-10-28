# ITAR Architectural Substitution Patterns for Agentic AI

Use these five architectural substitution patterns during **Phase 2 (Solution Design)** to replace non-compliant or blocked Gemini Enterprise Agent Platform components with 100% ITAR-compliant Google Cloud services.

---

## Pattern 1: Self-Hosted Agent Runtime & Sovereign Observability (Replaces Managed Agent Runtime)

### Problem
`AgentService` (Next-Gen Managed Agents / Sobi) and `InteractionsService` (Interactions API) are hard-blocked in code for ITAR projects (`ALLOW_ONLY_ITAR_COMPLIANT_APIS_ORG_POLICY` and `COMPLIANCE_CHECK_BLOCK_ITAR_PROJECT`). Legacy `ReasoningEngine` runtimes also introduce compliance friction in ITAR environments due to opaque tenant networking and coupling to blocked sandbox/memory-bundle services.

### Architectural Replacement
Decouple the **Agent Framework (`google-adk`)** from **Managed Agent Hosting**:
- Package the ADK `Agent`, `Runner`, tool definitions, and A2A server into a customer-managed container stored in CMEK-encrypted **Artifact Registry** (`artifactregistry.us-central1.rep.googleapis.com`).
- Deploy on either **Cloud Run** or **GKE Private Clusters** inside the Assured Workloads ITAR VPC Service Controls perimeter.
- Pin all LLM and embedding calls to `https://aiplatform.us.rep.googleapis.com` with implicit context caching disabled.
- Separate **Runtime vs. CI/CD Service Accounts** (`<agent>-app` runtime identity vs. `<agent>-runner` deployment identity — `google-agents-cli-deploy` pattern) and disable the default `run.app` public URL (`run.googleapis.com/invoker-iam-disabled: "false"`), fronting the service with an **Internal or Regional External Application Load Balancer + Cloud Armor WAF (`sqli-v33-stable`, XSS) + Identity-Aware Proxy (IAP)**.
- Route all outbound VPC traffic via **Direct VPC Egress** (`--vpc-egress=all-traffic`) through a subnet with **Private Google Access** (`private_ip_google_access = true`) pointing to `restricted.googleapis.com` (`199.36.153.4/30`).

### Three-Tier Sovereign Agent Observability (`google-agents-cli-observability`)
Never integrate third-party external telemetry SaaS platforms (e.g., AgentOps, Arize Phoenix Cloud, W&B Weave) in ITAR workloads. Implement three-tier US-sovereign observability:
1. **Tier 1 — Distributed Execution Tracing (`Cloud Trace`)**: Enable OpenTelemetry Cloud Trace (`otel_to_cloud=True`) to record agent orchestration spans (`invoke_agent`, `call_llm`, `execute_tool`) in US regions without exporting raw prompt payloads.
2. **Tier 2 — Privacy-Preserving Prompt & Response Logging (`Cloud Logging`)**: Configure `ADK_CAPTURE_MESSAGE_CONTENT_IN_SPANS=false` (`NO_CONTENT` mode) or route sanitized telemetry to a CMEK-encrypted **Cloud Logging Regional Bucket** in `us` after passing through **Cloud DLP** (`dlp.us.rep.googleapis.com`).
3. **Tier 3 — Conversational & Tool Analytics (`BigQuery Agent Analytics`)**: Stream structured agent turn metadata, latency, token consumption, and tool-invocation outcomes to a CMEK-encrypted **BigQuery** dataset (`bigquery.us-central1.rep.googleapis.com`) via the ADK BigQuery Agent Analytics plugin (`--bq-analytics`).

### Decision Matrix: Cloud Run vs. GKE Private Cluster

| Criterion | Option 1A: Cloud Run (`run.us-central1.rep.googleapis.com`) | Option 1B: GKE Private Cluster (`container.googleapis.com`) |
| :--- | :--- | :--- |
| **Best For** | Conversational agents, A2A microservices, async Pub/Sub workers, rapid per-project deployment | Multi-agent meshes requiring stateful pod affinity, custom GPU/TPU sidecars, or kernel-isolated `gVisor` code sandboxes |
| **Mandatory ITAR Controls** | Annotation `run.googleapis.com/ephemeral-disk-disable: "true"`, CMEK key, disabled `run.app` URL, `--ingress=internal-and-cloud-load-balancing`, `--vpc-egress=all-traffic` | Private cluster (no public node IPs), Shielded GKE Nodes, CMEK boot disks & application-layer secrets encryption, Workload Identity, `restricted` Pod Security Standards |
| **Operational Overhead** | Minimal (Serverless, scales to/from minimum instances) | Moderate to High (Cluster lifecycle, node pool management, network policies) |

---

## Pattern 2: Dual-Tier Agent Memory & Session Architecture (Replaces Sessions & Memory Bank)

### Problem
- `MemoryBundleService` (Agent Memory Bundles) is hard-blocked in code for ITAR projects.
- Gemini Enterprise built-in personalization memory (`personalization-memory`) conflicts with Zero Data Retention requirements and must be set to `FEATURE_STATE_OFF`.
- Managed `SessionService` is coupled to `ReasoningEngine`.

### Architectural Replacement
Leverage ADK's clean separation between `BaseSessionService` (short-term chronological turn history and working state) and `BaseMemoryService` (long-term cross-session semantic and episodic memory) to build a **Three-Tier ITAR Memory Architecture**:

1. **Tier 2A — Hot Working Memory & Active Session Cache (`Memorystore for Redis`)**:
   - **Service**: Memorystore for Redis (`redis.us-central1.rep.googleapis.com`) with CMEK and `TRANSIT_ENCRYPTION_MODE_SERVER_AUTHENTICATION`.
   - **Role**: Provides sub-millisecond read/write access to active conversation turns, agent scratchpad variables, and short-TTL semantic cache entries.
2. **Tier 2B — Durable Session Event Log & Long-Term Semantic Memory Bank (`AlloyDB for PostgreSQL + pgvector + ScaNN`)**:
   - **Service**: AlloyDB for PostgreSQL (`alloydb.us-central1.rep.googleapis.com`) encrypted with CMEK across primary, read pools, and backups, connected via **Private Service Connect (PSC)** or Private Services Access.
   - **Role 1 (Session Log)**: Persists immutable `sessions`, `events`, `app_states`, and `user_states` records via ADK's `DatabaseSessionService`. (Alternative: **Cloud Spanner** `spanner.us.rep.googleapis.com` for multi-region strong consistency, or **Firestore** `firestore.us.rep.googleapis.com` with `disableEnhancedTextSearch: true`).
   - **Role 2 (Long-Term Memory Bank)**: Stores extracted, deduplicated atomic facts, user preferences, and episodic summaries indexed with `pgvector` and AlloyDB's **`alloydb_scann`** index using 768-dimensional embeddings from `text-embedding-005` (`aiplatform.us.rep.googleapis.com`).
   - **AlloyDB ScaNN & Hybrid Search Tuning (`google-cloud-solution-hybrid-search-alloydb` & `alloydb-basics`)**:
     - Configure automatic index maintenance (`scann.enable_preview_features = 'on'`), size `num_leaves` to `sqrt(rows)` (up to 10M vectors) or `power(rows, 2/3)` (10M–100M+ vectors), and set query-time `scann.satisfy_limit = 'relaxed_order'` with `scann.max_pct_leaves_to_search = 15`.
     - Combine `alloydb_scann` cosine distance (`<=>`) with PostgreSQL `GIN` (`tsvector`) full-text search via **Reciprocal Rank Fusion (RRF)** so part numbers and contract clauses match with 100% lexical precision alongside semantic recall.
     - Route all agent database connections through the **AlloyDB Auth Proxy** or **AlloyDB Language Connectors** (TLS 1.3 + IAM Database Authentication `alloydb.iam.authentication = 'on'`), lock role `search_path = pg_catalog, pg_temp`, and expose database operations exclusively through **MCP Toolbox for Databases** with backend-enforced tenant filters (never raw LLM-generated `execute_sql`).
     - Enable **Multi-Zone High Availability (HA)** and **Continuous Backup & Recovery** (14–35 day window) for microsecond **Point-In-Time Recovery (PITR)** against corrupted agent memory consolidation runs.
   - **Tenant & Clearance Isolation**: Enforces PostgreSQL **Row-Level Security (RLS)** keyed on the authenticated user identity (`user_id`) and program/contract clearance attributes.
   - **Asynchronous Consolidation Pipeline**: The ADK runtime publishes a lightweight turn-completion event to **Pub/Sub** (`pubsub.us-central1.rep.googleapis.com`). A background **Cloud Run Memory Worker** consumes the event, invokes **Gemini 1.5 Flash** (`aiplatform.us.rep.googleapis.com`) to extract durable facts and resolve contradictions, embeds the consolidated facts (`text-embedding-005`), and upserts them into AlloyDB.
3. **Tier 2C — Institutional & Historical Precedent Memory (`BigQuery VECTOR_SEARCH`)**:
   - **Service**: BigQuery (`bigquery.us-central1.rep.googleapis.com`) with CMEK, Column-Level Security, and Row-Level Access Policies.
   - **Role**: Serves as the petabyte-scale analytical memory tier across millions of historical contracts, engineering change orders, or quality reports.

---

## Pattern 3: Private BYO-MCP, Dual-Gate Governance & Isolated Sandboxes (Replaces Cloud MCPs, Skill Registry & Managed Sandboxes)

### Problem
- Assured Workloads ITAR documentation explicitly prohibits Google Cloud hosted MCP servers because they lack in-use and in-transit US data residency guarantees.
- `SkillRegistryService` and `SandboxEnvironmentService` are hard-blocked in code for ITAR projects.

### Architectural Replacement
1. **Self-Hosted BYO-MCP Tool Servers**:
   - Package all enterprise integrations (ERP, PLM/Teamcenter, CLM, BigQuery, internal REST/gRPC APIs) as customer-managed **FastMCP servers** (using Streamable HTTP) or **OpenAPI 3.x microservices** running on **Cloud Run** or **GKE** inside the ITAR VPC-SC perimeter.
2. **Dual-Gate Agent Ingress & Egress Governance (`google-cloud-solution-multi-agent-security` & `apigee-agent-gateway-governance`)**:
   - **Gate 1 — Inbound Client-to-Agent (`CLIENT_TO_AGENT`)**: Place an **Internal or Regional External Application Load Balancer + Cloud Armor WAF + IAP** in front of the ADK runtime to validate Workforce Identity OIDC tokens and inspect inbound prompts via **Cloud DLP** (`dlp.us.rep.googleapis.com`).
   - **Gate 2 — Outbound Agent-to-Tool / Model (`AGENT_TO_ANYWHERE`)**: Route all outbound agent tool invocations and model calls through **Apigee X (`apigee.us.rep.googleapis.com`)** connected via **Private Service Connect (PSC) Network Attachments**.
   - **Fine-Grained MCP Tool-Level Authorization**: Use **IAP / Envoy `AuthzPolicy` CEL rules** inspecting `iap.googleapis.com/mcp.toolName` and `iap.googleapis.com/mcp.tool.isReadOnly == true` to enforce read-only vs. mutating tool access by user clearance role, and enforce **Apigee Service Extension (`ext-proc`, `EXTENSIBLE`)** policies for per-model token quotas (`llm-token-quota`) and semantic response caching.
   - Register all approved MCP and A2A endpoints in **Cloud Service Directory** (`servicedirectory.us-central1.rep.googleapis.com`) and **App Hub** (`apphub.us.rep.googleapis.com`).
3. **Isolated Code & Document Execution Sandbox (`gke-platform-security` & `gke-workload-security`)**:
   - Dispatch untrusted Python code or file-parsing tasks to a dedicated **GKE Sandbox (`gVisor`)** node pool (`--sandbox type=gvisor`) or isolated **Cloud Run Job** (`run.us-central1.rep.googleapis.com`).
   - Enforce Kubernetes **Pod Security Standards (`restricted` profile)** (`allowPrivilegeEscalation: false`, `readOnlyRootFilesystem: true`, `runAsNonRoot: true`, drop `ALL` Linux capabilities), mount secrets in-memory via **Secret Manager CSI Driver**, and apply a **GKE Dataplane V2 (Cilium) `NetworkPolicy`** with `DENY ALL` egress and `NetworkLogging` enabled.

---

## Pattern 4: ITAR-Compliant Enterprise RAG & Grounding (Replaces Public Search/Maps Grounding)

### Problem
Grounding with Google Search and Google Maps egresses outside the US compliance boundary and is excluded from ITAR (`constraints/vertexai.disableGenAIGoogleSearchGrounding = true`).

### Architectural Replacement
1. **Unstructured Document & Intranet Search (`Vertex AI Search`)**:
   - Provision **Vertex AI Search** datastores on the US multi-region endpoint (`https://discoveryengine.us.rep.googleapis.com`) backed exclusively by ITAR-compliant **Cloud Storage** (`storage.us.rep.googleapis.com`) buckets or **BigQuery** (`bigquery.us-central1.rep.googleapis.com`) datasets encrypted with CMEK inside the same VPC-SC perimeter.
2. **Custom Fine-Grained Vector RAG (`AlloyDB pgvector` or `Vertex AI Vector Search`)**:
   - For technical manuals, CAD metadata, or contract clause libraries requiring custom chunking and hybrid lexical + vector filtering, ingest documents via **Dataflow** (`dataflow.us-central1.rep.googleapis.com`) using **Gemini 1.5 Flash** multimodal parsing and index into **AlloyDB `pgvector` (`alloydb_scann`)** or **Vertex AI Vector Search** (`aiplatform.us.rep.googleapis.com` with CMEK and Private Service Connect).

---

## Pattern 5: Surfacing Custom ITAR Agents in the Gemini Enterprise App (`google-agents-cli-publish`)

### Architectural Flow
1. **Gemini Enterprise App as the Unified Frontend**:
   - Deploy the **Gemini Enterprise App** in the `us` multi-region (`discoveryengine.us.rep.googleapis.com`) within the Assured Workloads ITAR folder, with `personalization-memory`, `prompt-gallery`, `notebook-lm`, and `agent-sharing` set to `FEATURE_STATE_OFF` on the `Engine` resource.
2. **Agent-to-Agent (A2A) Registration Mode (`--registration-type a2a`)**:
   - Whereas standard Gemini Enterprise registrations default to managed Agent Engine (`--registration-type adk`), ITAR deployments **must** use **A2A Registration Mode (`--registration-type a2a`)** pointing to the self-hosted Cloud Run / Apigee Agent Card endpoint (`/a2a/app/.well-known/agent-card.json`).
   - Grant the **Discovery Engine Service Agent** (`service-<PROJECT_NUMBER>@gcp-sa-discoveryengine.iam.gserviceaccount.com`) the **`roles/run.servicesInvoker`** IAM role on the target Cloud Run service (or Internal ALB / Apigee gateway) so the Gemini Enterprise UI can invoke the self-hosted A2A agent while propagating the user's Workforce Identity OIDC token.
3. **Runtime Guardrail Gate (`Sensitive Data Protection / Cloud DLP`)**:
   - Inspect inbound prompts and outbound tool/model outputs through **Cloud DLP** (`dlp.us.rep.googleapis.com`) to redact or mask unauthorized PII or export-controlled identifiers according to program policy before logging or cross-system routing.
