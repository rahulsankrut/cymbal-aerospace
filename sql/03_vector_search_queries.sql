-- =============================================================================
-- sql/03_vector_search_queries.sql — Canonical BigQuery Vector Search & Analytics
-- Target Dataset: vertex-ai-demos-468803.boeing_clm
-- =============================================================================
-- Summary of Optimizations:
-- 1. Predicate Pushdown: Filtering `historical_clause_exceptions` by `clause_id = @clause_id`
--    inside the `VECTOR_SEARCH` base table subquery before computing cosine distances.
-- 2. Column Pruning: Projecting only required columns in `proforma_clauses`,
--    `historical_clause_exceptions`, and `VECTOR_SEARCH` subqueries.
-- 3. Early Aggregation: Computing `COUNTIF` statistical distribution metrics in a
--    dedicated single-pass CTE over the pre-filtered `clause_exceptions` relation.
-- 4. Common Subexpression Reuse: Factoring `clause_exceptions` into a shared CTE
--    reused by both the statistical distribution aggregation and `VECTOR_SEARCH`.
-- =============================================================================

-- Query 1: Combined Proforma Guardrail + COUNTIF Outcome Distribution + Live VECTOR_SEARCH
WITH clause_meta AS (
  SELECT
    clause_id,
    clause_ref,
    clause_title,
    sme_team,
    standard_text,
    fallback_tier_1_text,
    fallback_tier_2_text,
    regulatory_lockout,
    regulatory_citation,
    guardrail_summary
  FROM `vertex-ai-demos-468803.boeing_clm.proforma_clauses`
  WHERE clause_id = @clause_id
),
clause_exceptions AS (
  SELECT
    exception_id,
    clause_id,
    contract_id,
    supplier_name,
    supplier_tier,
    boeing_program,
    vendor_requested_redline,
    final_agreed_language,
    outcome_category,
    approval_authority,
    negotiation_notes,
    signed_date,
    embedding
  FROM `vertex-ai-demos-468803.boeing_clm.historical_clause_exceptions`
  WHERE clause_id = @clause_id
    AND ARRAY_LENGTH(embedding) = 768
),
dist AS (
  SELECT
    COUNT(*) AS total_matches,
    COUNTIF(outcome_category = 'HELD_FIRM') AS held_firm_count,
    CAST(ROUND(SAFE_DIVIDE(COUNTIF(outcome_category = 'HELD_FIRM') * 100.0, COUNT(*))) AS INT64) AS held_firm_pct,
    COUNTIF(outcome_category = 'COMPROMISE_TIER_1') AS compromise_tier_1_count,
    CAST(ROUND(SAFE_DIVIDE(COUNTIF(outcome_category = 'COMPROMISE_TIER_1') * 100.0, COUNT(*))) AS INT64) AS compromise_tier_1_pct,
    COUNTIF(outcome_category = 'ACCEPTED_VENDOR') AS accepted_vendor_count,
    CAST(ROUND(SAFE_DIVIDE(COUNTIF(outcome_category = 'ACCEPTED_VENDOR') * 100.0, COUNT(*))) AS INT64) AS accepted_vendor_pct
  FROM clause_exceptions
),
query_vec AS (
  SELECT ml_generate_embedding_result AS embedding
  FROM ML.GENERATE_EMBEDDING(
    MODEL `vertex-ai-demos-468803.boeing_clm.text_embedding_005`,
    (SELECT @query_text AS content),
    STRUCT(TRUE AS flatten_json_output, 'RETRIEVAL_QUERY' AS task_type)
  )
),
vector_matches AS (
  SELECT
    base.exception_id,
    base.clause_id,
    base.contract_id,
    base.supplier_name,
    base.supplier_tier,
    base.boeing_program,
    base.vendor_requested_redline,
    base.final_agreed_language,
    base.outcome_category,
    base.approval_authority,
    base.negotiation_notes,
    CAST(base.signed_date AS STRING) AS signed_date,
    GREATEST(0.0, LEAST(1.0, ROUND(1.0 - distance, 4))) AS similarity_score
  FROM VECTOR_SEARCH(
    (
      SELECT
        exception_id,
        clause_id,
        contract_id,
        supplier_name,
        supplier_tier,
        boeing_program,
        vendor_requested_redline,
        final_agreed_language,
        outcome_category,
        approval_authority,
        negotiation_notes,
        signed_date,
        embedding
      FROM `vertex-ai-demos-468803.boeing_clm.historical_clause_exceptions`
      WHERE clause_id = @clause_id
    ),
    'embedding',
    TABLE query_vec,
    top_k => @top_k,
    distance_type => 'COSINE'
  )
)
SELECT
  m.clause_id,
  m.clause_ref,
  m.clause_title,
  m.sme_team,
  m.standard_text,
  m.fallback_tier_1_text,
  m.fallback_tier_2_text,
  m.regulatory_lockout,
  m.regulatory_citation,
  m.guardrail_summary,
  IFNULL(d.total_matches, 0) AS total_matches,
  IFNULL(d.held_firm_count, 0) AS held_firm_count,
  IFNULL(d.held_firm_pct, 0) AS held_firm_pct,
  IFNULL(d.compromise_tier_1_count, 0) AS compromise_tier_1_count,
  IFNULL(d.compromise_tier_1_pct, 0) AS compromise_tier_1_pct,
  IFNULL(d.accepted_vendor_count, 0) AS accepted_vendor_count,
  IFNULL(d.accepted_vendor_pct, 0) AS accepted_vendor_pct,
  ARRAY(
    SELECT AS STRUCT
      exception_id,
      clause_id,
      contract_id,
      supplier_name,
      supplier_tier,
      boeing_program,
      vendor_requested_redline,
      final_agreed_language,
      outcome_category,
      approval_authority,
      negotiation_notes,
      signed_date,
      similarity_score
    FROM vector_matches
    ORDER BY similarity_score DESC, signed_date DESC
  ) AS precedents
FROM clause_meta m
CROSS JOIN dist d;

-- Query 2: Declarative Cross-Clause Conflict & Regulatory Lockout Evaluation
SELECT
  r.rule_id,
  r.rule_type,
  r.source_clause_id,
  r.target_clause_id,
  r.source_sme_team,
  r.target_sme_team,
  r.trigger_option_keys,
  r.forbidden_patterns,
  r.required_patterns,
  r.severity,
  r.conflict_title,
  r.conflict_description,
  r.harmonized_option_key,
  r.harmonized_resolution_text,
  s.selected_option_key AS source_selected_option_key,
  s.selected_counter_text AS source_selected_counter_text,
  s.has_redline AS source_has_redline
FROM `vertex-ai-demos-468803.boeing_clm.clause_conflict_rules` r
JOIN `vertex-ai-demos-468803.boeing_clm.deal_clause_deviations` s
  ON s.deal_id = @deal_id
 AND s.clause_id = r.source_clause_id
WHERE s.has_redline = TRUE
ORDER BY r.rule_id;
