# Sanitization Rules

Apply these rules strictly when cleaning the document text:

## 1. Remove PII (Personally Identifiable Information)

-   Delete individual names, teams, products, personal or individual email
    addresses, phone numbers, and internal project codenames. (Note: Do NOT
    delete physical office locations or headquarters addresses, as these are
    public information).
-   Replace them with a meaningful placeholder that reflects the generic role or
    category (e.g., `<Generic Role/Team>`, `<Internal Product>`, `<Project
    Name>`).
-   **CRITICAL**: Do NOT remove generic role names (e.g., Lead Counsel,
    Commercial Counsel, VP of Finance). Retain them as they are; only specific
    individuals' names should be replaced.

## 2. Remove Internal Links and Proprietary Systems

Look for patterns of proprietary internal systems across any industry. Delete
and replace the following:

-   **Intranet Domains:** Anything ending in `.corp`, `.local`, `.internal`, or
    accessed via internal IP addresses.
-   **Knowledge Base Namespaces:** URLs or text referencing internal wikis,
    Confluence, SharePoint, Notion, Quip, or internal `g3doc` references.
-   **Custom Shortlinks:** `go/`, `link/`, `goto/`, `aka.ms/`, `sz/`, or similar
    custom company redirects.
-   **Ticketing Systems:** References to internal Jira projects (e.g.,
    `PROJ-123`), ServiceNow portals, or Zendesk instances.
-   **Messaging Channels:** References to internal communication channels (e.g.,
    Slack channels like `#incident-sev1`, Discord, or Google Chat spaces).

**Important Exception (Public vs. Internal URLs):** Do NOT remove links to
widely known, publicly accessible websites (e.g., `wikipedia.org/wiki/...`,
public `github.com` repositories, or public `sec.gov` filings). You can identify
internal websites because they typically use corporate subdomains (e.g.,
`wiki.company.com`), lack a standard TLD (e.g., `http://go/`), or are referenced
in a strictly internal context.

Replace these internal links or tool names with a meaningful generic name. The
placeholder should describe what the system does or points to, wrapped in
brackets without the actual URL (e.g., `[Internal Help Desk]`, `[Internal Policy
Document]`, `[Company Ticketing System]`).

## 3. Grammatical Flow & Structural Normalizer

When automated scripts or agents excise names, links, and sentences, the
resulting document often looks like Swiss cheese (e.g., "If [REDACTED] approves
at [REDACTED], then [REDACTED] applies."). Awkward gaps destroy readability and
look amateurish when presented to outside counsel. You must polish the excised
text to restore pristine grammatical flow.

### Syntactic & Grammatical Normalization Rules

| Syntactic Defect        | Grammatical &           | Sample Before -> After   |
: Pattern (Post-Excision) : Structural              : Transformation           :
:                         : Normalization Mandate   :                          :
| ----------------------- | ----------------------- | ------------------------ |
| Orphaned Prepositions / | Remove dangling         | Submit the form to at    |
: Articles                : prepositions (at, by,   : go/intake -> Submit the  :
:                         : via, to) left behind    : form via the designated  :
:                         : when a name or link was : intake channel           :
:                         : stripped.               :                          :
| Repeated Placeholder    | Merge multiple adjacent | Contact [Legal Counsel]  |
: Tokens                  : [REMOVED] or generic    : at [REMOVED] via         :
:                         : tokens into a single    : [REMOVED] -> Contact the :
:                         : cohesive functional     : designated Legal Counsel :
:                         : clause.                 :                          :
| Disjointed Conditional  | Re-structure            | If counterparty rejects, |
: Transitions             : conditional sentences   : then if deal > $1M       :
:                         : where the THEN clause   : concede to 1x, otherwise :
:                         : was excised during      : escalate. -> If the      :
:                         : strategy filtering.     : counterparty rejects our :
:                         :                         : primary position,        :
:                         :                         : escalate the matter to   :
:                         :                         : Legal Counsel.           :
| Broken Table & List     | Clean up empty table    | Remove empty bullet      |
: Formatting              : rows, dangling bullet   : points (-); re-align     :
:                         : points, or broken       : markdown table pipe      :
:                         : column delimiters       : boundaries (| Header |). :
:                         : caused by text          :                          :
:                         : excisions.              :                          :

### Execution Protocol & Logic

1.  **Syntactic & Paragraph Scan**: Parse every paragraph and table cell in the
    post-excision document string.
2.  **Grammatical Engine**: Run natural language grammar checks (subject-verb
    agreement, transition logic, dangling modifiers) across all modified
    sentences.
3.  **Readability Smoothing**: Rephrase disjointed sentences to ensure
    professional, authoritative tone and smooth transitions.
4.  **Formatting Verification**: Output the grammatically normalized text
    verified for structural cohesion.

## 4. Preserve Legal Meaning

-   Even after removing the contents and replacing it, the whole meaning of the
    playbook must be the same as the original playbook.
-   Do NOT alter core legal instructions, fallback language, or policy
    requirements. The legal substance must remain unchanged.

A legal playbook tells the negotiator what standard terms the company requires,
what fallbacks are acceptable, and when they must escalate. When sanitizing a
playbook, it is critical to preserve the nuances of these elements while
replacing the internal jargon or PII. Here are the core components and how they
should be preserved:

**1. Standard Clauses (The "Ideal" Position)** This is the baseline language the
company prefers to use.

-   *Example (Confidentiality):* "The Receiving Party agrees to hold all
    Confidential Information in strict confidence and to protect it with the
    same degree of care it uses to protect its own confidential information, but
    no less than a reasonable degree of care."
-   *Example (Governing Law):* "This Agreement shall be governed by the laws of
    the State of Delaware, without regard to its conflict of laws principles."

**2. Requirements & Obligations** These are affirmative actions a party MUST
take. The obligation must remain, but internal tools/links might need to be
scrubbed.

-   *Example (Data Security Requirement):* "Vendor must maintain SOC 2 Type II
    compliance at all times and provide an updated report annually."
-   *Example (Notice Requirement):* "In the event of a data breach, the Vendor
    must notify the Company within 48 hours via email to [Insert Generic Legal
    Alias]." (Before sanitization, this might have said notify
    security-incidents@google.com or submit a ticket at go/breach).
