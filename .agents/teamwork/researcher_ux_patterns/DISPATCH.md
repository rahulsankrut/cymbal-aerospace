## 2026-10-20 — researcher_ux_patterns
You are `researcher_ux_patterns` (`worker` / Aerospace CLM Persona & Interaction Architect).

### Must Read First
- `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.agents/teamwork/ORIGINAL_REQUEST.md`
- `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.agents/teamwork/BRIEFING.md`
- `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/CYMBAL_AEROSPACE_DEMO_GUIDE.md`
- `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/specs/02_domain_models.py`
- `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/specs/03_mcp_and_rest_contract.md`

### Strict Ownership Scope
- **Allowed to create/edit**: `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.agents/teamwork/researcher_ux_patterns/handoff.md`
- **Forbidden to edit**: `specs/*`, `src/*`, `skills/*`

### Mission & Acceptance Criteria
1. Analyze the end-to-end user journey across the 4 Cymbal Aerospace CLM workflows (`clm-contract-intake`, `clm-comms`, `clm-tax-tariff-review`, `clm-contract-consolidation`) and the 5 personas:
   - **Rahul Kasanagottu** (Contract Owner / Sr. Procurement Specialist)
   - **Megan Bowen** (Engineering & FAA Airworthiness DER — `GP1 §12.2` Lockout)
   - **Lee Gu** (VP Aviation Legal & IP Counsel — `GP1 §19 & §24` $90M Super-Cap)
   - **Pradeep Gupta** (VP Global Tax & Trade — `SP3 §4.1` vs `GP1 §3.1` FFP Conflict)
   - **Alex Wilber** (CISO & Defense Cyber — `SP5 §3.2` DFARS 72-Hr Lockout)
2. Identify the critical micro-interactions that MUST work seamlessly in the UI:
   - **Visualizing the Counter-Position Diff**: Showing *what changed* between the Vendor's Redline and Cymbal's Recommended Counter-Position (strikethrough + highlight), and immediately resolving into clean accepted contract text when the user clicks **Accept changes**.
   - **Rewriting with Input / Inline Editing**: Allowing the reviewer or owner to edit the counter-position text or apply AI/Playbook presets (`Hold Firm`, `Tier-1 Compromise`, `Accept Vendor`, `Custom Rewrite`) and see the live diff update in real time.
   - **Human User Commenting (`w:author`)**: Adding comments attributed to the logged-in reviewer (`Rahul Kasanagottu`, `Pradeep Gupta`, etc.) that persist to `BA-2026-AV-8921_Working_Review.docx` and display as margin comment cards.
   - **Precedent Grounding Across All 4 Clauses**: Every clause (`GP1-12`, `GP1-19`, `SP3-04`, `SP5-03`) shows its 16 historical BigQuery Tier-1 Avionics precedents, similarity scores, and outcome breakdown bar.
   - **User Evaluation & Note-Taking Bar**: Design an interactive floating/docked **UX Evaluator & Notes Drawer** inside the 12-Variation Mockup Lab so the user can test each of the 12 variations, rate it (1–5 stars), check off favorite components ("Keep Header", "Keep Diff Card", "Keep Precedent Drawer", "Keep Action Menu"), write freeform test notes per variation, and export/save all notes with 1 click.
3. Write your complete UX Architecture & Evaluation Plan to `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.agents/teamwork/researcher_ux_patterns/handoff.md`.
