# Data Dictionary — SaaS Analytics Dataset

This document describes all five tables in the dataset, their columns, data types, and business definitions.

---

## Table of Contents

1. [account](#1-account)
2. [subscription](#2-subscription)
3. [feature_usage](#3-feature_usage)
4. [support_ticket](#4-support_ticket)
5. [churn_event](#5-churn_event)

---

## 1. account

One row per customer account. This is the central entity that all other tables link back to.

| Column | Type | Description |
|---|---|---|
| `account_id` | ID | Primary key. Unique identifier for each customer account. |
| `account_name` | String | Fictional company name associated with the account. |
| `industry` | Categorical | SaaS vertical the account belongs to (e.g., DevTools, EdTech). |
| `country` | String | Country of the account, stored as an ISO 3166-1 alpha-2 code (e.g., `US`, `DE`). |
| `signup_date` | Date | Date the account was created. |
| `referral_source` | Categorical | Channel through which the account was acquired. Values: `organic`, `ads`, `event`, `partner`, `other`. |
| `plan_tier` | Categorical | Plan the account signed up on initially. Values: `Basic`, `Pro`, `Enterprise`. |
| `seats` | Integer | Number of licensed user seats at the account level. |
| `is_trial` | Boolean | Indicates whether the account is currently on a free trial (`TRUE`) or not (`FALSE`). |
| `churn_flag` | Boolean | Indicates whether the account has churned at any point (`TRUE`) or is still active (`FALSE`). |

---

## 2. subscription

One row per subscription record. An account can have multiple subscriptions over time (e.g., after a plan change or reactivation).

| Column | Type | Description |
|---|---|---|
| `subscription_id` | ID | Primary key. Unique identifier for each subscription record. |
| `account_id` | ID (FK) | Foreign key referencing `account.account_id`. |
| `start_date` | Date | Date the subscription became active. |
| `end_date` | Date | Date the subscription ended. `NULL` for currently active subscriptions. |
| `plan_tier` | Categorical | Plan tier at the time of billing. Values: `Basic`, `Pro`, `Enterprise`. |
| `seats` | Integer | Number of licensed seats under this subscription. |
| `mrr_amount` | Currency (USD) | Monthly Recurring Revenue for this subscription. |
| `arr_amount` | Currency (USD) | Annual Recurring Revenue for this subscription. Typically `mrr_amount × 12`. |
| `is_trial` | Boolean | Indicates whether this subscription is a free trial (`TRUE`) or a paid plan (`FALSE`). |
| `upgrade_flag` | Boolean | Indicates whether the account upgraded to a higher plan mid-cycle (`TRUE`). |
| `downgrade_flag` | Boolean | Indicates whether the account downgraded to a lower plan mid-cycle (`TRUE`). |
| `churn_flag` | Boolean | Indicates whether this subscription ended due to churn (`TRUE`). |
| `billing_frequency` | Categorical | How often the subscription is billed. Values: `monthly`, `annual`. |
| `auto_renew_flag` | Boolean | Indicates whether the subscription is set to renew automatically. Approximately 80% of records are `TRUE`. |

---

## 3. feature_usage

One row per usage event. Tracks how accounts interact with individual product features over time.

| Column | Type | Description |
|---|---|---|
| `usage_id` | ID | Unique identifier per usage event. Not a primary key — serves as a unique identifier only, not a guaranteed surrogate key. |
| `subscription_id` | ID (FK) | Foreign key referencing `subscription.subscription_id`. |
| `usage_date` | Date | Date on which the usage event occurred. |
| `feature_name` | Categorical | Name of the feature used. Drawn from a pool of 40 distinct SaaS features. |
| `usage_count` | Integer | Number of times the feature was triggered during this event. |
| `usage_duration_secs` | Integer | Total time spent on the feature during this event, in seconds. |
| `error_count` | Integer | Number of errors logged during this usage event. |
| `is_beta_feature` | Boolean | Indicates whether the feature is in beta (`TRUE`). Approximately 10% of records are flagged as beta. |

---

## 4. support_ticket

One row per support ticket. Captures customer service interactions at the account level.

| Column | Type | Description |
|---|---|---|
| `ticket_id` | ID | Primary key. Unique identifier for each support ticket. |
| `account_id` | ID (FK) | Foreign key referencing `account.account_id`. |
| `submitted_at` | Datetime | Timestamp when the ticket was opened by the customer. |
| `closed_at` | Datetime | Timestamp when the ticket was resolved and closed. |
| `resolution_time_hours` | Float | Total time from submission to closure, in hours. |
| `priority` | Categorical | Ticket priority level assigned at submission. Values: `low`, `medium`, `high`, `urgent`. |
| `first_response_time_minutes` | Integer | Number of minutes between ticket submission and the first support response. |
| `satisfaction_score` | Integer | Customer satisfaction rating submitted after ticket closure. Scale: 1 (lowest) to 5 (highest). `NULL` if the customer did not respond. |
| `escalation_flag` | Boolean | Indicates whether the ticket was escalated to a higher support tier (`TRUE`). |

---

## 5. churn_event

One row per churn instance. Records the details of each account departure, including reason and any associated refund.

| Column | Type | Description |
|---|---|---|
| `churn_event_id` | ID | Primary key. Unique identifier for each churn event. |
| `account_id` | ID (FK) | Foreign key referencing `account.account_id`. |
| `churn_date` | Date | Date on which the account officially churned. |
| `reason_code` | Categorical | Primary reason given for churning (e.g., `pricing`, `support`, `features`). |
| `refund_amount_usd` | Currency (USD) | Refund or credit amount issued at churn. Defaults to `$0`; approximately 25% of records carry a non-zero value. |
| `preceding_upgrade_flag` | Boolean | Indicates whether the account had a plan upgrade within the 90 days before churning (`TRUE`). |
| `preceding_downgrade_flag` | Boolean | Indicates whether the account had a plan downgrade within the 90 days before churning (`TRUE`). |
| `is_reactivation` | Boolean | Indicates whether the churning account had previously churned and reactivated (`TRUE`). Approximately 10% of churn events are reactivations. |
| `feedback_text` | String | Optional free-text comment submitted by the customer at churn. May be `NULL`. |

---

*Last updated: June 15, 2026*
