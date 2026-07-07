#  04 - Revenue Cohort Analysis by Referral Channel

---

## WHAT

A method that groups customers into signup cohorts based on their `signup_month`, then analyzes revenue (MRR) retention period-over-period for each acquisition channel within every signup cohort, while identifying which acquisition channels generate the highest Average MRR and Total ARR.

### Objectives

1. For each acquisition channel and signup cohort, measure how revenue (MRR) retention evolves period-over-period after signup.

2. Identify which referral channels generate the highest Average MRR and Total ARR.

### Scope

1. Cohort construction using `signup_date` (account level), with the first subscription `start_date` used only as the revenue retention anchor for calculating period offsets.

2. Period-over-period Revenue Retention % per cohort.

3. Average MRR and Total ARR per referral channel, based on active subscriptions.

### Out of Scope / Non-goals

1. Customer/logo retention or churn rate  — not part of this revenue-based analysis.
2. Root-cause analysis of why revenue changes period-over-period.

---

## WHY

1. Reveals each acquisition channel's revenue retention and growth over the long term, not just at signup.
2. Helps understand customer revenue behavior per acquisition channel over time.
3. Guides pre-launch acquisition budget decisions toward the channels that generate the most durable revenue.

---

## HOW

### What's the plan? Tools?

- Convert `signup_date` and `start_date` columns to year-month format.

- Left join `accounts` to `subscriptions` on `account_id`:
  - Pandas: `accounts.merge(subscriptions, on='account_id', how='left')`
  - SQL: `accounts a LEFT JOIN subscriptions s ON a.account_id = s.account_id`

- Drop/exclude accounts with no subscriptions (NaN `start_date` after the left join) before computing the cohort anchor — these never converted to a paying subscription and shouldn't be counted in revenue cohorts.

- Each account belongs to a cohort based solely on its `signup_month`. Separately, determine the earliest (first) `start_date` among the account's subscriptions. This first subscription date serves only as the anchor for calculating revenue retention periods and does not define the cohort itself.

- Calculate `period_number` for each subscription (not each account) as: that subscription's start_month − the account's anchor start_month. This way, if an account has multiple subscriptions, each one's revenue lands in its correct period relative to the cohort anchor, instead of all being bucketed into period 0.

- Aggregate (sum) `mrr_amount` by `signup_month`, `referral_source`, and `period_number`, using all subscriptions (correctly distributed across periods per the previous step).

- Calculate revenue retention rate by dividing each period's aggregated `mrr_amount` by the period 0 `mrr_amount` for that same cohort. Label this clearly as **Revenue Retention %** (not customer/logo retention).

- Filter subscriptions to active-only using `subscriptions.churn_flag == False `
  
- Aggregate (sum) `mrr_amount` per `account_id `

-  Group by `referral_source` and take the mean of the account-level totals from pervious step to get the Average MRR per acquisition channel.


- Calculate Total ARR per acquisition channel by summing `arr_amount` grouped by `referral_source` directly (a straight sum isn't affected by how many subscriptions an account has, so no account-level pre-aggregation is needed here).

---

## INPUT

### Data Requirements

1. `ravenstack_accounts.csv`
2. `ravenstack_subscriptions.csv`

---

## OUTPUT

### Minimum Viable Product (MVP)

- Cohort table (signup_month × referral_source × period_number)
- Revenue Retention % per cohort per period
- Average MRR per acquisition channel & Total ARR per acquisition channel
- Recommended visualizations: heatmap for the retention matrix, line chart for MRR trend per referral channel

### Metrics

Success is measured by a cohort table that correctly attributes each subscription's revenue to its right `period_number` relative to the account's anchor date, a Revenue Retention % that is clearly distinguished from customer/logo retention, and channel-level MRR/ARR metrics that are consistently based on active subscriptions and correctly weighted at the account level.

---
