# Data Quality Report

## Purpose

This document records data quality issues identified during project setup and validation activities.

Findings should be reviewed before analysis, reporting, or model development.

---

## Summary

| Table | Field | Issue | Status |
|---------|---------|---------|---------|
| feature_usage | usage_id | Duplicate values found in a field expected to be unique | Open |

---

## Findings

### Finding 1: Duplicate usage_id Values

**Table:** feature_usage

**Field:** usage_id

**Issue:** Duplicate values were identified in the usage_id field of the feature_usage table.

According to the dataset documentation, usage_id is defined as a primary key and should therefore contain unique values. Validation checks identified multiple records sharing the same usage_id, indicating a discrepancy between the documented schema and the actual data.

**Validation Method**

Duplicate `usage_id` values were identified using a data validation query executed against the Neon database. Refer to the associated GitHub issue for the validation query and supporting evidence.


**Impact:**

- Usage_id is not functioning as a unique event identifier.
- May impact feature engineering, event aggregation, and usage metrics.
- Indicates a mismatch between the documented schema and the supplied dataset.

**Investigation Notes:**

- Composite primary key constraints were verified; however, it could not be determined whether duplicate usage_id values were intentional or the result of a data quality issue.
- No foreign key constraint exists on usage_id.
- A uniqueness test on the proposed composite key (subscription_id, feature_name, usage_date) identified duplicate composite key values.
- Investigation of the duplicate composite key records suggested that a single logical usage event may have been erroneously split across multiple rows.

**Resolution:**
- Exclude usage_id column from downstream analysis
-  Aggregate records sharing the same logical event into a single row based on business rules.
- Adopt a composite key consisting of `subscription_id`, `feature_name`, and `usage_date`
- Update the data dictionary and project documentation to reflect the revised key structure.


**Status:**

Open. Pending team review and approval of the proposed resolution.

---

## Revision History

| Date | Author | Change |
|--------|--------|--------|
| 2026-06-12 | Audrey | Initial draft |