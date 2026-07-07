# 03 - Support Workload Forecasting

---

## WHAT

Forecast weekly support ticket volume for the 4 weeks post-launch, segmented by plan tier (Basic, Pro, Enterprise), using historical ticket patterns from the pilot period.

### Objectives

1. Accurately forecast weekly support ticket volumes for the 4 weeks post-launch, segmented by Basic, Pro, and Enterprise plan tiers.
2. Provide a data-backed staffing recommendation by calculating the buffer (upper bound vs. point estimate) to ensure the support team is adequately resourced for launch demand.

### Scope

*What is included in this task.*

1. **Data Preparation**: Joining `support_tickets` and `subscriptions` data to map historical tickets to their respective plan tiers, ensuring we accurately capture the plan tier active at the time of each ticket.
2. **Exploratory Data Analysis (EDA)**: Evaluating historical trends per tier to select the most appropriate, lightweight forecasting method (see point 3 below)
3. **Time-Series Modeling**: Aggregating historical ticket volumes by week and applying either a Rolling Average or Holt's Linear Method based on the EDA findings.
4. **Forecasting & Reporting**: Generating 4-week forward forecasts with 90% confidence bounds, calculating buffer values, and exporting a staffing summary table for operations.

### Out of Scope / Non-goals

*What is explicitly NOT included.*

1. Forecasting ticket volumes by specific issue categories, priority levels, or resolution times.
2. Calculating the exact number of support agents required; this task focuses on ticket volume and buffer, not headcount.
3. Modeling the impact of specific launch marketing campaigns or external factors beyond historical pilot trends.

---

## WHY

Different plan tiers generate very different support volumes and expectations. Forecasting volume per tier gives the support team a data-backed headcount plan — staffing to the upper confidence bound prevents being caught short at launch.

---

## HOW

### What's the plan? Tools?

*Step-by-step of what needs to be done.*

| Stage | Work To Be Done | Tools |
|------|-------|-------|
| **1. Data Engineering - Part 1** | Join `support_tickets.csv` to `ravenstack_subscriptions.csv` on `account_id`. Filter the join for active `plan_tier` at the time of the ticket submission | Neon, SQL, Jupyter Notebook, Pandas |
| **2. Data Engineerin - Part 2** | Aggregate ticket counts by week and plan tier (`submitted_at` floored to week start date). | Neon, SQL, Jupyter Notebook, Pandas |
| **3. EDA & Method Selection** | Before forecasting, evaluate the historical trend for each plan tier to select the most appropriate modeling approach:<br>• ***Data Viz & Trend Check***: Plot weekly ticket volumes per tier and calculate the average Week-over-Week (WoW) growth rate.<br>• ***Decision Rule***: If the data is relatively flat/stationary (WoW growth ~0%), proceed with **Rolling Average** method. If there is a clear, consistent upward or downward trend (WoW growth > 5%), proceed with **Holt's Linear** method. | Jupyter Notebook, pandas, matplotlib/seaborn |
| **4. Model Evaluation (Backtesting)** | Before finalizing the forecast, validate the chosen method's accuracy:<br> *Temporal Split*: Hold out the last 2 weeks of the pilot data as a "test set".<br>• *Blind Forecast*: Train the model on the remaining weeks and predict the held-out 2 weeks.<br>• ***Calculate Error***: Compute the Mean Absolute Percentage Error (MAPE) to ensure accuracy is acceptable (target < 15-20%). | Jupyter Notebook, numpy or scikit-learn (for mean_absolute_percentage_error) |
| **5. Forecasting (4 Weeks)** | Generate 4-week forward forecasts based on the selected method:<br>• *Option 1 Rolling Average*: Calculate the point estimate using the average ticket volume of the last 4 weeks of the pilot.<br>• *Option 2 Holt’s Linear*: Fit a Holt's model to capture both the baseline level and the growth trend, projecting that calculated growth trend forward to future periods. | **Option 1 Rolling Average**: pandas, numpy<br>• **Option 2 Holt's Linear**: statsmodel (statsmodels.tsa.holtwinters) |
| **6. Buffer Calculation** | Calculate the 90% confidence bound staffing buffer for each tier/week to ensure we are prepared for launch:<br>• **For Rolling Average**: `Buffer = 1.28 * Standard Deviation of the historical weekly volumes`.<br>•  **For Holt's Linear**: `Buffer = 1.28 * Standard Deviation of the model's historical errors (residuals)`.<br>• *Upper Bound* = `Point Estimate + Buffer`. | Numpy, Pandas (for standard deviation and arithmetic calculations) |
| **7. Stakeholder Report** | Combine into a staffing summary table — predicted volume, upper-bound volume, and explicit buffer per week per tier, plus weekly totals. | Jupyter Notebook, pandas, matplotlib/seaborn, excel/pdf |
---

## INPUT

### Data Requirements

*What data/files are needed.*

1. `support_tickets` table
2. `subscriptions` table

---

## OUTPUT

### Minimum Viable Product (MVP)

*The simplest version that adds value.*

- **Weekly forecast chart**: Historical + 4-week forecast line with 90% confidence band, one panel per plan tier.
- **Staffing summary table**: Predicted, upper-bound, and buffer ticket volume per tier per week, with weekly totals.
- **`ticket_forecast_4weeks.csv`**: Exportable forecast for ops and support team planning.
- **Stakeholder callout**: Flag if historical trend is growing week-over-week (launch surge signal) and recommend staffing to upper bound (90th percentile), not point estimate.
  - *Buffer calculation*: Explicitly show the difference (`upper_bound - predicted`) to quantify the buffer.
  - *Rationale*: The point estimate says "this is what will probably happen." The 90th percentile says "this is what you need to be ready for." Being ready for something is more important that simply estimating what will probably happen.

### Metrics

*How success will be measured.*

1. **Model Appropriateness**: The EDA step successfully identifies the underlying data patterns (stationary vs. trending) for each tier, ensuring the chosen forecasting method aligns with the data.
2. **Operational Utility**: The support and ops teams successfully receive and utilise the forecast CSV and summary table for launch scheduling.
3. **Forecast Coverage**: (Measured post-launch) Actual ticket volumes fall within the 90% confidence interval (upper bound) of the forecast.
