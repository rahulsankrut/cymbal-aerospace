"""
Clause segmentation and metadata alignment for Boeing GP1 / SP3 / SP5 contracts.
Supports both structured Heading 2 metadata headers and fallback section-number alignment
for generic .docx documents without metadata tags.
"""
from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Dict, Literal, Optional
from lxml import etree

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

ProformaDoc = Literal["GP1", "SP3", "SP5"]
SmeTeam = Literal["ENGINEERING", "LEGAL", "TAX", "CYBER", "PROCUREMENT"]
RiskLevel = Literal["CRITICAL", "HIGH", "MOD", "NONE"]


@dataclass(frozen=True)
class ClauseHeaderMetadata:
    clause_id: str
    proforma_doc: ProformaDoc
    clause_ref: str
    clause_title: str
    sme_team: SmeTeam
    sme_owner_label: str
    risk_level: RiskLevel
    regulatory_flag: str


# Canonical 12-clause metadata fallback registry for Boeing GP1 / SP3 / SP5
CANONICAL_CLAUSE_REGISTRY: Dict[str, ClauseHeaderMetadata] = {
    "GP1-01": ClauseHeaderMetadata(
        clause_id="GP1-01",
        proforma_doc="GP1",
        clause_ref="GP1 §1.1",
        clause_title="Definitions & Order of Precedence",
        sme_team="PROCUREMENT",
        sme_owner_label="Procurement & Subcontracts",
        risk_level="NONE",
        regulatory_flag="Cymbal Corporate GP1 Standard",
    ),
    "GP1-03": ClauseHeaderMetadata(
        clause_id="GP1-03",
        proforma_doc="GP1",
        clause_ref="GP1 §3.1",
        clause_title="Firm-Fixed-Price SOW Cap & Pricing Integrity",
        sme_team="PROCUREMENT",
        sme_owner_label="Procurement & Cost Management",
        risk_level="NONE",
        regulatory_flag="Firm-Fixed-Price SOW Lock",
    ),
    "GP1-05": ClauseHeaderMetadata(
        clause_id="GP1-05",
        proforma_doc="GP1",
        clause_ref="GP1 §5.2",
        clause_title="Packing, Marking & Aerospace Preservation",
        sme_team="ENGINEERING",
        sme_owner_label="Supplier Logistics & Packaging",
        risk_level="NONE",
        regulatory_flag="ATA Spec 300 / D6-81628",
    ),
    "GP1-07": ClauseHeaderMetadata(
        clause_id="GP1-07",
        proforma_doc="GP1",
        clause_ref="GP1 §7.1",
        clause_title="Quality Management System (AS9100 Rev D)",
        sme_team="ENGINEERING",
        sme_owner_label="Supplier Quality Assurance",
        risk_level="NONE",
        regulatory_flag="AS9100 Rev D / D6-82479",
    ),
    "GP1-09": ClauseHeaderMetadata(
        clause_id="GP1-09",
        proforma_doc="GP1",
        clause_ref="GP1 §9.1",
        clause_title="Changes & Equitable Adjustment",
        sme_team="PROCUREMENT",
        sme_owner_label="Procurement & Subcontracts",
        risk_level="NONE",
        regulatory_flag="Cymbal Corporate GP1 Standard",
    ),
    "GP1-12": ClauseHeaderMetadata(
        clause_id="GP1-12",
        proforma_doc="GP1",
        clause_ref="GP1 §12.2",
        clause_title="Warranty & FAA Source Inspection",
        sme_team="ENGINEERING",
        sme_owner_label="Engineering & QA (FAA DER)",
        risk_level="HIGH",
        regulatory_flag="FAA 14 CFR Part 21 Lockout",
    ),
    "GP1-15": ClauseHeaderMetadata(
        clause_id="GP1-15",
        proforma_doc="GP1",
        clause_ref="GP1 §15.1",
        clause_title="Termination for Convenience",
        sme_team="LEGAL",
        sme_owner_label="Corporate Legal & Commercial",
        risk_level="NONE",
        regulatory_flag="FAR 52.249-2 Aligned",
    ),
    "GP1-19": ClauseHeaderMetadata(
        clause_id="GP1-19",
        proforma_doc="GP1",
        clause_ref="GP1 §19 & §24",
        clause_title="Limitation of Liability & IP Indemnity",
        sme_team="LEGAL",
        sme_owner_label="Corporate Legal & IP",
        risk_level="CRITICAL",
        regulatory_flag="Corporate Legal Playbook Tier-1",
    ),
    "GP1-28": ClauseHeaderMetadata(
        clause_id="GP1-28",
        proforma_doc="GP1",
        clause_ref="GP1 §28.1",
        clause_title="Governing Law & Dispute Resolution",
        sme_team="LEGAL",
        sme_owner_label="Corporate Legal",
        risk_level="NONE",
        regulatory_flag="Delaware / Washington Law Standard",
    ),
    "SP3-02": ClauseHeaderMetadata(
        clause_id="SP3-02",
        proforma_doc="SP3",
        clause_ref="SP3 §2.1",
        clause_title="Export Compliance (ITAR & EAR)",
        sme_team="TAX",
        sme_owner_label="Global Trade Controls",
        risk_level="NONE",
        regulatory_flag="22 CFR 120-130 (ITAR) / 15 CFR 730-774 (EAR)",
    ),
    "SP3-04": ClauseHeaderMetadata(
        clause_id="SP3-04",
        proforma_doc="SP3",
        clause_ref="SP3 §4.1",
        clause_title="Customs, Duties & International Tariffs",
        sme_team="TAX",
        sme_owner_label="Global Tax & Trade",
        risk_level="MOD",
        regulatory_flag="Cross-Clause SOW §3.1 Dependency",
    ),
    "SP5-03": ClauseHeaderMetadata(
        clause_id="SP5-03",
        proforma_doc="SP5",
        clause_ref="SP5 §3.2",
        clause_title="Cybersecurity Incident Reporting (DFARS)",
        sme_team="CYBER",
        sme_owner_label="Supplier Cyber Defense",
        risk_level="HIGH",
        regulatory_flag="DFARS 252.204-7012 Lockout",
    ),
}

