-- =============================================================================
-- sql/02_seed_data.sql — Seed Canonical Cymbal Aerospace CLM Dataset in Live BigQuery
-- Target Dataset: vertex-ai-demos-468803.boeing_clm
-- =============================================================================

-- 1. Seed 12 Canonical Cymbal Aerospace Proforma Clauses (GP1, SP3, SP5)
TRUNCATE TABLE `vertex-ai-demos-468803.boeing_clm.proforma_clauses`;

INSERT INTO `vertex-ai-demos-468803.boeing_clm.proforma_clauses` (
  clause_id, proforma_doc, clause_ref, clause_title, sme_team, sme_owner_label,
  risk_level, standard_text, fallback_tier_1_text, fallback_tier_2_text,
  regulatory_lockout, regulatory_citation, guardrail_summary, embedding
)
VALUES
  (
    'GP1-01', 'GP1', 'GP1 §1.1', 'Definitions & Order of Precedence',
    'PROCUREMENT', 'Procurement & Subcontracts', 'NONE',
    '1.1 (a) Definitions: "Buyer" means Cymbal Aerospace Corporation or its wholly-owned aerospace subsidiary identified on the face of the Master Purchase Agreement (`BA-2026-AV-8921`). "Seller" means Apex AeroSystems Inc. or the legal entity furnishing Goods and flight-critical software hereunder. "Goods" means the Triple-Redundant Fly-By-Wire Flight Control Computers (`FCC-900`), Line Replaceable Units (`LRUs`), embedded DAL-A flight control firmware, and associated technical deliverables specified in Statement of Work (`SOW-AV-8921`) Schedule A. (b) Order of Precedence: In the event of any ambiguity or inconsistency among Contract documents, Special Provisions (`SP3` International & Tariff Provisions and `SP5` Cybersecurity & Defense Provisions) shall take precedence over these General Provisions (`GP1`), expressly excluding the Firm-Fixed-Price (`FFP`) unit price locks and $45,000,000 aggregate ceiling set forth in GP1 §3.1 and SOW Schedule A, which shall govern over any conflicting Special Provision unless modified by a formal bilateral Change Order.',
    '1.1 (a) Definitions: "Buyer" means Cymbal Aerospace Corporation or its wholly-owned aerospace subsidiary identified on the face of the Master Purchase Agreement (`BA-2026-AV-8921`). "Seller" means Apex AeroSystems Inc. or the legal entity furnishing Goods and flight-critical software hereunder. "Goods" means the Triple-Redundant Fly-By-Wire Flight Control Computers (`FCC-900`), Line Replaceable Units (`LRUs`), embedded DAL-A flight control firmware, and associated technical deliverables specified in Statement of Work (`SOW-AV-8921`) Schedule A. (b) Order of Precedence: In the event of any ambiguity or inconsistency among Contract documents, Special Provisions (`SP3` International & Tariff Provisions and `SP5` Cybersecurity & Defense Provisions) shall take precedence over these General Provisions (`GP1`), expressly excluding the Firm-Fixed-Price (`FFP`) unit price locks and $45,000,000 aggregate ceiling set forth in GP1 §3.1 and SOW Schedule A, which shall govern over any conflicting Special Provision unless modified by a formal bilateral Change Order.',
    '1.1 (a) Definitions: "Buyer" means Cymbal Aerospace Corporation or its wholly-owned aerospace subsidiary identified on the face of the Master Purchase Agreement (`BA-2026-AV-8921`). "Seller" means Apex AeroSystems Inc. or the legal entity furnishing Goods and flight-critical software hereunder. "Goods" means the Triple-Redundant Fly-By-Wire Flight Control Computers (`FCC-900`), Line Replaceable Units (`LRUs`), embedded DAL-A flight control firmware, and associated technical deliverables specified in Statement of Work (`SOW-AV-8921`) Schedule A. (b) Order of Precedence: In the event of any ambiguity or inconsistency among Contract documents, Special Provisions (`SP3` International & Tariff Provisions and `SP5` Cybersecurity & Defense Provisions) shall take precedence over these General Provisions (`GP1`), expressly excluding the Firm-Fixed-Price (`FFP`) unit price locks and $45,000,000 aggregate ceiling set forth in GP1 §3.1 and SOW Schedule A, which shall govern over any conflicting Special Provision unless modified by a formal bilateral Change Order.',
    FALSE, 'Cymbal Corporate GP1 Standard',
    'Maintain GP1 §3.1 Firm-Fixed-Price precedence over Special Provisions.',
    []
  ),
  (
    'GP1-03', 'GP1', 'GP1 §3.1', 'Firm-Fixed-Price SOW Cap & Pricing Integrity',
    'PROCUREMENT', 'Procurement & Cost Management', 'NONE',
    '3.1 (a) Firm-Fixed-Price Lock: Unless expressly modified by a bilateral Change Order executed by Buyer\'s Vice President of Avionics Procurement referencing this GP1 §3.1 and Statement of Work (`SOW-AV-8921`) Schedule A, all unit prices ($150,000 per shipset across 300 C780/C730-MAX shipsets) and the forty-five million dollar ($45,000,000.00) total Contract ceiling are strictly Firm-Fixed-Price (`FFP`) and shall not be subject to uncapped surcharges, tariff pass-throughs, customs duty adjustments, foreign exchange fluctuations, or raw material commodity indexing. (b) Invoicing & Payment Integrity: Seller shall submit itemized electronic invoices upon DDP acceptance of each production lot at Buyer\'s Everett or Renton final assembly line, payable Net Sixty (60) days. Any unilateral invoice surcharge not authorized by an executed GP1 §3.1 Change Order shall be automatically rejected.',
    '3.1 (a) Firm-Fixed-Price Lock: Unless expressly modified by a bilateral Change Order executed by Buyer\'s Vice President of Avionics Procurement referencing this GP1 §3.1 and Statement of Work (`SOW-AV-8921`) Schedule A, all unit prices ($150,000 per shipset across 300 C780/C730-MAX shipsets) and the forty-five million dollar ($45,000,000.00) total Contract ceiling are strictly Firm-Fixed-Price (`FFP`) and shall not be subject to uncapped surcharges, tariff pass-throughs, customs duty adjustments, foreign exchange fluctuations, or raw material commodity indexing. (b) Invoicing & Payment Integrity: Seller shall submit itemized electronic invoices upon DDP acceptance of each production lot at Buyer\'s Everett or Renton final assembly line, payable Net Sixty (60) days. Any unilateral invoice surcharge not authorized by an executed GP1 §3.1 Change Order shall be automatically rejected.',
    '3.1 (a) Firm-Fixed-Price Lock: Unless expressly modified by a bilateral Change Order executed by Buyer\'s Vice President of Avionics Procurement referencing this GP1 §3.1 and Statement of Work (`SOW-AV-8921`) Schedule A, all unit prices ($150,000 per shipset across 300 C780/C730-MAX shipsets) and the forty-five million dollar ($45,000,000.00) total Contract ceiling are strictly Firm-Fixed-Price (`FFP`) and shall not be subject to uncapped surcharges, tariff pass-throughs, customs duty adjustments, foreign exchange fluctuations, or raw material commodity indexing. (b) Invoicing & Payment Integrity: Seller shall submit itemized electronic invoices upon DDP acceptance of each production lot at Buyer\'s Everett or Renton final assembly line, payable Net Sixty (60) days. Any unilateral invoice surcharge not authorized by an executed GP1 §3.1 Change Order shall be automatically rejected.',
    FALSE, 'Firm-Fixed-Price SOW Lock',
    'Strict Firm-Fixed-Price SOW lock ($45M ceiling). Any Special Provision tariff surcharge adjustment must be strictly capped at 2.0% aggregate adjustment or executed via bilateral Change Order.',
    []
  ),
  (
    'GP1-05', 'GP1', 'GP1 §5.2', 'Packing, Marking & Aerospace Preservation',
    'ENGINEERING', 'Supplier Logistics & Packaging', 'NONE',
    '5.2 (a) Flight-Critical Avionics Preservation: Seller shall clean, preserve, pack, mark, and ship all `FCC-900` Flight Control Computer LRUs in strict accordance with Cymbal Aerospace Supplier Packaging Specification `D6-81628` and Air Transport Association (`ATA`) Spec 300 Category I reusable container and MIL-STD-1686 Class 1 electro-static discharge (`ESD`) protection standards. (b) Traceability & Barcoding: Each individual LRU chassis and exterior shipping container shall bear permanent UID/GS1-128 serialized barcoding, shock-watch and tilt-indicator telemetry seals, desiccant humidity indicators, and an enclosed FAA Form 8130-3 Authorized Release Certificate. Any shipment arriving with tripped shock indicators or breached ESD shielding shall be rejected at Seller\'s sole expense.',
    '5.2 (a) Flight-Critical Avionics Preservation: Seller shall clean, preserve, pack, mark, and ship all `FCC-900` Flight Control Computer LRUs in strict accordance with Cymbal Aerospace Supplier Packaging Specification `D6-81628` and Air Transport Association (`ATA`) Spec 300 Category I reusable container and MIL-STD-1686 Class 1 electro-static discharge (`ESD`) protection standards. (b) Traceability & Barcoding: Each individual LRU chassis and exterior shipping container shall bear permanent UID/GS1-128 serialized barcoding, shock-watch and tilt-indicator telemetry seals, desiccant humidity indicators, and an enclosed FAA Form 8130-3 Authorized Release Certificate. Any shipment arriving with tripped shock indicators or breached ESD shielding shall be rejected at Seller\'s sole expense.',
    '5.2 (a) Flight-Critical Avionics Preservation: Seller shall clean, preserve, pack, mark, and ship all `FCC-900` Flight Control Computer LRUs in strict accordance with Cymbal Aerospace Supplier Packaging Specification `D6-81628` and Air Transport Association (`ATA`) Spec 300 Category I reusable container and MIL-STD-1686 Class 1 electro-static discharge (`ESD`) protection standards. (b) Traceability & Barcoding: Each individual LRU chassis and exterior shipping container shall bear permanent UID/GS1-128 serialized barcoding, shock-watch and tilt-indicator telemetry seals, desiccant humidity indicators, and an enclosed FAA Form 8130-3 Authorized Release Certificate. Any shipment arriving with tripped shock indicators or breached ESD shielding shall be rejected at Seller\'s sole expense.',
    FALSE, 'ATA Spec 300 / D6-81628',
    'Require ATA Spec 300 Class 1 ESD protection and Cymbal D6-81628 packaging compliance.',
    []
  ),
  (
    'GP1-07', 'GP1', 'GP1 §7.1', 'Quality Management System (AS9100 Rev D)',
    'ENGINEERING', 'Supplier Quality Assurance', 'NONE',
    '7.1 (a) Accredited Aerospace QMS: Seller shall establish and maintain an IAQG-accredited `AS9100 Rev D` Quality Management System, `RTCA DO-178C` Design Assurance Level A (`DAL-A`) software lifecycle compliance, `RTCA DO-254` complex electronic hardware assurance, and Cymbal Aerospace Quality Management System Requirements for Suppliers (`D6-82479`) throughout Contract performance. (b) First Article Inspection & Sub-Tier Flowdown: Prior to initial production lot delivery, Seller shall complete a full `AS9102` First Article Inspection Report (`FAIR`) witnessed by Buyer\'s Supplier Quality Representative and shall flow down identical AS9100 Rev D and counterfeit electronic part avoidance (`AS5553`) controls to all sub-tier wafer foundries and forging sub-contractors.',
    '7.1 (a) Accredited Aerospace QMS: Seller shall establish and maintain an IAQG-accredited `AS9100 Rev D` Quality Management System, `RTCA DO-178C` Design Assurance Level A (`DAL-A`) software lifecycle compliance, `RTCA DO-254` complex electronic hardware assurance, and Cymbal Aerospace Quality Management System Requirements for Suppliers (`D6-82479`) throughout Contract performance. (b) First Article Inspection & Sub-Tier Flowdown: Prior to initial production lot delivery, Seller shall complete a full `AS9102` First Article Inspection Report (`FAIR`) witnessed by Buyer\'s Supplier Quality Representative and shall flow down identical AS9100 Rev D and counterfeit electronic part avoidance (`AS5553`) controls to all sub-tier wafer foundries and forging sub-contractors.',
    '7.1 (a) Accredited Aerospace QMS: Seller shall establish and maintain an IAQG-accredited `AS9100 Rev D` Quality Management System, `RTCA DO-178C` Design Assurance Level A (`DAL-A`) software lifecycle compliance, `RTCA DO-254` complex electronic hardware assurance, and Cymbal Aerospace Quality Management System Requirements for Suppliers (`D6-82479`) throughout Contract performance. (b) First Article Inspection & Sub-Tier Flowdown: Prior to initial production lot delivery, Seller shall complete a full `AS9102` First Article Inspection Report (`FAIR`) witnessed by Buyer\'s Supplier Quality Representative and shall flow down identical AS9100 Rev D and counterfeit electronic part avoidance (`AS5553`) controls to all sub-tier wafer foundries and forging sub-contractors.',
    FALSE, 'AS9100 Rev D / D6-82479',
    'Mandatory AS9100 Rev D certification and Cymbal D6-82479 supplier quality flowdown.',
    []
  ),
  (
    'GP1-09', 'GP1', 'GP1 §9.1', 'Changes & Equitable Adjustment',
    'PROCUREMENT', 'Procurement & Subcontracts', 'NONE',
    '9.1 (a) Directed Engineering & Schedule Changes: Buyer\'s Authorized Procurement Representative may at any time, by written Change Order without notice to sureties, direct changes within the general scope of this Contract in (i) drawings, avionics bus interface control documents (`ICDs`), or technical specifications, (ii) method of shipment or aerospace preservation, or (iii) place and schedule of delivery. Seller shall proceed immediately with performance of the Contract as changed. (b) Equitable Adjustment Claims: If any directed change under §9.1(a) causes a verified increase or decrease in the cost of or time required for performance, Seller must assert any claim for equitable adjustment in writing within thirty (30) calendar days from receipt of the written Change Order, supported by certified cost and pricing data.',
    '9.1 (a) Directed Engineering & Schedule Changes: Buyer\'s Authorized Procurement Representative may at any time, by written Change Order without notice to sureties, direct changes within the general scope of this Contract in (i) drawings, avionics bus interface control documents (`ICDs`), or technical specifications, (ii) method of shipment or aerospace preservation, or (iii) place and schedule of delivery. Seller shall proceed immediately with performance of the Contract as changed. (b) Equitable Adjustment Claims: If any directed change under §9.1(a) causes a verified increase or decrease in the cost of or time required for performance, Seller must assert any claim for equitable adjustment in writing within thirty (30) calendar days from receipt of the written Change Order, supported by certified cost and pricing data.',
    '9.1 (a) Directed Engineering & Schedule Changes: Buyer\'s Authorized Procurement Representative may at any time, by written Change Order without notice to sureties, direct changes within the general scope of this Contract in (i) drawings, avionics bus interface control documents (`ICDs`), or technical specifications, (ii) method of shipment or aerospace preservation, or (iii) place and schedule of delivery. Seller shall proceed immediately with performance of the Contract as changed. (b) Equitable Adjustment Claims: If any directed change under §9.1(a) causes a verified increase or decrease in the cost of or time required for performance, Seller must assert any claim for equitable adjustment in writing within thirty (30) calendar days from receipt of the written Change Order, supported by certified cost and pricing data.',
    FALSE, 'Cymbal Corporate GP1 Standard',
    'Unilateral directed changes within scope require Authorized Procurement Representative written order.',
    []
  ),
  (
    'GP1-12', 'GP1', 'GP1 §12.2', 'Warranty & FAA Source Inspection',
    'ENGINEERING', 'Engineering & QA (FAA DER)', 'HIGH',
    '12.2 (a) Airworthiness & Hardware/Firmware Warranty: Seller warrants all Goods, including `FCC-900` flight control hardware, triplex voting channels, and embedded `DO-178C DAL-A` avionics firmware, to be free from defects in design, material, and workmanship for thirty-six (36) months from initial aircraft delivery to Cymbal Aerospace\'s airline customer, and Seller shall repair or replace defective flight-critical LRUs on an Aircraft-on-Ground (`AOG`) 24-hour turnaround basis at Seller\'s expense. (b) Regulatory Source Surveillance: Cymbal Aerospace and Federal Aviation Administration (`FAA`) representatives may conduct unannounced source inspections at Seller\'s facility at any time to verify `AS9100 Rev D` quality compliance, `FAA 14 CFR Part 21.140` production certificate airworthiness conformity, and sub-tier test bench calibration records.',
    '12.2 (a) Airworthiness & Hardware/Firmware Warranty: Seller warrants all Goods, including `FCC-900` flight control hardware, triplex voting channels, and embedded `DO-178C DAL-A` avionics firmware, to be free from defects in design, material, and workmanship for twenty-four (24) months from initial aircraft delivery to Cymbal Aerospace\'s airline customer or thirty (30) months from factory shipment, whichever occurs first, and Seller shall repair or replace defective flight-critical LRUs on an Aircraft-on-Ground (`AOG`) 24-hour turnaround basis at Seller\'s expense. (b) Regulatory Source Surveillance: Cymbal Aerospace and Federal Aviation Administration (`FAA`) representatives may conduct unannounced source inspections at Seller\'s facility at any time to verify `AS9100 Rev D` quality compliance, `FAA 14 CFR Part 21.140` production certificate airworthiness conformity, and sub-tier test bench calibration records.',
    '12.2 (a) Airworthiness & Hardware/Firmware Warranty: Seller warrants all Goods against defects in material, workmanship, and avionics firmware for twenty-four (24) months from factory shipment. (b) Regulatory Source Surveillance: Cymbal Aerospace and FAA representatives retain unannounced source inspection access at Seller\'s facility at any time under FAA 14 CFR Part 21.140, with 48-hour courtesy coordination for non-safety routine quality reviews.',
    TRUE, 'FAA 14 CFR Part 21 Lockout',
    'HARD REGULATORY LOCKOUT: FAA 14 CFR Part 21.140 and AS9100 Rev D strictly prohibit prior-notice restrictions on FAA/Cymbal Aerospace airworthiness source inspections. Warranty period minimum is 24 months from delivery (36 months baseline).',
    []
  ),
  (
    'GP1-15', 'GP1', 'GP1 §15.1', 'Termination for Convenience',
    'LEGAL', 'Corporate Legal & Commercial', 'NONE',
    '15.1 (a) Unilateral Right to Terminate: Buyer may terminate all or any severable portion of this Contract for convenience at any time by written notice of termination to Seller. Upon receipt of such notice, Seller shall immediately stop all terminated work, place no further sub-tier purchase orders for raw materials or semiconductors, and protect all property in which Buyer has or may acquire an interest. (b) Termination Settlement & Cap: Seller\'s sole recovery upon termination for convenience, aligned with `FAR 52.249-2` principles, shall be limited to documented actual costs incurred for work-in-process prior to termination notice plus a reasonable profit on completed work, never to exceed the terminated portion of the GP1 §3.1 Firm-Fixed-Price Contract value, with zero recovery for anticipatory or consequential profits.',
    '15.1 (a) Unilateral Right to Terminate: Buyer may terminate all or any severable portion of this Contract for convenience at any time by written notice of termination to Seller. Upon receipt of such notice, Seller shall immediately stop all terminated work, place no further sub-tier purchase orders for raw materials or semiconductors, and protect all property in which Buyer has or may acquire an interest. (b) Termination Settlement & Cap: Seller\'s sole recovery upon termination for convenience, aligned with `FAR 52.249-2` principles, shall be limited to documented actual costs incurred for work-in-process prior to termination notice plus a reasonable profit on completed work, never to exceed the terminated portion of the GP1 §3.1 Firm-Fixed-Price Contract value, with zero recovery for anticipatory or consequential profits.',
    '15.1 (a) Unilateral Right to Terminate: Buyer may terminate all or any severable portion of this Contract for convenience at any time by written notice of termination to Seller. Upon receipt of such notice, Seller shall immediately stop all terminated work, place no further sub-tier purchase orders for raw materials or semiconductors, and protect all property in which Buyer has or may acquire an interest. (b) Termination Settlement & Cap: Seller\'s sole recovery upon termination for convenience, aligned with `FAR 52.249-2` principles, shall be limited to documented actual costs incurred for work-in-process prior to termination notice plus a reasonable profit on completed work, never to exceed the terminated portion of the GP1 §3.1 Firm-Fixed-Price Contract value, with zero recovery for anticipatory or consequential profits.',
    FALSE, 'FAR 52.249-2 Aligned',
    'Preserve Buyer unilateral termination for convenience right aligned with FAR 52.249-2.',
    []
  ),
  (
    'GP1-19', 'GP1', 'GP1 §19 & §24', 'Limitation of Liability & IP Indemnity',
    'LEGAL', 'Corporate Legal & IP', 'CRITICAL',
    '19.1 (a) Direct, Line-Stoppage & Airworthiness Recall Liability: Seller\'s aggregate liability to Cymbal Aerospace for direct damages, Everett/Renton final assembly line-stoppage costs, Fleet Airworthiness Directive (`AD`) grounding/retrofit campaigns, and airworthiness recall costs shall be uncapped. 24.1 (b) Intellectual Property Indemnification: Seller shall defend, indemnify, and hold harmless Cymbal Aerospace and its airline customers against all third-party patent, copyright, trade secret, and intellectual property infringement claims arising from the manufacture, sale, or use of the Goods including system-level avionics bus integration, and if any `FCC-900` unit is enjoined, Seller shall at its sole expense procure a perpetual royalty-free license or re-architect the infringing avionics module to maintain FAA type-design airworthiness.',
    '19.1 (a) Direct, Line-Stoppage & Airworthiness Recall Liability: Seller\'s liability for general direct damages and final assembly line-stoppage shall be capped at two hundred percent (200%) of the total Purchase Order value ($90M), provided that liability for Fleet Airworthiness Directive (`AD`) recall, gross negligence, willful misconduct, and §24 IP indemnification shall remain strictly uncapped. 24.1 (b) Intellectual Property Indemnification: Seller shall defend, indemnify, and hold harmless Cymbal Aerospace and its airline customers against all third-party intellectual property infringement claims including system-level avionics bus integration, except where such claim arises solely from Cymbal Aerospace\'s proprietary flight control bus specifications.',
    '19.1 (a) Direct, Line-Stoppage & Airworthiness Recall Liability: Seller\'s liability for general direct damages shall be capped at one hundred fifty percent (150%) of the total Purchase Order value ($67.5M), with uncapped liability for airworthiness directives and IP indemnity. 24.1 (b) Intellectual Property Indemnification: Seller shall defend and indemnify Cymbal Aerospace against all third-party intellectual property infringement claims except where arising solely from Cymbal Aerospace-furnished specifications.',
    FALSE, 'Corporate Legal Playbook Tier-1',
    'Reject 1x PO ($45M) general cap. Playbook Tier-1 Compromise permits a 2x PO ($90M) super-cap on general direct damages only if airworthiness recall, gross negligence, and IP indemnity remain uncapped, and narrows IP carveout to claims arising solely from Cymbal Aerospace proprietary bus specifications.',
    []
  ),
  (
    'GP1-28', 'GP1', 'GP1 §28.1', 'Governing Law & Dispute Resolution',
    'LEGAL', 'Corporate Legal', 'NONE',
    '28.1 (a) Governing Law & Exclusive Venue: This Contract and all claims, controversies, or disputes arising hereunder shall be governed by and construed in accordance with the substantive laws of the State of Delaware, excluding its conflict of laws rules and excluding the United Nations Convention on Contracts for the International Sale of Goods (`CISG`). Exclusive judicial venue shall lie in the state or federal courts located in Wilmington, Delaware or King County, Washington. (b) Continuity of Flight-Critical Supply: Pending final resolution of any dispute, claim, or Change Order valuation, Seller shall proceed diligently with uninterrupted manufacture, testing, and delivery of all `FCC-900` flight control units in accordance with Buyer\'s production schedule.',
    '28.1 (a) Governing Law & Exclusive Venue: This Contract and all claims, controversies, or disputes arising hereunder shall be governed by and construed in accordance with the substantive laws of the State of Delaware, excluding its conflict of laws rules and excluding the United Nations Convention on Contracts for the International Sale of Goods (`CISG`). Exclusive judicial venue shall lie in the state or federal courts located in Wilmington, Delaware or King County, Washington. (b) Continuity of Flight-Critical Supply: Pending final resolution of any dispute, claim, or Change Order valuation, Seller shall proceed diligently with uninterrupted manufacture, testing, and delivery of all `FCC-900` flight control units in accordance with Buyer\'s production schedule.',
    '28.1 (a) Governing Law & Exclusive Venue: This Contract and all claims, controversies, or disputes arising hereunder shall be governed by and construed in accordance with the substantive laws of the State of Delaware, excluding its conflict of laws rules and excluding the United Nations Convention on Contracts for the International Sale of Goods (`CISG`). Exclusive judicial venue shall lie in the state or federal courts located in Wilmington, Delaware or King County, Washington. (b) Continuity of Flight-Critical Supply: Pending final resolution of any dispute, claim, or Change Order valuation, Seller shall proceed diligently with uninterrupted manufacture, testing, and delivery of all `FCC-900` flight control units in accordance with Buyer\'s production schedule.',
    FALSE, 'Delaware / Washington Law Standard',
    'Maintain Delaware or Washington state governing law and uninterrupted delivery during disputes.',
    []
  ),
  (
    'SP3-02', 'SP3', 'SP3 §2.1', 'Export Compliance (ITAR & EAR)',
    'TAX', 'Global Trade Controls', 'NONE',
    '2.1 (a) Export Control Regulatory Compliance: Seller shall comply with all applicable U.S. export control laws and regulations, including the International Traffic in Arms Regulations (`ITAR`, 22 CFR Parts 120–130) and the Export Administration Regulations (`EAR`, 15 CFR Parts 730–774), covering dual-use flight control algorithms (`ECCN 7A994` / `7E994`) and defense technical data. (b) Export Classification & Deemed Exports: Seller shall maintain active DDTC registration where applicable, furnish accurate ECCN/USML Commodity Jurisdiction classifications prior to first shipment, and prevent unauthorized deemed exports of Cymbal Aerospace technical data to foreign nationals without prior U.S. Department of State or Bureau of Industry and Security (`BIS`) authorization.',
    '2.1 (a) Export Control Regulatory Compliance: Seller shall comply with all applicable U.S. export control laws and regulations, including the International Traffic in Arms Regulations (`ITAR`, 22 CFR Parts 120–130) and the Export Administration Regulations (`EAR`, 15 CFR Parts 730–774), covering dual-use flight control algorithms (`ECCN 7A994` / `7E994`) and defense technical data. (b) Export Classification & Deemed Exports: Seller shall maintain active DDTC registration where applicable, furnish accurate ECCN/USML Commodity Jurisdiction classifications prior to first shipment, and prevent unauthorized deemed exports of Cymbal Aerospace technical data to foreign nationals without prior U.S. Department of State or Bureau of Industry and Security (`BIS`) authorization.',
    '2.1 (a) Export Control Regulatory Compliance: Seller shall comply with all applicable U.S. export control laws and regulations, including the International Traffic in Arms Regulations (`ITAR`, 22 CFR Parts 120–130) and the Export Administration Regulations (`EAR`, 15 CFR Parts 730–774), covering dual-use flight control algorithms (`ECCN 7A994` / `7E994`) and defense technical data. (b) Export Classification & Deemed Exports: Seller shall maintain active DDTC registration where applicable, furnish accurate ECCN/USML Commodity Jurisdiction classifications prior to first shipment, and prevent unauthorized deemed exports of Cymbal Aerospace technical data to foreign nationals without prior U.S. Department of State or Bureau of Industry and Security (`BIS`) authorization.',
    FALSE, '22 CFR 120-130 (ITAR) / 15 CFR 730-774 (EAR)',
    'Strict compliance with ITAR (22 CFR 120-130) and EAR (15 CFR 730-774).',
    []
  ),
  (
    'SP3-04', 'SP3', 'SP3 §4.1', 'Customs, Duties & International Tariffs',
    'TAX', 'Global Tax & Trade', 'MOD',
    '4.1 (a) Importer of Record & Customs Clearance: Seller shall act as Importer of Record for all imported sub-tier components, raw aerospace titanium forgings, and radiation-hardened semiconductor wafers. (b) Tariff & Duty Allocation: All unit prices in Statement of Work (`SOW-AV-8921`) Schedule A are DDP (Incoterms 2020) Cymbal Aerospace Everett/Renton facility and inclusive of all import duties, customs fees, and tariffs, and Seller shall cooperate with Buyer\'s Global Trade team on U.S. CBP duty drawback documentation.',
    '4.1 (a) Importer of Record & Customs Clearance: Seller shall act as Importer of Record for all imported sub-tier components, raw aerospace titanium forgings, and radiation-hardened semiconductor wafers. (b) Tariff & Duty Allocation: All unit prices in Statement of Work (`SOW-AV-8921`) Schedule A are DDP (Incoterms 2020) Cymbal Aerospace Everett/Renton facility. Any verified new Section 232/301 tariff increase exceeding 5.0% on raw titanium forgings or semiconductor wafers shall be shared 50/50 between Cymbal Aerospace and Seller, strictly capped at a maximum aggregate adjustment of 2.0% of the GP1 §3.1 Firm-Fixed-Price SOW unit price.',
    '4.1 (a) Importer of Record & Customs Clearance: Seller shall act as Importer of Record for all imported sub-tier components. (b) Tariff & Duty Allocation: All unit prices are DDP Cymbal Aerospace Everett/Renton facility. Verified Section 232/301 tariff increases above 5.0% on raw titanium forgings may be shared 50/50 up to a maximum cap of 2.0% of the GP1 §3.1 Firm-Fixed-Price SOW unit price upon documentary customs proof.',
    FALSE, 'Cross-Clause SOW §3.1 Dependency',
    'CROSS-CLAUSE GUARDRAIL: Any tariff sharing or pass-through in SP3 §4.1 MUST be explicitly capped at a maximum aggregate adjustment of 2.0% to preserve the GP1 §3.1 Firm-Fixed-Price SOW Cap ($45M ceiling). Uncapped >5% pass-through triggers a CRITICAL cross-clause conflict with Procurement.',
    []
  ),
  (
    'SP5-03', 'SP5', 'SP5 §3.2', 'Cybersecurity Incident Reporting (DFARS)',
    'CYBER', 'Supplier Cyber Defense', 'HIGH',
    '3.2 (a) CUI Safeguards & NIST SP 800-171 Rev 2 Compliance: Seller shall maintain an accredited Cybersecurity Maturity Model Certification (`CMMC 2.0 Level 2`) posture and implement all 110 security controls in `NIST SP 800-171 Rev 2` across all engineering networks storing or processing Cymbal Aerospace Covered Defense Information (`CDI`), Controlled Unclassified Information (`CUI`), or `FCC-900` flight control source code. (b) Mandatory Cyber Incident Reporting & Forensics: Pursuant to `DoD DFARS 252.204-7012`, Seller shall report any cybersecurity incident affecting Cymbal Aerospace CDI or technical data to Buyer\'s Cyber Security Operations Center (`CSOC`) and the DoD DIBNet portal within seventy-two (72) hours of discovery, preserve affected system media for ninety (90) days, and provide raw forensic log images and malware telemetry upon request.',
    '3.2 (a) CUI Safeguards & NIST SP 800-171 Rev 2 Compliance: Seller shall maintain an accredited Cybersecurity Maturity Model Certification (`CMMC 2.0 Level 2`) posture and implement all 110 security controls in `NIST SP 800-171 Rev 2` across all engineering networks storing or processing Cymbal Aerospace Covered Defense Information (`CDI`), Controlled Unclassified Information (`CUI`), or `FCC-900` flight control source code. (b) Mandatory Cyber Incident Reporting & Forensics: Pursuant to `DoD DFARS 252.204-7012`, Seller shall report any cybersecurity incident affecting Cymbal Aerospace CDI or technical data within seventy-two (72) hours of discovery via preliminary notification, followed by root-cause forensic log images within five (5) business days.',
    '3.2 (a) CUI Safeguards & NIST SP 800-171 Rev 2 Compliance: Seller shall maintain NIST SP 800-171 controls across all systems processing Cymbal Aerospace CDI/CUI. (b) Mandatory Cyber Incident Reporting & Forensics: Seller shall submit mandatory DFARS 252.204-7012 cyber incident notification within seventy-two (72) hours of discovery, with full forensic packet delivery within seven (7) business days.',
    TRUE, 'DFARS 252.204-7012 Lockout',
    'HARD REGULATORY LOCKOUT: DoD DFARS 252.204-7012 mandates cyber incident reporting within 72 hours of discovery. Extending initial notification to 10 business days is a federal defense flowdown violation.',
    []
  );