-   *Example (Data Retention & Legal Holds):* "All public channel messages are
    retained for 90 days, while private messages are retained for 180 days.
    Legal holds override all deletion policies." (Do NOT alter these specific
    retention periods or legal hold requirements).

**3. Restrictions & Limitations** These dictate what a party CANNOT do. These
are highly sensitive to change.

-   *Example (Assignment):* "Neither party may assign this Agreement without the
    prior written consent of the other party."
-   *Example (Subcontracting):* "Vendor shall not subcontract any of its
    obligations without prior written approval. If approved, Vendor remains
    fully liable for all acts of the subcontractor."

**4. Rights & Permissions** These define what a party is ALLOWED to do under the
contract.

-   *Example (Audit Rights):* "The Company reserves the right, upon 30 days'
    written notice, to audit the Vendor's facilities to ensure compliance with
    data protection obligations."
-   *Example (Termination for Convenience):* "Either party may terminate this
    Agreement for any reason upon ninety (90) days prior written notice."

**5. Penalties & Remedies** These outline the consequences if a requirement or
restriction is violated.

-   *Example (Indemnification):* "Vendor agrees to defend, indemnify, and hold
    harmless the Company against any third-party claims arising from Vendor's
    gross negligence or willful misconduct."
-   *Example (Limitation of Liability Caps):* "Total aggregate liability for
    either party shall not exceed the total amounts paid under this Agreement in
    the twelve (12) months preceding the claim."

**6. Fallback Positions (Negotiation Guidelines)** Playbooks provide "Fallbacks"
if the other party pushes back. Internal strategy must be sanitized but the
negotiation leverage must be preserved. **CRITICAL: You must preserve generic
commercial numerical thresholds (e.g. standard Net 30/45/60 payment terms, 99.x%
SLA guarantees, standard $50,000 threshold, standard 5% renewal caps). Do NOT
scrub these generic commercial values. You MUST scrub highly confidential
internal numbers. This includes internal margin targets (e.g., 30% or 40%
margin) and raw price floors (e.g., $0.05/GB/month, $15,000 minimum deal size).
Do NOT confuse these internal floors with standard commercial thresholds;
internal price floors must ALWAYS be scrubbed.**

-   *Standard Position:* "Payment terms are Net 30." (Retain standard
    positions).
-   *First Fallback:* "If customer rejects standard terms, we can accept
    commercially reasonable extended terms without escalation." (Scrubbed the
    specific "Net 45" fallback).
-   *Second Fallback:* "If customer insists on further extended terms, require a
    standard late fee penalty." (Scrubbed the specific "Net 60" and "2%"
    limits).
-   *Escalation Trigger:* "Any request for payment terms beyond acceptable
    limits MUST be escalated to the [Insert Approver Role] for approval."
    (Scrubbed the specific "Net 60" trigger and specific names).