# Section number to canonical clause_id map for generic .docx without metadata tags
SECTION_NUMBER_TO_CLAUSE_ID: Dict[str, str] = {
    "1.1": "GP1-01",
    "3.1": "GP1-03",
    "5.2": "GP1-05",
    "7.1": "GP1-07",
    "9.1": "GP1-09",
    "12.2": "GP1-12",
    "15.1": "GP1-15",
    "19.1": "GP1-19",
    "19": "GP1-19",
    "28.1": "GP1-28",
    "2.1": "SP3-02",
    "4.1": "SP3-04",
    "3.2": "SP5-03",
}

_STRUCTURED_HEADER_RE = re.compile(
    r"^\[(?P<clause_id>[A-Z0-9\-]+)\]\s+"
    r"(?P<clause_ref>[^—\-]+?)\s*[—\-]\s*"
    r"(?P<clause_title>[^|]+?)"
    r"(?:\s*\|\s*(?P<kv_tail>.+))?$"
)

_LEADING_SECTION_RE = re.compile(
    r"^\s*(?:(?:Article|Section|Clause|GP1|SP3|SP5)\s*§?\s*)?(?P<sec>\d+(?:\.\d+)?)\s*(?:[—\-:\.]\s*(?P<title>[^.\n]{3,90}))?",
    re.IGNORECASE,
)


def infer_clause_metadata_from_content(
    clause_id: str,
    clause_ref: str,
    clause_title: str,
    body_text: str = "",
) -> ClauseHeaderMetadata:
    """
    Dynamically infer SME team, owner, risk level, and regulatory flag from clause title and body text
    for arbitrary new .docx contracts whose clauses are not in CANONICAL_CLAUSE_REGISTRY.
    """
    combined = f"{clause_ref} {clause_title} {body_text}".lower()
    proforma_doc = _infer_proforma_doc(clause_id, clause_ref)

    if any(k in combined for k in ("cyber", "dfars", "252.204-7012", "nist", "800-171", "cui", "incident", "forensic", "breach", "infosec")):
        sme_team: SmeTeam = "CYBER"
        sme_owner_label = "Alex Wilber (CISO Lead, Supplier Cyber Defense)"
        risk_level: RiskLevel = "HIGH"
        regulatory_flag = "DFARS 252.204-7012 / NIST SP 800-171"
    elif any(k in combined for k in ("tariff", "customs", "duty", "duties", "232", "301", "import", "export", "itar", "ear", "tax", "ddp", "incoterms")):
        sme_team = "TAX"
        sme_owner_label = "Pradeep Gupta (Director, Global Tax & Trade)"
        risk_level = "MOD"
        regulatory_flag = "Cross-Clause SOW Pricing / Trade Compliance"
    elif any(k in combined for k in ("warranty", "inspection", "faa", "14 cfr", "airworthiness", "as9100", "quality", "conformity", "der", "source inspection", "packing", "preservation")):
        sme_team = "ENGINEERING"
        sme_owner_label = "Megan Bowen (Lead Airworthiness & QA DER)"
        risk_level = "HIGH" if any(w in combined for w in ("warranty", "faa", "14 cfr", "unannounced", "airworthiness")) else "MOD"
        regulatory_flag = "FAA 14 CFR Part 21 / AS9100 Rev D"
    elif any(k in combined for k in ("liability", "indemn", "intellectual property", "patent", "copyright", "ip ", "consequential", "governing law", "dispute", "termination", "arbitration", "liquidated")):
        sme_team = "LEGAL"
        sme_owner_label = "Miriam Graham (VP Corporate Legal & IP)"
        risk_level = "CRITICAL" if any(w in combined for w in ("liability", "indemn", "cap", "uncapped")) else "MOD"
        regulatory_flag = "Corporate Legal Playbook Guardrail"
    else:
        sme_team = "PROCUREMENT"
        sme_owner_label = "Diego Siciliani (VP Procurement Finance)"
        risk_level = "MOD" if any(w in combined for w in ("price", "pricing", "discount", "payment", "surcharge", "ceiling")) else "NONE"
        regulatory_flag = "Cymbal Corporate GP1 Standard"

    return ClauseHeaderMetadata(
        clause_id=clause_id,
        proforma_doc=proforma_doc,
        clause_ref=clause_ref,
        clause_title=clause_title or f"Section {clause_ref}",
        sme_team=sme_team,
        sme_owner_label=sme_owner_label,
        risk_level=risk_level,
        regulatory_flag=regulatory_flag,
    )


