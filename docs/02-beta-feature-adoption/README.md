# 02 - Feature Adoption Tracking During Beta Phases

---

## WHAT

Analyse adoption patterns of beta-flagged features (`is_beta_feature = TRUE`) across accounts, and correlate adoption signals with churn risk from Task #1.

### Objectives

1. Determine which product features show the highest and lowest adoption rates across the beta phase (SMART Q6) — measured at the account level via frequency, adoption flag, time-to-first-use, and stickiness.
2. Test whether low feature adoption predicts eventual churn (SMART Q6), scoped to the beta period, and flag zero-adoption, high-churn-risk accounts for pre-launch outreach.

### Scope

*What is included in this task.*

1. All accounts and beta-flagged features present in `ravenstack_feature_usage.csv`, including adoption metrics (frequency, adoption flag, time-to-first-use, usage count, duration, error count, feature breadth, and stickiness ratio).
2. Statistical comparison of churned vs. retained accounts (Mann-Whitney U test, logistic regression), segmented by `plan_tier` and `industry`, cross-referenced with churn risk scores from Task #1.

### Out of Scope / Non-goals

*What is explicitly NOT included.*

1. Non-beta (generally available) feature usage analysis.
2. Building or retraining the churn prediction model itself — that model is consumed as an input from Task #1, not reproduced here.

---

## WHY

*The goals — why this task matters.*

1. To surface which beta features are driving engagement versus being ignored — and flag zero-adoption accounts before public launch.
2. To quantify how much feature adoption signals (breadth, frequency, duration) contribute to churn risk, informing both product and retention strategy.

---

## HOW

### What's the plan? Tools?

*Step-by-step of what needs to be done.*

- Filter `ravenstack_feature_usage.csv` to `is_beta_feature = TRUE`, join via `subscription_id` → `account_id`.
- Compute per-account adoption metrics:
  - **Frequency** — sum `usage_count`, grouped by `account_id` / `feature_name`.
  - **Adoption flag** — binary (0/1): `1` if the account has ≥1 usage record for a feature (`usage_count > 0`), `0` if it never appears in the usage log. Zero-adoption accounts require a cross-join of the full account list against all beta features, left-joined to usage data, with missing values filled as `0`.
  - **Time-to-first-use** (`usage_date − start_date`), total `usage_count`, avg `usage_duration_secs`, avg `error_count`, and feature breadth (distinct `feature_name` count).
  - **Stickiness** — Week 1 usage = within 7 days of `start_date`; Week 2+ usage = after day 7; stickiness ratio = Week 2+ usage / Week 1 usage.
- Rank features by adoption rate — surface top 5 and bottom 5 beta features.
- Build a composite feature score: normalised adoption rate × stickiness × inverse churn-risk correlation (Spearman), ranked into a feature league table.
- Compare adoption between churned vs. retained accounts — avg feature breadth, usage count, and session duration by `churn_flag`.
- Run a Mann-Whitney U test on feature breadth (churned vs. retained) to statistically validate whether low adoption predicts churn.
- Run logistic regression (breadth + frequency + duration → churn label) to quantify each signal's contribution.
- Segment all metrics by `plan_tier` and `industry`.
- Flag zero-adoption accounts with high churn risk scores from Task #1.

---

## INPUT

### Data Requirements

*What data/files are needed.*

1. `ravenstack_feature_usage.csv` *(filter: `is_beta_feature = TRUE`)*
2. `ravenstack_subscriptions.csv`
3. `ravenstack_accounts.csv`
4. `ravenstack_churn_events.csv`
5. `churn_risk_scores.csv` *(derived — output of Task #1)*

---

## OUTPUT

### Minimum Viable Product (MVP)

*The simplest version that adds value.*

- Top & bottom 5 feature adoption chart — bar chart of highest and lowest adopted beta features.
- Feature league table — ranked composite score: adoption × stickiness × churn-risk correlation.
- Churned vs. retained comparison table — avg breadth, usage count, duration by `churn_flag`.
- Mann-Whitney U result — statistical test: does low adoption significantly predict churn?
- Logistic regression report — coefficient table showing which adoption signals matter most.
- `plan_tier` × `industry` adoption heatmap — segment-level adoption gaps.
- Zero-adoption high-risk account list — priority outreach targets for customer success.
- Stakeholder report — key findings, feature recommendations, and pre-launch action plan.

### Metrics

*How success will be measured.*

- Mann-Whitney U test on feature breadth (churned vs. retained) returns a statistically significant result (p < 0.05).
- Logistic regression coefficients for breadth, frequency, and duration are non-trivial and interpretable in direction and magnitude.
- 100% of zero-adoption accounts are cross-referenced against Task #1 churn risk scores and delivered as a prioritized outreach list.

---