## 5. Filter Proprietary Strategies & Thresholds

An internal playbook tells negotiators exactly where the organization will bend.
If outside counsel or co-counsel shares this unredacted playbook with the
counterparty, all negotiation leverage is instantly destroyed. You must scrub
internal concession thresholds while retaining external standard positions.

### Proprietary Strategy & Concession Filtering Matrix

| Proprietary      | Internal Playbook | External          | Strategic         |
: Content Vector   : Text (Sensitive   : Sanitized         : Rationale         :
:                  : Concession Logic) : Replacement       :                   :
:                  :                   : (Commercial       :                   :
:                  :                   : Standard)         :                   :
| ---------------- | ----------------- | ----------------- | ----------------- |
| Walk-Away        | "We demand 2x ARR | Sanitized Rule:   | Prevents          |
: Concession       : liability cap. If : "Our standard     : counterparty from :
: Limits           : vendor rejects,   : position requires : bypassing initial :
:                  : we can concede    : a mutual          : 2x demand         :
:                  : down to 1x ARR if : liability cap of  : directly to the   :
:                  : deal value >      : 1x to 2x trailing : 1x floor.         :
:                  : $200k without VP  : annual fees paid, :                   :
:                  : sign-off."        : depending on      :                   :
:                  :                   : transaction scope :                   :
:                  :                   : and risk          :                   :
:                  :                   : profile."         :                   :
| Financial Margin | "Do not allow     | Sanitized Rule:   | Protects          |
: & Fee Limits     : renewal fee       : "Annual fee       : commercial        :
:                  : increases above   : increases upon    : pricing leverage  :
:                  : 5%. If pushed,    : renewal must be   : during renewal    :
:                  : accept up to 8%   : strictly capped   : discussions.      :
:                  : if multi-year     : at the lesser of  :                   :
:                  : prepayment is     : Consumer Price    :                   :
:                  : secured."         : Index (CPI) or    :                   :
:                  :                   : 5.0%."            :                   :
| Approval Bypass  | "If CISO is out   | Sanitized Rule:   | Eliminates        |
: Guidance         : of office,        : "Any deviation    : counterparty      :
:                  : General Counsel   : from standard     : knowledge of      :
:                  : can unilaterally  : Data Processing   : internal          :
:                  : sign off on       : Addendum terms    : administrative    :
:                  : missing DPA if    : requires formal   : workarounds.      :
:                  : deal closes       : written approval  :                   :
:                  : before Q3 end."   : from Corporate    :                   :
:                  :                   : Compliance and    :                   :
:                  :                   : CISO."            :                   :
| Counterparty     | "Acme Cloud has a | Sanitized Rule:   | Removes           |
: Vulnerability    : weak IP indemnity : "All agreements   : vendor-specific   :
: Notes            : in their standard : must contain      : tactical          :
:                  : terms; push hard  : robust, mutual    : commentary and    :
:                  : on Section 5 to   : indemnification   : maintains         :
:                  : force defense     : for third-party   : objective         :
:                  : control."         : intellectual      : neutrality.       :
:                  :                   : property          :                   :
:                  :                   : infringement with :                   :
:                  :                   : defense control   :                   :
:                  :                   : rights."          :                   :
| Licensing Floors | "Target a 40%     | Sanitized Rule:   | Completely        |
: & Margins        : margin on all     : "All software     : removes internal  :
:                  : software licenses : licenses must     : financial targets :
:                  : with a minimum    : meet the standard : and minimum deal  :
:                  : licensing floor   : minimum           : size metrics.     :
:                  : of $47,500."      : commercial margin :                   :
:                  :                   : and volume        :                   :
:                  :                   : requirements."    :                   :

### Execution Protocol & Logic

1.  **Semantic Concession Scanning**: Mine text for conditional concession
    syntax ("if pushed", "we can concede", "concede up to", "concede down to",
    "without approval", "internal only").
2.  **Threshold Isolation**: Isolate numerical floors and ceilings that
    represent confidential walk-away limits, fallback positions, escalation
    triggers, margin targets, or minimum deal sizes rather than stated starting
    positions. **CRITICAL: You MUST preserve generic commercial thresholds (like
    $50,000 SLA penalties, 99.5% availability, 5% renewal caps, Net 30/45/60).
    You MUST completely remove specific highly confidential internal numbers.
    This includes internal margin targets (e.g., 30% or 40% margin) and raw
    price floors (e.g., $0.05/GB/month, $15,000 minimum deal size).**
3.  **Tactical Abstraction**: Replace specific internal concession formulas with
    standardized, commercially reasonable guidance rules.