def is_heading_2_paragraph(p_el: etree._Element, w_ns: str = W_NS) -> bool:
    """Return True if the <w:p> element has a Heading 2 paragraph style."""
    p_pr = p_el.find(f"{{{w_ns}}}pPr")
    if p_pr is None:
        return False
    p_style = p_pr.find(f"{{{w_ns}}}pStyle")
    if p_style is None:
        return False
    val = (p_style.get(f"{{{w_ns}}}val") or "").strip().lower().replace(" ", "")
    return val == "heading2"


def _infer_proforma_doc(clause_id: str, clause_ref: str) -> ProformaDoc:
    prefix = clause_id.split("-")[0].upper()
    if prefix in ("GP1", "SP3", "SP5"):
        return prefix  # type: ignore[return-value]
    ref_prefix = clause_ref.split()[0].upper() if clause_ref else ""
    if ref_prefix in ("GP1", "SP3", "SP5"):
        return ref_prefix  # type: ignore[return-value]
    return "GP1"


def parse_heading_metadata(heading_text: str) -> Optional[ClauseHeaderMetadata]:
    """
    Parse a structured Heading 2 string of the form:
    '[GP1-12] GP1 §12.2 — Warranty & FAA Source Inspection | SME_TEAM=ENGINEERING | OWNER=... | RISK=HIGH | REG=...'
    """
    cleaned = heading_text.strip()
    if not cleaned:
        return None

    m = _STRUCTURED_HEADER_RE.match(cleaned)
    if m:
        clause_id = m.group("clause_id").strip()
        clause_ref = m.group("clause_ref").strip()
        clause_title = m.group("clause_title").strip()
        kv_tail = m.group("kv_tail") or ""

        kv_map: Dict[str, str] = {}
        for part in kv_tail.split("|"):
            if "=" in part:
                k, v = part.split("=", 1)
                kv_map[k.strip().upper()] = v.strip()

        fallback = CANONICAL_CLAUSE_REGISTRY.get(clause_id)
        proforma_doc = _infer_proforma_doc(clause_id, clause_ref)
        sme_team = kv_map.get("SME_TEAM") or (fallback.sme_team if fallback else "PROCUREMENT")
        sme_owner_label = kv_map.get("OWNER") or (fallback.sme_owner_label if fallback else "Procurement & Subcontracts")
        risk_level = kv_map.get("RISK") or (fallback.risk_level if fallback else "NONE")
        regulatory_flag = kv_map.get("REG") or (fallback.regulatory_flag if fallback else "Cymbal Corporate GP1 Standard")

        return ClauseHeaderMetadata(
            clause_id=clause_id,
            proforma_doc=proforma_doc,
            clause_ref=clause_ref,
            clause_title=clause_title,
            sme_team=sme_team,  # type: ignore[arg-type]
            sme_owner_label=sme_owner_label,
            risk_level=risk_level,  # type: ignore[arg-type]
            regulatory_flag=regulatory_flag,
        )

    # Check if heading mentions a known clause_id or section number
    for cid, meta in CANONICAL_CLAUSE_REGISTRY.items():
        if cid in cleaned or meta.clause_ref in cleaned:
            return meta

    # Strip any trailing status tags like '[✓ ACCEPTED BY ...]' or '[CYMBAL COUNTER-PROPOSAL]'
    cleaned_no_status = re.sub(r"\s*\[(?:✓|PENDING|CYMBAL|ACCEPTED)[^\]]*\]\s*$", "", cleaned).strip()

    sec_m = _LEADING_SECTION_RE.match(cleaned_no_status)
    if sec_m:
        sec_num = sec_m.group("sec")
        mapped_id = SECTION_NUMBER_TO_CLAUSE_ID.get(sec_num)
        if mapped_id and mapped_id in CANONICAL_CLAUSE_REGISTRY:
            cand_meta = CANONICAL_CLAUSE_REGISTRY[mapped_id]
            title_words = [w.lower() for w in re.findall(r"[A-Za-z]{4,}", cand_meta.clause_title)]
            cleaned_lower = cleaned_no_status.lower()
            # Only map to canonical GP1/SP3/SP5 clause if heading has no custom title or shares at least one keyword/proforma prefix
            has_custom_title = bool(sec_m.group("title")) or ("—" in cleaned_no_status) or ("-" in cleaned_no_status)
            if not has_custom_title or cand_meta.proforma_doc.lower() in cleaned_lower or any(tw in cleaned_lower for tw in title_words):
                return cand_meta
        # Dynamic Heading 2 with an arbitrary section number (e.g. 'GP1 §6.1 — Delivery Schedule' or 'Section 2.1 — Packing')
        parts = re.split(r"\s*[—\-:]\s*", cleaned_no_status, maxsplit=1)
        clause_ref = parts[0].strip() if len(parts) > 1 else f"GP1 §{sec_num}"
        clause_title = parts[1].strip() if len(parts) > 1 else (sec_m.group("title") or cleaned_no_status).strip()
        prefix = "SP3" if "SP3" in clause_ref.upper() else ("SP5" if "SP5" in clause_ref.upper() else "GP1")
        sec_San = sec_num.split(".")[0].zfill(2)
        dyn_id = f"{prefix}-{sec_San}"
        if dyn_id in CANONICAL_CLAUSE_REGISTRY:
            dyn_id = f"DOC-{sec_num.replace('.', '_')}"
        return infer_clause_metadata_from_content(dyn_id, clause_ref, clause_title, cleaned_no_status)

    # Generic Heading 2 without a leading section number (e.g. 'Force Majeure & Excusable Delay')
    slug = re.sub(r"[^A-Z0-9]+", "-", cleaned_no_status.upper()).strip("-")[:12] or "CUSTOM"
    dyn_id = f"GP1-{slug}"
    parts = re.split(r"\s*[—\-:]\s*", cleaned_no_status, maxsplit=1)
    clause_ref = parts[0].strip() if len(parts) > 1 and len(parts[0]) <= 18 else f"GP1 §{slug[:6]}"
    clause_title = parts[1].strip() if len(parts) > 1 and len(parts[0]) <= 18 else cleaned_no_status[:80]
    return infer_clause_metadata_from_content(dyn_id, clause_ref, clause_title, cleaned_no_status)


