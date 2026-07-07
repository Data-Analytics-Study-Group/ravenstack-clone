# 5 — Plan Tier Upgrade Funnel by Industry

---

## WHAT

A method that analyzes the plan tier upgrade funnel by industry, showing the number of accounts that upgrade from the Basic tier to higher tiers and the conversion rate for each upgrade path.

### Objectives

1. Identify which industries have the highest upgrade rates from the Basic plan.
2. Measure the effectiveness of the upgrade funnel across different industries.

### Scope

1. Accounts that started on the Basic tier (`accounts.plan_tier = 'Basic'`), tracked for upgrades to Pro or Enterprise.
2. Conversion rate calculation per upgrade path (Basic → Pro, Basic → Enterprise), broken down by industry.

### Out of Scope / Non-goals

1. Downgrade analysis (kept as a separate task to avoid mixing upgrade and downgrade directional metrics).
2. Accounts that did not start on the Basic tier (e.g., accounts starting directly on Pro or Enterprise).

---

## WHY

1. Identify which industries have the highest upgrade rates from the Basic plan.
2. Measure the effectiveness of the upgrade funnel across different industries.
3. Help prioritize sales and marketing efforts toward industries with the greatest upgrade potential.
4. Support product and pricing decisions by understanding upgrade behavior across industries.

---

## HOW

### What's the plan? Tools?

- Join `subscriptions` and `accounts` on `account_id`.
- Identify all accounts that started on the Basic plan (`accounts.plan_tier = 'Basic'`). This is the funnel base population — the denominator for all conversion rates in this task.
- Use `upgrade_flag` (or upgrade information) in `subscriptions` to identify which Basic accounts upgraded.
- Count Basic → Pro upgrades by industry.
- Count Basic → Enterprise upgrades by industry.
- Combine the results into a single table.
- Calculate the conversion rate for each upgrade path within each industry:
  - Basic → Pro = Upgraded to Pro / Total Basic accounts
  - Basic → Enterprise = Upgraded to Enterprise / Total Basic accounts

---

## INPUT

### Data Requirements

1. `ravenstack_accounts.csv`
2. `ravenstack_subscriptions.csv`

---

## OUTPUT

### Minimum Viable Product (MVP)

- Funnel table by industry
- Count of accounts that upgraded to each plan tier (Pro, Enterprise)
- Conversion rate per upgrade path, per industry

### Metrics

Success is measured by a funnel table where the denominator for every conversion rate is consistently the count of accounts that started on the Basic tier per industry (not all accounts, and not accounts already filtered by `upgrade_flag`), with upgrade paths (Basic → Pro, Basic → Enterprise) reported separately per industry.

---