-- 2. Seed 64 Historical Executed Clause Exceptions (16 per Redlined Clause)
TRUNCATE TABLE `vertex-ai-demos-468803.boeing_clm.historical_clause_exceptions`;

INSERT INTO `vertex-ai-demos-468803.boeing_clm.historical_clause_exceptions` (
  exception_id, clause_id, contract_id, supplier_name, supplier_tier, boeing_program,
  vendor_requested_redline, final_agreed_language, outcome_category,
  approval_authority, negotiation_notes, signed_date, embedding
)
VALUES
  -- =========================================================================
  -- GP1-12: 16 Precedents (14 HELD_FIRM, 2 COMPROMISE_TIER_1, 0 ACCEPTED_VENDOR)
  -- =========================================================================
  ('EXC-GP1-12-01', 'GP1-12', 'BA-2025-AV-4102', 'Honeywell Aerospace', 'Tier-1 Avionics', '787',
   'Seller warrants Goods for 12 months from factory shipment and requires 30 days prior written notice before facility inspections.',
   'Seller warrants all Goods for 36 months from aircraft delivery. Cymbal Aerospace and FAA representatives may conduct unannounced source inspections at any time under FAA 14 CFR Part 21.140.',
   'HELD_FIRM', 'Chief FAA DER & VP Supplier Quality', 'Rejected 30-day notice due to FAA 14 CFR Part 21.140 regulatory lockout; held 36-month airworthiness warranty.', DATE '2025-11-14', []),
  ('EXC-GP1-12-02', 'GP1-12', 'BA-2025-AV-3988', 'Collins Aerospace', 'Tier-1 Avionics', '737-MAX',
   'Warranty limited to 12 months ex-works; source inspections subject to 15 business days advance written scheduling.',
   'Seller warrants all Goods for 36 months from initial aircraft delivery. Cymbal Aerospace and FAA retain unannounced source inspection rights at Seller facilities at any time.',
   'HELD_FIRM', 'Director, Flight Controls QA', 'FAA Production Certificate 700 requires unrestricted FAA/Cymbal Aerospace source surveillance.', DATE '2025-09-22', []),
  ('EXC-GP1-12-03', 'GP1-12', 'BA-2025-AV-3710', 'Thales Avionics', 'Tier-1 Avionics', '777X',
   'Seller warrants avionics LRU hardware for 12 months from shipment and requests 30 days advance notice for cleanroom audits.',
   'Seller warrants all Goods for 36 months from aircraft delivery. Unannounced FAA and Cymbal Aerospace source inspections preserved per AS9100 Rev D.',
   'HELD_FIRM', 'Principal FAA DER', 'Cleanroom shift disruption mitigated via escort protocol, not prior-notice lockout.', DATE '2025-08-05', []),
  ('EXC-GP1-12-04', 'GP1-12', 'BA-2025-AV-3504', 'BAE Systems Controls', 'Tier-1 Avionics', '737-MAX',
   'Reduce warranty to 18 months from shipment and require 14 days written notice prior to quality audits.',
   '36-month warranty from initial aircraft delivery and mandatory unannounced FAA/Cymbal Aerospace source inspection access retained in full.',
   'HELD_FIRM', 'VP Engineering & Quality', 'Flight-critical spoiler control electronics cannot waive unannounced FAA Part 21 access.', DATE '2025-06-18', []),
  ('EXC-GP1-12-05', 'GP1-12', 'BA-2024-AV-2911', 'Moog Aircraft Group', 'Tier-1 Actuation & Avionics', '787',
   '12 months warranty from factory gate; scheduled source inspections upon 30 days prior written notice.',
   '36 months warranty from delivery to airline customer; unannounced Cymbal Aerospace and FAA source inspections at any time.',
   'HELD_FIRM', 'Chief Engineer, 787 Avionics', 'Held firm on both 36-month warranty and unannounced FAA Part 21.140 access.', DATE '2024-12-03', []),
  ('EXC-GP1-12-06', 'GP1-12', 'BA-2024-AV-2840', 'Safran Electronics & Defense', 'Tier-1 Avionics', '777X',
   'Seller proposes 12-month warranty from delivery and 21-day advance notice for facility audits.',
   '36-month warranty from initial aircraft delivery; unannounced Cymbal Aerospace and FAA source inspections preserved.',
   'HELD_FIRM', 'FAA DER & Supplier QA Lead', 'Zero exceptions allowed on FAA 14 CFR Part 21 right of access.', DATE '2024-10-19', []),
  ('EXC-GP1-12-07', 'GP1-12', 'BA-2024-AV-2615', 'Parker Aerospace', 'Tier-1 Flight Controls', '737-MAX',
   '12 months warranty from factory shipment and 30 days written notice for non-emergency inspections.',
   '36 months warranty from aircraft delivery and unrestricted unannounced source inspection right.',
   'HELD_FIRM', 'Director, Supplier Quality Assurance', 'Standard GP1 §12.2 enforced without modification.', DATE '2024-08-27', []),
  ('EXC-GP1-12-08', 'GP1-12', 'BA-2024-AV-2490', 'L3Harris Avionics', 'Tier-1 Avionics', 'BDS',
   '12-month commercial warranty from shipment; 30-day advance written notice for facility inspections.',
   '36-month warranty from delivery; unannounced FAA and Cymbal Aerospace source inspections at any time.',
   'HELD_FIRM', 'BDS Quality Director', 'Mandatory FAA and DCMA unannounced audit flowdown preserved.', DATE '2024-07-11', []),
  ('EXC-GP1-12-09', 'GP1-12', 'BA-2024-AV-2208', 'Curtiss-Wright Defense Solutions', 'Tier-1 Avionics', '787',
   '12 months warranty from shipment; scheduled source inspections upon 10 business days notice.',
   '36 months warranty from initial aircraft delivery; unannounced source inspections at any time.',
   'HELD_FIRM', 'Principal FAA DER', 'Held firm on GP1 §12.2 baseline.', DATE '2024-05-15', []),
  ('EXC-GP1-12-10', 'GP1-12', 'BA-2024-AV-1980', 'Crane Aerospace & Electronics', 'Tier-1 Avionics', '737-MAX',
   'Warranty 15 months from shipment; source inspections subject to 30 days prior written notice.',
   '36 months warranty from aircraft delivery; unannounced Cymbal Aerospace and FAA source inspections at any time.',
   'HELD_FIRM', 'Supplier QA Manager', 'FAA 14 CFR Part 21.140 prohibits prior notice gating.', DATE '2024-03-29', []),
  ('EXC-GP1-12-11', 'GP1-12', 'BA-2023-AV-1745', 'Astronics Corporation', 'Tier-1 Avionics', '777X',
   '12 months warranty from factory shipment; 30 days written notice required for facility audits.',
   '24 months warranty from initial aircraft delivery (30 months from shipment max), while preserving unannounced Cymbal Aerospace and FAA source inspections at any time.',
   'COMPROMISE_TIER_1', 'VP Engineering & Chief DER', 'Granted Tier-1 compromise on warranty duration (24mo delivery / 30mo shipment) for cabin power electronics, but held 100% firm on unannounced FAA source inspections.', DATE '2023-11-20', []),
  ('EXC-GP1-12-12', 'GP1-12', 'BA-2023-AV-1612', 'Meggitt Avionics', 'Tier-1 Avionics', '787',
   '12 months warranty from factory shipment and 14 days advance notice for source inspections.',
   '24 months warranty from initial aircraft delivery or 30 months from shipment; unannounced FAA and Cymbal Aerospace source inspections preserved at all times.',
   'COMPROMISE_TIER_1', 'Director, Avionics QA', 'Compromised on 24-month warranty period only; rejected prior notice on FAA inspections.', DATE '2023-09-08', []),
  ('EXC-GP1-12-13', 'GP1-12', 'BA-2023-AV-1490', 'GKN Aerospace', 'Tier-1 Aerostructures & Systems', '777X',
   '12 months warranty from shipment; 30 days prior written notice for source inspections.',
   '36 months warranty from aircraft delivery; unannounced Cymbal Aerospace and FAA source inspections at any time.',
   'HELD_FIRM', 'Chief FAA DER', 'Held firm on full GP1 §12.2 baseline.', DATE '2023-07-19', []),
  ('EXC-GP1-12-14', 'GP1-12', 'BA-2023-AV-1305', 'Spirit AeroSystems', 'Tier-1 Structures & Systems', '737-MAX',
   '18 months warranty from factory delivery; 7 days advance written notice for source audits.',
   '36 months warranty from aircraft delivery; unannounced Cymbal Aerospace and FAA source inspections at any time.',
   'HELD_FIRM', 'VP Quality & Airworthiness', 'Unannounced FAA/Cymbal Aerospace audit access strictly enforced.', DATE '2023-05-02', []),
  ('EXC-GP1-12-15', 'GP1-12', 'BA-2023-AV-1188', 'Eaton Aerospace', 'Tier-1 Fluid & Avionics', '787',
   '12 months warranty from shipment; scheduled inspections upon 30 days written notice.',
   '36 months warranty from initial aircraft delivery; unannounced FAA and Cymbal Aerospace source inspections at any time.',
   'HELD_FIRM', 'Principal FAA DER', 'Held firm per FAA Part 21 mandate.', DATE '2023-03-14', []),
  ('EXC-GP1-12-16', 'GP1-12', 'BA-2023-AV-1044', 'Triumph Group', 'Tier-1 Integrated Systems', '737-MAX',
   '12 months ex-works warranty; 30 days advance notice for facility source inspection.',
   '36 months warranty from initial aircraft delivery; unannounced FAA and Cymbal Aerospace source inspections at any time.',
   'HELD_FIRM', 'Director, Supplier Quality', 'Held firm on GP1 §12.2.', DATE '2023-01-25', []),

  -- =========================================================================
  -- GP1-19: 16 Precedents (4 HELD_FIRM, 11 COMPROMISE_TIER_1, 1 ACCEPTED_VENDOR)
  -- =========================================================================
  ('EXC-GP1-19-01', 'GP1-19', 'BA-2025-AV-4102', 'Honeywell Aerospace', 'Tier-1 Avionics', '787',
   'Liability capped at 100% (1x) of PO value; IP indemnity excludes any claim arising from combination of Goods with Cymbal Aerospace or third-party avionics bus.',
   'Direct damages capped at 200% (2x) of PO value ($90M equivalent), with uncapped liability for airworthiness recall, gross negligence, and IP indemnity. IP carveout narrowed solely to claims caused by Cymbal Aerospace proprietary bus specifications.',
   'COMPROMISE_TIER_1', 'VP Corporate Legal & Chief IP Counsel', 'Playbook Tier-1 Compromise accepted: 2x PO super-cap on general direct damages + narrowed Cymbal Aerospace-sole-spec IP carveout.', DATE '2025-11-14', []),
  ('EXC-GP1-19-02', 'GP1-19', 'BA-2025-AV-3988', 'Collins Aerospace', 'Tier-1 Avionics', '737-MAX',
   'Cap direct damages and line-stoppage at 100% of PO price; exclude IP infringement arising from system combination.',
   '200% (2x PO) super-cap on general direct damages; uncapped airworthiness recall and IP indemnity; IP carveout restricted solely to Cymbal Aerospace proprietary flight control bus specifications.',
   'COMPROMISE_TIER_1', 'Senior Counsel, Commercial & IP', 'Standard Tier-1 Avionics compromise per Corporate Legal Playbook.', DATE '2025-09-22', []),
  ('EXC-GP1-19-03', 'GP1-19', 'BA-2025-AV-3710', 'Thales Avionics', 'Tier-1 Avionics', '777X',
   'Seller liability shall not exceed 100% of total Purchase Order value; broad combination IP exclusion.',
   '200% (2x PO) cap on general direct damages; uncapped recall, gross negligence, and IP indemnity; IP exclusion limited solely to Cymbal Aerospace proprietary specifications.',
   'COMPROMISE_TIER_1', 'VP Corporate Legal', 'Aligned with Tier-1 avionics precedent (2x PO cap + uncapped safety/IP).', DATE '2025-08-05', []),
  ('EXC-GP1-19-04', 'GP1-19', 'BA-2025-AV-3504', 'BAE Systems Controls', 'Tier-1 Avionics', '737-MAX',
   '1x PO liability cap across all direct and recall damages; exclude system-level bus combination IP claims.',
   '2x PO (200%) cap on general direct damages; airworthiness recall and §24 IP indemnification remain strictly uncapped; IP carveout narrowed to Cymbal Aerospace sole specifications.',
   'COMPROMISE_TIER_1', 'Deputy General Counsel', 'Protected uncapped airworthiness recall and system integration IP.', DATE '2025-06-18', []),
  ('EXC-GP1-19-05', 'GP1-19', 'BA-2024-AV-2911', 'Moog Aircraft Group', 'Tier-1 Actuation & Avionics', '787',
   'Cap Seller direct liability at 100% of Contract value and carve out combination IP claims.',
   '200% (2x PO) super-cap on direct damages; uncapped recall and IP indemnity; narrowed Cymbal Aerospace-sole-spec IP exception.',
   'COMPROMISE_TIER_1', 'Senior Counsel, Commercial & IP', 'Playbook Tier-1 Compromise executed.', DATE '2024-12-03', []),
  ('EXC-GP1-19-06', 'GP1-19', 'BA-2024-AV-2840', 'Safran Electronics & Defense', 'Tier-1 Avionics', '777X',
   '100% PO cap on direct damages; no indemnity for combination with aircraft flight control bus.',
   '200% (2x PO) cap on direct damages; uncapped airworthiness recall and IP indemnity; carveout limited solely to Cymbal Aerospace proprietary bus specifications.',
   'COMPROMISE_TIER_1', 'VP Corporate Legal', 'Playbook Tier-1 Compromise executed.', DATE '2024-10-19', []),
  ('EXC-GP1-19-07', 'GP1-19', 'BA-2024-AV-2615', 'Parker Aerospace', 'Tier-1 Flight Controls', '737-MAX',
   'Limit direct damages to 1x PO value and exclude combination IP infringement.',
   '200% (2x PO) cap on direct damages; uncapped recall, willful misconduct, and IP indemnity; narrowed IP carveout.',
   'COMPROMISE_TIER_1', 'Senior Counsel, Commercial & IP', 'Consistent with Tier-1 Playbook fallback.', DATE '2024-08-27', []),
  ('EXC-GP1-19-08', 'GP1-19', 'BA-2024-AV-2490', 'L3Harris Avionics', 'Tier-1 Avionics', 'BDS',
   '100% PO liability cap and broad combination IP exclusion.',
   'Uncapped direct damages, line-stoppage, airworthiness recall, and full system-level IP indemnity.',
   'HELD_FIRM', 'BDS Chief Legal Counsel', 'Held firm on uncapped liability due to classified defense mission criticality.', DATE '2024-07-11', []),
  ('EXC-GP1-19-09', 'GP1-19', 'BA-2024-AV-2208', 'Curtiss-Wright Defense Solutions', 'Tier-1 Avionics', '787',
   'Cap liability at 100% of PO value; exclude IP claims from avionics bus integration.',
   '200% (2x PO) cap on direct damages; uncapped airworthiness recall and IP indemnity; narrowed Cymbal Aerospace-sole-spec IP carveout.',
   'COMPROMISE_TIER_1', 'Senior Counsel, Commercial & IP', 'Playbook Tier-1 Compromise approved.', DATE '2024-05-15', []),
  ('EXC-GP1-19-10', 'GP1-19', 'BA-2024-AV-1980', 'Crane Aerospace & Electronics', 'Tier-1 Avionics', '737-MAX',
   '1x PO cap on direct damages and combination IP carveout.',
   '200% (2x PO) cap on direct damages; uncapped recall and IP indemnity; narrowed IP carveout.',
   'COMPROMISE_TIER_1', 'Corporate Legal Director', 'Playbook Tier-1 Compromise approved.', DATE '2024-03-29', []),
  ('EXC-GP1-19-11', 'GP1-19', 'BA-2023-AV-1745', 'Astronics Corporation', 'Tier-1 Avionics', '777X',
   '100% PO liability cap and combination IP carveout for cabin electronics.',
   '200% (2x PO) cap on direct damages; uncapped recall and IP indemnity; narrowed IP carveout.',
   'COMPROMISE_TIER_1', 'Senior Counsel, Commercial & IP', 'Playbook Tier-1 Compromise approved.', DATE '2023-11-20', []),
  ('EXC-GP1-19-12', 'GP1-19', 'BA-2023-AV-1612', 'Meggitt Avionics', 'Tier-1 Avionics', '787',
   '100% PO cap on direct damages; exclude combination IP claims.',
   '200% (2x PO) cap on direct damages; uncapped recall and IP indemnity; narrowed IP carveout.',
   'COMPROMISE_TIER_1', 'Senior Counsel, Commercial & IP', 'Playbook Tier-1 Compromise approved.', DATE '2023-09-08', []),
  ('EXC-GP1-19-13', 'GP1-19', 'BA-2023-AV-1490', 'GKN Aerospace', 'Tier-1 Aerostructures & Systems', '777X',
   '100% PO cap on direct damages; exclude combination IP claims.',
   'Uncapped liability for direct damages, line-stoppage, recall, and full system-level IP indemnity.',
   'HELD_FIRM', 'VP Corporate Legal', 'Held firm on primary wing-flight-control structure interface.', DATE '2023-07-19', []),
  ('EXC-GP1-19-14', 'GP1-19', 'BA-2023-AV-1305', 'Spirit AeroSystems', 'Tier-1 Structures & Systems', '737-MAX',
   '1x PO liability cap on direct damages.',
   'Uncapped liability for direct damages, line-stoppage, and airworthiness recall.',
   'HELD_FIRM', 'General Counsel, Commercial Airplanes', 'Held firm on sole-source fuselage & flight control integration.', DATE '2023-05-02', []),
  ('EXC-GP1-19-15', 'GP1-19', 'BA-2023-AV-1188', 'Eaton Aerospace', 'Tier-1 Fluid & Avionics', '787',
   '100% PO cap on direct damages and combination IP exclusion.',
   'Uncapped liability for direct damages, recall, and IP indemnification.',
   'HELD_FIRM', 'Corporate Legal Director', 'Held firm on GP1 §19 & §24 baseline.', DATE '2023-03-14', []),
  ('EXC-GP1-19-16', 'GP1-19', 'BA-2023-AV-1044', 'Triumph Group', 'Tier-2 Non-Flight-Critical Subassembly', '737-MAX',
   '100% PO cap on direct damages and combination IP carveout for non-critical bracket sensor.',
   '100% PO cap on general direct damages accepted via one-time Executive VP waiver for non-flight-critical COTS bracket sensor.',
   'ACCEPTED_VENDOR', 'EVP Legal & Chief Risk Officer', 'Isolated COTS exception; explicitly barred as precedent for Class 1 flight-critical avionics.', DATE '2023-01-25', []),

  -- =========================================================================
  -- SP3-04: 16 Precedents (5 HELD_FIRM, 10 COMPROMISE_TIER_1, 1 ACCEPTED_VENDOR)
  -- =========================================================================
  ('EXC-SP3-04-01', 'SP3-04', 'BA-2025-AV-4102', 'Honeywell Aerospace', 'Tier-1 Avionics', '787',
   'Unit prices exclude new or increased Section 232/301 tariffs on titanium or semiconductor wafers exceeding 5%, passed through 100% to Cymbal Aerospace.',
   'Unit prices remain DDP Cymbal Aerospace Everett/Renton. Verified new Section 232/301 tariff increases >5.0% on titanium forgings or semiconductor wafers shared 50/50, strictly capped at a maximum aggregate adjustment of 2.0% of the GP1 §3.1 Firm-Fixed-Price SOW unit price.',
   'COMPROMISE_TIER_1', 'Director, Global Tax & VP Procurement', 'Harmonized 50/50 sharing with a hard 2.0% SOW cap to preserve GP1 §3.1 Firm-Fixed-Price integrity.', DATE '2025-11-14', []),
  ('EXC-SP3-04-02', 'SP3-04', 'BA-2025-AV-3988', 'Collins Aerospace', 'Tier-1 Avionics', '737-MAX',
   '100% pass-through to Cymbal Aerospace of any Section 232/301 duties on European titanium or Taiwanese wafers above 5%.',
   '50/50 tariff sharing above 5.0% threshold, strictly capped at a maximum aggregate adjustment of 2.0% of the GP1 §3.1 Firm-Fixed-Price SOW unit price.',
   'COMPROMISE_TIER_1', 'Global Tax & Procurement Joint Sign-off', 'Prevented cross-clause breach of GP1 §3.1 FFP ceiling via 2.0% aggregate cap.', DATE '2025-09-22', []),
  ('EXC-SP3-04-03', 'SP3-04', 'BA-2025-AV-3710', 'Thales Avionics', 'Tier-1 Avionics', '777X',
   'All unit prices exclude Section 301/232 tariffs exceeding 5%, which shall be billed 100% to Buyer.',
   'DDP Cymbal Aerospace Everett/Renton maintained; verified Section 232/301 tariff spikes >5.0% shared 50/50, capped at 2.0% maximum aggregate adjustment of GP1 §3.1 FFP unit price.',
   'COMPROMISE_TIER_1', 'Director, Global Tax & Trade', 'Harmonized with Procurement SOW §3.1 cap.', DATE '2025-08-05', []),
  ('EXC-SP3-04-04', 'SP3-04', 'BA-2025-AV-3504', 'BAE Systems Controls', 'Tier-1 Avionics', '737-MAX',
   'Pass through 100% of new customs duties and Section 232/301 tariffs exceeding 5% on semiconductor components.',
   '50/50 cost share on verified Section 232/301 tariffs >5.0%, strictly capped at a maximum aggregate adjustment of 2.0% of GP1 §3.1 FFP unit price.',
   'COMPROMISE_TIER_1', 'Global Tax & Subcontracts Lead', 'Joint Tax/Procurement harmonized language.', DATE '2025-06-18', []),
  ('EXC-SP3-04-05', 'SP3-04', 'BA-2024-AV-2911', 'Moog Aircraft Group', 'Tier-1 Actuation & Avionics', '787',
   'Exclude Section 232 titanium forging tariffs >5% from DDP price and pass through 100% to Cymbal Aerospace.',
   '50/50 sharing on verified Section 232/301 tariffs above 5.0%, capped at 2.0% aggregate adjustment of GP1 §3.1 FFP unit price.',
   'COMPROMISE_TIER_1', 'Director, Global Tax & Trade', 'Harmonized 50/50 split with 2.0% FFP cap.', DATE '2024-12-03', []),
  ('EXC-SP3-04-06', 'SP3-04', 'BA-2024-AV-2840', 'Safran Electronics & Defense', 'Tier-1 Avionics', '777X',
   '100% tariff pass-through above 5% on imported avionics sub-tier raw materials.',
   '50/50 sharing on verified Section 232/301 tariffs >5.0%, strictly capped at 2.0% of GP1 §3.1 FFP unit price.',
   'COMPROMISE_TIER_1', 'Global Tax & Procurement', '2.0% SOW cap enforced.', DATE '2024-10-19', []),
  ('EXC-SP3-04-07', 'SP3-04', 'BA-2024-AV-2615', 'Parker Aerospace', 'Tier-1 Flight Controls', '737-MAX',
   'Seller passes through 100% of Section 232/301 tariffs exceeding 5%.',
   '50/50 sharing above 5.0% threshold, capped at 2.0% maximum aggregate adjustment of GP1 §3.1 FFP unit price.',
   'COMPROMISE_TIER_1', 'Director, Global Tax', 'Harmonized with GP1 §3.1.', DATE '2024-08-27', []),
  ('EXC-SP3-04-08', 'SP3-04', 'BA-2024-AV-2490', 'L3Harris Avionics', 'Tier-1 Avionics', 'BDS',
   'Exclude new tariffs >5% from DDP unit price.',
   'All unit prices are DDP Cymbal Aerospace facility and 100% inclusive of all import duties, customs fees, and tariffs.',
   'HELD_FIRM', 'BDS Procurement Director', 'Held firm on 100% DDP inclusive pricing.', DATE '2024-07-11', []),
  ('EXC-SP3-04-09', 'SP3-04', 'BA-2024-AV-2208', 'Curtiss-Wright Defense Solutions', 'Tier-1 Avionics', '787',
   'Pass through 100% of Section 301 wafer tariffs exceeding 5%.',
   '50/50 sharing above 5.0%, strictly capped at 2.0% of GP1 §3.1 FFP unit price.',
   'COMPROMISE_TIER_1', 'Director, Global Tax & Trade', 'Harmonized Tier-1 compromise.', DATE '2024-05-15', []),
  ('EXC-SP3-04-10', 'SP3-04', 'BA-2024-AV-1980', 'Crane Aerospace & Electronics', 'Tier-1 Avionics', '737-MAX',
   '100% pass-through of Section 232/301 tariffs above 5%.',
   '50/50 sharing above 5.0%, strictly capped at 2.0% of GP1 §3.1 FFP unit price.',
   'COMPROMISE_TIER_1', 'Director, Global Tax & Trade', 'Harmonized Tier-1 compromise.', DATE '2024-03-29', []),
  ('EXC-SP3-04-11', 'SP3-04', 'BA-2023-AV-1745', 'Astronics Corporation', 'Tier-1 Avionics', '777X',
   '100% pass-through of Section 301 tariffs above 5%.',
   '50/50 sharing above 5.0%, strictly capped at 2.0% of GP1 §3.1 FFP unit price.',
   'COMPROMISE_TIER_1', 'Director, Global Tax & Trade', 'Harmonized Tier-1 compromise.', DATE '2023-11-20', []),
  ('EXC-SP3-04-12', 'SP3-04', 'BA-2023-AV-1612', 'Meggitt Avionics', 'Tier-1 Avionics', '787',
   'Exclude tariffs >5% from DDP unit price.',
   'All unit prices are DDP Cymbal Aerospace facility and inclusive of all import duties, customs fees, and tariffs.',
   'HELD_FIRM', 'VP Procurement', 'Held firm on DDP inclusive pricing.', DATE '2023-09-08', []),
  ('EXC-SP3-04-13', 'SP3-04', 'BA-2023-AV-1490', 'GKN Aerospace', 'Tier-1 Aerostructures & Systems', '777X',
   'Pass through Section 232 titanium duties >5%.',
   'All unit prices are DDP Cymbal Aerospace facility and inclusive of all import duties, customs fees, and tariffs.',
   'HELD_FIRM', 'VP Procurement', 'Titanium sourced via Cymbal Aerospace TMX master agreement; held firm on DDP.', DATE '2023-07-19', []),
  ('EXC-SP3-04-14', 'SP3-04', 'BA-2023-AV-1305', 'Spirit AeroSystems', 'Tier-1 Structures & Systems', '737-MAX',
   'Exclude new duties >5% from unit price.',
   'All unit prices are DDP Cymbal Aerospace facility and inclusive of all import duties, customs fees, and tariffs.',
   'HELD_FIRM', 'VP Procurement', 'Held firm on SP3 §4.1 baseline.', DATE '2023-05-02', []),
  ('EXC-SP3-04-15', 'SP3-04', 'BA-2023-AV-1188', 'Eaton Aerospace', 'Tier-1 Fluid & Avionics', '787',
   'Pass through 100% of tariffs above 5%.',
   'All unit prices are DDP Cymbal Aerospace facility and inclusive of all import duties, customs fees, and tariffs.',
   'HELD_FIRM', 'Director, Global Tax', 'Held firm on SP3 §4.1 baseline.', DATE '2023-03-14', []),
  ('EXC-SP3-04-16', 'SP3-04', 'BA-2023-AV-1044', 'Triumph Group', 'Tier-2 Non-FFP Time & Materials', '737-MAX',
   'Pass through Section 232 tariffs >5% on cost-reimbursable tooling contract.',
   'Accepted tariff pass-through above 5% ONLY because underlying contract was Cost-Reimbursable (not GP1 §3.1 Firm-Fixed-Price).',
   'ACCEPTED_VENDOR', 'VP Procurement & Tax', 'Not applicable to GP1 §3.1 Firm-Fixed-Price SOW contracts.', DATE '2023-01-25', []),

  -- =========================================================================
  -- SP5-03: 16 Precedents (15 HELD_FIRM, 1 COMPROMISE_TIER_1, 0 ACCEPTED_VENDOR)
  -- =========================================================================
  ('EXC-SP5-03-01', 'SP5-03', 'BA-2025-AV-4102', 'Honeywell Aerospace', 'Tier-1 Avionics', '787',
   'Report cybersecurity incidents within 10 business days following confirmation of a material breach.',
   'Maintain NIST SP 800-171 controls and report any cybersecurity incident affecting Cymbal Aerospace Covered Defense Information or technical data within 72 hours of discovery, and provide forensic log images upon request.',
   'HELD_FIRM', 'CISO & Lead Supplier Cyber Defense', 'DFARS 252.204-7012 imposes a strict 72-hour mandatory federal reporting window; 10-day delay rejected.', DATE '2025-11-14', []),
  ('EXC-SP5-03-02', 'SP5-03', 'BA-2025-AV-3988', 'Collins Aerospace', 'Tier-1 Avionics', '737-MAX',
   'Cyber incident reporting within 10 business days after internal SOC root-cause verification.',
   'Mandatory 72-hour cyber incident reporting from discovery per DFARS 252.204-7012 and NIST SP 800-171.',
   'HELD_FIRM', 'Director, Supplier Cyber Defense', 'Held firm on 72-hour statutory window.', DATE '2025-09-22', []),
  ('EXC-SP5-03-03', 'SP5-03', 'BA-2025-AV-3710', 'Thales Avionics', 'Tier-1 Avionics', '777X',
   'Notify Cymbal Aerospace within 7 business days of confirmed breach affecting technical data.',
   'Report any cybersecurity incident within 72 hours of discovery and provide forensic log images upon request.',
   'HELD_FIRM', 'Supplier Cyber Defense Lead', 'DFARS 252.204-7012 lockout enforced.', DATE '2025-08-05', []),
  ('EXC-SP5-03-04', 'SP5-03', 'BA-2025-AV-3504', 'BAE Systems Controls', 'Tier-1 Avionics', '737-MAX',
   '10 business days notification window for cybersecurity incidents.',
   '72-hour notification from discovery per DFARS 252.204-7012.',
   'HELD_FIRM', 'BDS & Commercial Cyber Lead', 'Zero tolerance for extending 72-hour DFARS reporting window.', DATE '2025-06-18', []),
  ('EXC-SP5-03-05', 'SP5-03', 'BA-2024-AV-2911', 'Moog Aircraft Group', 'Tier-1 Actuation & Avionics', '787',
   'Report cyber incidents within 10 business days following forensic validation.',
   '72-hour preliminary cyber incident notification upon discovery enforced; full root-cause forensic log packet permitted within 5 business days.',
   'COMPROMISE_TIER_1', 'CISO & Supplier Cyber Defense', 'Kept mandatory 72-hour initial notification intact while allowing 5 business days for deep forensic log image delivery.', DATE '2024-12-03', []),
  ('EXC-SP5-03-06', 'SP5-03', 'BA-2024-AV-2840', 'Safran Electronics & Defense', 'Tier-1 Avionics', '777X',
   '10 business days following confirmation of a material breach to report cyber incidents.',
   '72 hours of discovery per DFARS 252.204-7012 and NIST SP 800-171.',
   'HELD_FIRM', 'Supplier Cyber Defense Lead', 'Held firm on SP5 §3.2 baseline.', DATE '2024-10-19', []),
  ('EXC-SP5-03-07', 'SP5-03', 'BA-2024-AV-2615', 'Parker Aerospace', 'Tier-1 Flight Controls', '737-MAX',
   '5 business days after breach confirmation to notify Cymbal Aerospace Cyber Defense.',
   '72 hours of discovery per DFARS 252.204-7012.',
   'HELD_FIRM', 'Supplier Cyber Defense Lead', 'Held firm on 72-hour DFARS lockout.', DATE '2024-08-27', []),
  ('EXC-SP5-03-08', 'SP5-03', 'BA-2024-AV-2490', 'L3Harris Avionics', 'Tier-1 Avionics', 'BDS',
   '10 business days following SOC confirmation.',
   '72 hours of discovery per DFARS 252.204-7012.',
   'HELD_FIRM', 'BDS Cyber Director', 'Held firm on 72-hour DoD reporting mandate.', DATE '2024-07-11', []),
  ('EXC-SP5-03-09', 'SP5-03', 'BA-2024-AV-2208', 'Curtiss-Wright Defense Solutions', 'Tier-1 Avionics', '787',
   '10 business days following confirmation of material breach.',
   '72 hours of discovery per DFARS 252.204-7012.',
   'HELD_FIRM', 'Supplier Cyber Defense Lead', 'Held firm on SP5 §3.2.', DATE '2024-05-15', []),
  ('EXC-SP5-03-10', 'SP5-03', 'BA-2024-AV-1980', 'Crane Aerospace & Electronics', 'Tier-1 Avionics', '737-MAX',
   '10 business days cyber incident notification.',
   '72 hours of discovery per DFARS 252.204-7012.',
   'HELD_FIRM', 'Supplier Cyber Defense Lead', 'Held firm on SP5 §3.2.', DATE '2024-03-29', []),
  ('EXC-SP5-03-11', 'SP5-03', 'BA-2023-AV-1745', 'Astronics Corporation', 'Tier-1 Avionics', '777X',
   '10 business days following confirmation of breach.',
   '72 hours of discovery per DFARS 252.204-7012.',
   'HELD_FIRM', 'Supplier Cyber Defense Lead', 'Held firm on SP5 §3.2.', DATE '2023-11-20', []),
  ('EXC-SP5-03-12', 'SP5-03', 'BA-2023-AV-1612', 'Meggitt Avionics', 'Tier-1 Avionics', '787',
   '10 business days cyber incident notification window.',
   '72 hours of discovery per DFARS 252.204-7012.',
   'HELD_FIRM', 'Supplier Cyber Defense Lead', 'Held firm on SP5 §3.2.', DATE '2023-09-08', []),
  ('EXC-SP5-03-13', 'SP5-03', 'BA-2023-AV-1490', 'GKN Aerospace', 'Tier-1 Aerostructures & Systems', '777X',
   '10 business days after forensic root-cause confirmation.',
   '72 hours of discovery per DFARS 252.204-7012.',
   'HELD_FIRM', 'Supplier Cyber Defense Lead', 'Held firm on SP5 §3.2.', DATE '2023-07-19', []),
  ('EXC-SP5-03-14', 'SP5-03', 'BA-2023-AV-1305', 'Spirit AeroSystems', 'Tier-1 Structures & Systems', '737-MAX',
   '7 business days cyber incident notification.',
   '72 hours of discovery per DFARS 252.204-7012.',
   'HELD_FIRM', 'Supplier Cyber Defense Lead', 'Held firm on SP5 §3.2.', DATE '2023-05-02', []),
  ('EXC-SP5-03-15', 'SP5-03', 'BA-2023-AV-1188', 'Eaton Aerospace', 'Tier-1 Fluid & Avionics', '787',
   '10 business days following confirmation of material breach.',
   '72 hours of discovery per DFARS 252.204-7012.',
   'HELD_FIRM', 'Supplier Cyber Defense Lead', 'Held firm on SP5 §3.2.', DATE '2023-03-14', []),
  ('EXC-SP5-03-16', 'SP5-03', 'BA-2023-AV-1044', 'Triumph Group', 'Tier-1 Integrated Systems', '737-MAX',
   '10 business days cyber notification window.',
   '72 hours of discovery per DFARS 252.204-7012.',
   'HELD_FIRM', 'Supplier Cyber Defense Lead', 'Held firm on SP5 §3.2.', DATE '2023-01-25', []);

