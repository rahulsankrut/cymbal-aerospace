# Gemini Enterprise Agent Platform: ITAR Compliance Matrix

This reference documents the authoritative ITAR compliance posture of every component in the **Gemini Enterprise Agent Platform** and supporting Google Cloud services under Assured Workloads **ITAR (`OFFERING_ITAR`)**.

## 1. Three-Layer Enforcement Model in ITAR Environments

1. **Assured Workloads Service Allowlist (`constraints/gcp.restrictServiceUsage`)**:
   - Defined in `offering_itar/ga.textproto` and `private_ga.textproto`. Only explicitly allowlisted Google Cloud APIs can be enabled in an ITAR folder.
2. **Vertex AI Control Plane Gate (`OrgPolicyProcessor.java` & `ResourceApi.java`)**:
   - Enforces `constraints/vertexai.allowOnlyITARCompliantAPIs`.
   - Any control-plane action declaring `OrgPolicyRequirement.ALLOW_ONLY_ITAR_COMPLIANT_APIS_ORG_POLICY` is **unconditionally rejected on all endpoints** with `FAILED_PRECONDITION`.
   - All other `aiplatform.googleapis.com` control-plane actions are **confined to the US Multi-Region Regional Endpoint (`aiplatform.us.rep.googleapis.com`, `serverLocation = "us"`)**.
3. **Vertex AI Data Plane Gate (`compliance_org_policy_module.cc`)**:
   - Any RPC declaring `COMPLIANCE_CHECK_BLOCK_ITAR_PROJECT` in its proto definition is **unconditionally rejected**.
   - All inference/dataplane requests must arrive on the US multi-region endpoint (`aiplatform.us.rep.googleapis.com`).
   - On `PredictionService` (`GenerateContent`, `StreamGenerateContent`, `CountTokens`), `LlmUtilityService`, and `LlmBidiService`, any model whose ID starts with `gemini-2` (`kNonCompliantModelPrefix = "gemini-2"`) is rejected (`itar_il5_model_not_compliant`).

---

## 2. Pillar-by-Pillar Agent Platform Compliance Table

