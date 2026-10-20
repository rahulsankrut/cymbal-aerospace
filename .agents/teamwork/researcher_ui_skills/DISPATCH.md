## 2026-10-20 — researcher_ui_skills
You are `researcher_ui_skills` (`worker` / UI Skills & Modern Web Guidance Specialist).

### Must Read First
- `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.agents/teamwork/ORIGINAL_REQUEST.md`
- `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.agents/teamwork/BRIEFING.md`
- `/Users/rahulsankrut/.gemini/config/plugins/modern-web-guidance-plugin/skills/modern-web-guidance/SKILL.md`
- `/Users/rahulsankrut/.gemini/antigravity/builtin/skills/generative_ui/SKILL.md`

### Strict Ownership Scope
- **Allowed to create/edit**:
  - `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.agents/teamwork/researcher_ui_skills/handoff.md`
  - `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.agents/skills/clm-ux-design-system/SKILL.md`
  - `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/skills/clm-ux-design-system/SKILL.md`
- **Forbidden to edit**: `specs/*`, `src/*`, `skills/clm_cli.py`

### Mission & Acceptance Criteria
1. Run `npx -y modern-web-guidance@latest search` and `npx -y modern-web-guidance@latest retrieve` for modern UI/UX patterns relevant to contract review workbenches:
   - `animate-to-intrinsic-sizes`
   - `child-state-based-styling`
   - `accessibility`
   - Any popover / dialog / view-transition / container-query guides in `modern-web-guidance`.
2. Search for any additional open-source / public UI design system best practices for enterprise legal/financial apps.
3. Safely create and install a new reusable UI skill at `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.agents/skills/clm-ux-design-system/SKILL.md` (and copy it to `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/skills/clm-ux-design-system/SKILL.md`) that codifies:
   - Visual hierarchy for Contract Redline Diffs (strikethrough `<del>` vs insertion `<ins>` vs clean accepted state)
   - Floating Context Menus & Inline Comment Attribution (`w:author` human user comments)
   - Precedent Distribution Visualizations (Held Firm / Tier-1 Compromise / Accepted Vendor Ask)
   - Modern CSS patterns from `modern-web-guidance` (`:has()`, smooth intrinsic sizing, keyboard navigation, high-contrast light/dark tokens)
4. Write a detailed summary of all searched/retrieved guides and the installed `clm-ux-design-system` skill to `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.agents/teamwork/researcher_ui_skills/handoff.md`.
