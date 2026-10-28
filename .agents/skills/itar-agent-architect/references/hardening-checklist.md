# ITAR Compliance Hardening & Guardrail Checklist (`OFFERING_ITAR`)

This reference compiles the mandatory **Assured Workloads v1/v2 enrollment workflows**, **Organization Policies**, **CMEK encryption requirements**, **Gemini Enterprise `Engine.features` lockdowns**, **service-specific compensating controls**, and **Google Cloud Well-Architected Framework (WAF) 6-pillar alignment** from Google Cloud Assured Workloads ITAR (`_itar.yaml`, `deploy-gemini-gov.md`, and `cloud/assurance/common/controls/pkg/data/itar/`).

---

## 0. Greenfield vs. Brownfield Assured Workloads ITAR Enrollment (`assuredworkloads-*`)

| Enrollment Path | Target Scenario | Architectural Workflow & Controls |
| :--- | :--- | :--- |
| **Path A: Greenfield Provisioning (`Assured Workloads v1 — CONSUMER_FOLDER`)** | New agentic AI landing zone created from scratch | Provision a new Assured Workloads folder with `regime = ITAR` (`OFFERING_ITAR`). Automatically applies **Preventive** Organization Policies (`allowOnlyITARCompliantAPIs`, `resourceLocations`, `restrictNonCmekServices`) on Day 0 and binds CJIS/ITAR-vetted US-Person Cloud Customer Care personnel. |
| **Path B: Brownfield Migration (`Assured Workloads v2 / Compliance Manager — existingFolder` or `existingProject`)** | Existing GCP folders/projects being brought into ITAR compliance without breaking running workloads | 1. **Attach in Monitor (`Detective`) Mode**: Bind the ITAR Data Boundary Framework in `Detective` mode via Compliance Manager (`workload.enableComplianceMonitoring = true`).<br>2. **Run Continuous Evaluation Service (CES)**: Evaluate real-time compliance drift across `locationScore`, `serviceScore`, and `cmekScore` (`assuredworkloads-environment-assessor`).<br>3. **Remediate Drift & Upgrade to `Preventive` Mode**: Migrate non-CMEK resources, disable blocked APIs, and transition the framework to `Preventive` enforcement.<br>4. **Add Custom `Detective` Cloud Controls**: Because Google-managed Data Boundary Frameworks are immutable, author enterprise-specific CEL controls (e.g., verifying Cloud Run `ephemeral-disk-disable = "true"`) in a separate **Custom Cloud Control Framework** (`assuredworkloads-frameworks-author`) attached alongside the built-in ITAR framework. |

---

## 1. Mandatory Organization Policies on the ITAR Folder

Apply and audit these Organization Policies at the Assured Workloads ITAR folder level before deploying any agent infrastructure:

| Constraint | Required Configuration | Enforcement Purpose |
| :--- | :--- | :--- |
| **`constraints/vertexai.allowOnlyITARCompliantAPIs`** | `enforce: true` | **Hard Gate**: Blocks non-ITAR Vertex AI & Agent Platform APIs (`AgentService`, `InteractionsService`, `SandboxEnvironmentService`, `MemoryBundleService`, `SkillRegistryService`, `CollaborativeProjectService`, and `gemini-2*` models) at the API gateway. |
| **`constraints/vertexai.disableGenAIGoogleSearchGrounding`** | `enforce: true` | Prevents Gemini and agent queries from egressing to public Google Search. |
| **`constraints/vertexai.disableGenAIGoogleMapsGrounding`** | `enforce: true` | Prevents Gemini and agent queries from egressing to public Google Maps. |
| **`constraints/vertexai.allowedGenAIModels`** | Allowlist only ITAR-authorized model families (e.g., `gemini-1.5-pro`, `gemini-1.5-flash`, `text-embedding-005`) | Prevents developers or agents from invoking unauthorized model versions or partner models. |
| **`constraints/gcp.resourceLocations`** | Restrict to US locations (`in:us-locations`, `us-central1`, `us-east1`, `us-east4`, `us-west1`, `us`) | Guarantees physical data residency inside the United States. |
| **`constraints/gcp.restrictNonCmekServices`** | Deny all stateful services without a CMEK key (`storage.googleapis.com`, `bigquery.googleapis.com`, `sqladmin.googleapis.com`, `alloydb.googleapis.com`, `spanner.googleapis.com`, `redis.googleapis.com`, `pubsub.googleapis.com`, `aiplatform.googleapis.com`, `discoveryengine.googleapis.com`, `run.googleapis.com`, `container.googleapis.com`, `artifactregistry.googleapis.com`, `secretmanager.googleapis.com`, `logging.googleapis.com`) | Ensures all data at rest is encrypted with customer-managed keys in Cloud KMS (`us`). |
| **`constraints/gcp.restrictCmekCryptoKeyProjects`** | Restrict to the dedicated ITAR KMS Security Project (`projects/<itar-kms-project>`) | Ensures CMEK keys originate only from the authorized ITAR key management project. |
| **`constraints/gcp.restrictServiceUsage`** | Restrict to the `OFFERING_ITAR` approved service list | Prevents enabling out-of-scope Google Cloud APIs inside the ITAR folder. |
| **`constraints/compute.vmExternalIpAccess`** | `DENY_ALL` | Prohibits public IP addresses on Compute Engine and GKE nodes. |
| **`constraints/run.allowedIngress`** | Allow `internal` and `internal-and-cloud-load-balancing` only | Prevents unauthenticated or direct public internet access to Cloud Run agent services. |

