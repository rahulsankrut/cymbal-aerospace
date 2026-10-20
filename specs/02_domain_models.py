"""
specs/02_domain_models.py — Shared Pydantic v2 Contract (FROZEN)
Every module across Ingestion, BigQuery Storage, Precedent/Conflict Intelligence,
Exporters, FastMCP, FastAPI, and the Spark CLM CLI & Document Reviewer UI
validates against these exact models.
"""
from typing import List, Literal, Optional
from pydantic import BaseModel, ConfigDict, Field


class StrictContractModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


# 1. Output of the .docx Parser & Diff Engine
class ExtractedClauseDiff(StrictContractModel):
    clause_id: str = Field(..., description="Canonical clause ID, e.g. GP1-12, GP1-19, SP3-04, SP5-03")
    proforma_doc: Literal["GP1", "SP3", "SP5"]
    clause_ref: str = Field(..., description="Section citation, e.g. GP1 §12.2")
    clause_title: str
    sme_team: Literal["ENGINEERING", "LEGAL", "TAX", "CYBER", "PROCUREMENT"]
    sme_owner_label: str
    risk_level: Literal["CRITICAL", "HIGH", "MOD", "NONE"]
    regulatory_flag: str
    has_redline: bool = Field(..., description="True if <w:ins>, <w:del>, or text deviation exists; False if untouched")
    boeing_baseline_text: str
    vendor_redline_text: str
    insertions: List[str] = Field(default_factory=list)
    deletions: List[str] = Field(default_factory=list)
    vendor_comments: List[str] = Field(default_factory=list)
    diff_html: str = Field(..., description="HTML with <span class='diff-del'> and <span class='diff-add'> markup")


# 2. Output of BigQuery VECTOR_SEARCH & Statistical Aggregation
class OutcomeDistribution(StrictContractModel):
    total_matches: int
    held_firm_count: int
    held_firm_pct: int
    compromise_tier_1_count: int
    compromise_tier_1_pct: int
    accepted_vendor_count: int
    accepted_vendor_pct: int


class PrecedentMatchItem(StrictContractModel):
    exception_id: str
    clause_id: str
    contract_id: str
    supplier_name: str
    supplier_tier: str
    boeing_program: str
    vendor_requested_redline: str
    final_agreed_language: str
    outcome_category: Literal["HELD_FIRM", "COMPROMISE_TIER_1", "ACCEPTED_VENDOR"]
    approval_authority: str
    negotiation_notes: str
    signed_date: str
    similarity_score: float = Field(..., ge=0.0, le=1.0)


class PlaybookOption(StrictContractModel):
    option_key: Literal["hold_firm", "compromise_tier_1", "accept_vendor"]
    label: str
    badge: str
    badge_class: str
    counter_text: str


class PrecedentSearchResult(StrictContractModel):
    clause_id: str
    clause_ref: str
    clause_title: str
    sme_team: str
    guardrail_summary: str
    regulatory_lockout: bool
    regulatory_citation: str
    distribution: OutcomeDistribution
    precedents: List[PrecedentMatchItem]
    playbook_options: List[PlaybookOption]


# 3. Input from the Document Reviewer UI, Spark CLM CLI, and FastMCP Tool when an SME/Owner submits a position
class SMEReviewSubmission(StrictContractModel):
    deal_id: str = Field(default="BA-2026-AV-8921")
    clause_id: str
    sme_team: Literal["ENGINEERING", "LEGAL", "TAX", "CYBER", "PROCUREMENT"]
    selected_option_key: Literal[
        "hold_firm",
        "compromise_tier_1",
        "accept_vendor",
        "custom_harmonized",
        "custom_counter",
    ]
    selected_counter_text: str
    sme_reviewer: str = Field(..., description="Human user name attributed on the Word <w:comment> (never a system name)")
    sme_rationale: str = Field(..., description="User comment text written to word/comments.xml")
    source_surface: Literal[
        "GEMINI_AGENT_MCP",
        "EXPERIENCE_LAYER_UI",
        "SPARK_CLM_CLI",
        "DOCUMENT_REVIEWER_UI",
    ] = "EXPERIENCE_LAYER_UI"


# 4. Cross-Clause Conflict & Full Deal Workbench State served to UI, Spark Canvas & MCP
class CrossClauseConflict(StrictContractModel):
    rule_id: str
    rule_type: Literal["CROSS_CLAUSE_CONFLICT", "REGULATORY_LOCKOUT"]
    source_clause_id: str
    target_clause_id: str
    source_sme_team: str
    target_sme_team: str
    severity: Literal["CRITICAL_CONFLICT", "REGULATORY_BLOCK"]
    conflict_title: str
    conflict_description: str
    harmonized_option_key: str
    harmonized_resolution_text: str


class AuditEventItem(StrictContractModel):
    event_id: str
    deal_id: str
    clause_id: str
    sme_team: str
    actor: str
    action: str
    selected_option_key: str
    rationale: str
    source_surface: str
    created_at: str


class ClauseWorkbenchItem(StrictContractModel):
    clause_id: str
    proforma_doc: Literal["GP1", "SP3", "SP5"]
    clause_ref: str
    clause_title: str
    has_redline: bool
    sme_team: Literal["ENGINEERING", "LEGAL", "TAX", "CYBER", "PROCUREMENT"]
    sme_owner_label: str
    risk_level: Literal["CRITICAL", "HIGH", "MOD", "NONE"]
    regulatory_flag: str
    boeing_baseline_text: str
    vendor_redline_text: str
    diff_html: str
    vendor_comment: str
    recommended_option_key: str
    recommended_counter_text: str
    selected_option_key: str
    selected_counter_text: str
    sme_status: Literal["UNTOUCHED", "PENDING", "PENDING_SME", "APPROVED", "CONFLICT"]
    sme_reviewer: str
    sme_rationale: str
    precedent_analysis: Optional[PrecedentSearchResult] = None


class DealWorkbenchState(StrictContractModel):
    deal_id: str
    vendor_name: str
    supplier_tier: str
    boeing_program: str
    contract_value_usd: float
    proforma_stack: str
    pricing_model: str
    sow_cap_clause_ref: str
    sharepoint_folder_url: str
    deviation_matrix_xlsx: str
    total_clauses_parsed: int
    untouched_clauses_count: int
    redlined_clauses_count: int
    status: Literal[
        "INGESTED",
        "IN_SME_REVIEW",
        "CONFLICT_DETECTED",
        "READY_FOR_DISPATCH",
        "COUNTER_PROPOSAL_GENERATED",
    ]
    bigquery_dataset: str
    clauses: List[ClauseWorkbenchItem]
    active_conflicts: List[CrossClauseConflict]
    recent_events: List[AuditEventItem]
    updated_at: str
