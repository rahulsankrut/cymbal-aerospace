# Contract Clause Schema (Simplified for Classification)

Use this schema definition to map raw text differences (redlines) to the
corresponding contract clauses and attributes.

--------------------------------------------------------------------------------

## 1. Clauses (`clauses`)

This section defines specific legal and operational clauses in the contract.

### `shortfall_rollover_terms`

*   **Description**: Terms allowing the customer to roll over a percentage of an
    unmet minimum commitment shortfall to the subsequent commitment period.

*   **Key Properties**:

    *   `allowed` (boolean): Whether shortfall rollover is permitted.
    *   `cap_percentage` (number): The maximum percentage of shortfall that can
        be rolled over.
    *   `rollover_period` (duration): The period into which the shortfall is
        rolled (e.g., 'subsequent Commitment Period').

### `excess_rollover_terms`

*   **Description**: Terms allowing the customer's spend that exceeds the
    minimum commitment in one period to count toward shortfalls in subsequent
    periods.

*   **Key Properties**:

    *   `allowed` (boolean): Whether excess rollover is permitted.
    *   `cap_percentage` (number): Cap on excess rollover (usually 100%).

### `pricing_conditions`

*   **Description**: Special conditions regarding pricing.
*   **Key Properties**:
    *   `sustained_use_discounts_excluded` (boolean): Whether Sustained Use
        Discounts (SUDs) are excluded.
    *   `list_price_as_ceiling` (boolean): Customer pays the lower of the fixed
        price or the then-current list price.
    *   `marketplace_cap_percentage` (number): Cap on marketplace spend counting
        toward commitment.

### `renewal_terms`

*   **Description**: Terms governing contract renewal.
*   **Key Properties**:
    *   `reversion_to_list_price` (boolean): Whether prices revert to standard
        list prices upon renewal.

### `currency_terms`

*   **Description**: Terms governing currency and billing.
*   **Key Properties**:
    *   `billing_currency` (string): The currency used for billing (e.g., USD,
        EUR).

### `termination_and_cancellation`

*   **Description**: Terms regarding contract termination, cancellation fees,
    and notice periods.
*   **Key Properties**:
    *   `termination_rights_allowed` (boolean): Whether customer has rights to
        terminate for convenience.
    *   `termination_penalty_exists` (boolean): Whether a cancellation fee or
        penalty exists.
    *   `cancellation_fee_percentage` (number): Percentage of unsatisfied
        commitment charged as penalty.
    *   `cancellation_fee_amount` (money): Flat fee charged for cancellation.
    *   `termination_notice_period_days` (integer): Advance notice required for
        termination.

### `affiliate_terms`

*   **Description**: Terms regarding affiliate participation.
*   **Key Properties**:
    *   `participation_enabled` (boolean): Whether approved customer affiliates
        can receive discounts or count toward commitments.

### `force_majeure_terms`

*   **Description**: Terms regarding extraordinary events beyond control.
*   **Key Properties**:
    *   `present` (boolean): Whether a Force Majeure clause is present.

### `free_service_provision`

*   **Description**: Provisions for free services or support.
*   **Key Properties**:
    *   `present` (boolean): Whether free services/support are provided.
    *   `description` (string): Description of the free services.

### `price_protection_terms`

*   **Description**: Terms protecting the customer from price increases.
*   **Key Properties**:
    *   `duration` (duration): Period during which prices are protected.

### `survival_of_obligation`

*   **Description**: Terms that survive contract expiration or termination.
*   **Key Properties**:
    *   `present` (boolean): Whether obligations survive.
    *   `survival_duration` (duration): How long they survive.

### `credit_conversion_terms`

*   **Description**: Terms allowing conversion of funds (e.g., PSF to GCP
    Service Credits).
*   **Key Properties**:
    *   `from_psf_allowed` (boolean): Whether conversion is allowed.
    *   `max_conversion_amount` (money): Maximum amount allowed for conversion.

--------------------------------------------------------------------------------

## 2. Credits and Funds (`credits_and_funds`)

This section defines credits, funds, and milestones.

*   **Description**: Service credits, learning funds, or other
    promotional/incentive funds.
*   **Key Properties for Mapping**:
    *   `name` (string): e.g., "Service Credit 1", "True Up Credits", "Learning
        Fund".
    *   `type` (string): e.g., "Service Credit", "Learning Fund".
    *   `amount` (money or percentage): The value of the credit/fund.
    *   `validity_period` (duration): Duration for which the credit is valid.
    *   `applicable_services` (array of scopes): Which SKUs or services the
        credit can be applied to.

--------------------------------------------------------------------------------

## 3. Discounts (`discounts`)

This section defines negotiated discounts.

*   **Description**: Negotiated percentage discounts, spending-based discounts,
    or fixed rate discounts.
*   **Key Properties for Mapping**:
    *   `type` (string): e.g., `PERCENTAGE_DISCOUNT`, `SPENDING_BASED_DISCOUNT`,
        `FLEX_CUD_DISCOUNT`.
    *   `program_name` (string): e.g., "GCP Custom Discount", "Partner Program".
    *   `service_scope` (array of scopes): The scope of services receiving the
        discount.
    *   `flat_rate_discount` / `spend_based_discount` (object): The specific
        discount percentages and tiers.

--------------------------------------------------------------------------------

## 4. Commitments (`commitments`)

This section defines spending commitments.

*   **Description**: Minimum spending commitments over specific periods.
*   **Key Properties for Mapping**:
    *   `period_name` (string): e.g., "Year 1", "Commitment Period 1".
    *   `duration` (duration): e.g., 12 Months.
    *   `amount` (money): The commitment amount (e.g., USD 1,000,000).