| Pillar | Component / Service | ITAR Posture | Required Endpoint / Gate | Architectural Guidance |
| :--- | :--- | :--- | :--- | :--- |
| **BUILD** | **Agent Development Kit (ADK)** & Client SDKs (`google-cloud-agentplatform`) | **COMPLIANT** | `https://aiplatform.us.rep.googleapis.com` | Client-side open-source orchestration framework. Compliant when hosted on ITAR compute (Cloud Run / GKE) and pinned to `aiplatform.us.rep.googleapis.com`. |
| **BUILD** | **Gemini 3.x Foundation Models** (`gemini-3.5-pro`, `gemini-3.5-flash`, `gemini-3.7-pro`, `gemini-3.8-flash`, `gemini-3.8-live`) | **COMPLIANT** | `https://aiplatform.us.rep.googleapis.com` | Guarantees US Data Boundary for data at rest, in transit, and in-use ML processing. Disable implicit context caching for Zero Data Retention. |
| **BUILD** | **Gemini 2.x Models** (`gemini-2.0-*`, `gemini-2.5-*`) | **BLOCKED IN CODE** | Rejected by `compliance_org_policy_module.cc` | Blocked by `kNonCompliantModelPrefix = "gemini-2"`. Always specify Gemini 3.x models. |
| **BUILD** | **Text & Multimodal Embeddings** (`text-embedding-005`, `multimodalembedding`) | **COMPLIANT** | `https://aiplatform.us.rep.googleapis.com` | Compliant when invoked via `aiplatform.us.rep.googleapis.com`. |
| **BUILD** | **Model Garden (Self-Deployed Open Models)** | **COMPLIANT** | `https://aiplatform.us.rep.googleapis.com` | Serving infrastructure (Vertex AI Online/Batch Prediction) is ITAR-authorized with CMEK and Private Service Connect. |
| **BUILD** | **Vertex AI Vector Search & RAG Engine** (`vertexragdataservice`, IndexEndpoints) | **COMPLIANT** | `https://aiplatform.us.rep.googleapis.com` | Compliant when configured with CMEK, VPC-SC, and Private Service Connect. |
| **BUILD** | **Vertex AI Search (Agent Search)** | **COMPLIANT** | `https://discoveryengine.us.rep.googleapis.com` | Compliant when indexed data stores reside in ITAR Cloud Storage or BigQuery with CMEK. |
| **BUILD** | **Interactions API** (`InteractionsService`) | **BLOCKED IN CODE** | Blocked by `COMPLIANCE_CHECK_BLOCK_ITAR_PROJECT` | Every RPC (`CreateInteraction`, `GetInteraction`, `DeleteInteraction`, etc.) is hard-blocked for ITAR projects. |
| **BUILD** | **Grounding with Google Search & Google Maps** | **EXCLUDED** | Disable via `constraints/vertexai.disableGenAIGoogleSearchGrounding` | Egresses outside boundary. Must disable Search Grounding via Org Policy and disable `mapsgrounding.googleapis.com`. |
| **BUILD** | **Imagen & Veo Media Generation** | **EXCLUDED** | Deny via `constraints/vertexai.allowedGenAIModels` | Legacy Imagen and Veo models are excluded from government/ITAR scope. |
| **SCALE** | **Gemini Enterprise App (Agentspace Platform)** | **COMPLIANT (With Feature Lockdowns)** | `https://discoveryengine.us.rep.googleapis.com` | Compliant when deployed in `us` multi-region with CMEK, VPC-SC, and unauthorized `Engine.features` turned off. |
| **SCALE** | **Managed Agent Service (Next-Gen Agent Builder / Sobi)** (`AgentService`) | **BLOCKED IN CODE** | Blocked by `ALLOW_ONLY_ITAR_COMPLIANT_APIS_ORG_POLICY` | All `CreateAgent`, `GetAgent`, `ListAgents`, `UpdateAgent`, `DeleteAgent` actions reject ITAR projects. Replace with ADK on Cloud Run / GKE. |
| **SCALE** | **Managed Agent Sandbox Environments** (`SandboxEnvironmentService`, `EnvironmentService`) | **BLOCKED IN CODE** | Blocked by `ALLOW_ONLY_ITAR_COMPLIANT_APIS_ORG_POLICY` | All sandbox creation, template, pool, and execution actions reject ITAR projects. Replace with GKE `gVisor` or locked-down Cloud Run Jobs. |
| **SCALE** | **Agent Memory Bundles (Next-Gen Managed Memory)** (`MemoryBundleService`) | **BLOCKED IN CODE** | Blocked by `ALLOW_ONLY_ITAR_COMPLIANT_APIS_ORG_POLICY` | All memory bundle CRUD, read, write, and scan actions reject ITAR projects. Replace with AlloyDB `pgvector` + Memorystore for Redis. |
| **SCALE** | **Agent Skill Registry & Collaborative Projects** (`SkillRegistryService`, `CollaborativeProjectService`) | **BLOCKED IN CODE** | Blocked by `ALLOW_ONLY_ITAR_COMPLIANT_APIS_ORG_POLICY` | All skill registry and collaborative project actions reject ITAR projects. Replace with Service Directory + App Hub. |
| **SCALE** | **Gemini Enterprise Personalization & Memory** (`personalization-memory`) | **EXCLUDED** | Set `FEATURE_STATE_OFF` on Discovery Engine `Engine` | Must disable `personalization-memory` and `personalization-suggested-highlights` on the Gemini Enterprise Engine. |
| **SCALE** | **Google Cloud Hosted MCP Servers** | **EXCLUDED** | Prohibited by Assured Workloads ITAR documentation | ITAR does not provide in-use or in-transit data residency controls for Google-hosted Cloud MCP servers. Use customer-hosted BYO-MCP on Cloud Run / GKE. |
| **SCALE** | **Gemini Enterprise Inference (Online & Batch Prediction)** | **COMPLIANT** | `https://aiplatform.us.rep.googleapis.com` | Formally in Assured Workloads ITAR scope (`PRODUCT_GEN_AI_SERVING`, `PRODUCT_VERTEX_AI_PREDICTION_ONLINE`, `PRODUCT_VERTEX_AI_PREDICTION_BATCH`). |
| **GOVERN** | **Agent Identity & Workforce Identity Federation** | **COMPLIANT** | `https://iam.googleapis.com` | Formally in Assured Workloads ITAR scope. |
| **GOVERN** | **Sensitive Data Protection (Cloud DLP)** | **COMPLIANT** | `https://dlp.us.rep.googleapis.com` | Formally in Assured Workloads ITAR scope for runtime prompt/response inspection and de-identification. |
| **GOVERN** | **Agent Registry / App Hub** | **COMPLIANT (Private GA)** | `https://apphub.us.rep.googleapis.com` | Included in `offering_itar/private_ga.textproto`. |
| **OPTIMIZE** | **Gen AI Evaluation Service & Vertex AI Pipelines** | **COMPLIANT** | `https://aiplatform.us.rep.googleapis.com` | Compliant when AutoRater judge models, evaluation datasets (BigQuery/GCS), and pipeline artifacts are pinned to `aiplatform.us.rep.googleapis.com` with CMEK. |
| **OPTIMIZE** | **Agent Observability (Cloud Logging & Monitoring)** | **COMPLIANT** | `https://logging.us.rep.googleapis.com` | Formally in Assured Workloads ITAR scope with CMEK log buckets. |
| **OPTIMIZE** | **AlphaEvolve & Google Antigravity** | **EXCLUDED** | Not in ITAR scope | Explicitly excluded from ITAR in Gemini Enterprise compliance documentation. |

