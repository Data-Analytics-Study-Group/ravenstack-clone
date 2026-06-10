Hello all! I want to thank everyone who has contributed to our project. We appreciate all your efforts. 

## Branching

During our time working on this project we will either be assigned or take on different tasks. It is crucial that we do so on a different branch. We are following GitHub workflow meaning all branches are merged into `main`. This is to avoid unnecessary changes `main`. After cloning the repo on your local device, be sure to update your cloned repo by using commands in step one below. Once `main` is up to date, create a new branch where you will work on your assigned task(s). Be sure to review branch naming conventions before creating a new branch. Each task should have its own branch, avoid making a large amount of changes on a single branch as it can complicate the review process.

```bash
# Step 1 — Make sure your local main is up to date before branching
git checkout main
git pull origin main

# Step 2 — Create your new branch and switch to it
git checkout -b <type>/<short-description>

# Example
git checkout -b explore/customer-churn-patterns
```

## Branch Naming Convention

All branches must follow this format:
```
<type>/<short-description>
```

### Types

| Prefix | Purpose |
|--------|---------|
| `data/` | Data cleaning or pipeline changes |
| `explore/` | EDA or one-off investigations |
| `pipeline/` | ETL/ELT workflows and orchestration (Airflow, dbt, etc.) |
| `fix/` | Fixing a bug in code, a broken pipeline, or bad logic |
| `docs/` | READMEs, data dictionaries, methodology writeups |
| `eval/` | Model evaluation, metrics, and validation work |
| `viz/` | Dashboards, charts, and reporting visuals |

### Rules for the Description

- **2–5 words max** — keep it concise
- **Use imperative form** — `normalize-sales-schema` not `normalized-sales-schema`
- **Use lowercase with hyphens** — `fix-null-join-logic` not `Fix_Null_Join_Logic`
- **Be precise** — anyone reading the branch name should know what it adds to the project
- **Avoid vague names** — `fix/updates` or `data/changes` tell nobody anything

### Examples

| ✅ Good | ❌ Bad |
|--------|--------|
| `data/normalize-sales-schema` | `data/changes` |
| `explore/customer-churn-patterns` | `explore/analysis` |
| `pipeline/daily-revenue-aggregation` | `pipeline/new-pipeline` |
| `fix/null-handling-join-step` | `fix/bug` |
| `viz/executive-kpi-dashboard` | `viz/dashboard2` |

## Commit and PR

When you have finished your tasks commit your branch using the commands below:

```bash
# Step 1 — See what has changed
git status

# Step 2 — Stage your changes
git add .                  # stages all modified or new files

git add <file_name>        # or stage a specific file, e.g. git add docs/contribute.md

# Step 3 — Commit your changes
git commit -m "docs: create contribute markdown"

# Step 4 — Push branch to GitHub
git push origin <type>/<short-description>
# e.g. git push origin docs/create-contribute-markdown
```
Once pushed, go to the repository on GitHub. You will see a prompt that says **Compare & Pull Request** - click it, fill out PR template and submit for review. Every PR requires one other team member to review and approve the changes before merging with the `main`.