-- 3. Populate Live 768-Dim Embeddings via Vertex AI text-embedding-005
UPDATE `vertex-ai-demos-468803.boeing_clm.proforma_clauses` AS t
SET t.embedding = e.ml_generate_embedding_result
FROM ML.GENERATE_EMBEDDING(
  MODEL `vertex-ai-demos-468803.boeing_clm.text_embedding_005`,
  (
    SELECT
      clause_id,
      CONCAT(clause_ref, ' ', clause_title, ': ', standard_text, ' | Guardrail: ', guardrail_summary) AS content
    FROM `vertex-ai-demos-468803.boeing_clm.proforma_clauses`
  ),
  STRUCT(TRUE AS flatten_json_output, 'RETRIEVAL_DOCUMENT' AS task_type)
) AS e
WHERE t.clause_id = e.clause_id;

UPDATE `vertex-ai-demos-468803.boeing_clm.historical_clause_exceptions` AS t
SET t.embedding = e.ml_generate_embedding_result
FROM ML.GENERATE_EMBEDDING(
  MODEL `vertex-ai-demos-468803.boeing_clm.text_embedding_005`,
  (
    SELECT
      exception_id,
      CONCAT(
        clause_id, ' | Supplier: ', supplier_name, ' (', supplier_tier, ', ', boeing_program, ') | ',
        'Vendor Redline: ', vendor_requested_redline, ' | ',
        'Agreed Outcome (', outcome_category, '): ', final_agreed_language
      ) AS content
    FROM `vertex-ai-demos-468803.boeing_clm.historical_clause_exceptions`
  ),
  STRUCT(TRUE AS flatten_json_output, 'RETRIEVAL_DOCUMENT' AS task_type)
) AS e
WHERE t.exception_id = e.exception_id;

