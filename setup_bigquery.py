"""
setup_bigquery.py — Seeds and verifies the live BigQuery dataset `vertex-ai-demos-468803.boeing_clm`.

Executes:
1. `specs/01_bq_schema.sql` (schema, remote embedding model `text_embedding_005`, and 6 tables)
2. `sql/02_seed_data.sql` (12 proforma clauses, 64 historical precedents, live 768-dim embeddings,
   4 conflict/lockout rules, 3 active portfolio deals: `BA-2026-AV-8921`, `BA-2026-TR-5510`, `BA-2026-LG-7740`)
3. Deterministic deal workbench initialization across all 3 portfolio deals (36 deal clause deviations)
4. Post-seed verification checks against live BigQuery.
"""
from __future__ import annotations

from pathlib import Path
import sys

from google.cloud import bigquery

PROJECT_ROOT = Path(__file__).resolve().parent
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from boeing_clm.config import BQ_DATASET, BQ_LOCATION, GCP_PROJECT_ID, SPECS_DIR
from boeing_clm.storage.repository import CANONICAL_DEAL_PROFILES, BigQueryCLMRepository


JOB_LABELS = {"datacloud": "antigravity"}


def run_sql_script(client: bigquery.Client, sql_path: Path) -> None:
    """Execute a multi-statement SQL script in BigQuery with mandatory attribution labels."""
    sql_text = sql_path.read_text(encoding="utf-8")
    job_config = bigquery.QueryJobConfig(labels=JOB_LABELS)
    print(f"[setup_bigquery] Executing {sql_path.relative_to(PROJECT_ROOT)} ...")
    query_job = client.query(sql_text, job_config=job_config, location=BQ_LOCATION)
    query_job.result()
    print(f"[setup_bigquery] Completed {sql_path.name} (job_id={query_job.job_id}).")


def verify_seed(client: bigquery.Client, project_id: str = GCP_PROJECT_ID, dataset: str = BQ_DATASET) -> dict:
    """Verify row counts and live 768-dimensional embeddings across all seeded tables."""
    verification_sql = f"""
    SELECT
      (SELECT COUNT(*) FROM `{project_id}.{dataset}.proforma_clauses`) AS proforma_count,
      (SELECT COUNTIF(ARRAY_LENGTH(embedding) = 768) FROM `{project_id}.{dataset}.proforma_clauses`) AS proforma_embedded_count,
      (SELECT COUNT(*) FROM `{project_id}.{dataset}.historical_clause_exceptions`) AS precedent_count,
      (SELECT COUNTIF(ARRAY_LENGTH(embedding) = 768) FROM `{project_id}.{dataset}.historical_clause_exceptions`) AS precedent_embedded_count,
      (SELECT COUNT(*) FROM `{project_id}.{dataset}.clause_conflict_rules`) AS conflict_rules_count,
      (SELECT COUNT(*) FROM `{project_id}.{dataset}.active_deals`) AS active_deals_count,
      (SELECT COUNT(*) FROM `{project_id}.{dataset}.deal_clause_deviations`) AS deviations_count,
      (SELECT COUNT(*) FROM `{project_id}.{dataset}.sme_review_events`) AS audit_events_count
    """
    job_config = bigquery.QueryJobConfig(labels=JOB_LABELS)
    row = next(iter(client.query(verification_sql, job_config=job_config, location=BQ_LOCATION).result()))
    summary = dict(row.items())
    print("[setup_bigquery] Verification summary:", summary)

    assert summary["proforma_count"] == 12, f"Expected 12 proforma clauses, got {summary['proforma_count']}"
    assert summary["proforma_embedded_count"] == 12, (
        f"Expected 12 embedded proforma clauses (768-dim), got {summary['proforma_embedded_count']}"
    )
    assert summary["precedent_count"] == 64, f"Expected 64 historical precedents, got {summary['precedent_count']}"
    assert summary["precedent_embedded_count"] == 64, (
        f"Expected 64 embedded historical precedents (768-dim), got {summary['precedent_embedded_count']}"
    )
    assert summary["conflict_rules_count"] == 4, f"Expected 4 conflict rules, got {summary['conflict_rules_count']}"
    assert summary["active_deals_count"] == 3, f"Expected 3 active deals, got {summary['active_deals_count']}"
    assert summary["deviations_count"] == 36, f"Expected 36 deal clause deviations, got {summary['deviations_count']}"
    assert summary["audit_events_count"] >= 13, f"Expected >=13 audit events, got {summary['audit_events_count']}"
    return summary


def main() -> None:
    client = bigquery.Client(project=GCP_PROJECT_ID, location=BQ_LOCATION)
    schema_sql = SPECS_DIR / "01_bq_schema.sql"
    seed_sql = PROJECT_ROOT / "sql" / "02_seed_data.sql"

    run_sql_script(client, schema_sql)
    run_sql_script(client, seed_sql)

    repo = BigQueryCLMRepository(project_id=GCP_PROJECT_ID, dataset=BQ_DATASET)
    for deal_id in CANONICAL_DEAL_PROFILES:
        print(f"[setup_bigquery] Seeding canonical workbench state for {deal_id} ...")
        repo.reset_deal_workbench(deal_id=deal_id, source_surface="EXPERIENCE_LAYER_UI", include_precedents=False)

    verify_seed(client, GCP_PROJECT_ID, BQ_DATASET)
    print(f"[setup_bigquery] SUCCESS: `{GCP_PROJECT_ID}.{BQ_DATASET}` is live and verified.")


if __name__ == "__main__":
    main()
