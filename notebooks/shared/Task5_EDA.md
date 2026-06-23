# Task 5: Plan Tier Upgrade Funnel by Industry — Required Data

## Purpose
This document lists the data fields required to execute Task 5 (Plan Tier Upgrade Funnel by Industry) and confirms whether each field is available in the RavenStack dataset.

## Required Fields

### From `accounts.csv`
| Field | Purpose in Task 5 | Available? |
|---|---|---|
| `account_id` | Primary key, used to join with `subscriptions` | Yes |
| `industry` | Used to group the funnel and conversion rates by industry | Yes |
| `plan_tier` | Used to identify accounts that started on the Basic tier (funnel base population) | Yes |

### From `subscriptions.csv`
| Field | Purpose in Task 5 | Available? |
|---|---|---|
| `subscription_id` | Unique identifier for each subscription row | Yes |
| `account_id` | Foreign key, used to join with `accounts` | Yes |
| `upgrade_flag` | Used to filter accounts that genuinely upgraded mid-cycle | Yes |
| `plan_tier` | Used to identify which tier an upgraded account moved to (Pro or Enterprise) | Yes |

## Derived Fields (calculated during the task, not in raw data)
| Field | How it's derived |
|---|---|
| `basic_starters` | Accounts where `accounts.plan_tier == 'Basic'`, grouped by `industry` |
| `upgraded_to_pro` | Accounts where `upgrade_flag == True` and `subscriptions.plan_tier == 'Pro'`, grouped by `industry` |
| `upgraded_to_enterprise` | Accounts where `upgrade_flag == True` and `subscriptions.plan_tier == 'Enterprise'`, grouped by `industry` |
| `conversion_rate_pro` | `upgraded_to_pro` ÷ `basic_starters`, per industry |
| `conversion_rate_enterprise` | `upgraded_to_enterprise` ÷ `basic_starters`, per industry |

## Data Availability Conclusion
All fields required for Task 5 are available directly in the existing `accounts.csv` and `subscriptions.csv` tables. No additional data collection, external sources, or other RavenStack tables (`feature_usage`, `support_tickets`, `churn_events`) are needed for this specific task.

The only work needed is **deriving** new fields (`basic_starters`, `upgraded_to_pro`, `upgraded_to_enterprise`, conversion rates) from the existing raw columns — not sourcing new data.