def resolve_clause_metadata(heading_text: Optional[str], body_text: str) -> Optional[ClauseHeaderMetadata]:
    """
    Resolve ClauseHeaderMetadata from either an explicit Heading 2 string or, if absent,
    by aligning the body paragraph's leading section number (e.g. '12.2', '19.1', '4.1', '3.2', or any 'X.Y').
    """
    if heading_text:
        parsed = parse_heading_metadata(heading_text)
        if parsed is not None:
            return parsed

    body_clean = body_text.strip()
    if not body_clean:
        return None

    sec_m = _LEADING_SECTION_RE.match(body_clean)
    if sec_m:
        sec_num = sec_m.group("sec")
        mapped_id = SECTION_NUMBER_TO_CLAUSE_ID.get(sec_num)
        if mapped_id and mapped_id in CANONICAL_CLAUSE_REGISTRY:
            return CANONICAL_CLAUSE_REGISTRY[mapped_id]
        raw_title = (sec_m.group("title") or "").strip()
        if not raw_title:
            first_sent = body_clean[sec_m.end():].strip().split(".")[0][:65].strip()
            raw_title = first_sent or f"Section {sec_num}"
        prefix = "SP3" if "SP3" in body_clean[:12].upper() else ("SP5" if "SP5" in body_clean[:12].upper() else "GP1")
        sec_major = sec_num.split(".")[0].zfill(2)
        dyn_id = f"{prefix}-{sec_major}"
        if dyn_id in CANONICAL_CLAUSE_REGISTRY:
            dyn_id = f"{prefix}-{sec_num.replace('.', '_')}"
        return infer_clause_metadata_from_content(dyn_id, f"{prefix} §{sec_num}", raw_title, body_clean)

    for cid, meta in CANONICAL_CLAUSE_REGISTRY.items():
        if body_clean.startswith(cid) or body_clean.startswith(meta.clause_ref):
            return meta

    return None
