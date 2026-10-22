# Contract Cross-Referencing & Clause Exit Gates

Use these rules during **Phase 2: Audit & Decision Logic** to process clauses
deterministically, prevent reasoning loops, and check multi-clause legal
dependencies. **DO NOT output any Phase 2 audit text to the user.**

--------------------------------------------------------------------------------

## Phase 2 Decision Schema (Surgical XML Data Model)

Use this XML format to structure your internal evaluation for clauses reaching
Gate 3 (redlines, modifications, omissions, warnings, or escalations) and save
these records into the `clause_audit_scratchpad.xml` session artifact under the
hood. For compliant clauses accepted under Gate 1 or Gate 2, do not generate an
XML record. **CRITICAL: Keep this evaluation strictly internal.**

```xml
<clause_audit>
  <clause_reference>Section Name or Missing Topic</clause_reference>

  <scratchpad>
    - Topic: [Identify the topic]
    - Current Draft Analysis: [Briefly state what the counterparty's clause actually says or demands]
    - Playbook/Heuristic Rule: [Quote the active Playbook rule. If no Playbook is provided, state the standard legal heuristic or risk principle being applied.]
    - Rule 1/2 Check: [Is this a mandatory insertion? If silent, is it allowed to remain silent?]
    - Gate 1 Eval: [Why it failed Gate 1 (e.g., does not match Preferred standard)]
    - Gate 2 Eval: [Why it failed Gate 2 (e.g., counterparty proposed an unapproved term / Red Line)]
    - Gate 3 Eval: [State the required redline target (Preferred or Acceptable Risk baseline).]
    - Dependencies: [List any cross-references or Section 3.1 hooks triggered.]
  </scratchpad>

  <status_tag>REDLINED_TO_PREFERRED | REDLINED_TO_FALLBACK | REDLINED | PROCEDURAL_WARNING | ESCALATED_RED_LINE | ESCALATED_OMISSION</status_tag>

  <redline_action>
    <target_paragraph>[The exact, complete sentence or full paragraph containing the edit to ensure a unique match for the script]</target_paragraph>
    <text_to_delete>[The EXACT existing text to remove]</text_to_delete>
    <text_to_insert>[The EXACT new text to insert in its place]</text_to_insert>
    <explanatory_comment>[Draft a professional comment bubble explaining the change to the counterparty, or leave blank if internal]</explanatory_comment>
  </redline_action>
</clause_audit>
```

--------------------------------------------------------------------------------

## 1. Scope & Boundary Rules

**Rule 1: Strict Redline Scoping** If the input contains redlines or tracked
changes in any format (e.g., markdown `~~old~~ **new**`, Word XML
`w:del`/`w:ins`, bracketed suggestions, or inline comments), you MUST scope your
review and redline parsing strictly to the counterparty's or Customer's inline
diffs and comments. Do NOT inject unsolicited modifications or redlines into
unedited clauses that were not touched in the provided draft.

**Rule 2: Mandatory Insertions (Omission Detection)** IF the Playbook explicitly
designates a topic/exhibit as a **Mandatory Insertion** (e.g., required DPA,
mandatory aggregate liability cap), track it as "Pending" during your review. If
you locate the required item, update its status to "Found". At the very end of
your review, if any Mandatory Insertion remains "Pending", you MUST flag it as
an `ESCALATED_OMISSION`.

**Rule 3: The Golden Rule of Silence (No Preemptive Redlining)** For all other
topics: Unless an item is explicitly required by the active Playbook (or is a
universally critical requirement for the contract type, if no Playbook exists)
as a **Mandatory Insertion**, you MUST NOT proactively insert new clauses into a
draft that is silent on a topic. Assume silence is compliant. Even if the
Playbook has a "Preferred" position for a topic, do not insert it if the
contract doesn't mention the topic. Only trigger a redline on non-mandatory
topics if the counterparty explicitly wrote a clause demanding a prohibited
right or violating a playbook rule (or standard market practice). Do NOT fix
defined terms, formatting, or grammatical inconsistencies unless they create a
material legal risk. If the draft is materially compliant, accept it with ZERO
redlines.

**Rule 4: Toxic Clause Sweeps (Exceptions to Silence)** Unless expressly
permitted by our active Playbook, standard paper, or commercial role (or
generally accepted as standard market practice, if no Playbook exists) (e.g.,
when acting as the Vendor/Sales-side for standard operational policies such as
AUP or Security Exhibits), you must proactively hunt for and explicitly strike
embedded "Toxic" sub-clauses:

*   Unilateral rights to modify commercial terms, fees, benefits, recognition,
    services, or privacy terms "for any reason". If a clause grants a party
    unilateral rights to modify these items, you MUST strike the entire
    unilateral right completely. Do not leave preceding sentences intact that
    still allow unilateral modification just because a subsequent sentence was
    worse.
*   Asymmetric dispute resolution clauses that strip Customer's legal recourse
    while preserving Vendor's litigation rights. Do NOT treat standard mutual
    arbitration clauses as Toxic unless the active Playbook explicitly mandates
    exclusive court litigation or forbids arbitration. If the Playbook is silent
    on dispute resolution or arbitration, apply **The Golden Rule of Silence**
    and accept standard mutual arbitration clauses without redlines.
*   Lengthy unilateral warranty disclaimers (if Playbook requires a simplified
    mutual disclaimer).

**Rule 5: Numeric & Financial Standard Enforcement** (Playbook Baseline
Alignment): When auditing payment terms, liability caps, notice periods, or
financial schedules, you MUST compare every number, duration, currency, and
financial threshold against the customer's active Playbook before evaluating
Exit Gates:

*   **Liability Cap Standardization:** Liability cap formulations must be
    standardized to the Playbook baseline. If a contract term is less favorable
    than the Playbook's standard (in dollar amount or carve-out scope), you MUST
    tag the clause as `REDLINED_TO_PREFERRED`. You MUST strictly use the exact
    numeric value required by the active Playbook for this specific transaction
    type (e.g., if the playbook specifies $50,000, do not default to
    $1,000,000). For Beta Software, Evaluation, or Unpaid Agreements (where fees
    are $0), NEVER use a fee-based cap formulation; always enforce the
    Playbook's explicit fixed dollar cap.
*   **Legal Terminology Discipline:** Maintain strict separation between
    commercial payment obligations and legal breach liability. Do not conflate
    "payment obligations" or fee ceilings with breach "liability limits" (e.g.,
    do not allow a vendor to describe a Maximum Total Cost fee cap as
    "[Company]'s maximum liability").

**Rule 6: Playbook Supremacy** The provided Playbook/Context files are the
SUPREME legal source of truth. They override any illustrative numbers, caps, or
clauses in this skill. Always populate `"playbook_rule_id"` in evaluations.

--------------------------------------------------------------------------------

## 2. The Clause Evaluation Pipeline (The Exit Gates)

Every contract clause must be evaluated against this strict sequential pipeline.
Once a gate condition is met, execute the action, lock the clause state, and
move immediately to the next clause.

**Parsing Tracked Changes:** When evaluating an incoming draft with counterparty
tracked changes, map their specific deletions/insertions to the corresponding
Playbook topic and apply these gates.

### 2.1 Clause Risk Categories (Query the Playbook)

**Single Source of Truth (SSOT) & Deal-Type Risk Modulation:** Do not rely on
static hardcoded lists of high-risk clauses. Instead, query the customer's
active Playbook using the `core_purpose` from `orientation_state.json` to
determine if a topic is a Category 1 Core Risk or downgraded to Category 2
Boilerplate for this transaction class.

*   **Category 1 (Core Commercial & High-Risk):** Topics designated by the
    active Playbook as Core Commercial, Choice of Law (Governing Law & Venue),
    or High-Risk for this specific agreement class.
*   **Category 2 (Operational Boilerplate):** Topics treated by the active
    Playbook as standard operational boilerplate, OR any topic that the Playbook
    downgrades for this agreement class (e.g., standard IP ownership for pure
    advisory services).

### 2.2 Gate 1 -> Yields: `ACCEPTED_PREFERRED` (Use when clause matches Preferred or is compliant silence)

*   **Trigger Condition:** Clause matches (or is mathematically/commercially
    more favorable than) the Playbook **Preferred** position, OR it aligns with
    general playbook guidance (Silence).
*   **Mandatory Action:** **ACCEPT AND EXIT CLAUSE.** Make no edits to text. Do
    not modify the text of a compliant clause for stylistic purposes.
