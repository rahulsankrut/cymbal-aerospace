"""
src/boeing_clm/intelligence/conflict_detector.py — Declarative Cross-Clause Conflict & Regulatory Lockout Engine.

Evaluates `vertex-ai-demos-468803.boeing_clm.clause_conflict_rules` against active deal deviations
in BigQuery with zero LLM calls (100% deterministic rule evaluation).
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from google.cloud import bigquery

from boeing_clm.config import BQ_DATASET, BQ_LOCATION, DEFAULT_DEAL_ID, GCP_PROJECT_ID
from boeing_clm.models import CrossClauseConflict

JOB_LABELS = {"datacloud": "antigravity"}


def is_rule_triggered(
    rule: Dict[str, Any],
    selected_option_key: str,
    selected_counter_text: str,
) -> bool:
    """Deterministically evaluate whether a clause position violates a conflict or lockout rule."""
    trigger_keys = [str(k).strip().lower() for k in (rule.get("trigger_option_keys") or [])]
    forbidden_pats = [str(p).strip().lower() for p in (rule.get("forbidden_patterns") or []) if p]
    required_pats = [str(p).strip().lower() for p in (rule.get("required_patterns") or []) if p]

    opt_key = (selected_option_key or "").strip().lower()
    text_lower = (selected_counter_text or "").lower()

    has_forbidden = any(pat in text_lower for pat in forbidden_pats)
    has_required = all(pat in text_lower for pat in required_pats) if required_pats else False

    if opt_key in trigger_keys and not (has_required and not has_forbidden):
        return True
    if has_forbidden and not has_required:
        return True
    if rule.get("rule_type") == "REGULATORY_LOCKOUT" and required_pats and not has_required:
        return True
    return False


def row_to_conflict_model(rule: Dict[str, Any]) -> CrossClauseConflict:
    """Convert a BigQuery `clause_conflict_rules` row dict to a `CrossClauseConflict` Pydantic model."""
    return CrossClauseConflict(
        rule_id=rule["rule_id"],
        rule_type=rule["rule_type"],
        source_clause_id=rule["source_clause_id"],
        target_clause_id=rule["target_clause_id"],
        source_sme_team=rule["source_sme_team"],
        target_sme_team=rule["target_sme_team"],
        severity=rule["severity"],
        conflict_title=rule["conflict_title"],
        conflict_description=rule["conflict_description"],
        harmonized_option_key=rule["harmonized_option_key"],
        harmonized_resolution_text=rule["harmonized_resolution_text"],
    )


class BigQueryConflictDetector:
    """Evaluates declarative cross-clause conflict and regulatory lockout rules in live BigQuery."""

    def __init__(
        self,
        client: Optional[bigquery.Client] = None,
        project_id: str = GCP_PROJECT_ID,
        dataset: str = BQ_DATASET,
    ) -> None:
        self.project_id = project_id
        self.dataset = dataset
        self.client = client or bigquery.Client(project=project_id, location=BQ_LOCATION)

    @property
    def dataset_fqn(self) -> str:
        return f"{self.project_id}.{self.dataset}"

    def list_rules(self, source_clause_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """Fetch declarative rules from `clause_conflict_rules` in BigQuery."""
        where_clause = "WHERE source_clause_id = @source_clause_id" if source_clause_id else ""
        sql = f"""
        SELECT
          rule_id,
          rule_type,
          source_clause_id,
          target_clause_id,
          source_sme_team,
          target_sme_team,
          trigger_option_keys,
          forbidden_patterns,
          required_patterns,
          severity,
          conflict_title,
          conflict_description,
          harmonized_option_key,
          harmonized_resolution_text
        FROM `{self.dataset_fqn}.clause_conflict_rules`
        {where_clause}
        ORDER BY rule_id
        """
        params = (
            [bigquery.ScalarQueryParameter("source_clause_id", "STRING", source_clause_id)]
            if source_clause_id
            else []
        )
        job_config = bigquery.QueryJobConfig(query_parameters=params, labels=JOB_LABELS)
        rows = self.client.query(sql, job_config=job_config, location=BQ_LOCATION).result()
        return [dict(r.items()) for r in rows]

    def get_rule(self, rule_id: str) -> Dict[str, Any]:
        """Fetch a single conflict rule by `rule_id` from BigQuery."""
        sql = f"""
        SELECT
          rule_id,
          rule_type,
          source_clause_id,
          target_clause_id,
          source_sme_team,
          target_sme_team,
          trigger_option_keys,
          forbidden_patterns,
          required_patterns,
          severity,
          conflict_title,
          conflict_description,
          harmonized_option_key,
          harmonized_resolution_text
        FROM `{self.dataset_fqn}.clause_conflict_rules`
        WHERE rule_id = @rule_id
        LIMIT 1
        """
        job_config = bigquery.QueryJobConfig(
            query_parameters=[bigquery.ScalarQueryParameter("rule_id", "STRING", rule_id)],
            labels=JOB_LABELS,
        )
        rows = list(self.client.query(sql, job_config=job_config, location=BQ_LOCATION).result())
        if not rows:
            raise ValueError(f"Conflict rule '{rule_id}' not found in `{self.dataset_fqn}.clause_conflict_rules`.")
        return dict(rows[0].items())

    def evaluate_clause_submission(
        self,
        clause_id: str,
        selected_option_key: str,
        selected_counter_text: str,
    ) -> List[CrossClauseConflict]:
        """Evaluate whether a specific clause position violates any rule in `clause_conflict_rules`."""
        rules = self.list_rules(source_clause_id=clause_id)
        conflicts: List[CrossClauseConflict] = []
        for rule in rules:
            if is_rule_triggered(rule, selected_option_key, selected_counter_text):
                conflicts.append(row_to_conflict_model(rule))
        return conflicts

    def evaluate_deal_conflicts(self, deal_id: str = DEFAULT_DEAL_ID) -> List[CrossClauseConflict]:
        """
        Join `clause_conflict_rules` against `deal_clause_deviations` in live BigQuery
        and return all currently active `CrossClauseConflict` items for `deal_id`.
        """
        sql = f"""
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
        FROM `{self.dataset_fqn}.clause_conflict_rules` r
        JOIN `{self.dataset_fqn}.deal_clause_deviations` s
          ON s.deal_id = @deal_id
         AND s.clause_id = r.source_clause_id
        WHERE s.has_redline = TRUE
        ORDER BY r.rule_id
        """
        job_config = bigquery.QueryJobConfig(
            query_parameters=[bigquery.ScalarQueryParameter("deal_id", "STRING", deal_id)],
            labels=JOB_LABELS,
        )
        rows = self.client.query(sql, job_config=job_config, location=BQ_LOCATION).result()
        active_conflicts: List[CrossClauseConflict] = []
        for row in rows:
            rule_dict = dict(row.items())
            if is_rule_triggered(
                rule_dict,
                selected_option_key=rule_dict.get("source_selected_option_key", ""),
                selected_counter_text=rule_dict.get("source_selected_counter_text", ""),
            ):
                active_conflicts.append(row_to_conflict_model(rule_dict))
        return active_conflicts