---

## 3. Assured Workloads ITAR (`OFFERING_ITAR`) Approved Backing Services for Agent Architectures

All replacement patterns must draw strictly from the following ITAR-approved Google Cloud services (all requiring **CMEK** and **US regional/multi-regional endpoints**):

- **Compute & Containers**: Cloud Run (`run.us-central1.rep.googleapis.com`), Google Kubernetes Engine (`container.googleapis.com`), Compute Engine (`compute.googleapis.com`), Artifact Registry (`artifactregistry.us-central1.rep.googleapis.com`).
- **Databases & Memory**: Memorystore for Redis (`redis.us-central1.rep.googleapis.com`), AlloyDB for PostgreSQL (`alloydb.us-central1.rep.googleapis.com`), Cloud Spanner (`spanner.us.rep.googleapis.com`), Cloud SQL (`sqladmin.googleapis.com`), Firestore (`firestore.us.rep.googleapis.com`), Cloud Bigtable (`bigtable.us.rep.googleapis.com`).
- **Analytics & Enterprise Search**: BigQuery (`bigquery.us-central1.rep.googleapis.com`), Vertex AI Search / Discovery Engine (`discoveryengine.us.rep.googleapis.com`), Cloud Storage (`storage.us.rep.googleapis.com`), Dataflow (`dataflow.us-central1.rep.googleapis.com`), Dataplex (`dataplex.us-central1.rep.googleapis.com`).
- **Messaging & Orchestration**: Pub/Sub (`pubsub.us-central1.rep.googleapis.com`), Eventarc (`eventarc.us-central1.rep.googleapis.com`), Cloud Composer (`composer.us-central1.rep.googleapis.com`).
- **Networking, API & Security**: Apigee (`apigee.us.rep.googleapis.com`), Service Directory (`servicedirectory.us-central1.rep.googleapis.com`), Sensitive Data Protection / Cloud DLP (`dlp.us.rep.googleapis.com`), Cloud KMS / EKM (`cloudkms.us.rep.googleapis.com`), Secret Manager (`secretmanager.us.rep.googleapis.com`), VPC Service Controls (`accesscontextmanager.googleapis.com`).
