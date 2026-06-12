Hello all! I want to thank everyone who has contributed to our project. We appreciate all your efforts. 

## Getting Started

1. Clone git repo
```bash
git clone <https://github.com/Data-Analytics-Study-Group/ravenstack-pl.git>
cd ravenstack-pl
```
2. Create a new branch for your work: `git checkout -b <type>/<short-description>`


## Branch Naming Convention

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

### Commit Branch

When you have finished your tasks commit your branch using the commands below:

1. Ensure your branch is up to date with `main` by running: `git pull main`

2. Check what files are staged: `git status`

3. Stage all modified files `git add .` or stage specific files: `git add <file_name>`                

4. Commit your changes: `git commit -m "docs: create contribute markdown"`

5. Push branch to GitHub: `git push origin <type>/<short-description>`

### Make a Pull Request (PR)

Once you have pushed branch, go to the repository on GitHub. Then:

1. Open PR by clicking ###Compare & Pull Request### in the yellow banner

2. In the PR template, write what changes were made and why in the Summary section.

3. Click the right label

4. Place a snapshot (if necessary)

### Review PR

- Every PR must be reviewed by at least one team member

- The reviewer must check that code is clean and safe to merger in `main`

- If any issues or concerns are found in code leave a comment, the author will mmake updates and re-request PR review

### Approved PR

- Once approved merge branch into `main`

- Delete branch after merge