-- 4. Seed Declarative Cross-Clause Conflict & Regulatory Lockout Rules
TRUNCATE TABLE `vertex-ai-demos-468803.boeing_clm.clause_conflict_rules`;

INSERT INTO `vertex-ai-demos-468803.boeing_clm.clause_conflict_rules` (
  rule_id, rule_type, source_clause_id, target_clause_id, source_sme_team, target_sme_team,
  trigger_option_keys, forbidden_patterns, required_patterns, severity,
  conflict_title, conflict_description, harmonized_option_key, harmonized_resolution_text
)
VALUES
  (
    'CONFLICT-SP3-04-GP1-03',
    'CROSS_CLAUSE_CONFLICT',
    'SP3-04',
    'GP1-03',
    'TAX',
    'PROCUREMENT',
    ['accept_vendor'],
    ['exceeding five percent (5%)', 'passed through 100%', 'uncapped'],
    ['capped at a maximum aggregate adjustment of 2.0%'],
    'CRITICAL_CONFLICT',
    'Cross-Clause Conflict: SP3 §4.1 Tariff Pass-Through Violates GP1 §3.1 Firm-Fixed-Price SOW Cap',
    'Global Tax approved a >5% Section 232/301 tariff surcharge pass-through on SP3 §4.1, which directly violates Cymbal Aerospace Procurement Firm-Fixed-Price SOW Cap in GP1 §3.1 ($45M ceiling).',
    'custom_harmonized',
    '4.1 (a) Importer of Record & Customs Clearance: Seller shall act as Importer of Record for all imported sub-tier components, raw aerospace titanium forgings, and radiation-hardened semiconductor wafers. (b) Tariff & Duty Allocation: All unit prices in Statement of Work (`SOW-AV-8921`) Schedule A are DDP (Incoterms 2020) Cymbal Aerospace Everett/Renton facility. Any verified new Section 232/301 tariff increase exceeding 5.0% on raw titanium forgings or semiconductor wafers shall be shared 50/50 between Cymbal Aerospace and Seller, strictly capped at a maximum aggregate adjustment of 2.0% of the GP1 §3.1 Firm-Fixed-Price SOW unit price.'
  ),
  (
    'LOCKOUT-GP1-12-FAA',
    'REGULATORY_LOCKOUT',
    'GP1-12',
    'GP1-12',
    'ENGINEERING',
    'ENGINEERING',
    ['accept_vendor'],
    ['thirty (30) days prior written notice', 'scheduled inspections upon thirty'],
    ['unannounced source inspections'],
    'REGULATORY_BLOCK',
    'Regulatory Lockout: GP1 §12.2 Prior Notice Violates FAA 14 CFR Part 21.140',
    'FAA 14 CFR Part 21.140 / AS9100 Rev D mandatory unannounced right of access cannot be waived or restricted by 30-day prior written notice.',
    'hold_firm',
    '12.2 (a) Airworthiness & Hardware/Firmware Warranty: Seller warrants all Goods, including `FCC-900` flight control hardware, triplex voting channels, and embedded `DO-178C DAL-A` avionics firmware, to be free from defects in design, material, and workmanship for thirty-six (36) months from initial aircraft delivery to Cymbal Aerospace\'s airline customer, and Seller shall repair or replace defective flight-critical LRUs on an Aircraft-on-Ground (`AOG`) 24-hour turnaround basis at Seller\'s expense. (b) Regulatory Source Surveillance: Cymbal Aerospace and Federal Aviation Administration (`FAA`) representatives may conduct unannounced source inspections at Seller\'s facility at any time to verify `AS9100 Rev D` quality compliance, `FAA 14 CFR Part 21.140` production certificate airworthiness conformity, and sub-tier test bench calibration records.'
  ),
  (
    'LOCKOUT-SP5-03-DFARS',
    'REGULATORY_LOCKOUT',
    'SP5-03',
    'SP5-03',
    'CYBER',
    'CYBER',
    ['accept_vendor'],
    ['ten (10) business days'],
    ['seventy-two (72) hours'],
    'REGULATORY_BLOCK',
    'Regulatory Lockout: SP5 §3.2 10-Day Delay Violates DoD DFARS 252.204-7012',
    'DoD DFARS 252.204-7012 mandatory 72-hour cyber incident reporting window cannot be extended to 10 business days.',
    'hold_firm',
    '3.2 (a) CUI Safeguards & NIST SP 800-171 Rev 2 Compliance: Seller shall maintain an accredited Cybersecurity Maturity Model Certification (`CMMC 2.0 Level 2`) posture and implement all 110 security controls in `NIST SP 800-171 Rev 2` across all engineering networks storing or processing Cymbal Aerospace Covered Defense Information (`CDI`), Controlled Unclassified Information (`CUI`), or `FCC-900` flight control source code. (b) Mandatory Cyber Incident Reporting & Forensics: Pursuant to `DoD DFARS 252.204-7012`, Seller shall report any cybersecurity incident affecting Cymbal Aerospace CDI or technical data to Buyer\'s Cyber Security Operations Center (`CSOC`) and the DoD DIBNet portal within seventy-two (72) hours of discovery, preserve affected system media for ninety (90) days, and provide raw forensic log images and malware telemetry upon request.'
  );

