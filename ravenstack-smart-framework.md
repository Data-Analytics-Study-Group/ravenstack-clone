# Ravenstack Customer 360 : SMART Framework

## Q1: Churn Prediction
**Question:** Can we predict which active accounts will churn within the next 30 days by analyzing their lifetime subscription history and support ticket behavior? 

**Why it matters:** Identifying at-risk customers enables proactive retention efforts (e.g., sending offers or prioritizing support) before the public launch, aiming to reduce overall churn.

| Specific | Measurable | Achievable | Relevant | Time-bound |
| :--- | :--- | :--- | :--- | :--- |
| Predict active account churn using lifetime subscription and support data. | Evaluate model performance using accuracy scores and a confusion matrix. | Labeled historical churn and support data are available to train a binary classifier (Logistic Regression/XGBoost). | Enables proactive retention and targets high-risk accounts prior to launch. | Predicts churn occurring within a **30-day** forward-looking window. |

**Data Inputs:** `subscriptions.csv`, `support_tickets.csv`, `churn_events.csv`

---

## Q2: Feature Adoption & Churn
**Question:** What are the adoption patterns of beta features across accounts, and does low feature adoption statistically correlate with an increased risk of churn? 

**Why it matters:** Surfaces which beta features are driving engagement versus being ignored, allowing the team to flag zero-adoption accounts for targeted outreach before public launch.

| Specific | Measurable | Achievable | Relevant | Time-bound |
| :--- | :--- | :--- | :--- | :--- |
| Analyze beta feature adoption metrics (frequency, stickiness, breadth) and correlate with churn risk. | Quantify adoption rates and validate churn correlation using a Mann-Whitney U test and logistic regression. | Feature usage logs and churn risk scores (from Q1) are available and joinable. | Shapes product recommendations and flags zero-adoption high-risk accounts. | Focused specifically on the usage window during the **beta phase**. |

**Data Inputs:** `ravenstack_feature_usage.csv`, `ravenstack_subscriptions.csv`, `ravenstack_accounts.csv`, `ravenstack_churn_events.csv`, `churn_risk_scores.csv`

---

## Q3: Support Workload Forecasting
**Question:** Can we forecast weekly support ticket volume for the 4 weeks post-launch, segmented by plan tier, to establish a data-backed headcount plan? 

**Why it matters:** Different plan tiers generate varying support volumes. Forecasting with upper confidence bounds prevents the support team from being understaffed during a launch surge.

| Specific | Measurable | Achievable | Relevant | Time-bound |
| :--- | :--- | :--- | :--- | :--- |
| Forecast weekly support ticket volume segmented by plan tier (Basic, Pro, Enterprise). | Produce predicted volumes and a 90% confidence interval to calculate staffing upper bounds. | Historical weekly ticket series from the pilot period are available to train a Prophet model. | Ensures operational readiness and adequate support headcount for the launch. | Forecast spans exactly **4 weeks** post-launch. |

**Data Inputs:** `ravenstack_support_tickets.csv`, `ravenstack_subscriptions.csv`

---

## Q4: Revenue Cohort Analysis by Channel
**Question:** How much revenue does each acquisition channel generate over time when grouping customers by their signup month and referral source? 

**Why it matters:** Reveals long-term retention and revenue behaviors, guiding pre-launch acquisition budget decisions toward the most profitable channels.

| Specific | Measurable | Achievable | Relevant | Time-bound |
| :--- | :--- | :--- | :--- | :--- |
| Group customers by signup month and referral source to track revenue generation over time. | Calculate Revenue Retention percentage, Average MRR, and Total ARR per channel. | Sign-up dates, referral sources, and MRR amounts are joinable between accounts and subscriptions. | Directs the marketing budget toward channels with the highest long-term revenue. | Tracks revenue across sequential **monthly periods** relative to a cohort's anchor date. |

**Data Inputs:** `ravenstack_accounts.csv`, `ravenstack_subscriptions.csv`

---

## Q5: Plan Tier Upgrade Funnel by Industry
**Question:** What is the conversion rate of accounts upgrading from the Basic tier to higher tiers (Pro, Enterprise), and how does this vary by industry segment? 

**Why it matters:** Highlights which industries have the highest demand for premium plans, informing targeted upselling and sales strategies.

