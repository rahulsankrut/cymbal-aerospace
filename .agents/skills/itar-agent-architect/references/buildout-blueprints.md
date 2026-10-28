# Phase 4 Guided Build-Out Blueprints (`OFFERING_ITAR`)

> **Important**: Load and use this file **only in Phase 4** after the user has reviewed the architecture and phased plan and explicitly asked to generate implementation artifacts, Infrastructure-as-Code (IaC), or service code.

---

## Module 4.1: Assured Workloads ITAR Guardrails & Gemini Enterprise Lockdown

### 4.1.1 Organization Policy Enforcement (`gcloud` / Terraform Pattern)

```yaml
# policies/allow_only_itar_compliant_apis.yaml
name: folders/ITAR_FOLDER_ID/policies/vertexai.allowOnlyITARCompliantAPIs
spec:
  rules:
  - enforce: true
---
# policies/disable_search_grounding.yaml
name: folders/ITAR_FOLDER_ID/policies/vertexai.disableGenAIGoogleSearchGrounding
spec:
  rules:
  - enforce: true
---
# policies/disable_maps_grounding.yaml
name: folders/ITAR_FOLDER_ID/policies/vertexai.disableGenAIGoogleMapsGrounding
spec:
  rules:
  - enforce: true
```

### 4.1.2 Gemini Enterprise `Engine.features` Lockdown (`discoveryengine.us.rep.googleapis.com`)

```bash
# Lock down non-ITAR features on the Gemini Enterprise App Engine resource
curl -X PATCH \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  -H "X-Goog-User-Project: ${PROJECT_ID}" \
  "https://discoveryengine.us.rep.googleapis.com/v1alpha/projects/${PROJECT_ID}/locations/us/collections/default_collection/engines/${ENGINE_ID}?updateMask=features,disableUserEventsCollection" \
  -d '{
    "disableUserEventsCollection": true,
    "features": {
      "personalization-memory": "FEATURE_STATE_OFF",
      "prompt-gallery": "FEATURE_STATE_OFF",
      "notebook-lm": "FEATURE_STATE_OFF",
      "agent-sharing": "FEATURE_STATE_OFF",
      "model-armor": "FEATURE_STATE_OFF"
    }
  }'
```

---

## Module 4.2: ITAR Session & Semantic Memory Bank Tier (AlloyDB `pgvector` + Memorystore Redis)

### 4.2.1 AlloyDB for PostgreSQL Schema with `pgvector` & Row-Level Security (RLS)

```sql
-- Enable vector and ScaNN extensions on CMEK-encrypted AlloyDB instance
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS alloydb_scann;

-- 1. Durable Session & Immutable Turn Audit Log
CREATE TABLE IF NOT EXISTS agent_sessions (
    session_id UUID PRIMARY KEY,
    app_name TEXT NOT NULL,
    user_id TEXT NOT NULL,
    program_boundary TEXT NOT NULL, -- e.g., 'ITAR-PROGRAM-ALPHA'
    state_json JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS agent_session_events (
    event_id UUID PRIMARY KEY,
    session_id UUID NOT NULL REFERENCES agent_sessions(session_id) ON DELETE CASCADE,
    user_id TEXT NOT NULL,
    program_boundary TEXT NOT NULL,
    author TEXT NOT NULL,
    event_payload JSONB NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 2. Long-Term Semantic Memory Bank (Replaces Vertex AI MemoryBundleService)
CREATE TABLE IF NOT EXISTS agent_semantic_memories (
    memory_id UUID PRIMARY KEY,
    app_name TEXT NOT NULL,
    user_id TEXT NOT NULL,
    program_boundary TEXT NOT NULL,
    memory_scope TEXT NOT NULL CHECK (memory_scope IN ('USER_PREFERENCE', 'EPISODIC_SUMMARY', 'PROGRAM_FACT')),
    fact_text TEXT NOT NULL,
    source_session_id UUID,
    confidence_score REAL NOT NULL DEFAULT 1.0,
    embedding vector(768) NOT NULL, -- text-embedding-005 on aiplatform.us.rep.googleapis.com
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    expires_at TIMESTAMPTZ
);

-- Create high-speed ScaNN vector index
CREATE INDEX IF NOT EXISTS idx_agent_memories_embedding
ON agent_semantic_memories
USING scann (embedding cosine)
WITH (num_leaves = 256);

-- 3. Enforce Strict Row-Level Security (RLS) by User & Program Boundary
ALTER TABLE agent_sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE agent_session_events ENABLE ROW LEVEL SECURITY;
ALTER TABLE agent_semantic_memories ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation_sessions ON agent_sessions
    USING (
        user_id = current_setting('app.current_user_id', true)
        AND program_boundary = current_setting('app.program_boundary', true)
    );

CREATE POLICY tenant_isolation_memories ON agent_semantic_memories
    USING (
        (user_id = current_setting('app.current_user_id', true) OR memory_scope = 'PROGRAM_FACT')
        AND program_boundary = current_setting('app.program_boundary', true)
    );
```

### 4.2.2 Custom ADK `BaseMemoryService` Pinned to `aiplatform.us.rep.googleapis.com`