---

## 2. Gemini Enterprise (`discoveryengine.us.rep.googleapis.com`) Hardening

When surfacing an agent in the **Gemini Enterprise App** under ITAR, apply all of the following configurations on the `us` multi-region endpoint (`https://discoveryengine.us.rep.googleapis.com`):

1. **Multi-Region CMEK Enrollment**:
   - Register the `us` multi-region Cloud KMS key via the Discovery Engine `cmekConfigs` API before creating any DataStore or Engine.
   - Ensure single-tenant CMEK separation per security domain (maximum 10 single-tenant keys per project).
2. **Disable Out-of-Scope Engine Features (`Engine.features`)**:
   - `personalization-memory`: `FEATURE_STATE_OFF` *(Mandatory — replaces built-in memory with the ITAR AlloyDB + Redis Memory Bank)*
   - `prompt-gallery`: `FEATURE_STATE_OFF` *(Mandatory — Prompt Gallery is out of ITAR scope)*
   - `notebook-lm`: `FEATURE_STATE_OFF` *(Mandatory — NotebookLM Enterprise is out of ITAR scope)*
   - `agent-sharing`: `FEATURE_STATE_OFF` *(Recommended — restricts unmanaged peer-to-peer no-code agent sharing)*
   - `model-armor`: `FEATURE_STATE_OFF` *(If Model Armor is not yet authorized in the target Assured Workloads overlay; substitute with **Cloud DLP** on `dlp.us.rep.googleapis.com`)*
3. **Disable User Event Telemetry Collection**:
   - Set `disableUserEventsCollection: true` on the Gemini Enterprise Engine to prevent user query telemetry from entering non-CMEK analytics pipelines.
4. **Enforce Source System ACLs on DataStores**:
   - Configure `aclEnabled: true` on every Vertex AI Search DataStore so retrieval strictly honors the calling user's Workforce Identity Federation / Cloud Identity groups.
5. **A2A Agent Registration & Service Agent Binding (`google-agents-cli-publish`)**:
   - Register self-hosted agents using `--registration-type a2a` pointing to `/a2a/app/.well-known/agent-card.json` and grant `roles/run.servicesInvoker` to `service-<PROJECT_NUMBER>@gcp-sa-discoveryengine.iam.gserviceaccount.com`.

---

## 3. Service-Specific Compensating Controls (`_itar.yaml` & Specialist Skills)

Each backing service used in the ITAR Agent Reference Architecture requires specific configuration attributes mandated by Assured Workloads ITAR (`_itar.yaml`) and GCP specialist security skills:

| Service | Mandatory Compensating Control | Verification Attribute / Setting |
| :--- | :--- | :--- |
| **Cloud Run** (`run.googleapis.com`) | Disable local unencrypted ephemeral disk storage (`in_memory` volume only), attach CMEK key, disable default `run.app` URL, separate `<agent>-app` runtime SA from `<agent>-runner` CI/CD SA, and route traffic via Direct VPC Egress. | Revision annotation: `run.googleapis.com/ephemeral-disk-disable: "true"`, `run.googleapis.com/encryption-key: <kms-key>`, `run.googleapis.com/invoker-iam-disabled: "false"` |
| **Vertex AI Inference** (`aiplatform.us.rep.googleapis.com`) | Pin endpoint to `https://aiplatform.us.rep.googleapis.com`. Disable implicit context caching on Gemini calls (or bind explicit `CachedContent` to CMEK). Maintain Vertex AI Zero Data Retention (ZDR). | Client `api_endpoint = "aiplatform.us.rep.googleapis.com"` |
| **Memorystore for Redis** (`redis.googleapis.com`) | Enable in-transit encryption (`SERVER_AUTHENTICATION`), enable Redis AUTH, attach a US CMEK key, and deploy inside Private Service Access / PSC. | `transitEncryptionMode: SERVER_AUTHENTICATION`, `authEnabled: true`, `customerManagedKey: <kms-key>` |
| **AlloyDB for PostgreSQL** (`alloydb.googleapis.com`) | Attach US CMEK key to primary, read pool, and backup configs; require SSL (`ENCRYPTED_ONLY`); connect via AlloyDB Auth Proxy (TLS 1.3 + IAM auth); lock `search_path = pg_catalog, pg_temp`; enable `pgvector` / `alloydb_scann` auto-maintenance, Multi-Zone HA, Continuous Backup (PITR), and Row-Level Security (RLS); expose queries via **MCP Toolbox for Databases**. | `encryptionConfig.kmsKeyName`, `sslConfig.sslMode: ENCRYPTED_ONLY`, `alloydb.iam.authentication = 'on'`, PostgreSQL `ALTER TABLE ... ENABLE ROW LEVEL SECURITY` |
| **Apigee X & IAP Tool Governance** (`apigee.googleapis.com` / `iap.googleapis.com`) | Route `AGENT_TO_ANYWHERE` egress via Private Service Connect (PSC) Network Attachments; enforce IAP / Envoy `AuthzPolicy` CEL rules on `iap.googleapis.com/mcp.toolName` and `iap.googleapis.com/mcp.tool.isReadOnly`; configure Apigee `ext-proc` (`EXTENSIBLE`) per-model token quotas. | `AuthzPolicy` CEL expression + Apigee `LLMTokenQuota` policy |
| **Firestore** (`firestore.googleapis.com`) | If used as the session store, **Enhanced Text Search must be disabled** (`disableEnhancedTextSearch: true`) and CMEK applied. | `disableEnhancedTextSearch: true`, `cmekConfig.kmsKeyName` |
| **Cloud KMS / Cloud EKM** (`cloudkms.googleapis.com`) | All CMEK keys must reside in `us` or US regions, use **Cloud HSM** or **Cloud EKM** protection level where required, and set `destroyScheduledDuration >= 30 days` (`2592000s`). | `destroyScheduledDuration: "2592000s"`, `protectionLevel: HSM` |
| **Google Kubernetes Engine** (`container.googleapis.com`) | Private Cluster (`enablePrivateNodes: true`, `enablePrivateEndpoint: true`), Boot Disk CMEK, Application-layer Secrets Encryption (CMEK), **GKE Sandbox (`gVisor`)** node pools, `restricted` Pod Security Standards, Secret Manager CSI Driver, and Dataplane V2 `DENY ALL` egress `NetworkPolicy` with `NetworkLogging`. | `sandboxConfig.type: GVISOR`, `databaseEncryption.keyName`, `pod-security.kubernetes.io/enforce: restricted` |
| **Sovereign Agent Observability** (`logging.googleapis.com` / `cloudtrace.googleapis.com` / `bigquery.googleapis.com`) | Enable Cloud Trace (`otel_to_cloud=True`), set `ADK_CAPTURE_MESSAGE_CONTENT_IN_SPANS=false` (`NO_CONTENT`), stream structured analytics via BigQuery Agent Analytics (`--bq-analytics`) to CMEK BigQuery, and route Data Access Audit Logs (`ADMIN_READ`, `DATA_READ`, `DATA_WRITE`) to a CMEK-encrypted regional Log Bucket in `us`. Prohibit external SaaS telemetry. | Log Bucket `cmekSettings.kmsKeyName`, `location: us`, `ADK_CAPTURE_MESSAGE_CONTENT_IN_SPANS=false` |

---

## 4. Google Cloud Well-Architected Framework (WAF) 6-Pillar Alignment (`google-cloud-solution-architecture` & `google-cloud-waf-security`)