| Specific | Measurable | Achievable | Relevant | Time-bound |
| :--- | :--- | :--- | :--- | :--- |
| Identify accounts starting on the Basic tier and track upgrades to Pro and Enterprise, segmented by industry. | Count total upgrades and calculate the exact upgrade conversion rate per plan per industry. | Account industry segments and subscription plan upgrade flags are available. | Informs targeted sales pipelines and highlights the most upgrade-prone industries. | Analyzes the total upgrade conversion history of the pilot population. |

**Data Inputs:** `ravenstack_accounts.csv`, `ravenstack_subscriptions.csv`

---

## Q6: Monthly Churn Rate Analysis by Plan Tier
**Question:** What is the monthly churn rate per subscription plan tier during the pilot period, and which tier shows the highest concentration of churn? 

**Why it matters:** Allows the business to focus retention efforts and adjust pricing or plan designs precisely where they are needed before the official launch.

| Specific | Measurable | Achievable | Relevant | Time-bound |
| :--- | :--- | :--- | :--- | :--- |
| Calculate the monthly churn rate broken down exclusively by subscription plan tier. | Churn rate = (churned / total active that month) × **100**. | Active subscription statuses and cancellation events are available. | Directly impacts pricing structures and plan design decisions prior to launch. | Limited strictly to the **pilot window** timeframe. |

**Data Inputs:** `ravenstack_subscriptions.csv`, `churn_events.csv`


# Ravenstack Customer 360: Task to SMART Question Mapping

This table outlines which proposed task from the team's brainstorming sessions matches the formalized SMART framework questions.

| Team Task | SMART Framework Question | Shared Objective |
| :--- | :--- | :--- |
| **Task 1: Churn prediction using subscriptions + support data** | **Q1: Churn Prediction** | Both aim to predict whether an active account will churn within a 30-day window based on lifetime subscription history and support ticket behavior. |
| **Task 2: Feature adoption tracking during beta phases** | **Q2: Feature Adoption & Churn** | Both focus on analyzing the adoption patterns of beta features to determine if low adoption statistically correlates with a higher risk of churn. |
| **Task 3: Support workload forecasting** | **Q3: Support Workload Forecasting** | Both involve forecasting weekly support ticket volumes for the 4 weeks post-launch, segmented by plan tier, to help establish operational readiness and headcount planning. |
| **Task 4: Revenue cohort analysis by referral channel** | **Q4: Revenue Cohort Analysis by Channel** | Both track long-term revenue generation by grouping customers according to their signup month and referral source to calculate metrics like Average MRR and Total ARR. |
| **Task 5: Plan tier upgrade funnel by industry** | **Q5: Plan Tier Upgrade Funnel by Industry** | Both seek to calculate the conversion rate of accounts upgrading from the Basic tier to higher tiers (Pro, Enterprise) and segment this data by industry. |
| **Task 6: Monthly Churn Rate Analysis by Plan Tier** | **Q6: Monthly Churn Rate Analysis by Plan Tier** | Both require calculating the monthly churn rate during the pilot period, exclusively broken down by subscription plan tier, to identify where churn is most concentrated. |

---

### Key Alignments & Data Inputs

The mapping above shows a 1:1 alignment between the team's brainstormed tasks and the final SMART questions. Here is a breakdown of the specific shared data inputs required to execute each aligned pairing:

* **Task 1 / Q1:** Relies on `subscriptions.csv`, `support_tickets.csv`, and `churn_events.csv`. 
* **Task 2 / Q2:** Requires `ravenstack_feature_usage.csv` (filtered by beta features), `ravenstack_subscriptions.csv`, `ravenstack_accounts.csv`, `ravenstack_churn_events.csv`, and derived `churn_risk_scores.csv`. 
* **Task 3 / Q3:** Combines `ravenstack_support_tickets.csv` with `ravenstack_subscriptions.csv`.
* **Task 4 / Q4:** Joins `ravenstack_accounts.csv` and `ravenstack_subscriptions.csv`.
* **Task 5 / Q5:** Utilizes `ravenstack_accounts.csv` and `ravenstack_subscriptions.csv`.
* **Task 6 / Q6:** Needs `ravenstack_subscriptions.csv` and `churn_events.csv`.