# Task 4: Revenue Cohort Analysis by Referral Channel — Required Data

## Purpose
This document lists the data fields required to execute Task 4 (Revenue Cohort Analysis by Referral Channel) and confirms whether each field is available in the RavenStack dataset.

## Required Fields

### From `accounts.csv`
| Field | Purpose in Task 4 | Available? |
|---|---|---|
| `account_id` | Primary key, used to join with `subscriptions` | Yes |
| `signup_date` | Used to define the cohort's signup month | Yes |
| `referral_source` | Used to segment cohorts by acquisition channel | Yes |

### From `subscriptions.csv`
| Field | Purpose in Task 4 | Available? |
|---|---|---|
| `subscription_id` | Unique identifier for each subscription row | Yes |
| `account_id` | Foreign key, used to join with `accounts` | Yes |
| `start_date` | Used to calculate the account's anchor date and each subscription's `period_number` | Yes |
| `mrr_amount` | Used to calculate revenue per cohort, per period, and revenue retention % | Yes |
| `arr_amount` | Used to calculate Total ARR per acquisition channel | Yes |

## Derived Fields (calculated during the task, not in raw data)
| Field | How it's derived |
|---|---|
| `signup_month` | `accounts.signup_date` converted to year-month |
| `anchor_date` | Minimum `start_date` per `account_id` in `subscriptions` |
| `anchor_month` | `anchor_date` converted to year-month |
| `start_month` | `subscriptions.start_date` converted to year-month |
| `period_number` | `start_month` − `anchor_month` (per subscription) |

## Data Availability Conclusion
All fields required for Task 4 are available directly in the existing `accounts.csv` and `subscriptions.csv` tables. No additional data collection, external sources, or other RavenStack tables (`feature_usage`, `support_tickets`, `churn_events`) are needed for this specific task.

The only work needed is **deriving** new columns (`signup_month`, `anchor_date`, `anchor_month`, `start_month`, `period_number`) from the existing raw fields — not sourcing new data.
