# 01 — Churn Prediction Using Subscriptions & Support Data

---

## WHAT

Build a model that predicts whether an active account will churn within the first 30 days of the public launch, based on its lifetime subscription history and support ticket behavior.

Active accounts can be split into 2 distinct groups:
- NEW sign ups less than 30 days old
- MATURE accounts at least 30 days old



### Objectives

1. **Main Objective**: Produce a predictive model to identiy high risk accounts that are likely to churn in the next 30 days.
2. **Secondary Objective**: Identify customer behaviours and account characteristics most strongly associated with churn  (e.g. support ticket experience, feature usage patterns)
3. **Business Operational Objective**: Create some kind of identifier that will allow the business to prioritize intervention for highest risk customers 


### Scope

- Training on accounts that are active up to the training cut off date
- Predicting churn in the following days for all accounts still active on that training cutoff date up until a test cut off date
- Risk Scoring 


### Out of Scope / Non-goals

*What is explicitly NOT included.*

1. Predicting churn for new sign ups less than 30 days old 
(This is a non goal because new sign ups have no pattern history and likely have different drivers for churn, thus requiring a different set of onboarding measures)


2. Retroactively predicting churn for accounts that have already churned before launch date

3. Predicting downgrades or loss of revenue


---

## WHY

*The goals — why this task matters.*

- By knowing the key drivers of churn, we can design **interventions** to counter drivers of churn (e.g., send offers, prioritize support) to combat these key drivers. 
- Through risk scoring, we can make **timely interventions** to **proactively retain at‑risk customers** before the public launch
- Overall, we aim to **reduce churn** and **improve launch metrics**.

---

## HOW

### What's the plan? Tools?

| Stage | Work to Be Done | Tools |
|-------|------------------|-------|
| **1. Load the data** | **✅ Completed:** Load the raw customer data into the analysis environment. | Neon, SQL, pandas |
| **2. Clean the data** | **✅ Completed:** Clean and prepare the dataset by handling missing values, correcting data types, removing duplicates, and resolving inconsistencies. | Neon, SQL, pandas, numpy |
| **3. Perform EDA** | **🛠️ Work In Progress:** Explore customer behaviour, churn distribution, feature relationships, and identify potential predictors. | Neon, SQL, pandas, matplotlib, seaborn |
| **4. Feature engineering** | Create meaningful features (e.g., customer activity, tenure, usage statistics) from the raw data. | SQL, pandas, numpy |
| **5. Build the modeling table** | Combine engineered features into a single modelling table where each row represents one customer and includes the target (churn label). | Neon, SQL, pandas |
| **6. Split the data** | Perform a time-based train/test split to avoid data leakage and simulate future predictions. | scikit-learn, pandas |
| **7. Pre-process data (feature columns X)** | Separate features (X) and target (y); separate numerical and categorical features; encode categorical variables; scale numerical variables (if required); prepare the target label. | Pipeline, ColumnTransformer, OneHotEncoder, StandardScaler |
| **8. Train the model(s)** | Train one or more binary classification models (e.g., Logistic Regression and/or XGBoost). | scikit-learn, XGBoost |
| **9. Evaluate model performance** | Assess model performance using the Confusion Matrix, Precision, Recall, F1-score, Accuracy, and ROC-AUC. | scikit-learn.metrics |
| **10. Interpret results** | Analyse feature importance, explain model predictions, and communicate findings using visualisations or dashboards. | matplotlib, seaborn, SHAP, dashboard (optional) |

---

## INPUT

### Data Requirements

*What data/files are needed.*

**Processed Data**
1. `accounts` table
2. `subscriptions` table
3. `feature_usage` table
4. `support_tickets` table
5. `churn_events` table

**Feature Columns in Modeling Table**
1. Time‑since‑signup aggregates (account age)
2. Speed & frequency of adoption (usage log like time since last login, total usage, usage rate)
3. Support response time trends (average response time, number of tickets)
4. Plan‑change history (how many subscription plans)
5. Churn label (binary)

**Training Set**
- Mature accounts still active on the training cut off date (cannot be less than 30 days from last record)
- Features created using data on or before the training cut off date to prevent data leakage
- Target/Label: churned or not within the 30 days following the cut off date (binary: 1=churned, 0=retained)

**Testing Set**
- Mature accounts still active on a later cutoff date
- Features created using data available on or before the test cutoff date to prevent leakage
- Target/Label: churned or not within the 30 day window leading up to the test cut off date (binary: 1=churned, 0=retained)
- Used for evaluating model performance

---

## OUTPUT

### Minimum Viable Product (MVP)

**CHURN PREDICTION MODEL:** 
1. Trained model (.pkl file)
2. Confusion Matrix: Shows the actual prediction results.
3. Precision: how many flagged customers actually churned? 
4. Recall, F1-score: Evaluate performance at chosen threshold (e.g., 0.5).
5. ROC-AUC: To compare models; evaluates the model’s overall ability to separate churners from non-churners.  

**DATA VIZ, REPORTS AND EXECUTIVE SUMMARY:**
- List of high‑risk accounts with risk scores and top risk factor
- Feature importance report (top drivers of churn for mature accounts)
- Stakeholder report (summary with key findings, recommendations, and visualizations)
- SHAP 


### Metrics

*How success will be measured.*

[Success criteria here]

---