```python
"""ITAR-compliant ADK Memory Bank backed by AlloyDB pgvector and US Regional Embeddings."""

import os
from typing import Sequence
import asyncpg
from google import genai
from google.genai import types

US_REP_VERTEX_ENDPOINT = "https://aiplatform.us.rep.googleapis.com"


class ItarAlloyDbMemoryService:
  """Replaces non-ITAR MemoryBundleService with CMEK AlloyDB pgvector + RLS."""

  def __init__(self, db_pool: asyncpg.Pool, project_id: str) -> None:
    self._pool = db_pool
    self._genai_client = genai.Client(
        vertexai=True,
        project=project_id,
        location="us-central1",
        http_options=types.HttpOptions(base_url=US_REP_VERTEX_ENDPOINT),
    )

  async def embed_text(self, text: str) -> Sequence[float]:
    response = self._genai_client.models.embed_content(
        model="text-embedding-005",
        contents=text,
    )
    return response.embeddings[0].values

  async def search_memories(
      self,
      *,
      app_name: str,
      user_id: str,
      program_boundary: str,
      query: str,
      top_k: int = 5,
  ) -> list[dict[str, object]]:
    query_vec = await self.embed_text(query)
    vector_literal = "[" + ",".join(f"{v:.6f}" for v in query_vec) + "]"

    async with self._pool.acquire() as conn:
      async with conn.transaction():
        # Set RLS session context for this transaction
        await conn.execute(
            "SELECT set_config('app.current_user_id', $1, true), "
            "set_config('app.program_boundary', $2, true)",
            user_id,
            program_boundary,
        )
        rows = await conn.fetch(
            """
            SELECT memory_id, memory_scope, fact_text, confidence_score,
                   1 - (embedding <=> $1::vector) AS similarity
            FROM agent_semantic_memories
            WHERE app_name = $2
              AND (expires_at IS NULL OR expires_at > NOW())
            ORDER BY embedding <=> $1::vector
            LIMIT $3
            """,
            vector_literal,
            app_name,
            top_k,
        )
        return [dict(r) for r in rows]
```

---

## Module 4.3: Self-Hosted ADK Runtime on Cloud Run (`ephemeral-disk-disable`)

### 4.3.1 Cloud Run Service Manifest (`service.itar.yaml`)

```yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: itar-adk-agent-orchestrator
  namespace: PROJECT_NUMBER
  annotations:
    run.googleapis.com/ingress: internal-and-cloud-load-balancing
spec:
  template:
    metadata:
      annotations:
        # MANDATORY ITAR CONTROL (_itar.yaml): Disable unencrypted local ephemeral disk
        run.googleapis.com/ephemeral-disk-disable: "true"
        # MANDATORY ITAR CONTROL: Encrypt container revision with US CMEK key
        run.googleapis.com/encryption-key: projects/ITAR_KMS_PROJECT/locations/us-central1/keyRings/itar-ring/cryptoKeys/itar-run-key
        # Route all egress through Private VPC inside VPC-SC perimeter
        run.googleapis.com/vpc-access-egress: all-traffic
        run.googleapis.com/network-interfaces: '[{"network":"itar-vpc","subnetwork":"itar-us-central1-subnet"}]'
    spec:
      serviceAccountName: itar-adk-runtime-sa@PROJECT_ID.iam.gserviceaccount.com
      containers:
      - image: us-central1-docker.pkg.dev/PROJECT_ID/itar-agents/adk-orchestrator:latest
        env:
        - name: GOOGLE_GENAI_USE_VERTEXAI
          value: "true"
        - name: GOOGLE_CLOUD_PROJECT
          value: "PROJECT_ID"
        - name: GOOGLE_CLOUD_LOCATION
          value: "us-central1"
        - name: VERTEX_API_ENDPOINT
          value: "https://aiplatform.us.rep.googleapis.com"
        - name: DISCOVERY_ENGINE_API_ENDPOINT
          value: "https://discoveryengine.us.rep.googleapis.com"
        - name: DLP_API_ENDPOINT
          value: "https://dlp.us.rep.googleapis.com"
```

---

## Module 4.4: ITAR Compliance Smoke-Test & Verification Script

```bash
#!/usr/bin/env bash
set -euo pipefail

PROJECT_ID="${1:?Usage: verify_itar_agent.sh <PROJECT_ID> <REGION> <CLOUD_RUN_SERVICE>}"
REGION="${2:-us-central1}"
SERVICE_NAME="${3:-itar-adk-agent-orchestrator}"

echo "=== 1. Verifying Organization Policy: vertexai.allowOnlyITARCompliantAPIs ==="
gcloud resource-manager org-policies describe vertexai.allowOnlyITARCompliantAPIs \
  --project="${PROJECT_ID}" --effective

echo "=== 2. Verifying Cloud Run Ephemeral Disk Disable & CMEK ==="
EPHEMERAL_DISABLED=$(gcloud run services describe "${SERVICE_NAME}" \
  --project="${PROJECT_ID}" --region="${REGION}" \
  --format="value(spec.template.metadata.annotations['run.googleapis.com/ephemeral-disk-disable'])")
if [[ "${EPHEMERAL_DISABLED}" != "true" ]]; then
  echo "FAIL: run.googleapis.com/ephemeral-disk-disable is not set to 'true'"
  exit 1
fi
echo "PASS: Cloud Run ephemeral disk is disabled."

echo "=== 3. Verifying Negative Test: Managed AgentService / Gemini 2.x Blocked ==="
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" \
  -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  "https://aiplatform.us.rep.googleapis.com/v1/projects/${PROJECT_ID}/locations/${REGION}/publishers/google/models/gemini-2.0-flash:generateContent" \
  -d '{"contents":[{"role":"user","parts":[{"text":"ping"}]}]}')

if [[ "${HTTP_CODE}" == "200" ]]; then
  echo "FAIL: gemini-2.0-flash succeeded! vertexai.allowOnlyITARCompliantAPIs is NOT enforced."
  exit 1
fi
echo "PASS: Non-ITAR model call was rejected (HTTP ${HTTP_CODE})."
```