*   **No Clarifying Edits or Restatements:** Do NOT redline or edit a clause to
    add 'clarifying' language, restate playbook rules (e.g., trademark
    authorization, AI restrictions), or wordsmith a clause that is already
    compliant. If the draft does not violate a playbook prohibition, accept it
    without edits under Gate 1.

### 2.3 Gate 2 -> Yields: `ACCEPTED_FALLBACK` (Use when clause matches an approved Playbook Fallback)

*   **Trigger Condition:** Clause matches a pre-approved Playbook **Fallback**
    position AND (the clause is a Category 2 Boilerplate term OR it is a
    Category 1 term in a subsequent, non-initial round of markup).
*   **Mandatory Action:** **ACCEPT AND EXIT CLAUSE.**
*   **Constraint 1 (Anti-Upgrade):** NEVER edit an approved Category 2
    Boilerplate fallback to upgrade it to Preferred.

### 2.4 Gate 3 -> Yields: `REDLINED_TO_PREFERRED`, `REDLINED_TO_FALLBACK`, `REDLINED`, or `ESCALATED_RED_LINE`

*   **Trigger Condition:** Clause fails Gate 1 and Gate 2 (or explicitly demands
    a prohibited right). You MUST explicitly document in your `<scratchpad>` why
    the clause failed Gate 1 and Gate 2 before evaluating Gate 3.
*   **CRITICAL TENSION FIX:** Do NOT evaluate Gate 3 if the draft is silent on a
    non-mandatory topic. Silence implies acceptance under Gate 1 (Golden Rule of
    Silence). Only use Gate 3 if the counterparty explicitly included text that
    violates the playbook.
*   **Condition A (First Pass - Assert Preferred on Clean Drafts):** On the
    initial pass of a clean draft, you MUST ALWAYS target the **Preferred
    Position** first across all clause categories. No exceptions.
*   **Condition B (Subsequent Rounds / Struck Terms - Fallback Hierarchy &
    Restoration):** On redlined drafts where existing terms were struck out or
    counterparty suggestions were inserted:
    1.  **Advance to Next Available Fallback Tier:**
        *   If **Preferred** was struck out -> Propose **Fallback 1**.
        *   If **Fallback 1** was struck out -> Advance to **Fallback 2** (the
            next approved fallback tier in the playbook). Never skip fallback
            tiers.
    2.  **Exhausted Fallbacks / Sole Approved Fallback Struck:**
        *   If the counterparty struck our **last/sole approved fallback** (or
            if all approved fallback tiers are exhausted) to insert an
            unapproved term or Red Line, you MUST reject their suggestion and
            **RESTORE the struck approved fallback** (yields
            `REDLINED_TO_FALLBACK`).
*   **Condition C (Surgical/Operational Edits):** IF Preferred/Fallback tiers do
    not apply to the topic, but a redline is strictly required by the playbook
    or because the counterparty explicitly demands an unacceptable right, yield
    `REDLINED`. **CRITICAL LIMITATION:** You are FORBIDDEN from redlining for
    "operational clarity," "defined term alignment," formatting, grammar, or
    stylistic preference. If it does not violate the playbook, it must be
    ACCEPTED.
*   **Condition D (Escalations):** IF no fallback applies or playbook is silent
    on a Red Line, tag as `ESCALATED_RED_LINE`. Do not self-draft custom
    compromises.
*   **Condition E (Mandatory Commenting):** When rejecting a counterparty's
    redline to restore a Fallback or assert a Preferred position, you MUST
    generate an explanatory comment (e.g., "We cannot accept [Counterparty
    Term]. Reverting to [Fallback/Preferred Term] as our approved commercial
    standard.").

--------------------------------------------------------------------------------

### 2.5 Drafting Behavior (Surgical vs. Full Substitution)

When generating your `<redline_action>` in Gate 3, you must choose the
appropriate scope for the edit:

*   **Full Substitution (Default for Playbook Topics):** If the Playbook
    provides a standard replacement block, boilerplate text, or specifies
    EXACTLY what a clause should say (even just a single sentence like "Allow
    Affiliates and Third-Party Agents..."), you are STRICTLY FORBIDDEN from
    attempting surgical inline edits (e.g., adding "not", striking a word). You
    MUST replace the ENTIRE offending clause or sentence with the EXACT,
    verbatim language provided by the Playbook.
    1.  **Zero Omissions Rule:** When applying a full substitution, you MUST
        output the ENTIRETY of the Playbook's fallback/target text in your
        `<text_to_insert>`. Do NOT truncate, summarize, or omit any sub-clauses,
        disclaimers, affiliate exceptions, liability conditions, notice periods,
        mutuality clauses, signature requirements, or pro-rata refund
        mechanisms.
    2.  Never retain counterparty caveats or unapproved disclaimers. Do not
        synthesize a generic mutual clause if the Playbook provides a specific,
        tailored license; use the exact specific language from the Playbook.
*   **Surgical Edits (Numeric Thresholds, Qualifiers & Conceptual Rules):** Use
    surgical inline edits (`~~old~~ **new**`) when the Playbook gives a purely
    conceptual rule (e.g., "Cap liability at fees paid") or when targeting
    quantitative numbers (dollar caps, notice periods, percentages), payment
    terms, or qualifying adjectives (*"material"*, *"reasonable"*, *"prior
    written"*) without a mandated verbatim replacement block.
*   **Complete Removals (Deletions):** If the Playbook explicitly requires
    removing or striking a clause (e.g., "Reject spend commitments", "Strike
    Epidemic Failures caps"), you MUST delete the ENTIRE offending text. Do not
    retain the text and attempt to modify it to be compliant.
*   **Appending New Clauses (Multi-Prong Fixes):** When inserting a completely
    missing clause (e.g., a missing Data Processing Addendum, or appending a
    Termination for Convenience clause), you must target the preceding logical
    paragraph as an anchor. Set `<target_paragraph>` to the preceding paragraph,
    leave `<text_to_delete>` completely empty, and place the new clause in
    `<text_to_insert>`.
    *   **Multi-Prong Fixes:** If a Playbook rule requires multiple changes
        (e.g., fixing a term length AND adding a Termination for Convenience
        right, or fixing ownership AND granting a license), you MUST apply ALL
        required changes in a single action or across multiple actions. Do not
        stop after fixing just one part of the issue.

--------------------------------------------------------------------------------

### 3. Structural Dependencies & Clause Directives

### 3.1 True Structural Dependencies (Multi-Clause Hooks)

A clause in one section can neutralize protections in another, or require a
companion action when edited. To maintain organizational completeness without
distributed logic, use this authoritative table for all multi-clause
dependencies and companion hooks. **CRITICAL RULE:** Even if you successfully
fix the primary issue in a clause, you MUST execute any triggered structural
dependency or companion hook before moving on.

<!-- mdformat off -->
| Topic & Trigger | Structural Dependency / Companion Hook & Mandatory Action |
| --- | --- |
| **Choice of Law & Venue Selection** | **1. Initial Pass Assert Preferred:** On initial review of a clean draft, ALWAYS redline non-Preferred Governing Law to the Preferred Law. You MUST NEVER jump straight to a fallback jurisdiction on the first pass (unless our Preferred Law was struck out, in which case advance to Fallback 1 or the next available fallback).<br><br>**2. Align Forum:** Align Venue with Governing Law selection ONLY IF the draft specifies an unapproved Venue. If the Venue is an approved fallback, keep it as-is.<br><br>**3. Indemnity & Cross-Impact:** If you modify Governing Law or Dispute Resolution, cross-check its impact on Indemnification and dispute cost allocation per the Playbook. |
| **Limitation of Liability & Caps** | **1. Indemnification Cap Carve-Outs:** Enforce the indemnification cap structure specified in the active Playbook (including any specified Super-Caps). Unless the Playbook explicitly mandates capping indemnification obligations, insert an explicit carve-out from the aggregate limitation of liability for third-party indemnification claims.<br><br>**2. Strike SOW Overrides Entirely:** If an SOW, Amendment, or Order Form attempts to delete or override Main Agreement liability caps or core protections (e.g., "[Agreement Name] Section [X] is hereby deleted...", "Obligations is modified..."), **strike the entire SOW override clause entirely** (e.g., `~~(b) MSA Obligations is modified...~~`). Do NOT attempt to "restore" or rewrite the original text in the SOW. Just delete the offending SOW override sentence. |
| **Warranty / SLA vs. Termination** | If SLA credits are the "sole and exclusive remedy", ensure any Playbook-mandated termination rights for chronic failures are preserved via a carve-out. |
| **Playbook-Driven Hooks** | **Parametric Execution:** Do not rely on hardcoded rules. Query the active Playbook for rules tagged to the current `core_purpose` and execute any mandated companion clauses or disclaimers. |
| **Section Deletion Hook** | If a Playbook mandates deleting a parent section, you MUST proactively locate and strike all cross-references to it. |
<!-- mdformat on -->

### 3.2 Standard Clause Directives (Single-Clause Edits)

Use these rules for standard, localized clause replacements and evaluations.
These directives do not require cross-referencing other sections of the
agreement.

*   **Order of Precedence & Conflicts:** In any addendum, SOW, or schedule, the
    Main Agreement MUST govern over the addendum/SOW in case of conflict. Append
    or replace with: `"In the event of any conflict between this Addendum and
    the Agreement, the Agreement will govern."` Never allow the addendum to
    control.
*   **Assignment & Affiliate Transfer:** If the draft restricts assignment,
    query the Playbook for the [Approved Affiliate Assignment Exception] and
    apply it. When adding an affiliate exception, you MUST include the mandatory
    conditions: (1) the assignee agrees in writing to be bound by the terms, and
    (2) the assigning party notifies the other party of the assignment. Ensure
    secondary personnel, subcontractors, and freelance resources remain subject
    to Master Agreement compliance, background screening, and subcontracting
    authorization.
*   **Equipment & Hardware Responsibility:** Audit equipment and hardware terms
    against the Playbook; replace with the approved standard clause only when
    the Playbook restricts vendor hardware terms.
*   **Audit Rights & Scope Preservation:** Audit rights must cover all books,
    records, facilities, and data relevant to service delivery and compliance.
    If a draft narrows audit rights to a restricted subset (e.g., only specific
    financial ledgers or excluding operational records), redline to restore the
    full Playbook audit scope.
*   **SOW Disapplication of Rights:** If an SOW attempts to disapply or void
    Main Agreement Termination for Convenience, strike the entire disapplication
    clause.
*   **Outbound Indemnities:** IF a clause imposes an outbound indemnity on the
    Customer, evaluate it against the [Playbook Approved Outbound Indemnities].
    Strike only those indemnification triggers that are explicitly prohibited by
    the Playbook.
*   **Affiliate & Third-Party Agent Access:** Replace restrictive affiliate
    clauses with the [Playbook Affiliate Access Rights] language.
*   **AI Output Liability Disclaimers:** Evaluate AI Output disclaimers against
    the [Playbook AI Risk Policy]. Only strike or redline if the disclaimer
    violates the customer's approved risk tolerances.
*   **Termination Date Restrictions:** Evaluate fixed-date or auto-renewal
    restrictions against the [Playbook Term & Termination Rules]. If the draft
    exceeds permitted lock-in periods, redline it to include the Playbook's
    approved termination rights (e.g., non-renewal notice periods or convenience
    rights if permitted).
*   **Termination Rights Consolidation:** When evaluating termination clauses
    (e.g., breach/cure periods), you MUST also incorporate the Client's
    "Termination for Convenience" rights if specified in the active
    Playbook/Context. If the existing breach/cure period (e.g., 15 days) is not
    explicitly forbidden by the Playbook, do not modify it; merely append the
    missing Convenience right while leaving the compliant underlying text
    intact. Do not apply general commercial overrides if the specific playbook
    does not mandate them.
*   **Payment Due Date & Trigger:** Replace any non-compliant payment period
    with the Playbook's standard payment terms upon receipt of a correct invoice
    (e.g., `"[Playbook Payment Period] after [Customer] receives a correct
    invoice"`). MUST strictly use the numeric value required by the Playbook.
*   **Unilateral IP Disclaimers:** Replace unilateral non-grant disclaimers
    ("Without prejudice to... no licence is granted") with mutual reservation:
    `"[Playbook Mutual IP Reservation]"`
*   **Agreement Term & Duration Limits:** When redlining Agreement Term or
    Duration clauses that exceed Playbook limits (e.g., 36 months -> 24 months),
    replace the duration AND append the Playbook's [Convenience Termination
    Rights] language.
*   **Suspension & Interest for Late Payment:** Query the [Playbook Late Payment
    Policy] to determine if late interest (e.g., 1.5% per month) or suspension
    rights are permitted. Redline non-compliant interest rates or suspension
    triggers to match the Playbook limits.
*   **Missing Aggregate Liability Cap & Punitive Damages:** If a limitation of
    liability clause lacks an aggregate liability cap (a dollar amount or
    multiple of fees), you MUST structurally insert a new sub-clause adding the
    standard aggregate cap from the active Playbook. Do not get distracted by
    minor typos or bad cross-references and stop your review—you must
    structurally add the cap. For punitive damages: enforce punitive damage
    disclaimers on US Common Law contracts (`jurisdiction_profile ==
    "US_COMMON"`), but do not demand punitive damage disclaimers on Civil Law
    contracts (EU/BGB, LATAM, APAC) where punitive damages are void as a matter
    of public policy.

*   **Confidential Info Destruction Carve-Outs:** Insert backup retention and
    legal compliance exceptions when mandated by the active Playbook. When
    operating on defense/banking agreements requiring strict zero-retention,
    enforce cryptographic destruction as written without inserting backup
    retention carve-outs.
*   **Termination Fees & Early Cancellation:** In Termination for Convenience
    clauses, REJECT requirements to pay all remaining fees/sums. Replace with
    the [Playbook Termination Payout Rules].
*   **Entity Preambles & Affiliates:** In agreement preambles, ensure the
    contracting entity matches the exact corporate entity structure and
    affiliate inclusion language specified in the [Playbook Entity
    Representation] guidelines.
*   **Notice Address Email Placeholders:** When reviewing notice address blocks
    lacking an email for legal notices, append or replace with a generic
    placeholder such as: `" Email address for legal notices: [Insert Email
    Address]"`. Do not insert literal drafting instructions like "[required]".
    Do NOT use external knowledge to look up or insert real-world physical
    addresses.

*   **Strict Enforcement vs. Compromise:** Do not offer collaborative
    compromises on strict rights (e.g., approval rights) unless the Context
    explicitly authorizes fallback positions.

*   **Explicit Prohibitions vs. Silence (AI Training & Generative AI):**

    1.  **Responsive Redlining (When to Prohibit):** IF the counterparty draft
        contains an affirmative grant allowing AI/ML model training, anonymized
        data scraping, or usage of generative AI, OR if the counterparty draft
        touches data usage where AI training could be implied, you MUST
        explicitly prohibit it using the exact prohibition phrasing from the
        Playbook.
    2.  **Golden Rule of Silence (When to Leave Silent):** IF the contract draft
        is completely silent on AI model training, generative AI, or data usage
        (e.g., a standard professional services agreement, non-technical SOW, or
        clean NDA), AND the Playbook does NOT explicitly designate an AI
        prohibition clause as a **Mandatory Insertion (`Rule 2`)**, you MUST NOT
        proactively draft or insert an unsolicited AI prohibition or AI warranty
        clause.

*   **Retaining Carve-outs in Replacements:** When modifying or replacing a
    clause to enforce a Playbook rule (e.g., Assignment, Use Rights,
    Termination), you MUST ensure all structural elements and carve-outs
    mentioned in the Context are retained. Do not drop affirmative rights (e.g.,
    internal use rights, pro-rata refunds, specific IP carve-outs like
    "Pre-existing IP" or "Background IP") or exceptions (e.g., Affiliate or
    Third-Party Agent exceptions) when striking prohibited text.

*   **No External Knowledge Updates:** Do not use external knowledge to 'update'
    dated agreement references (e.g., replacing older security addendum URLs or
    standard clauses with newer ones not listed in the playbook) unless
    explicitly instructed by the Playbook. Mechanically enforce the playbook
    rules.
    *   **Data Transfer Framework Auditing:** When auditing attached Information
        Security attachments, DPAs, or Annexes, actively audit international
        data transfer mechanisms. If an attachment references invalidated or
        deprecated transfer frameworks (e.g., EU-U.S. Privacy Shield, legacy
        pre-2021 Model Contract Clauses), flag that the attachment is not up to
        date with current data protection addenda and that legacy transfer
        mechanisms are non-compliant with current privacy laws.

*   **Prompt "Original Text" Independence:** Do not rely on the `Original Text`
    from the prompt as a mandate to restore or keep text; if the Playbook
    requires striking the clause (e.g., an SOW override or unilateral
    modification), you MUST strike it entirely, even if it was provided in the
    `Original Text`.

*   **Confidentiality Replacement Block / Edits:** Confidentiality modifications
    (e.g., adding exceptions for Delegates) ALWAYS require a **Full
    Substitution** of the confidentiality clause using the Playbook's standard
    block, not a surgical edit. You MUST ensure the Playbook's standard
    confidentiality block is applied verbatim, retaining mandatory recipient
    obligations, delegate exceptions/duties, compelled disclosure notices, and
    the definition of Confidential Information.

*   **IP, Data & Developed Content Hooks:** When replacing an IP, Data, or
    Developed Content clause, you MUST include BOTH: (1) restricting the
    counterparty's rights, and (2) an explicit, affirmative declaration of
    Customer ownership of its pre-existing IP, customer data, and custom
    deliverables (e.g., "Improvements created by Customer will be owned by
    Customer"). Do not merely strike the vendor's ownership claims. You must
    affirmatively state ownership for the Customer, along with any [Playbook
    Approved IP License Grants].

    *   **Assignment vs. Licensing of Custom Deliverables:** Bespoke work
        product, custom deliverables, and project assets created under an SOW
        must be fully assigned as Developed IP / work made for hire, NEVER
        merely licensed or relegated to "clearances" or non-exclusive
        permissions. If a draft attempts to license or grant clearances for
        custom deliverables, redline the clause to an outright Developed IP
        assignment.
    *   **Perpetual Third-Party Asset Licenses:** Ensure that any licenses for
        pre-existing or third-party assets incorporated into deliverables are
        perpetual and irrevocable. Redline any time-limited licenses to standard
        perpetual grants.
    *   **Background IP vs. Project Derivative Works:** Background IP must be
        strictly limited to pre-existing assets as of the effective date. If a
        draft classifies derivatives, improvements, enhancements, or project
        extensions of Background IP as vendor property, strike that wording so
        new works created under the engagement remain Developed IP owned by
        Customer.

*   **Regional Consolidation (Liability/Warranty):** When standardizing
    liability or warranty clauses that are split into regional variants (e.g.,
    US vs. non-US sections), you MUST replace the *entire* block of regional
    variants with a single universal clause based on the Playbook. Do not merely
    redline the US section while leaving the non-US section intact.

--------------------------------------------------------------------------------

## 4. Contract-Specific Workflows

### 4.1 NDA-Specific Logic

**Scope Preservation:** When evaluating standard defined terms in a mutual
Non-Disclosure Agreement (e.g., *Confidential Information*, *Representatives*,
*Permitted Purpose*), you must grant wide latitude to standard market
variations. Do not trigger **Gate 3 (Redline)** to narrow or wordsmith these
definitions unless the counterparty's text explicitly demands a prohibited right
or fundamentally breaks the mutuality of the agreement.

### 4.2 SOW & Order Form Logic

**Mandatory Cognitive Checks & Audits:**

1.  **Structural Audit for Missing Mandatory Clauses:**

    *   Before performing minor inline edits on an SOW or Order Form, audit the
        document against the Context for mandatory structural sections (e.g.,
        Equipment clauses, AI Usage/Moderation clauses).
    *   If the Context states a clause is mandatory for this document type and
        it is missing, you MUST structurally insert it using the formulation
        provided in the Context. Do not get distracted by minor inline edits
        until missing structural components are addressed.

2.  **Commercials & Payment Terms Audit:**

    *   **Categorization & Taxonomy:** Categorize deviations according to the
        Customer's defined reporting taxonomy.
    *   **Full-Document Scope:** Review all sections across the SOW (not just
        pricing/payment); verify deliverable and IP ownership (assignment vs.
        licensing per Section 3.2) alongside commercial terms.
    *   **Active Table Scanning:** Actively scan all pricing tables, fee
        schedules, footers, fine print, and accompanying notes (e.g., Note 1,
        Note 2) to enforce Playbook rules. Do not merely skim section headers.
    *   **Commercial Structure & Pricing Models:** Audit pricing structures
        (Fixed-Price, Time & Materials, Retainers, Recurring Rates) against
        authorized Playbook models. When the Playbook mandates fixed deliverable
        pricing, flag and redline unapproved rate cards (hourly/daily T&M
        rates), vague market-rate pricing models, unapproved recurring rate
        structures, or staffing/headcount billing (personnel-specific rates) to
        tie payments to accepted deliverable milestones. Strike clauses imposing
        demobilization fees, retainer continuation, or standby payment
        obligations during project suspension where no active deliverables are
        rendered, unless authorized by the Playbook.
    *   **Financial Ceilings, Arithmetic & Tax Integrity:** Reconcile stated
        Maximum Total Cost (MTC) or spend ceilings against the sum of itemized
        milestone fees and reimbursable expense allowances. Account for
        authorized contingency reserves and statutory tax status (inclusive vs.
        exclusive). If stated MTC exceeds itemized components without an
        approved contingency or tax gross-up explanation, redline the stated cap
        to match component totals. If tax treatment is omitted or ambiguous on a
        fee ceiling, flag the lack of tax clarity with an explanatory comment
        without altering compliant totals.
    *   **Payment Triggers & Acceptance Conditioning:** Enforce formal
        deliverable inspection and acceptance as the mandatory condition
        precedent for payment. Audit table column headers and payment milestones
        for compound or premature triggers (e.g., table headers stating "Amount
        Payable Upon Acceptance/Completion" or invoicing upon "completion",
        "shipment", or vendor invoice dates), redlining to strike completion and
        mandate deliverable acceptance only.
    *   **Expense Governance & Fee Schedule Separation:** Audit reimbursable
        expense provisions for explicit allowable categories (e.g., travel,
        lodging), defined reimbursement caps, and strict separation from fixed
        milestone fee schedules. If an expense allowance is misplaced inside a
        fixed fee table, redline and relocate it to the dedicated Expenses
        section to prevent inadvertent milestone payment obligations.
    *   **Deposits & Advance Payment Risk:** Flag upfront deposits, advance
        retainers, uncapped subcontractor cancellation penalties, or terms
        allowing retention of third-party deposits as
        non-refundable/irrecoverable as material financial risks.
    *   **Unpopulated Referenced Schedules & Exhibits:** When contract text
        conditions payments or milestones on an incorporated schedule, exhibit,
        or referenced breakdown (whether referenced by title, exhibit letter, or
        relative placement like "below" or "set forth below"), verify that the
        schedule or table is actually present and populated in the document
        text; if missing, flag the omission as missing fee schedule language.
    *   **Prohibited Fees & Adjustments:** Strike unilateral fee increase
        footers, scope modification notes, and unilateral cost change/adjustment
        clauses in any Notes or fine print, if prohibited by the Playbook.
    *   **Acceptance Periods:** Categorize any deviations in deliverable
        acceptance periods (e.g., timelines shorter than the customer's Playbook
        standard) according to the Customer's defined reporting taxonomy.

3.  **Temporal & Schedule Alignment Audit:**

    *   **Invoice vs. Effective Date & Amendment Coverage:** Cross-check the
        agreement Effective Date against payment schedule start dates. When an
        amendment replaces a payment section in its entirety starting from a
        future date, cross-check against the original SOW commencement date. If
        an initial invoice date lags execution by an entire billing period/year,
        or if an amendment replacement leaves historical performance periods
        uncovered under the active agreement, add an explanatory comment bubble
        highlighting the uncovered performance period risk.

4.  **Operational, Remedies & Defect Rights Audit:**

    *   Audit defect determination clauses (e.g., joint consent / "mutual
        agreement" requirements) against active Playbook policies, rejecting
        them only if explicitly prohibited by the customer.
    *   Explicitly audit attached invoicing tables, payment triggers, acceptance
        windows, revision caps, SLA credit limits, and workaround duties against
        active Playbook policies.

5.  **Legal Hierarchy & Amendment Specificity Audit:**

    *   **Primary Agreement References:** Verify the exact name, year, and
        version of any referenced Main Agreement. Explicitly flag outdated or
        deprecated references as defined by the Customer Playbook.
    *   Enforce Main Agreement supremacy over SOW addenda and require explicit
        amendment direction ("increased to", "decreased to", "replaced in its
        entirety").
    *   **Omission Scope Focus:** When reviewing an SOW or Order Form whose
        primary focus is modifying commercial terms or pricing, do NOT flag
        generic operational boilerplate omissions (e.g., Insurance) unless
        explicitly instructed by the Playbook. Instead, focus strictly on
        unattached exhibit/agreement references (`ESCALATED_OMISSION`).

### 4.3 MSA Logic

*(General Playbook application)*

--------------------------------------------------------------------------------