-- 5. Seed Active Deal (BA-2026-AV-8921)
TRUNCATE TABLE `vertex-ai-demos-468803.boeing_clm.active_deals`;

INSERT INTO `vertex-ai-demos-468803.boeing_clm.active_deals` (
  deal_id, vendor_name, supplier_tier, boeing_program, contract_value_usd,
  proforma_stack, pricing_model, sow_cap_clause_ref, sharepoint_folder_url,
  deviation_matrix_xlsx, total_clauses_parsed, untouched_clauses_count,
  redlined_clauses_count, status, updated_at
)
VALUES (
  'BA-2026-AV-8921',
  'Apex AeroSystems Inc.',
  'Tier-1 Avionics',
  'Cymbal C780 / C730-MAX Flight Control Electronics (FCC-900)',
  45000000.0,
  'Cymbal GP1 (General Provisions) + SP3 (International/Tax) + SP5 (Cyber/DFARS)',
  'Firm-Fixed-Price (FFP) — $45,000,000 Ceiling',
  'GP1 §3.1',
  'https://36zrbd.sharepoint.com/sites/CymbalAerospace/Shared%20Documents/BA-2026-AV-8921',
  'BA-2026-AV-8921_SharePoint_Deviation_Matrix.xlsx',
  12,
  8,
  4,
  'CONFLICT_DETECTED',
  CURRENT_TIMESTAMP()
);

-- 6. Seed Deal Clause Deviations (12 Clauses: 8 Untouched, 4 Redlined with Initial Conflict on SP3-04)
TRUNCATE TABLE `vertex-ai-demos-468803.boeing_clm.deal_clause_deviations`;

