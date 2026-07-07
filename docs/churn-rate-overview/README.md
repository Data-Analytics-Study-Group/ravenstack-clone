# 06 - Monthly Churn Rate Analysis by Plan Tier

---

## WHAT

*One or two sentences describing exactly what this task delivers.*

Calculate the monthly churn rate broken down by subscription plan tier (e.g., Free, Starter, Pro) during the pilot period, in order to identify which tier shows the highest churn concentration.

### Objectives

1. Determine whether the majority of churn is originating from one specific plan.
2. Give the business a data-backed basis to focus retention efforts precisely where they're needed before the official launch, rather than treating all customers the same.

### Scope

*What is included in this task.*

1. Active subscriptions and cancellation events for the pilot window, grouped by month and plan tier.
2. Monthly churn rate calculation per tier, with cross-tier comparison to pinpoint the highest concentration of churn.

### Out of Scope / Non-goals

*What is explicitly NOT included.*

1. Customer lifetime value, cohort retention, or churn analysis beyond the pilot window.
2. Root-cause analysis of individual cancellation reasons.

---

## WHY

*The goals — why this task matters.*

1. To determine if the majority of churn is originating from one specific plan.
2. To allow the business to focus retention efforts precisely where they are needed before the official launch, rather than treating all customers the same.
3. To directly inform and impact pricing and plan design decisions at launch.

---

## HOW

### What's the plan? Tools?

*Step-by-step of what needs to be done.*

- Filter the dataset to include only the pilot window.
- Group the active subscriptions by month and by plan tier.
- Group the cancellation events by month and by plan tier.
- Calculate the monthly churn rate for each tier using the formula: `(churned / total active that month) * 100`.
- Compare the resulting rates across all tiers to pinpoint the highest concentration of churn.

---

## INPUT

### Data Requirements

*What data/files are needed.*

1. `ravenstack_subscriptions.csv`
2. `churn_events.csv`

---

## OUTPUT

### Minimum Viable Product (MVP)

*The simplest version that adds value.*

- **Monthly Churn Table** — a detailed breakdown of active accounts, churned accounts, and the churn rate percentage per month for each plan tier.
- **Tier Churn Trend Chart** — a line chart visualizing the monthly churn rate over the pilot period, with separate lines for each plan tier.
- **Highest Churn Concentration Report** — a summary identifying the worst-performing tier with actionable recommendations for pricing, plan design, or targeted retention efforts.

### Metrics

*How success will be measured.*

Success is measured by a validated monthly churn table that reconciles against total active account counts, a trend chart that clearly shows relative churn levels across tiers over the pilot period, and a concentration report that names the highest-churn tier with recommendations the business can act on before launch.

---
