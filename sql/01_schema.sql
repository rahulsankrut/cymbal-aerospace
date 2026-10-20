-- =============================================================================
-- specs/01_bq_schema.sql — Canonical BigQuery Database Contract (FROZEN)
-- Target Dataset: vertex-ai-demos-468803.boeing_clm
-- =============================================================================

CREATE SCHEMA IF NOT EXISTS `vertex-ai-demos-468803.boeing_clm`
OPTIONS (
  location = 'US',
  description = 'Boeing CLM Precedent Intelligence, Playbook Guardrails, and Multi-SME Deal Workbench State'
);

CREATE OR REPLACE MODEL `vertex-ai-demos-468803.boeing_clm.text_embedding_005`
REMOTE WITH CONNECTION `vertex-ai-demos-468803.us.vertex_ai`
OPTIONS (ENDPOINT = 'text-embedding-005');

-- 1. Canonical Boeing Proforma Clauses & Playbook Guardrails (12 Clauses across GP1, SP3, SP5)
CREATE OR REPLACE TABLE `vertex-ai-demos-468803.boeing_clm.proforma_clauses` (
  clause_id STRING NOT NULL,
  proforma_doc STRING NOT NULL,
  clause_ref STRING NOT NULL,
  clause_title STRING NOT NULL,
  sme_team STRING NOT NULL,
  sme_owner_label STRING NOT NULL,
  risk_level STRING NOT NULL,
  standard_text STRING NOT NULL,
  fallback_tier_1_text STRING NOT NULL,
  fallback_tier_2_text STRING NOT NULL,
  regulatory_lockout BOOL NOT NULL,
  regulatory_citation STRING NOT NULL,
  guardrail_summary STRING NOT NULL,
  embedding ARRAY<FLOAT64>
);

-- 2. Historical Executed Clause Exceptions (60+ Precedents for VECTOR_SEARCH & SQL Distribution)
CREATE OR REPLACE TABLE `vertex-ai-demos-468803.boeing_clm.historical_clause_exceptions` (
  exception_id STRING NOT NULL,
  clause_id STRING NOT NULL,
  contract_id STRING NOT NULL,
  supplier_name STRING NOT NULL,
  supplier_tier STRING NOT NULL,
  boeing_program STRING NOT NULL,
  vendor_requested_redline STRING NOT NULL,
  final_agreed_language STRING NOT NULL,
  outcome_category STRING NOT NULL,
  approval_authority STRING NOT NULL,
  negotiation_notes STRING NOT NULL,
  signed_date DATE NOT NULL,
  embedding ARRAY<FLOAT64>
);

-- 3. Active Deals (Deal Metadata & M365 Links)
CREATE OR REPLACE TABLE `vertex-ai-demos-468803.boeing_clm.active_deals` (
  deal_id STRING NOT NULL,
  vendor_name STRING NOT NULL,
  supplier_tier STRING NOT NULL,
  boeing_program STRING NOT NULL,
  contract_value_usd FLOAT64 NOT NULL,
  proforma_stack STRING NOT NULL,
  pricing_model STRING NOT NULL,
  sow_cap_clause_ref STRING NOT NULL,
  sharepoint_folder_url STRING NOT NULL,
  deviation_matrix_xlsx STRING NOT NULL,
  total_clauses_parsed INT64 NOT NULL,
  untouched_clauses_count INT64 NOT NULL,
  redlined_clauses_count INT64 NOT NULL,
  status STRING NOT NULL,
  updated_at TIMESTAMP NOT NULL
);

-- 4. Deal Clause Deviations (Active State for Each Extracted Clause)
CREATE OR REPLACE TABLE `vertex-ai-demos-468803.boeing_clm.deal_clause_deviations` (
  deal_id STRING NOT NULL,
  clause_id STRING NOT NULL,
  proforma_doc STRING NOT NULL,
  clause_ref STRING NOT NULL,
  clause_title STRING NOT NULL,
  has_redline BOOL NOT NULL,
  sme_team STRING NOT NULL,
  sme_owner_label STRING NOT NULL,
  risk_level STRING NOT NULL,
  regulatory_flag STRING NOT NULL,
  boeing_baseline_text STRING NOT NULL,
  vendor_redline_text STRING NOT NULL,
  diff_html STRING NOT NULL,
  vendor_comment STRING NOT NULL,
  insertions_json STRING NOT NULL,
  deletions_json STRING NOT NULL,
  recommended_option_key STRING NOT NULL,
  recommended_counter_text STRING NOT NULL,
  selected_option_key STRING NOT NULL,
  selected_counter_text STRING NOT NULL,
  sme_status STRING NOT NULL,
  sme_reviewer STRING NOT NULL,
  sme_rationale STRING NOT NULL,
  updated_at TIMESTAMP NOT NULL
);

-- 5. Immutable Append-Only SME Review Events (Audit Log)
CREATE OR REPLACE TABLE `vertex-ai-demos-468803.boeing_clm.sme_review_events` (
  event_id STRING NOT NULL,
  deal_id STRING NOT NULL,
  clause_id STRING NOT NULL,
  sme_team STRING NOT NULL,
  actor STRING NOT NULL,
  action STRING NOT NULL,
  selected_option_key STRING NOT NULL,
  selected_counter_text STRING NOT NULL,
  rationale STRING NOT NULL,
  source_surface STRING NOT NULL,
  created_at TIMESTAMP NOT NULL
);

-- 6. Declarative Cross-Clause Conflict & Regulatory Lockout Rules
CREATE OR REPLACE TABLE `vertex-ai-demos-468803.boeing_clm.clause_conflict_rules` (
  rule_id STRING NOT NULL,
  rule_type STRING NOT NULL,
  source_clause_id STRING NOT NULL,
  target_clause_id STRING NOT NULL,
  source_sme_team STRING NOT NULL,
  target_sme_team STRING NOT NULL,
  trigger_option_keys ARRAY<STRING>,
  forbidden_patterns ARRAY<STRING>,
  required_patterns ARRAY<STRING>,
  severity STRING NOT NULL,
  conflict_title STRING NOT NULL,
  conflict_description STRING NOT NULL,
  harmonized_option_key STRING NOT NULL,
  harmonized_resolution_text STRING NOT NULL
);