INSERT INTO `vertex-ai-demos-468803.boeing_clm.deal_clause_deviations` (
  deal_id, clause_id, proforma_doc, clause_ref, clause_title, has_redline,
  sme_team, sme_owner_label, risk_level, regulatory_flag, boeing_baseline_text,
  vendor_redline_text, diff_html, vendor_comment, insertions_json, deletions_json,
  recommended_option_key, recommended_counter_text, selected_option_key,
  selected_counter_text, sme_status, sme_reviewer, sme_rationale, updated_at
)
VALUES
  (
    'BA-2026-AV-8921', 'GP1-01', 'GP1', 'GP1 §1.1', 'Definitions & Order of Precedence', FALSE,
    'PROCUREMENT', 'Procurement & Subcontracts', 'NONE', 'Cymbal Corporate GP1 Standard',
    '1.1 (a) Definitions: "Buyer" means Cymbal Aerospace Corporation or its wholly-owned aerospace subsidiary identified on the face of the Master Purchase Agreement (`BA-2026-AV-8921`). "Seller" means Apex AeroSystems Inc. or the legal entity furnishing Goods and flight-critical software hereunder. "Goods" means the Triple-Redundant Fly-By-Wire Flight Control Computers (`FCC-900`), Line Replaceable Units (`LRUs`), embedded DAL-A flight control firmware, and associated technical deliverables specified in Statement of Work (`SOW-AV-8921`) Schedule A. (b) Order of Precedence: In the event of any ambiguity or inconsistency among Contract documents, Special Provisions (`SP3` International & Tariff Provisions and `SP5` Cybersecurity & Defense Provisions) shall take precedence over these General Provisions (`GP1`), expressly excluding the Firm-Fixed-Price (`FFP`) unit price locks and $45,000,000 aggregate ceiling set forth in GP1 §3.1 and SOW Schedule A, which shall govern over any conflicting Special Provision unless modified by a formal bilateral Change Order.',
    '1.1 (a) Definitions: "Buyer" means Cymbal Aerospace Corporation or its wholly-owned aerospace subsidiary identified on the face of the Master Purchase Agreement (`BA-2026-AV-8921`). "Seller" means Apex AeroSystems Inc. or the legal entity furnishing Goods and flight-critical software hereunder. "Goods" means the Triple-Redundant Fly-By-Wire Flight Control Computers (`FCC-900`), Line Replaceable Units (`LRUs`), embedded DAL-A flight control firmware, and associated technical deliverables specified in Statement of Work (`SOW-AV-8921`) Schedule A. (b) Order of Precedence: In the event of any ambiguity or inconsistency among Contract documents, Special Provisions (`SP3` International & Tariff Provisions and `SP5` Cybersecurity & Defense Provisions) shall take precedence over these General Provisions (`GP1`), expressly excluding the Firm-Fixed-Price (`FFP`) unit price locks and $45,000,000 aggregate ceiling set forth in GP1 §3.1 and SOW Schedule A, which shall govern over any conflicting Special Provision unless modified by a formal bilateral Change Order.',
    '1.1 (a) Definitions: "Buyer" means Cymbal Aerospace Corporation or its wholly-owned aerospace subsidiary identified on the face of the Master Purchase Agreement (`BA-2026-AV-8921`). "Seller" means Apex AeroSystems Inc. or the legal entity furnishing Goods and flight-critical software hereunder. "Goods" means the Triple-Redundant Fly-By-Wire Flight Control Computers (`FCC-900`), Line Replaceable Units (`LRUs`), embedded DAL-A flight control firmware, and associated technical deliverables specified in Statement of Work (`SOW-AV-8921`) Schedule A. (b) Order of Precedence: In the event of any ambiguity or inconsistency among Contract documents, Special Provisions (`SP3` International & Tariff Provisions and `SP5` Cybersecurity & Defense Provisions) shall take precedence over these General Provisions (`GP1`), expressly excluding the Firm-Fixed-Price (`FFP`) unit price locks and $45,000,000 aggregate ceiling set forth in GP1 §3.1 and SOW Schedule A, which shall govern over any conflicting Special Provision unless modified by a formal bilateral Change Order.',
    '', '[]', '[]',
    'hold_firm',
    '1.1 (a) Definitions: "Buyer" means Cymbal Aerospace Corporation or its wholly-owned aerospace subsidiary identified on the face of the Master Purchase Agreement (`BA-2026-AV-8921`). "Seller" means Apex AeroSystems Inc. or the legal entity furnishing Goods and flight-critical software hereunder. "Goods" means the Triple-Redundant Fly-By-Wire Flight Control Computers (`FCC-900`), Line Replaceable Units (`LRUs`), embedded DAL-A flight control firmware, and associated technical deliverables specified in Statement of Work (`SOW-AV-8921`) Schedule A. (b) Order of Precedence: In the event of any ambiguity or inconsistency among Contract documents, Special Provisions (`SP3` International & Tariff Provisions and `SP5` Cybersecurity & Defense Provisions) shall take precedence over these General Provisions (`GP1`), expressly excluding the Firm-Fixed-Price (`FFP`) unit price locks and $45,000,000 aggregate ceiling set forth in GP1 §3.1 and SOW Schedule A, which shall govern over any conflicting Special Provision unless modified by a formal bilateral Change Order.',
    'hold_firm',
    '1.1 (a) Definitions: "Buyer" means Cymbal Aerospace Corporation or its wholly-owned aerospace subsidiary identified on the face of the Master Purchase Agreement (`BA-2026-AV-8921`). "Seller" means Apex AeroSystems Inc. or the legal entity furnishing Goods and flight-critical software hereunder. "Goods" means the Triple-Redundant Fly-By-Wire Flight Control Computers (`FCC-900`), Line Replaceable Units (`LRUs`), embedded DAL-A flight control firmware, and associated technical deliverables specified in Statement of Work (`SOW-AV-8921`) Schedule A. (b) Order of Precedence: In the event of any ambiguity or inconsistency among Contract documents, Special Provisions (`SP3` International & Tariff Provisions and `SP5` Cybersecurity & Defense Provisions) shall take precedence over these General Provisions (`GP1`), expressly excluding the Firm-Fixed-Price (`FFP`) unit price locks and $45,000,000 aggregate ceiling set forth in GP1 §3.1 and SOW Schedule A, which shall govern over any conflicting Special Provision unless modified by a formal bilateral Change Order.',
    'UNTOUCHED', 'Auto-Verified (No Redline)', 'Clause matches Cymbal Aerospace Proforma GP1 baseline with zero Track Changes.', CURRENT_TIMESTAMP()
  ),
  (
    'BA-2026-AV-8921', 'GP1-03', 'GP1', 'GP1 §3.1', 'Firm-Fixed-Price SOW Cap & Pricing Integrity', FALSE,
    'PROCUREMENT', 'Procurement & Cost Management', 'NONE', 'Firm-Fixed-Price SOW Lock',
    '3.1 (a) Firm-Fixed-Price Lock: Unless expressly modified by a bilateral Change Order executed by Buyer\'s Vice President of Avionics Procurement referencing this GP1 §3.1 and Statement of Work (`SOW-AV-8921`) Schedule A, all unit prices ($150,000 per shipset across 300 C780/C730-MAX shipsets) and the forty-five million dollar ($45,000,000.00) total Contract ceiling are strictly Firm-Fixed-Price (`FFP`) and shall not be subject to uncapped surcharges, tariff pass-throughs, customs duty adjustments, foreign exchange fluctuations, or raw material commodity indexing. (b) Invoicing & Payment Integrity: Seller shall submit itemized electronic invoices upon DDP acceptance of each production lot at Buyer\'s Everett or Renton final assembly line, payable Net Sixty (60) days. Any unilateral invoice surcharge not authorized by an executed GP1 §3.1 Change Order shall be automatically rejected.',
    '3.1 (a) Firm-Fixed-Price Lock: Unless expressly modified by a bilateral Change Order executed by Buyer\'s Vice President of Avionics Procurement referencing this GP1 §3.1 and Statement of Work (`SOW-AV-8921`) Schedule A, all unit prices ($150,000 per shipset across 300 C780/C730-MAX shipsets) and the forty-five million dollar ($45,000,000.00) total Contract ceiling are strictly Firm-Fixed-Price (`FFP`) and shall not be subject to uncapped surcharges, tariff pass-throughs, customs duty adjustments, foreign exchange fluctuations, or raw material commodity indexing. (b) Invoicing & Payment Integrity: Seller shall submit itemized electronic invoices upon DDP acceptance of each production lot at Buyer\'s Everett or Renton final assembly line, payable Net Sixty (60) days. Any unilateral invoice surcharge not authorized by an executed GP1 §3.1 Change Order shall be automatically rejected.',
    '3.1 (a) Firm-Fixed-Price Lock: Unless expressly modified by a bilateral Change Order executed by Buyer\'s Vice President of Avionics Procurement referencing this GP1 §3.1 and Statement of Work (`SOW-AV-8921`) Schedule A, all unit prices ($150,000 per shipset across 300 C780/C730-MAX shipsets) and the forty-five million dollar ($45,000,000.00) total Contract ceiling are strictly Firm-Fixed-Price (`FFP`) and shall not be subject to uncapped surcharges, tariff pass-throughs, customs duty adjustments, foreign exchange fluctuations, or raw material commodity indexing. (b) Invoicing & Payment Integrity: Seller shall submit itemized electronic invoices upon DDP acceptance of each production lot at Buyer\'s Everett or Renton final assembly line, payable Net Sixty (60) days. Any unilateral invoice surcharge not authorized by an executed GP1 §3.1 Change Order shall be automatically rejected.',
    '', '[]', '[]',
    'hold_firm',
    '3.1 (a) Firm-Fixed-Price Lock: Unless expressly modified by a bilateral Change Order executed by Buyer\'s Vice President of Avionics Procurement referencing this GP1 §3.1 and Statement of Work (`SOW-AV-8921`) Schedule A, all unit prices ($150,000 per shipset across 300 C780/C730-MAX shipsets) and the forty-five million dollar ($45,000,000.00) total Contract ceiling are strictly Firm-Fixed-Price (`FFP`) and shall not be subject to uncapped surcharges, tariff pass-throughs, customs duty adjustments, foreign exchange fluctuations, or raw material commodity indexing. (b) Invoicing & Payment Integrity: Seller shall submit itemized electronic invoices upon DDP acceptance of each production lot at Buyer\'s Everett or Renton final assembly line, payable Net Sixty (60) days. Any unilateral invoice surcharge not authorized by an executed GP1 §3.1 Change Order shall be automatically rejected.',
    'hold_firm',
    '3.1 (a) Firm-Fixed-Price Lock: Unless expressly modified by a bilateral Change Order executed by Buyer\'s Vice President of Avionics Procurement referencing this GP1 §3.1 and Statement of Work (`SOW-AV-8921`) Schedule A, all unit prices ($150,000 per shipset across 300 C780/C730-MAX shipsets) and the forty-five million dollar ($45,000,000.00) total Contract ceiling are strictly Firm-Fixed-Price (`FFP`) and shall not be subject to uncapped surcharges, tariff pass-throughs, customs duty adjustments, foreign exchange fluctuations, or raw material commodity indexing. (b) Invoicing & Payment Integrity: Seller shall submit itemized electronic invoices upon DDP acceptance of each production lot at Buyer\'s Everett or Renton final assembly line, payable Net Sixty (60) days. Any unilateral invoice surcharge not authorized by an executed GP1 §3.1 Change Order shall be automatically rejected.',
    'UNTOUCHED', 'Auto-Verified (No Redline)', 'Firm-Fixed-Price SOW Cap ($45M ceiling) locked per GP1 §3.1.', CURRENT_TIMESTAMP()
  ),
  (
    'BA-2026-AV-8921', 'GP1-05', 'GP1', 'GP1 §5.2', 'Packing, Marking & Aerospace Preservation', FALSE,
    'ENGINEERING', 'Supplier Logistics & Packaging', 'NONE', 'ATA Spec 300 / D6-81628',
    '5.2 (a) Flight-Critical Avionics Preservation: Seller shall clean, preserve, pack, mark, and ship all `FCC-900` Flight Control Computer LRUs in strict accordance with Cymbal Aerospace Supplier Packaging Specification `D6-81628` and Air Transport Association (`ATA`) Spec 300 Category I reusable container and MIL-STD-1686 Class 1 electro-static discharge (`ESD`) protection standards. (b) Traceability & Barcoding: Each individual LRU chassis and exterior shipping container shall bear permanent UID/GS1-128 serialized barcoding, shock-watch and tilt-indicator telemetry seals, desiccant humidity indicators, and an enclosed FAA Form 8130-3 Authorized Release Certificate. Any shipment arriving with tripped shock indicators or breached ESD shielding shall be rejected at Seller\'s sole expense.',
    '5.2 (a) Flight-Critical Avionics Preservation: Seller shall clean, preserve, pack, mark, and ship all `FCC-900` Flight Control Computer LRUs in strict accordance with Cymbal Aerospace Supplier Packaging Specification `D6-81628` and Air Transport Association (`ATA`) Spec 300 Category I reusable container and MIL-STD-1686 Class 1 electro-static discharge (`ESD`) protection standards. (b) Traceability & Barcoding: Each individual LRU chassis and exterior shipping container shall bear permanent UID/GS1-128 serialized barcoding, shock-watch and tilt-indicator telemetry seals, desiccant humidity indicators, and an enclosed FAA Form 8130-3 Authorized Release Certificate. Any shipment arriving with tripped shock indicators or breached ESD shielding shall be rejected at Seller\'s sole expense.',
    '5.2 (a) Flight-Critical Avionics Preservation: Seller shall clean, preserve, pack, mark, and ship all `FCC-900` Flight Control Computer LRUs in strict accordance with Cymbal Aerospace Supplier Packaging Specification `D6-81628` and Air Transport Association (`ATA`) Spec 300 Category I reusable container and MIL-STD-1686 Class 1 electro-static discharge (`ESD`) protection standards. (b) Traceability & Barcoding: Each individual LRU chassis and exterior shipping container shall bear permanent UID/GS1-128 serialized barcoding, shock-watch and tilt-indicator telemetry seals, desiccant humidity indicators, and an enclosed FAA Form 8130-3 Authorized Release Certificate. Any shipment arriving with tripped shock indicators or breached ESD shielding shall be rejected at Seller\'s sole expense.',
    '', '[]', '[]',
    'hold_firm',
    '5.2 (a) Flight-Critical Avionics Preservation: Seller shall clean, preserve, pack, mark, and ship all `FCC-900` Flight Control Computer LRUs in strict accordance with Cymbal Aerospace Supplier Packaging Specification `D6-81628` and Air Transport Association (`ATA`) Spec 300 Category I reusable container and MIL-STD-1686 Class 1 electro-static discharge (`ESD`) protection standards. (b) Traceability & Barcoding: Each individual LRU chassis and exterior shipping container shall bear permanent UID/GS1-128 serialized barcoding, shock-watch and tilt-indicator telemetry seals, desiccant humidity indicators, and an enclosed FAA Form 8130-3 Authorized Release Certificate. Any shipment arriving with tripped shock indicators or breached ESD shielding shall be rejected at Seller\'s sole expense.',
    'hold_firm',
    '5.2 (a) Flight-Critical Avionics Preservation: Seller shall clean, preserve, pack, mark, and ship all `FCC-900` Flight Control Computer LRUs in strict accordance with Cymbal Aerospace Supplier Packaging Specification `D6-81628` and Air Transport Association (`ATA`) Spec 300 Category I reusable container and MIL-STD-1686 Class 1 electro-static discharge (`ESD`) protection standards. (b) Traceability & Barcoding: Each individual LRU chassis and exterior shipping container shall bear permanent UID/GS1-128 serialized barcoding, shock-watch and tilt-indicator telemetry seals, desiccant humidity indicators, and an enclosed FAA Form 8130-3 Authorized Release Certificate. Any shipment arriving with tripped shock indicators or breached ESD shielding shall be rejected at Seller\'s sole expense.',
    'UNTOUCHED', 'Auto-Verified (No Redline)', 'Clause matches Cymbal Aerospace Proforma GP1 baseline with zero Track Changes.', CURRENT_TIMESTAMP()
  ),
  (
    'BA-2026-AV-8921', 'GP1-07', 'GP1', 'GP1 §7.1', 'Quality Management System (AS9100 Rev D)', FALSE,
    'ENGINEERING', 'Supplier Quality Assurance', 'NONE', 'AS9100 Rev D / D6-82479',
    '7.1 (a) Accredited Aerospace QMS: Seller shall establish and maintain an IAQG-accredited `AS9100 Rev D` Quality Management System, `RTCA DO-178C` Design Assurance Level A (`DAL-A`) software lifecycle compliance, `RTCA DO-254` complex electronic hardware assurance, and Cymbal Aerospace Quality Management System Requirements for Suppliers (`D6-82479`) throughout Contract performance. (b) First Article Inspection & Sub-Tier Flowdown: Prior to initial production lot delivery, Seller shall complete a full `AS9102` First Article Inspection Report (`FAIR`) witnessed by Buyer\'s Supplier Quality Representative and shall flow down identical AS9100 Rev D and counterfeit electronic part avoidance (`AS5553`) controls to all sub-tier wafer foundries and forging sub-contractors.',
    '7.1 (a) Accredited Aerospace QMS: Seller shall establish and maintain an IAQG-accredited `AS9100 Rev D` Quality Management System, `RTCA DO-178C` Design Assurance Level A (`DAL-A`) software lifecycle compliance, `RTCA DO-254` complex electronic hardware assurance, and Cymbal Aerospace Quality Management System Requirements for Suppliers (`D6-82479`) throughout Contract performance. (b) First Article Inspection & Sub-Tier Flowdown: Prior to initial production lot delivery, Seller shall complete a full `AS9102` First Article Inspection Report (`FAIR`) witnessed by Buyer\'s Supplier Quality Representative and shall flow down identical AS9100 Rev D and counterfeit electronic part avoidance (`AS5553`) controls to all sub-tier wafer foundries and forging sub-contractors.',
    '7.1 (a) Accredited Aerospace QMS: Seller shall establish and maintain an IAQG-accredited `AS9100 Rev D` Quality Management System, `RTCA DO-178C` Design Assurance Level A (`DAL-A`) software lifecycle compliance, `RTCA DO-254` complex electronic hardware assurance, and Cymbal Aerospace Quality Management System Requirements for Suppliers (`D6-82479`) throughout Contract performance. (b) First Article Inspection & Sub-Tier Flowdown: Prior to initial production lot delivery, Seller shall complete a full `AS9102` First Article Inspection Report (`FAIR`) witnessed by Buyer\'s Supplier Quality Representative and shall flow down identical AS9100 Rev D and counterfeit electronic part avoidance (`AS5553`) controls to all sub-tier wafer foundries and forging sub-contractors.',
    '', '[]', '[]',
    'hold_firm',
    '7.1 (a) Accredited Aerospace QMS: Seller shall establish and maintain an IAQG-accredited `AS9100 Rev D` Quality Management System, `RTCA DO-178C` Design Assurance Level A (`DAL-A`) software lifecycle compliance, `RTCA DO-254` complex electronic hardware assurance, and Cymbal Aerospace Quality Management System Requirements for Suppliers (`D6-82479`) throughout Contract performance. (b) First Article Inspection & Sub-Tier Flowdown: Prior to initial production lot delivery, Seller shall complete a full `AS9102` First Article Inspection Report (`FAIR`) witnessed by Buyer\'s Supplier Quality Representative and shall flow down identical AS9100 Rev D and counterfeit electronic part avoidance (`AS5553`) controls to all sub-tier wafer foundries and forging sub-contractors.',
    'hold_firm',
    '7.1 (a) Accredited Aerospace QMS: Seller shall establish and maintain an IAQG-accredited `AS9100 Rev D` Quality Management System, `RTCA DO-178C` Design Assurance Level A (`DAL-A`) software lifecycle compliance, `RTCA DO-254` complex electronic hardware assurance, and Cymbal Aerospace Quality Management System Requirements for Suppliers (`D6-82479`) throughout Contract performance. (b) First Article Inspection & Sub-Tier Flowdown: Prior to initial production lot delivery, Seller shall complete a full `AS9102` First Article Inspection Report (`FAIR`) witnessed by Buyer\'s Supplier Quality Representative and shall flow down identical AS9100 Rev D and counterfeit electronic part avoidance (`AS5553`) controls to all sub-tier wafer foundries and forging sub-contractors.',
    'UNTOUCHED', 'Auto-Verified (No Redline)', 'Clause matches Cymbal Aerospace Proforma GP1 baseline with zero Track Changes.', CURRENT_TIMESTAMP()
  ),
  (
    'BA-2026-AV-8921', 'GP1-09', 'GP1', 'GP1 §9.1', 'Changes & Equitable Adjustment', FALSE,
    'PROCUREMENT', 'Procurement & Subcontracts', 'NONE', 'Cymbal Corporate GP1 Standard',
    '9.1 (a) Directed Engineering & Schedule Changes: Buyer\'s Authorized Procurement Representative may at any time, by written Change Order without notice to sureties, direct changes within the general scope of this Contract in (i) drawings, avionics bus interface control documents (`ICDs`), or technical specifications, (ii) method of shipment or aerospace preservation, or (iii) place and schedule of delivery. Seller shall proceed immediately with performance of the Contract as changed. (b) Equitable Adjustment Claims: If any directed change under §9.1(a) causes a verified increase or decrease in the cost of or time required for performance, Seller must assert any claim for equitable adjustment in writing within thirty (30) calendar days from receipt of the written Change Order, supported by certified cost and pricing data.',
    '9.1 (a) Directed Engineering & Schedule Changes: Buyer\'s Authorized Procurement Representative may at any time, by written Change Order without notice to sureties, direct changes within the general scope of this Contract in (i) drawings, avionics bus interface control documents (`ICDs`), or technical specifications, (ii) method of shipment or aerospace preservation, or (iii) place and schedule of delivery. Seller shall proceed immediately with performance of the Contract as changed. (b) Equitable Adjustment Claims: If any directed change under §9.1(a) causes a verified increase or decrease in the cost of or time required for performance, Seller must assert any claim for equitable adjustment in writing within thirty (30) calendar days from receipt of the written Change Order, supported by certified cost and pricing data.',
    '9.1 (a) Directed Engineering & Schedule Changes: Buyer\'s Authorized Procurement Representative may at any time, by written Change Order without notice to sureties, direct changes within the general scope of this Contract in (i) drawings, avionics bus interface control documents (`ICDs`), or technical specifications, (ii) method of shipment or aerospace preservation, or (iii) place and schedule of delivery. Seller shall proceed immediately with performance of the Contract as changed. (b) Equitable Adjustment Claims: If any directed change under §9.1(a) causes a verified increase or decrease in the cost of or time required for performance, Seller must assert any claim for equitable adjustment in writing within thirty (30) calendar days from receipt of the written Change Order, supported by certified cost and pricing data.',
    '', '[]', '[]',
    'hold_firm',
    '9.1 (a) Directed Engineering & Schedule Changes: Buyer\'s Authorized Procurement Representative may at any time, by written Change Order without notice to sureties, direct changes within the general scope of this Contract in (i) drawings, avionics bus interface control documents (`ICDs`), or technical specifications, (ii) method of shipment or aerospace preservation, or (iii) place and schedule of delivery. Seller shall proceed immediately with performance of the Contract as changed. (b) Equitable Adjustment Claims: If any directed change under §9.1(a) causes a verified increase or decrease in the cost of or time required for performance, Seller must assert any claim for equitable adjustment in writing within thirty (30) calendar days from receipt of the written Change Order, supported by certified cost and pricing data.',
    'hold_firm',
    '9.1 (a) Directed Engineering & Schedule Changes: Buyer\'s Authorized Procurement Representative may at any time, by written Change Order without notice to sureties, direct changes within the general scope of this Contract in (i) drawings, avionics bus interface control documents (`ICDs`), or technical specifications, (ii) method of shipment or aerospace preservation, or (iii) place and schedule of delivery. Seller shall proceed immediately with performance of the Contract as changed. (b) Equitable Adjustment Claims: If any directed change under §9.1(a) causes a verified increase or decrease in the cost of or time required for performance, Seller must assert any claim for equitable adjustment in writing within thirty (30) calendar days from receipt of the written Change Order, supported by certified cost and pricing data.',
    'UNTOUCHED', 'Auto-Verified (No Redline)', 'Clause matches Cymbal Aerospace Proforma GP1 baseline with zero Track Changes.', CURRENT_TIMESTAMP()
  ),
  (
    'BA-2026-AV-8921', 'GP1-12', 'GP1', 'GP1 §12.2', 'Warranty & FAA Source Inspection', TRUE,
    'ENGINEERING', 'Engineering & QA (FAA DER)', 'HIGH', 'FAA 14 CFR Part 21 Lockout',
    '12.2 (a) Airworthiness & Hardware/Firmware Warranty: Seller warrants all Goods, including `FCC-900` flight control hardware, triplex voting channels, and embedded `DO-178C DAL-A` avionics firmware, to be free from defects in design, material, and workmanship for thirty-six (36) months from initial aircraft delivery to Cymbal Aerospace\'s airline customer, and Seller shall repair or replace defective flight-critical LRUs on an Aircraft-on-Ground (`AOG`) 24-hour turnaround basis at Seller\'s expense. (b) Regulatory Source Surveillance: Cymbal Aerospace and Federal Aviation Administration (`FAA`) representatives may conduct unannounced source inspections at Seller\'s facility at any time to verify `AS9100 Rev D` quality compliance, `FAA 14 CFR Part 21.140` production certificate airworthiness conformity, and sub-tier test bench calibration records.',
    '12.2 (a) Airworthiness & Hardware/Firmware Warranty: Seller warrants all Goods, including `FCC-900` flight control hardware, triplex voting channels, and embedded `DO-178C DAL-A` avionics firmware, to be free from defects in design, material, and workmanship for twelve (12) months from factory shipment, and Seller shall repair or replace defective flight-critical LRUs on an Aircraft-on-Ground (`AOG`) 24-hour turnaround basis at Seller\'s expense. (b) Regulatory Source Surveillance: Cymbal Aerospace and Federal Aviation Administration (`FAA`) representatives may conduct scheduled inspections upon thirty (30) days prior written notice to verify `AS9100 Rev D` quality compliance, `FAA 14 CFR Part 21.140` production certificate airworthiness conformity, and sub-tier test bench calibration records.',
    '12.2 (a) Airworthiness & Hardware/Firmware Warranty: Seller warrants all Goods, including `FCC-900` flight control hardware, triplex voting channels, and embedded `DO-178C DAL-A` avionics firmware, to be free from defects in design, material, and workmanship for <span class="diff-del">thirty-six (36) months from initial aircraft delivery to Cymbal Aerospace\'s airline customer</span><span class="diff-add">twelve (12) months from factory shipment</span>, and Seller shall repair or replace defective flight-critical LRUs on an Aircraft-on-Ground (`AOG`) 24-hour turnaround basis at Seller\'s expense. (b) Regulatory Source Surveillance: Cymbal Aerospace and Federal Aviation Administration (`FAA`) representatives may conduct <span class="diff-del">unannounced source inspections at Seller\'s facility at any time</span><span class="diff-add">scheduled inspections upon thirty (30) days prior written notice</span> to verify `AS9100 Rev D` quality compliance, `FAA 14 CFR Part 21.140` production certificate airworthiness conformity, and sub-tier test bench calibration records.',
    'Apex AeroSystems Legal: Our standard commercial avionics warranty is 12 months from ex-works factory shipment, and unannounced facility audits disrupt Class-100 cleanroom assembly shifts; we require 30 days advance written notice.', '["twelve (12) months from factory shipment", "scheduled inspections upon thirty (30) days prior written notice"]', '["thirty-six (36) months from initial aircraft delivery to Cymbal Aerospace\'s airline customer", "unannounced source inspections at Seller\'s facility at any time"]',
    'hold_firm',
    '12.2 (a) Airworthiness & Hardware/Firmware Warranty: Seller warrants all Goods, including `FCC-900` flight control hardware, triplex voting channels, and embedded `DO-178C DAL-A` avionics firmware, to be free from defects in design, material, and workmanship for thirty-six (36) months from initial aircraft delivery to Cymbal Aerospace\'s airline customer, and Seller shall repair or replace defective flight-critical LRUs on an Aircraft-on-Ground (`AOG`) 24-hour turnaround basis at Seller\'s expense. (b) Regulatory Source Surveillance: Cymbal Aerospace and Federal Aviation Administration (`FAA`) representatives may conduct unannounced source inspections at Seller\'s facility at any time to verify `AS9100 Rev D` quality compliance, `FAA 14 CFR Part 21.140` production certificate airworthiness conformity, and sub-tier test bench calibration records.',
    'hold_firm',
    '12.2 (a) Airworthiness & Hardware/Firmware Warranty: Seller warrants all Goods, including `FCC-900` flight control hardware, triplex voting channels, and embedded `DO-178C DAL-A` avionics firmware, to be free from defects in design, material, and workmanship for thirty-six (36) months from initial aircraft delivery to Cymbal Aerospace\'s airline customer, and Seller shall repair or replace defective flight-critical LRUs on an Aircraft-on-Ground (`AOG`) 24-hour turnaround basis at Seller\'s expense. (b) Regulatory Source Surveillance: Cymbal Aerospace and Federal Aviation Administration (`FAA`) representatives may conduct unannounced source inspections at Seller\'s facility at any time to verify `AS9100 Rev D` quality compliance, `FAA 14 CFR Part 21.140` production certificate airworthiness conformity, and sub-tier test bench calibration records.',
    'APPROVED', 'Dr. Aris Thorne (Principal FAA DER, Flight Controls QA)', 'Rejected vendor 12-month warranty and 30-day inspection notice. FAA 14 CFR Part 21.140 and AS9100 Rev D mandate unannounced source inspection access at all times. Precedent shows 88% (14/16) held firm.', CURRENT_TIMESTAMP()
  ),
  (
    'BA-2026-AV-8921', 'GP1-15', 'GP1', 'GP1 §15.1', 'Termination for Convenience', FALSE,
    'LEGAL', 'Corporate Legal & Commercial', 'NONE', 'FAR 52.249-2 Aligned',
    '15.1 (a) Unilateral Right to Terminate: Buyer may terminate all or any severable portion of this Contract for convenience at any time by written notice of termination to Seller. Upon receipt of such notice, Seller shall immediately stop all terminated work, place no further sub-tier purchase orders for raw materials or semiconductors, and protect all property in which Buyer has or may acquire an interest. (b) Termination Settlement & Cap: Seller\'s sole recovery upon termination for convenience, aligned with `FAR 52.249-2` principles, shall be limited to documented actual costs incurred for work-in-process prior to termination notice plus a reasonable profit on completed work, never to exceed the terminated portion of the GP1 §3.1 Firm-Fixed-Price Contract value, with zero recovery for anticipatory or consequential profits.',
    '15.1 (a) Unilateral Right to Terminate: Buyer may terminate all or any severable portion of this Contract for convenience at any time by written notice of termination to Seller. Upon receipt of such notice, Seller shall immediately stop all terminated work, place no further sub-tier purchase orders for raw materials or semiconductors, and protect all property in which Buyer has or may acquire an interest. (b) Termination Settlement & Cap: Seller\'s sole recovery upon termination for convenience, aligned with `FAR 52.249-2` principles, shall be limited to documented actual costs incurred for work-in-process prior to termination notice plus a reasonable profit on completed work, never to exceed the terminated portion of the GP1 §3.1 Firm-Fixed-Price Contract value, with zero recovery for anticipatory or consequential profits.',
    '15.1 (a) Unilateral Right to Terminate: Buyer may terminate all or any severable portion of this Contract for convenience at any time by written notice of termination to Seller. Upon receipt of such notice, Seller shall immediately stop all terminated work, place no further sub-tier purchase orders for raw materials or semiconductors, and protect all property in which Buyer has or may acquire an interest. (b) Termination Settlement & Cap: Seller\'s sole recovery upon termination for convenience, aligned with `FAR 52.249-2` principles, shall be limited to documented actual costs incurred for work-in-process prior to termination notice plus a reasonable profit on completed work, never to exceed the terminated portion of the GP1 §3.1 Firm-Fixed-Price Contract value, with zero recovery for anticipatory or consequential profits.',
    '', '[]', '[]',
    'hold_firm',
    '15.1 (a) Unilateral Right to Terminate: Buyer may terminate all or any severable portion of this Contract for convenience at any time by written notice of termination to Seller. Upon receipt of such notice, Seller shall immediately stop all terminated work, place no further sub-tier purchase orders for raw materials or semiconductors, and protect all property in which Buyer has or may acquire an interest. (b) Termination Settlement & Cap: Seller\'s sole recovery upon termination for convenience, aligned with `FAR 52.249-2` principles, shall be limited to documented actual costs incurred for work-in-process prior to termination notice plus a reasonable profit on completed work, never to exceed the terminated portion of the GP1 §3.1 Firm-Fixed-Price Contract value, with zero recovery for anticipatory or consequential profits.',
    'hold_firm',
    '15.1 (a) Unilateral Right to Terminate: Buyer may terminate all or any severable portion of this Contract for convenience at any time by written notice of termination to Seller. Upon receipt of such notice, Seller shall immediately stop all terminated work, place no further sub-tier purchase orders for raw materials or semiconductors, and protect all property in which Buyer has or may acquire an interest. (b) Termination Settlement & Cap: Seller\'s sole recovery upon termination for convenience, aligned with `FAR 52.249-2` principles, shall be limited to documented actual costs incurred for work-in-process prior to termination notice plus a reasonable profit on completed work, never to exceed the terminated portion of the GP1 §3.1 Firm-Fixed-Price Contract value, with zero recovery for anticipatory or consequential profits.',
    'UNTOUCHED', 'Auto-Verified (No Redline)', 'Clause matches Cymbal Aerospace Proforma GP1 baseline with zero Track Changes.', CURRENT_TIMESTAMP()
  ),
  (
    'BA-2026-AV-8921', 'GP1-19', 'GP1', 'GP1 §19 & §24', 'Limitation of Liability & IP Indemnity', TRUE,
    'LEGAL', 'Corporate Legal & IP', 'CRITICAL', 'Corporate Legal Playbook Tier-1',
    '19.1 (a) Direct, Line-Stoppage & Airworthiness Recall Liability: Seller\'s aggregate liability to Cymbal Aerospace for direct damages, Everett/Renton final assembly line-stoppage costs, Fleet Airworthiness Directive (`AD`) grounding/retrofit campaigns, and airworthiness recall costs shall be uncapped. 24.1 (b) Intellectual Property Indemnification: Seller shall defend, indemnify, and hold harmless Cymbal Aerospace and its airline customers against all third-party patent, copyright, trade secret, and intellectual property infringement claims arising from the manufacture, sale, or use of the Goods including system-level avionics bus integration, and if any `FCC-900` unit is enjoined, Seller shall at its sole expense procure a perpetual royalty-free license or re-architect the infringing avionics module to maintain FAA type-design airworthiness.',
    '19.1 (a) Direct, Line-Stoppage & Airworthiness Recall Liability: Seller\'s aggregate liability to Cymbal Aerospace for direct damages, Everett/Renton final assembly line-stoppage costs, Fleet Airworthiness Directive (`AD`) grounding/retrofit campaigns, and airworthiness recall costs shall not exceed one hundred percent (100%) of the total Purchase Order value ($45M). 24.1 (b) Intellectual Property Indemnification: Seller shall defend, indemnify, and hold harmless Cymbal Aerospace and its airline customers against all third-party patent, copyright, trade secret, and intellectual property infringement claims arising from the manufacture, sale, or use of the Goods except where such claim arises from combination of Goods with any Cymbal Aerospace or third-party flight control bus, and if any `FCC-900` unit is enjoined, Seller shall at its sole expense procure a perpetual royalty-free license or re-architect the infringing avionics module to maintain FAA type-design airworthiness.',
    '19.1 (a) Direct, Line-Stoppage & Airworthiness Recall Liability: Seller\'s aggregate liability to Cymbal Aerospace for direct damages, Everett/Renton final assembly line-stoppage costs, Fleet Airworthiness Directive (`AD`) grounding/retrofit campaigns, and airworthiness recall costs shall <span class="diff-del">be uncapped</span><span class="diff-add">not exceed one hundred percent (100%) of the total Purchase Order value ($45M)</span>. 24.1 (b) Intellectual Property Indemnification: Seller shall defend, indemnify, and hold harmless Cymbal Aerospace and its airline customers against all third-party patent, copyright, trade secret, and intellectual property infringement claims arising from the manufacture, sale, or use of the Goods<span class="diff-del"> including system-level avionics bus integration</span><span class="diff-add"> except where such claim arises from combination of Goods with any Cymbal Aerospace or third-party flight control bus</span>, and if any `FCC-900` unit is enjoined, Seller shall at its sole expense procure a perpetual royalty-free license or re-architect the infringing avionics module to maintain FAA type-design airworthiness.',
    'Apex AeroSystems Legal: Board risk policy requires a strict 1x PO liability cap ($45M) across all direct/recall damages and a standard commercial carveout excluding IP claims arising from combination of our LRUs with Cymbal Aerospace\'s flight control bus.', '["not exceed one hundred percent (100%) of the total Purchase Order value ($45M)", " except where such claim arises from combination of Goods with any Cymbal Aerospace or third-party flight control bus"]', '["be uncapped", " including system-level avionics bus integration"]',
    'compromise_tier_1',
    '19.1 (a) Direct, Line-Stoppage & Airworthiness Recall Liability: Seller\'s liability for general direct damages and final assembly line-stoppage shall be capped at two hundred percent (200%) of the total Purchase Order value ($90M), provided that liability for Fleet Airworthiness Directive (`AD`) recall, gross negligence, willful misconduct, and §24 IP indemnification shall remain strictly uncapped. 24.1 (b) Intellectual Property Indemnification: Seller shall defend, indemnify, and hold harmless Cymbal Aerospace and its airline customers against all third-party intellectual property infringement claims including system-level avionics bus integration, except where such claim arises solely from Cymbal Aerospace\'s proprietary flight control bus specifications.',
    'compromise_tier_1',
    '19.1 (a) Direct, Line-Stoppage & Airworthiness Recall Liability: Seller\'s liability for general direct damages and final assembly line-stoppage shall be capped at two hundred percent (200%) of the total Purchase Order value ($90M), provided that liability for Fleet Airworthiness Directive (`AD`) recall, gross negligence, willful misconduct, and §24 IP indemnification shall remain strictly uncapped. 24.1 (b) Intellectual Property Indemnification: Seller shall defend, indemnify, and hold harmless Cymbal Aerospace and its airline customers against all third-party intellectual property infringement claims including system-level avionics bus integration, except where such claim arises solely from Cymbal Aerospace\'s proprietary flight control bus specifications.',
    'APPROVED', 'Elena Rostova, J.D. (Senior Counsel, Commercial & IP)', 'Applied Playbook Tier-1 Compromise (69% historical precedent across 11/16 Tier-1 avionics deals): 2x PO ($90M) super-cap on general direct damages while holding uncapped liability for airworthiness recall and IP indemnity, narrowing the IP carveout strictly to Cymbal Aerospace proprietary bus specifications.', CURRENT_TIMESTAMP()
  ),
  (
    'BA-2026-AV-8921', 'GP1-28', 'GP1', 'GP1 §28.1', 'Governing Law & Dispute Resolution', FALSE,
    'LEGAL', 'Corporate Legal', 'NONE', 'Delaware / Washington Law Standard',
    '28.1 (a) Governing Law & Exclusive Venue: This Contract and all claims, controversies, or disputes arising hereunder shall be governed by and construed in accordance with the substantive laws of the State of Delaware, excluding its conflict of laws rules and excluding the United Nations Convention on Contracts for the International Sale of Goods (`CISG`). Exclusive judicial venue shall lie in the state or federal courts located in Wilmington, Delaware or King County, Washington. (b) Continuity of Flight-Critical Supply: Pending final resolution of any dispute, claim, or Change Order valuation, Seller shall proceed diligently with uninterrupted manufacture, testing, and delivery of all `FCC-900` flight control units in accordance with Buyer\'s production schedule.',
    '28.1 (a) Governing Law & Exclusive Venue: This Contract and all claims, controversies, or disputes arising hereunder shall be governed by and construed in accordance with the substantive laws of the State of Delaware, excluding its conflict of laws rules and excluding the United Nations Convention on Contracts for the International Sale of Goods (`CISG`). Exclusive judicial venue shall lie in the state or federal courts located in Wilmington, Delaware or King County, Washington. (b) Continuity of Flight-Critical Supply: Pending final resolution of any dispute, claim, or Change Order valuation, Seller shall proceed diligently with uninterrupted manufacture, testing, and delivery of all `FCC-900` flight control units in accordance with Buyer\'s production schedule.',
    '28.1 (a) Governing Law & Exclusive Venue: This Contract and all claims, controversies, or disputes arising hereunder shall be governed by and construed in accordance with the substantive laws of the State of Delaware, excluding its conflict of laws rules and excluding the United Nations Convention on Contracts for the International Sale of Goods (`CISG`). Exclusive judicial venue shall lie in the state or federal courts located in Wilmington, Delaware or King County, Washington. (b) Continuity of Flight-Critical Supply: Pending final resolution of any dispute, claim, or Change Order valuation, Seller shall proceed diligently with uninterrupted manufacture, testing, and delivery of all `FCC-900` flight control units in accordance with Buyer\'s production schedule.',
    '', '[]', '[]',
    'hold_firm',
    '28.1 (a) Governing Law & Exclusive Venue: This Contract and all claims, controversies, or disputes arising hereunder shall be governed by and construed in accordance with the substantive laws of the State of Delaware, excluding its conflict of laws rules and excluding the United Nations Convention on Contracts for the International Sale of Goods (`CISG`). Exclusive judicial venue shall lie in the state or federal courts located in Wilmington, Delaware or King County, Washington. (b) Continuity of Flight-Critical Supply: Pending final resolution of any dispute, claim, or Change Order valuation, Seller shall proceed diligently with uninterrupted manufacture, testing, and delivery of all `FCC-900` flight control units in accordance with Buyer\'s production schedule.',
    'hold_firm',
    '28.1 (a) Governing Law & Exclusive Venue: This Contract and all claims, controversies, or disputes arising hereunder shall be governed by and construed in accordance with the substantive laws of the State of Delaware, excluding its conflict of laws rules and excluding the United Nations Convention on Contracts for the International Sale of Goods (`CISG`). Exclusive judicial venue shall lie in the state or federal courts located in Wilmington, Delaware or King County, Washington. (b) Continuity of Flight-Critical Supply: Pending final resolution of any dispute, claim, or Change Order valuation, Seller shall proceed diligently with uninterrupted manufacture, testing, and delivery of all `FCC-900` flight control units in accordance with Buyer\'s production schedule.',
    'UNTOUCHED', 'Auto-Verified (No Redline)', 'Clause matches Cymbal Aerospace Proforma GP1 baseline with zero Track Changes.', CURRENT_TIMESTAMP()
  ),
  (
    'BA-2026-AV-8921', 'SP3-02', 'SP3', 'SP3 §2.1', 'Export Compliance (ITAR & EAR)', FALSE,
    'TAX', 'Global Trade Controls', 'NONE', '22 CFR 120-130 (ITAR) / 15 CFR 730-774 (EAR)',
    '2.1 (a) Export Control Regulatory Compliance: Seller shall comply with all applicable U.S. export control laws and regulations, including the International Traffic in Arms Regulations (`ITAR`, 22 CFR Parts 120–130) and the Export Administration Regulations (`EAR`, 15 CFR Parts 730–774), covering dual-use flight control algorithms (`ECCN 7A994` / `7E994`) and defense technical data. (b) Export Classification & Deemed Exports: Seller shall maintain active DDTC registration where applicable, furnish accurate ECCN/USML Commodity Jurisdiction classifications prior to first shipment, and prevent unauthorized deemed exports of Cymbal Aerospace technical data to foreign nationals without prior U.S. Department of State or Bureau of Industry and Security (`BIS`) authorization.',
    '2.1 (a) Export Control Regulatory Compliance: Seller shall comply with all applicable U.S. export control laws and regulations, including the International Traffic in Arms Regulations (`ITAR`, 22 CFR Parts 120–130) and the Export Administration Regulations (`EAR`, 15 CFR Parts 730–774), covering dual-use flight control algorithms (`ECCN 7A994` / `7E994`) and defense technical data. (b) Export Classification & Deemed Exports: Seller shall maintain active DDTC registration where applicable, furnish accurate ECCN/USML Commodity Jurisdiction classifications prior to first shipment, and prevent unauthorized deemed exports of Cymbal Aerospace technical data to foreign nationals without prior U.S. Department of State or Bureau of Industry and Security (`BIS`) authorization.',
    '2.1 (a) Export Control Regulatory Compliance: Seller shall comply with all applicable U.S. export control laws and regulations, including the International Traffic in Arms Regulations (`ITAR`, 22 CFR Parts 120–130) and the Export Administration Regulations (`EAR`, 15 CFR Parts 730–774), covering dual-use flight control algorithms (`ECCN 7A994` / `7E994`) and defense technical data. (b) Export Classification & Deemed Exports: Seller shall maintain active DDTC registration where applicable, furnish accurate ECCN/USML Commodity Jurisdiction classifications prior to first shipment, and prevent unauthorized deemed exports of Cymbal Aerospace technical data to foreign nationals without prior U.S. Department of State or Bureau of Industry and Security (`BIS`) authorization.',
    '', '[]', '[]',
    'hold_firm',
    '2.1 (a) Export Control Regulatory Compliance: Seller shall comply with all applicable U.S. export control laws and regulations, including the International Traffic in Arms Regulations (`ITAR`, 22 CFR Parts 120–130) and the Export Administration Regulations (`EAR`, 15 CFR Parts 730–774), covering dual-use flight control algorithms (`ECCN 7A994` / `7E994`) and defense technical data. (b) Export Classification & Deemed Exports: Seller shall maintain active DDTC registration where applicable, furnish accurate ECCN/USML Commodity Jurisdiction classifications prior to first shipment, and prevent unauthorized deemed exports of Cymbal Aerospace technical data to foreign nationals without prior U.S. Department of State or Bureau of Industry and Security (`BIS`) authorization.',
    'hold_firm',
    '2.1 (a) Export Control Regulatory Compliance: Seller shall comply with all applicable U.S. export control laws and regulations, including the International Traffic in Arms Regulations (`ITAR`, 22 CFR Parts 120–130) and the Export Administration Regulations (`EAR`, 15 CFR Parts 730–774), covering dual-use flight control algorithms (`ECCN 7A994` / `7E994`) and defense technical data. (b) Export Classification & Deemed Exports: Seller shall maintain active DDTC registration where applicable, furnish accurate ECCN/USML Commodity Jurisdiction classifications prior to first shipment, and prevent unauthorized deemed exports of Cymbal Aerospace technical data to foreign nationals without prior U.S. Department of State or Bureau of Industry and Security (`BIS`) authorization.',
    'UNTOUCHED', 'Auto-Verified (No Redline)', 'Clause matches Cymbal Aerospace Proforma SP3 baseline with zero Track Changes.', CURRENT_TIMESTAMP()
  ),
  (
    'BA-2026-AV-8921', 'SP3-04', 'SP3', 'SP3 §4.1', 'Customs, Duties & International Tariffs', TRUE,
    'TAX', 'Global Tax & Trade', 'MOD', 'Cross-Clause SOW §3.1 Dependency',
    '4.1 (a) Importer of Record & Customs Clearance: Seller shall act as Importer of Record for all imported sub-tier components, raw aerospace titanium forgings, and radiation-hardened semiconductor wafers. (b) Tariff & Duty Allocation: All unit prices in Statement of Work (`SOW-AV-8921`) Schedule A are DDP (Incoterms 2020) Cymbal Aerospace Everett/Renton facility and inclusive of all import duties, customs fees, and tariffs, and Seller shall cooperate with Buyer\'s Global Trade team on U.S. CBP duty drawback documentation.',
    '4.1 (a) Importer of Record & Customs Clearance: Seller shall act as Importer of Record for all imported sub-tier components, raw aerospace titanium forgings, and radiation-hardened semiconductor wafers. (b) Tariff & Duty Allocation: All unit prices in Statement of Work (`SOW-AV-8921`) Schedule A are exclusive of any new or increased Section 232/301 tariffs on titanium forgings or semiconductor wafers exceeding five percent (5%), which shall be passed through 100% to Cymbal Aerospace, and Seller shall cooperate with Buyer\'s Global Trade team on U.S. CBP duty drawback documentation.',
    '4.1 (a) Importer of Record & Customs Clearance: Seller shall act as Importer of Record for all imported sub-tier components, raw aerospace titanium forgings, and radiation-hardened semiconductor wafers. (b) Tariff & Duty Allocation: All unit prices in Statement of Work (`SOW-AV-8921`) Schedule A are <span class="diff-del">DDP (Incoterms 2020) Cymbal Aerospace Everett/Renton facility and inclusive of all import duties, customs fees, and tariffs</span><span class="diff-add">exclusive of any new or increased Section 232/301 tariffs on titanium forgings or semiconductor wafers exceeding five percent (5%), which shall be passed through 100% to Cymbal Aerospace</span>, and Seller shall cooperate with Buyer\'s Global Trade team on U.S. CBP duty drawback documentation.',
    'Apex AeroSystems Tax: Due to volatile Section 232/301 trade duties on European titanium forgings and Taiwanese semiconductor wafers, Seller cannot absorb open-ended tariff spikes under DDP pricing and requires 100% pass-through of tariff increases above 5%.', '["exclusive of any new or increased Section 232/301 tariffs on titanium forgings or semiconductor wafers exceeding five percent (5%), which shall be passed through 100% to Cymbal Aerospace"]', '["DDP (Incoterms 2020) Cymbal Aerospace Everett/Renton facility and inclusive of all import duties, customs fees, and tariffs"]',
    'compromise_tier_1',
    '4.1 (a) Importer of Record & Customs Clearance: Seller shall act as Importer of Record for all imported sub-tier components, raw aerospace titanium forgings, and radiation-hardened semiconductor wafers. (b) Tariff & Duty Allocation: All unit prices in Statement of Work (`SOW-AV-8921`) Schedule A are DDP (Incoterms 2020) Cymbal Aerospace Everett/Renton facility. Any verified new Section 232/301 tariff increase exceeding 5.0% on raw titanium forgings or semiconductor wafers shall be shared 50/50 between Cymbal Aerospace and Seller, strictly capped at a maximum aggregate adjustment of 2.0% of the GP1 §3.1 Firm-Fixed-Price SOW unit price.',
    'accept_vendor',
    '4.1 (a) Importer of Record & Customs Clearance: Seller shall act as Importer of Record for all imported sub-tier components, raw aerospace titanium forgings, and radiation-hardened semiconductor wafers. (b) Tariff & Duty Allocation: All unit prices in Statement of Work (`SOW-AV-8921`) Schedule A are exclusive of any new or increased Section 232/301 tariffs on titanium forgings or semiconductor wafers exceeding five percent (5%), which shall be passed through 100% to Cymbal Aerospace, and Seller shall cooperate with Buyer\'s Global Trade team on U.S. CBP duty drawback documentation.',
    'CONFLICT', 'Marcus Chen, CPA (Director, Global Tax & Trade)', 'Accepted vendor >5% Section 232/301 titanium and wafer tariff pass-through to avoid Q3 avionics delivery delay, pending Procurement verification against SOW cap.', CURRENT_TIMESTAMP()
  ),
  (
    'BA-2026-AV-8921', 'SP5-03', 'SP5', 'SP5 §3.2', 'Cybersecurity Incident Reporting (DFARS)', TRUE,
    'CYBER', 'Supplier Cyber Defense', 'HIGH', 'DFARS 252.204-7012 Lockout',
    '3.2 (a) CUI Safeguards & NIST SP 800-171 Rev 2 Compliance: Seller shall maintain an accredited Cybersecurity Maturity Model Certification (`CMMC 2.0 Level 2`) posture and implement all 110 security controls in `NIST SP 800-171 Rev 2` across all engineering networks storing or processing Cymbal Aerospace Covered Defense Information (`CDI`), Controlled Unclassified Information (`CUI`), or `FCC-900` flight control source code. (b) Mandatory Cyber Incident Reporting & Forensics: Pursuant to `DoD DFARS 252.204-7012`, Seller shall report any cybersecurity incident affecting Cymbal Aerospace CDI or technical data to Buyer\'s Cyber Security Operations Center (`CSOC`) and the DoD DIBNet portal within seventy-two (72) hours of discovery, preserve affected system media for ninety (90) days, and provide raw forensic log images and malware telemetry upon request.',
    '3.2 (a) CUI Safeguards & NIST SP 800-171 Rev 2 Compliance: Seller shall maintain an accredited Cybersecurity Maturity Model Certification (`CMMC 2.0 Level 2`) posture and implement all 110 security controls in `NIST SP 800-171 Rev 2` across all engineering networks storing or processing Cymbal Aerospace Covered Defense Information (`CDI`), Controlled Unclassified Information (`CUI`), or `FCC-900` flight control source code. (b) Mandatory Cyber Incident Reporting & Forensics: Pursuant to `DoD DFARS 252.204-7012`, Seller shall report any cybersecurity incident affecting Cymbal Aerospace CDI or technical data to Buyer\'s Cyber Security Operations Center (`CSOC`) and the DoD DIBNet portal within ten (10) business days following confirmation of a material breach, preserve affected system media for ninety (90) days, and provide raw forensic log images and malware telemetry upon request.',
    '3.2 (a) CUI Safeguards & NIST SP 800-171 Rev 2 Compliance: Seller shall maintain an accredited Cybersecurity Maturity Model Certification (`CMMC 2.0 Level 2`) posture and implement all 110 security controls in `NIST SP 800-171 Rev 2` across all engineering networks storing or processing Cymbal Aerospace Covered Defense Information (`CDI`), Controlled Unclassified Information (`CUI`), or `FCC-900` flight control source code. (b) Mandatory Cyber Incident Reporting & Forensics: Pursuant to `DoD DFARS 252.204-7012`, Seller shall report any cybersecurity incident affecting Cymbal Aerospace CDI or technical data to Buyer\'s Cyber Security Operations Center (`CSOC`) and the DoD DIBNet portal within <span class="diff-del">seventy-two (72) hours of discovery</span><span class="diff-add">ten (10) business days following confirmation of a material breach</span>, preserve affected system media for ninety (90) days, and provide raw forensic log images and malware telemetry upon request.',
    'Apex AeroSystems CISO: Our internal Security Operations Center (SOC) requires 10 business days to complete forensic root-cause triage and confirm a material breach before issuing external customer notifications.', '["ten (10) business days following confirmation of a material breach"]', '["seventy-two (72) hours of discovery"]',
    'hold_firm',
    '3.2 (a) CUI Safeguards & NIST SP 800-171 Rev 2 Compliance: Seller shall maintain an accredited Cybersecurity Maturity Model Certification (`CMMC 2.0 Level 2`) posture and implement all 110 security controls in `NIST SP 800-171 Rev 2` across all engineering networks storing or processing Cymbal Aerospace Covered Defense Information (`CDI`), Controlled Unclassified Information (`CUI`), or `FCC-900` flight control source code. (b) Mandatory Cyber Incident Reporting & Forensics: Pursuant to `DoD DFARS 252.204-7012`, Seller shall report any cybersecurity incident affecting Cymbal Aerospace CDI or technical data to Buyer\'s Cyber Security Operations Center (`CSOC`) and the DoD DIBNet portal within seventy-two (72) hours of discovery, preserve affected system media for ninety (90) days, and provide raw forensic log images and malware telemetry upon request.',
    'hold_firm',
    '3.2 (a) CUI Safeguards & NIST SP 800-171 Rev 2 Compliance: Seller shall maintain an accredited Cybersecurity Maturity Model Certification (`CMMC 2.0 Level 2`) posture and implement all 110 security controls in `NIST SP 800-171 Rev 2` across all engineering networks storing or processing Cymbal Aerospace Covered Defense Information (`CDI`), Controlled Unclassified Information (`CUI`), or `FCC-900` flight control source code. (b) Mandatory Cyber Incident Reporting & Forensics: Pursuant to `DoD DFARS 252.204-7012`, Seller shall report any cybersecurity incident affecting Cymbal Aerospace CDI or technical data to Buyer\'s Cyber Security Operations Center (`CSOC`) and the DoD DIBNet portal within seventy-two (72) hours of discovery, preserve affected system media for ninety (90) days, and provide raw forensic log images and malware telemetry upon request.',
    'APPROVED', 'Capt. Devon Brooks (Lead, Supplier Cyber Defense)', 'Held firm on 72-hour incident notification. DFARS 252.204-7012 and NIST SP 800-171 impose a non-negotiable 72-hour DoD reporting window (94% held firm across 15/16 historical contracts).', CURRENT_TIMESTAMP()
  );