| WAF Pillar | ITAR Agent Platform Architectural Controls |
| :--- | :--- |
| **1. Security, Privacy & Compliance** | Zero-trust VPC-SC perimeter; Assured Workloads ITAR `Preventive` + `Detective` CEL controls; Cloud HSM CMEK (`destroyScheduledDuration >= 30d`); Workforce Identity OIDC propagation; AlloyDB RLS + `search_path` hardening; Dual-Gate `CLIENT_TO_AGENT` & `AGENT_TO_ANYWHERE` governance; GKE `gVisor` + `restricted` PSS; Cloud DLP redaction. |
| **2. Reliability** | Multi-region US endpoints (`aiplatform.us.rep.googleapis.com`, `discoveryengine.us.rep.googleapis.com`); AlloyDB Multi-Zone HA + microsecond PITR (14–35d window); Memorystore HA replicas; Cloud Pub/Sub Dead-Letter Queues (DLQs) for async memory consolidation; Apigee automated retry/circuit-breaking. |
| **3. Cost Optimization** | Asynchronous Pub/Sub memory consolidation using **Gemini 1.5 Flash** off the critical path; **Apigee Service Extension (`ext-proc`)** per-program token budgets (`llm-token-quota`) and semantic caching; Cloud Run scale-to-minimum-instances for bursty BYO-MCP tools. |
| **4. Operational Excellence** | Separation of `<agent>-app` runtime SA and `<agent>-runner` CI/CD SA; automated Terraform pre-deployment validation (`terraform validate`); Three-Tier Sovereign Agent Observability (Cloud Trace + `NO_CONTENT` Cloud Logging + CMEK BigQuery Agent Analytics); Compliance Manager CES drift monitoring. |
| **5. Performance Efficiency** | Sub-5ms active session state in Memorystore for Redis; AlloyDB `alloydb_scann` two-level quantization with `scann.satisfy_limit = 'relaxed_order'` and RRF hybrid search; asynchronous post-turn fact extraction keeping p95 conversational latency low. |
| **6. Sustainability** | Right-sized serverless Cloud Run execution; tiered storage offloading cold historical logs to BigQuery and Cloud Storage Autoclass; semantic caching reducing redundant LLM inference compute. |

---

## 5. Pre-ATO Verification Gate Checklist

Use these verification gates before signing off on Phase 3 or transitioning to production in Phase 4:

- [ ] **Console & Endpoint Gate**: All administrative actions use `console.us.cloud.google.com` and all SDK/REST calls target `*.us.rep.googleapis.com`.
- [ ] **Hard-Block Gate**: Calling `AgentService`, `MemoryBundleService`, `SandboxEnvironmentService`, `InteractionsService`, or a `gemini-2*` model inside the project fails with an explicit `ALLOW_ONLY_ITAR_COMPLIANT_APIS_ORG_POLICY` error.
- [ ] **Ephemeral Disk & Ingress Gate**: Every Cloud Run revision hosting an ADK agent or BYO-MCP server includes `run.googleapis.com/ephemeral-disk-disable: "true"`, has its default `run.app` URL disabled, and uses separate runtime (`-app`) and CI/CD (`-runner`) service accounts.
- [ ] **Memory Sovereignty & Database Hardening Gate**: Gemini Enterprise `personalization-memory` is confirmed `FEATURE_STATE_OFF`; all session turns and semantic memories reside in CMEK-encrypted Memorystore for Redis and AlloyDB `pgvector` (`alloydb_scann`) with Row-Level Security (RLS), AlloyDB Auth Proxy TLS 1.3 + IAM auth, locked `search_path`, PITR enabled, and **MCP Toolbox for Databases** enforcing parameterized queries.
- [ ] **Dual-Gate Tool Governance & Zero Public Egress Gate**: VPC Service Controls perimeter blocks external internet egress from all agent runtime and `gVisor` sandbox workloads (`restricted` PSS + Dataplane V2 `NetworkLogging`); Apigee + IAP CEL rules govern MCP tool access (`iap.googleapis.com/mcp.toolName`) and model token budgets; Search and Maps grounding are blocked by Organization Policy.
- [ ] **Sovereign Observability Gate**: `ADK_CAPTURE_MESSAGE_CONTENT_IN_SPANS=false` (`NO_CONTENT`) is active; Cloud Trace, CMEK Cloud Logging (`us`), and CMEK BigQuery Agent Analytics are operational with zero third-party telemetry exporters.