-- 7. Seed Immutable SME Review Events Audit Trail
TRUNCATE TABLE `vertex-ai-demos-468803.boeing_clm.sme_review_events`;

INSERT INTO `vertex-ai-demos-468803.boeing_clm.sme_review_events` (
  event_id, deal_id, clause_id, sme_team, actor, action,
  selected_option_key, selected_counter_text, rationale, source_surface, created_at
)
VALUES
  (
    'EVT-8921-001', 'BA-2026-AV-8921', 'ALL', 'PROCUREMENT',
    'Lead Contract Owner (M. Vance)', 'INGESTED_REDLINE', 'hold_firm',
    'Parsed 12 clauses from Vendor_Redlined_GP1.docx: 8 untouched auto-collapsed, 4 redlined routed to Engineering, Legal, Tax, and Cyber SMEs.',
    'Deterministic OOXML Track Changes extraction completed against Cymbal_GP1_Standard.docx.',
    'GEMINI_AGENT_MCP', TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 25 MINUTE)
  ),
  (
    'EVT-8921-002', 'BA-2026-AV-8921', 'GP1-12', 'ENGINEERING',
    'Dr. Aris Thorne (Principal FAA DER, Flight Controls QA)', 'SME_APPROVED', 'hold_firm',
    '12.2 (a) Airworthiness & Hardware/Firmware Warranty: Seller warrants all Goods, including `FCC-900` flight control hardware, triplex voting channels, and embedded `DO-178C DAL-A` avionics firmware, to be free from defects in design, material, and workmanship for thirty-six (36) months from initial aircraft delivery to Cymbal Aerospace\'s airline customer, and Seller shall repair or replace defective flight-critical LRUs on an Aircraft-on-Ground (`AOG`) 24-hour turnaround basis at Seller\'s expense. (b) Regulatory Source Surveillance: Cymbal Aerospace and Federal Aviation Administration (`FAA`) representatives may conduct unannounced source inspections at Seller\'s facility at any time to verify `AS9100 Rev D` quality compliance, `FAA 14 CFR Part 21.140` production certificate airworthiness conformity, and sub-tier test bench calibration records.',
    'Enforced FAA 14 CFR Part 21.140 unannounced inspection lockout and 36-month warranty (88% held firm across 16 precedents).',
    'EXPERIENCE_LAYER_UI', TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 18 MINUTE)
  ),
  (
    'EVT-8921-003', 'BA-2026-AV-8921', 'GP1-19', 'LEGAL',
    'Elena Rostova, J.D. (Senior Counsel, Commercial & IP)', 'SME_APPROVED', 'compromise_tier_1',
    '19.1 (a) Direct, Line-Stoppage & Airworthiness Recall Liability: Seller\'s liability for general direct damages and final assembly line-stoppage shall be capped at two hundred percent (200%) of the total Purchase Order value ($90M), provided that liability for Fleet Airworthiness Directive (`AD`) recall, gross negligence, willful misconduct, and §24 IP indemnification shall remain strictly uncapped. 24.1 (b) Intellectual Property Indemnification: Seller shall defend, indemnify, and hold harmless Cymbal Aerospace and its airline customers against all third-party intellectual property infringement claims including system-level avionics bus integration, except where such claim arises solely from Cymbal Aerospace\'s proprietary flight control bus specifications.',
    'Selected Playbook Tier-1 Compromise (2x PO $90M super-cap + narrowed Cymbal Aerospace sole-spec IP carveout; 69% Tier-1 precedent).',
    'EXPERIENCE_LAYER_UI', TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 12 MINUTE)
  ),
  (
    'EVT-8921-004', 'BA-2026-AV-8921', 'SP5-03', 'CYBER',
    'Capt. Devon Brooks (Lead, Supplier Cyber Defense)', 'SME_APPROVED', 'hold_firm',
    '3.2 (a) CUI Safeguards & NIST SP 800-171 Rev 2 Compliance: Seller shall maintain an accredited Cybersecurity Maturity Model Certification (`CMMC 2.0 Level 2`) posture and implement all 110 security controls in `NIST SP 800-171 Rev 2` across all engineering networks storing or processing Cymbal Aerospace Covered Defense Information (`CDI`), Controlled Unclassified Information (`CUI`), or `FCC-900` flight control source code. (b) Mandatory Cyber Incident Reporting & Forensics: Pursuant to `DoD DFARS 252.204-7012`, Seller shall report any cybersecurity incident affecting Cymbal Aerospace CDI or technical data to Buyer\'s Cyber Security Operations Center (`CSOC`) and the DoD DIBNet portal within seventy-two (72) hours of discovery, preserve affected system media for ninety (90) days, and provide raw forensic log images and malware telemetry upon request.',
    'Enforced DFARS 252.204-7012 mandatory 72-hour cyber incident reporting lockout (94% held firm across 16 precedents).',
    'EXPERIENCE_LAYER_UI', TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 MINUTE)
  ),
  (
    'EVT-8921-005', 'BA-2026-AV-8921', 'SP3-04', 'TAX',
    'Marcus Chen, CPA (Director, Global Tax & Trade)', 'CONFLICT_TRIGGERED', 'accept_vendor',
    '4.1 (a) Importer of Record & Customs Clearance: Seller shall act as Importer of Record for all imported sub-tier components, raw aerospace titanium forgings, and radiation-hardened semiconductor wafers. (b) Tariff & Duty Allocation: All unit prices in Statement of Work (`SOW-AV-8921`) Schedule A are exclusive of any new or increased Section 232/301 tariffs on titanium forgings or semiconductor wafers exceeding five percent (5%), which shall be passed through 100% to Cymbal Aerospace, and Seller shall cooperate with Buyer\'s Global Trade team on U.S. CBP duty drawback documentation.',
    'Global Tax acceptance of uncapped >5% Section 232/301 tariff pass-through triggered CRITICAL_CONFLICT with GP1 §3.1 Firm-Fixed-Price SOW Cap ($45M ceiling).',
    'EXPERIENCE_LAYER_UI', TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 2 MINUTE)
  );
